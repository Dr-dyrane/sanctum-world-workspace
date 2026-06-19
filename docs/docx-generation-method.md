# DOCX Generation Method - The Complete Working Loop

Date: 2026-06-04. Author: Claude, from the Korvin Merrow build. This is the deep method behind the approved World Spec and the 33 reference files. The spec took 3 visual-fidelity trials to ace; every failure and its fix is encoded here so the next run aces it in one. Companion docs: `worlds/korvin-merrow/reference-file-design/epic-note-design-system.md` (the visual design), `tools/generate_reference_files.py` (the generator), `docs/workspace-guardrails-lessons.md` (rules 4, 6, 8).

## 0. The philosophy in one paragraph

DOCX work fails when you eyeball and trust. It succeeds when you MEASURE the target, BUILD with the object model, VERIFY bytes after every save, RENDER to pixels, and DIFF numbers against the target before declaring anything done. Never trust "the script printed saved". Never trust "it looks close". Every claim about a document must be checkable by a command.

## 1. The loop (run this for every DOCX task)

```
RECON -> BUILD -> INTEGRITY GATE -> RENDER -> NUMERIC DIFF -> VISUAL CHECK -> iterate until diff is zero
```

### Step 1: RECON - measure the target before writing any build code

Never start from what a document "probably" looks like. Dump it.

```python
# structure dump: every paragraph (with style) and table (dims + header) IN BODY ORDER
from docx import Document
from docx.oxml.ns import qn
d = Document("target_or_template.docx")
paras, tbls, pi, ti = d.paragraphs, d.tables, 0, 0
for child in d.element.body.iterchildren():
    if child.tag == qn('w:p'):
        p = paras[pi]; pi += 1
        if p.text.strip(): print(f"P{pi-1} <{p.style.name}> {p.text[:80]}")
    elif child.tag == qn('w:tbl'):
        t = tbls[ti]; ti += 1
        hdr = " | ".join(c.text.strip()[:18] for c in t.rows[0].cells)
        print(f"  TBL{ti-1} {len(t.rows)}x{len(t.columns)} :: {hdr}")
```

```python
# fingerprint: the numbers that define the look (sizes, colors, fills, borders, styles)
import zipfile, re, collections
doc = zipfile.ZipFile(path).read('word/document.xml').decode('utf8')
sty = zipfile.ZipFile(path).read('word/styles.xml').decode('utf8')
print("sizes:",  collections.Counter(re.findall(r'<w:sz w:val="(\d+)"', doc)))      # half-points!
print("colors:", collections.Counter(re.findall(r'<w:color w:val="([^"]+)"', doc)))
print("fills:",  collections.Counter(re.findall(r'w:fill="([^"]+)"', doc)))
print("borders:",collections.Counter(re.findall(r'<w:(?:top|bottom|left|right|insideH|insideV)\b[^/>]*w:color="([^"]+)"', doc)))
print("styles:", sorted(set(re.findall(r'w:styleId="([^"]+)"', sty))))
```

Korvin findings this surfaced (would never be caught by eye): template body is uniformly 8pt (w:sz 16) with 10pt (20) only in the Patient Profile table; table hairlines are single 0.5pt #CCCCCC (black belongs only to the title card and callouts); title card is a LIGHT BLUE #D6E4F0 box with blue text, not a blue band with white text; the template's named table styles (Table1-20) are EMPTY SHELLS - the visible look is direct formatting, so "re-link to table styles" is a dead end and you must match the direct-format values.

Also recon CONVENTIONS from the instruction guide before styling anything (guardrail 7). Korvin's source-verified set: heading/table-header blue #4472C4; NO em dashes, en dashes, or arrow characters anywhere; synthetic banners centered top AND bottom; date displays MM/DD/YYYY; medication route "Oral" not "PO" (letter-O collides with P0-priority regex checks); Origin column tokens exactly "Public Domain" / "Databank Template" / "Custom Made" / "Writer Produced File, not a template".

### Step 2: BUILD - two modes, choose deliberately

