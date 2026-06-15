# Spec-stage upload readiness - Ondina Vasquell - 2026-06-13

Verdict: READY to upload the spec, the world reference files, and the transcripts. One caveat: the EW31 image is pending a Codex regeneration (audit fix); upload the corrected EW31, not the current one. Platform stays manual (decision 13) - this is the what-goes-where for Alexander to upload; nothing is auto-uploaded. Gate tools/verify/verify_ondina.py: PASS (60 docx). Leakage guard: PASS (no task/golden/external content in the world set; world files carry zero design or benchmark register).

## 2.1) Spec Document (one file)
- worlds/ondina-vasquell/submission/Alexander_World_Vasquell_latest_6_13.docx

## 2.2) Template / Reference Files - WORLD-LEVEL ONLY (34 files)
These become the shared world filesystem the agent reads on every task. Upload exactly these:
- 29 world DOCX: worlds/ondina-vasquell/phase-3-build-task-artifacts/world-files/*.docx
- 3 supplementary DOCX: worlds/ondina-vasquell/phase-3-build-task-artifacts/supplementary-files/*.docx
- 2 images: world-files/wound_photo_05202026.jpg and abi_tbi_tracing_05192026.jpg (upload the REGENERATED EW31 tracing per EW31-codex-regen-prompt.md; EW30 is ready)

## 2.3) Claude Transcripts (both required)
- worlds/ondina-vasquell/submission/Ondina_Vasquell_Brainstorm_Claude_Transcript.docx
- worlds/ondina-vasquell/submission/Ondina_Vasquell_World_Spec_Claude_Transcript.docx

## DO NOT UPLOAD in 2.2 (the leakage guard - this is what screws tasking if it leaks)
The following are NOT world files and must never enter the shared world reference bucket. They are uploaded later at Step 10 task setup, each WITH its own task, or stay internal:
- 9 task-level files (task-files/ and the copies in platform/taskN/current/) - mount each only with its task.
- 10 goldens, 10 task prompts, 10 grader guidelines, run-instructions, preregistrations, A0.5 records (platform/) - task-setup artifacts, writer-finalized; never in the world bucket.
- build/ scripts, all .md planning/audit docs, the manifest, the retrospective - internal only.
Why: a severity-forward external surface (denial, CDI query, coding worksheet, concurrent review) or a golden in the shared world filesystem would be visible to every task and pre-answer or contaminate the tasking. Exactly one task file may be visible per task, under its own volume (DO-NOT-REPEAT mount-coherence rule).

## After upload (Alexander-operated)
- Run Spec AutoQC (2.4); address or fix every non-pass flag; rerun until clean.
- Step 10 task setup: finalize goldens, mount each task file with its task, run Task AutoQC per task.
- Confirm at pilot time: `find /docs -type f` shows exactly the world set plus the one task file for that task; nothing task-specific in a second volume.

## Status of the brainstorm (Part 1)
Already uploaded and Brainstorm AutoQC PASS per the platform card; reviewer feedback pending. The expanded Brainstorm transcript is in 2.3 above.
