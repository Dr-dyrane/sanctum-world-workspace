# Tooling Audit

Audit date: 2026-05-29
Mac update: 2026-06-11

No tools were installed during this audit.

## Summary

The 2026-05-29 table below is the Windows snapshot. The current local Codex thread on 2026-06-11 is macOS 26.5.1 on arm64. Use the Mac update first when working from this machine.

## macOS update, 2026-06-11

No tools were installed during this check.

| Tool | Status on this Mac | Why It Matters | Action |
| --- | --- | --- | --- |
| Bundled Codex Python | Installed: `/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3` | Preferred runtime for DOCX, spreadsheet, and verification scripts | Use this path for repo automation |
| Bundled Poppler | Installed: `/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo` and `pdftoppm` | PDF inspection and PDF to PNG rendering | Use bundled paths if bare commands are absent |
| Bundled LibreOffice / soffice | Present at `/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/soffice`, but fails on this Mac | Required for the full DOCX render gate | Fix dependencies before treating a render failure as a DOCX defect |
| Homebrew | Missing from PATH | Cleanest way to satisfy the bundled LibreOffice absolute dylib links on Apple Silicon | Install only with Alexander approval |
| Homebrew dylibs expected by bundled LibreOffice | Missing under `/opt/homebrew/opt/` | `libvcllo.dylib` and `libcairo-lo.2.dylib` link to `little-cms2`, `fontconfig`, and `freetype` at Homebrew paths | With approval: install Homebrew, then `brew install little-cms2 fontconfig freetype` |
| `qlmanage` | Installed: `/usr/bin/qlmanage` | Quick Look DOCX thumbnail render for fast visual sanity checks | Fallback only, not the full render gate |
| `textutil` | Installed: `/usr/bin/textutil` | DOCX to HTML/text conversion for text sanity checks | Fallback only, not a layout gate |
| `sips` | Installed: `/usr/bin/sips` | Image inspection and conversion | Useful with Quick Look output |
| `cupsfilter` | Installed: `/usr/sbin/cupsfilter`; DOCX MIME not supported in our check | Possible document filter on some Macs | Do not rely on it for DOCX rendering here |
| `otool` | Installed: `/usr/bin/otool` | Dylib dependency inspection | Use to diagnose Mac render failures |

Mac render doctrine:

- Full DOCX visual QA still means LibreOffice render to PDF or PNG, followed by visual inspection.
- A bundled `soffice` failure that names `/opt/homebrew/opt/little-cms2/lib/liblcms2.2.dylib`, `/opt/homebrew/opt/fontconfig/lib/libfontconfig.1.dylib`, or `/opt/homebrew/opt/freetype/lib/libfreetype.6.dylib` is a machine dependency failure, not evidence the DOCX is corrupt.
- Quick Look fallback command: `qlmanage -t -s 1600 -o /tmp/docx-preview file.docx`. It is useful for first-page visual sanity only.
- Text fallback command: `textutil -convert html -output /tmp/docx.html file.docx`. It is useful for text extraction sanity only.
- The clean Mac fix, if Alexander approves installs, is to follow the current official Homebrew install instructions, confirm Apple Silicon prefix `/opt/homebrew`, then run `brew install little-cms2 fontconfig freetype`.

## Windows snapshot, 2026-05-29

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
