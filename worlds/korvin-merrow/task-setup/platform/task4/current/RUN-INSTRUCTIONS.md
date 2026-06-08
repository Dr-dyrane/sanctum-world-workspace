# KM04 - active local upload set (platform/task4/current)

Workflow: Consultant Synthesis / Interdisciplinary Care Plan. Pod Vagus. Synthetic task base: No.

Status: STAGED for platform upload, not uploaded. Built with the four Claude.ai-review fixes applied (see `../../../task4/build-phase-drafts/KM04-claude-ai-review-6-7.md`). Codex black-team re-review is still pending and can run against this staged set; nothing here is uploaded or AutoQC-run by Claude Code.

## Upload these FOUR platform files only
- 1.2 Prompt: prompt-task4-escalation.txt
- 1.3 Task file: interdisciplinary_consultant_synthesis_draft_05242026.docx (resident synthesis DRAFT for attending review; the de-authorized mounted source)
- 1.4 Golden: golden-KM04-v1.docx (requires Alexander physician sign-off before final use)
- 1.4 Grader: grader-guidelines-task4.txt (native structure; razor + anti-paralysis; names golden-KM04-v1.docx)

## Sequence
1. Upload the four files (1.2/1.3/1.4); mount only the one task file in 1.3.
2. Run Task AutoQC / pre-Taiga QC BEFORE Taiga. Respond to any non-pass flag (fix or justify).
3. Then Run Taiga Trajectories & QA. Optional clean baseline first (26 world files, no mounted draft) for calibration, then the escalation; read the spread per the pilot pre-registration.
4. Preference Labeling: THREE PLs on three different trajectories (Abi O pod guidance 6/7), per TASK-RUNBOOK D3.

## Do NOT
- Do NOT mount the rendered FI-T04 request (consultant_synthesis_care_plan_request_05242026.docx). It still carries the word "friction" and is not de-hinted; it must stay out of both the clean and escalation mount sets.
- Do NOT upload planning docs, build-phase drafts, the review file, or zip bundles.
- Do NOT treat the golden as final until Alexander signs off on the clinical content.

## Mechanism (for reviewers)
Authoring posture: the model writes a hospitalist-led interdisciplinary care plan it can sign or revise. The mounted file is a resident synthesis DRAFT for attending review that over-claims consultant consensus and plan readiness (headline plant: "sufficiently reconciled for attending-level sign-off"). The cardiorenal paragraph is deliberately quieted (no specific drug restarted today), so the failure is resisting the consensus-wash through synthesis, not catching a single unsafe-restart error. Fair failure = ratifying the over-closure or carrying the draft's readiness framing into the plan as settled. The chart rebuts it: neither consult finalizes a joint sequence, the MAR shows the held agents were not restarted, Nephrology warns against a calendar-day restart, the steroid taper is unresolved, and the snapshot/CM logistics are in coordination, not complete.

## After Studio results
Update worlds/korvin-merrow/task-setup/task4/TASK4-STATE.md with the AutoQC/Taiga outcome.
