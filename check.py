#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""项目规范检查（仓库唯一入口）。

用法（脚本可从任意目录运行）：
    python check.py                      # 全库检查（无论当前目录在哪）
    python check.py path/to/note.md ...  # 只检查指定文件 / 目录（相对路径以当前工作目录为基准，绝对路径亦可）

路径统一：所有参数先经 check_notes.normalize() 归一化为仓库相对 posix 路径，
之后的豁免判断、报错定位、链接解析全部只使用归一化路径。越出仓库根的参数报错。

两部分：
1. 文件名规范（**仅 warning，不影响退出码**）：kebab-case 倾向（非 ASCII / 空格 /
   大写字母 / 下划线）、daily note 日期命名（严格 YYYY-MM-DD）、扩展名大小写；
   非 kebab 例外名单见仓库根的 .checkallow；被 git 忽略的本地文件自动跳过
   （git 不可用时退化为不过滤）。
2. 链接与格式（**error 影响退出码**）：scripts/check_notes.py 的 run()。

退出码：0 = 通过（可含 warning）；1 = 存在链接 / 格式 error；
        2 = 用法问题（路径不存在 / 越出仓库 / 显式传入非 .md 文件 / 未检查到任何 .md）。
"""
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, 'reconfigure'):
        _stream.reconfigure(encoding='utf-8')

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'scripts'))
import check_notes  # noqa: E402  （链接 / 格式规则与路径归一化的单一事实源）

ALLOWLIST_FILE = HERE / '.checkallow'
READMES = ('README.md', 'AGENTS.md')


def load_allowlist():
    """读取 .checkallow：每行一个仓库相对路径，# 开头为注释，路径同样经 normalize()。

    坏条目（越出仓库 / 不存在）跳过并提示，不让整个检查崩溃。
    """
    allowed = set()
    if not ALLOWLIST_FILE.is_file():
        return allowed
    for raw in ALLOWLIST_FILE.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        try:
            rel = check_notes.normalize(line, cwd=HERE, root=HERE)
        except ValueError:
            print(f'⚠️ .checkallow 条目越出仓库，已忽略：{line}')
            continue
        if not (HERE / rel).exists():
            print(f'⚠️ .checkallow 条目不存在，已忽略：{line}')
            continue
        allowed.add(rel)
    return allowed


def valid_date(stem):
    try:
        datetime.strptime(stem, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def filename_warnings(rel_files, allowed):
    warns = []
    for pos in sorted(rel_files):
        name = pos.rsplit('/', 1)[-1]
        if name in READMES or pos in allowed:
            continue

        is_md = name.endswith('.md')
        if not is_md and name.lower().endswith('.md'):
            warns.append(f'{pos}:1: 扩展名大小写应为 .md（该文件不在链接检查范围内）')

        # 非 ASCII / 空格对所有文件（含 PDF 等附件）都提示；kebab 与大小写规则只适用于 .md
        stem = name[:-3] if is_md else name
        issues = []
        if any(ord(c) > 127 for c in stem):
            issues.append('非 ASCII 字符（约定英文文件名）')
        if ' ' in stem:
            issues.append('空格')
        if is_md and re.search(r'[A-Z_]', stem):
            issues.append('大写字母 / 下划线')
        if issues:
            warns.append(f"{pos}:1: 文件名风格：{'、'.join(issues)}（建议 kebab-case）")

        if not is_md:
            continue
        parent = pos.rsplit('/', 1)[0] if '/' in pos else '.'
        if parent == 'journal/daily':
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', stem) or not valid_date(stem):
                warns.append(f'{pos}:1: daily note 文件名应为合法日期 YYYY-MM-DD')
    return warns


def git_ignored(rel_files):
    """返回被 git 忽略的路径集合（-z 传参避免 CJK / 空格路径被引号转义）。

    git 不可用 / 超时 / 非仓库时返回空集（不过滤，行为退化为原样检查）。
    """
    if not rel_files:
        return set()
    try:
        r = subprocess.run(
            ['git', 'check-ignore', '--stdin', '-z'],
            input=b'\0'.join(p.encode('utf-8') for p in rel_files),
            capture_output=True, cwd=HERE, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return set()
    if r.returncode not in (0, 1):  # 0=有忽略项，1=无，128 等=出错
        return set()
    return {p for p in r.stdout.decode('utf-8', errors='replace').split('\0') if p}


def main():
    args = sys.argv[1:]

    if not args:
        targets = ['.']  # 无参数 = 全库（相对仓库根，与当前目录无关）
    else:
        # 1. 归一化全部参数（越界 / 不存在 → 退出码 2）
        targets = []
        for a in args:
            try:
                rel = check_notes.normalize(a)
            except ValueError:
                print(f'❌ 路径位于仓库之外：{a}')
                sys.exit(2)
            if not (HERE / rel).exists():
                print(f'❌ 传入的路径不存在：{a}')
                sys.exit(2)
            targets.append(rel)

        # 显式传入的文件必须是 .md（非 .md 不做链接检查，避免“0 文件却显示通过”）
        for a, rel in zip(args, targets):
            if (HERE / rel).is_file() and not rel.endswith('.md'):
                print(f'❌ 显式传入的文件不是 Markdown，无法检查：{a}')
                sys.exit(2)

    # 2. 展开为仓库相对文件列表（只遍历一次，链接检查复用同一列表）
    # 文件名检查覆盖 attachments/（附件名同样约定英文 kebab-case）；链接检查随后会自动跳过非 .md。
    # git 忽略的本地文件（教材 PDF 等）不参与检查——它们不进仓库，命名不构成规范问题。
    fn_skip = set(check_notes.SKIP_DIRS) - {'attachments'}
    rel_files = check_notes.expand(targets, skip_dirs=fn_skip)
    ignored = git_ignored(rel_files)
    if ignored:
        rel_files = [p for p in rel_files if p not in ignored]
    allowed = load_allowlist()
    fn_warns = filename_warnings(rel_files, allowed)

    print('📦 文件名规范检查（仅 warning，不影响退出码）')
    if fn_warns:
        print(f'⚠️ warnings ({len(fn_warns)}):')
        for w in fn_warns:
            print('  ' + w)
    else:
        print('✅ 无文件名警告')
    print()

    # 3. 链接与格式检查
    print('🔗 链接与格式检查（scripts/check_notes.py，error 影响退出码）')
    errs, warns, n = check_notes.run_files(rel_files)
    print(f'检查了 {n} 个 Markdown 文件')
    if n == 0:
        print('❌ 未检查到任何 Markdown 文件')
        sys.exit(2)
    if warns:
        print(f'\n⚠️ warnings ({len(warns)}):')
        for w in warns:
            print('  ' + w)
    if errs:
        print(f'\n❌ errors ({len(errs)}):')
        for e in errs:
            print('  ' + e)
        sys.exit(1)
    print('\n✅ 无 error' + ('（有 warning，见上）' if warns else ''))


if __name__ == '__main__':
    main()
