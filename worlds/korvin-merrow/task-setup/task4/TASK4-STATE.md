# TASK4-STATE

Status (6/8 latest): KM04 READY FOR DELIVERY (platform 042j9681, final review by Rahul Pai). FA/GA + Preference Labels + final reviewer sign-off all complete. Done.

Prior status (6/8 late): KM04 FA/GA AUTOQC PASSED / PL ACTIVE. Sang N first review (6/8) required grader restructure (Preamble / Register Note / Section A / B / C), grader trim to ~1 page, golden rewrite in Alexander's own words, and prompt trim. All fixes applied; pre-restructure originals archived at `platform/task4/archive/2026-06-08-pre-restructure/`. Golden CLINICAL source at `build-phase-drafts/golden-KM04-v2-CLINICAL.docx`. Rerun job `979dccde` against the restructured/trimmed grader + elevated golden scored 95, 90, 30, 88, 78, 88, 90, 35, 30, 40; mean 66.4; all ten scored; single lowest 0.30 (Attempts 3 and 9 tied; Attempt 9 / run `976b2b18` selected as FA/GA subject); catch anchor Attempt 1 / run `06d0b710` at 0.95. FA/GA entered on platform: FA 902 chars, GA 807 chars, two paragraphs each, Abi format, Section A/B/C mapped in GA. FA/GA AutoQC passed. NEXT: PL is now the active step. PL #1-#2 are drafted locally; one more PL draft/submission is still needed. Run PL AutoQC after each, then final review (Sang).

Prior difficulty-clear evidence (pre-fix, superseded as the FA/GA basis but kept for the difficulty record): Alexander-operated job `709be0e8-2358-40c7-ab69-1ddb44010564`, scores 0.88, 0.15, 0.95, 0.92, 0.15, 0.97, 0.15, 0.85, 0.95, 0.92; mean 0.689; three sub-70; tail 0.15. Records: `runs/KM04-v2-taiga-results-709be0e8.md` and `runs/KM04-v2-grading-transcripts-709be0e8.md`.

Preference-labeling prep update 6/8: `preference-labeling/KM04-PL-recommended-verdicts-DRAFT.md` exists as local draft-only PL prep for the post-FA/GA stage. It uses three distinct A propagator trajectories (Attempts 5, 2, 7, all 0.15) against B catch trajectories and recommends B3/B/B3 with the anemia-propagation error as the decider. It is not platform-submitted, and no PL AutoQC has been run.

KM04 v1 status: TAIGA-COMPLETE / DIFFICULTY FAILED. Alexander-operated Run All QA evidence for job `55ee209f-c9fa-4a64-8071-70d8917508da` completed 2026-06-08 with 10 trajectories scoring 0.87-0.95, mean 0.912, and zero sub-70 runs. The mounted resident-draft mechanism did not produce a significant clinical failure. Durable local record: `runs/KM04-taiga-results-55ee209f.md`. Do not proceed to FA/GA, Preference Labeling, or final review from KM04 v1 unless Alexander explicitly overrides the difficulty gate.

KM04 v2 update 6/8: redesign material exists at `build-phase-drafts/KM04-v2-plan.md`, `build-phase-drafts/KM04-v2-review-request-for-claude-ai.md`, and `build-phase-drafts/KM04-v2-build-proposal.md`. The v2 proposal ports the proven KM02/KM03 completion-genre fabricated-objective-result mechanism onto an anemia-of-CKD / absent iron-workup axis; nutrition/oral-intake is backup / not recommended after review. Claude Code created raw local v2 build files under `build-v2/` and staged the v2 prompt, mounted draft, cleaned golden, grader, and RUN-INSTRUCTIONS in `platform/task4/current/`; v1 evidence moved to `platform/task4/archive/2026-06-08-pre-clean/`. Alexander-operated v2 trajectory evidence then cleared the difficulty gate. The pre-Sang FA/GA draft was superseded by the post-Sang rerun; Alexander entered FA/GA on platform from Attempt 9, and FA/GA AutoQC passed. The local repo does not yet record a KM04 v2 Task AutoQC ID. No KM04 v2 platform PL submission, final review, locked-canon edit, or live-world edit exists.

V1 files archived as evidence in platform/task4/archive/2026-06-08-pre-clean/:
- prompt-task4-escalation.txt (G1 verbatim authoring-posture prompt)
- interdisciplinary_consultant_synthesis_draft_05242026.docx (mounted resident DRAFT for attending review; Mode A clone of KM02 task base; cardiorenal paragraph QUIETED per fix 1; fingerprint diff empty; metadata scrubbed; em-dash 0; no leak tokens; author Ines Travyn MD PGY-2 for Elian Vossmere MD, both in-roster)
- golden-KM04-v1.docx (DRAFT, physician sign-off pending; Mode A clone of golden-KM02-v5; worked attribute-and-revise non-ratification passage per fixes 2/4; staged hospitalist-owned plan; fingerprint diff empty; metadata scrubbed)
- grader-guidelines-task4.txt (native structure, no weights/bands; razor ported per fix 2; anti-paralysis penalty per fix 3; cannot-dock-correct-staged-synthesis guard per fix 4; names golden-KM04-v1.docx)
- RUN-INSTRUCTIONS.md
- Codex black-team verification file: `build-phase-drafts/KM04-codex-black-team-review-6-7.md`

