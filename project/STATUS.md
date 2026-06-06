# Project Status

## Current Phase

World Spec APPROVED (2026-06-04). Execution Artifact Generation COMPLETE; RL Studio upload and Spec AutoQC COMPLETE under Alexander's direct authorization and operation. Final AutoQC board: 108/109 pass; the sole open flag is Home Medications (prednisone dose/frequency), the world's intentional central source-of-truth design, justified in Spec AutoQC Notes (field 2.5). Human World Spec Review is APPROVED by Stacey S. Engineering pipeline run #1 completed; Step 9 / "Ready for Pipeline Fixes" is CLOSED. Final Files AutoQC passed 78/78 after three revisions; world creation completed 2026-06-05 11:20 AM PDT as `Healthcare_247_Merrow` (`world_d50c832ac6474a68ba982a77e28a6bbe`, snapshot `snap_0fb032e95b324710b12a7432cf7da6c1`, 26 files synced). Pod assignment is `#vaguspod` with EPM Rose and pod leads Abi O / Larry E. Task 1 has advanced through AO rework, hardening, Abi pre-check, revised platform entry, pilot runs, and FA/GA. Alexander reports the current platform stage is Preference Labeling for Task 1. Source-of-truth sequence from the 06/02 instruction document: Step 14 FA/GA, Step 15 Preference Labeling, Step 16 AutoQC on FA + PL, Step 17 final reviewer review. No local Preference Labeling content is tracked yet unless Alexander adds or authorizes it.

Ratification: `worlds/korvin-merrow/final-submission-resolution/ratifications/final-submission-resolution-ratification.md`. Locked artifacts under `worlds/korvin-merrow/final-submission-resolution/locked/`.

Artifact staging note: generated submission-facing artifacts are under `korvin-merrow-final-submission-staging/`. The active canonical staging set is `01_spec-document/Alexander_World_Merrow_latest_6_4.docx`, `02_template-reference-files/final/` with 33 date-stamped DOCX files, and the sanitized Claude transcript DOCX/PDF. The local Drive mirror `korvin-merrow-drive-package/` is gitignored reviewer-convenience sync material, not repository canon. No manifest, zip, scoring artifact, AutoQC response, or final submission package has been created.

Drive sync note: Step 9 is finalized, so the Drive mirror is eligible for refresh to the accepted/finalized 26-file world-level set if Alexander explicitly authorizes Drive mutation. Until that authorization, the local repository remains canonical. When synced, label the Drive package as `Step 9 final / world created - Healthcare_247_Merrow` and keep task setup materials separate for Step 10. For the three 06/05 revised world files, prefer Drive "Upload new version" on the existing Drive files over duplicate uploads.

## Current World

Working title: Korvin Merrow World

## Current State

Brainstorm Human Review returned GO from Stacey S after SEND BACK remediation. Reviewer approved the Korvin Merrow Brainstorm and indicated next steps are World Spec and file template development. Preparation Layer, World Spec v1, File Inventory Architecture v1, File Inventory v1, Synthetic World-Level File Construction Plan v1, FI-W01 through FI-W22, Task-Level Context File Architecture v1, FI-T01 through FI-T07, Supplementary File Architecture v1, FI-S01 through FI-S04, Task Prompt Architecture v1, Task Prompt Construction, and Expected Output Architecture v1 are locked and complete. Entire File Ecosystem is complete: FI-W01 through FI-W22, FI-T01 through FI-T07, and FI-S01 through FI-S04. Task Prompt Architecture v1 is locked at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md`, with validation review at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md` and ratification at `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`.

