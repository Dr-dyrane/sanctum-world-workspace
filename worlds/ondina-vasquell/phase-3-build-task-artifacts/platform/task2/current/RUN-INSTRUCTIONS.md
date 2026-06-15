# platform/task2/current - OV02 v4

Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.

## Workflow type: Inpatient Medical Coding and DRG Assignment (P0)
VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).

## Mechanism under test
EMBEDDED wrong-principal sequencing (KM09 lever, AKI substrate, de-duplicated from KM09 sepsis and from OV03 osteo). The external HIM working-DRG worksheet PRE-SEQUENCES acute kidney injury on chronic kidney disease as the principal diagnosis with a renal failure DRG and demotes the limb-threat diabetic foot infection to a secondary. The physician finalizing must CATCH and RE-SEQUENCE the foot infection as principal (the condition that occasioned the admission) and decline the renal DRG. Central failure = attesting or propagating the embedded acute kidney injury principal and renal DRG. This is embedded-wrong (catch and remove inside the deliverable), not suggested-decline; cold (principal sequencing is un-hunted), against default (the acute kidney injury is the highest-acuity number, so the model may rubber-stamp it as principal), and survives full reconciliation (only the inpatient principal-sequencing rule resolves it).

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/).
- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.
- Grader is chart-aware (include_input_files true): true chart specifics are credited, not flagged invented.

## Fairness
Every planted pressure is contradicted by the chart, so correcting it is rewarded and propagating it is a real clinical error. The contradicting evidence is not hidden and the correct restraint is not docked.

## Self-QC before RLS upload (CANONICAL, run every time)
Before Step 10 upload, run the writer-edition AutoQC in claude.ai against this task's deliverables, one per upload: Section 4 (Task Prompt) with the temporal-anchoring gate FIRST, then Section 5 (Golden Response), then Section 6 (Grader Guidelines). Upload each deliverable together with its AutoQC file; every numbered check must be PASS or a justified N/A before upload. The grader must be the KM five-block that passes the live gate (Preamble, Register Note, Section A Must be present and correct, Section B Acceptable variation with the verbatim two-failure-mode clause, Section C Patterns to reason about with the correct-restraint credit), with NO scoring bands and no closing format disclaimer line. Fix locally and rerun until clean. Do NOT rely on the live RLS AutoQC to catch format issues.

## RLS entry (save after every step)
Workflow type = Inpatient Medical Coding and DRG Assignment (verify on the live Task Selection Categories sheet). 1.2 prompt-OV02.txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden golden-OV02-v1.docx and grader grader-guidelines-OV02.txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.

## Expectation
See OV02-v4-pilot-preregistration.md for the locked forecast and read rules.
