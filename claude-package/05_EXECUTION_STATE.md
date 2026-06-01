# Execution State

Purpose: compressed current state for Claude. Use `project/STATUS.md` and `docs/status-dashboard.md` locally for live status.

## Project State

Current phase: File Inventory v1 / File Inventory v1 candidate review.

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

- No reviewer blocker. Preparation Layer is complete. World Spec Skeleton v1 is locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`. World Spec v1 is locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`, with ratification recorded at `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`. World Spec Construction is complete. File Inventory Architecture v1 is locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`, with ratification recorded at `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`. Phase 3 File Inventory Architecture is complete. File Inventory v1 candidate table is active at `worlds/korvin-merrow/file-inventory/candidate-review/file-inventory-v1.md`. Synthetic files, chart notes, discharge summaries, medication lists, medication schedules, lab values, vital signs, consultant recommendation text, tasks, prompts, expected outputs, goldens, grader guidance, DOCX submission packaging, AutoQC, and RL Studio upload remain gated on explicit Alexander authorization for the relevant step.

Next legal action:

- Use `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md` and `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md` for orientation.
- Use `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md` and `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md` as the locked Clinical Story Skeleton v1 record.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md` for ratified governance/story-logic guardrails.
- Use `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md` as the locked identity source.
- Use `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md` for carry-forward implementation notes only; do not reopen locked identity values.
- Use `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md` as the ratified governance source.
- Use `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md` for accepted governance clarifications.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md` for governance ratification status.
- Use `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md` for the canonical date framework and `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md` for the locked +7/+30-from-discharge doctrine.
- Use `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md` for locked baseline anchors and `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md` for physician sign-off.
- Use `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md` as the locked story-evolution framework.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md` for ratification and carry-forward trap-distinction notes.
- Use `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md` only as historical task-architecture interview scaffold; `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md` is authoritative.
- Use `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md` as the locked task-architecture package.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md` for task architecture ratification, 2.108 contingency, and workflow-supersession notes.
- Use `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md` as the locked medication architecture package.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md` for the medication expansion ratification record.
- Use `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md` for the accepted physician decision removing insulin lispro from baseline architecture and reserving it as future inpatient-only candidate logic.
- Use `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md` as the locked baseline comorbidity architecture.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md` for comorbidity ratification and carry-forward watch items.
- Use `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md` as the locked provider/care-team roster architecture.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md` for provider roster ratification and naming guardrails.
- Use `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md` as the locked surgical/procedural history architecture.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md` for surgical-history ratification and noise-control guardrails.
- Use `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md` as the locked HD1-HD6 daily evolution framework.
- Use `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md` for preparation-layer completion and daily framework ratification.
- Use `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md` as the locked World Spec Skeleton.
- Use `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md` for World Spec Skeleton ratification and watch items.
- Do not revise the locked Clinical Story Skeleton or locked Identity Package, draft World Spec, create milestones, or create file inventory until Alexander explicitly starts/authorizes the relevant phase.
- Do not modify Brainstorm unless new reviewer feedback arrives.

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
- World Spec example source documents recorded under `reference/word-spec-examples/`.
- File Inventory Architecture v1 ratified and locked: `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`.
- File Inventory Architecture ratification recorded: `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`.
- File Inventory v1 candidate table created: `worlds/korvin-merrow/file-inventory/candidate-review/file-inventory-v1.md`.

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

- State synchronization and preparation.
- World Spec Construction activities explicitly authorized by Alexander, one step at a time.
- Auditing.
- Checklist building.
- Reviewer-risk analysis.
- Claude package refresh.
- Local documentation updates that preserve phase boundaries.

## Not Authorized Right Now

- Revising the locked Clinical Story Skeleton without explicit Alexander approval.
- Revising Identity Package v1 without explicit Alexander approval.
- Treating the Identity Package review addendum as permission to reopen MRN, DOB, age, anthropometrics, allergy, or code status.
- Changing Governance Package v1 without Alexander approval.
- World Spec drafting before explicit Alexander authorization for drafting.
- Populating the World Spec template before explicit Alexander authorization for template population.
- Creating synthetic file contents, chart notes, or downstream file/task outputs.
- Creating milestones before Alexander authorizes that step.
- Creating medication schedules, medication reconciliation outputs, hospital medication changes, admission medication lists, or discharge medication lists before Alexander authorizes those steps.
- Creating synthetic patient files.
- Creating final task prompts.
- Creating golden responses.
- Creating grader guidelines.
- Creating failure analysis.
- Changing Brainstorm clinical content beyond the approved reviewer remediation.
- Modifying Brainstorm unless new reviewer feedback arrives.
- Further identity changes or task concept changes beyond the reviewer-required Korvin Merrow remediation without Alexander approval.
- Accessing RL Studio or browser operations without explicit authorization.

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
- `reference/world-spec-guidelines/08_autoqc_master_index.md`
- `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`
- `project/WORKSPACE_FILE_MAP.md`
