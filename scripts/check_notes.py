#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""轻量笔记校验：链接、图片、frontmatter、代码围栏、表格、编码。

用法（仓库根目录运行）：
    python scripts/check_notes.py               # 全量检查
    python scripts/check_notes.py path/to/note.md ...   # 只检查指定文件

退出码：发现 error 返回 1，只有 warning 返回 0。

约定（与 AGENTS.md 一致）：
- templates/ 下的 {{...}} 与空 [[]] 是占位符，不检查 wikilink 目标；
- 示例代码里的 [[Construct]]、[[Scopes]] 等都在围栏/行内代码内，会被跳过；
-Foam 允许引用尚未创建的笔记（placeholder），悬空 wikilink 只记 warning。
"""
import os
import re
import sys
from pathlib import Path

# 输出含 emoji：在 GBK 等非 UTF-8 控制台（如中文 Windows PowerShell）下强制 UTF-8，
# 避免 UnicodeEncodeError 导致检查中断。
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, 'reconfigure'):
        _stream.reconfigure(encoding='utf-8')

SKIP_DIRS = {'.git', 'node_modules', 'attachments', 'archive', '.zcode',
             '.claude', '.vscode', 'scripts'}
TEMPLATE_DIR = 'templates'
URL_RE = re.compile(r'^(https?:|mailto:|<|#)')

errors, warnings = [], []


def err(path, line, msg):
    errors.append(f'{path}:{line}: {msg}')


def warn(path, line, msg):
    warnings.append(f'{path}:{line}: {msg}')


def fence_open_len(line):
    s = line.lstrip()
    n = len(s) - len(s.lstrip('`'))
    return n if n >= 3 else 0


def scan_lines(text):
    """Yield (lineno, line, in_fence) with fence state tracked by fence length."""
    stack = []
    for i, line in enumerate(text.split('\n'), 1):
        n = fence_open_len(line)
        if n:
            if not stack:
                stack.append(n)
                yield i, line, True
                continue
            if n >= stack[-1]:
                stack.pop()
                yield i, line, True
                continue
        yield i, line, bool(stack)


def strip_inline_code(line):
    return re.sub(r'`[^`]*`', '', line)


def github_slug(heading):
    s = heading.strip().lower()
    out = []
    for ch in s:
        if ch.isalnum() or ch in ' -_':
            out.append(ch)
    return ''.join(out).replace(' ', '-')


def collect(text):
    """Return (prose, headings, fences_balanced)."""
    prose = []
    headings = {}
    balanced = True
    for i, line, in_fence in scan_lines(text):
        if in_fence:
            continue
        prose.append((i, line))
        m = re.match(r'^(#{1,6})\s+(.*?)\s*#*$', line)
        if m:
            headings.setdefault(github_slug(m.group(2)), i)
    # fence balance: any line opening a fence that never closed leaves stack non-empty
    stack = []
    for line in text.split('\n'):
        n = fence_open_len(line)
        if n:
            if not stack:
                stack.append(n)
            elif n >= stack[-1]:
                stack.pop()
    if stack:
        balanced = False
    return prose, headings, balanced


def frontmatter_check(path, text):
    if not text.startswith('---'):
        warn(path, 1, '缺少 YAML frontmatter')
        return
    end = text.find('\n---', 3)
    if end == -1:
        err(path, 1, 'frontmatter 没有结束定界符 ---')
        return
    fm = text[3:end]
    if not fm.strip():
        err(path, 1, 'frontmatter 为空')
        return
    for key in ('title', 'tags', 'created'):
        if not re.search(rf'^{key}\s*:', fm, re.M):
            warn(path, 1, f'frontmatter 缺少 {key}')


def wikilink_check(path, prose, all_notes, in_templates):
    for i, line in prose:
        for m in re.finditer(r'\[\[([^\]\[]+)\]\]', strip_inline_code(line)):
            raw = m.group(1)
            target = raw.split('|')[0].strip()
            if not target or target.startswith('{{'):
                continue
            if in_templates:
                continue
            file_part, _, anchor = target.partition('#')
            file_part = file_part.strip()
            if not file_part:
                if anchor and anchor.lstrip('^') not in {h for h in []}:
                    pass
                continue
            if file_part not in all_notes:
                if re.search(r'[/\\]', file_part):
                    warn(path, i, f'wikilink 目标不存在: [[{raw}]]')
                else:
                    warn(path, i, f'悬空/裸文件名 wikilink: [[{raw}]]')
            elif anchor:
                slug = github_slug(anchor.lstrip('^'))
                if slug and slug not in HEADINGS.get(file_part, {}):
                    warn(path, i, f'wikilink 锚点不存在: [[{raw}]]')


def mdlink_check(path, prose, all_notes, headings_index):
    for i, line in prose:
        clean = strip_inline_code(line)
        for m in re.finditer(r'(!?)\[([^\]]*)\]\(([^)\s]+)\)', clean):
            is_img, target = m.group(1) == '!', m.group(3)
            if URL_RE.match(target):
                continue
            t = target
            anchor = ''
            if not is_img and '#' in t:
                t, _, anchor = t.partition('#')
            if t.startswith('/'):
                resolved = Path('.' + t)
            else:
                resolved = Path(path).parent / t
            found = None
            for cand in (resolved, Path(str(resolved) + '.md')):
                if cand.is_file():
                    found = cand
                    break
            if found is None:
                (err if is_img or not anchor else err)(path, i, f'目标不存在: ({target})')
                continue
            if anchor and not is_img:
                target_text = found.read_text(encoding='utf-8', errors='replace')
                _, heads, _ = collect(target_text)
                if github_slug(anchor) not in heads:
                    warn(path, i, f'锚点不存在: ({target})')


def table_check(path, prose):
    block = []

    def flush():
        if len(block) >= 2:
            def ncols(row):
                body = row.strip().strip('|')
                return len(re.split(r'(?<!\\)\|', body))
            want = ncols(block[0][1])
            for j, row in block[1:]:
                got = ncols(row)
                if got != want:
                    err(path, j, f'表格列数不一致（应为 {want}，实际 {got}）: {row.strip()[:60]}')
        block.clear()

    for i, line in prose:
        if line.lstrip().startswith('|'):
            block.append((i, line))
        else:
            flush()
    flush()


def main():
    roots = sys.argv[1:] or ['.']
    files = []
    for root in roots:
        if root.endswith('.md'):
            files.append(Path(root))
            continue
        for r, ds, fs in os.walk(root):
            ds[:] = [d for d in ds if d not in SKIP_DIRS]
            for f in fs:
                if f.endswith('.md'):
                    files.append(Path(r, f))

    # wikilink 目标索引始终基于整个知识库，避免单文件模式下误报
    vault = []
    for r, ds, fs in os.walk('.'):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            if f.endswith('.md'):
                vault.append(Path(r, f))
    all_notes = {p.as_posix()[:-3] for p in vault}
    global HEADINGS
    HEADINGS = {}
    vault_text = {}
    for p in vault:
        pos = p.as_posix()
        try:
            vault_text[pos] = p.read_bytes().decode('utf-8')
        except UnicodeDecodeError:
            continue
    for pos, text in vault_text.items():
        _, heads, _ = collect(text)
        HEADINGS[pos[:-3]] = set(heads)

    contents = {p.as_posix(): vault_text[p.as_posix()]
                for p in files if p.as_posix() in vault_text}
    for p in files:
        pos = p.as_posix()
        raw = p.read_bytes()
        try:
            raw.decode('utf-8')
        except UnicodeDecodeError as e:
            err(pos, 1, f'不是合法 UTF-8: {e}')
            continue
        if b'\r\n' in raw:
            warn(pos, 1, '包含 CRLF 行尾')
        if raw and not raw.endswith(b'\n'):
            warn(pos, len(raw.split(b'\n')), '缺少末尾换行')

    for pos, text in contents.items():
        prose, heads, balanced = collect(text)
        in_templates = pos.startswith(TEMPLATE_DIR + '/')
        in_topics = pos.startswith('topics/')
        if in_topics:
            frontmatter_check(pos, text)
        if not balanced:
            err(pos, 1, '代码围栏不配对（有未闭合的 ``` 块）')
        wikilink_check(pos, prose, all_notes, in_templates)
        mdlink_check(pos, prose, all_notes, HEADINGS)
        table_check(pos, prose)

    print(f'检查了 {len(contents)} 个 Markdown 文件')
    if warnings:
        print(f'\n⚠️ warnings ({len(warnings)}):')
        for w in warnings:
            print('  ' + w)
    if errors:
        print(f'\n❌ errors ({len(errors)}):')
        for e in errors:
            print('  ' + e)
        sys.exit(1)
    print('\n✅ 无 error' + ('（有 warning，见上）' if warnings else ''))


if __name__ == '__main__':
    main()
