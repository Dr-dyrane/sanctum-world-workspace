# Korvin Merrow World Spec DOCX - Full Audit, Provenance Fix, and Codex Finish Plan

> **COMPLETION NOTE (2026-06-04, Claude):** Visual Fidelity + final Voice pass APPLIED directly to `korvin-merrow-final-submission-staging/01_spec-document/Korvin_Merrow_World_Spec.docx` on top of Codex's `fd02da0` regeneration. Changes (formatting only, zero content/canon changes): all font sizes normalized to template baseline (8 pt body/tables x647, 10 pt Patient Profile + title metadata x24, 16 pt title x1; eliminated all 6/6.5/7.5 pt runs); all 138 black table borders -> template hairline single 0.5 pt `CCCCCC`; fill `D9EAF7` -> template `D6E4F0`; title block restyled from solid-blue/white-text band to the template's light-blue `D6E4F0` card with `4472C4` title and gray metadata; final voice residual removed ("Korvin Merrow tests whether a clinician can manage a familiar..." -> "Korvin Merrow presents a familiar..."). Verified: opens in python-docx, EOCD present, renders to PDF (11 pp), page-1 visually matches template identity. Headings were already template Heading 1/2 styles; Section 1 retains exactly five H2 subsections; med list is a 1.2 sub-table. PENDING: git commit in real environment ("checkpoint: world spec visual fidelity and voice final pass") and Word-open spot-check by Alexander. World Spec is otherwise COMPLETE for pre-AutoQC purposes; focus moves to reference files.
>
> **ROUND-2 ADDENDUM (same date):** Second template comparison closed the remaining deltas: margins corrected to template 1080 twips; template "Terminology: Traps vs. Frictions" and "Self-Containment Principle" callout boxes grafted verbatim from template XML (correct placement: end of 1.5 and end of Section 4; green palette restored). The two authoring-instruction callouts ("Optional Sections", "Additional Tasks") were intentionally omitted as writer-guidance furniture. Two blank pages (after Section 3 and trailing) removed via empty-paragraph cleanup; Heading 1 pageBreakBefore is template-native behavior and retained. Final: 11 pages, zero blank pages, opens cleanly, EOCD intact, 26 tables, 87 paragraphs. Commit note for Codex: "checkpoint: world spec template-fidelity round 2 (callouts, margins, pagination)".

Date: 2026-06-03
Status: ACTIONABLE PLAN (no locked canon modified; no doses asserted as canon)
Owner of clinical sign-off: Alexander (physician source of truth)
Executor: Codex (real git environment)

---

## 0. TL;DR

The World Spec content is strong and structurally close. Exactly **one blocking issue** stands between it and 9/10 submission-grade: the medication table contains **7 doses that were invented at build time** and do not trace to physician-approved canon. This plan (a) audits the full document, (b) **solves** the provenance gap by reducing it to a one-pass physician approval sheet with safe standard defaults, and (c) gives Codex an ordered, deterministic finish sequence with a hard "no unsourced dose" guardrail and a file-integrity gate (the DOCX has twice been saved corrupt/truncated).

Definition of done: a DOCX that opens in Word, renders to PDF, uses the official template's styles, contains only canon-or-approved clinical specifics, and passes the acceptance checklist in section 6.

---

## 1. Audit - current state (reconciled from Claude + Codex reviews)

### Matches / strong (keep)
- All canonical sections present: 1 Clinical Scenario, 2 Task Specifications, 3 World File Plan, 4 World Summary.
- Patient profile, medication table, milestone table, trap/friction tables, six task blocks, and 7-column file-plan tables all present and readable (landscape file plan acceptable per AutoQC when tables would wrap).
- Six tasks, no TP-KM07 invented; FI-T07 correctly described as a medication-safety addendum to Task 1.
- File plan complete and correct: FI-W01-22 (22), FI-T01-07 (7), FI-S01-04 (4); no duplicate IDs, no missing rows, supplementary marked non-load-bearing.
- Source fidelity (non-medication): no altered dates, task count, traps, frictions, or source hierarchy; prednisone ambiguity preserved; no hidden adrenal-insufficiency reveal; no post-world leakage; no golden/grader/scoring/AutoQC/manifest leakage.
- Stacey carry-overs resolved: fictional name, World Type declaration, comorbidity burden (14), discharge-source-hierarchy / FI-W22 visible-but-incomplete rule.

