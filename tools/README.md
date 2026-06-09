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

## Rules

- Do not store binaries, installers, package archives, credentials, or generated caches here.
- `__pycache__/` is gitignored automatically.
- System tools installed via `winget` or `pip`; do not vendor them here.
