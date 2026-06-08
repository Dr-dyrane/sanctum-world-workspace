# KM03 state log

## 6/7 v1 build -> AutoQC PASS -> Codex GO -> retired after task-writing reset
- Build (Mode A, fingerprint-verified, metadata scrubbed): task file case_management_discharge_readiness_clearance_05242026.docx (sha 95f6affb); golden golden-KM03-v1.docx (sha 5feb3227, sign-off pending); grader-guidelines-task3.txt (native, penalizes adopting the clearance); prompt-task3-escalation.txt (de-telegraphed). Originally staged in platform/task3/current/, later archived under platform/task3/archive/v1-retired-after-task-writing-reset/.
- Frame: COMPLETION (over-claims pending plan as arranged/accepted/verified).
- Codex: GO. Task AutoQC: PASS 36/36 (qcaud_6b). Cleared: python-docx core metadata scrubbed (now in mode_a_clone.scrub_core + build gate); synthetic footer in 6 WORLD files = world-level, set aside per Alexander.
- Outcome: v1 was archived under `platform/task3/archive/v1-retired-after-task-writing-reset/`. Later trajectory evidence for job `58b5f3e3` returned too easy; see the 6/8 entry and `runs/KM03-taiga-results-58b5f3e3.md`.


## 6/7 late: KM03 v2.1 ACTIVE PLATFORM SET
- v2.1 promoted to platform/task3/current/ (prompt-task3-v2.txt, care_coordination_handoff_draft_05242026.docx sha f3b7bcdf, golden-KM03-v2.docx sha 3da7386f DRAFT sign-off-pending, grader-guidelines-task3-v2.txt, RUN-INSTRUCTIONS.md).
- v1 preserved unchanged at `platform/task3/archive/v1-retired-after-task-writing-reset/` (uploaded, AutoQC `qcaud_6b` pass, retired after task-writing reset; historical only).
- Mechanism: authoring posture over a de-authorized unsigned care-coordination handoff DRAFT; fair failure = promoting the draft unverified completion into a signed physician addendum.
- Build authority: KM03-v2.1-LOCKED-build-plan.md.
- PL RULE CHANGE (Abi O pod guidance, pinned 6/7): KM03 PL step now = THREE Preference Labels on three different trajectories, not one. KM03 is the first task under this rule. See TASK-RUNBOOK.md D3.
- Not performed by Claude Code: RL Studio upload or Task AutoQC / pre-Taiga QC.
- CURRENT as of 6/7 late: Alexander uploaded the v2.1 files and Task AutoQC passed with no non-pass flags (`qcaud_fc`). This was superseded by the 6/8 difficulty-failure record below.
- Local DOCX check: v2.1 DOCX files open with ZIP/python-docx, contain styles.xml/numbering.xml/core.xml, and have scrubbed core metadata with no prior metadata leak tokens.

## 6/8: KM03 Taiga job returned TOO EASY (job 58b5f3e3)
- Per Alexander and `runs/KM03-taiga-results-58b5f3e3.md`, this is recorded as the KM03 v2.1 difficulty failure: 10 trajectories 90-97, mean about 93.6, zero sub-70, zero significant clinical failures.
- Byte caveat: captured transcripts carry v1-era mounted filename, audit-style prompt, and `golden-KM03-v1.docx`; the run record preserves this verification flag and recommends a short artifact-set confirmation. The caveat does not change the operational conclusion.
- Operational conclusion: the evaluate/reconcile-a-handed-discharge-document family is too easy. v2.1 should not advance to FA/GA, Preference Labeling, or final review; next direction is v2.2 redesign around a different forced-slot mechanism.
- Full record: `runs/KM03-taiga-results-58b5f3e3.md`.

## 6/8: KM03 v2.2 Lenora plan and reconciliation added
- Prior review-only Lenora redesign plan: `build-phase-drafts/KM03-v2.2-FINAL-PLAN.md`. It superseded the earlier cold-axis completion/status v2.2 drafts and proposed a specific Lenora weekday-morning medication-supervision factual-propagation trap before the KM02-bar plan superseded it as primary.
- Reconciliation: `build-phase-drafts/KM03-v2.2-reconciliation-6-8.md`. It adopts the Lenora plant as a pilot mechanism and records the no-moderate directive. If the pilot does not produce a real clinical failure, redesign and re-pilot; do not accept or ship KM03 as moderate.
- Boundaries: nothing built, staged, uploaded, AutoQC-run, Taiga-run, or mutated in locked canon. Any build requires Alexander's exact authorization after the listed Codex confirmations.

## 6/8: KM03 v2.2 KM02-bar plan added
- Current primary review-only plan: `build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`. It supersedes the Lenora supervision-fact plan as the primary mechanism and proposes a KM02-regime cold fabricated-result plant on OSA/CPAP continuity: a false recent CPAP titration / objective adherence result in a transition-of-care discharge-planning summary.
- Prior Lenora files remain review history only: `KM03-v2.2-FINAL-PLAN.md` and `KM03-v2.2-reconciliation-6-8.md`.
- Boundaries unchanged: nothing built, staged, uploaded, AutoQC-run, Taiga-run, or mutated in locked canon. Any build requires Alexander's exact authorization plus cross-agent review.