### Blocking defect
- **B1 - Invented medication doses (provenance).** The locked architecture has 20 medication *names* but only 12 physician-approved *doses* (+ prednisone intentionally ambiguous). The build filled the remaining 7 with plausible-but-unsourced dose/frequency values. This is the recurring "polished output with silent invented clinical specificity" failure mode. **Must be closed before submission.** Solved in section 2-section 3.

### Major (fix in regen)
- **M1 - File integrity.** The artifact has repeatedly been saved truncated/corrupt (missing `styles.xml`, `numbering.xml`, and the ZIP end-of-central-directory). My sandbox currently still reads a 25,042-byte unopenable copy. Any regen MUST be verified openable. See section 4 guardrail G3.
- **M2 - Section renumbering vs official template.** Current doc inserts `1.3 Home Medication List` and renumbers Clinical History->1.4, Key Milestones->1.5, Complexity->1.6. Official template is 1.1 Big Picture, 1.2 Patient Profile, 1.3 Clinical History, 1.4 Key Milestones, 1.5 Complexity. Decide: keep the medication list inside 1.2/1.3 to preserve official numbering, OR keep the dedicated subsection and accept the deviation (examples do front-load meds, so a labeled medication block is defensible - but do not silently renumber the canonical five subsections).
- **M3 - Draft prompts not naturalistic / telegraph traps.** Task draft prompts reproduce the full multi-bullet TP-KM request and enumerate trap domains (e.g., "Inpatient-only medication actions that must not be converted..."). Template requires short, natural end-user prompts. Rewrite each as 1-3 sentence natural messages; keep the detailed reasoning only in Expected Output / Failure Design.

### Minor (polish)
- **P1 - Workspace register leaks** in final-facing prose: "four locked workflows," "v1 submission candidate," and a file-plan description copied verbatim from the inventory ("...without creating values in this artifact"). Strip these.
- **P2 - Over-architectural clinical voice.** Phrases like "designed source-of-truth problem," "trap architecture," "agent/model" are fine inside Failure Design but should be removed from Sections 1.x so the clinical scenario reads physician-authored.
- **P3 - Visual verbatim-ness.** Move toward template header blue `4472C4` and black borders; lift table body type from 6-7 pt to ~8 pt (7 pt only for the densest file-plan tables); prose ~9-10 pt. Current gray-bordered/dark-blue look is clean but not verbatim.
- **P4 - Totals line format.** Use the template's "Total file count: 22 + 7 + 4 = 33 unique files" form.

---

## 2. The fix in principle

Rule to adopt permanently: **No dose, route, frequency, strength, or numeric clinical value enters a submission artifact unless it traces to (a) physician-approved canon, or (b) an explicit, signed approval in this sheet. Intentionally ambiguous values (prednisone) stay ambiguous.**

The provenance gap is closed in two steps:
1. Lock the 12 already-approved doses unchanged.
2. Convert the 7 invented values into **proposed standard defaults flagged for Alexander's one-pass approval** (section 3). These are conservative, guideline-standard, CKD3-appropriate values - chosen so Alexander can most likely approve as-is, but he may correct any cell. Nothing is asserted as canon until he signs.

---

## 3. Medication Dose Approval Sheet (the deliverable that solves B1)

Patient context for dosing judgment: 62 M, CKD stage 3 (baseline Cr 1.6-1.8, eGFR ~40-50), HFrEF/CAD, T2DM, chronic prednisone for PMR.