Task Prompt Construction is LOCKED. Six task prompts (TP-KM01 through TP-KM06) are locked under `worlds/korvin-merrow/task-prompts/locked/` with `task-prompt-construction-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md`. Expected Output Architecture v1 is LOCKED under `worlds/korvin-merrow/expected-output-architecture/locked/`. Ratification is recorded at `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md`. Expected Output Construction is LOCKED under `worlds/korvin-merrow/expected-outputs/locked/`, with EO-KM01 through EO-KM06 and `expected-output-construction-validation-review.md` locked. Ratification is recorded at `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`. FI-T07 remains addendum support for EO-KM01 only; no EO-KM07 was created. Golden Architecture v1 is LOCKED under `worlds/korvin-merrow/golden-architecture/locked/`, with `golden-architecture-v1.md`, `golden-architecture-validation-review.md`, and `golden-architecture-audit-reconciliation.md` preserved unchanged. Ratification is recorded at `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md`. Golden Architecture status is COMPLETE. Golden Construction is LOCKED under `worlds/korvin-merrow/goldens/locked/`: Golden-KM01 through Golden-KM06 plus `golden-construction-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md`. Goldens status is COMPLETE. Grader Guidance Architecture v1 is LOCKED under `worlds/korvin-merrow/grader-guidance-architecture/locked/`, with `grader-guidance-architecture-v1.md` and `grader-guidance-architecture-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`. Grader Guidance Architecture status is COMPLETE. Grader Guidance Construction is LOCKED under `worlds/korvin-merrow/grader-guidance/locked/`: GG-KM01 through GG-KM06 plus `grader-guidance-construction-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`. Grader Guidance status is COMPLETE. AutoQC Architecture v1 is LOCKED under `worlds/korvin-merrow/autoqc-architecture/locked/`: `autoqc-architecture-v1.md` and `autoqc-architecture-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`. AutoQC Architecture status is COMPLETE. AutoQC Construction is LOCKED under `worlds/korvin-merrow/autoqc/locked/`: `autoqc-construction-v1.md` and `autoqc-construction-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`. AutoQC status is COMPLETE. Packaging Architecture v1 is LOCKED under `worlds/korvin-merrow/packaging-architecture/locked/`: `packaging-architecture-v1.md` and `packaging-architecture-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`. Packaging Architecture status is COMPLETE. Packaging Construction is LOCKED under `worlds/korvin-merrow/packaging/locked/`: `packaging-construction-v1.md` and `packaging-construction-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/packaging/ratifications/packaging-construction-ratification.md`. Packaging status is COMPLETE. Submission Preparation is LOCKED under `worlds/korvin-merrow/submission-preparation/locked/`: `submission-preparation-v1.md` and `submission-preparation-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/submission-preparation/ratifications/submission-preparation-ratification.md`. Execution Preparation v1 is LOCKED under `worlds/korvin-merrow/execution-preparation/locked/`: `execution-preparation-v1.md` and `execution-preparation-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/execution-preparation/ratifications/execution-preparation-ratification.md`. Execution Preparation status is COMPLETE. Later execution artifact generation, RL Studio upload, and Spec AutoQC were performed under Alexander's direct authorization and operation; no platform responses, AutoQC responses, scoring rubrics, scoring thresholds, point allocations, pass/fail bands, manifests, final submission packages, final signed medication list, final discharge order, or invented post-discharge outcome were created in the repository.

Source/reference note: Alexander added World Spec example source documents under `reference/word-spec-examples/`. This folder is intentionally local-only and gitignored because the example corpus is large and can confuse project-specific source-of-truth boundaries. Preserve it as source/reference material, not authored Korvin Merrow content.

Claude transcript resolution note: `docs/claude-transcript-formatted.md` is the authoritative transcript upload artifact. The Claude share URL `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040` is preserved as supporting provenance and reviewer-access support. `docs/claude-transcript.md` remains raw historical/provenance evidence only. No further transcript architecture, transcript review, transcript mechanism review, transcript scope review, or transcript URL review is required unless future RL Studio instructions explicitly contradict this decision.

Claude Identity Package hostile-review observations are recorded as carry-forward implementation notes in `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`. Identity Package v1 remains locked.

Task-design physician-perspective guidance from Medicine Team Lead has been recorded as a future task-layer rule only. It does not alter source-of-truth hierarchy, Governance Package v1, locked clinical architecture, or locked synthetic files. Future task prompts, expected outputs, goldens, and grader guidance must frame final deliverables from the physician perspective or physician voice.

