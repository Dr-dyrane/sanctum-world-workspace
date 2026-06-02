# Git Workflow

Git is used for local checkpoints, rollback, and change review. Do not push or publish unless Alexander confirms the target remote is private and safe.

## Recommended Branches

- `main`: stable private baseline.
- `korvin-merrow-brainstorm`: current Brainstorm work and submitted artifacts.
- `korvin-merrow-world-spec`: future World Spec work after Brainstorm GO.
- `reviewer-fixes/*`: human reviewer feedback revisions.
- `autoqc-fixes/*`: AutoQC remediation branches.

Current note: the active local branch may still be `james-carter-brainstorm` because it tracks `origin/james-carter-brainstorm` and is ahead by local commits. Treat that as a known historical branch-name mismatch, not a current patient-identity signal. Rename only after Alexander approves the remote strategy.

## Tagging Strategy

Suggested tags:

- `v0-brainstorm-submitted`
- `v1-brainstorm-approved`
- `v2-world-spec-submitted`
- `v3-world-spec-approved`

Use tags only after the milestone has actually occurred.

## Checkpoint Commit Examples

```powershell
git add project/STATUS.md worlds/korvin-merrow/reviews/brainstorm-autoqc-02.md
git commit -m "checkpoint: record brainstorm autoqc pass"

git add worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx
git commit -m "checkpoint: rebuild brainstorm using official docx template"
```

## Rollback Commands

Inspect recent history:

```powershell
git log --oneline -10
```

View a file at a previous checkpoint:

```powershell
git show <commit>:path/to/file
```

Restore one file from a checkpoint:

```powershell
git restore --source <commit> -- path/to/file
```

Create a recovery branch before risky changes:

```powershell
git switch -c reviewer-fixes/<topic>
```

Avoid destructive commands like `git reset --hard` unless Alexander explicitly requests them.

## Clean Working Tree Before RL Studio Upload

Before upload:

```powershell
git status --short --branch
git diff
```

Recommended rule:

- Clean working tree, or
- only known, intentional upload-related changes pending.

After upload or AutoQC:

- Save results locally.
- Update `project/STATUS.md`.
- Commit a checkpoint.

## Collaborator Session Exit Discipline

Every Codex, Claude, or writer session must leave the repository in a clean handoff state so the next collaborator can reconstruct state from repository files alone.

Before ending a working session:

1. Confirm the working tree is clean, or explicitly document any uncommitted state.
2. Confirm `project/STATUS.md` and `docs/status-dashboard.md` reflect the current phase and next eligible phase.
3. Confirm locked artifacts were not changed unless Alexander explicitly authorized the change.
4. Confirm candidate artifacts are clearly located and status-labeled.
5. Confirm newly locked artifacts have been moved to locked paths and ratification records are created and referenced.
6. Confirm continuity surfaces and Claude handoff files are updated.
7. Confirm stale active candidate paths are removed or explicitly marked historical.
8. Confirm no unauthorized files were created.
9. Confirm carry-forward watch items and future task-layer guidance are preserved.
10. Create a checkpoint commit for completed work unless Alexander explicitly instructs not to commit.

Final reports must state what changed, what did not change, current status, next eligible phase, and whether the repository is safe for another collaborator to continue.

## Remote Safety

This workspace currently has an `origin` remote configured. Before any push, verify:

- remote is private
- no prohibited source docs or secrets are staged
- `.gitignore` protects credentials and local exports
- Alexander approves the push
