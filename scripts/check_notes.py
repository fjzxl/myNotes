#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""笔记链接 / 格式校验库（由 check.py 调用，不提供独立命令行）。

路径统一规则（本模块所有对外接口都遵守）：
- 任何路径先经 normalize() 归一化为「仓库相对 posix 路径」（如 topics/x/y.md；仓库根为 '.'）；
- 越出仓库根的路径直接报错（normalize 抛 ValueError，链接解析记 error），不做静默忽略；
- 各项检查只使用归一化后的路径：豁免判断、报错定位、链接解析都以它为准。

对外接口：
    normalize(path, cwd=None, root=ROOT) -> str     单个路径归一化（越界抛 ValueError）
    expand(rel_paths, root=ROOT, skip_dirs=None) -> list[str]  展开为仓库内全部文件
    run(rel_paths, root=ROOT) -> (errors, warnings, n_checked)  展开后检查
    run_files(files, root=ROOT) -> (errors, warnings, n_checked)  复用已展开的列表

约定（与 AGENTS.md 一致）：
- templates/ 下的 {{...}} 与空 [[]] 是占位符，不检查 wikilink；
- 示例代码里的 [[Construct]] 等位于围栏 / 行内代码内，会被跳过；
- 笔记间链接一律用 Markdown 相对路径链接：任何非模板 wikilink 都记 error；
- 链接目标按磁盘实际大小写核对（GitHub 区分大小写，Windows 文件系统不区分）。
"""
import os
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {'.git', 'node_modules', 'attachments', 'archive', '.zcode', '.claude',
             '.vscode', 'scripts', 'tests', '__pycache__'}
TEMPLATE_DIR = 'templates'
BOM = '\ufeff'
URL_RE = re.compile(r'^(https?:|mailto:|#)')
LINK_RE = re.compile(r'(!?)\[([^\]]*)\]\(([^)]*)\)')
TITLE_RE = re.compile(r'\s+(?:"[^"]*"|\'[^\']*\')\s*$')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)\s*#*$')


class Report:
    """收集 error / warning，代替模块级全局列表（可重入、可测试）。"""

    def __init__(self):
        self.errors = []
        self.warnings = []

    def err(self, path, line, msg):
        self.errors.append(f'{path}:{line}: {msg}')

    def warn(self, path, line, msg):
        self.warnings.append(f'{path}:{line}: {msg}')


# ---------------------------------------------------------------- 路径统一

def normalize(path, cwd=None, root=ROOT):
    """把用户给出的路径（相对 cwd 或绝对）统一为仓库相对 posix 路径。越界抛 ValueError。"""
    base = Path(cwd) if cwd is not None else Path.cwd()
    p = (base / path).resolve()
    return p.relative_to(Path(root).resolve()).as_posix()


def _rel_from_walk(p, root):
    return Path(os.path.abspath(p)).relative_to(root).as_posix()


def expand(rel_paths, root=ROOT, skip_dirs=None):
    """展开为仓库相对路径的文件列表（目录递归，跳过 skip_dirs；显式给出的文件不跳过）。"""
    skip = SKIP_DIRS if skip_dirs is None else set(skip_dirs)
    root = Path(root).resolve()
    out = set()
    for t in rel_paths:
        base = root / t
        if base.is_file():
            out.add(_rel_from_walk(base, root))
        elif base.is_dir():
            for r, ds, fs in os.walk(base):
                ds[:] = [d for d in ds if d not in skip]
                for f in fs:
                    out.add(_rel_from_walk(Path(r, f), root))
        else:
            raise FileNotFoundError(t)
    return sorted(out)


# ---------------------------------------------------------------- 文本工具

def fence_open(line):
    """若该行是代码围栏（``` 或 ~~~，>=3 个），返回 (字符, 长度)，否则 None。"""
    s = line.lstrip()
    if not s or s[0] not in '`~':
        return None
    ch = s[0]
    n = len(s) - len(s.lstrip(ch))
    if n < 3:
        return None
    if ch == '`' and '`' in s[n:]:  # 反引号围栏的信息串中不能再出现反引号
        return None
    return ch, n


