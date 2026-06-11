# Git Workflow

Git is used for local checkpoints, rollback, and change review. Do not push or publish unless Alexander confirms the target remote is private and safe.

## Running git from the agent sandbox - the deletion-grant lesson (2026-06-11)

The agent's bash sandbox mounts this folder CREATE/OVERWRITE-ONLY by default: it can make and edit files, but UNLINK and RENAME are blocked. Every git WRITE command renames or removes files (the index lockfile, refs, objects), so `git add`, `git commit`, `git fetch`, `git merge`, `git pull`, `git push`, `git rebase`, `git reset`, `git checkout`, and clearing `.git/*.lock` all fail with "Operation not permitted" - as do plain `rm` and `mv`. Creating and overwriting files works, which is why an agent can edit the tree but (by default) not commit. This is the practical meaning of the old "sandbox = no git" environment note.

UNBLOCK IT WITH THE DELETION GRANT. When a delete (or any git write) fails with "Operation not permitted", call the cowork capability `mcp__cowork__allow_cowork_file_delete` with any path in the folder (for example `.git/index.lock`). The user approves once, and deletion is enabled for the WHOLE folder for the rest of the session. Verified 6/11: the grant lifts RENAME as well as unlink, so full git then works directly from the agent - we committed and pushed three commits this way. So the refined rule is: the sandbox cannot do git UNTIL the delete permission is granted; after the grant it can.

STALE LOCKS. A git op interrupted by the restriction (a `fetch`/`merge` that half-ran) leaves 0-byte `.git/HEAD.lock` / `.git/index.lock` that block every later git command. After the grant, clear them first: `rm -f .git/HEAD.lock .git/index.lock`.

IDENTITY. This repo is preconfigured `user.name = Claude Code`, `user.email = claude-code@sanctum.local`, so agent commits read as "Claude Code" unless you change them. To commit under the human author: `git config user.name "<name>" && git config user.email "<email>"`.

The workflow that worked (6/11):
1. If `rm`/git fails with "Operation not permitted", call `allow_cowork_file_delete` and have the user approve.
2. `rm -f .git/HEAD.lock .git/index.lock` to clear any stale locks.
3. Stage by LOGICAL change and commit in groups: `git add <paths> && git commit -m "..."` (one commit per coherent change set, not one giant commit).
4. `git push origin <branch>` only after the user approves the push.
5. Verify: `git status -sb` shows no ahead/behind, and `git log --oneline -5` shows the new commits.

Alternative: the environment also assigns git+delete to Codex; if the agent is not granted delete, hand the grouped commit commands to the user or Codex to run in a real terminal.

## Recommended Branches

- `main`: stable private baseline.
- `korvin-merrow-brainstorm`: current Brainstorm work and submitted artifacts.
- `korvin-merrow-world-spec`: future World Spec work after Brainstorm GO.
- `reviewer-fixes/*`: human reviewer feedback revisions.
- `autoqc-fixes/*`: AutoQC remediation branches.

Current note (2026-06-11): the active branch is `korvin-merrow-brainstorm`, tracking `origin/korvin-merrow-brainstorm` and in sync with it after the 6/11 push (commits `cb22931`, `3e1522f`, `a3d9ecf`). The `james-carter-brainstorm` remote branch still exists as a historical branch-name artifact, not a current patient-identity signal; do not rename without Alexander's remote-strategy approval.

## Tagging Strategy

Suggested tags:

- `v0-brainstorm-submitted`
- `v1-brainstorm-approved`
- `v2-world-spec-submitted`
- `v3-world-spec-approved`

Use tags only after the milestone has actually occurred.

## Checkpoint Commit Examples

```powershell
git add WORKSPACE_FILE_MAP.md (root; Active task status section) worlds/korvin-merrow/reviews/brainstorm-autoqc-02.md
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
- Update `WORKSPACE_FILE_MAP.md (root; Active task status section)`.
- Commit a checkpoint.

## Collaborator Session Exit Discipline

Every Codex, Claude, or writer session must leave the repository in a clean handoff state so the next collaborator can reconstruct state from repository files alone.

Before ending a working session:

1. Confirm the working tree is clean, or explicitly document any uncommitted state.
2. Confirm `WORKSPACE_FILE_MAP.md (root; Active task status section)` and `docs/status-dashboard.md` reflect the current phase and next eligible phase.
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
