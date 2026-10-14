#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check.py / scripts/check_notes.py 回归测试（标准库 unittest，全部在临时目录中构造夹具）。

运行：在仓库根目录执行  python -m unittest discover -s tests -v
"""
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / 'scripts'))
import check_notes  # noqa: E402

_spec = importlib.util.spec_from_file_location('check_entry', HERE / 'check.py')
check_entry = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_entry)


class Fixture(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name).resolve()

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, data):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(data, bytes):
            p.write_bytes(data)
        else:
            p.write_text(data, encoding='utf-8', newline='\n')
        return rel

    def run_rel(self, *rels):
        return check_notes.run(list(rels), root=self.root)


class PathNormalization(Fixture):
    def test_absolute_and_relative_normalize_equal(self):
        (self.root / 'templates').mkdir()
        rel = check_notes.normalize('templates', cwd=self.root, root=self.root)
        absolute = check_notes.normalize(str(self.root / 'templates'), cwd=self.root, root=self.root)
        self.assertEqual(rel, 'templates')
        self.assertEqual(rel, absolute)

    def test_outside_root_raises(self):
        with self.assertRaises(ValueError):
            check_notes.normalize('..', cwd=self.root, root=self.root)

    def test_missing_path_raises(self):
        with self.assertRaises(FileNotFoundError):
            check_notes.expand(['no/such/dir'], root=self.root)

    def test_expand_skip_dirs_is_configurable(self):
        self.write('attachments/a.png', b'x')
        self.write('topics/b.md', '# b\n')
        default = check_notes.expand(['.'], root=self.root)
        self.assertIn('topics/b.md', default)
        self.assertNotIn('attachments/a.png', default)
        incl = check_notes.expand(['.'], root=self.root,
                                  skip_dirs=set(check_notes.SKIP_DIRS) - {'attachments'})
        self.assertIn('attachments/a.png', incl)

    def test_templates_exempt_from_wikilink_error_via_absolute_path(self):
        self.write('templates/t.md', '---\ntitle: x\n---\n[[]] and [[Foo]]\n')
        errs, _, n = check_notes.run([str(self.root / 'templates')], root=self.root)
        # 绝对路径与相对路径都应得到同样结果：templates 下不报 wikilink
        self.assertEqual(n, 1)
        self.assertEqual([e for e in errs if '[[' in e], [])


class Links(Fixture):
    def test_raw_space_in_target_is_error(self):
        self.write('a.md', '[x](b c.md)\n')
        self.write('b c.md', '# b\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertTrue(any('未编码空格' in e for e in errs), errs)

    def test_percent20_target_ok(self):
        self.write('a.md', '[x](b%20c.md)\n')
        self.write('b c.md', '# b\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertEqual(errs, [])

    def test_angle_bracket_target_with_space_ok(self):
        self.write('a.md', '[x](<b c.md>)\n')
        self.write('b c.md', '# b\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertEqual(errs, [])

    def test_angle_bracket_target_is_validated(self):
        # 回归：<路径> 曾因 URL_RE 含 '<' 被整体跳过（死代码），缺失目标不报错
        self.write('a.md', '[x](<missing.md>)\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertTrue(any('目标不存在' in e for e in errs), errs)

    def test_case_mismatch_is_error(self):
        # 回归：Windows 大小写不敏感，须按磁盘实际大小写核对，否则 GitHub 404
        self.write('b.md', '# b\n')
        cache = {}
        self.assertTrue(check_notes._exact_case(cache, self.root, 'b.md'))
        self.assertFalse(check_notes._exact_case(cache, self.root, 'B.md'))
        self.write('a.md', '[x](B.md)\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertTrue(errs, 'expected an error for a case-mismatched link')

    def test_wikilink_is_error_outside_templates(self):
        self.write('a.md', 'see [[Foo]]\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertTrue(any('wikilink' in e for e in errs), errs)

    def test_link_outside_repo_is_error(self):
        self.write('a.md', '[x](../../etc.md)\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertTrue(errs, 'expected an error for a link leaving the repo')


class Frontmatter(Fixture):
    def test_four_dashes_do_not_close_frontmatter(self):
        self.write('topics/x.md', '---\ntitle: a\ntags: []\ncreated: 1\nupdated: 1\n----\nbody\n')
        self.write('topics/y.md', '---\ntitle: a\n---\n')  # 对照：正常闭合
        errs, _, _ = self.run_rel('topics')
        self.assertTrue(any('x.md' in e and 'frontmatter' in e for e in errs), errs)
        self.assertFalse(any('y.md' in e for e in errs), errs)

    def test_bom_does_not_break_frontmatter(self):
        self.write('topics/x.md', '\ufeff---\ntitle: a\ntags: []\ncreated: 1\nupdated: 1\n---\nbody\n')
        _, warns, _ = self.run_rel('topics')
        self.assertFalse(any('缺少 YAML frontmatter' in w for w in warns), warns)


class Fences(Fixture):
    def test_tilde_fence_content_skipped(self):
        self.write('a.md', '~~~\n[[NotAWikilink]]\n~~~\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertEqual(errs, [])

    def test_fence_char_must_match(self):
        # ``` 围栏内出现 ~~~ 不得误判为闭合；内容整体跳过
        self.write('a.md', '```\n[[X]]\n~~~\n[[Y]]\n```\n')
        errs, _, _ = self.run_rel('a.md')
        self.assertEqual(errs, [])


class Tables(Fixture):
    def test_pipe_inside_inline_code_does_not_split_cells(self):
        self.write('t.md', '| a | b |\n|---|---|\n| `x\\|y` | 2 |\n')
        errs, _, _ = self.run_rel('t.md')
        self.assertEqual(errs, [])

    def test_double_backtick_code_does_not_split_cells(self):
        self.write('t.md', '| a | b |\n|---|---|\n| ``x|y`` | 2 |\n')
        errs, _, _ = self.run_rel('t.md')
        self.assertEqual(errs, [])

    def test_real_column_mismatch_is_error(self):
        self.write('t.md', '| a | b |\n|---|---|\n| 1 | 2 | 3 |\n')
        errs, _, _ = self.run_rel('t.md')
        self.assertTrue(any('表格列数' in e for e in errs), errs)


class ReadErrors(Fixture):
    def test_invalid_utf8_is_reported_not_crash(self):
        self.write('bad.md', b'\xff\xfe\x00bad\n')
        errs, _, n = self.run_rel('bad.md')
        self.assertEqual(n, 0)
        self.assertTrue(any('UTF-8' in e for e in errs), errs)


class FilenameRules(Fixture):
    def test_daily_note_date_validation(self):
        warns = check_entry.filename_warnings(
            ['journal/daily/2026-02-30.md', 'journal/daily/2026-10-13.md'], set())
        self.assertEqual(len([w for w in warns if 'daily' in w]), 1)
        self.assertIn('2026-02-30', warns[0])

    def test_allowlist_matches_normalized_path(self):
        warns = check_entry.filename_warnings(['topics/tools/Foam.md'],
                                              {'topics/tools/Foam.md'})
        self.assertEqual(warns, [])

    def test_non_ascii_pdf_name_warned(self):
        warns = check_entry.filename_warnings(['topics/languages/japanese/语法.pdf'], set())
        self.assertEqual(len(warns), 1)
        self.assertIn('非 ASCII', warns[0])

    def test_uppercase_md_extension_warned(self):
        warns = check_entry.filename_warnings(['a/b.MD'], set())
        self.assertEqual(len(warns), 1)


if __name__ == '__main__':
    unittest.main()
