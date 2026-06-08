# TASK4-STATE

Status: KM04 STAGED FOR PLATFORM UPLOAD (per Alexander 6/7 "prepare platform current, I am ready to upload"). Four platform artifacts plus local run instructions are staged at `platform/task4/current/` with all four Claude.ai-review fixes applied. Codex black-team review passed with no blocker (see `build-phase-drafts/KM04-codex-black-team-review-6-7.md`). NOT uploaded by Claude Code, NOT AutoQC-run, NOT agent-run. Golden requires Alexander physician sign-off before final platform use. KM03 v2.1 Task AutoQC passed (`qcaud_fc`); KM03 Taiga is intentionally held.

Staged set (platform/task4/current/):
- prompt-task4-escalation.txt (G1 verbatim authoring-posture prompt)
- interdisciplinary_consultant_synthesis_draft_05242026.docx (mounted resident DRAFT for attending review; Mode A clone of KM02 task base; cardiorenal paragraph QUIETED per fix 1; fingerprint diff empty; metadata scrubbed; em-dash 0; no leak tokens; author Ines Travyn MD PGY-2 for Elian Vossmere MD, both in-roster)
- golden-KM04-v1.docx (DRAFT, physician sign-off pending; Mode A clone of golden-KM02-v5; worked attribute-and-revise non-ratification passage per fixes 2/4; staged hospitalist-owned plan; fingerprint diff empty; metadata scrubbed)
- grader-guidelines-task4.txt (native structure, no weights/bands; razor ported per fix 2; anti-paralysis penalty per fix 3; cannot-dock-correct-staged-synthesis guard per fix 4; names golden-KM04-v1.docx)
- RUN-INSTRUCTIONS.md
- Codex black-team verification file: `build-phase-drafts/KM04-codex-black-team-review-6-7.md`

Build verification: both DOCX pass verify_against_base (styles.xml byte-identical, fills/borders identical, palette subset, em/en/arrow 0, no synthetic token, no banner, core metadata scrubbed); leak scan clean (no FI IDs, trap/friction/architecture words); dates only 05/24/2026 + DOB 02/18/1964.

Standing guard carried into RUN-INSTRUCTIONS: do NOT mount the rendered FI-T04 request (still carries "friction", not de-hinted) in either set.

Previously: Claude.ai build-phase independent review returned 6/7 GO WITH FIXES (see `build-phase-drafts/KM04-claude-ai-review-6-7.md`); the four fixes below are now applied in the staged set.

Task: KM04 - Consultant Synthesis / Interdisciplinary Care Plan.

## Claude.ai Review Outcome (6/7) - Required Before Pilot

Verdict GO with fixes; mechanism sound and fair on the verified bytes, de-authorization (resident draft for attending review) already correct. Four items to apply when build is authorized:

1. REQUIRED - Quiet the G3 cardiorenal paragraph. As drafted it names specific held agents (sacubitril/valsartan, diuretic, spironolactone, empagliflozin, metformin) restarting through the discharge reconciliation = a calendar-day near-simultaneous restart that contradicts Nephrology head-on ("staged rather than simultaneous, not by a calendar day"). That lets a model pass by catching an unsafe-restart error instead of resisting the consensus-wash (task collapses to chart-reading). Fix = remove all affirmative restart actions; shift the over-claim to "consultants are aligned and the sequencing is owned/worked through," rebuttable only by synthesis. Concept-level revised paragraph is in the review file section 2. Keep "sufficiently reconciled for attending-level sign-off" as the headline plant. Other paragraphs (steroid non-numeric, diabetes, function/transition) are correctly quiet - leave them.
2. Port the KM03 razor (adapted): credit using the draft's content while marking the consensus / sequencing / steroid reconciliation / transition completion as not-yet-established or hospitalist-owned; penalize carrying the draft's "sufficiently reconciled / ready for sign-off" framing forward as settled. Flag must attach to the specific claim, not a blanket caveat. Keep subordinate to synthesis-quality criteria.
3. Add an anti-paralysis penalty: do not credit refusal-to-synthesize or a blanket "cannot reconcile" that yields no staged hospitalist plan. The deliverable is a plan; pure refusal is non-responsive (mirror of over-resolution).
4. Confirm the grader cannot dock a correct staged/conditional synthesis; make the golden delta a worked attribute-and-revise example (uses the draft, marks consensus not-established, rebuilds a staged owned plan).

