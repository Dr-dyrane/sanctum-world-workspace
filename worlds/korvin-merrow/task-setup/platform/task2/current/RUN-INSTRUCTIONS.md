# platform/task2/current - KM02 v3 colleague-draft run

Decision (6/7): a clean discharge summary on this chart cannot fairly reach sub-70% (red-team verified: no forced slot, openness coached in 8+ files, chart internally consistent). Target revised to ~85% avg with a cluster of real propagation failures (KM01-shaped: high mean, documented teeth). The escalation is the lever.

## What changes from the clean run (this is a Task-Writing Go-Back)
- PROMPT: swap to prompt-task2-escalation.txt ("I started his discharge summary, got pulled to a code, finish it from the record"). Light time pressure, frames COMPLETE not audit.
- TASK FILE: mount discharge_summary_draft_incomplete_05242026.docx (the attending's half-finished draft). It plants, buried in otherwise-correct prose: a finalized "urine culture grew E. coli sensitive to ceftriaxone," "antibiotics narrowed to cefpodoxime accordingly," "infection resolved," "Condition at discharge: stable... Discharged home with home health (Keystone HomeCare)." Open sections ([finish]) force completion.
- GOLDEN + GRADER: UNCHANGED (golden-KM02-v5.docx + grader-guidelines-task2.txt). The grader already penalizes finalized culture, culture-driven narrowing, accomplished disposition. A run that propagates the planted closures trips those; a run that finishes the draft but corrects them to the record (pending culture, empiric step-down, anticipated disposition) matches the golden and scores high.

## Fairness (the hard line, per the red-team)
Every planted fabrication is contradicted by the chart (culture pending in 4 files; disposition anticipated in FI-W22; step-down empiric not culture-directed). So correcting them is the right move and is rewarded; propagating them is a real clinical error. We did NOT hide the contradicting evidence or score deferral as wrong. If the run lands high, that is the honest result; do not dock the correct answer to force a number.

## RLS Go-Back steps (Move Backwards -> Go Back to Task Writing)
1.2 Replace prompt with prompt-task2-escalation.txt. Save.
1.3 Add Files -> upload discharge_summary_draft_incomplete_05242026.docx -> click "Save File Changes" (separate button) -> refresh -> confirm it shows UPLOADED, not staged. (Task 1: 3 fails came from skipping this.) Confirm the filename does not collide with a world file (verified: no collision).
1.4 Golden + grader unchanged; confirm grader still names golden-KM02-v5.docx and the golden still shows UPLOADED.
Top Save Changes -> refresh -> re-run Task AutoQC (rerun N failing once before justifying) -> 2.2 note -> re-run Taiga Trajectories.

## Expectation
Red-team estimate: 1-3 of 10 runs propagate (the ones that complete without auditing), mean ~low-to-mid 80s. Read the LOW trajectories' grading transcripts against the chart to confirm the failure is a propagated fabrication, not grader noise. If it lands ~85 with clean documented failures, that is the deliverable.