def strip_inline_code(line):
    """去掉行内代码 `...`、``...``（按等长反引号对匹配），便于链接 / 表格 / wikilink 判断。"""
    return re.sub(r'(`+)(.+?)\1', '', line)


def github_slug(heading):
    s = heading.strip().lower()
    return ''.join(ch for ch in s if ch.isalnum() or ch in ' -_').replace(' ', '-')


def collect(text):
    """单次遍历返回 (prose, headings, fences_balanced)。

    headings 为 GitHub 式锚点集合（重复标题生成 foo、foo-1、foo-2 …）。
    """
    prose, headings, used = [], {}, set()
    stack = []
    for i, line in enumerate(text.split('\n'), 1):
        f = fence_open(line)
        if f and stack and f[0] == stack[-1][0] and f[1] >= stack[-1][1]:
            stack.pop()
            continue
        if f and not stack:
            stack.append(f)
            continue
        if stack:
            continue
        prose.append((i, line))
        m = HEADING_RE.match(line)
        if m:
            base = slug = github_slug(m.group(2))
            k = 1
            while slug in used:
                slug = f'{base}-{k}'
                k += 1
            used.add(slug)
            headings.setdefault(slug, i)
    return prose, headings, not stack


# ---------------------------------------------------------------- 链接辅助

def _dir_listing(cache, d):
    key = ('dir', str(d))
    if key not in cache:
        try:
            cache[key] = set(os.listdir(d))
        except OSError:
            cache[key] = set()
    return cache[key]


def _exact_case(cache, root, rel_os_path):
    """按磁盘实际大小写逐级核对（GitHub 大小写敏感，Windows 不敏感）。"""
    cur = root
    for part in rel_os_path.split(os.sep):
        if not part or part == '.':
            continue
        if part not in _dir_listing(cache, cur):
            return False
        cur = cur / part
    return True


def _headings(cache, root, rel):
    key = ('heads', rel)
    if key not in cache:
        try:
            text = (root / rel).read_text(encoding='utf-8-sig', errors='replace')
        except OSError:
            cache[key] = {}
        else:
            cache[key] = collect(text)[1]
    return cache[key]


# ---------------------------------------------------------------- 各项检查

def frontmatter_check(rep, pos, text):
    lines = text.split('\n')
    if not lines or lines[0].rstrip() != '---':
        rep.warn(pos, 1, '缺少 YAML frontmatter')
        return
    end = next((j for j in range(1, len(lines)) if lines[j].rstrip() == '---'), None)
    if end is None:
        rep.err(pos, 1, 'frontmatter 没有结束定界符 ---（须独占一行）')
        return
    fm = '\n'.join(lines[1:end])
    if not fm.strip():
        rep.err(pos, 1, 'frontmatter 为空')
        return
    for key in ('title', 'tags', 'created', 'updated'):
        if not re.search(rf'^{key}\s*:', fm, re.M):
            rep.warn(pos, 1, f'frontmatter 缺少 {key}')


def wikilink_check(rep, pos, prose, in_templates):
    if in_templates:
        return
    for i, line in prose:
        for m in re.finditer(r'\[\[([^\]\[]+)\]\]', strip_inline_code(line)):
            raw = m.group(1)
            if not raw.split('|')[0].strip() or raw.startswith('{{'):
                continue
            rep.err(pos, i, f'wikilink（[[{raw}]]）已全库停用：Foam 各版本/各表面对 wikilink 的点击解析'
                            f'不一致（失败时回退「创建笔记」），GitHub 等标准渲染器也不识别；'
                            f'请改用相对路径 Markdown 链接 [文字](路径.md)')


