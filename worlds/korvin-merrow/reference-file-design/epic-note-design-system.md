# Epic-Style Synthetic Note Design System - Korvin Merrow Reference Files

Date: 2026-06-03
Purpose: define an exact-as-possible Epic/EHR visual + structural design for the 26 template/reference files (FI-W01-FI-W22, FI-S01-FI-S04) so they read as authentic hospital chart documents instead of Markdown->DOCX conversions.
Fidelity target: as close to real Epic note printouts as practical. No Epic logos, trademarks, or proprietary template copying - structure, terminology, and layout conventions only.

## 0. Core principles (read first)

1. **Render locked content only.** Every clinical fact, date, name, and value must come from the locked FI source file. **Never invent vitals, labs, doses, or values to fill an Epic field.** Where a note type implies a value the canon does not provide, either reference the source file (e.g., "see Flowsheet, FI-W12") or mark it "Pending"/"Unverified" - which is itself authentic EHR behavior at admission.
2. **Fictional, no-PHI.** Patient is synthetic. Use a fictional facility identity (see section 1). No real Epic branding.
3. **One design, many note types.** A shared chrome (banner, fonts, signature, footer) + per-note-type body skeletons (section 4).
4. **Consistency across all 26 files** - same banner, fonts, margins, signature, and footer everywhere.

## 0a. Source-guide-verified corrections (added after checking reference folder)

Confirmed against `New Writers Version - Instruction Guide (05_24).md` and the example packages. These OVERRIDE earlier choices in this spec where they conflict:

1. **Synthetic disclaimer banner is required** and goes **centered, top AND bottom** of each rendered page - not top-right. Guide line 1356: "Synthetic training document banners centered top and bottom of rendered PDFs." See section 3.6.
2. **Heading / table-header blue is `#4472C4`** (house standard), not navy `#1F3864`. Update all header/accent fills accordingly.
3. **No em dashes, en dashes, or arrow characters** anywhere - use plain hyphens, colons, or restructure. (The current FI-W03 sample uses "-" and "-"; both must be replaced in the real build.)
4. **House style for clinical document templates is Courier New monospace** ("to preserve EHR voice fidelity"). DECISION NEEDED: keep the polished Arial Epic look (most realistic, matches "as-exact-to-Epic" goal) OR switch to Courier New monospace (matches the stated house convention). Flag for Alexander; default to whichever the example world-level files actually use.
5. **Authentic clinical writing is terse and abbreviation-heavy.** Engineering files 4-10x too long is a known failure pattern; keep notes concise.

Workflow nuance (important): per the guide, the writer curates **template/reference files with generic descriptive names, no datestamps** (e.g., `Office_Visit_Note.docx`, `Echocardiogram_Report.docx` as seen in the example DataBank folder), and **engineering's pipeline generates the actual synthetic files** with EMR (Epic/Cerner) formatting and the synthetic banner at Step 7. So heavy Epic styling by us is optional for *template* rows (engineering reformats), but is required for **writer-produced files** that bypass engineering (handwritten lists, images, audio, etc.). Decide per row whether each FI file is a template (engineering formats) or writer-produced (we finalize, banner included).

## 1. Facility & global identity

- Fictional facility: **Mercy Vale Regional Medical Center** (use consistently; change once here if desired).
- Encounter identifiers (fictional, reuse across files so they cross-reference): MRN **KM-6427819**; CSN (encounter/contact serial) **CSN-204418827**; FIN/Account **FIN-7740552**; Unit **5 West Medicine**, Room/Bed vary by note where supported, else "5W".
- Admit date 05/18/2026; world close HD6 05/23/2026 18:00. Hospital Day (HD) per note date.

## 2. Page setup & typography (exact)

