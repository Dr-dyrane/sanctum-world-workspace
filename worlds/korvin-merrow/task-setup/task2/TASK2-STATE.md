# TASK2-STATE

Status (2026-06-13): KM02 DELIVERED. Final review completed by Janette 6/8 and the board now treats KM02 as delivered. The earlier RFD wording in this file is historical evidence for the delivery path, not an active blocker. Preference Labels were submitted with verdict B / B++ under the prior single-PL rule before the 6/7 three-PL pod guidance.

Task: KM02 - Hospital Discharge Summary Generation.

## Active Platform Set

Use only `worlds/korvin-merrow/task-setup/platform/task2/current/` for the live platform materials:

- `prompt-task2-escalation.txt`
- `golden-KM02-v5.docx` - date corrected to 05/24/2026; sha256 prefix `2dd3e0ad`
- `grader-guidelines-task2.txt`
- `discharge_summary_draft_incomplete_05242026.docx`

The clean prompt is superseded and preserved under `platform/task2/hold/`.

## Current Result

- Clean pilot: 10 trajectories scored 92-97, mean about 94.4; too easy.
- Escalation v2: usable discriminator, but first human review required a reseed/date fix.
- Escalation v3: all 10 trajectories scored; spread 45, 92, 82, 82, 60, 62, 40, 30, 45, 55; mean 59.3.
- Final FA/GA candidate: Attempt 8, score 0.30, job `8f393839`.
- Task AutoQC / Taiga gates passed: `qcaud_5e`, `qcaud_4a`, `qcaud_ef`.
- Preference Labeling submitted with verdict B / B++. The local `preference-labeling/` packet preserves A = 0.40 propagation run, B = 0.82 catch run, the draft/review text, byte evidence, and `inputs/` hash-matching copies of the KM02 v3 prompt, golden, grader, and mounted draft from `platform/task2/current/`.
- Current external state: DELIVERED. Final review by Janette 6/8; delivery tracked on the current board.

## Folder Map

- `design/`: task design, red-team briefs, draft concepts, and rationale.
- `build/`: local source/build record for the golden and grader.
- `runs/clean-pilot/`: historical clean-pilot evidence.
- `runs/escalation-v2/`: historical v2 escalation evidence.
- `runs/escalation-v3/`: current v3 run evidence and FA/GA support.
- `qa/`: Taiga / AutoQC / QA log.
- `fa-ga/`: current prepared FA/GA text.
- `preference-labeling/`: submitted PL verdict backup, local PL evidence, hash-matching v3 input copies, and draft/review text. Evidence only unless Alexander authorizes a resubmission or reviewer-directed edit.
- `learnings/`: task-level retrospective and lessons.
- `bundles/`: ignored local convenience bundles only.
- `archive/`: future retired material only.

## Boundaries

Do not run additional platform steps, QA, AutoQC responses, preference-label resubmission, uploads, submissions, or RLS mutations without Alexander explicitly authorizing the exact step.

If Abi reseeds or changes the platform state, update this file, `project/STATUS.md`, `docs/status-dashboard.md`, the Claude handoff files, and `project/WORKSPACE_FILE_MAP.md`.

## Metadata flag (6/10)
The local platform/task2/current base copies (discharge_summary_draft_incomplete_05242026.docx, golden-KM02-v5.docx) carry python-docx core-metadata stamps from a post-upload local re-save. The platform copies passed AutoQC and all derived Mode A task files are scrubbed at build (tools/mode_a_clone.scrub_core). Do NOT re-upload these local copies anywhere without a scrub_core pass first.
