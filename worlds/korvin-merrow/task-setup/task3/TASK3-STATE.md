# TASK3-STATE

Status: KM03 escalation FAILED through v2.1; redesign to v2.2 needed. Per Alexander, v2.1 is too easy (Taiga job 58b5f3e3, 10 trajectories 90-97, mean ~93.6, zero sub-70, fails the difficulty gate). Lineage: v1 too easy -> v2.1 -> v2.1 also too easy. (Byte note: the captured transcripts carry v1-era naming/audit prompt/golden-v1; recorded as v2.1 per Alexander, worth a 30-sec confirm of which set executed - does not change the conclusion.) KM04 v1 failed the same gate (job 55ee209f, mean 0.912), so the whole "evaluate/reconcile a handed discharge document" family is too easy for this model.

ROOT CAUSE: KM03/KM04 are caution-genre tasks; the model's trained default (be cautious, preserve conditionality, do not rubber-stamp) IS the correct answer, so caution is free and there is no forced wrong commitment. Source-authority tweaks do not fix this.

v2.2 DIRECTION (the only mechanism that ever produced a Korvin sub-70 = KM02 completion-propagation): flip the genre from "evaluate readiness" to "finalize/file the discharge-planning document of record"; plant a finding-like false completed-coordination OUTCOME on a COLD axis (e.g. in-home safety eval completed / agency start-of-care completed - NOT prednisone/cardiorenal, which the model hunts); grader scores propagation of that finding into the filed document, not "preserved conditional readiness". Full strategy + cross-agent review questions: `build-phase-drafts/KM03-v2.2-strategy-draft.md`. Same medicine likely applies to KM04. DRAFT only; no build/stage/upload; pending Alexander + cross-agent (Claude.ai/Codex) review then build authorization.

Task: KM03 - discharge planning documentation escalation. Status: failed through v2.1 and awaiting v2.2 redesign authorization.

## Current Material

- `design/KM03-design-plan-for-review.md`: pre-build design plan that inherits the Task 1 and Task 2 lessons.
- `KM03-3rd-reader-review-and-build-gates.md`: third-reader review confirming the design direction but blocking build until G1-G3 close.
- `build-phase-drafts/`: draft packet for reviewing G1-G3 closure concepts. Source drafts and copied inputs are trackable; the local ZIP bundle is ignored.
- `build-phase-drafts/01-build-phase-review-responses.md`: build-phase review response record. Captures the frame decision from STRIP to COMPLETION and the v2.1 source-authority correction.
- `KM03-state-log.md`: live event log for KM03 after staging, including Task AutoQC pass and trajectory/QA state.
- `../platform/task3/current/`: prior KM03 v2.1 platform set. It is evidence only after the difficulty failure, not a shipping candidate.
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
- Current run decision: do not proceed to FA/GA, Preference Labeling, final review, or another Taiga run from v2.1; review/authorize v2.2 redesign first.
- Local DOCX check: current v2.1 DOCX files open as ZIP and with python-docx, contain required Word package parts, and have scrubbed core metadata with no `python-docx`, local path, Codex/Claude, trap, source-of-truth, synthetic-banner, or signed-clearance leakage.
- Open: v2.2 redesign review/authorization, with the transcript-lineage caveat preserved in the run record.

## Inherited Guardrails

- Apply the Task 1 realism lessons before building task files.
- Apply the Task 2 forced-slot / discriminator lesson before any pilot.
- Do not trust a previously verified artifact after a framing change without re-auditing dates, anchors, prompt framing, task files, golden, and grader.
- Verify world facts from the agent-read DOCX layer at `worlds/korvin-merrow/file-review/upload/filesystem/`, not from markdown summaries or convenience bundles.

## Boundaries

Do not rerun AutoQC, rerun agents, rerun QA, upload additional files, create AutoQC responses, create preference-label artifacts, write FA/GA or PL from v2.1, redesign v2.2, or mutate RL Studio unless Alexander explicitly authorizes that exact step. Current next step: review the v2.2 strategy, not another v2.1 platform action.


## 6/7 late: KM03 v2.1 ACTIVE PLATFORM SET

v2.1 was promoted to `platform/task3/current/` and Task AutoQC passed (`qcaud_fc`). Later trajectory evidence is recorded at `runs/KM03-taiga-results-58b5f3e3.md`: recorded as v2.1 per Alexander, with v1-era artifact naming caveat, and difficulty-failed at 90-97. The v2.1 set is evidence only; do not advance it without explicit redesign/override authorization.