- Page: US Letter, portrait (landscape only for wide flowsheets/MAR if columns wrap). Margins: 0.6" top/bottom, 0.7" left/right.
- **Body font: Arial 9.5 pt**, black `#000000`, line spacing 1.05, space-after 4 pt. (Arial = closest to Epic Hyperspace printout.)
- **Section headers: Arial Bold 10 pt**, color `#1F3864` (Epic navy), Title Case or ALL CAPS, with a 0.5 pt bottom rule in `#BFBFBF` spanning the text width.
- **Note title: Arial Bold 13 pt** `#1F3864`.
- Banner name: Arial Bold 12 pt `#1F3864`; banner field labels Arial Bold 8 pt `#595959`; banner values Arial 8.5 pt black.
- Tables: Arial 8.5 pt; header row fill `#DCE6F1` (light Epic blue), bold; body borders 0.5 pt `#BFBFBF`. Dense flowsheets may drop to 8 pt.
- Accent palette: navy `#1F3864`, Epic light blue `#DCE6F1`, banner gray-blue `#EDF1F7`, rule gray `#BFBFBF`, muted label gray `#595959`.

## 3. Shared chrome (every note)

### 3.1 Facility band (top, full width)
Thin band: left = **MERCY VALE REGIONAL MEDICAL CENTER** (bold navy 9 pt); right = "Confidential - Generated [Filed date/time]" (gray 7.5 pt). 0.5 pt bottom rule.

### 3.2 Patient header banner ("storyboard")
A light-blue-gray (`#EDF1F7`) bordered box. Layout:
- Row 1 (spanning): **KORVIN MERROW** (bold navy 12 pt)  -  right-aligned: **MRN KM-6427819**
- Grid below (4-column: Label / Value / Label / Value), 8 pt labels, fields:
  `DOB 02/18/1964 (62 yo) | Sex Male` - `Code Status Full Code` - `Allergies Lisinopril (cough)` - `CSN CSN-204418827` - `Admit 05/18/2026` - `Hospital Day HD#` - `Attending Elian Vossmere, MD` - `Location 5 West Medicine` - `Service Hospitalist`
- Pull every value from the file's metadata header; omit fields a given note type doesn't carry.

### 3.3 Note title + filing metadata
- Title line: note-type name (e.g., "History & Physical", "ED Triage Note", "Progress Note (APSO)", "Nephrology Consultation").
- Filing line (gray 8 pt): `Author: <name, credential> | Service: <service> | Date of Service: MM/DD/YYYY HHMM | Filed: <same/after> | Status: Signed`.

### 3.4 Signature block (end of note)
- Rule, then: `Electronically signed by <Author Name, Credential> on MM/DD/YYYY HHMM` (italic 9 pt).
- Add a cosign line only where clinically appropriate (resident note -> "Cosigned by <Attending>, MD").

### 3.5 Page header/footer (running)
- Header (every page after 1, 7.5 pt gray): `Korvin Merrow - MRN KM-6427819 - DOB 02/18/1964 - CSN-204418827`.
- Footer: left = facility + note type; center = "CONFIDENTIAL"; right = `Page X of Y`.

## 4. Note-type body skeletons (map each FI file)

Each maps a locked FI file to its Epic note type and section order. Fill sections from the file; keep the file's own headings' content but re-label to Epic-standard section names.

