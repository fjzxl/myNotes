# Repository guidance

- This is a Markdown knowledge base for VS Code + Foam. Commands and application code inside topic notes are teaching examples, not repository tooling; there is no repository build, test, lint, or CI pipeline.
- Keep note prose in the surrounding language (predominantly Chinese), with English filenames. Save text as UTF-8 with LF endings.

## Notes and navigation

- Subject references belong in `topics/`; atomic Zettelkasten notes and Map of Content (MOC) indexes belong in `notes/`. Tools are a separate subject under `topics/tools/`; exam prep (软考 etc.) is a separate subject under `topics/exams/`; language learning (日语 etc.) is a separate subject under `topics/languages/`.
- There are six MOC files in `notes/` (programming, AI, math, history, exams, languages), matching the README. Update the relevant existing index when adding or moving a topic note.
- Long tutorials are split into a hub note plus chapter notes: `topics/programming/Web/javascript.md` navigates 8 chapters in `topics/programming/Web/javascript/`, `topics/programming/Web/css.md` navigates 10 stage notes in `topics/programming/Web/css/`, and `topics/math/inequalities.md` navigates 6 chapter notes in `topics/math/inequalities/` (the hub keeps the overview table and 口诀速记). Put new content in the matching chapter (or a new chapter linked from the hub), not back into the hub.
- Delivering a planned long-form unit doubles as a Zettelkasten pass: extract 3–5 atomic permanent notes into `notes/` (from `templates/permanent-note.md`, English filenames, one concept each) that link back to the source unit, and list them under the unit's entry in the matching MOC.
- Note-to-note links (plain or with heading anchors) use the Markdown form `[label](relative/path.md)` / `[label](relative/path.md#github-slug)` — path relative to the source note (`../` is fine), spaces percent-encoded (`notes/MOC - math.md` → `notes/MOC%20-%20math.md`); slug rules as in `github_slug` in `scripts/check_notes.py`. These links jump natively in VS Code preview, Foam, and GitHub.
- Do NOT use `[[...]]` wikilinks outside `templates/` (intentional `[[]]` placeholders there are exempt): Foam's wikilink click-resolution is inconsistent across versions and surfaces — unresolved ones fall back to "create note" (observed 2026-10-12/13 from a journal note, see README changelog), and standard renderers (GitHub etc.) don't treat wikilinks as links at all. `check_notes.py` reports every non-template wikilink as an error. Check inbound links when renaming notes.
- Store assets under `attachments/`, separate from notes. Existing topic images use Markdown paths such as `/attachments/images/math/inequalities/amgm-semicircle.png`; these are distinct from Foam wikilinks. Exception: large textbook PDFs stay local next to their notes (e.g. `topics/languages/japanese/*.pdf`, gitignored — see the note in `.gitignore`).
- Start new structured notes from `templates/` and retain the applicable YAML metadata. Topic notes carry `title`/`tags`/`created`/`updated` frontmatter; template `{{...}}` fields and empty `[[]]` links are intentional placeholders, not broken content to repair globally.

## Templates and rendering

- Full templates live in `templates/*.md`; `.vscode/foam.code-snippets` contains separate abbreviated skeletons. When changing a template's interface or adding one, check the matching snippet and the catalogs in `templates/README.md` and `README.md`.
- `templates/cornell-note.md` uses HTML/CSS Grid: inspect it with Markdown Preview Enhanced. Preserve the layout rather than flattening it into a Markdown table.
- `templates/cornell-marp.md` and `topics/programming/Java/slides/Servlet-lifecycle.md` are Marp documents. Preserve their frontmatter, slide separators, and class directives; preview with Marp. Export guidance is in `topics/tools/marp-guide.md`.
- Verification for note edits: run `python check.py` (works from any directory; no arguments checks the whole vault). It prints filename-convention warnings (kebab-case style, daily-note date naming, extension case — intentional exceptions are listed in the root `.checkallow`, one repo-relative path per line with `#` comments; gitignored local files such as the textbook PDFs are skipped automatically) plus the link/format errors of `scripts/check_notes.py` (Markdown-link/wikilink/image targets, same-note and cross-note heading anchors, frontmatter shape, fence balance, table columns, encoding and line endings; link errors set the exit code, filename issues are warnings only; wikilinks are errors everywhere except `templates/` placeholders), plus checking relevant rendered output, especially math, Mermaid diagrams, and HTML layouts.

## Local configuration gotchas

- `.gitignore` excludes `.vscode/*` except `.vscode/extensions.json` and `.vscode/foam.code-snippets`; the local `settings.json` is not tracked — do not assume edits to it will be included in a commit.
- Workspace `.json` configuration and snippets contain comments (JSONC); strict JSON parsing will reject them.
- The Python interpreter path in local VS Code/Claude settings is machine-specific, not a portable setup prerequisite. `.claude/` and `.zcode/` are ignored local state.
