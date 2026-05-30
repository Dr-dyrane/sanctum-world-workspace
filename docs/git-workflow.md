# Git Workflow

Git is used for local checkpoints, rollback, and change review. Do not push or publish unless Alexander confirms the target remote is private and safe.

## Recommended Branches

- `main`: stable private baseline.
- `james-carter-brainstorm`: current Brainstorm work and submitted artifacts.
- `james-carter-world-spec`: future World Spec work after Brainstorm GO.
- `reviewer-fixes/*`: human reviewer feedback revisions.
- `autoqc-fixes/*`: AutoQC remediation branches.

## Tagging Strategy

Suggested tags:

- `v0-brainstorm-submitted`
- `v1-brainstorm-approved`
- `v2-world-spec-submitted`
- `v3-world-spec-approved`

Use tags only after the milestone has actually occurred.

## Checkpoint Commit Examples

```powershell
git add project/STATUS.md worlds/james-carter/reviews/brainstorm-autoqc-02.md
git commit -m "checkpoint: record brainstorm autoqc pass"

git add worlds/james-carter/submission/Korvin_Merrow_Brainstorm.docx
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

## Remote Safety

This workspace currently has an `origin` remote configured. Before any push, verify:

- remote is private
- no prohibited source docs or secrets are staged
- `.gitignore` protects credentials and local exports
- Alexander approves the push

