# TASK3-STATE

Status (6/8 late, current): KM03 POST-SANG RERUN COMPLETE / LOCAL FA-GA RE-DERIVED. Rerun job `8e97cdd7` against the restructured grader + elevated golden scored 80, 62, 90, 30, 90, 88, 82, 87, 85, 70; mean 76.4; all ten scored; single lowest Attempt 4 / run `c2eea662` at 0.30; second-lowest Attempt 2 at 0.62; two sub-70 and three sub-90. The local `fa-ga/FA-GA-current.md` now supersedes the old pre-fix `877aa204` Attempt 9 draft and is verified against Attempt 4 output bytes plus the pasted grading transcript. Failure signature remains the intended CPAP propagation, with 0.90 comparators correcting it. NEXT ELIGIBLE PLATFORM STEP: FA/GA entry on Attempt 4 only if Alexander explicitly authorizes it. Do not create PL or final-review materials until platform FA/GA is entered, FA/GA AutoQC is resolved, and Alexander authorizes the next exact step. KM04 remains at post-Sang rerun gate.

Prior status: KM03 v2.2 cleared the Taiga difficulty gate after Task AutoQC pass and grading-transcript verification. Job `877aa204` scored 20, 25, 32, 68, 83, 85, 90, 95, 95, 97 with mean 69.0, four sub-70 runs, six sub-90 runs, and tail to 0.20. Grading transcripts are verified clean in `runs/KM03-v2.2-grading-transcripts-877aa204.md`: all reviewed sub-70 failures are intended CPAP-propagation failures, and the 0.97 comparator confirms correct CPAP withhold is rewarded. Local FA/GA current draft: `fa-ga/FA-GA-current.md`, verified against Attempt 9 trajectory bytes and the grading transcript, with Attempt 9 at 0.20 as subject and Attempt 8 at 0.97 as GA cross-check anchor. This draft is physician-owned and not platform-entered. Prior v2.1 is difficulty-failed (Taiga job 58b5f3e3, 10 trajectories 90-97, mean ~93.6, zero sub-70, fails the difficulty gate). Lineage: v1 too easy -> v2.1 -> v2.1 also too easy -> v2.2 CPAP/OSA fabricated-objective-result mechanism built, AutoQC-passed, empirically cleared difficulty, transcript-verified, and locally drafted for FA/GA. (Byte note: the captured `58b5f3e3` transcripts carry v1-era naming/audit prompt/golden-v1; recorded as v2.1 per Alexander, worth preserving but does not change the conclusion.) KM04 v1 failed the same gate (job 55ee209f, mean 0.912), so the whole "evaluate/reconcile a handed discharge document" family is too easy for this model.

ROOT CAUSE: KM03/KM04 are caution-genre tasks; the model's trained default (be cautious, preserve conditionality, do not rubber-stamp) IS the correct answer, so caution is free and there is no forced wrong commitment. Source-authority tweaks do not fix this.

