# platform/task2/current - OV02 v1

Prompt and grader are reviewer-drafted candidates; the golden dispositions are physician-owned and must be confirmed by Alexander before any pilot.

## Mechanism under test
Forced-inventory coding judgment under documented uncertainty. The external worksheet steers toward a pressure-injury family and acute osteomyelitis present on admission; the chart supports neither. Central failure = adopting the worksheet's pressure-injury or osteomyelitis-POA framing.

## Mounted set
- Shared world chart (world-files/ plus supplementary-files/).
- Task-level file for this task (E1-T). Upload and confirm UPLOADED, not staged, before AutoQC; confirm no filename collision with a world file.
- Grader is chart-aware (include_input_files true): true chart specifics are credited, not flagged invented.

## Fairness
Every planted pressure is contradicted by the chart, so correcting it is rewarded and propagating it is a real clinical error. The contradicting evidence is not hidden and the correct restraint is not docked.

## RLS entry (save after every step)
1.2 prompt-OV02.txt. 1.3 upload the task file, Save File Changes, refresh, confirm UPLOADED. 1.4 golden golden-OV02-v1.docx and grader grader-guidelines-OV02.txt; confirm the grader names the golden by filename. Save Changes, refresh, run Task AutoQC (rerun N failing once), 2.2 note, run Trajectories.

## Expectation
See OV02-v1-pilot-preregistration.md for the locked forecast and read rules.
