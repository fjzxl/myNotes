# Repository guidance

- This is a Markdown knowledge base for VS Code + Foam. Commands and application code inside topic notes are teaching examples, not repository tooling; there is no repository build, test, lint, or CI pipeline.
- Keep note prose in the surrounding language (predominantly Chinese), with English filenames. Save text as UTF-8 with LF endings.

## Notes and navigation

- Subject references belong in `topics/`; atomic Zettelkasten notes and Map of Content (MOC) indexes belong in `notes/`. Tools are a separate subject under `topics/tools/`; exam prep (软考 etc.) is a separate subject under `topics/exams/`.
- There are five MOC files in `notes/` (programming, AI, math, history, exams), matching the README. Update the relevant existing index when adding or moving a topic note.
- Long tutorials are split into a hub note plus chapter notes: `topics/programming/Web/javascript.md` navigates 8 chapters in `topics/programming/Web/javascript/`, and `topics/programming/Web/css.md` navigates 10 stage notes in `topics/programming/Web/css/`. Put new content in the matching chapter (or a new chapter linked from the hub), not back into the hub.
- Use workspace-root-relative Foam links without `.md`: `[[topics/tools/Foam]]` or `[[topics/tools/Foam|label]]`. Avoid bare filenames and `../` in wikilinks; check inbound links when renaming notes.
- Store assets under `attachments/`, separate from notes. Existing topic images use Markdown paths such as `/attachments/images/math/inequalities/amgm-semicircle.png`; these are distinct from Foam wikilinks.
- Start new structured notes from `templates/` and retain the applicable YAML metadata. Topic notes carry `title`/`tags`/`created`/`updated` frontmatter; template `{{...}}` fields and empty `[[]]` links are intentional placeholders, not broken content to repair globally.

## Templates and rendering

- Full templates live in `templates/*.md`; `.vscode/foam.code-snippets` contains separate abbreviated skeletons. When changing a template's interface or adding one, check the matching snippet and the catalogs in `templates/README.md` and `README.md`.
- `templates/cornell-note.md` uses HTML/CSS Grid: inspect it with Markdown Preview Enhanced. Preserve the layout rather than flattening it into a Markdown table.
- `templates/cornell-marp.md` and `topics/programming/Java/slides/Servlet-lifecycle.md` are Marp documents. Preserve their frontmatter, slide separators, and class directives; preview with Marp. Export guidance is in `topics/tools/marp-guide.md`.
- Verification for note edits: run `python scripts/check_notes.py` (checks wikilink/Markdown-link/image targets, heading anchors, frontmatter shape, fence balance, table columns, encoding and line endings; dangling wikilinks on intentionally-labeled placeholder notes are warnings, not errors), plus checking relevant rendered output, especially math, Mermaid diagrams, and HTML layouts.

## Local configuration gotchas

- `.gitignore` excludes `.vscode/*` except `.vscode/extensions.json`; the local `settings.json` and `foam.code-snippets` are not tracked. Do not assume edits to them will be included in a commit.
- Workspace `.json` configuration and snippets contain comments (JSONC); strict JSON parsing will reject them.
- The Python interpreter path in local VS Code/Claude settings is machine-specific, not a portable setup prerequisite. `.claude/` and `.zcode/` are ignored local state.
