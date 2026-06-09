# Visual Signoff Specification

## Goal

Ensure the final documents look genuinely professional, not merely non-broken. Visual QA is performed against the rendered PDF preview of every Office file; when GPT-based review is used, page-image renders derived from that PDF are supplied so the reviewer can inspect the actual pixels.

## Prerequisites

- **LibreOffice** must be installed and available as `soffice` on the system PATH. This is a hard requirement for default mode. If LibreOffice is unavailable, the pipeline stops and writes `expert_action_required.md` unless degraded mode is enabled (see `runtime/degraded_mode_policy.md`).

## Evaluation Method

Render to PDF, then multimodal evaluation:

0. For any standalone diagram asset or any Office document that embeds generated diagrams, run the diagram mechanical validator first.
   - The validator must emit a machine-readable quality report.
   - The validator should also emit targeted crops for declared or auto-detected high-risk regions (wrap connectors, dense fan-in, tight label zones, etc.).
   - Any blocking defect in a diagram asset blocks signoff before multimodal review.
1. Each Office file (.docx, .pptx, .xlsx) is converted to PDF via headless LibreOffice.
2. If the OpenAI review harness is used, generate page-image renders from the PDF preview (or equivalent rendered page images) so GPT can inspect the actual page pixels.
3. `run_visual_review.py` invokes GPT-5.4 through non-interactive `codex exec`.
4. The reviewer inspects the attached page-image renders and uses extracted document text from PPTX/DOCX/XLSX/PDF artifacts only for supporting evidence and location anchors.
5. The reviewer evaluates the rendered appearance against the document's declared visual class and format-specific blocking checks.

## Evaluation Protocol

```
For each rendered file:

1. Main agent converts to PDF:
   soffice --headless --convert-to pdf "file.docx" --outdir previews/

2. Run `doc_gen_pipeline/openai_review_harness/run_visual_review.py` with:
   - PDF preview path
   - Page-image render path(s) derived from that PDF when available
   - Source Office artifact path for supporting extraction
   - Intended visual_class for this document
   - Format-specific blocking checks (from this spec)
   - Diagram validator report and risk-window crops, if diagrams are present
   - Visual signoff criteria

3. Visual Critic reviews the rendered PDF surface via the supplied page images and supporting extracted document text

4. Visual Critic applies format-specific blocking checks, using the diagram report/crops as a supplement rather than a substitute for page-level review

5. Visual Critic returns:
   - PASS or FAIL
   - Specific visual issues with page/slide references
   - Fix instructions for any defect

Default behavior:
  If LibreOffice is unavailable, stop the run and write expert_action_required.md.

Optional degraded mode (requires explicit opt-in):
  - Visual Critic relies on structural extraction only without rendered page images
  - Record degraded-mode notice: "Visual QA in structural mode - release confidence reduced"
  - See runtime/degraded_mode_policy.md for details
```

## Blocking Checks by Format

### Word / PDF

- Weak title hierarchy (missing or inconsistent heading levels)
- Inconsistent spacing between sections
- Crowded tables (insufficient padding, overlapping content)
- Bad page breaks (orphaned headers, split tables)
- Cheap-looking default styling (unstyled body, default fonts)
- Unreadable callouts or footnotes
- Any embedded diagram with a blocking defect from the diagram validator
- Any embedded diagram that is visibly pixelated or unreadable at intended page size

### PowerPoint

- Crowded slides (too much content per slide)
- Generic boilerplate layout
- Low-quality chart or table composition
- Weak spacing or alignment
- Inconsistent grid usage across slides
- Visual mismatch between slides in the same deck
- Any embedded or full-slide diagram with a blocking defect from the diagram validator
- Any embedded or full-slide diagram whose flow is ambiguous or unreadable at presentation size

### Excel

- Unstyled raw-looking workbook when the file is meant to be client-facing
- Poor tab ordering
- Unreadable headers
- Obvious generator artifacts (placeholder text, debug values)

### Email HTML

Email archives must be generated via `email_formatting_tools/generate_email_html.py`.

- Missing sidebar/main panel UI structure
- Raw text dump instead of professional email client appearance
- Missing or broken logo embedding
- Non-functional search bar
- Thread display out of chronological order
- Missing signature blocks
- Generic boilerplate tone (all emails sound the same)
- Broken HTML structure or styling

## Content Richness Checks

Visual quality includes not just formatting correctness but visual content density appropriate to the document type.