**Mode A - Template fill (used for the World Spec).** When an official template exists, open THAT file and fill it in place. Never rebuild from blank `Document()` - that discards styles.xml, theme, numbering and you will never perfectly rebuild them.
- Replace placeholder text by clearing runs and adding a fresh run with explicit formatting (placeholder runs are often gray/italic instructional style - reusing them poisons your text).
- Add table rows by deep-copying the last styled row: `import copy; t._tbl.append(copy.deepcopy(t.rows[-1]._tr))` - cloned rows inherit cell shading/borders.
- Insert new blocks relative to anchors: `anchor._p.addnext(new_el)` / `addprevious`. To insert several elements in order with addnext, add them in REVERSE order.

**Mode B - Design-system generation (used for the 33 reference files).** When no template binds you, build from blank with a fixed design constant set and helper functions, then mass-produce. See `tools/generate_reference_files.py` for the full working implementation: shade(), borders(), run() with explicit font/size/color on EVERY run, band()/header() chrome, md-table -> styled table, pull-quote detection, per-file chrome from parsed metadata.

Non-negotiable build rules (each one is a paid-for scar):
1. **Object model for structure, never regex on raw XML.** A regex splice once produced invalid XML and a corrupt deployed file. Raw-XML regex is acceptable ONLY for flat value substitution (a color code, a size value), never for moving/inserting/deleting elements.
2. **Locate tables/paragraphs by CONTENT, never by position.** Positional indices shift the moment you insert anything. The Korvin patcher crashed exactly this way. Pattern:
   ```python
   fail_tables = [t for t in d.tables if len(t.columns)==2 and t.rows[0].cells[0].text.strip()=='Key Trap']
   prompt_boxes = [t for t in d.tables if len(t.rows)==1 and len(t.columns)==1 and t.rows[0].cells[0].text.startswith('Draft Prompt')]
   ```
3. **Set font name, size, color, bold explicitly on every run you create.** Inherited formatting is where gray-italic ghosts and wrong sizes come from.
4. **Scan ALL containers when searching text** - paragraphs AND every table cell (`for t in d.tables: for r in t.rows: for c in r.cells: ...`). The "letter-O PO" hunt failed first time because only paragraphs were scanned; the hits were in table cells.
5. **Keep the last-valid copy** of the file until the new one passes the gate. Recovery from the regex-splice corruption worked only because /tmp held the prior valid build.
6. Half-points: python-docx `Pt(8)` == `w:sz val="16"`. When diffing fingerprints remember the x2.

### Step 3: INTEGRITY GATE - after every single save

```python
raw = open(path,'rb').read()
assert raw.find(b'PK\x05\x06') >= 0, "no EOCD - truncated zip"
import zipfile; names = zipfile.ZipFile(path).namelist()
assert 'word/styles.xml' in names and 'word/document.xml' in names
from docx import Document; Document(path)   # must open
```
Korvin produced TWO corrupt saves (truncated zip, missing styles.xml) that "looked done" until this gate caught them. A file that fails any check does not exist, whatever the generator printed. (Environment note: the Claude-sandbox mount sometimes serves truncated READS of healthy files - if the gate fails on a file you did not just write, verify in the real environment before "fixing" it. Guardrail 1.)

### Step 4: RENDER - pixels are part of the spec

```bash
soffice --headless --convert-to pdf file.docx          # LibreOffice, timeout generously
pdftoppm -png -r 100 file.pdf page                     # page images
pdftotext file.pdf -                                   # split on \f to find BLANK PAGES
```
Then actually LOOK at page 1 and one dense page. Checks that only renders catch: blank pages (empty paragraphs interacting with Heading-1 pageBreakBefore - fix by deleting empty paragraphs via the object model, checking pPr for sectPr before removing); unreadable density (6pt text passes every XML check and fails every human); layout collapse in tables.
Caveat: the sandbox LibreOffice lacks Calibri/Calibri Light and substitutes (sometimes a serif). Font-family judgments need a Windows/Word render; everything else (sizes, colors, fills, breaks) is reliable.

Mac note, 2026-06-11: in the local macOS Codex app session, the bundled runtime includes `soffice`, `pdfinfo`, and `pdftoppm`, but `soffice` currently fails because its LibreOffice dylibs link to missing Homebrew paths under `/opt/homebrew/opt/` for `little-cms2`, `fontconfig`, and `freetype`. That is a machine dependency failure, not a DOCX failure. The clean fix, with Alexander approval, is to install Homebrew dependencies: `brew install little-cms2 fontconfig freetype`.

