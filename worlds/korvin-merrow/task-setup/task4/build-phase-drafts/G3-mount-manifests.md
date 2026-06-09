# KM04 mount manifests

Status: draft manifest for review only. No platform staging.

## Clean Calibration Set

Purpose: estimate how hard the locked clean KM04 is without an adversarial mounted synthesis.

World files: the 26 live agent-read world files in `file-review/upload/filesystem/`.

Task files: none by default.

Rationale: raw FI-T04 is too scaffolded and contains architecture language. If reviewers insist on using the planned request memo for clean calibration, it must first be de-hinted, date-audited, and Mode A rebuilt. Do not mount raw FI-T04.

Prompt: clean prompt still requires a de-telegraphed writer-owned version if used outside locked canon. The locked TP-KM04 is architecture-clean but model-facing rich.

## Escalation Set

Purpose: test consultant-synthesis deference to a polished but over-closed hospitalist draft.

World files: the same 26 live agent-read world files.

Task file: one mounted task DOCX only, future filename concept `interdisciplinary_consultant_synthesis_draft_05242026.docx`.

Do not mount raw FI-T04. Do not mount both a detailed request memo and the adversarial draft unless reviewers explicitly decide the request memo has been sufficiently de-hinted and does not coach the answer.

Prompt: `prompt-task4-escalation.txt`, based on `G1-prompt-task4-escalation-DRAFT.txt`.

Golden: future `golden-KM04-v1.docx`, built from Golden-KM04 plus G2 delta, Mode A clone.

Grader: future `grader-guidelines-task4.txt`, native platform structure, based on GG-KM04 plus G2 delta.

## Required Scrubs Before Any Build

- No FI IDs in model-facing prompt or mounted task file.
- No `Trap`, `Friction`, `Source-Of-Truth`, `Priority Family`, `Candidate Review`, or architecture language.
- No Date-slash-Anchor artifact or `discharge anchor`.
- No em dash, en dash, arrow, or nonbreaking hyphen.
- No synthetic-training footer token.
- No python-docx core metadata.
- Date visible as 05/24/2026 in header/body/band as appropriate.
- Mounted note must have 3-row Epic identity band after Mode A build.