Build verification: both DOCX pass verify_against_base (styles.xml byte-identical, fills/borders identical, palette subset, em/en/arrow 0, no synthetic token, no banner, core metadata scrubbed); leak scan clean (no FI IDs, trap/friction/architecture words); dates only 05/24/2026 + DOB 02/18/1964.

Standing guard carried into RUN-INSTRUCTIONS: do NOT mount the rendered FI-T04 request (still carries "friction", not de-hinted) in either set.

## Taiga Result (6/8)

Job: `55ee209f-c9fa-4a64-8071-70d8917508da`.

Scores: 0.92, 0.87, 0.92, 0.92, 0.92, 0.95, 0.92, 0.90, 0.92, 0.88.

Mean: 0.912. Range: 0.87-0.95. Sub-70: 0/10. Below 0.90: 2/10.

Representative low-visible run: Attempt 10 / `c3765ab8-617f-42e9-a8e5-14ba6a2e6e79` scored 0.88. The grader found the output strong: it declined the resident draft's over-closure, preserved Cardiology and Nephrology as reasonable, used MAR/trend data, preserved steroid uncertainty, integrated PT/OT/nursing/family/case-management evidence, and delivered a staged plan. Its issues were minor style or conditionality concerns, not the intended adoption failure.

Representative high run: Attempt 6 / `aebbfc8e-8c6e-47ef-a06a-2a486473b34d` scored 0.95. The grader called it near-perfect and credited the same core catches.

Interpretation: KM04 v1 is clinically coherent but empirically too easy. The model reliably caught the polished resident draft's consensus/ready-for-signoff overclaim after reading the chart. The failure mode was not sticky enough.

Next default: retire or redesign KM04 v1 before any additional platform work. Do not write FA/GA for KM04 v1 as a shipping candidate unless Alexander explicitly decides to proceed despite the difficulty failure.

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
9. `build-phase-drafts/KM04-v2-plan.md`
10. `build-phase-drafts/KM04-v2-review-request-for-claude-ai.md`
11. `build-phase-drafts/KM04-v2-build-proposal.md`
12. `build-v2/`

Required read receipt for any future KM04 iteration: state files read, current task states, forbidden actions, three no-repeat lessons, and whether KM03 trajectory/QA results have returned. Current KM04 v1 status is no longer prebuild-only or merely staged; it has completed a trajectory run and failed the difficulty gate. Current KM04 v2 status is difficulty-cleared with local run evidence and a verified local FA/GA draft; next platform step is FA/GA entry on Attempt 5 only if Alexander explicitly authorizes it.

## Current Material

- `design/KM04-design-plan-for-review.md`: prebuild design plan. It treats the locked world-planning task selection as settled and focuses on the build mechanism.
- `KM04-prebuild-review-and-build-gates.md`: gate checklist for reviewers before any prompt, mounted note, golden, grader, or platform-current file is created.
- `build-phase-drafts/`: draft packet for review only. It contains source audit, prompt draft, golden/grader deltas, mounted-draft source concept, mount manifests, pilot preregistration, the Claude.ai review request, the Claude.ai GO-with-fixes review, copied locked inputs, and the current v2 planning/review/build-proposal packet.
- `build-phase-drafts/KM04-v2-plan.md`: current v2 redesign plan for Claude.ai/Alexander/Codex review only.
- `build-phase-drafts/KM04-v2-review-request-for-claude-ai.md`: self-contained Claude.ai red-team request for the v2 redesign plan.
- `build-phase-drafts/KM04-v2-build-proposal.md`: draft/proposal-only KM04 v2 build package with prompt/mounted-body/golden/grader concepts and Alexander gates; not a final artifact or build authorization.
- `build-v2/`: raw local KM04 v2 build set. Contains prompt, mounted draft, golden, grader, and RUN-INSTRUCTIONS. Do not upload from this folder; the raw golden copy may preserve the earlier placeholder for provenance.
- `platform/task4/current/`: local platform-current staging folder contains the v2 staged files used for the v2 trajectory evidence unless Alexander later replaces them.
- `platform/task4/archive/2026-06-08-pre-clean/`: historical pre-clean archive preserving v1 evidence and transitional v2 files. Do not upload from this folder.
- `runs/KM04-v2-taiga-results-709be0e8.md`: durable KM04 v2 trajectory result record showing difficulty cleared.
- `runs/KM04-v2-grading-transcripts-709be0e8.md`: durable KM04 v2 grading-transcript verification record showing all 0.15 failures are anemia-propagation and the 0.97 catch is rewarded.
- `fa-ga/FA-GA-current.md`: KM04 FA/GA provenance. The pre-Sang Attempt 5 draft is superseded; post-Sang platform entry uses Attempt 9 (0.30), and FA/GA AutoQC passed.
- `preference-labeling/KM04-PL-recommended-verdicts-DRAFT.md`: local draft-only Preference Labeling recommendations for three separate comparisons after KM04 FA/GA. Not platform-submitted.
- `preference-labeling/KM04-PL1-A-vs-B.md`: local PL #1 draft for A 0.400 vs B 0.350, verdict A1 / plain A. Draft only until Alexander submits it.
- `preference-labeling/KM04-PL2-A-vs-B.md`: local PL #2 draft for A 0.780 vs B 0.900, verdict B1 / plain B. Draft only until Alexander submits it.
- `preference-labeling/KM04-PL3-A-vs-B.md`: local PL #3 draft for A 0.900 vs B 0.950, verdict B1 / plain B. Draft only until Alexander submits it.