Task-Level Context File Architecture v1 reconciliation review is complete. FI-T inventory / task-layer architecture reconciliation is recorded at `worlds/korvin-merrow/file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md`. The locked File Inventory metadata now reflects FI-T02, FI-T04, FI-T05, and FI-T06 secondary trap/friction support where already supported by locked Task Architecture Package v1. Task-Level Context File Architecture v1 clarifies that P0/P1/P2 labels are tracker-provenance metadata only, not governing workflow architecture. Architecture ratification and lock are complete after Reviewer A recertification LOCK READY / GO and Reviewer B LOCK READY / GO. Historical architecture-lock boundary: no FI-T files, FI-S files, supplementary files, prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, submission artifacts, or synthetic files were created during architecture ratification. This boundary is superseded by the later authorized Task-Level Context File Construction lock recorded above.

Collaborator session-exit discipline is now a standing process / handoff rule: every Codex, Claude, or writer session must leave the repository clean or explicitly documented, keep current and next phase surfaces updated, preserve locked artifacts unless explicitly authorized, label candidate artifacts clearly, move newly locked artifacts into locked paths with ratification references, update continuity and Claude handoff surfaces, remove or clearly mark stale active candidate paths, record carry-forward watch items and future task-layer guidance, and create a checkpoint commit for completed work unless Alexander explicitly instructs not to commit. Final reports must state what changed, what did not change, current status, next eligible phase, and whether the repository is safe for another collaborator to continue.

Cross-artifact consistency verification is now a standing governance rule: before any architecture, inventory, matrix, mapping, coverage table, workflow table, trap table, friction table, hierarchy table, or governance artifact is created, modified, ratified, or locked, collaborators must explicitly cross-check applicable locked canonical sources and document any expansion, narrowing, redistribution, reprioritization, relabeling, or reclassification before ratification or lock. Historical, planning, superseded, tracker, or provenance metadata must not be silently promoted into governing architecture.

Reasoning discipline is now a standing workspace backbone rule recorded at `docs/reasoning-discipline.md`: before any expensive/irreversible commitment or any causal claim about why a system behaved a certain way, read the ground truth artifact first (config, transcript, output, or file) and state what is verified versus inferred. Stay fast for reversible two-way-door work. This is cross-world operating doctrine, not Korvin clinical canon.

## RL Studio Submission

Task ID: cyau8803

Status: Brainstorm approved / World Spec v1 locked / File Inventory v1 locked / World-level synthetic file layer complete / Task-level context files locked and complete / Supplementary files locked and complete / Entire file ecosystem complete

Original submission timestamp: 5/29/2026 2:49 PM PDT

Latest remediation submission: revised Korvin Merrow Brainstorm uploaded; AutoQC 0 failed, 51 passed; diagnostics reviewed; plan resubmitted for reviewer review.

Reviewer GO: Stacey S approved Brainstorm via Slack. Recorded in `worlds/korvin-merrow/reviews/reviewer-go-01.md`.

## Current Pass

Task 1 Preference Labeling: ACTIVE. Step 9 generated-file review is closed and preserved under `worlds/korvin-merrow/file-review/`. Task 1 platform artifacts, trajectory records, FA/GA records, Abi review records, hardening drafts, and lifecycle record are preserved under `worlds/korvin-merrow/task-setup/`. Current action is PL work in RL Studio/Taiga: compare the two selected attempts against the golden, choose the A4-B4 preference scale, and write the seven-section justification. Do not create PL text locally unless Alexander explicitly asks.

## Next Pass

Current phase: Task 1 Preference Labeling. Source docs checked: 05/24 guide and 06/02 instruction document both place PL after FA/GA and before AutoQC on FA + PL / final review. `docs/reasoning-discipline.md` is the verification gate for future expensive decisions and platform-behavior claims. Further RL Studio actions beyond the currently authorized PL work, FA+PL AutoQC, final reviewer review, additional task uploads, additional agent runs, additional QA runs, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, manifest creation, final submission packaging, additional uploads, and additional submission actions remain blocked unless explicitly authorized by Alexander for the exact step.