### Blocking (executive_polished only)

- PPTX: Fewer than 30% of content slides contain a chart, visualization, or diagram
- PPTX: More than 2 consecutive text-only slides (no chart, table, diagram, or image)
- PPTX: Only 1 type of visual element used across the entire deck (e.g., only tables)
- DOCX: A data-rich document (financial memo, benchmark report, valuation analysis) with zero embedded charts or conditionally-formatted tables
- XLSX: A client-facing workbook with 20+ data rows and no embedded chart on any worksheet

## Visual Classes

Each document must declare one visual class. The Visual Critic evaluates the file against its declared class.

| Class | Description |
|-------|-------------|
| `executive_polished` | Client-facing deliverable. Must look fully professional: strong typography, consistent branding, polished layout, and data visualizations (charts/diagrams) appropriate to document type. Text-only executive decks and chart-free financial memos are blocking. Highest visual bar. |
| `internal_working` | Internal team document. Should be clean and readable but does not require branding or polish. |
| `raw_export` | Data export or system output. May look rough. Only checked for basic readability. |
| `email_thread` | Email archive. Must look like a real email client, not a text dump. |
| `reference_material` | Supporting reference document. Should be organized and readable but not polished. |

## Required Output per Document

For each document evaluated:

- **Visual class**: The declared class for this document
- **Pass/Fail**: Overall verdict
- **Defect list**: Each defect with severity and description
- **Page/slide references**: Specific location of each defect
- **Fix instructions**: What needs to change to resolve each defect

## Release Rule

Release is **blocked** unless all `executive_polished` documents pass the Visual Critic evaluation, including content richness checks. An executive_polished deck with no charts or an executive_polished financial memo with no data visualizations fails content richness and blocks release. Documents of other visual classes are also blocking by default when realism, readability, file-type credibility, or artifact usability is affected; only the sole allowed `trivial_next_turn_fix` may remain open for the next pass.

---

## Template Acceptance Standard (R02)

The Visual Signoff must additionally verify the 3 brand template documents. Templates are evaluated before any other documents in the visual QA pass. A template failure blocks all downstream visual reviews until corrected.

### DOCX Brand Template — Required

- Typography hierarchy is present with visually distinct levels: Title, H1, H2, H3, Body, Data/Table text, Footnote/Caption.
- Color palette section present showing brand colors with labels and hex codes.
- Table formatting example with styled header row and alternating row or border treatment.
- Callout or highlight box example present.
- Footer example with page number placement and branding text.
- Document looks like a real internal corporate style guide — not a stub or placeholder.

### PPTX Brand Template — Required

- All six slide types present: title slide, section divider slide, chart slide, table slide, framework slide, appendix slide.
- Client style system applied to every slide (palette, fonts, logo placement, spacing).
- Chart slide has a real chart with labeled axes and a slide title.
- Table slide has a formatted data table with styled header and body rows.
- Framework slide has a 2x2 matrix, process flow, or similar analytical framework.
- Appendix slide has the correct appendix-page treatment.
- Template looks like real example slides, not a sparse skeleton.

### XLSX Brand Template — Required

- Summary sheet with a chart and KPI section using brand header style.
- Formatted table sheet with named header style, banded rows, and example data.
- Chart sheet with at least one chart connected to data.
- Assumptions sheet with labeled input parameters and formatted numeric values.
- Numeric formats demonstrated: currency, percentage, and date.
- Conditional formatting present on at least one numeric column.
- Tab color conventions applied with at least 2 differently-colored tabs.

---

## Extended Content-Richness Blocking (R03 — Scope Expansion)

Content-richness blocking is extended beyond `executive_polished` in the following cases:

### Solver-Critical Non-Polished Documents

Any document with `role: core_evidence`, `role: routing`, or `role: constraint` is solver-critical regardless of visual class. For solver-critical files:

- `reference_material` class: sparse or obviously unfinished layouts are **blocking**, not warnings. The content-richness exemption for reference_material does not apply to solver-critical files.
- `internal_working` class: clearly incomplete layouts (headings only, empty tables, minimal content that wouldn't survive real-world distribution) are **blocking** for solver-critical files.

### Organizational Branding

- Every document with `brand_mode: client_template` must show visible brand identity (name/logo and primary color accent). Absence is **blocking** at all visual classes.
- Every document with `brand_mode: secondary_org_profile` must show consistent visual identity for the authoring organization. Unstyled plain documents are **blocking**.
- Every document with `brand_mode: neutral_system_export` must read as a neutral system or machine export rather than an invented client-branded artifact. Applying client-style branding to a neutral export is **blocking**.

---

## PPTX Realism Blocking Checks (R03)

These checks apply to every PPTX in world_files/ regardless of visual class.

| Check | Rule | Severity |
|-------|------|----------|
| Slide count | Fewer than 6 total slides | Blocking |
| Content slide count (full_form) | Fewer than 4 content-bearing slides (excluding title, section divider, appendix cover) | Blocking |
| Blank canvas | Content slide with >50% blank area (no text, chart, table, image, or diagram) | Blocking |
| Solver-critical stub | Solver-critical PPTX with only a short note plus empty space, no analytical content | Blocking |
| Brand consistency | Master, typography, palette, or contrast doesn't match declared brand_mode | Blocking |
| Clipped elements | Table, timeline, chart, or text box clipped at slide border, off-canvas, or overlapping another element | Blocking |

---

## DOCX Realism Blocking Checks (R03)

| Check | Rule | Severity |
|-------|------|----------|
| Stub full_form | full_form DOCX with fewer than 3 pages of substantive content | Blocking |
| Short-form misclassification | short_form applied to a document that should be full-length analysis | Blocking |
| Margin cutoffs | Table columns, signature areas, or timelines cut off at page margins | Blocking |

---

## XLSX Realism Blocking Checks (R03)

| Check | Rule | Severity |
|-------|------|----------|
| Header style | Client-facing XLSX without a named/styled header row | Blocking |
| Numeric formats | Currency, percentage, or date columns without proper number formatting | Blocking |
| Summary chart | Client-facing XLSX without a chart on the summary/dashboard tab (unless manifest split_justification explicitly exempts) | Blocking |
| Spreadsheet family split | Related analytical views split across separate files without an explicit manifest realism justification | Blocking |
| CSV scope | CSV file without format_fit: raw_export | Blocking |

---

## File-Type Realism Blocking Checks (R03)

| Check | Rule | Severity |
|-------|------|----------|
| Signature docs as PPTX | Checklist, approval, SOW, contract form with format: pptx | Blocking |
| PPTX for non-presentations | format: pptx with format_fit: document, workbook, or raw_export | Blocking |
| Format-purpose mismatch | format_fit doesn't match realistic document-type purpose for the content | Blocking |

---

## Visual Legibility Blocking Checks (R03)

| Check | Rule | Severity |
|-------|------|----------|
| Body text contrast | Primary body text produces low contrast against background | Blocking |
| Accent color misuse | Saturated accent color used for core body text paragraphs | Blocking |

---

## Filler Content Rule (R03)

- Filler content is acceptable only when topic-relevant (it fills a section whose topic is real but specific data has not been set).
- Filler is not acceptable as a substitute for substantive content that makes the artifact look plausibly complete for its document type.
- Every in-world document must look like it could plausibly be sent, filed, or presented in a real professional context. Documents that no real professional would distribute are **blocking** regardless of visual formatting.

---

## Presentation Mode Compliance (R03b)

Visual signoff must evaluate presentation-mode-sensitive artifacts against the declared `presentation_mode`. This is separate from in-world client branding.

### Scope

- All `executive_polished` documents and the golden deliverable are subject to presentation-mode compliance evaluation.
- The four world regenerations must each declare an explicit mode from: `bcg`, `mckinsey`, `bain`. The value `generic` is not permitted for new regenerations.
- Mode compliance is evaluated using presentation_mode conventions documented in the pipeline's internal reference materials. Do not require literal MBB logos, footer text, or real firm marks.

### What the Visual Review Must Confirm

1. **Title conventions** match the declared mode (BCG: action titles with data; McKinsey: governing-thought titles; Bain: mixed action/topic titles).
2. **Layout and palette behavior** match the declared mode.
3. **Narrative structure** matches the declared mode (BCG: situation-complication-resolution; McKinsey: answer-first pyramid; Bain: target-diagnostic-intervention-implementation).
4. **Signature elements** are present for the declared mode.

### Blocking Conditions (R03b)

- Any `executive_polished` document that fails presentation-mode compliance for the declared mode is **blocking**.
- The golden deliverable that does not match the declared `presentation_mode` is **blocking**.
- `reference_materials/` must not appear in world_files/ or release/. If any reference_materials/ file is found in the output package, it is **blocking**.
