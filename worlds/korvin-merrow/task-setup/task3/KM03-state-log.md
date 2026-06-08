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
