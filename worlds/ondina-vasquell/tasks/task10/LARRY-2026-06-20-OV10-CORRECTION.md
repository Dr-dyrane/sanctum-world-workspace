# OV10 reviewer correction - Larry E, 1st review, 2026-06-20

Status: OV10 is NOT being reworked yet (Alexander's direction). This file records the correction verbatim-in-substance and the distilled principles, and drives the World 3 (Marva Lydell) safety audit at worlds/marva-lydell/docs/W3-OV10-LESSONS-AUDIT.md. Canonicalized 2026-06-20 as pod doctrine binding all worlds and tasks at reference/world-spec-guidelines/POLICY-2026-06-20-deprecated-workflows-and-task-fairness.md.

## The flag
Any task with consistent failure this low (~15%) across all ten runs is flagged as unfair. The trap and intent were understood; the issue is fairness of the failure, not effort or competence.

## The four corrections

1. Finishing a note is not a realistic workflow. Per the team leads, completing or finishing a note is not how this is done in practice: in real life a clinician either uses AI to write the whole note and then proofreads and signs it, or does not use it at all. Not a hard no, but not encouraged.

2. Do not intentionally feed the model false information. Make the task viable by providing complete notes and, where appropriate, withholding information, but planting false facts to be distrusted is discouraged. Confirming information is sometimes legitimate, but the model carrying over something that was stated in the chart should NOT, by itself, earn a 15% score. What IS fair: disagreements between consultants, accidental non-adjusted medications, accidental omissions of information. A good model: a signed and complete resident note that makes a common mistake, with the task being to catch that mistake.

3. Follow all update workflows from the new project instructions for the resubmission, including the new grader guidelines and FA/GA format.

4. The discharge-summary / note-completion workflow is deprecated. They will soon stop accepting it. OV10 was started before the new guidelines, so there is a limited window to quickly resubmit and possibly get it accepted; otherwise, move it to another approved workflow.

## Distilled principles (carry-forward)
- P1 No note-completion / "finish the note" tasks. Deprecated workflow; prefer full-authorship deliverables or review-and-correct-a-complete-note.
- P2 The scored failure must come from a realistic, catchable clinical error (consultant disagreement, accidental non-adjusted med, accidental omission, a common mistake in a signed complete note), never from punishing the model for trusting a deliberately planted falsehood in the patient's own record.
- P3 No universal floor. A task that floors every run (~15% x10) is unfair; tasks must discriminate (capable models can pass).
- P4 New-format compliance: grader guidelines + FA/GA + PL on the current project instructions for any (re)submission.
