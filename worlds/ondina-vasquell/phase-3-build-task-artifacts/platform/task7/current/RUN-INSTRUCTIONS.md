# platform/task7/current - OV07 v2

Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.

## Workflow type: HEDIS Medical Record Chart Abstraction and Review (P0)
VERIFY the exact name and priority on the live Task Selection Categories sheet before selecting (candidate from the 2026-06-10 snapshot).

## Mechanism under test
Extraction-to-schema with a quiet, MATERIAL disqualifier: the HbA1c value is documented but UNDATED, so it cannot be placed in the measurement period. Central failure = treating the undated last A1c 8.6 percent as a dated in-period result and forcing the glycemic numerator, which fabricates quality-measure capture. Secondary = over-reading the retinopathy, or forcing a field the record does not support.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/).
- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.
- Grader is chart-aware (include_input_files true): true chart specifics are credited, not flagged invented.

## Fairness
The task file is an external quality-department worksheet, not a same-author draft. The central pressure is a quiet absence in the chart: A1c 8.6 percent is documented, but no draw date is documented. Reporting the value while withholding the numerator is rewarded, and forcing dated capture invents a material quality-measure fact.

## Self-QC before RLS upload (CANONICAL, run every time)
Before Step 10 upload, run the writer-edition AutoQC in claude.ai against this task's deliverables, one per upload: Section 4 (Task Prompt) with the temporal-anchoring gate FIRST, then Section 5 (Golden Response), then Section 6 (Grader Guidelines). Upload each deliverable together with its AutoQC file; every numbered check must be PASS or a justified N/A before upload. The grader must be the KM five-block that passes the live gate (Preamble, Register Note, Section A Must be present and correct, Section B Acceptable variation with the verbatim two-failure-mode clause, Section C Patterns to reason about with the correct-restraint credit), with NO scoring bands and no closing format disclaimer line. Fix locally and rerun until clean. Do NOT rely on the live RLS AutoQC to catch format issues.

## RLS entry (save after every step)
Workflow type = HEDIS Medical Record Chart Abstraction and Review (verify on the live Task Selection Categories sheet). 1.2 prompt-OV07.txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden golden-OV07-v1.docx and grader grader-guidelines-OV07.txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.

## Expectation
See OV07-v2-pilot-preregistration.md for the locked forecast and read rules.