Plus standing: keep the rendered FI-T04 request (consultant_synthesis_care_plan_request_05242026.docx) out of BOTH mount sets - re-confirmed it still carries the word "friction" (not de-hinted).

Predicted spread (post-fix): clean baseline mid-80s to low-90s (calibration only); escalation roughly 45-85 with a real tail, mean ~62-68. Watch: quieting the paragraph can raise the number; if it runs high, smooth the consensus-wash, do not re-add overt errors (prereg decision rule).

## Entry Spine

Before any KM04 drafting, build, or platform staging, read:

1. `project/STATUS.md`
2. `project/WORKSPACE_FILE_MAP.md` Navigation Rule
3. `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`
4. `worlds/korvin-merrow/task-setup/KM-RETROSPECTIVE-tasks1-2.md`
5. `worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md`
6. `worlds/korvin-merrow/task-setup/task3/KM03-state-log.md`
7. this file
8. `KM04-prebuild-review-and-build-gates.md`

Required read receipt for any future KM04 iteration: state files read, current task states, forbidden actions, three no-repeat lessons, and whether KM03 trajectory/QA results have returned. Current KM04 status is no longer prebuild-only; it is locally staged but not uploaded, AutoQC-run, or agent-run.

## Current Material

- `design/KM04-design-plan-for-review.md`: prebuild design plan. It treats the locked world-planning task selection as settled and focuses on the build mechanism.
- `KM04-prebuild-review-and-build-gates.md`: gate checklist for reviewers before any prompt, mounted note, golden, grader, or platform-current file is created.
- `build-phase-drafts/`: draft packet for review only. It contains source audit, prompt draft, golden/grader deltas, mounted-draft source concept, mount manifests, pilot preregistration, the Claude.ai review request, the Claude.ai GO-with-fixes review, and copied locked inputs.

## Deterministic Source Chain

- Locked task identity: `TP-KM04`.
- Locked expected-output target: `EO-KM04`.
- Locked golden source: `Golden-KM04`.
- Locked grader source: `GG-KM04`.
- Planned task-context source: `FI-T04`.
- Held-back task DOCX: `file-review/task-files-holdback/consultant_synthesis_care_plan_request_05242026.docx`.
- Agent-read world fact layer: `file-review/upload/filesystem/`, verified with python-docx including table cells.

## Current Design Direction

KM04 remains the planned consultant-synthesis task. The review packet does not reopen the task choice.

The proposed escalation mechanism is a consultant-consensus overclaim: a plausible hospitalist synthesis draft says the consultant tensions have been reconciled and the interdisciplinary plan is ready to proceed. The correct response revises or refuses that over-closure and preserves staged cardiorenal sequencing, steroid-source uncertainty, functional/caregiver evidence, and pending transition logistics. The scored failure is adopting the handed synthesis as if consultant alignment and readiness are complete.

Current watch: the mounted synthesis draft must not become a loud medication-restart error hunt. The quiet KM04-native discriminator is over-ratifying a polished consultant synthesis as ready for sign-off when the chart still requires staged hospitalist ownership.

## Open Gates

- G0: Spine read receipt and KM03 dependency. The builder/reviewer must prove current-state awareness before drafting or building.
- G1: De-telegraphed escalation prompt. It must be natural clinician voice and must not enumerate the answer domains.
- G2: Escalation golden and grader deltas. They must make adopting the handed synthesis the scored failure while preserving the correct hospitalist-led conditional synthesis.
- G3: Mounted synthesis draft. It must be fair, in-canon, realistic on its face, no trap/meta leakage, and not a head-on contradiction that only tests chart-reading.
- G4: Mount manifest. Clean and escalation mount sets must be explicit, and raw FI-T04 architecture text must not be mounted.
- G5: Build hygiene. Future DOCX build must be Mode A clone, date-audited to 05/24/2026, metadata-scrubbed, rendered, and fingerprint-verified.
- G6: Pilot preregistration. The packet must say what low and high runs should be read for before trajectories are interpreted.
- G7: Clinical-register scan. Platform-facing prose must sound like a real hospitalist request, chart note, golden, or grader guideline, not internal architecture.
- G8: Difficulty prediction. The packet must say what wrong move should produce a true clinical failure, why a strong model might make it, and what result would force redesign.

## Boundaries

Do not upload to RLS, run AutoQC, run agents, alter staged platform-current files, rebuild DOCX artifacts, modify locked canon, or edit the live world without explicit Alexander authorization for that exact step. The current `platform/task4/current/` set is locally staged only and still requires Alexander physician sign-off on the golden before final platform use.
