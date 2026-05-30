# Identity Migration Log

Date: 2026-05-30

## Summary

Old working name: James Carter

New current patient identity: Korvin Merrow

Reason: Human reviewer Stacey S required an unmistakably fictional name because the prior working name could be a real common name.

Scope: full active/current project identity migration. Historical reviewer and audit artifacts were preserved with notes rather than rewritten.

## Current Status

- Brainstorm SEND BACK remediation is in progress.
- World Spec is not authorized.
- RL Studio reupload is not authorized yet.
- Comorbidity expansion and medication specificity still require Alexander's physician approval before being incorporated into the final Brainstorm.

## Files And Paths Changed

Active identity/content files:

- `AGENTS.md`
- `README.md`
- `docs/git-workflow.md`
- `docs/security-and-privacy.md`
- `docs/status-dashboard.md`
- `docs/reviewer-response-protocol.md`
- `project/PASS_PLAN.md`
- `project/EXECUTION_CHECKLIST.md`
- `project/STATUS.md`
- `project/WORKSPACE_FILE_MAP.md`
- `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`

Claude package:

- `claude-package/04_JAMES_CARTER_CONTEXT.md` renamed to `claude-package/04_KORVIN_MERROW_CONTEXT.md`
- `claude-package/05_EXECUTION_STATE.md`
- `claude-package/06_HANDOFF_STATE.md`

World folder:

- `worlds/james-carter/` renamed to `worlds/korvin-merrow/`

Future-facing world files:

- `worlds/korvin-merrow/brainstorm.md`
- `worlds/korvin-merrow/clinical-logic.md`
- `worlds/korvin-merrow/frictions.md`
- `worlds/korvin-merrow/traps.md`
- `worlds/korvin-merrow/task-map.md`
- `worlds/korvin-merrow/world-spec.md`
- `worlds/korvin-merrow/JAMES_CARTER_PASS_PLAN.md` renamed to `worlds/korvin-merrow/KORVIN_MERROW_PASS_PLAN.md`
- `worlds/korvin-merrow/reviewer-feedback.md`
- `worlds/korvin-merrow/world-spec-prep/claude-review-triage.md`
- `worlds/korvin-merrow/world-spec-prep/decision-register.md`
- `worlds/korvin-merrow/world-spec-prep/post-go-interview-plan.md`
- `worlds/korvin-merrow/world-spec-prep/readiness-map.md`

Submission artifact:

- `worlds/korvin-merrow/submission/James_Carter_Brainstorm.docx` removed
- `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx` created as interim remediation artifact

Reviewer-remediation files:

- `worlds/korvin-merrow/rename-audit.md`
- `worlds/korvin-merrow/reviewer-comorbidity-decision-brief.md`
- `worlds/korvin-merrow/reviewer-medication-decision-brief.md`

## Historical Files Intentionally Left With Old Name

These files are preserved as historical evidence. Notes were added where appropriate:

- `worlds/korvin-merrow/brainstorm-development-history.md`
- `worlds/korvin-merrow/brainstorm-internal-audit.md`
- `worlds/korvin-merrow/reviews/brainstorm-autoqc-01.md`
- `worlds/korvin-merrow/reviews/claude-brainstorm-review-01.md`
- `worlds/korvin-merrow/reviews/claude-brainstorm-review-response-01.md`

Historical note text used:

```text
Historical artifact used prior working name James Carter; current patient identity is Korvin Merrow.
```

## Branch Status

Current branch: `james-carter-brainstorm`

Remote tracking branch: `origin/james-carter-brainstorm`

Remote exists: `origin` at `https://github.com/Dr-dyrane/sanctum-world-workspace.git`

Pushed status at audit time: branch tracks remote and is ahead locally.

Proposed branch name: `korvin-merrow-brainstorm`

Branch rename not performed yet. Do not force push without Alexander approval.

Exact commands for later approval:

```powershell
git branch -m korvin-merrow-brainstorm
git push origin -u korvin-merrow-brainstorm
git push origin --delete james-carter-brainstorm
```

The final delete command should only be run after confirming the new remote branch exists and Alexander approves removing the old remote branch.

## Search Verification

Search command:

```powershell
rg -n --hidden -g '!**/.git/**' -g '!**/__pycache__/**' -g '!**/.cache/**' "James Carter|James_Carter|JAMES_CARTER|james-carter"
```

Remaining occurrences are classified as:

- Historical old-name artifacts.
- Migration/audit documentation.
- Current branch name pending approval for branch rename.

No active current submission source, current submission DOCX filename, Claude current context filename, or future-facing world folder uses the old patient identity.

## Remaining Reviewer Fixes

Already prepared:

- `World Type: Typical Clinical World` added to Brainstorm source and interim DOCX.
- Synthetic identity migrated to Korvin Merrow.
- Comorbidity decision brief created.
- Medication decision brief created.

Still requires Alexander approval:

- Which comorbidities to add.
- Which medications and doses to include.
- Whether to use compact or full medication list format in the Brainstorm.
- Whether to regenerate final DOCX after those approved clinical edits.

## Guardrails

- Do not reupload yet.
- Do not start World Spec.
- Do not alter historical reviewer evidence blindly.
- Do not lock proposed comorbidities or medications until Alexander approves them.
