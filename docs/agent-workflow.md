# Agent Workflow

## Authority Model

Alexander is the physician expert, clinical source of truth, and final approver.

Assistants may help structure, audit, format, and manage continuity. Assistants must not replace physician judgment.

## Codex Role

Codex is the local workspace manager:

- reads `STATUS.md` first
- checks phase gates
- organizes files
- indexes source-of-truth materials
- manages git checkpoints
- prepares Claude-ready inputs
- audits Claude output
- simulates reviewer risks
- records AutoQC and reviewer feedback

Codex must stop before irreversible actions such as RL Studio submission, browser control, external access, or phase advancement unless explicitly authorized.

## Claude Role

Claude is the official Sanctum drafting assistant when the instruction guide recommends it.

Claude may:

- conduct structured interviews
- organize physician-provided decisions
- draft template structure after authorization
- improve consistency and formatting
- run reviewer-style critique

Claude must not:

- originate scenario concept, traps, task ideas, or final clinical decisions
- write final task prompts from scratch
- write golden responses, grader guidelines, or failure analysis during onboarding
- introduce unsupported clinical facts, dates, lab values, medications, doses, or file names

## ChatGPT Role

ChatGPT may be used as an ad hoc reasoning, review, or critique assistant if Alexander chooses. It follows the same boundaries as Codex and Claude.

Any ChatGPT output should be treated as advisory, not authoritative.

## Phase Gates

- Brainstorm Human Review must return GO before World Spec drafting.
- World Spec must clear AutoQC and Human Review before onboarding completion.
- Do not proceed to steps 7-17 without explicit phase update.

## Authorship And Good Faith Compliance

- Physician-originated clinical reasoning should remain visible.
- AI assistance should be used for structure and audit, not ghost-authoring prohibited content.
- Task prompts must come from Alexander.
- AutoQC disagreements should be documented honestly.
- Reviewer feedback should be preserved in RL Studio and locally summarized.

