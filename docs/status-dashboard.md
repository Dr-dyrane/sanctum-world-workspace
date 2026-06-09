# Status Dashboard

## Current Gate

**WORLD CREATED (6/5/2026, 11:20 AM PDT): Healthcare_247_Merrow is live. Step 9 COMPLETE. Current stage: Task 1 FINAL REVIEW COMPLETE / APPROVED.**

- Final Files AutoQC: PASS 78/78 (after 3 revisions; full chain in `worlds/korvin-merrow/file-review/file-review-log.md`).
- World ID: `world_d50c832ac6474a68ba982a77e28a6bbe`; synced snapshot `snap_0fb032e95b324710b12a7432cf7da6c1`, 26 files, sync complete.
- World name convention used: `Healthcare_Number_PatientName` per the 5.0 platform card (supersedes instruction doc ordering); 247 = next after Healthcare_246_Gutey.
- Resources: External Fetcher Agent + Prometheus Stream Agent; model anthropic/claude-opus-4-6; judge anthropic/claude-sonnet-4-5. No rubric items or checkpoints yet.
- Onboarding history: Spec AutoQC 108/109 (prednisone by design), Stacey approval 6/4, pipeline run #1, 179-finding triage, 11 content edits + 2 de-bold passes, 7 task files held back, two platform bugs diagnosed (two Apply-to-Task buttons; org AutoQC quota outage) and escalated with engineering.
- Pod: `#vaguspod`; EPM Rose; pod leads Abi O and Larry E. Pod welcome thread is the home base for world/task communications.
- Task 1 source of truth: `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`.
- Task runbook: `worlds/korvin-merrow/task-setup/TASK-RUNBOOK.md`.
- Reasoning discipline: `docs/reasoning-discipline.md` is the workspace verification gate for one-way-door decisions and causal platform-behavior claims.
- Doc spine: `project/WORKSPACE_FILE_MAP.md` Navigation Rule is the repository read spine. Task-stage work must begin from that ladder plus the active `TASKN-STATE.md`, not from memory or nearby drafts.
- Task 1 state: AO rework, hardening, Abi pre-check, revised platform entry, pilot runs, FA/GA, Preference Labeling, and final human review are complete. Abi Osagie completed the final review checklist on 2026-06-06 with applicable items marked Yes or N/A.
- Task 1 scores: 78, 72, 92, 95, 93, 92, 92, 92, 90, 94 (mean 89%, zero below 70). Current read after grading transcripts and saved-output comparison: well-built and clinically discriminating but not deeply stumping; the 0.72 and 0.78 runs omitted metformin ER from the medication disposition, the 0.78 run also under-dispositioned gabapentin, and a 90s-cluster comparator covered metformin.
- Grader read: Good/Great candidate. Abi later corrected the mechanism: the grader should be described as scoring the model output against the golden and grader guidelines, not as independently going into the chart. Preserve the mechanism-agnostic wording in future FA/GA and grader analysis.
- Local trajectory exports: Task 1 trajectory outputs captured under `worlds/korvin-merrow/task-setup/task1/trajectories/v1/` and `worlds/korvin-merrow/task-setup/task1/trajectories/v2/`.
- FA/GA status: round-2 FA/GA submitted on batch v3, run 8 / `db617c58`; GA rated Great. Final local copy is `worlds/korvin-merrow/task-setup/task1/FA-GA-final.md`, preserving historical batch v2 text and current round-2 submitted text.
- FA/GA AutoQC status: batch v2 FA/GA AutoQC history is preserved; Abi first human review returned SEND BACK / rework required; governing review record is `worlds/korvin-merrow/task-setup/reviews/task1-first-human-review-ao-2026-06-05.md`.
- Final review record: `worlds/korvin-merrow/task-setup/reviews/task1-final-review-ao-2026-06-06.md`. Reviewer note: golden demographics header placement was unrealistic; writer edited and reviewer uploaded the new golden, with no QC rerun needed because no other changes were required.
- Step 10/11 source guidance: instruction doc 06_02 sections "How to Set up Your Task in RLS", Golden Response, Grader Guidelines, plus lived Task 1 lessons in `docs/world-pipeline-playbook.md` sections A2-A5.

## Brainstorm

- RL Studio submission: completed
- Task ID: `cyau8803`
- Status: Brainstorm approved / ready for World Spec transition
- Submission timestamp: `5/29/2026 2:49 PM PDT`
- AutoQC: revised Brainstorm rerun completed, `0 failed / 51 passed`
- Diagnostics: reviewed
- Human review: GO from Stacey S after SEND BACK remediation
- Approval source: Slack / Stacey S
- Reviewer note: "great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."
- Current remediation: identity/world-type fixes, approved comorbidity expansion, and approved medication specificity applied and resubmitted
- Revised DOCX: `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`
- Reupload: completed

## World Spec

