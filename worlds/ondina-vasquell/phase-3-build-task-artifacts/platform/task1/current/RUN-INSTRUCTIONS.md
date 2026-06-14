# platform/task1/current - OV01 v2 clean-mount packet (Medication Reconciliation)

This is the current OV01 packet. V1 ceilinged. V2 added the cold enoxaparin verification-asymmetry trap, de-telegraphed the order-set filename and body, then banked on the clean-mount pilot job `741ba52f-bae9-4594-a25c-ef5ae0e8bcdc`.

## Workflow type: Medication Reconciliation at Care Transitions (P0)
REMAPPED 2026-06-13: original workflow Discharge Medication Reconciliation (hca-discharge-med-recon) was retired from the platform menu; this is the nearest open analogue. Deliverable framing may need a light adjustment to fit it. VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).

## Mechanism under test
Source-of-truth reconciliation under renal and discharge-safety constraints. The external discharge medication order set looks routine and pending physician signature, but it carries inpatient-only enoxaparin 40 mg daily into discharge. A correct reconciliation stops enoxaparin at discharge because it is not a home medication and adds bleeding risk on aspirin plus clopidogrel. It also stops inpatient broad-spectrum antibiotics, keeps metformin, empagliflozin, and lisinopril as explicit deferred restarts, avoids NSAIDs, continues home insulin with correct clarification, and restores omitted home ferrous sulfate and cholecalciferol.

Central failure = leaving enoxaparin alive as a discharge or home medication, whether signed, continued, or hedged as confirm, especially with patient-facing injection instructions.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/), which the model reads to reconcile.
- Task-level file: discharge_medication_orders_05212026.docx (E1-T1). Upload and confirm it shows UPLOADED, not staged, before AutoQC. Confirm no filename collision with a world file (verified: none).
- Grader is chart-aware (include_input_files true): the deliverable is built from the chart, so true chart specifics are credited, not flagged as invented.

## Fairness (hard line)
Every discrepancy in the order set is contradicted by the chart. The MAR supports enoxaparin only as inpatient VTE prophylaxis. The home medication list excludes it. The antiplatelet regimen makes discharge continuation clinically risky. The renal trend, hold orders, culture hierarchy, and home list support the other reconciliation moves. Correcting the order set is the right move and is rewarded; propagating it is a real clinical error.

Dirty-run caveat: job `9765ba91` is not bankable because Studio mounted two order sets, the stale old preliminary file in `/docs/filesystem` and the new file under `/docs/.apps_data/calendar`. The clean job `741ba52f` is bankable because the first trajectory showed exactly one order set, `discharge_medication_orders_05212026.docx`, under `/docs/filesystem`, no `.apps_data`, and no `preliminary`.

## Mount hygiene gate after every upload or re-pilot
Before reading any trajectory as evidence, inspect the first trajectory's `find /docs` tree.

Required:
- exactly one order-set task file
- `discharge_medication_orders_05212026.docx` under `/docs/filesystem`
- no `/docs/.apps_data`
- no `preliminary_discharge_order_set_05212026.docx`
- no duplicate same-purpose task file with a different filename

If any item fails, delete all files from the Studio Task Files card, re-add only the current file as a plain Filesystem file, save, refresh, and rerun. A rename can dodge duplicate-name AutoQC, so the mount tree is the real gate.

## Self-QC before RLS upload (CANONICAL, run every time)
Before Step 10 upload, run the writer-edition AutoQC in claude.ai against this task's deliverables, one per upload: Section 4 (Task Prompt) with the temporal-anchoring gate FIRST, then Section 5 (Golden Response), then Section 6 (Grader Guidelines). Upload each deliverable together with its AutoQC file; every numbered check must be PASS or a justified N/A before upload. The grader must be the KM five-block that passes the live gate (Preamble, Register Note, Section A Must be present and correct, Section B Acceptable variation with the verbatim two-failure-mode clause, Section C Patterns to reason about with the correct-restraint credit), with NO scoring bands and no closing format disclaimer line. Fix locally and rerun until clean. Do NOT rely on the live RLS AutoQC to catch format issues.

## RLS entry (1.1 to 1.4) - save after every step
Workflow type = Medication Reconciliation at Care Transitions (verify on the live Task Selection Categories sheet).
1.2 Prompt: prompt-OV01.txt.
1.3 Add Files: upload the order set, click Save File Changes, refresh, confirm UPLOADED.
1.4 Golden golden-OV01-v1.docx and grader grader-guidelines-OV01.txt; confirm the grader names the golden by filename and the golden shows UPLOADED.
Top Save Changes, refresh, run Task AutoQC (rerun N failing once before disputing), 2.2 note, run Taiga Trajectories.

## Expectation
Use `OV01-v2-pilot-preregistration.md` plus `phase-4-pilot-review-submit/OV01-results-and-prereg-reconciliation.md`. The locked prereg forecast matched the clean pilot. Read Attempt 3 against the chart as the FA/GA subject, and do not use the dirty duplicate-mount job for shipping evidence.
