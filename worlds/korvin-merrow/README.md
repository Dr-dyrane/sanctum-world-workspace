# Korvin Merrow World

Current state: Expected Output Architecture v1 / CANDIDATE REVIEW.

Start here only after reading `project/STATUS.md`.

## Folder Guide

- `active/`: current authored world-facing working files and placeholders.
- `planning/`: world-specific pass and planning documents.
- `history/`: historical development artifacts that preserve audit trail.
- `remediation/`: reviewer SEND BACK remediation decision briefs and compliance review.
- `reviews/`: external/human/AutoQC review artifacts and reviewer feedback history.
- `submission/`: RL Studio submission artifacts.
- `world-spec-prep/`: World Spec preparation cockpit plus lifecycle subfolders for locked decisions, locked, ratifications, reviews, decision logs, and planning scaffolds.
- `world-spec-construction/`: World Spec construction lifecycle folders for candidate review artifacts, locked construction artifacts, and ratifications.
- `file-inventory/`: file inventory lifecycle area. Locked architecture defines planned file ecosystem, and locked File Inventory v1 defines the planned inventory rows; neither creates synthetic files or chart contents.
- `synthetic-files/`: synthetic file construction lifecycle area. Locked construction plan governs construction order; Batch 1 through Batch 5 files are locked, and the World-Level Synthetic File Layer is complete.
- `task-layer-architecture/`: task-layer architecture lifecycle area. Locked architecture defines future FI-T governance and does not create task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
- `task-context-files/`: task-level context file lifecycle area. FI-T01 through FI-T07 are locked request-framing files only.
- `supplementary-file-architecture/`: supplementary FI-S architecture lifecycle area. Locked architecture defines future FI-S01 through FI-S04 only and does not construct FI-S files.
- `supplementary-files/`: supplementary FI-S file construction lifecycle area. FI-S01 through FI-S04 are locked supplementary files.
- `task-prompt-architecture/`: task-prompt architecture lifecycle area. Locked Task Prompt Architecture v1 defines future prompt families and packaging rules only; it does not create task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
- `task-prompts/`: task prompt construction lifecycle area. TP-KM01 through TP-KM06 are locked prompts only; they do not create expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.
- `expected-output-architecture/`: expected-output architecture lifecycle area. Candidate Expected Output Architecture v1 defines EO-KM01 through EO-KM06 structure only; it does not create actual expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.

## Active Entry Points