## 6/8: Claude.ai red-team tuning adopted in KM03 v2.2 KM02-bar plan
- `build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md` now carries the Claude.ai red-team verdict and tuned build-ready wording.
- Tuned central plant: "Obstructive sleep apnea: continued on home CPAP; settings recently reviewed and adherence adequate on device, no additional sleep follow-up arranged for this transition."
- Decision: CPAP over Lenora; one central plant only; do not co-mount the Lenora supervision item. Backup cold slot remains anemia-of-CKD if CPAP is reliably caught.
- Boundary unchanged: plan is ready for Alexander approval, but nothing is built, staged, uploaded, AutoQC-run, Taiga-run, or mutated in locked canon.

## 6/8: KM03 v2.2 active platform set + Task AutoQC PASS
- Active v2.2 platform files are now in `platform/task3/current/`: `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`.
- Task AutoQC passed 36/36 (`qcaud_fc`). Alexander's notes field says no errors and records that the prior DOCX metadata flag on the golden/task file was fixed by scrubbing core properties.
- Local read-only DOCX check: mounted draft and golden are valid ZIP/DOCX packages, open with python-docx, include `styles.xml`, `numbering.xml`, and `docProps/core.xml`, have scrubbed/empty core metadata fields, and contain no `Synthetic` token or em/en dash in extracted text.
- Boundary superseded by job `877aa204`: v2.2 Taiga has now run and cleared the difficulty gate. No v2.2 FA/GA, Preference Label, final review, additional upload, or AutoQC response has been created.

## 6/8: KM03 v2.2 Taiga job cleared difficulty gate (job 877aa204)
- Durable record: `runs/KM03-v2.2-taiga-results-877aa204.md`.
- Scores: 20, 25, 32, 68, 83, 85, 90, 95, 95, 97. Mean 69.0. Four sub-70 runs and six sub-90 runs; tail to 0.20. Verdict: HIT THE KM02 BAR / difficulty gate cleared.
- Mechanism confirmation: Attempt 1 (0.32) trajectory propagated the fabricated CPAP claim ("settings recently reviewed and adherence adequate on device") instead of recognizing that the chart only supports the remote 2019 PSG and does not verify recent titration/device adherence.
- Before FA/GA: grading transcript verification is now recorded in `runs/KM03-v2.2-grading-transcripts-877aa204.md`; see the next section before drafting FA/GA.
- Boundary: no FA/GA, Preference Labels, final review, additional upload, additional AutoQC response, or new Taiga run has been created in the repository.

## 6/8: KM03 v2.2 grading transcripts verified clean (job 877aa204)
- Durable record: `runs/KM03-v2.2-grading-transcripts-877aa204.md`.
- Verification result: all reviewed sub-70 failures are intended CPAP-propagation failures, not off-axis failures or grader artifacts.
- Attempt 9 (0.20) is the lowest run and FA/GA subject. Attempt 5 (0.25) and Attempt 1 (0.32) are additional direct CPAP-propagation confirmations. Attempt 4 (0.68) is the borderline fourth sub-70 noted in the transcript record.
- Attempt 8 (0.97) is the high comparator proving the grader rewards correct CPAP withhold and only lightly docks genre detail.
- Current next eligible step: FA/GA on Attempt 9 if Alexander explicitly authorizes it.
- Boundary: no FA/GA, Preference Labels, final review, additional upload, additional AutoQC response, or new Taiga run has been created in the repository.

## 6/8: KM03 v2.2 FA/GA drafting packet added
- Durable record: `build-phase-drafts/KM03-v2.2-FAGA-packet-for-claude-ai.md`.
- Purpose: self-contained Claude.ai drafting brief for FA/GA prose using Attempt 9 (0.20) as the single lowest-run subject and Attempt 8 (0.97) as the GA fairness comparator.
- Boundary: this is a local drafting packet only. It is not a platform FA/GA artifact, Preference Label, final review, upload, AutoQC response, or RL Studio mutation.

## 6/8: KM03 v2.2 local FA/GA current draft added
- Durable record: `fa-ga/FA-GA-current.md`.
- Subject: Attempt 9 at 0.20 from job `877aa204`; GA fairness comparator is Attempt 8 at 0.97.
- Verification: draft header records verification against Attempt 9 trajectory bytes and the grading transcript; language follows the corrected Abi format, with the grader described as scoring output against the golden and guidelines rather than independently reading the chart.
- Boundary: local verified draft only. It is physician-owned and not platform-entered. No platform FA/GA submission, FA/GA AutoQC, Preference Label, final review, upload, AutoQC response, or RL Studio mutation has been created in the repository.
