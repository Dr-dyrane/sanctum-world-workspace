# Tooling Verification

Verification date: 2026-05-29

Tools live on the machine. Only this verification documentation lives in the repo.

## System Tools

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
