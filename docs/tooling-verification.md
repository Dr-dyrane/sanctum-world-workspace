# Tooling Verification

Verification date: 2026-05-29
Mac verification update: 2026-06-11

Tools live on the machine. Only this verification documentation lives in the repo.

The 2026-05-29 verification below is a Windows snapshot. The current local Codex thread on 2026-06-11 is macOS 26.5.1 on arm64. Use the Mac verification first when working from this machine.

## macOS System Tools, 2026-06-11

| Tool | Version / Status | Executable path | Verification command | Result |
| --- | --- | --- | --- | --- |
| macOS | 26.5.1, arm64 | system | `sw_vers`; `uname -m` | PASS |
| Bundled Codex Python | Python 3.12.13 | `/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3` | `python3 --version` using bundled path | PASS |
| Bundled Poppler pdfinfo | 26.05.0 | `/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdfinfo` | `pdfinfo -v` using bundled path | PASS |
| Bundled Poppler pdftoppm | 26.05.0 | `/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm` | `pdftoppm -v` using bundled path | PASS |
| Bundled LibreOffice / soffice | Present but currently cannot launch | `/Users/dyrane/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/soffice` | `soffice --version` using bundled path | FAIL, missing `/opt/homebrew/opt/little-cms2/lib/liblcms2.2.dylib` |
| Quick Look thumbnailer | Installed | `/usr/bin/qlmanage` | `command -v qlmanage`; test thumbnail render on KM10 golden | PASS |
| textutil | Installed | `/usr/bin/textutil` | `command -v textutil`; test DOCX to HTML conversion | PASS |
| sips | Installed | `/usr/bin/sips` | `command -v sips` | PASS |
| cupsfilter | Installed, but not usable for DOCX here | `/usr/sbin/cupsfilter` | `command -v cupsfilter`; DOCX MIME check | FAIL for DOCX path |
| otool | Installed | `/usr/bin/otool` | `otool -L` on bundled LibreOffice dylibs | PASS |
| Homebrew | Missing | none on PATH | `command -v brew` | MISSING |
| System LibreOffice | Missing | none on PATH | `command -v soffice`; `command -v libreoffice` | MISSING |

## macOS Python Package Verification, 2026-06-11

Verified in the bundled Codex Python environment.

| Package | Bundled Codex Python version | Result |
| --- | --- | --- |
| python-docx (`docx`) | 1.2.0 | PASS |
| openpyxl | 3.1.5 | PASS |
| pandas | 2.2.3 | PASS |
| lxml | 6.0.2 | PASS |

## macOS Render Finding, 2026-06-11

Bundled LibreOffice is present, but its framework dylibs link to Homebrew-style absolute paths:

- `/opt/homebrew/opt/little-cms2/lib/liblcms2.2.dylib`
- `/opt/homebrew/opt/fontconfig/lib/libfontconfig.1.dylib`
- `/opt/homebrew/opt/freetype/lib/libfreetype.6.dylib`

Those paths are absent on this Mac. The same libraries exist inside the bundled Poppler tree, but the cleaner system-level fix is to install the Homebrew packages only after Alexander approves. Until then, Quick Look and textutil are sanity fallbacks, not replacements for the full render gate.

## Windows System Tools, 2026-05-29

| Tool | Version | Executable path | Verification command | Result |
| --- | --- | --- | --- | --- |
| LibreOffice / soffice | 26.2.3.2 | `C:\Program Files\LibreOffice\program\soffice.com` | `soffice --version` | PASS |
| Pandoc | 3.9.0.2 | `C:\Users\Dyrane\AppData\Local\Pandoc\pandoc.exe` | `pandoc --version` | PASS |
| Poppler pdfinfo | 25.07.0 | `C:\Users\Dyrane\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin\pdfinfo.exe` | `pdfinfo -v` | PASS |
| Poppler pdftoppm | 25.07.0 | `C:\Users\Dyrane\AppData\Local\Microsoft\WinGet\Packages\oschwartz10612.Poppler_Microsoft.Winget.Source_8wekyb3d8bbwe\poppler-25.07.0\Library\bin\pdftoppm.exe` | `pdftoppm -v` | PASS |

## Python Environments

| Environment | Version / Path | Notes |
| --- | --- | --- |
| User Python via `py` | Python 3.14.3 | Packages installed with `py -m pip install --upgrade ...` |
| Bundled Codex Python | `C:\Users\Dyrane\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe` | Packages also installed here because Codex document/spreadsheet workflows commonly use this runtime |

## Python Package Verification

Verified by importing each module and reading `__version__` where available.

| Package | User Python version | Bundled Codex Python version | Verification command | Result |
| --- | --- | --- | --- | --- |
| PyPDF2 | 3.0.1 | 3.0.1 | `py - <<imports>>`; bundled Python equivalent | PASS |
| pdfplumber | 0.11.9 | 0.11.9 | `py - <<imports>>`; bundled Python equivalent | PASS |
| python-docx (`docx`) | 1.2.0 | 1.2.0 | `py - <<imports>>`; bundled Python equivalent | PASS |
| openpyxl | 3.1.5 | 3.1.5 | `py - <<imports>>`; bundled Python equivalent | PASS |
| pandas | 3.0.3 | 3.0.3 | `py - <<imports>>`; bundled Python equivalent | PASS |
| lxml | 6.1.1 | 6.1.1 | `py - <<imports>>`; bundled Python equivalent | PASS |

## PATH Notes

- User PATH was updated to include LibreOffice, Pandoc, and Poppler binary directories.
- Bare commands now resolve for `soffice`, `pandoc`, `pdfinfo`, and `pdftoppm`.
- The plain `python` command may still resolve to the Microsoft Store alias; use `py` or the bundled Codex Python path for reliable execution.