Task 1 canonical lifecycle log: `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`. It wins over scattered summaries for Task 1 status. Task 1 platform provenance lives under `worlds/korvin-merrow/task-setup/platform/task1/`, including superseded task files, golden-response v1/v2/v3, grader-guideline v1-v5, and prompt/task memo variants. The repeatable per-task runbook is `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`; it now uses the post-Abi realism gate and `grader-guidelines-task1-v5.txt` mechanism-agnostic structure as the current Task 1 rework model. Task 1 trajectory exports are preserved under `worlds/korvin-merrow/task-setup/task1/trajectories/v1/`, `worlds/korvin-merrow/task-setup/task1/trajectories/v2/`, and `worlds/korvin-merrow/task-setup/task1/trajectories/low-runs/`; batch v2 findings are historical after the task-file deletion, while batch v3 findings are current for the submitted round-2 FA/GA. The independent FA/GA prompt brief is `worlds/korvin-merrow/task-setup/task1/FA-GA-independent-review-brief.md`; `worlds/korvin-merrow/task-setup/task1/FA-GA-final.md` preserves historical batch v2 wording and current round-2 submitted FA/GA. The older Step 10 preparation packet remains at `worlds/korvin-merrow/task-setup/step10-review-packet.md` for Tasks 2-6 planning and de-hinting.

## Active Blocker

Active blocker: no repository blocker. Current platform work is Task 1 Preference Labeling. Await Alexander-provided PL details or explicit authorization before writing, editing, uploading, or submitting PL content, running FA+PL AutoQC, or moving to final reviewer review.

## Current Git Checkpoint

checkpoint: track task hardening drafts and task 2 seed

Previous checkpoint: beaa174 checkpoint: clean workspace before artifact generation

## Active Branch

Current after cleanup: korvin-merrow-brainstorm

Previous branch: james-carter-brainstorm

Branch rename status: local branch renamed and pushed to `origin/korvin-merrow-brainstorm`; tag `korvin-spec-submitted` created for the final cleanup checkpoint. Remote retirement of `origin/james-carter-brainstorm` is deferred because GitHub rejected deletion while that branch is the remote current/default branch. Next repository-admin step: switch the remote default/current branch away from `james-carter-brainstorm`, then delete the old remote branch.

## Rollback Strategy

Return to baseline commit if workflow becomes corrupted.

## Next Command For Codex

Support Alexander's active Preference Labeling state. Source-of-truth docs say PL compares two selected attempts A vs B against the golden, selects the A4-B4 preference scale, and writes a seven-section justification. Do not invent A/B facts or draft PL content without the actual platform-selected responses and explicit Alexander authorization. Use `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md` as the canonical Task 1 history source.

At the end of any working session, apply the collaborator session-exit discipline before final reporting and commit completed process or construction work unless Alexander explicitly instructs not to commit.

## Scope Guardrails

Preference Labeling is now the active authorized stage for Task 1 by Alexander's report. Do not create PL text without the actual selected A/B responses. Do not proceed to FA+PL AutoQC, final reviewer review, additional task uploads, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, manifest creation, final submission packaging, additional uploads, or additional submission actions unless Alexander explicitly authorizes the exact phase/action.
## Execution Artifact Generation Outputs
Status: COMPLETE / CANONICALIZED.
Generated staging root: korvin-merrow-final-submission-staging/.
Generated artifacts:
- korvin-merrow-final-submission-staging/01_spec-document/Alexander_World_Merrow_latest_6_4.docx (canonical submitted spec)
- korvin-merrow-final-submission-staging/02_template-reference-files/final/ with 33 date-stamped DOCX files (canonical reference/task-file upload set)
- korvin-merrow-final-submission-staging/03_claude-transcript/Korvin_Merrow_Claude_Transcript.docx
- korvin-merrow-final-submission-staging/03_claude-transcript/Korvin_Merrow_Claude_Transcript.pdf
- korvin-merrow-final-submission-staging/04_optional-qc-inputs/Korvin_Merrow_Brainstorm.docx
Hold folder: korvin-merrow-final-submission-staging/05_hold-not-upload/ exists and is empty. TP/EO/Golden/GG artifacts were not exported. The previous `world-level/`, `supplementary/`, and `pretty/` staging variants are superseded by `final/`.
Verification: 33 final DOCX files are present and match the ignored Drive mirror by filename/hash. Final World Spec DOCX was regenerated from the official template and verified with required Word package parts plus rendered PDF. Transcript export retains Claude share URL provenance and omits internal repository path metadata from the generated upload artifact. The transcript PDF is aligned to the Drive mirror; byte differences between regenerated PDFs are timestamp/render artifacts, not content differences.