| File | Epic note type | Body sections (in order) |
|---|---|---|
| FI-W01 | **ED Triage Note** (nursing) | Chief Complaint - Mode of Arrival - **ESI Acuity** - Triage Vitals (flowsheet table; values only if in file, else "see flowsheet") - Triage Assessment - Allergies - Reported Meds (unverified) |
| FI-W02 | **ED Provider Note** | HPI - ROS - Exam - ED Course - MDM/Impression - Disposition |
| FI-W03 | **History & Physical** | Reason for Admission - HPI - Baseline Functional/Cognitive Status - Past Medical History - Surgical/Procedural History - Home Medications (table, status=Unverified) - Allergies - Physical Exam (or "deferred/see flowsheet") - Assessment & Plan (numbered problem list) - Admission Reasoning |
| FI-W04 | **Medication Reconciliation Note** (Pharmacy) | Source of History - Home Medication List (table: Med/Dose/Route/Freq/Source/Status) - Discrepancies & Uncertainties - Reconciliation Actions/Recommendations |
| FI-W05 | **Pharmacy Refill History Report** | Pharmacy/Source - Fill History (table: Med/Last Fill/Days Supply/Pattern) - Adherence Notes |
| FI-W06 | **Outpatient Rheumatology Correspondence** (letter style) | Letterhead (outpatient) - Re: PMR/Prednisone - History - Current Recommendation - Signature |
| FI-W07 | **Primary Care Outpatient Summary** | Problem List - Baseline Status - Chronic Meds - Follow-up Context |
| FI-W08-FI-W11 | **Progress Note (APSO)** | **Assessment & Plan (by problem)** - Subjective - Objective (vitals/labs -> "see flowsheet") - interim events |
| FI-W12 | **Results Review / Flowsheet** | Trend tables by system (renal, infection, hemodynamic) - table-heavy, landscape if needed |
| FI-W13 | **Medication Administration Record (MAR)** | MAR grid: Med/Scheduled/Given/Held + action notes (landscape) |
| FI-W14-FI-W16 | **Consultation Note** (Nephro/Cardio/Endo) | Reason for Consult - HPI/Pertinent History - Exam/Data - Impression - Recommendations |
| FI-W17 | **Nursing Flowsheet / Observation Notes** | Shift assessments table - narrative observations |
| FI-W18-FI-W19 | **PT / OT Evaluation** | Reason for Referral - Objective Measures - Assessment - Functional Recommendations / D/C needs |
| FI-W20 | **Care Conference / Family Communication Note** | Participants - Family-Reported Baseline - Concerns - Plan/Disposition discussion |
| FI-W21 | **Case Management / SW Note** | Insurance/Disposition - Home Support - Barriers - Plan |
| FI-W22 | **Discharge Planning Snapshot** | Summary of Course - Current Status - Proposed Plan - Pending Items (intentionally reassuring-but-incomplete) |
| FI-S01-FI-S02 | **Provenance Summary** (background) | Source - Summary - Relevance (marked supplementary) |
| FI-S03 | **Home Support / Equipment Reference** | Equipment/Services list - Logistics |
| FI-S04 | **Problem List / Past History Snapshot** | Problem list table - history snapshot |

## 5. Shared table styles
- **Vitals/flowsheet:** time across columns OR rows; header fill `#DCE6F1`; numeric cells right-aligned; only populate cells that exist in the file.
- **Medications:** columns Medication | Dose | Route | Frequency | Source | Status. For admission/med-rec notes, Dose/Freq = blank or "Unverified" unless the value is canon - this is authentic and respects the no-invented-value rule.
- **Problem list / A&P:** numbered, bold problem name, indented plan beneath.

## 6. Build method
- Build with **python-docx** for cell-level control of banner, shading, borders, and signature; one parametric builder function consumes a locked FI `.md` and emits the Epic DOCX.
- Parse the FI file's metadata header (File ID, Date/Anchor, Author/Source, etc.) to populate the banner and filing line; map the file's `##` sections to the Epic skeleton (section 4).
- After save, run the integrity gate (opens in python-docx; `styles.xml` present; ZIP EOCD present) and render to PDF with LibreOffice for visual check. Do the authoritative build in the real git environment (the sandbox mount has served truncated copies).
- Output to `02_template-reference-files/world-level/` and `/supplementary/`, overwriting the plain pandoc versions.

## 7. Guardrails
- No invented clinical values (see section 0.1). No Epic logos/trademarks. No new clinical facts beyond the locked file. Supplementary (FI-S) clearly marked supplementary/background. Keep prednisone dose/taper ambiguous wherever it appears.

## 8. Status
Design v1. One rendered sample (FI-W03 H&P) accompanies this spec for visual approval before mass application to all 26 files.
