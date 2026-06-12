# 2a - Substrate arming map (the bridge from Phase 1 to the chart)

Only open this AFTER the Phase 1 task-and-trap plan is locked. The world is now built to ARM the traps you designed, not the other way around. Every file exists because a task needs it for a correct answer.

## The arming principle

For each Phase-1 trap, the chart must document the contradiction or mandate that makes the wrong move the model's own fault, and it must do so QUIETLY and across more than one document (single-source, loud contradictions clear). World files provide raw material, never the answer-key synthesis. If one task legitimately needs a completed synthesis, scope it as a task-level file and explain why the user lacks it.

## Arming table (fill in, one row per trap)

| Task | Trap | The contradiction/mandate to document | Documents that carry it | Cross-doc synthesis required | The tempting wrong value the chart also supports on its surface |
|---|---|---|---|---|---|
| T1 | | | | | |
| T2 | | | | | |
| T3 | | | | | |
| T4 | | | | | |
| T5 | | | | | |

## World spec build (downstream of the table)

Use `reference/world-spec-guidelines/` (01 required structure, 02 rubric checklist, 03 common mistakes, 04 AutoQC requirements, 09 writer playbook) and the spec templates in `reference/templates/`. Build the spec packages in `world-spec-prep/` (identity, comorbidity, medication, timeline, provider roster, baseline anchors, daily course, governance). Generalize from korvin-merrow's `world-spec-prep/` only as a worked example; do not copy its content.

## Standing substrate rules (paid for on KM)

- Minimum 30 world-level files (pod rule, 06/10).
- Verify world facts against the agent-read docx at `file-review/upload/filesystem/` with python-docx INCLUDING table cells, never against markdown convenience copies.
- Every encounter and deliverable strictly AFTER the world snapshot date; nothing future-dated, ever.
- On any framing change later, re-audit every surviving artifact's dates, voice, status fields, and grader chart-access setting.
- A task-context file is optional and dangerous: realistic, correctly dated, free of project artifacts, NECESSARY, and never an answer manual. Delete any file that tells the model how to complete the deliverable.
- Names new to the world checked for collisions across all files; facility and provider names consistent throughout.

## Self-check before Phase 3

- [ ] Every Phase-1 trap has a row here and is armed by a documented contradiction or mandate.
- [ ] No trap relies on chart silence.
- [ ] Each contradiction is quiet and spread across 2+ documents.
- [ ] No answer-key synthesis sits in a shared world file.
- [ ] All dates post-snapshot; facility and provider names consistent; >=30 files.