Mac fallbacks while LibreOffice is blocked:

```bash
qlmanage -t -s 1600 -o /tmp/docx-preview file.docx
textutil -convert html -output /tmp/docx.html file.docx
```

Use Quick Look for first-page visual sanity and textutil for text sanity only. They do not replace the full render gate because they do not prove multi-page PDF layout, page breaks, dense-table behavior, or PDF-to-PNG rendering.

### Step 5: NUMERIC DIFF - the definition of "matches the template"

Run the Step-1 fingerprint on BOTH files and compare. Done means: size set identical; border colors identical; fill palette a subset of the target's; margins equal (pgMar twips); styles.xml byte-identical when template-filling; zero banned characters. "Looks the same" is not a state; "fingerprint diff is empty" is.
The Korvin spec hit this state on trial 3: trial 1 = wrong sizes everywhere (6-7.5pt) + 138 black borders + solid-blue title; trial 2 = sizes/borders/fills/title fixed by global value mapping; trial 3 = grafted the template's substantive callout boxes verbatim (Terminology, Self-Containment - copy the whole <w:tbl> element from the template XML so styling travels with it), fixed margins 1008->1080, removed blank pages. Each trial was driven by the diff, not by taste.

### Step 6: CONTENT SCANS - before any "done"

- Banned characters: em dash, en dash, and arrow glyphs - count must be 0 in everything you author (quoted auditor text in notes fields is exempt).
- Workspace register: "locked", "ratification", "candidate", "this artifact", "the world tests" must not appear in final-facing prose (template-native occurrences exempt - verify provenance before "fixing").
- Letter-O "PO" tokens (ordinal 0x4F) anywhere - use "Oral" for routes.
- No invented clinical values: every dose/lab/vital traces to locked canon or a signed approval row; intentional ambiguities stay ambiguous (guardrail 5).

## 2. How the 33 reference files were actually made (Mode B end-to-end)

