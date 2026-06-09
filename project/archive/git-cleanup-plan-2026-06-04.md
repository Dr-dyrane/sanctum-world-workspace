# Git Cleanup Plan (for Codex, post spec-submission)

Date: 2026-06-04. Goal: clean tree, future-ready workspace. Sandbox cannot delete or commit; Codex executes. Verify each step's file list against live `git status` (sandbox sees mount ghosts the real env may not).

## 0. Clear stale lock first
`.git/index.lock` may exist (sandbox commit attempts). Remove before any operation.

## 1. Deletions (git rm / fs delete)
- `korvin-merrow-final-submission-staging/01_spec-document/Korvin_Merrow_World_Spec.docx` - superseded by Alexander_World_Merrow_latest_6_4.docx.
- `korvin-merrow-final-submission-staging/02_template-reference-files/world-level/` and `/supplementary/` (the 26 plain pandoc drafts) - superseded by `/final/`.
- `korvin-merrow-final-submission-staging/02_template-reference-files/pretty/` - intermediate generation (FI-named); the artisan FI-W01 sample is preserved in worlds/korvin-merrow/reference-file-design/samples/. Keep /final/ only.
- Drive-package mirror stale files per korvin-merrow-drive-package/CODEX_SYNC_GO.md section 1.
- `_probe_overwrite.md` at repo root (sandbox write-capability probe; delete).
- `worlds/korvin-merrow/final-submission-resolution/candidate-review/` leftovers if both files still exist there (locked/ copies are canonical).

## 2. Commit groups (suggested order)
1. `checkpoint: spec autoqc remediation rounds 1-5 and final spec` - Alexander_World_Merrow_latest_6_4.docx, worlds/korvin-merrow/autoqc-remediation/, updated staging transcript DOCX/PDF.
2. `checkpoint: final reference file set and design system` - 02_template-reference-files/final/ (33), worlds/korvin-merrow/reference-file-design/.
3. `checkpoint: workspace guardrails, playbook, and preflight checklist` - docs/workspace-guardrails-lessons.md, docs/world-pipeline-playbook.md, reference/checklists/spec-autoqc-preflight.md, tools/generate_reference_files.py, project/GIT_CLEANUP_PLAN.md.
4. `checkpoint: governance and review records` - worlds/korvin-merrow/final-submission-resolution/world-spec-docx-bring-home-plan.md, worlds/korvin-merrow/reviews/stacey-corrections-recovery-report.md, korvin-merrow-drive-package/ (tree + GO doc; binaries optional, see 3).
5. `checkpoint: continuity surfaces post spec submission` - project/STATUS.md, claude-package updates, deletions from section 1.

## 3. .gitignore decisions (propose, Alexander confirms)
- Consider ignoring `korvin-merrow-drive-package/**/*.docx|pdf` (duplicates of staging binaries; tree + GO doc stay tracked). Alternative: track everything for provenance - repo size cost ~5 MB, acceptable either way.
- Do NOT add blanket `*.docx` ignores - staging finals are submission provenance.

## 4. Branch
Longstanding pending item: rename `james-carter-brainstorm` -> `korvin-merrow` (or `main`). After spec submission is a natural moment: create new branch from HEAD, push, set upstream, retire old name. Needs Alexander's go (remote tracking).

## 5. Mount-ghost files - DO NOT bulk-commit
These may show modified in some environments due to the known truncation/CRLF artifact: claude-package/04+06, reference/world-spec-guidelines/08_autoqc_master_index.md, worlds/korvin-merrow/active/clinical-logic.md, world-spec-prep/locked/{comorbidity,daily-hospital-course,provider-roster,surgical-history}*, two ratifications. In the REAL environment check `git diff` per file: commit only if the diff is a genuine content change someone made; otherwise restore from HEAD. Never commit a file whose working copy ends mid-sentence.

## 6. Future-world scaffold (optional, cheap now)
`mkdir worlds/_skeleton` mirroring korvin-merrow's folder tree with .gitkeep files, per docs/world-pipeline-playbook.md section B - makes World #2 a copy operation.

## 7. Exit criteria
- `git status` clean.
- Branch question answered.
- Tag suggestion: `git tag korvin-spec-submitted` at the final commit.
