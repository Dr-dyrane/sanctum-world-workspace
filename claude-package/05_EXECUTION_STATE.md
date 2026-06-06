# Execution State

Purpose: compressed current state for Claude. Use `project/STATUS.md` and `docs/status-dashboard.md` locally for live status.

## Project State

Current phase: Task 1 Preference Labeling. World Spec approval is complete, onboarding has ended, engineering pipeline run #1 completed, Step 9 generated-file review is closed, Final Files AutoQC passed 78/78 after three revisions, and the world was created as `Healthcare_247_Merrow` on 2026-06-05 at 11:20 AM PDT. Pod assignment is `#vaguspod`; EPM Rose; pod leads Abi O and Larry E. Task 1 advanced through AO rework, hardening, Abi pre-check, revised platform entry, pilot runs, and FA/GA. Alexander reports the current platform state is Preference Labeling. Source-of-truth: 06/02 instruction document, Step 15. PL compares two selected attempts (Response A vs Response B) against the golden response, selects the A4-B4 preference scale, and writes the seven-section justification. Step 9 audit trail remains at `worlds/korvin-merrow/file-review/`; Task 1 canonical lifecycle state is `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md`; governing review records are under `worlds/korvin-merrow/task-setup/reviews/`. Reasoning discipline lives at `docs/reasoning-discipline.md`.

Pipeline run #1 / Step 9 closeout state:

- Output ingested at `worlds/korvin-merrow/file-review/pipeline-output/`.
- Generated files: 33 DOCX files under `pipeline-output/filesystem/`.
- Metadata: 134 `.meta` files under `pipeline-output/.meta/`.
- Initial World Files AutoQC: 74/76 pass; the two fails were access/routing failures, not inspected-content failures.
- Final Files AutoQC: 78/78 pass after revision #3.
- World created: `Healthcare_247_Merrow`, world ID `world_d50c832ac6474a68ba982a77e28a6bbe`, snapshot `snap_0fb032e95b324710b12a7432cf7da6c1`, 26 files synced.
- Active protocol: `worlds/korvin-merrow/file-review/file-review-protocol.md`.
- Active Claude-assisted triage: `worlds/korvin-merrow/file-review/findings-triage.md`.
- Candidate revision log: `worlds/korvin-merrow/file-review/file-review-log.md`.
- Revised 33-file working snapshot: `worlds/korvin-merrow/file-review/revision/filesystem/`.
- Final 26-file world-level upload set: `worlds/korvin-merrow/file-review/upload/filesystem/`.
- Seven task-level files are held out at `worlds/korvin-merrow/file-review/task-files-holdback/` for later task setup handling.
- Items marked `[A]` required Alexander physician ruling before edits; rulings and candidate edits are recorded in the file-review log.
- Do not access RL Studio, upload additional task prompts/goldens/grader guidelines, run additional agents, run additional QA, create AutoQC responses, create task setup materials, edit the submitted Failure Analysis / Grader Analysis, create Preference Labeling text, run FA+PL AutoQC, or mutate platform state beyond Alexander-authorized PL work unless Alexander explicitly authorizes the exact step.

Transcript resolution: `docs/claude-transcript-formatted.md` is the authoritative transcript upload artifact. The Claude share URL `https://claude.ai/share/d5129364-5d6c-4a2c-acb3-282f367a0040` is supporting provenance and reviewer-access support. `docs/claude-transcript.md` remains raw historical/provenance evidence only. Historical James Carter references and export encoding artifacts inside it are expected provenance, not current identity defects.