- World Spec kickoff: recorded in `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`
- Physician decision log: recorded in `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`
- World Spec construction: complete
- World Spec Skeleton v1: locked
- World Spec Skeleton Phase: complete
- World Spec v1: locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`
- World Spec v1 ratification: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`
- File Inventory Architecture v1: locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`
- File Inventory Architecture ratification: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`
- Phase 3 File Inventory Architecture: complete
- File Inventory v1: locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`
- File Inventory v1 ratification: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-v1-ratification.md`
- FI-T inventory / task-layer architecture reconciliation: `worlds/korvin-merrow/file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md`
- File Inventory Planning: complete
- Synthetic World-Level File Construction Plan v1: locked at `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`
- Synthetic World-Level File Construction Plan ratification: `worlds/korvin-merrow/synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`
- Synthetic File Construction Governance: complete
- Batch 1 synthetic files FI-W01 through FI-W07: locked at `worlds/korvin-merrow/synthetic-files/locked/batch-1/`
- Batch 1 ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md`
- Batch 1 validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md`
- Batch 1 Construction: complete
- Batch 2 synthetic files FI-W08 through FI-W13: locked at `worlds/korvin-merrow/synthetic-files/locked/batch-2/`
- Batch 2 ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md`
- Batch 2 validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md`
- Batch 2 Construction: complete
- Batch 3 synthetic files FI-W14 through FI-W16: locked at `worlds/korvin-merrow/synthetic-files/locked/batch-3/`
- Batch 3 validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-3/batch-3-validation-review.md`
- Batch 3 ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-3-ratification.md`
- Batch 3 Construction: complete
- Batch 4 synthetic files FI-W17 through FI-W21: locked at `worlds/korvin-merrow/synthetic-files/locked/batch-4/`
- Batch 4 validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-4/batch-4-validation-review.md`
- Batch 4 ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md`
- FI-W20 inventory row reconciliation: `worlds/korvin-merrow/file-inventory/reviews/fi-w20-inventory-row-reconciliation.md`
- FI-S03 Trap #5 reconciliation: `worlds/korvin-merrow/file-inventory/reviews/supplementary-file-trap5-reconciliation.md`
- Batch 4 Construction: complete
- Batch 5 synthetic file FI-W22: locked at `worlds/korvin-merrow/synthetic-files/locked/batch-5/FI-W22_discharge-facing-plan-snapshot-before-world-close.md`
- Batch 5 validation review: `worlds/korvin-merrow/synthetic-files/locked/batch-5/batch-5-validation-review.md`
- Batch 5 ratification: `worlds/korvin-merrow/synthetic-files/ratifications/batch-5-ratification.md`
- Batch 5 Construction: complete
- World-Level Synthetic File Layer: complete
- Completed World-Level Files: FI-W01 through FI-W22
- World-Level Layer Closure Audit: `worlds/korvin-merrow/reviews/world-level-layer-closure-audit.md`
- Task-Level Context File Architecture v1: locked at `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md`
- Task-Level Context File Architecture v1 ratification: `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`
- Task-Level Context File Architecture v1 reconciliation: complete. File Inventory metadata now reflects supported FI-T secondary trap/friction mappings, and locked architecture marks P0/P1/P2 labels as tracker-provenance metadata rather than governing workflow architecture.
- Task-Level Context File Architecture: complete
- Task-Level Context File Construction: locked at `worlds/korvin-merrow/task-context-files/locked/`
- FI-T01 through FI-T07: locked as task-context files
- Task-context validation review: `worlds/korvin-merrow/task-context-files/locked/task-context-files-validation-review.md`
- Task-Level Context File Construction ratification: `worlds/korvin-merrow/task-context-files/ratifications/task-level-context-file-construction-ratification.md`
- Task-Level Context Files: complete
- Supplementary File Architecture v1: locked at `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-v1.md`
- Supplementary File Architecture validation review: `worlds/korvin-merrow/supplementary-file-architecture/locked/supplementary-file-architecture-validation-review.md`
- Supplementary File Architecture ratification: `worlds/korvin-merrow/supplementary-file-architecture/ratifications/supplementary-file-architecture-v1-ratification.md`
- Supplementary File Architecture: complete
- Supplementary File Architecture reconciliation finding: CLOSED
- Supplementary files FI-S01 through FI-S04: locked under `worlds/korvin-merrow/supplementary-files/locked/`
- Supplementary file construction validation review: `worlds/korvin-merrow/supplementary-files/locked/supplementary-file-construction-validation-review.md`
- Supplementary File Construction ratification: `worlds/korvin-merrow/supplementary-files/ratifications/supplementary-file-construction-ratification.md`
- Supplementary File Construction: locked
- Supplementary Files: complete
- Entire File Ecosystem: complete
- Completed File Ecosystem: FI-W01 through FI-W22; FI-T01 through FI-T07; FI-S01 through FI-S04
- Task Prompt Architecture v1: locked at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md`
- Task Prompt Architecture validation review: `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md`
- Task Prompt Architecture ratification: `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`
- Task Prompt Architecture: complete
- Task Prompt Construction: locked
- Task prompt locked files: `worlds/korvin-merrow/task-prompts/locked/`
- Files locked: TP-KM01 through TP-KM06
- Task prompt construction validation review: `worlds/korvin-merrow/task-prompts/locked/task-prompt-construction-validation-review.md`
- Task Prompt Construction ratification: `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md`
- Task Prompts: complete
- Expected Output Architecture v1: locked
- Expected Output Architecture locked artifacts: `worlds/korvin-merrow/expected-output-architecture/locked/`
- Locked files: `expected-output-architecture-v1.md`; `expected-output-architecture-validation-review.md`
- Ratification: `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md`
- Expected Output Architecture: complete
- Expected Output Construction: locked
- Expected Output locked files: `worlds/korvin-merrow/expected-outputs/locked/`
- Files locked: EO-KM01 through EO-KM06 plus `expected-output-construction-validation-review.md`
- Expected Output Construction ratification: `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`
- Expected Outputs: complete
- FI-T07 relationship: preserved as addendum support for EO-KM01 only; no EO-KM07 exists
- Golden Architecture v1: locked
- Golden Architecture locked artifacts: `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-v1.md`; `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-validation-review.md`; `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-audit-reconciliation.md`
- Golden Architecture ratification: `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md`
- Golden Architecture: complete
- Golden Construction: locked
- Golden Construction locked artifacts: `worlds/korvin-merrow/goldens/locked/`
- Files locked: Golden-KM01 through Golden-KM06 plus `golden-construction-validation-review.md`
- Golden Construction ratification: `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md`
- Goldens: complete
- FI-T07 relationship: preserved as addendum support for Golden-KM01 only; no Golden-KM07 exists
- Grader Guidance Architecture v1: locked
- Grader Guidance Architecture locked artifacts: `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-v1.md`; `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md`
- Grader Guidance Architecture ratification: `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`
- Grader Guidance Architecture: complete
- Grader Guidance Construction: locked
- Grader Guidance locked artifacts: `worlds/korvin-merrow/grader-guidance/locked/`
- Files locked: GG-KM01 through GG-KM06 plus `grader-guidance-construction-validation-review.md`
- Grader Guidance Construction ratification: `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`
- Grader Guidance: complete
- AutoQC Architecture v1: locked
- AutoQC Architecture locked artifacts: `worlds/korvin-merrow/autoqc-architecture/locked/`
- AutoQC Architecture ratification: `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`
- Files locked: `autoqc-architecture-v1.md`; `autoqc-architecture-validation-review.md`
- AutoQC Construction: locked
- AutoQC Construction locked artifacts: `worlds/korvin-merrow/autoqc/locked/`
- AutoQC Construction ratification: `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`
- Files locked: `autoqc-construction-v1.md`; `autoqc-construction-validation-review.md`
- AutoQC: complete
- Packaging Architecture v1: locked
- Packaging Architecture locked artifacts: `worlds/korvin-merrow/packaging-architecture/locked/`
- Files locked: `packaging-architecture-v1.md`; `packaging-architecture-validation-review.md`
- Packaging Architecture ratification: `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`
- Packaging Architecture: complete
- Packaging Construction: locked
- Packaging Construction locked artifacts: `worlds/korvin-merrow/packaging/locked/`
- Files locked: `packaging-construction-v1.md`; `packaging-construction-validation-review.md`
- Packaging Construction ratification: `worlds/korvin-merrow/packaging/ratifications/packaging-construction-ratification.md`
- Packaging: complete
- Submission Preparation: locked
- Submission Preparation locked artifacts: `worlds/korvin-merrow/submission-preparation/locked/`
- Files constructed: `submission-preparation-v1.md`; `submission-preparation-validation-review.md`
- Ratification: `worlds/korvin-merrow/submission-preparation/ratifications/submission-preparation-ratification.md`
- Execution Preparation: locked
- Execution Preparation locked artifacts: `worlds/korvin-merrow/execution-preparation/locked/`
- Files constructed: `execution-preparation-v1.md`; `execution-preparation-validation-review.md`
- Execution status: preparation locked; later submission-facing artifact generation, RL Studio upload, and Spec AutoQC occurred under Alexander's direct authorization and operation
- Final Submission Resolution: LOCKED
- Final Submission Resolution locked artifacts: `worlds/korvin-merrow/final-submission-resolution/locked/final-submission-resolution-v1.md` and `worlds/korvin-merrow/final-submission-resolution/locked/final-submission-resolution-validation-review.md`; ratification at `worlds/korvin-merrow/final-submission-resolution/ratifications/final-submission-resolution-ratification.md`
- Execution Artifact Generation: COMPLETE / CANONICALIZED; generated one canonical spec DOCX, one canonical 33-file reference/task upload set, and sanitized transcript DOCX/PDF. No AutoQC response, scoring artifact, manifest, final package, or zip was created in the repository.
- Spec AutoQC: COMPLETE at 108/109; sole remaining prednisone warning is intentional and note-justified
- Human World Spec Review: APPROVED by Stacey S; approval record `worlds/korvin-merrow/reviews/reviewer-spec-approval-01.md`
- Reviewer routing correction: Reference File Origin labels corrected to the template-canonical `Custom Made` token and re-uploaded
- No GG-KM07 exists
- Current phase: Task 1 final human review COMPLETE / APPROVED
- Active Task 1 lifecycle log: `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`
- Task 1 platform provenance: `worlds/korvin-merrow/task-setup/platform/task1/`; active/live folder contains only `prompt-task1-v5.txt`, `golden-response-task1-v6.docx`, `grader-guidelines-task1-v10.txt`, `medication_safety_handoff_pharmacy_05232026.docx`, and README. Superseded prompt/golden/grader/task-file iterations live under `platform/task1/archive/` as historical evidence only.
- Tasks 2-6 prep packet: `worlds/korvin-merrow/task-setup/step10-review-packet.md`
- Task 5 local review packet: `worlds/korvin-merrow/task-setup/task5/TASK5-STATE.md`, current reset plan `task5/design/KM05-v2-design-plan-6-8.md`, older historical reviews `task5/design/KM05-claude-ai-proposal-6-7.md` and `task5/design/KM05-codex-black-team-6-7.md`, `task5/KM05-prebuild-review-and-build-gates.md`, and `task5/build-phase-drafts/`. Review-only reset / HOLD, not a build or platform set.
- Active file-review protocol: `worlds/korvin-merrow/file-review/file-review-protocol.md`
- Active Claude-assisted triage: `worlds/korvin-merrow/file-review/findings-triage.md`
- Candidate revision log: `worlds/korvin-merrow/file-review/file-review-log.md`
- Final upload set used for world creation: `worlds/korvin-merrow/file-review/upload/filesystem/` with 26 world files; task files held out under `worlds/korvin-merrow/file-review/task-files-holdback/`
- Claude transcript: `docs/claude-transcript-formatted.md` is the authoritative transcript upload artifact. `docs/claude-transcript.md` remains raw historical/provenance evidence. Supporting Claude share URL: `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040`.
- Task-design physician-perspective guidance: recorded as a future task-layer rule only. It does not change source-of-truth hierarchy or Governance Package v1; future task prompts and deliverables must remain physician-centered even when supporting sources are pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources.
- Collaborator session-exit discipline: standing process / handoff rule. Every future session must leave the repository clean or explicitly documented, update phase and next-phase surfaces, preserve locked artifacts unless explicitly authorized, label candidate artifacts, move newly locked artifacts to locked paths with ratification references, update continuity and Claude handoff files, record carry-forward watch items and future task-layer guidance, commit completed work unless explicitly told not to, and report what changed, what did not change, current status, next eligible phase, and whether the repository is safe for another collaborator.
- Cross-artifact consistency verification: standing governance rule. Before creating, modifying, ratifying, or locking architecture, inventory, matrices, mappings, workflow/trap/friction/hierarchy tables, or governance artifacts, future collaborators must cross-check applicable locked canonical sources and document any expansion, narrowing, redistribution, reprioritization, relabeling, or reclassification before ratification or lock.
- Clinical Story Skeleton: v1 locked, reviewed, and ratified
- Identity Package: v1 locked
- Governance Package: v1 ratified
- Physician Architecture Layer: complete
- Key Milestones Calendar Skeleton: v1 locked
- Baseline Anchor Package: v1 locked
- Clinical Story Timeline Package: v1 locked
- Task Architecture Interview: v1 historical planning scaffold
- Task Architecture Package: v1 locked
- Medication Expansion Package: v1 locked
- Comorbidity Expansion Package: v1 locked
- Provider Roster Package: v1 locked
- Surgical History Package: v1 locked
- Daily Hospital Course Framework: v1 locked
- Preparation Layer: complete
- World Spec Skeleton v1: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`
- World Spec Skeleton ratification: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md`
- Official Claude World Spec session: pending
- Current state: World Spec v1 is locked; File Inventory Architecture v1 is locked; File Inventory v1 is locked with FI-W20 row reconciliation, FI-T inventory/task-layer architecture reconciliation, and FI-S03 Trap #5 reconciliation recorded; Synthetic World-Level File Construction Plan v1 is locked; Synthetic File Construction Governance is complete; Batch 1 synthetic world-level files are locked; Batch 2 synthetic world-level files are locked; Batch 3 synthetic world-level files are locked; Batch 4 synthetic world-level files are locked; Batch 5 FI-W22 is locked; World-Level Synthetic File Layer is complete; Task-Level Context File Architecture v1 is locked and Task-Level Context File Architecture is complete; FI-T01 through FI-T07 are locked and Task-Level Context Files are complete; Supplementary File Architecture v1 is locked and Supplementary File Architecture is complete; FI-S01 through FI-S04 are locked and Supplementary Files are complete; Entire File Ecosystem is complete; Task Prompt Architecture v1 is locked and complete; Task Prompt Construction is locked; Task Prompts are complete; Expected Output Architecture v1 is locked and Expected Output Architecture is complete; Expected Output Construction is locked and Expected Outputs are complete; Golden Architecture v1 is locked and Golden Architecture is complete; Golden Construction is locked and Goldens are complete under `worlds/korvin-merrow/goldens/locked/`; Grader Guidance Architecture v1 is locked under `worlds/korvin-merrow/grader-guidance-architecture/locked/`; Grader Guidance Construction is locked under `worlds/korvin-merrow/grader-guidance/locked/`; Grader Guidance is complete; AutoQC Architecture v1 is locked under `worlds/korvin-merrow/autoqc-architecture/locked/`; AutoQC Architecture is complete; AutoQC Construction is locked under `worlds/korvin-merrow/autoqc/locked/`; AutoQC is complete; Packaging Architecture v1 is locked under `worlds/korvin-merrow/packaging-architecture/locked/`; Packaging Architecture is complete; Packaging Construction is locked under `worlds/korvin-merrow/packaging/locked/`; Packaging is complete; Submission Preparation is locked under `worlds/korvin-merrow/submission-preparation/locked/`; Submission Preparation is complete; Execution Preparation v1 is locked under `worlds/korvin-merrow/execution-preparation/locked/`; Transcript Resolution v1 is locked under `worlds/korvin-merrow/transcript-resolution/locked/`; Final Submission Resolution v1 is locked under `worlds/korvin-merrow/final-submission-resolution/locked/` with ratification under `worlds/korvin-merrow/final-submission-resolution/ratifications/`; calendar, baseline anchors, Clinical Story Timeline Package v1, Task Architecture Package v1, Medication Expansion Package v1, Comorbidity Expansion Package v1, Provider Roster Package v1, Surgical History Package v1, Daily Hospital Course Framework v1, and World Spec Skeleton v1 are locked
- World Spec prep packet: created
- Official World Spec template: saved locally
- World Spec AutoQC prompt v6.3: saved locally
- World Spec AutoQC v6.3 checks: indexed in `reference/world-spec-guidelines/08_autoqc_master_index.md`
- World Spec writer playbook: created in `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`
- Clinical Story Skeleton review: `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`
- Clinical Story Skeleton ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`
- Identity Package v1: `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`
- Identity Package review addendum: `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`
- Governance Package v1: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`
- Governance Package clarification: `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`
- Governance Package ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`
- Key Milestones Calendar Skeleton v1: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`
- Key Milestones Calendar ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`
- Baseline Anchor Package v1: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`
- Baseline Anchor ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`
- Clinical Story Timeline Package v1: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`
- Clinical Story Timeline ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`
- Task Architecture Interview v1: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`
- Task Architecture Package v1: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`
- Task Architecture ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`
- Medication Expansion Package v1: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`
- Medication Expansion ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`
- Medication Expansion Decision Addendum: `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md`
- Comorbidity Expansion Package v1: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`
- Comorbidity Expansion ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`
- Provider Roster Package v1: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`
- Provider Roster ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`
- Surgical History Package v1: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`
- Surgical History ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`
- Daily Hospital Course Framework v1: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`
- Daily Hospital Course Framework ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`
- Fetched World Spec example source documents: `reference/word-spec-examples/` (local-only / gitignored)
- Latest physician decision log: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`
- World Spec prep folder structure: reorganized by lifecycle buckets (`candidate-review/`, `locked/`, `ratifications/`, `reviews/`, `decision-logs/`, `planning-scaffolds/`)
- Current phase: Task 1 final human review complete. Step 9 generated-file review is complete, Final Files AutoQC passed 78/78, and `Healthcare_247_Merrow` is live. Task 2 / KM02 is COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review (PL-only final round; tagged; marked RFD). KM02 v3 active platform set remains under `worlds/korvin-merrow/task-setup/platform/task2/current/`, with golden sha prefix `2dd3e0ad`, all recorded checks green, final FA/GA subject Attempt 8 at 0.30, and Preference Labels submitted with verdict B / B++. KM03 state starts at `worlds/korvin-merrow/task-setup/task3/TASK3-STATE.md` and `worlds/korvin-merrow/task-setup/task3/KM03-state-log.md`. KM03 v2.1 is archived as difficulty-failed evidence under `worlds/korvin-merrow/task-setup/platform/task3/archive/v2.1-difficulty-failed-after-58b5f3e3/`; active KM03 v2.2 platform files live under `worlds/korvin-merrow/task-setup/platform/task3/current/`, passed Task AutoQC 36/36 (`qcaud_fc`), and Taiga job `877aa204` cleared the difficulty gate (mean 69.0, four sub-70, six sub-90). KM03 post-Sang rerun job `8e97cdd7` selected Attempt 4 (0.30); Alexander entered FA/GA on platform and FA/GA AutoQC passed. KM04 v1 failed the 6/8 trajectory difficulty gate: job `55ee209f`, 10 runs 0.87-0.95, mean 0.912, zero sub-70; record at `worlds/korvin-merrow/task-setup/task4/runs/KM04-taiga-results-55ee209f.md`. KM04 v2 cleared the difficulty gate after Alexander-operated job `709be0e8`: mean 0.689, three sub-70 runs, tail 0.15. Durable records are `worlds/korvin-merrow/task-setup/task4/runs/KM04-v2-taiga-results-709be0e8.md` and `worlds/korvin-merrow/task-setup/task4/runs/KM04-v2-grading-transcripts-709be0e8.md`; grading transcripts confirm all 0.15 failures are anemia-propagation and the 0.97 catch is rewarded. KM04 post-Sang rerun job `979dccde` selected Attempt 9 (0.30); Alexander entered FA/GA on platform and FA/GA AutoQC passed. KM04 PL #1-#2 drafts exist locally; no KM04 PL has been platform-submitted, and no final review, locked-canon edit, or live-world edit exists. Further RL Studio/platform actions remain under Alexander's explicit/direct operation.
- KM05 current local state: review-only reset under `worlds/korvin-merrow/task-setup/task5/`. Start with `worlds/korvin-merrow/task-setup/task5/design/KM05-v2-design-plan-6-8.md` and paired review request `worlds/korvin-merrow/task-setup/task5/build-phase-drafts/KM05-v2-review-request-for-claude-ai.md`; older 6/7 convergence files are preserved as history and their moderate-task fallback is retired by the 6/8 no-moderate directive in `TASK-RUNBOOK.md`. Current lead hypothesis is a cold home-health-start / completed medication-review / good-adherence interval-observation claim inside a transition-clinic draft; renal-BMP is backup only. Any future KM05 path must become a genuine difficulty discriminator with a real clinical failure. No DOCX build, platform staging, upload, AutoQC, agent run, or QA has been performed.
- KM04 PL prep update: local draft `worlds/korvin-merrow/task-setup/task4/preference-labeling/KM04-PL-recommended-verdicts-DRAFT.md` exists for three separate post-FA/GA PL comparisons from job `709be0e8`. It is not platform-submitted and no PL AutoQC has been run.
- KM03 6/8 update: job `58b5f3e3` is recorded by Alexander as the KM03 v2.1 difficulty failure (10 trajectories 90-97, mean about 93.6, zero sub-70), with a transcript-lineage caveat because captured outputs show v1-era filenames/prompt/golden-v1. Record: `worlds/korvin-merrow/task-setup/task3/runs/KM03-taiga-results-58b5f3e3.md`. Next path is Alexander's held Taiga decision for v2.2, not FA/GA/PL/final review from v2.1.
- KM03 v2.2 Lenora plan history 6/8: `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-FINAL-PLAN.md` superseded the earlier cold-axis completion/status idea but is now itself superseded as primary by the KM02-bar plan. Preserve as review history only unless Alexander re-selects that mechanism.
- KM03 v2.2 reconciliation update 6/8: `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-reconciliation-6-8.md` adopts the Lenora plant as a pilot mechanism and records the 6/8 no-moderate directive. If the pilot does not produce a real clinical failure, redesign and re-pilot; do not accept or ship KM03 as moderate.
- KM03 v2.2 KM02-bar plan update 6/8: current primary mechanism source is `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02-BAR-PLAN.md`, with Claude.ai review request at `worlds/korvin-merrow/task-setup/task3/build-phase-drafts/KM03-v2.2-KM02bar-review-request-for-claude-ai.md`. It supersedes the Lenora supervision-fact plan as the primary mechanism and uses a tuned cold fabricated objective result on OSA/CPAP continuity.
- KM03 v2.2 platform / Taiga update 6/8: active platform set is `worlds/korvin-merrow/task-setup/platform/task3/current/prompt-task3-v2.2.txt`, `worlds/korvin-merrow/task-setup/platform/task3/current/discharge_planning_summary_draft_05242026.docx`, `worlds/korvin-merrow/task-setup/platform/task3/current/golden-KM03-v2.2.docx`, and `worlds/korvin-merrow/task-setup/platform/task3/current/grader-guidelines-task3-v2.2.txt`. Task AutoQC passed 36/36 (`qcaud_fc`); local read-only DOCX check found scrubbed core metadata and no Synthetic token or em/en dash. Taiga job `877aa204` cleared the difficulty gate with scores 20, 25, 32, 68, 83, 85, 90, 95, 95, 97 (mean 69.0). Durable record: `worlds/korvin-merrow/task-setup/task3/runs/KM03-v2.2-taiga-results-877aa204.md`. Verified local draft: `worlds/korvin-merrow/task-setup/task3/fa-ga/FA-GA-current.md`. No platform-entered FA/GA, PL, final review, additional upload, or AutoQC response exists.
- Pod guidance update: from KM03 onward, Preference Labeling requires three separate A/B labels on three different trajectories, with Preference Labels AutoQC after each. KM01/KM02 were submitted under the prior single-label rule.
- Grader-guidelines structure + length lessons (Sang/Trigeminus, 6/8): new canonical doc `docs/grader-guidelines-lessons.md` records the required five-block grader structure (Preamble naming the golden verbatim, Register Note, Section A must-be-present, Section B acceptable-variation with the verbatim two-failure-mode clause, Section C patterns opening verbatim with the central planted failure first and a credit-correct-restraint pattern) and the bloat fix (cap ~1 page / 1.25 max, body ratio ~A 40 / B 20 / C 40, Section C compressed to "watch for X + one-line why" with no inline file walkthroughs - guidance, not a review document). Cross-referenced from `docs/reviewer-response-protocol.md` and `reference/checklists/reviewer-failure-patterns.md`. Prompt sub-lesson: the first-person physician prompt carries no how-to meta-guidance (Sang deleted KM04's trailing instruction sentence).
- KM03/KM04 review fixes applied (Sang, 6/8): both graders restructured into the five-block format and their goldens elevated to the pipeline clinical register (named consultants/staff/agencies, concrete specifics; trap-carrier lines kept plain), GAs mapped to Sections A/B/C. KM04 grader trimmed to ~1 page (484 words, A35/B25/C40) and approved by Sang to proceed; KM04 prompt synced to Sang's edited version (trailing sentence removed). Active KM04 set under `worlds/korvin-merrow/task-setup/platform/task4/current/`, pre-restructure artifacts archived under `platform/task4/archive/2026-06-08-pre-restructure/`. Historical gate: Taiga trajectory rerun against the new grader+golden was required and later completed. Current state is the post-fix rerun plus FA/GA platform-entry lines below; PL prep remains held until FA/GA AutoQC resolves.
- KM03 post-fix rerun update (6/8): KM03 rerun against the restructured grader + elevated golden is complete. Job `8e97cdd7` scored 80, 62, 90, 30, 90, 88, 82, 87, 85, 70; mean 76.4; single lowest Attempt 4 / run `c2eea662` at 0.30; two sub-70 and three sub-90. `worlds/korvin-merrow/task-setup/task3/fa-ga/FA-GA-current.md` now supersedes the pre-fix `877aa204` Attempt 9 draft. Alexander later completed platform FA/GA entry on Attempt 4; FA/GA AutoQC passed.
- KM04 post-fix rerun update (6/8): KM04 rerun against the restructured/trimmed grader + elevated golden is complete. Job `979dccde` scored 95, 90, 30, 88, 78, 88, 90, 35, 30, 40; mean 66.4; single lowest score 0.30 shared by Attempts 3 and 9; Attempt 9 / run `976b2b18` selected for FA/GA; catch anchor Attempt 1 / run `06d0b710` scored 0.95. `worlds/korvin-merrow/task-setup/task4/fa-ga/FA-GA-current.md` now supersedes the pre-fix `709be0e8` Attempt 5 draft. Alexander later completed platform FA/GA entry on Attempt 9; FA/GA AutoQC passed. KM03 and KM04 both now have post-fix local FA/GA drafts; platform FA/GA entry is recorded in the next line.
- KM03/KM04 FA-GA platform entry (6/8): Alexander entered both FA/GA records on platform. KM03 uses Attempt 4 (0.30), FA 787 chars, GA 749 chars. KM04 uses Attempt 9 (0.30), FA 902 chars, GA 807 chars. FA/GA AutoQC passed for both. PL is now active: KM03 PL #1-#3 are drafted locally; KM03 needs their platform submission, and KM04 PL #1-#2 are drafted locally while KM04 still needs one more PL draft/submission. Run PL AutoQC after each, then final review.

## Tooling

- LibreOffice installed and verified
- Pandoc installed and verified
- Poppler installed and verified
- Python document-processing packages installed and verified
- MCP/integration audit completed

## Boundaries

- Do not revise locked World Spec v1 without Alexander approval.
- Do not revise the locked Clinical Story Skeleton unless Alexander explicitly reopens it.
- Do not reopen Identity Package v1; use the review addendum only as carry-forward implementation notes.
- Do not change Governance Package v1 without Alexander approval.
- Do not create milestones before Alexander authorizes that step.
- Do not create task-level, supplementary, or downstream task/file contents before Alexander authorizes that step.
- Do not revise locked task architecture, revise locked task prompts, or create downstream task artifacts before Alexander authorizes that step.
- Do not treat fetched World Spec examples as authored Korvin Merrow content or source-of-truth material.
- Do not modify Brainstorm unless new reviewer feedback arrives.
- Do not modify clinical content beyond reviewer-required remediation without Alexander approval.
- Task 1 final human review is complete. Task 2 / KM02 is COMPLETE / RFD (Ready for Delivery) after Janette's 6/8 final review (PL-only final round; tagged; marked RFD) after passing qcaud_5e, qcaud_4a, qcaud_ef, and Preference Labeling with verdict B / B++. KM03 and KM04 post-Sang reruns are complete, Alexander entered both FA/GA records on platform, and FA/GA AutoQC passed for both. Prior KM03 v2.1 job `58b5f3e3`, KM03 `877aa204`, and KM04 `709be0e8` remain historical difficulty evidence. Do not advance to PL, final review, rerun, or additional upload without exact Alexander authorization. KM05 is review-only reset / HOLD from `task5/design/KM05-v2-design-plan-6-8.md` and not build-ready. Do not run additional task uploads, agent runs, QA runs, platform responses, AutoQC responses, preference-label resubmission, KM03 platform FA-GA/PL/final review without exact authorization, KM03 Taiga rerun, KM04 PL/final review, KM05 build/platform staging, scoring rubrics, scoring thresholds, pass/fail bands, point allocations, manifest creation, final submission packaging, additional uploads, or additional submission actions without explicit Alexander authorization for the exact step.
- Do not access RL Studio again without explicit authorization.
- Do not end a working session without applying collaborator session-exit discipline.
## Execution Artifact Generation Outputs
- Staging root: korvin-merrow-final-submission-staging/
- World Spec DOCX: korvin-merrow-final-submission-staging/01_spec-document/Alexander_World_Merrow_latest_6_4.docx
- Reference/task DOCX upload set: korvin-merrow-final-submission-staging/02_template-reference-files/final/ (33 files)
- Claude Transcript DOCX/PDF: korvin-merrow-final-submission-staging/03_claude-transcript/
- Optional Brainstorm copy: korvin-merrow-final-submission-staging/04_optional-qc-inputs/Korvin_Merrow_Brainstorm.docx
- Hold-not-upload folder: korvin-merrow-final-submission-staging/05_hold-not-upload/
- Local Drive mirror: korvin-merrow-drive-package/ is gitignored and non-canonical


---
PRE-SANG SNAPSHOT 6/8 (superseded by post-Sang reruns and platform FA/GA entry below): KM02 COMPLETE / RFD (Ready for Delivery). Janette completed final review 6/8 (PL-only final round; RLS skim/ENV/FA-GA/PL and Taiga ENV/FA/PL checked; task tagged; marked RFD). Both prior human reviews passed (Abi 6/7), all recorded KM02 checks are green, and Preference Labels were submitted with verdict B / B++. Golden sha 2dd3e0ad. KM03 v2.1 platform set is retained as evidence after difficulty failure; job `58b5f3e3` is recorded as the difficulty-failed trajectory run. Active KM03 v2.2 platform set is present in `platform/task3/current/` and passed Task AutoQC 36/36 (`qcaud_fc`): `prompt-task3-v2.2.txt`, `discharge_planning_summary_draft_05242026.docx`, `golden-KM03-v2.2.docx`, and `grader-guidelines-task3-v2.2.txt`. Taiga job `877aa204` cleared the difficulty gate (mean 69.0, four sub-70, six sub-90); grading transcripts are verified clean; local FA/GA drafting packet exists; verified local FA/GA current draft exists at `task3/fa-ga/FA-GA-current.md`; FA/GA subject is Attempt 9 (0.20). Retired v1 passed Task AutoQC 36/36 (`qcaud_6b`) after core metadata scrub; later job `58b5f3e3` confirmed v1 was too easy and is historical only. KM04 v1 failed the 6/8 trajectory difficulty gate: job `55ee209f`, 10 runs 0.87-0.95, mean 0.912, zero sub-70. KM04 v2 cleared the difficulty gate after job `709be0e8`: mean 0.689, three sub-70 runs, tail 0.15. Current lead axis is anemia-of-CKD / absent iron-workup propagation. Local FA/GA current draft exists at `task4/fa-ga/FA-GA-current.md`, subject Attempt 5 (0.15), comparator Attempt 6 (0.97). KM05 is review-only reset from `task5/design/KM05-v2-design-plan-6-8.md` and has not been built or platform-staged.


---
6/7 late plus 6/8 archive correction: KM03 v2.1 WAS ACTIVE AFTER ALEXANDER UPLOAD, then difficulty-failed and was archived at platform/task3/archive/v2.1-difficulty-failed-after-58b5f3e3/ (prompt-task3-v2.txt, care_coordination_handoff_draft_05242026.docx, golden-KM03-v2.docx, grader-guidelines-task3-v2.txt, RUN-INSTRUCTIONS.md). v1 remains preserved at platform/task3/archive/v1-retired-after-task-writing-reset/ (uploaded, AutoQC qcaud_6b pass, later job 58b5f3e3 returned too easy, retired after task-writing reset; historical only). Mechanism history: authoring posture over a de-authorized unsigned care-coordination handoff DRAFT; fair failure = promoting the draft unverified completion into a signed physician addendum. Build authority history = KM03-v2.1-LOCKED-build-plan.md. CURRENT: active KM03 v2.2 set is platform/task3/current/ (prompt-task3-v2.2.txt, discharge_planning_summary_draft_05242026.docx, golden-KM03-v2.2.docx, grader-guidelines-task3-v2.2.txt, RUN-INSTRUCTIONS.md). Task AutoQC passed 36/36 (`qcaud_fc`); Taiga job `877aa204` cleared the initial difficulty gate; local FA/GA current draft existed at that stage; later post-Sang rerun/platform FA/GA entry is recorded below. No platform-submitted KM03 PL or final review exists.

6/8 KM05 reset: KM05 is review-only / HOLD. Start at `worlds/korvin-merrow/task-setup/task5/TASK5-STATE.md` and `task5/design/KM05-v2-design-plan-6-8.md`, then read the older 6/7 review files only as history. The current lead hypothesis is a cold home-health-start / completed medication-review / good-adherence interval-observation claim inside a transition-clinic draft; renal-BMP is backup only. The older moderate-task framing is retired by the 6/8 no-moderate directive; future KM05 must target a real clinical failure. No DOCX build, platform-current staging, RL Studio upload, Task AutoQC, Taiga trajectories, QA, or platform mutation.

---

## CURRENT STATUS SNAPSHOT (2026-06-08 PM) - all six tasks

Authoritative per-task state lives in each TASKn-STATE.md; this is the one-screen roll-up.

- KM01: Ready for Delivery (Janette S). Discharge Med Reconciliation.
- KM02: Ready for Delivery (Janette S). Discharge Summary. Mean 59.3, deep.
- KM03: Ready for Delivery (Sang N / Paolo S). Post-Sang rerun (job 8e97cdd7) mean 76.4, FA/GA re-derived on Att4 (0.30) at task3/fa-ga/FA-GA-current.md. Grader restructured to Sang five-block, golden elevated to clinical register.
- KM04: Awaiting Final Review (platform 042j9681). Care plan, anemia/iron cold plant. Rerun job 979dccde mean 66.4, FA/GA on Att9 (0.30) at task4/fa-ga/FA-GA-current.md. Grader trimmed to ~1 page per Sang.
- KM05: FA/GA SUBMITTED for first human review. Mechanism arc: NSAID (too easy, 0.95) -> multi-fab (all-floor 0.20, unfair) -> RE-CENTERED on the premature cardiorenal restart. Validated re-pilot job 90946b05: bimodal, mean 0.36, floors ~0.12-0.30, catchers 0.85; fair and bankable. Active set platform/task5/current/ (prompt/draft/golden-KM05-v4.docx/grader-v4). FA/GA at task5/fa-ga/FA-GA-current.md (subject Att10 0.12, anchor Att5 0.85). NSAID v2 set archived at platform/task5/archive/2026-06-08-nsaid-retired/. Pending: 3 Preference Labels after FA/GA review.
- KM06: v2 STAGED, ready for Alexander pilot. Arc: bone-health omission (chart-silent, dropped) -> orthostatic propagation v1 (pilot job 2eac7eca mean ~93, FAILED: orthostatic is WARM for a fall-risk review) -> v2 ECHO/LVEF cold propagation in a documentation deliverable (pre-discharge transition summary). Active set platform/task6/current/ (prompt-v2, pre_discharge_transition_summary_draft_05232026.docx, golden-KM06-v2.docx, grader-v2). Build build-docx-km06-v2.py; design design/KM06-REVISED-orthostatic-propagation-plan-6-8.md (+ KM06-build-packet-6-8.md, superseded). v1 archived at platform/task6/archive/2026-06-08-orthostatic-v1-tooeasy/.

World-level: 4 distinct workflows across 6 tasks (Discharge Med Rec, Discharge Summary, Discharge Planning Documentation x3 [KM03/05/06], Interdisciplinary Care Plan) - within the AutoQC 2.107 band of 3-5 distinct; repetition allowed. KM06 could reclassify to a Quality/Safety workflow for 5 distinct if desired.

Knowledge docs current: docs/task-difficulty-lessons.md (idea>writing, 4-point trap test, cold/warm evidence table, fairness, pilot-reading), docs/grader-guidelines-lessons.md (Sang five-block + bloat fix), docs/clinical-voice-lessons.md (golden register). Performance report at task-setup/KM-WORLD-PERFORMANCE-REPORT.md (note: its sub-70 count is 19/38% but the true count is 21/42%; KM-World-Performance.xlsx computes the correct values).

Standing build hygiene (all task DOCX): Mode A clone of KM02 bases (golden-KM02-v5.docx / discharge_summary_draft_incomplete_05242026.docx), styles.xml byte-identical, fingerprint diff empty, core metadata scrubbed, zero em/en/arrow/asterisk/brackets, only in-world dates, no off-world names. Verify-on-bytes before every stage.

---

## PLATFORM STATUS (2026-06-08 late, from Tasks board screenshot) - 6 tasks live

All six tasks now exist in Healthcare_247_Merrow. ID -> task mapping (per KM-WORLD-PERFORMANCE-REPORT):
- Task 1 (KM01): Ready for Delivery (Janette S).
- waivf867 (KM02): Ready for Delivery (Janette S).
- c8izef70 (KM03): Ready for Delivery (Paolo S).
- 042j9681 (KM04): READY FOR DELIVERY (Rahul Pai) - CHANGED from Awaiting Final Review; final reviewer signed off.
- b0tza971 (KM05): Running Taiga Trajectories & QA - the re-pilot after Abi's draft fix (BP attribution on interval + item 1).
- 2zw95f4e (KM06): Running Task AutoQC - KM06 is now a created platform task (6th task slot filled).

So: 4 tasks Ready for Delivery (KM01-04), KM05 re-running trajectories (fairness fix applied), KM06 in Task AutoQC.

OPEN ITEM (KM06 difficulty): KM06 echo/LVEF v2 FAILED its difficulty pilot (job dc3e4c8a mean ~97, all-caught), as did orthostatic v1 (job 2eac7eca ~93). Both warm. The cold quiet-closure axes (culture/CPAP/iron) are spent in KM02-04; the remaining salient axes (orthostatic, echo) are warm. Proposed but not yet built/verified: a KM05-style JUDGMENT trap (undisprovable interval bait -> chart-contradicted action) on a fresh axis - lead candidate is de-escalating the first-week supervision / fall precautions on a plausible "wife reports he is back to baseline" interval bait (chart-contradicted by Morse 65 + documented med-management errors + supervision-required-first-5-7-days). Whatever is uploaded as 2zw95f4e must still clear the difficulty gate; if the staged echo v2 was uploaded, it will pass AutoQC (format) but is not difficulty-cleared.

---

## PLATFORM STATUS (2026-06-09, from Tasks board) - all 6 tasks + AQC-EVAL

| KM | Platform ID | Status | Updated By |
|----|-------------|--------|------------|
| KM01 | Task 1 | Ready for Delivery | Janette S |
| KM02 | waivf867 | Ready for Delivery | Janette S |
| KM03 | c8izef70 | Ready for Delivery | Paolo S |
| KM04 | 042j9681 | Ready for Delivery | Rahul Pai |
| KM05 | b0tza971 | Awaiting First Human Review | Alexander U |
| KM06 | 2zw95f4e | Awaiting First Human Review | Alexander U |
| (KM06 AQC-EVAL) | [AQC-EVAL] 2zw95f4e | Task Writing | Dhruv Ahuja (Needs Attention From: Dhruv Ahuja) |

Roll-up: 4 Ready for Delivery (KM01-04); KM05 + KM06 back at Awaiting First Human Review after their re-pilots and FA/GA.

KM05 (b0tza971): Abi's first-review fairness fix applied (home BP re-attributed to patient report on the interval line AND item 1). Post-fix re-pilot job 0348a7dc: spread approx 20,95,88,40,68,70,20,35,[?],15; mean ~50; bimodal and FAIR (legitimate sub-40 floors + clean 88/95 catchers). FA/GA re-paired to job 0348a7dc (subject Att1 cfef56c9 0.20, the verified floor; literal single-lowest is 0.15 run 10 pending its transcript to lock the run ID; catch anchor Att2 2443d7e5 0.95). Floor signature confirmed across three runs (Att1/Att4/Att7 all restarted held GDMT on the patient-reported BP). Next: enter FA/GA -> FA/GA AutoQC -> 3 PL.

KM06 (2zw95f4e): v4 false-closure banked as the distinct sixth at mean 0.83 with a real floor (job 38fd1c2e). FA/GA byte-checked. Difficulty spread across the suite now KM05 36, KM02 59, KM04 66, KM03 76, KM06 83, KM01 89. Bank framing: distinct sixth at 0.83, NOT a sub-70; antibiotic-leg caveat to Abi proactively. Two QA flags disposed (identity = stale v3 file; enable_anthropic_api = tech issue).

---

## PLATFORM STATUS (2026-06-09, latest board)

| KM | Platform ID | Status | Updated By |
|----|-------------|--------|------------|
| KM01 | Task 1 | Ready for Delivery | Abimbola O |
| KM02 | waivf867 | Ready for Delivery | Abimbola O |
| KM03 | c8izef70 | Ready for Delivery | Abimbola O |
| KM04 | 042j9681 | Ready for Delivery | Abimbola O |
| KM05 | b0tza971 | Awaiting Final Review | Alexander U |
| KM06 | 2zw95f4e | Running Taiga Trajectories & QA | Alexander U |

KM05: all 3 Preference Labels submitted (A++/A++/plain-A) -> moved to Awaiting Final Review. KM06: Abi's prompt self-containment correction applied (reconcile-and-correct instruction); re-uploaded and Taiga re-run + QA now running on the fixed prompt. KM01-04 delivered (Abi O reviewer).

---

## PLATFORM STATUS (2026-06-09, latest board) - KM06 v5 SENT FOR HUMAN REVIEW

| KM | Platform ID | Status | Updated By | Needs Attention |
|----|-------------|--------|------------|-----------------|
| KM01 | Task 1 | Ready for Delivery | Abimbola O | - |
| KM02 | waivf867 | Ready for Delivery | Abimbola O | - |
| KM03 | c8izef70 | Ready for Delivery | Abimbola O | - |
| KM04 | 042j9681 | Ready for Delivery | Abimbola O | - |
| KM05 | b0tza971 | In Final Review | Janette S | Janette S |
| KM06 | 2zw95f4e | Awaiting First Human Review | Alexander U | - |
| (KM06 AQC-EVAL) | [AQC-EVAL] 2zw95f4e | Task Writing | Dhruv Ahuja | Dhruv Ahuja |

KM06: the reconcile-prompt false-closure v4 died at mean ~0.98 and was RETIRED; the insulin-uptitration v5 (job f0934a26, bimodal mean 0.60, four floors) replaced it, FA/GA rewritten (FA 996 / GA 916), and the task is now SENT FOR HUMAN REVIEW (Awaiting First Human Review). NOTE-FOR-ABI-task6.md staged in task6/ for the reviewer (covers v4 retirement, v5 mechanism, draft-attribution fairness, KM05 acknowledged-reuse, workflow = Treatment Plan Documentation for Chronic Disease Management). KM05 advanced from Awaiting Final Review to In Final Review under Janette S. KM01-04 Ready for Delivery (Abi O).

Roll-up: KM01-04 delivered; KM05 in final review (Janette); KM06 v5 awaiting first human review. Pending user action: push the local commits (TASK6-STATE v5 update, FA/GA rewrite, Abi note, this dashboard update) from your own terminal.

---

## UPDATE (2026-06-09, Abi 8:56 AM) - KM06 APPROVED -> PL; variety tip; Tasks 7/8 pivot

- KM06 (2zw95f4e): Abi "Approved. Ready for PL." Now in Preference Labeling - need 3 PLs on 3 different trajectories, PL AutoQC after each. Decider = premature basal-insulin uptitration. Planner: task6/preference-labeling/KM06-PL-recommended-verdicts-DRAFT.md.
- ABI VARIETY TIP (standing design rule): "would recommend future task not all follow the same structure of draft and finalize. We want to see a variety of tasks in your world and not a monotony, this is also an ask of the client." Tasks 7/8 must break the completion wrapper (new artifact/role/mechanism), even at the cost of floor depth.
- TASKS 7/8 PIVOT (pending Abi greenlight): T7 = specialist referral letter to NEPHROLOGY (new artifact + cognitive task; flatten-the-inter-service-tension judgment trap; fair via chart). T8 = inpatient pharmacist medication-therapy plan (new role + artifact; stacked-unsafe-rec, KM01 family, clears ~0.87). Honest trade: variety-first 7/8 likely land fair-clearer-to-mid, not new deep floors; deep floors are banked in KM02-KM06. Superseded/parked: the completion-genre fall-bundle (built, parked) and the gabapentin uptitration trap (verified-strong, unbuilt fallback). Detail in TASK7-STATE.md.

---

## UPDATE (2026-06-09, live frontier) - Tasks 1-6 RFD; T7/T8 active frontier

- KM01-KM06: Ready for Delivery.
- KM07: stuck waiting on EDM input. Local staged packet exists, but no upload/revision/rerun should proceed until that wait clears or Alexander authorizes the exact step.
- KM08: brainstorming for a viable pass. Current v3 inpatient-vs-observation design piloted too easy; use `task8/TASK8-STATE.md` and `task8/design/` as the active planning surface.