v2.2 CURRENT PLATFORM SET: `../platform/task3/current/prompt-task3-v2.2.txt`, `../platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `../platform/task3/current/golden-KM03-v2.2.docx`, and `../platform/task3/current/grader-guidelines-task3-v2.2.txt`. Mechanism source is `build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`: completion genre + fabricated objective result + cold/unprimed OSA/CPAP axis + 3+ document rebuttal. Claude.ai red-team (6/8) adopted CPAP over Lenora and tuned the plant to a home-DME continuity line: "settings recently reviewed and adherence adequate on device, no additional sleep follow-up arranged for this transition." One central CPAP/OSA plant only; do not co-mount Lenora. Alexander ran Task AutoQC and it passed 36/36 (`qcaud_fc`). Alexander then ran Taiga job `877aa204`, which cleared the difficulty gate. Grading transcripts are verified clean in `runs/KM03-v2.2-grading-transcripts-877aa204.md`. Local draft `fa-ga/FA-GA-current.md` exists for Attempt 9 and is not platform-entered. No platform FA/GA submission, Preference Label, final review, or AutoQC response exists from v2.2 yet. Next authorized-stage action, if Alexander approves, is platform FA/GA entry on Attempt 9 (0.20), with Attempt 8 (0.97) as GA cross-check anchor.

v2.2 PRIOR PLAN HISTORY (6/8): `build-phase-drafts/KM03-v2.2-FINAL-PLAN.md` and `build-phase-drafts/KM03-v2.2-reconciliation-6-8.md` preserve the Lenora weekday-morning supervision-fact mechanism and no-moderate correction, but they are no longer the primary plan after `KM03-v2.2-KM02-BAR-PLAN.md`. Preserve as review history; do not build from them unless Alexander explicitly re-selects that mechanism.

Task: KM03 - discharge planning documentation escalation. Status: v2.2 active / Task AutoQC passed / Taiga difficulty cleared / grading transcripts verified.

## Current Material

- `design/KM03-design-plan-for-review.md`: pre-build design plan that inherits the Task 1 and Task 2 lessons.
- `KM03-3rd-reader-review-and-build-gates.md`: third-reader review confirming the design direction but blocking build until G1-G3 close.
- `build-phase-drafts/`: draft packet for reviewing G1-G3 closure concepts. Source drafts and copied inputs are trackable; the local ZIP bundle is ignored.
- `build-phase-drafts/01-build-phase-review-responses.md`: build-phase review response record. Captures the frame decision from STRIP to COMPLETION and the v2.1 source-authority correction.
- `build-phase-drafts/KM03-v2.2-FAGA-packet-for-claude-ai.md`: self-contained FA/GA drafting packet for Claude.ai after transcript verification. It is not a platform FA/GA artifact and does not submit anything.
- `build-phase-drafts/KM03-golden-clinical-register-guide.md`: local clinical-register guide for Alexander's future golden wording polish. Support only; not golden text, not a DOCX build, and not platform-entered.
- `build-phase-drafts/grader-guidelines-task3-RESTRUCTURED.txt`: local section-mapped grader helper for FA/GA reasoning against the active v2.2 grader. Draft/support only; not a platform-current grader replacement and not upload-ready.
- `fa-ga/FA-GA-current.md`: verified local FA/GA current draft for Attempt 9 (0.20), with Attempt 8 (0.97) as GA comparator. It is physician-owned, local-only, and not platform-entered.
- `KM03-state-log.md`: live event log for KM03 after staging, including v1/v2.1 difficulty failures, v2.2 build, Task AutoQC pass, and trajectory/QA state.
- `../platform/task3/current/`: current folder contains only the active v2.2 platform set plus `RUN-INSTRUCTIONS.md`. Active files are `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`.
- `runs/KM03-v2.2-taiga-results-877aa204.md`: durable v2.2 trajectory result record. Job `877aa204` cleared the difficulty gate with mean 69.0 and four sub-70 runs.
- `runs/KM03-v2.2-grading-transcripts-877aa204.md`: durable grading-transcript verification record. It confirms the sub-70 failures are CPAP-propagation failures, the 0.97 comparator rewards correct withhold, and Attempt 9 (0.20) is the FA/GA subject.
- `../platform/task3/archive/v2.1-difficulty-failed-after-58b5f3e3/`: retired v2.1 platform evidence after the difficulty failure. Historical evidence only.
- `../platform/task3/archive/v1-retired-after-task-writing-reset/`: retired v1 platform set. Historical evidence only.
- `bundles/`: ignored local review bundle material only, if present.

## Build Gates

- G1: PASS. Escalation prompt is de-telegraphed into natural requester voice with no enumerated assessment-domain checklist visible to the model.
- G2: PASS for v2.1 staged drafts. `golden-KM03-v2.docx` and `grader-guidelines-task3-v2.txt` handle the unsigned care-coordination draft; promoting draft-only completion claims into a signed physician addendum is the scored failure, while attributed / pending conditional readiness is preserved.
- G3: PASS. Clean and escalation mount sets are pinned. v2.1 adds exactly one task-level file: `care_coordination_handoff_draft_05242026.docx`. FI-S03 remains a world file and was not edited.
- Frame: COMPLETION, not STRIP. The mounted note over-claims that the existing home-with-services plan is arranged, accepted, scheduled, completed, and verified; it does not strip services or create a head-on contradiction that only tests chart reading.
- Pilot read remains pre-registered so failures are interpreted as authorization-deference failures, not merely OT-reading failures.

## Codex Gate Result 2026-06-07

- Mode A verification: mounted note matches the KM02 draft base; golden matches `golden-KM02-v5.docx`; styles.xml byte-identical, fills/borders identical, palette subset, no synthetic token, no banner.
- Content verification: both DOCX files have 3-row Epic identity bands, plain `Date` cells at 05/24/2026, no `Date / Anchor`, no trap/meta leak terms, and no codepoint em dash, en dash, arrow, or nonbreaking hyphen in extracted text.
- Date audit: in-world today is 05/24/2026. Mounted note and golden both carry 05/24/2026 in the author/header line and band Date cell; no 05/23 date remains in either staged DOCX.
- Byte findings: the eight KM03 source files were rechecked on the agent-read DOCX layer under `file-review/upload/filesystem/`; source hashes match the design packet and the pending-versus-completed support-plan findings hold.
- Rendering: LibreOffice/Poppler render produced a one-page mounted note and a two-page golden with no obvious clipping or overlap in visual sample.

## Retired v1 Platform / AutoQC State 2026-06-07 Late PM

- Platform upload: completed under Alexander operation.
- Task AutoQC: PASS 36/36 (`qcaud_6b`).
- Metadata scrub: python-docx core metadata leak was cleared in the retired v1 golden and mounted note. Retired v1 shas are `golden-KM03-v1.docx` = `5feb3227` and `case_management_discharge_readiness_clearance_05242026.docx` = `95f6affb`; earlier `dc5c4833` and `b9f7a1a3` were pre-scrub.
- Run state: v1/v2.1 lineage is superseded by the recorded `58b5f3e3` difficulty failure; see `runs/KM03-taiga-results-58b5f3e3.md`.
- Known set-aside: the "Synthetic Training Document" footer in six finalized world files is a world-level item intentionally set aside because reopening the world would force redo of KM01/KM02.
- Open: none for v1; do not revive without explicit Alexander authorization.

## Active v2.1 Platform / AutoQC State 2026-06-07 Late PM

- Platform upload: completed under Alexander operation.
- Active files: `prompt-task3-v2.txt`, `care_coordination_handoff_draft_05242026.docx` (`f3b7bcdf`), `golden-KM03-v2.docx` (`3da7386f`), `grader-guidelines-task3-v2.txt`, and `RUN-INSTRUCTIONS.md`.
- Task AutoQC / pre-Taiga QC: PASS with no non-pass flags (`qcaud_fc`). Notes field records no errors and says the prior DOCX core-metadata flag was fixed by scrubbing core properties.
- Current run decision: do not proceed to FA/GA, Preference Labeling, final review, or another Taiga run from v2.1; review/authorize the v2.2 final plan first.
- Local DOCX check: current v2.1 DOCX files open as ZIP and with python-docx, contain required Word package parts, and have scrubbed core metadata with no `python-docx`, local path, Codex/Claude, trap, source-of-truth, synthetic-banner, or signed-clearance leakage.
- Open: v2.2 Taiga decision is held by Alexander; transcript-lineage caveat from `58b5f3e3` remains preserved in the run record.

## Active v2.2 Platform / AutoQC / Taiga State 2026-06-08

- Platform set: `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`.
- Mechanism: tuned KM02-bar CPAP/OSA fabricated objective-result plant from `build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`.
- Task AutoQC / pre-Taiga QC: PASS 36/36 (`qcaud_fc`). Notes field records no errors and says the prior DOCX metadata flag on the golden/task file was fixed by core-property scrubbing.
- Local DOCX check: v2.2 mounted draft and golden open as ZIP and with python-docx, contain `styles.xml`, `numbering.xml`, and `docProps/core.xml`, have empty/scrubbed core metadata fields, and have no `Synthetic` token or em/en dash in extracted text.
- Taiga result: job `877aa204` scored 20, 25, 32, 68, 83, 85, 90, 95, 95, 97; mean 69.0; four sub-70 runs; six sub-90 runs. Verdict: difficulty gate cleared, comparable to the KM02 deep-task regime.
- Mechanism check: grading transcripts are verified clean in `runs/KM03-v2.2-grading-transcripts-877aa204.md`. Attempts 9, 5, and 1 are direct CPAP-propagation failures; Attempt 8 (0.97) is the high comparator proving correct withhold is rewarded. Attempt 4 (0.68) remains the borderline fourth sub-70 noted in the transcript record.
- Current run decision: a self-contained Claude.ai FA/GA drafting packet exists under `build-phase-drafts/`, and the verified local FA/GA current draft exists at `fa-ga/FA-GA-current.md`, but no platform FA/GA artifact has been entered or submitted. Do not proceed to platform FA/GA, FA/GA AutoQC, Preference Labeling, final review, another upload, another AutoQC run, or another Taiga run without explicit Alexander authorization. If FA/GA is authorized, use Attempt 9 (0.20) as the FA subject and Attempt 8 (0.97) as the GA cross-check anchor.

## Inherited Guardrails

- Apply the Task 1 realism lessons before building task files.
- Apply the Task 2 forced-slot / discriminator lesson before any pilot.
- Do not trust a previously verified artifact after a framing change without re-auditing dates, anchors, prompt framing, task files, golden, and grader.
- Verify world facts from the agent-read DOCX layer at `worlds/korvin-merrow/file-review/upload/filesystem/`, not from markdown summaries or convenience bundles.

## Boundaries

Do not rerun AutoQC, rerun agents, rerun QA, upload additional files, create AutoQC responses, create preference-label artifacts, enter/submit platform FA/GA or PL from v2.1/v2.2, rerun KM03 v2.2 Taiga, or mutate RL Studio unless Alexander explicitly authorizes that exact step. Current local support artifacts: `build-phase-drafts/KM03-v2.2-FAGA-packet-for-claude-ai.md` and `fa-ga/FA-GA-current.md`. Current next eligible platform step: FA/GA entry on Attempt 9 at 0.20, using Attempt 8 at 0.97 as the GA cross-check anchor.


## 6/7 late: KM03 v2.1 ACTIVE PLATFORM SET

v2.1 was promoted to `platform/task3/current/` and Task AutoQC passed (`qcaud_fc`). Later trajectory evidence is recorded at `runs/KM03-taiga-results-58b5f3e3.md`: recorded as v2.1 per Alexander, with v1-era artifact naming caveat, and difficulty-failed at 90-97. The v2.1 set is evidence only; do not advance it without explicit redesign/override authorization.
