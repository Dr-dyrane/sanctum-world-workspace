# Tooling Audit

Audit date: 2026-05-29

No tools were installed during this audit.

## Summary

| Tool | Status | Why It Matters | Need Level | Recommended Install If Missing |
| --- | --- | --- | --- | --- |
| Git | Installed: `git version 2.51.0.windows.1` | Checkpoints, rollback, review | Required | Already installed |
| Python launcher | Installed: `py` reports Python 3.14.3 | General scripting fallback | Optional | Already installed |
| `python` command | Present but points to Microsoft Store alias and does not run Python | Can confuse scripts that call `python` | Optional to fix | Disable Windows App Execution Alias or install Python from python.org |
| Bundled Codex Python | Installed: Python 3.12.13 | Preferred for DOCX/spreadsheet automation in Codex | Required for local automation | Already available |
| Node.js | Installed: v22.19.0 | General JS tooling | Optional | Already installed |
| Bundled Codex Node | Installed: v24.14.0 | Codex runtime and document tooling | Required for bundled tools | Already available |
| Pandoc | Missing | Markdown/DOCX/PDF conversion | Optional | `winget install JohnMacFarlane.Pandoc` |
| LibreOffice / soffice | Missing | DOCX render-to-PDF/PNG visual QA | Recommended | `winget install TheDocumentFoundation.LibreOffice` |
| Poppler tools (`pdftoppm`, `pdfinfo`) | Missing | PDF rendering and inspection | Recommended | `winget install oschwartz10612.Poppler` |
| DOCX editing support | Installed via bundled Python `docx` | Generate and inspect Word files | Required | Already available |
| Spreadsheet support | Installed via bundled Python `openpyxl`, `pandas` | Read task tracker spreadsheets | Required | Already available |
| PDF Python libraries | Partial: `reportlab` installed; `PyPDF2` and `pdfplumber` missing | PDF generation exists; parsing is limited | Optional | Use bundled environment if available or install only with approval |
| Browser automation | Available as Codex/Chrome tooling, but Chrome bridge previously had trust issues | RL Studio navigation may require authenticated Chrome | Optional until RL Studio operation | Reconnect/repair bridge only with approval |
| MCP configuration | Present: `C:\Users\Dyrane\.codex\config.toml` | Tool/plugin configuration | Optional to inspect further | No install needed |

## Notes

- Use bundled Codex Python path for document/spreadsheet tasks:
  `C:\Users\Dyrane\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`
- Plain `python` is not reliable on this machine because it launches the Microsoft Store alias.
- LibreOffice is the main missing capability for visual DOCX rendering.
- Poppler is the main missing capability for PDF page rendering.
- Do not install tools without Alexander approval.