- `world-spec-prep/WORLD_SPEC_KICKOFF.md`
- `world-spec-construction/locked/world-spec-v1.md`
- `world-spec-construction/ratifications/world-spec-v1-ratification.md`
- `file-inventory/locked/file-inventory-v1.md`
- `file-inventory/ratifications/file-inventory-v1-ratification.md`
- `file-inventory/reviews/fi-t-inventory-task-layer-architecture-reconciliation.md`
- `file-inventory/reviews/supplementary-file-trap5-reconciliation.md`
- `synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`
- `synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`
- `synthetic-files/locked/batch-1/batch-1-validation-review.md`
- `synthetic-files/ratifications/batch-1-ratification.md`
- `synthetic-files/locked/batch-2/batch-2-validation-review.md`
- `synthetic-files/ratifications/batch-2-ratification.md`
- `synthetic-files/locked/batch-3/batch-3-validation-review.md`
- `synthetic-files/ratifications/batch-3-ratification.md`
- `synthetic-files/locked/batch-4/batch-4-validation-review.md`
- `synthetic-files/ratifications/batch-4-ratification.md`
- `synthetic-files/locked/batch-5/batch-5-validation-review.md`
- `synthetic-files/ratifications/batch-5-ratification.md`
- `task-layer-architecture/locked/task-level-context-file-architecture-v1.md`
- `task-layer-architecture/ratifications/task-level-context-file-architecture-v1-ratification.md`
- `task-context-files/locked/task-context-files-validation-review.md`
- `task-context-files/ratifications/task-level-context-file-construction-ratification.md`
- `task-context-files/locked/FI-T01_discharge-medication-reconciliation-request-context.md`
- `task-context-files/locked/FI-T02_discharge-summary-drafting-request-context.md`
- `task-context-files/locked/FI-T03_discharge-readiness-care-coordination-request-context.md`
- `task-context-files/locked/FI-T04_consultant-synthesis-interdisciplinary-care-plan-request-context.md`
- `task-context-files/locked/FI-T05_early-post-discharge-follow-up-assessment-request-context.md`
- `task-context-files/locked/FI-T06_patient-safety-readmission-risk-review-request-context.md`
- `task-context-files/locked/FI-T07_medication-safety-handoff-task-context-addendum.md`
- `supplementary-file-architecture/locked/supplementary-file-architecture-v1.md`
- `supplementary-file-architecture/locked/supplementary-file-architecture-validation-review.md`
- `supplementary-file-architecture/ratifications/supplementary-file-architecture-v1-ratification.md`
- `supplementary-files/locked/supplementary-file-construction-validation-review.md`
- `supplementary-files/ratifications/supplementary-file-construction-ratification.md`
- `task-prompt-architecture/locked/task-prompt-architecture-v1.md`
- `task-prompt-architecture/locked/task-prompt-architecture-validation-review.md`
- `task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`
- `task-prompts/locked/task-prompt-construction-validation-review.md`
- `task-prompts/ratifications/task-prompt-construction-ratification.md`
- `task-prompts/locked/TP-KM01.md`
- `task-prompts/locked/TP-KM02.md`
- `task-prompts/locked/TP-KM03.md`
- `task-prompts/locked/TP-KM04.md`
- `task-prompts/locked/TP-KM05.md`
- `task-prompts/locked/TP-KM06.md`
- `expected-output-architecture/candidate-review/expected-output-architecture-v1.md`
- `expected-output-architecture/candidate-review/expected-output-architecture-validation-review.md`
- `supplementary-files/locked/FI-S01_remote-pci-coronary-stent-provenance-summary.md`
- `supplementary-files/locked/FI-S02_remote-sleep-study-osa-provenance-summary.md`
- `supplementary-files/locked/FI-S03_home-support-equipment-logistics-reference.md`
- `supplementary-files/locked/FI-S04_problem-list-past-history-snapshot.md`
- `file-inventory/locked/file-inventory-architecture-v1.md`
- `file-inventory/ratifications/file-inventory-architecture-ratification.md`
- `world-spec-construction/locked/world-spec-skeleton-v1.md`
- `world-spec-construction/ratifications/world-spec-skeleton-ratification.md`
- `world-spec-prep/locked/clinical-story-timeline-package-v1.md`
- `world-spec-prep/ratifications/clinical-story-timeline-ratification.md`
- `world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`
- `world-spec-prep/locked/task-architecture-package-v1.md`
- `world-spec-prep/ratifications/task-architecture-ratification.md`
- `world-spec-prep/locked/medication-expansion-package-v1.md`
- `world-spec-prep/ratifications/medication-expansion-ratification.md`
- `world-spec-prep/reviews/medication-expansion-decision-addendum.md`
- `world-spec-prep/locked/comorbidity-expansion-package-v1.md`
- `world-spec-prep/ratifications/comorbidity-expansion-ratification.md`
- `world-spec-prep/locked/provider-roster-package-v1.md`
- `world-spec-prep/ratifications/provider-roster-ratification.md`
- `world-spec-prep/locked/surgical-history-package-v1.md`
- `world-spec-prep/ratifications/surgical-history-ratification.md`
- `world-spec-prep/locked/daily-hospital-course-framework-v1.md`
- `world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`
- `world-spec-prep/locked/baseline-anchor-package-v1.md`
- `world-spec-prep/ratifications/baseline-anchor-ratification.md`
- `world-spec-prep/locked/identity-package-v1.md`
- `world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`
- `world-spec-prep/decision-logs/physician-decision-log-02.md`
- `world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`
- `active/brainstorm.md`

World Spec v1 is locked. File Inventory Architecture v1 is locked. File Inventory v1 is locked with FI-W20, FI-T, and FI-S03 reconciliations recorded. FI-W01 through FI-W22, FI-T01 through FI-T07, FI-S01 through FI-S04, Task Prompt Architecture v1, and TP-KM01 through TP-KM06 are locked. Entire File Ecosystem, Task Prompt Architecture, and Task Prompts are complete. Task Prompt Architecture v1 is locked at `task-prompt-architecture/locked/task-prompt-architecture-v1.md`, with validation at `task-prompt-architecture/locked/task-prompt-architecture-validation-review.md` and ratification at `task-prompt-architecture/ratifications/task-prompt-architecture-ratification.md`. Task Prompt Construction is locked at `task-prompts/locked/`; ratification is recorded at `task-prompts/ratifications/task-prompt-construction-ratification.md`. Expected Output Architecture v1 is in candidate review at `expected-output-architecture/candidate-review/`. Next eligible phase is Expected Output Architecture Review. Do not create actual expected outputs, golden responses, grader guidance, AutoQC responses, DOCX submission artifacts, RL Studio uploads, templates, or reference files until Alexander explicitly authorizes the relevant step.

Task-design guidance: future task prompts and deliverables must be framed from the physician perspective or physician voice, even when supporting sources come from pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources. This is a task-layer rule only; it does not reopen Governance Package v1 or change source-of-truth hierarchy.

Cross-artifact consistency verification is a standing governance rule. Before creating, modifying, ratifying, or locking architecture, inventory, matrix, mapping, workflow/trap/friction/hierarchy table, or governance artifacts, collaborators must check applicable locked canonical sources and document any coverage or hierarchy change before ratification or lock.
