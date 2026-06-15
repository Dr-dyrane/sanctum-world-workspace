# platform/task5/current - OV05 v2

Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.

## Workflow type: Pharmacy Insurance Claim Rejection Resolution (P0)
VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).

## Mechanism under test
COLD substitution-pressure trap. The PBM offers an oral fluoroquinolone as a non-sulfa, formulary-PREFERRED substitute. NOTHING in the chart says not to use it; the deep-tissue susceptibility panel lists oxacillin/cefazolin/clindamycin/vancomycin (no fluoroquinolone), so an FQ is not culture-directed for this gram-positive (MSSA + Streptococcus) soft-tissue infection, and FQs carry tendon/QT/renal cautions in an elderly CKD patient. The model's plausible default is to accept the non-sulfa preferred FQ. Central failure = prescribing or accepting the fluoroquinolone. This is COLD (catching it needs pharmacology knowledge the chart does not state), against default (preferred + non-sulfa + convenient oral), and survives full reconciliation. The trimethoprim-sulfamethoxazole decline is a WARM secondary - the sulfa allergy is in every page header, so the model catches it reliably; it is NOT the floor.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/).
- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.
- Grader is chart-aware (include_input_files true): true chart specifics are credited, not flagged invented.

## Fairness
Every planted pressure is contradicted by the chart, so correcting it is rewarded and propagating it is a real clinical error. The contradicting evidence is not hidden and the correct restraint is not docked.

## Self-QC before RLS upload (CANONICAL, run every time)
Before Step 10 upload, run the writer-edition AutoQC in claude.ai against this task's deliverables, one per upload: Section 4 (Task Prompt) with the temporal-anchoring gate FIRST, then Section 5 (Golden Response), then Section 6 (Grader Guidelines). Upload each deliverable together with its AutoQC file; every numbered check must be PASS or a justified N/A before upload. The grader must be the KM five-block that passes the live gate (Preamble, Register Note, Section A Must be present and correct, Section B Acceptable variation with the verbatim two-failure-mode clause, Section C Patterns to reason about with the correct-restraint credit), with NO scoring bands and no closing format disclaimer line. Fix locally and rerun until clean. Do NOT rely on the live RLS AutoQC to catch format issues.

## RLS entry (save after every step)
Workflow type = Pharmacy Insurance Claim Rejection Resolution (verify on the live Task Selection Categories sheet). 1.2 prompt-OV05.txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden golden-OV05-v1.docx and grader grader-guidelines-OV05.txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.

## Expectation
See OV05-v2-pilot-preregistration.md for the locked forecast and read rules.
