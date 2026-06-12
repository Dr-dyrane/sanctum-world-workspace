# Tools Directory

All Python scripts for this workspace live here. Do not create `.py` files inside task folders.

## Subfolders

- `build/` — live build scripts, one per task, current version only. Run from repo root: `py tools/build/build-docx-kmNN-vX.py`
- `verify/` — substrate verification scripts (read-only, no mutations)
- `archive/` — dead/superseded scripts kept for reference; never execute

## Root-level scripts

- `mode_a_clone.py` — Mode A clone engine; imported by all build scripts
- `generate_reference_files.py` — reference file generator (NOT for task artifacts; see AGENTS.md guardrail 1)
- `build-world-performance-xlsx.py` — world performance spreadsheet builder

## Current non-task build script

- `build/build-docx-ondina-brainstorm.py` — Mode A clone build for `worlds/ondina-vasquell/submission/Ondina_Vasquell_Brainstorm.docx`

## macOS document-tool note, 2026-06-11

On the current local Mac, use the bundled Codex Python for repo automation:

`/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`

The bundled runtime also provides `soffice`, `pdfinfo`, and `pdftoppm` under:

`/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/`

Current Mac caveat: bundled `soffice` is present but fails because LibreOffice dylibs expect Homebrew libraries under `/opt/homebrew/opt/` for `little-cms2`, `fontconfig`, and `freetype`. That is a local dependency failure, not a DOCX defect. With Alexander approval, the clean fix is to install Homebrew and run `brew install little-cms2 fontconfig freetype`.

Until that is fixed, these built-in macOS tools are useful for sanity checks only:

- `qlmanage -t -s 1600 -o /tmp/docx-preview file.docx` for first-page visual preview.
- `textutil -convert html -output /tmp/docx.html file.docx` for text extraction review.
- `otool -L path/to/lib.dylib` for diagnosing missing dylib links.

Quick Look and textutil do not replace the full DOCX render gate in `docs/docx-generation-method.md`.

## Rules

- Do not store binaries, installers, package archives, credentials, or generated caches here.
- `__pycache__/` is gitignored automatically.
- System tools installed via `winget` or `pip`; do not vendor them here.
- On macOS, Homebrew or system package installs still require Alexander approval.