FI-W20 inventory row reconciliation is recorded at `worlds/korvin-merrow/file-inventory/reviews/fi-w20-inventory-row-reconciliation.md`. FI-S03 Trap #5 reconciliation is recorded at `worlds/korvin-merrow/file-inventory/reviews/supplementary-file-trap5-reconciliation.md`. World-Level Synthetic File Layer, Task-Level Context Files, Supplementary Files, the Entire File Ecosystem, Task Prompt Architecture, Task Prompt Construction, Expected Output Architecture, Expected Output Construction, Golden Architecture, Golden Construction, Grader Guidance Architecture, Grader Guidance Construction, AutoQC Architecture, AutoQC Construction, Packaging Architecture, Packaging Construction, and Submission Preparation are complete and locked. AutoQC Architecture v1 is locked under `worlds/korvin-merrow/autoqc-architecture/locked/` with ratification at `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`. AutoQC Construction is locked under `worlds/korvin-merrow/autoqc/locked/` with ratification at `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`. AutoQC is complete. Packaging Architecture v1 is locked under `worlds/korvin-merrow/packaging-architecture/locked/` with ratification at `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`. Packaging Construction is locked under `worlds/korvin-merrow/packaging/locked/` with `packaging-construction-v1.md` and `packaging-construction-validation-review.md`; ratification is recorded at `worlds/korvin-merrow/packaging/ratifications/packaging-construction-ratification.md`. Packaging is complete. Submission Preparation locked artifacts are under `worlds/korvin-merrow/submission-preparation/locked/`. Execution Preparation v1 locked artifacts are under `worlds/korvin-merrow/execution-preparation/locked/`, with ratification at `worlds/korvin-merrow/execution-preparation/ratifications/execution-preparation-ratification.md`. Task Prompt Architecture v1 is locked at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-v1.md`, with validation review at `worlds/korvin-merrow/task-prompt-architecture/locked/task-prompt-architecture-validation-review.md` and ratification at `worlds/korvin-merrow/task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`. Task Prompt Construction is locked at `worlds/korvin-merrow/task-prompts/locked/`; TP-KM01 through TP-KM06 and `task-prompt-construction-validation-review.md` are locked, with ratification recorded at `worlds/korvin-merrow/task-prompts/ratifications/task-prompt-construction-ratification.md`. Expected Output Architecture v1 is locked at `worlds/korvin-merrow/expected-output-architecture/locked/`, with ratification recorded at `worlds/korvin-merrow/expected-output-architecture/ratifications/expected-output-architecture-ratification.md`. Expected Output Construction is locked under `worlds/korvin-merrow/expected-outputs/locked/`; EO-KM01 through EO-KM06 and `expected-output-construction-validation-review.md` are locked, with ratification recorded at `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`. FI-T07 remains addendum support for EO-KM01 only; no EO-KM07 exists. Golden Architecture v1 is locked at `worlds/korvin-merrow/golden-architecture/locked/`, with audit reconciliation preserved at `worlds/korvin-merrow/golden-architecture/locked/golden-architecture-audit-reconciliation.md` and ratification recorded at `worlds/korvin-merrow/golden-architecture/ratifications/golden-architecture-ratification.md`. Golden Construction is locked at `worlds/korvin-merrow/goldens/locked/`: Golden-KM01 through Golden-KM06 plus `golden-construction-validation-review.md`. Ratification is recorded at `worlds/korvin-merrow/goldens/ratifications/golden-construction-ratification.md`. Goldens are complete. No Golden-KM07 exists. Grader Guidance Architecture v1 locked artifacts are under `worlds/korvin-merrow/grader-guidance-architecture/locked/`: `grader-guidance-architecture-v1.md` and `grader-guidance-architecture-validation-review.md`, with ratification recorded at `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`. Grader Guidance Construction is locked under `worlds/korvin-merrow/grader-guidance/locked/` with GG-KM01 through GG-KM06 and `grader-guidance-construction-validation-review.md`; ratification is recorded at `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`. Grader Guidance is complete. No GG-KM07, scoring rubric, scoring threshold, pass/fail band, point allocation, AutoQC response, populated DOCX artifact, manifest, final submission package, upload record, or submission artifact has been created.

Brainstorm:

- Original Brainstorm submitted in RL Studio.
- RL Studio task ID: `cyau8803`.
- RL Studio status: Brainstorm approved / ready for World Spec transition.
- Original submission timestamp: `5/29/2026 2:49 PM PDT`.
- Revised Korvin Merrow Brainstorm uploaded after SEND BACK remediation.
- Brainstorm AutoQC rerun: `0 failed / 51 passed`.
- Diagnostics reviewed.
- Plan resubmitted for reviewer review.
- Human Review: GO from Stacey S after SEND BACK remediation.
- Approval source: Slack / Stacey S.
- Reviewer message: "great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."

Current blocker:

- Active blocker: no repository blocker. Current platform work is Task 1 Preference Labeling. Do not invent A/B details or draft PL text without the actual selected responses and explicit Alexander authorization. Task 2 has a local seed draft folder only; Tasks 2-6 may continue locally only if Alexander explicitly authorizes bounded parallel prep. Additional platform actions beyond the current PL gate remain gated on explicit Alexander authorization for the exact step.

Next legal action:

- Use `worlds/korvin-merrow/task-setup/task1-lifecycle-log.md` as the canonical Task 1 source of truth.
- Use the 06/02 instruction document PL section, `docs/world-pipeline-playbook.md` section A5, `TASK-RUNBOOK.md`, and `docs/reasoning-discipline.md` for Task 1 Preference Labeling support.
- Use `worlds/korvin-merrow/file-review/file-review-protocol.md`, `worlds/korvin-merrow/file-review/time-strategy-and-state.md`, `worlds/korvin-merrow/file-review/findings-triage.md`, and `worlds/korvin-merrow/file-review/file-review-log.md` as the closed Step 9 audit trail.
- Treat `worlds/korvin-merrow/file-review/pipeline-output/filesystem/` as the downloaded V1 output, `worlds/korvin-merrow/file-review/revision/filesystem/` as the final revised 33-file working set, and `worlds/korvin-merrow/file-review/upload/filesystem/` as the final 26-file world-level upload set used for world creation.
- Treat `worlds/korvin-merrow/file-review/task-files-holdback/` as the seven task-level files intentionally held out of the world-level upload set for later task setup handling.
- Do not access RL Studio, upload task setup materials, run agents, run QA, create AutoQC responses, edit the submitted Failure Analysis / Grader Analysis, create PL text, run FA+PL AutoQC, or mutate platform state beyond the authorized PL work unless Alexander explicitly authorizes the exact step.
- Do not revise locked architecture, locked canon, original final submission staging, or the original pipeline output unless Alexander explicitly authorizes reopening.

## Completed