Legend - Source:
- **CANON** = physician-approved in `remediation/reviewer-remediation-compliance-review.md` (do not change).
- **AMBIGUOUS** = intentionally unfixed (Trap #1); must stay non-specific.
- **NEEDS APPROVAL** = proposed standard default; Alexander approves or corrects before build.

| # | Medication | Proposed dose | Route | Frequency | Indication | Source |
|---|---|---|---|---|---|---|
| 1 | Aspirin | 81 mg | PO | Daily | CAD secondary prevention | CANON |
| 2 | Atorvastatin | 40 mg | PO | Nightly | CAD / hyperlipidemia | CANON |
| 3 | Sacubitril/valsartan | 24/26 mg | PO | BID | HFrEF GDMT (post ACE-I intolerance) | CANON |
| 4 | Carvedilol | 12.5 mg | PO | BID | HFrEF / CAD | CANON |
| 5 | Furosemide | 40 mg | PO | Daily | HFrEF volume management | CANON |
| 6 | Spironolactone | 25 mg | PO | Daily | HFrEF MRA (K+/renal sensitive) | CANON |
| 7 | Empagliflozin | 10 mg | PO | Daily | HFrEF / T2DM | CANON |
| 8 | Metformin ER | 500 mg | PO | BID | T2DM (renally sensitive) | CANON |
| 9 | Insulin glargine | 18 units | SC | Nightly | T2DM basal | CANON |
| 10 | Gabapentin | 300 mg | PO | Nightly | Diabetic neuropathy (renally dosed) | CANON |
| 11 | Ferrous sulfate | 325 mg | PO | Every other day | Anemia of CKD | CANON |
| 12 | Alendronate | 70 mg | PO | Weekly | Steroid-related osteoporosis | CANON |
| 13 | Prednisone | (do NOT state a fixed dose) | PO | (uncertain / tapering) | PMR; recent taper, inconsistent records | AMBIGUOUS - keep |
| 14 | Calcium carbonate / vitamin D | 600 mg / 400 IU | PO | BID | Steroid bone protection | NEEDS APPROVAL (canon approved "daily" only, no strength) |
| 15 | Cholecalciferol (vit D3) | 1000 IU | PO | Daily | Vitamin D supplementation | NEEDS APPROVAL + **reconcile redundancy with #14** |
| 16 | Nitroglycerin | 0.4 mg | SL | 1 tab q5min PRN chest pain, max 3 | CAD angina rescue | NEEDS APPROVAL |
| 17 | Acetaminophen | 650 mg | PO | q6h PRN, max 3 g/day | Pain (hepatically capped for age) | NEEDS APPROVAL |
| 18 | Pantoprazole | 40 mg | PO | Daily | GERD / acid suppression | NEEDS APPROVAL |
| 19 | Polyethylene glycol 3350 | 17 g | PO | Daily PRN | Chronic constipation | NEEDS APPROVAL |
| 20 | Senna | 8.6 mg | PO | Nightly PRN | Constipation | NEEDS APPROVAL |

Physician actions required (one pass):
- Approve or correct rows 14-20 (the 7 NEEDS APPROVAL rows).
- Decide row 15 vs 14: keep both (separate cholecalciferol + combo) only if intentional; otherwise drop one to avoid double vitamin D.
- Confirm prednisone stays ambiguous (no fixed mg) in the spec body, consistent with Trap #1.

Once signed, these 7 rows become canon for the build. Until signed, the build must not emit them.

---

## 4. Build guardrails (apply to every regeneration)

- **G1 - Template fidelity.** Build by filling `reference/templates/World_Spec_Template_05_06.docx` in place. Preserve `styles.xml`, `theme1.xml`, `numbering.xml`, and the template's table styles. Do not rebuild from a blank `Document()`. Do not silently renumber the five canonical 1.x subsections (resolve M2 explicitly).
- **G2 - No unsourced specifics.** Every dose/value must map to CANON or an approved row in section 3. Prednisone stays ambiguous. No invented lab values beyond what FI-W12/FI-W13 already provide.
- **G3 - File-integrity gate (hard stop).** After save, the build MUST verify the file: (a) opens in python-docx, (b) contains `word/styles.xml` and `word/numbering.xml`, (c) has a ZIP end-of-central-directory (`PK\x05\x06`). If any check fails, the file is corrupt - re-save, do not proceed. Then render to PDF with LibreOffice and open it. Note: the workspace mount has repeatedly served truncated copies into the sandbox; do the authoritative save+verify in the real git environment, not via the sandbox mount.
- **G4 - Register.** Strip workspace language (locked/ratification/candidate/"this artifact"/architecture) from Sections 1 and 4 prose; keep design language only inside Failure Design.
- **G5 - No scope creep.** No new tasks, traps, frictions, files, scoring, golden, or grader content.

---

## 5. Codex finish plan (ordered)

Do these in order; commit each as a separate checkpoint.

1. **Confirm working file + clean tree.** Verify the current `Korvin_Merrow_World_Spec.docx` opens in the real environment (G3). Confirm the previously reported corruption is sandbox-only. Resolve the lingering working-tree state (the modified DOCX + untracked Stacey recovery report) before starting.
2. **Get clinical sign-off.** Put section 3 in front of Alexander; capture approvals/corrections for rows 14-20 and the vitamin-D reconciliation. Record the signed values (e.g., append a "Physician-approved" note to this file or to the medication-expansion package as an addendum - do not silently edit locked canon; create an approval record).
3. **Regenerate the World Spec DOCX** from the official template (G1) using: `world-spec-construction/locked/world-spec-v1.md` (narrative, traps, frictions, hierarchy), `file-inventory/locked/file-inventory-v1.md` (22/7/4 rows, 7-col mapping), `task-prompts/locked/TP-KM01-06` + `expected-outputs/locked/EO-KM01-06` (but rewrite Draft Prompts naturalistic per M3), and the **approved** medication sheet from section 3. Apply M2 decision on section numbering.
4. **Apply visual verbatim pass (P3):** template header blue `4472C4`, black borders, ~8 pt table body / ~9-10 pt prose, 7 pt only for densest file-plan tables.
5. **Language pass (P1/P2):** remove workspace register and over-architectural phrasing from Sections 1 and 4.
6. **Integrity + render verification (G3):** python-docx opens; styles.xml/numbering.xml present; EOCD present; LibreOffice -> PDF; eyeball the PDF for header color, borders, density, and that no instructional placeholder text remains.
7. **Self-check against acceptance checklist (section 6).**
8. **Commit:** `checkpoint: regenerate world spec docx (approved med doses, template-verbatim, integrity-verified)`.

Reference files reminder (unchanged by this plan): 26 required uploads (22 FI-W + 4 FI-S); 7 FI-T conditional; spec references 33 total.

---

## 6. Acceptance checklist (9/10 submission-grade)

- [ ] Opens in Word; PDF renders; `styles.xml`, `numbering.xml`, EOCD all present.
- [ ] Every medication dose traces to CANON or a signed section 3 approval; prednisone ambiguous; no other invented numeric specifics.
- [ ] Official template styles used; five canonical 1.x subsections not silently renumbered; M2 decision applied.
- [ ] Six tasks, each with workflow, **naturalistic** draft prompt (no trap telegraphing), expected output, failure-design (trap+remediation), and task-level files.
- [ ] File plan: 22/7/4, 7 columns, no dup/missing IDs, supplementary marked non-load-bearing, totals line in template format.
- [ ] No workspace register or over-architectural phrasing in Sections 1 and 4.
- [ ] Header blue `4472C4`, black borders, example-like font density.
- [ ] No golden/grader/scoring/AutoQC/manifest/upload leakage.
- [ ] Stacey carry-overs all reflected (name, World Type, comorbidity, medication specificity *with provenance*, prednisone ambiguity, discharge-source hierarchy).

When every box is checked, it is submission-ready. The only item that requires someone other than Codex is the section 3 physician sign-off - that is the true critical path.