1. Designed ONE artisan sample by hand (FI-W01 ED Triage) implementing the full design system; rendered; got human approval on the look BEFORE mass production.
2. Generalized into a parametric builder: parse each locked .md (metadata header + ## sections + bullets + md-tables), map File Type -> department/title/signature via keyword table, render with shared chrome (synthetic band top+bottom, masthead, patient storyboard, ruled section headers, styled tables, pull-quotes for quoted speech, signature block, running header/footer).
3. Strip workspace canon-guard lines (post-world/golden/grader mentions) so files read chart-real; translate IDs (FI-* -> EW/E#-T#/WS) during parse.
4. Build all 33 with the integrity gate ASSERTED INSIDE the loop (a failure stops the batch, not discovered later).
5. Spot-render the hardest cases (table-heavy trend file, a consult) and visually verify; not every file needs a render once the builder is proven, but every file needs the gate.
6. Output under final date-stamped names matching the spec file plan EXACTLY (pre-flight: set(spec filenames) == set(disk filenames), zero missing, zero extra).

## 3. Failure -> fix table (what cost us trials)

| Failure | Root cause | Fix / rule |
|---|---|---|
| Corrupt saves (x2): no EOCD, missing styles.xml | interrupted writes; trusting "saved" print | Integrity gate after every save (Step 3) |
| Invalid XML, dead file | regex splice of block structure | Object model only for structure; keep last-valid copy |
| Patcher IndexError, edits landed in wrong tables | positional table indices after inserting new tables | Content-based locators only |
| 6-7.5pt text, black borders, wrong title | building by taste instead of fingerprint | Recon first; diff to zero (Steps 1, 5) |
| Blank pages 11 and 13 | empty paragraphs + Heading1 pageBreakBefore | pdftotext blank-page scan; delete empty paras via object model |
| "PO" priority flag from auditor | medication route "PO" (per os) = letter O token | Routes as "Oral"; scan ALL cells before disputing an auditor |
| Em dashes/arrows flagged in transcript | source content carried them into the render | Sanitize em dash, en dash, and arrow glyphs at parse time |
| Gray instructional text poisoning filled content | reusing placeholder runs | Clear runs; create fresh runs with explicit formatting |
| Callout boxes lost their look when recreated | rebuilding instead of copying | deepcopy the whole <w:tbl> element from the source XML |
| Font looks wrong in sandbox render | LibreOffice font substitution | Judge fonts on Windows/Word; trust sandbox for everything else |

## 4. Codex quickstart (smallest correct run)

```bash
# 1. recon target/template (Step 1 scripts)
# 2. build via tools/generate_reference_files.py (Mode B) or in-place fill (Mode A)
python3 tools/generate_reference_files.py
# 3. gate + render + look
python3 -c "from docx import Document; raw=open(F,'rb').read(); assert raw.find(b'PK\x05\x06')>=0; Document(F); print('gate ok')"
soffice --headless --convert-to pdf "$F" && pdftoppm -png -r 100 out.pdf p && open p-1.png
# macOS fallback only when bundled LibreOffice is dependency-blocked:
qlmanage -t -s 1600 -o /tmp/docx-preview "$F"
# 4. fingerprint diff vs target; iterate until empty
```

If a run fails: do NOT tweak blindly. Re-run recon on the failing output, diff against target, fix the specific numbers, re-gate, re-render. The loop converges in <=3 iterations when driven by measurements; it never converges when driven by taste.

## 5. Off-text report images: render through the renderer, never hand-draw (added 2026-06-17, OV09)

An off-text image whose finding can plausibly live in a REPORT or printout (a radiology report, a device printout, a labs page, an outside study, a downtime note) is AUTHORED through the canonical renderer and RENDERED to an image. Do NOT hand-draw it with PIL and do NOT assume it needs a generative model. The rendered image then carries the exact house chrome (masthead, blue bar, patient storyboard, PATIENT/ENCOUNTER block, footer) and is indistinguishable from the other charts, because it is the same template.

Method (`worlds/ondina-vasquell/phase-3-build-task-artifacts/build/render_ov09_image.py` is the reference):

1. Author the report content as a normal house-style note through `build_one` (`epic.py`): title, filing line (Author with department, so the masthead dept parses), sections, signature. It inherits the masthead, storyboard, encounter block, and footer for free, and passes GUARD plus the metadata scrub.
2. `soffice --headless --convert-to pdf --outdir <tmp> report.docx`, then `pdftoppm -png -r 150 -f 1 -l 1 report.pdf pg`. Crop trailing whitespace with PIL `ImageOps.invert(im.convert("L")).getbbox()` and save as JPG.
3. Mount ONLY the image. The off-text floor needs an image the model may not open; a text docx is always read and ceilings (see `OV-FLOOR-MECHANISM-LIBRARY.md`). The report docx is a render source, not a mounted artifact.
4. QA: OCR the JPG (`tesseract`) to confirm the finding is legible and the banned-glyph count is 0; view page 1.

`soffice` runs in the build sandbox (LibreOffice present); it is dependency-broken on the Mac, so render in the sandbox, not locally.

For future or reopened work after Larry's 2026-06-18 send-back, do NOT use a generative render for clinical photographs. Codex, Nanobanana, and similar image generators are not acceptable sources for scored bedside photos, wound photos, medication-bottle photos, skin findings, or clinical imaging simulations in new or reopened tasks. If a genuine photo is essential, use only a public-domain or permissively licensed noncopyrighted real image after current project guidance confirms that route is allowed. Record source, license, retrieval date, and any crop or edit; strip identifiers and metadata; then confirm the image matches the chart's date, severity, and clinical facts. If that gate cannot be satisfied, redesign the trap away from a photo.

FAIRNESS CAVEAT (the "why is this report an image" test): a report-as-image is only realistic when the genre is naturally an image. A device printout (OV04 CPAP report) or a SCANNED OUTSIDE study is naturally an image; an INTERNAL dictated report (radiology, labs) is normally text in the EHR, so rendering it as an image is borderline and a reviewer can flag it. If the off-text finding is an internal report, frame it as a scanned outside study with a distinct letterhead or scan look, or redesign the mechanism. Making the image match the internal house style exactly makes the "why an image" question sharper, not softer.
