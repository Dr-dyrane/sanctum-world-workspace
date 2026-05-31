# Rename Audit

Date: 2026-05-30

Reviewer: Stacey S

Reviewer request: replace the prior common patient name with unmistakably fictional identity `Korvin Merrow`, including document title and submission filename.

## Files Changed For Active Remediation

Active project/context files:

- `AGENTS.md`
- `README.md`
- `docs/git-workflow.md`
- `docs/security-and-privacy.md`
- `docs/status-dashboard.md`
- `project/PASS_PLAN.md`
- `project/STATUS.md`
- `project/WORKSPACE_FILE_MAP.md`
- `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`

Claude package:

- `claude-package/04_KORVIN_MERROW_CONTEXT.md`
- `claude-package/05_EXECUTION_STATE.md`
- `claude-package/06_HANDOFF_STATE.md`

Active world files:

- `worlds/korvin-merrow/active/brainstorm.md`
- `worlds/korvin-merrow/active/clinical-logic.md`
- `worlds/korvin-merrow/active/frictions.md`
- `worlds/korvin-merrow/active/traps.md`
- `worlds/korvin-merrow/active/task-map.md`
- `worlds/korvin-merrow/active/world-spec.md`
- `worlds/korvin-merrow/planning/KORVIN_MERROW_PASS_PLAN.md`
- `worlds/korvin-merrow/reviews/reviewer-feedback.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/claude-review-triage.md`
- `worlds/korvin-merrow/world-spec-prep/decision-logs/decision-register.md`
- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/post-go-interview-plan.md`
- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/readiness-map.md`

Submission artifact:

- Removed old remediation target: `worlds/korvin-merrow/submission/James_Carter_Brainstorm.docx`
- Created renamed remediation artifact: `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`
- Renamed `claude-package/04_JAMES_CARTER_CONTEXT.md` to `claude-package/04_KORVIN_MERROW_CONTEXT.md`
- Renamed `worlds/korvin-merrow/JAMES_CARTER_PASS_PLAN.md` to `worlds/korvin-merrow/planning/KORVIN_MERROW_PASS_PLAN.md`

New reviewer-remediation files:

- `worlds/korvin-merrow/remediation/reviewer-comorbidity-decision-brief.md`
- `worlds/korvin-merrow/remediation/reviewer-medication-decision-brief.md`
- `worlds/korvin-merrow/history/rename-audit.md`

## Search Results

Command:

```powershell
rg -n --hidden -g '!**/.git/**' -g '!**/__pycache__/**' -g '!**/.cache/**' -g '!worlds/korvin-merrow/reviews/**' -g '!worlds/korvin-merrow/history/brainstorm-development-history.md' -g '!worlds/korvin-merrow/history/brainstorm-internal-audit.md' -g '!worlds/korvin-merrow/history/rename-audit.md' "James Carter|James_Carter|JAMES_CARTER"
```

Result:

```text
No matches.
```

Full repository search still finds the prior name only in historical archives:

```text
worlds/korvin-merrow/history/brainstorm-development-history.md
worlds/korvin-merrow/history/brainstorm-internal-audit.md
worlds/korvin-merrow/reviews/claude-brainstorm-review-01.md
worlds/korvin-merrow/reviews/brainstorm-autoqc-01.md
```

## Confirmation

- Active Brainstorm source uses `Korvin Merrow`.
- Active Brainstorm source title uses `Korvin Merrow World Brainstorm`.
- Submission DOCX title uses `Korvin Merrow World Brainstorm`.
- Submission DOCX file name is `Korvin_Merrow_Brainstorm.docx`.
- `World Type: Typical Clinical World` is present in the active Brainstorm source and DOCX.
- No active, non-historical file contains the prior patient name or prior uppercase filename slug, excluding this audit's own historical search documentation.

## Historical Archive Exception

The prior name remains in historical artifacts only so the project record preserves the original reviewer/Audit trail. These files should not be used as current submission content.
