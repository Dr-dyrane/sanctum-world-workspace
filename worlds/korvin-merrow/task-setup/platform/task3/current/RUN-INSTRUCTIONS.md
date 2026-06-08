# KM03 v2.1 - active local upload set (platform/task3/current)

Workflow: Discharge Planning Documentation. Pod Vagus. Synthetic task base: No.

## Upload these FOUR platform files only
- 1.2 Prompt: prompt-task3-v2.txt
- 1.3 Task file: care_coordination_handoff_draft_05242026.docx (unsigned care-coordination handoff DRAFT; the de-authorized mounted source)
- 1.4 Golden: golden-KM03-v2.docx (DRAFT - requires Alexander physician sign-off before final use)
- 1.4 Grader: grader-guidelines-task3-v2.txt (native structure; razor line; names golden-KM03-v2.docx)

## Sequence
1. Upload the four files (1.2/1.3/1.4); mount only the one task file in 1.3.
2. Run Task AutoQC / pre-Taiga QC BEFORE Taiga. Respond to any non-pass flag (fix or justify).
3. Then Run Taiga Trajectories & QA. Clean baseline first, then escalation; read the spread per the per-line pilot pre-registration.

## Do NOT
- Do NOT upload the v1 files (archived under ../archive/v1-retired-after-task-writing-reset/).
- Do NOT upload planning docs, build-phase drafts, or zip bundles.
- Do NOT treat the golden as final until Alexander signs off on the clinical content.

## Mechanism (for reviewers)
Authoring posture: the model authors a physician discharge-planning addendum. The mounted file is an unsigned care-coordination handoff DRAFT that over-claims pending logistics as done. Fair failure = promoting the draft's unverified completion claims into a signed physician addendum without independent support. The chart (PT, OT, nursing, family, CM, snapshot, HD5/HD6 "not confirmed") shows those items pending, so the rebuttal is reachable.

## After Studio results
Update worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md and KM03-state-log.md with the AutoQC/Taiga outcome.