def mdlink_check(rep, pos, prose, root, cache, own_headings):
    for i, line in prose:
        for m in LINK_RE.finditer(strip_inline_code(line)):
            is_img = m.group(1) == '!'
            inner = m.group(3).strip()
            if not inner:
                continue
            if inner.startswith('<'):
                end = inner.find('>')
                if end < 0:
                    rep.err(pos, i, f'链接目标 < 未闭合: ({m.group(3)})')
                    continue
                target = inner[1:end]
            else:
                if inner.startswith('#'):  # 同文档锚点 (#slug)：对本文标题校验
                    anchor = unquote(inner[1:].strip())
                    if anchor and github_slug(anchor) not in own_headings:
                        rep.warn(pos, i, f'锚点不存在: ({m.group(3)})')
                    continue
                if URL_RE.match(inner):
                    continue
                target = TITLE_RE.sub('', inner).strip()
                if re.search(r'\s', target):
                    rep.err(pos, i, f'链接目标含未编码空格（{target}），标准渲染器不识别；'
                                    f'请用 %20 编码，或写成 <路径>')
                    continue
            if not target or URL_RE.match(target):
                continue

            path_part, anchor = target, ''
            if not is_img and '#' in target:
                path_part, _, anchor = target.partition('#')
            path_part = unquote(path_part)
            if path_part.startswith('/'):
                resolved = root / path_part.lstrip('/')
            else:
                resolved = root / Path(pos).parent / path_part
            resolved = Path(os.path.normpath(resolved))

            found = next((c for c in (resolved, Path(str(resolved) + '.md')) if c.is_file()), None)
            if found is None:
                rep.err(pos, i, f'目标不存在: ({m.group(3)})')
                continue
            rel_os = os.path.relpath(str(found), str(root))
            if rel_os == os.pardir or rel_os.startswith(os.pardir + os.sep):
                rep.err(pos, i, f'链接指向仓库外: ({m.group(3)})')
                continue
            if not _exact_case(cache, root, rel_os):
                rep.err(pos, i, f'大小写与磁盘不一致（GitHub 区分大小写）: ({m.group(3)})')
                continue
            rel = Path(rel_os).as_posix()
            if anchor and not is_img and rel.endswith('.md'):
                if github_slug(unquote(anchor)) not in _headings(cache, root, rel):
                    rep.warn(pos, i, f'锚点不存在: ({m.group(3)})')


def table_check(rep, pos, prose):
    block = []

    def ncols(row):
        body = strip_inline_code(row).strip().strip('|')
        return len(re.split(r'(?<!\\)\|', body))

    def flush():
        if len(block) >= 2:
            want = ncols(block[0][1])
            for j, row in block[1:]:
                got = ncols(row)
                if got != want:
                    rep.err(pos, j, f'表格列数不一致（应为 {want}，实际 {got}）: {row.strip()[:60]}')
        block.clear()

    for i, line in prose:
        if line.lstrip().startswith('|'):
            block.append((i, line))
        else:
            flush()
    flush()


# ---------------------------------------------------------------- 入口

def _check(files, root):
    rep = Report()
    cache = {}
    checked = 0
    for pos in files:
        if not pos.endswith('.md'):
            continue
        try:
            raw = (root / pos).read_bytes()
        except OSError as e:
            rep.err(pos, 1, f'无法读取文件: {e}')
            continue
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError as e:
            rep.err(pos, 1, f'不是合法 UTF-8: {e}')
            continue
        checked += 1
        if text.startswith(BOM):
            text = text[1:]
        if b'\r\n' in raw:
            rep.warn(pos, 1, '包含 CRLF 行尾')
        if raw and not raw.endswith(b'\n'):
            rep.warn(pos, len(text.split('\n')), '缺少末尾换行')

        prose, heads, balanced = collect(text)
        if pos.startswith('topics/'):
            frontmatter_check(rep, pos, text)
        if not balanced:
            rep.err(pos, 1, '代码围栏不配对（有未闭合的围栏块）')
        wikilink_check(rep, pos, prose, pos.startswith(TEMPLATE_DIR + '/'))
        mdlink_check(rep, pos, prose, root, cache, heads)
        table_check(rep, pos, prose)

    return rep.errors, rep.warnings, checked


def run(rel_paths, root=ROOT):
    """对归一化后的仓库相对路径执行链接 / 格式检查，返回 (errors, warnings, 有效 md 文件数)。"""
    root = Path(root).resolve()
    return _check(expand(rel_paths, root), root)


def run_files(files, root=ROOT):
    """同 run()，但复用已由 expand() 展开的文件列表，避免重复遍历目录。"""
    root = Path(root).resolve()
    return _check(list(files), root)


if __name__ == '__main__':
    raise SystemExit('本文件已改为校验库；请在仓库根目录运行 `python check.py`。')
