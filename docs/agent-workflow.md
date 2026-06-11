# Agent Workflow

## Authority Model

Alexander is the physician expert, clinical source of truth, and final approver.

Assistants may help structure, audit, format, and manage continuity. Assistants must not replace physician judgment.

## Codex Role

Codex is the local workspace manager:

- reads `STATUS.md` first
- checks phase gates
- checks `WORKSPACE_FILE_MAP.md` before file creation, moves, renames, deletion, or restructuring
- updates `WORKSPACE_FILE_MAP.md` when structure, official sources/templates, submission artifacts, or duplicate-purpose files change
- organizes files
- indexes source-of-truth materials
- manages git checkpoints
- prepares Claude-ready inputs
- audits Claude output
- simulates reviewer risks
- records AutoQC and reviewer feedback

Codex must stop before irreversible actions such as RL Studio submission, browser control, external access, or phase advancement unless explicitly authorized.

## @data-analytics convention (standing rule, 2026-06-10)

Mentioning `@data-analytics` in a request invokes the data-analytics flow: load the reusable Korvin semantic layer, read the relevant workspace sources (state files, run records, dashboards, performance xlsx), and answer with verified facts plus analysis, forecasts, tables, charts, or reports. Use it for concrete analytics questions, for example: predict KM07/KM08 scores, audit the dashboard against the performance report, summarize pending work by task, build a score distribution table. Ground rules: answers are source-backed from local files, not chat memory; verified numbers are cited from the banked run records; score forecasts made before a pilot are banked as preregistration files under `taskN/runs/` (pattern: KM07-v2 and KM08-v4.1 preregistrations, 6/10) and are not edited after the pilot lands.

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
- Steps 7-17 require explicit phase update or direct Alexander authorization.
- For Korvin specifically, six tasks are delivered (KM01 through KM06) and four are under first human review (KM07 through KM10, KM07 being the fairness-corrected v3). For the current gate use the live status sources (`dashboard/km-world-dashboard.html`, `worlds/korvin-merrow/task-setup/KM-WORLD-PERFORMANCE-REPORT.md`, root `WORKSPACE_FILE_MAP.md`, the active `TASKN-STATE.md`), not this historical onboarding summary. The old `project/STATUS.md` pointer is obsolete (archived in the 6/9 restructure).

## Authorship And Good Faith Compliance

- Physician-originated clinical reasoning should remain visible.
- AI assistance should be used for structure and audit, not ghost-authoring prohibited content.
- Task prompts must come from Alexander.
- AutoQC disagreements should be documented honestly.
- Reviewer feedback should be preserved in RL Studio and locally summarized.