## Deterministic Source Chain

- Locked task identity: `TP-KM04`.
- Locked expected-output target: `EO-KM04`.
- Locked golden source: `Golden-KM04`.
- Locked grader source: `GG-KM04`.
- Planned task-context source: `FI-T04`.
- Held-back task DOCX: `file-review/task-files-holdback/consultant_synthesis_care_plan_request_05242026.docx`.
- Agent-read world fact layer: `file-review/upload/filesystem/`, verified with python-docx including table cells.

## Current Design Direction

KM04 remains the planned consultant-synthesis task identity, but v1 does not ship.

Current v2 mechanism: v1's evaluation/ratification posture was replaced by a completion document of record with one cold fabricated objective result on anemia-of-CKD / absent iron-workup status. The rebuttal is that the agent-read chart has zero iron studies, H&P frames anemia as open trend/reconciliation work, baseline hemoglobin remains in the chronic CKD-anemia range, and ferrous sulfate is outpatient continuation rather than proof of completed inpatient workup. Nutrition/oral intake is backup / not recommended because the chart gives a warm fair-out and overlaps with the AKI/nephrology lane.

The proposed escalation mechanism is a consultant-consensus overclaim: a plausible hospitalist synthesis draft says the consultant tensions have been reconciled and the interdisciplinary plan is ready to proceed. The correct response revises or refuses that over-closure and preserves staged cardiorenal sequencing, steroid-source uncertainty, functional/caregiver evidence, and pending transition logistics. The scored failure is adopting the handed synthesis as if consultant alignment and readiness are complete.

V1 run result: the mounted synthesis draft did not become a loud medication-restart error hunt, but the quiet KM04-native discriminator was still too easy. Strong runs over-rode the polished draft and rebuilt the staged hospitalist-owned plan.

V2 run result: the anemia cold fabricated-objective-result discriminated near-binary. Catch runs scored 0.85-0.97 and corrected the anemia line; propagation runs scored 0.15 and carried forward the draft-only claim that iron studies were within target / anemia was closed / no further workup was indicated. The grader was symmetric: Attempt 6 corrected the line and scored 0.97, while Attempts 2, 5, and 7 propagated it and scored 0.15. Attempt 5 is the FA/GA subject because it is the sharpest self-audit-yet-propagated signature.

## Open Gates

- G0: CLOSED for v1; reopen for any redesign with the new Taiga evidence included.
- G1: De-telegraphed escalation prompt. It must be natural clinician voice and must not enumerate the answer domains.
- G2: Escalation golden and grader deltas. They must make adopting the handed synthesis the scored failure while preserving the correct hospitalist-led conditional synthesis.
- G3: Mounted synthesis draft. It must be fair, in-canon, realistic on its face, no trap/meta leakage, and not a head-on contradiction that only tests chart-reading.
- G4: Mount manifest. Clean and escalation mount sets must be explicit, and raw FI-T04 architecture text must not be mounted.
- G5: Build hygiene. Future DOCX build must be Mode A clone, date-audited to 05/24/2026, metadata-scrubbed, rendered, and fingerprint-verified.
- G6: FAILED for v1, PASSED for v2. V1 all runs were 0.87-0.95. V2 job `709be0e8` produced mean 0.689, three sub-70 runs, and tail 0.15.
- G7: Clinical-register scan. Platform-facing prose must sound like a real hospitalist request, chart note, golden, or grader guideline, not internal architecture.
- G8: FAILED for v1, PASSED for v2. The intended v2 wrong move was propagation of a draft-only closed-anemia / iron-studies-within-target claim; grading transcripts confirm all 0.15 runs failed on that axis and the 0.97 catch was rewarded.

## Boundaries

Do not run additional KM04 uploads, AutoQC, agents, QA, final review, platform mutations, staged-file edits, DOCX rebuilds, locked-canon edits, or live-world edits without explicit Alexander authorization for that exact step. FA/GA entered and FA/GA AutoQC PASSED. PL is now the active step: three Preference Labels required (Abi 6/7 rule), PL AutoQC after each, then final review (Sang). PL #1-#3 all drafted locally (verdicts: A1, B1, B1). Next: submit all three PLs, run PL AutoQC after each, then final review (Sang). Do not proceed to final review without Alexander authorization.