- Brainstorm physician interview.
- Brainstorm draft assembly.
- Brainstorm internal audit.
- Claude hostile Brainstorm review triage and selective remediation.
- Brainstorm AutoQC remediation.
- Official Brainstorm template rebuild.
- Submission artifact generation: `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`.
- RL Studio Brainstorm upload.
- Brainstorm AutoQC final pass recorded.
- Brainstorm submitted for Human Review.
- Human Review SEND BACK captured.
- Synthetic identity and World Type remediation applied locally.
- Comorbidity decision brief created and physician-approved.
- Medication decision brief created and physician-approved.
- Reviewer remediation compliance review created.
- Active Brainstorm source updated with approved comorbidity expansion and medication specificity.
- `Korvin_Merrow_Brainstorm.docx` regenerated and locally verified.
- Revised Korvin Merrow Brainstorm uploaded to RL Studio.
- Brainstorm AutoQC rerun completed: `0 failed / 51 passed`.
- Diagnostics reviewed.
- Plan resubmitted for reviewer review.
- Brainstorm Human Review GO received from Stacey S.
- Reviewer GO recorded: `worlds/korvin-merrow/reviews/reviewer-go-01.md`.
- World Spec preparation packet created.
- Official World Spec template acquired: `reference/templates/World_Spec_Template_05_06.docx`.
- World Spec AutoQC v6.3 acquired: `reference/templates/AutoQC_Section_2_World_Spec_v6.3_writer.docx`.
- 113-check AutoQC master index created: `reference/world-spec-guidelines/08_autoqc_master_index.md`.
- World Spec writer playbook created: `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`.
- Reviewer response protocol created: `docs/reviewer-response-protocol.md`.
- Repository hardening and documentation completed.
- Document tooling installed and verified.
- MCP/integration audit completed.
- Claude World Spec prep review triaged: `worlds/korvin-merrow/world-spec-prep/reviews/claude-review-triage.md`.
- Workspace file map created: `project/WORKSPACE_FILE_MAP.md`.
- Post-GO interview plan created: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/post-go-interview-plan.md`.
- World Spec kickoff packet created: `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`.
- Workspace bloat/doctrine audit recorded inside the kickoff packet.
- Physician decision log created: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`.
- Post-kickoff physician decisions synchronized across kickoff, status, dashboard, clinical logic, and Claude handoff files.
- Clinical Story Skeleton interview framework created.
- Clinical Story Skeleton v1 locked by Alexander.
- Clinical Story Skeleton v1 reviewed with GO recommendation.
- Clinical Story Skeleton lock recorded in `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`.
- Clinical Story Skeleton v1 ratified after Claude hostile review minor findings.
- Ratification artifact created: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`.
- Identity Package v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`.
- Identity Package hostile-review addendum recorded: `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`.
- Governance Package v1 ratified: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`.
- Governance Package clarification recorded: `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`.
- Governance Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`.
- Physician Architecture Layer completed.
- Key Milestones Calendar Skeleton v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`.
- Key Milestones Calendar ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`.
- Baseline Anchor Package v1 locked after physician review: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`.
- Baseline Anchor Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`.
- Clinical Story Timeline Package v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`.
- Clinical Story Timeline Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`.
- Task Architecture Interview v1 preserved as planning scaffold: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`.
- Task Architecture Package v1 locked: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`.
- Task Architecture Package ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`.
- Medication Expansion Package v1 created for candidate review: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`.
- Medication Expansion Package v1 physician decisions resolved; decision addendum created: `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md`.
- Medication Expansion Package v1 ratified and locked: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`.
- Comorbidity Expansion Package v1 created for candidate review and then ratified/locked: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`.
- Comorbidity Expansion Package v1 ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`.
- Provider Roster Package v1 created for candidate review and then ratified/locked: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`.
- Provider Roster Package v1 ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`.
- Surgical History Package v1 created for candidate review and then ratified/locked: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`.
- Surgical History Package v1 ratification recorded: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`.
- Daily Hospital Course Framework v1 ratified and locked: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`.
- Preparation Layer completed: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`.
- World Spec Skeleton v1 locked and ratified: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`.
- World Spec v1 ratified and locked: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`.
- World Spec v1 ratification recorded: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`.
- World Spec example source documents recorded under `reference/word-spec-examples/` as local-only / gitignored reference material.
- File Inventory Architecture v1 ratified and locked: `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`.
- File Inventory Architecture ratification recorded: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`.
- File Inventory v1 ratified and locked: `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`.
- File Inventory v1 ratification recorded: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-v1-ratification.md`.
- File Inventory Planning completed.
- Synthetic World-Level File Construction Plan v1 ratified and locked: `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`.
- Synthetic World-Level File Construction Plan ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`.
- Synthetic File Construction Governance completed.
- Batch 1 synthetic world-level files ratified and locked: FI-W01 through FI-W07 under `worlds/korvin-merrow/synthetic-files/locked/batch-1/`.
- Batch 1 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md`.
- Batch 1 validation review locked: `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md`.
- Batch 2 synthetic world-level files ratified and locked: FI-W08 through FI-W13 under `worlds/korvin-merrow/synthetic-files/locked/batch-2/`.
- Batch 2 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md`.
- Batch 2 validation review locked: `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md`.
- Collaborator session-exit discipline integrated as a standing process / handoff rule in `AGENTS.md`, `project/STATUS.md`, `docs/status-dashboard.md`, `docs/git-workflow.md`, and Claude handoff surfaces.
- Batch 3 synthetic world-level files ratified and locked: FI-W14 through FI-W16 under `worlds/korvin-merrow/synthetic-files/locked/batch-3/`.
- Batch 3 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-3-ratification.md`.
- Batch 3 validation review locked: `worlds/korvin-merrow/synthetic-files/locked/batch-3/batch-3-validation-review.md`.
- Batch 4 synthetic world-level files locked: FI-W17 through FI-W21 under `worlds/korvin-merrow/synthetic-files/locked/batch-4/`.
- Batch 4 validation review recorded: `worlds/korvin-merrow/synthetic-files/locked/batch-4/batch-4-validation-review.md`.
- Batch 4 ratification recorded: `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md`.
- Batch 5 synthetic world-level file FI-W22 ratified and locked at `worlds/korvin-merrow/synthetic-files/locked/batch-5/FI-W22_discharge-facing-plan-snapshot-before-world-close.md`.
- Batch 5 validation review preserved at `worlds/korvin-merrow/synthetic-files/locked/batch-5/batch-5-validation-review.md`.
- Batch 5 ratification recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-5-ratification.md`.
- World-Level Synthetic File Layer completed: FI-W01 through FI-W22 locked.
- World-Level Layer Closure Audit passed at `worlds/korvin-merrow/reviews/world-level-layer-closure-audit.md`.
- Task-Level Context File Architecture v1 ratified and locked at `worlds/korvin-merrow/task-layer-architecture/locked/task-level-context-file-architecture-v1.md`.
- Task-Level Context File Architecture v1 ratification recorded at `worlds/korvin-merrow/task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`.
- Task-Level Context Files locked: FI-T01 through FI-T07.
- Supplementary Files locked: FI-S01 through FI-S04.
- Task Prompt Architecture v1 locked.
- Task Prompt Construction locked: TP-KM01 through TP-KM06.
- Expected Output Architecture v1 locked.
- Expected Output Construction ratified and locked: EO-KM01 through EO-KM06 plus `worlds/korvin-merrow/expected-outputs/locked/expected-output-construction-validation-review.md`.
- Expected Output Construction ratification recorded at `worlds/korvin-merrow/expected-outputs/ratifications/expected-output-construction-ratification.md`.
- Golden Architecture v1 locked.
- Golden Construction ratified and locked: Golden-KM01 through Golden-KM06 plus `worlds/korvin-merrow/goldens/locked/golden-construction-validation-review.md`.
- Grader Guidance Architecture v1 ratified and locked: `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-v1.md`.
- Grader Guidance Architecture validation review locked: `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md`.
- Grader Guidance Architecture ratification recorded: `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`.
- Grader Guidance Construction ratified and locked: GG-KM01 through GG-KM06 under `worlds/korvin-merrow/grader-guidance/locked/`.
- Grader Guidance Construction validation review locked: `worlds/korvin-merrow/grader-guidance/locked/grader-guidance-construction-validation-review.md`.
- Grader Guidance Construction ratification recorded: `worlds/korvin-merrow/grader-guidance/ratifications/grader-guidance-construction-ratification.md`.
- Grader Guidance status: COMPLETE.
- AutoQC Architecture v1 locked artifact: `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-v1.md`.
- AutoQC Architecture v1 validation review locked artifact: `worlds/korvin-merrow/autoqc-architecture/locked/autoqc-architecture-validation-review.md`.
- AutoQC Architecture v1 ratification recorded: `worlds/korvin-merrow/autoqc-architecture/ratifications/autoqc-architecture-ratification.md`.
- AutoQC Construction locked artifact: `worlds/korvin-merrow/autoqc/locked/autoqc-construction-v1.md`.
- AutoQC Construction validation review locked artifact: `worlds/korvin-merrow/autoqc/locked/autoqc-construction-validation-review.md`.
- AutoQC Construction ratification recorded: `worlds/korvin-merrow/autoqc/ratifications/autoqc-construction-ratification.md`.
- Packaging Architecture v1 locked artifact: `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-v1.md`.
- Packaging Architecture validation review locked artifact: `worlds/korvin-merrow/packaging-architecture/locked/packaging-architecture-validation-review.md`.
- Packaging Architecture ratification recorded: `worlds/korvin-merrow/packaging-architecture/ratifications/packaging-architecture-ratification.md`.
- Packaging Construction v1 candidate artifact: `worlds/korvin-merrow/packaging/locked/packaging-construction-v1.md`.
- Packaging Construction validation review candidate artifact: `worlds/korvin-merrow/packaging/locked/packaging-construction-validation-review.md`.

## Latest Git Checkpoints

- `af603ed checkpoint: expand world spec preparation and review workflow`
- `cf2ad14 checkpoint: install and verify document tooling stack`
- `17d6eb1 add instruction guide for new writers`
- `0d9b066 checkpoint: harden repository workflow and documentation`
- `02bb7bd checkpoint: add world spec autoqc prompt`
- `949929a checkpoint: prepare world spec operating packet`
- `b9b8766 checkpoint: submit brainstorm for human review`
- `6e8e0fd checkpoint: record brainstorm autoqc pass`
- `8820ddd checkpoint: rebuild brainstorm using official docx template`
- `96b5a68 checkpoint: address brainstorm autoqc findings`
- `6318735 checkpoint: complete Korvin Merrow identity migration`
- `1ca33f0 checkpoint: apply brainstorm reviewer remediation`
- `6e2ffb9 checkpoint: refresh reviewer remediation continuity files`
- `646f1df checkpoint: record brainstorm remediation resubmission`

## Authorized Right Now

- Task 1 AO review rework support.
- Claude-assisted review/de-hinting of Tasks 2-6 task prompts, goldens, and grader guidelines against final generated files, Task 1 lessons, and the 06/02 instruction guide.
- Local documentation updates that preserve phase boundaries.
- Drive sync planning notes only; do not mutate Drive unless explicitly authorized.
- Local documentation updates that preserve phase boundaries.
- Claude package refresh.
- Applying collaborator session-exit discipline at the end of every working session.

## Not Authorized Right Now

- Revising the locked Clinical Story Skeleton without explicit Alexander approval.
- Revising Identity Package v1 without explicit Alexander approval.
- Treating the Identity Package review addendum as permission to reopen MRN, DOB, age, anthropometrics, allergy, or code status.
- Changing Governance Package v1 without Alexander approval.
- Additional RL Studio access, task-material uploads, agent runs, QA runs, edits to submitted Failure Analysis / Grader Analysis, PL text creation/submission beyond the current authorized PL stage, or platform mutation before explicit authorization for the exact action.
- Rerunning Final Files AutoQC, uploading revisions, or using Apply to Task unless explicitly authorized for a corrective platform action.
- Applying edits labeled PROTECT.
- Editing generated DOCX files or locked task-layer artifacts before Alexander authorizes the exact change.
- Uploading task setup materials before explicit authorization.
- Creating AutoQC responses before explicit authorization.
- Creating additional supplementary files, chart notes, or downstream task outputs before explicit authorization.
- Creating milestones before Alexander authorizes that step.
- Creating medication schedules, medication reconciliation outputs, hospital medication changes, admission medication lists, or discharge medication lists before Alexander authorizes those steps.
- Creating additional synthetic patient files beyond locked Batch 1 before explicit authorization.
- Revising locked task prompts without explicit authorization.
- Reopening or modifying locked expected outputs without explicit authorization.
- Creating additional golden responses or revising candidate goldens without explicit authorization.
- Locking grader guidance before authorized review/ratification.
- Creating scoring rubrics.
- Creating scoring thresholds.
- Creating pass/fail bands.
- Creating point allocations.
- Creating failure analysis.
- Redesigning the world, reopening Governance Package v1, or changing source-of-truth hierarchy because of the Medicine Team Lead task-design guidance.
- Changing Brainstorm clinical content beyond the approved reviewer remediation.
- Modifying Brainstorm unless new reviewer feedback arrives.
- Further identity changes or task concept changes beyond the reviewer-required Korvin Merrow remediation without Alexander approval.
- Accessing RL Studio or browser operations without explicit authorization.

## Collaborator Session Exit Discipline

Standing process / handoff rule:

1. Working tree must be clean, or uncommitted state must be explicitly documented.
2. Current phase and next eligible phase must be updated.
3. Locked artifacts must remain unchanged unless Alexander explicitly authorized reopening or editing them.
4. Candidate artifacts must be clearly located and status-labeled.
5. Newly locked artifacts must move to locked paths, with ratifications created and referenced.
6. Continuity surfaces and Claude handoff files must be updated.
7. Stale active candidate paths must be removed or explicitly marked historical.
8. Unauthorized files must not be created.
9. Carry-forward watch items and future task-layer guidance must be preserved.
10. A checkpoint commit must be created for completed work unless Alexander explicitly instructs not to commit.
11. Final reports must state what changed, what did not change, current status, next eligible phase, and whether the repository is safe for another collaborator to continue.

## Claude Operating Mode

Claude remains the official Sanctum drafting assistant, but drafting is gated.

Claude may help:

- compress context;
- critique plans against AutoQC v6.3;
- identify reviewer risks;
- prepare Governance Package interview questions;
- organize physician decisions after Alexander provides them.

Claude must not replace physician judgment or originate clinical design.

## Current Prep Artifacts To Use

- `claude-package/01_SANCTUM_CORE_RULES.md`
- `claude-package/02_BRAINSTORM_GUIDE.md`
- `claude-package/03_WORLD_SPEC_GUIDE.md`
- `claude-package/04_KORVIN_MERROW_CONTEXT.md`
- `claude-package/05_EXECUTION_STATE.md`
- `claude-package/06_HANDOFF_STATE.md`
- `worlds/korvin-merrow/active/brainstorm.md`
- `worlds/korvin-merrow/active/task-map.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/claude-review-triage.md`
- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/post-go-interview-plan.md`
- `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`
- `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`
- `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`
- `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`
- `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`
- `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`
- `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`
- `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`
- `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md`
- `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-v1.md`
- `worlds/korvin-merrow/grader-guidance-architecture/locked/grader-guidance-architecture-validation-review.md`
- `worlds/korvin-merrow/grader-guidance-architecture/ratifications/grader-guidance-architecture-ratification.md`
- `reference/world-spec-guidelines/08_autoqc_master_index.md`
- `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`
- `project/WORKSPACE_FILE_MAP.md`
