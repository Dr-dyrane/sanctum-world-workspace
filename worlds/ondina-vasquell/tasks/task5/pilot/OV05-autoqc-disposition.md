# OV05 FA/GA AutoQC disposition (2026-06-18)

AutoQC: Fail 1/5. Flag: "FA Root Cause and Citations." Two rounds.

## Round 1 (two sub-points)
1. Specific sections. FIXED in the FA: it now cites the consult's Wound Assessment (red granulation, scant serous exudate) and Plan (daily moist dressing), Olwyn CWOCN 05/20, plus the note's Objective. The round-2 flag confirms the citation is accepted and does not re-raise it.
2. Cross-batch dressing (Dakin's vs silver alginate). JUSTIFIED, see below.

## Round 2 (sharpened to one claim)
Flag asserts the FA "misidentifies what is partly a task-design / world-file inconsistency as a straightforward agent failure," because batch c2e4161d graded a Dakin's/povidone/wet-to-dry order while batch 76d06fb2, the golden, and the rubric grade silver alginate.

## Disposition: JUSTIFY (FA is correct, unchanged). Verified facts:

1. The analyzed run is internally consistent. In job 76d06fb2 the mounted dressing order (wound_care_dressing_order_05242026.docx), the golden (golden-OV05.docx), and grader-guidelines-OV05.txt all specify the silver alginate + absorbent foam order. Trajectory 7 saw that order and carried it forward onto a clean low-exudate granulating bed. It was never graded against a dressing it did not see. Verified: grep of task5/current shows no Dakin's/povidone/wet-to-dry in any mounted artifact (only in this prereg and RUN-INSTRUCTIONS, which are provenance notes, not model-facing).

2. c2e4161d is the superseded v2 build, not a second grading of this task. v2 planted Dakin's wet-to-dry; it ceilinged 0.72 to 0.92 (the cytotoxic order is too obvious), so it was re-rolled to the current v3 silver-alginate build (76d06fb2). Two versions in two separate jobs. Commits: f85d499 (v2 Dakin's), 1fae960 (v3 silver alginate).

3. Not a world-file inconsistency. The v2-to-v3 change is entirely task-layer (the dressing order, golden, grader). The 34 world files and their generator clinical_data.py (which authors the CWOCN consult) last changed at d75b171, the parent of both builds, so they are identical across both batches. The bed the FA cites (Olwyn CWOCN, 05/20, Wound Assessment) is the same in both.

4. No low score is a task-design artifact. The Dakin's golden existed only in c2e4161d, the silver-alginate golden only in 76d06fb2. No trajectory was graded against a mismatched golden.

Conclusion: the agent-versus-task-design distinction is made. Within the analyzed batch there is no task-design failure, and the FA correctly attributes the failure to the agent. Housekeeping: submit only the v3 job (76d06fb2); discard the superseded v2 round (c2e4161d) if it is still attached to this task slot. Provenance also in the FA Status line and pilot/OV05-v2-dakins-ceiling-2026-06-18-job-c2e4161d.md.
