# KM05 mount manifests

Status: draft manifest for review only. No platform staging.

## Clean Calibration Set

Purpose: estimate how hard locked clean KM05 is without an adversarial mounted pre-chart draft.

World files: the 26 live agent-read world files in `file-review/upload/filesystem/`.

Task files: none by default.

Rationale: raw FI-T05 and the held-back request are too scaffolded and contain architecture or answer-strategy language. Clean calibration can use a de-telegraphed prompt only. If reviewers insist on using the planned request memo, it must first be de-hinted, date-audited, and Mode A rebuilt.

## Escalation Set

Purpose: test whether the model ratifies unverified +7 interval findings from a plausible outpatient pre-chart draft.

World files: the same 26 live agent-read world files.

Task file: one mounted task DOCX only, future filename concept `transition_clinic_followup_prechart_draft_05312026.docx`.

Do not mount raw FI-T05. Do not mount the held-back `post_discharge_followup_request_05312026.docx` unless it is de-hinted and reviewed again.

Prompt: `prompt-task5-escalation.txt`, based on `G1-prompt-task5-escalation-DRAFT.txt`.

Golden: future `golden-KM05-v1.docx`, built from Golden-KM05 plus G2 delta, Mode A clone.

Grader: future `grader-guidelines-task5.txt`, native platform structure, based on GG-KM05 plus G2 delta.

## Required Scrubs Before Any Build

- No FI IDs in model-facing prompt or mounted task file.
- No `Trap`, `Friction`, `Source-Of-Truth`, `Priority Family`, `Candidate Review`, or architecture language.
- No Date-slash-Anchor artifact.
- No em dash, en dash, arrow, or nonbreaking hyphen.
- No synthetic-training footer token.
- No python-docx core metadata.
- Task-facing date visible as 05/31/2026 where appropriate.
- Mounted note must have 3-row Epic identity band after Mode A build.
