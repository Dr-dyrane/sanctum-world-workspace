# Pod policy 2026-06-20: deprecated note-completion workflow + task fairness floor

Source: Larry E, first review of OV10 (Ondina Vasquell, Task 10), 6/20/2026. Verbatim-in-substance record at worlds/ondina-vasquell/tasks/task10/LARRY-2026-06-20-OV10-CORRECTION.md. These four rules bind all new worlds and tasks; they generalize a single-task correction into standing doctrine.

## 1. Note-completion / "finish the note" workflows are deprecated
Finishing or completing a note is not a realistic workflow. In practice a clinician either uses AI to author the whole note and then proofreads and signs it, or does not use it at all. The discharge-summary and note-completion workflow specifically is being phased out and will soon stop being accepted.
- Do NOT build "finish this started draft" or "complete this placeholder note" tasks.
- PREFER full-authorship deliverables (write the whole note, letter, or worksheet from the chart), or the review-and-correct pattern below.
- A task started before the new guidelines has a limited window to resubmit; otherwise move it to another approved workflow.

## 2. No planted false information; the scored failure must be a realistic, catchable error
Do not intentionally feed the model false facts to be distrusted. The model carrying over something stated in the patient's own chart must NOT, by itself, earn a floor (~15%) score.
- FAIR scored failures: disagreements between consultants, accidental non-adjusted medications, accidental omissions of information, a common mistake in a signed, complete resident note.
- Withholding information and asking the model to confirm or synthesize is legitimate. Planting a falsehood in the record purely to punish trust is not.

## 3. No universal floor (the task must discriminate)
A task that fails low (~15%) across all ten runs is flagged unfair, however well understood the trap is. A capable model must be able to pass; the catch must be reachable, not a guaranteed floor.
- At pilot, every task's score distribution must show a reachable pass. Any task that floors every run is redesigned, not shipped.

## 4. New-format compliance on every (re)submission
Any task built or resubmitted now uses the current project instructions: the current grader guidelines, the current FA/GA format, and the current PL format.

## The endorsed pattern: review-and-correct a complete signed note
Larry's own suggested viable shape: provide a signed, complete resident note that makes a common, realistic mistake, and ask the model to review the note and catch the mistake. This keeps the deliverable a real workflow, sources the failure from a realistic catchable error (rule 2), and avoids both note-completion (rule 1) and a planted falsehood.

## Worked example already in the repo
World 3 (Marva Lydell) Task 4 was redesigned off the note-completion format directly onto this pattern: an attending peer review of a COMPLETE signed resident transition note carrying two common, realistic errors (oxygen cleared despite a documented exertional desaturation; held agents silently resumed), on the approved Peer Review Case Analysis lane. Use it as the template when retiring a completion task. The W3 application audit is at worlds/marva-lydell/docs/W3-OV10-LESSONS-AUDIT.md.

## Carry-forward principles (short form)
- P1 No note-completion or finish-the-note tasks. Prefer full authorship or review-and-correct a complete note.
- P2 Failure from a realistic catchable error, never from a planted falsehood in the patient's own record.
- P3 No universal floor; capable models must be able to pass.
- P4 Current grader guidelines, FA/GA, and PL formats on every build and resubmission.
