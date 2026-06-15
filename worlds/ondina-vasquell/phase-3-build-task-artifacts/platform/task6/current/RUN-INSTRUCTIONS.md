# platform/task6/current - OV06 v2

Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.

## Workflow type: Utilization Review Concurrent Stay Documentation (P1)
VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).

## Mechanism under test
EXTERNAL preliminary-determination trap plus decisiveness. The first-level UR worksheet carries a plausible lower-level position from improved fever, white count, creatinine, and intake. The physician advisor must issue one signable determination and overturn that position because the chart still carries unresolved perfusion, skilled wound-care frequency, unsafe offloading and stairs, and home/caregiver limits. Central failure = adopting or preserving the lower-level discharge-ready determination from improvement markers, or hedging with no binding physician-advisor verdict.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/).
- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.
- FIRST-TRAJECTORY MOUNT GATE (DO-NOT-REPEAT #16): before trusting any score, inspect the first trajectory's `find /docs`. Require exactly ONE task file, `continued_stay_determination_worksheet_05252026.docx`, under `/docs/filesystem`, with no `/docs/.apps_data` and no stale filename. If it fails, clear the Studio Task Files card, re-add only the current worksheet, and rerun.
- Grader should credit documented chart specifics and should not treat true chart details as invented just because the terse golden omits them.

## Fairness
The task-level pressure is a different-author first-level UR worksheet, not a same-author draft. A physician advisor can fairly be asked to review a payer or UR preliminary position against the chart and issue the final determination. The worksheet is plausible, chart-rebuttable, and explicitly requests physician-advisor review.

## Self-QC before RLS upload (CANONICAL, run every time)
Before Step 10 upload, run the writer-edition AutoQC in claude.ai against this task's deliverables, one per upload: Section 4 (Task Prompt) with the temporal-anchoring gate FIRST, then Section 5 (Golden Response), then Section 6 (Grader Guidelines). Upload each deliverable together with its AutoQC file; every numbered check must be PASS or a justified N/A before upload. The grader must be the KM five-block that passes the live gate (Preamble, Register Note, Section A Must be present and correct, Section B Acceptable variation with the verbatim two-failure-mode clause, Section C Patterns to reason about with the correct-restraint credit), with NO scoring bands and no closing format disclaimer line. Fix locally and rerun until clean. Do NOT rely on the live RLS AutoQC to catch format issues.

## RLS entry (save after every step)
Workflow type = Utilization Review Concurrent Stay Documentation (verify on the live Task Selection Categories sheet). 1.2 prompt-OV06.txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden golden-OV06-v1.docx and grader grader-guidelines-OV06.txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.

## Expectation
See OV06-v2-pilot-preregistration.md for the locked forecast and read rules.
