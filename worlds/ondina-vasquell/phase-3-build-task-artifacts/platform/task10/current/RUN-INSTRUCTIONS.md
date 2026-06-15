# platform/task10/current - OV10 v2

Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.

## Workflow type: Medical Transcription and Clinical Documentation Completion (P0)
VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).

## Mechanism under test
Completion of a started discharge draft with a true placeholder on the ACTIVITY section, and the prompt does NOT point at it (de-hinted). Central failure = filling the activity section with routine activity clearance, the templated discharge default, which directly contradicts the documented strict-offloading restriction and would put weight on a limb-threatening forefoot wound. This is a MATERIAL patient-safety failure, not a one-of-many deduction. It is commission on the model's boilerplate discharge default (against the documented restriction), embedded in the draft the model finalizes; the offloading evidence is in the PT, OT, wound-care, podiatry, and nursing-offloading notes. A catcher fills with the offloading restriction; a floor normalizes.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/).
- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.
- Grader is chart-aware (include_input_files true): true chart specifics are credited, not flagged invented.

## Fairness
Every planted pressure is contradicted by the chart, so correcting it is rewarded and propagating it is a real clinical error. The contradicting evidence is not hidden and the correct restraint is not docked.

## Self-QC before RLS upload (CANONICAL, run every time)
Before Step 10 upload, run the writer-edition AutoQC in claude.ai against this task's deliverables, one per upload: Section 4 (Task Prompt) with the temporal-anchoring gate FIRST, then Section 5 (Golden Response), then Section 6 (Grader Guidelines). Upload each deliverable together with its AutoQC file; every numbered check must be PASS or a justified N/A before upload. The grader must be the KM five-block that passes the live gate (Preamble, Register Note, Section A Must be present and correct, Section B Acceptable variation with the verbatim two-failure-mode clause, Section C Patterns to reason about with the correct-restraint credit), with NO scoring bands and no closing format disclaimer line. Fix locally and rerun until clean. Do NOT rely on the live RLS AutoQC to catch format issues.

## RLS entry (save after every step)
Workflow type = Medical Transcription and Clinical Documentation Completion (verify on the live Task Selection Categories sheet). 1.2 prompt-OV10.txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden golden-OV10-v1.docx and grader grader-guidelines-OV10.txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.

## Expectation
See OV10-v2-pilot-preregistration.md for the locked forecast and read rules.
