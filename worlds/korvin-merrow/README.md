# Korvin Merrow World

Current state: Batch 4 Synthetic World-Level File Construction / Candidate Review.

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
- `synthetic-files/`: synthetic file construction lifecycle area. Locked construction plan governs construction order; Batch 1 and Batch 2 files are locked.

## Active Entry Points

- `world-spec-prep/WORLD_SPEC_KICKOFF.md`
- `world-spec-construction/locked/world-spec-v1.md`
- `world-spec-construction/ratifications/world-spec-v1-ratification.md`
- `file-inventory/locked/file-inventory-v1.md`
- `file-inventory/ratifications/file-inventory-v1-ratification.md`
- `synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`
- `synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`
- `synthetic-files/locked/batch-1/batch-1-validation-review.md`
- `synthetic-files/ratifications/batch-1-ratification.md`
- `synthetic-files/locked/batch-2/batch-2-validation-review.md`
- `synthetic-files/ratifications/batch-2-ratification.md`
- `synthetic-files/locked/batch-3/batch-3-validation-review.md`
- `synthetic-files/ratifications/batch-3-ratification.md`
- `synthetic-files/candidate-review/batch-4/batch-4-validation-review.md`
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

World Spec v1 is locked. File Inventory Architecture v1 is locked. Phase 3 File Inventory Architecture is complete. File Inventory v1 is locked at `file-inventory/locked/file-inventory-v1.md`, with FI-W20 row reconciliation recorded at `file-inventory/reviews/fi-w20-inventory-row-reconciliation.md`. File Inventory Planning is complete. Synthetic World-Level File Construction Plan v1 is locked at `synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`. Synthetic File Construction Governance is complete. Batch 1 synthetic world-level files FI-W01 through FI-W07 are locked at `synthetic-files/locked/batch-1/`. Batch 1 Construction is complete. Batch 2 synthetic world-level files FI-W08 through FI-W13 are locked at `synthetic-files/locked/batch-2/`. Batch 2 Construction is complete. Batch 3 synthetic world-level files FI-W14 through FI-W16 are locked at `synthetic-files/locked/batch-3/`. Batch 3 Construction is complete. Batch 4 synthetic world-level files FI-W17 through FI-W21 are in candidate review at `synthetic-files/candidate-review/batch-4/`. Next eligible phase is Batch 4 Candidate Review and ratification decision. Do not create FI-W22, task specifications, task prompts, expected outputs, golden responses, grader guidance, AutoQC responses, DOCX submission artifacts, RL Studio uploads, templates, or reference files until Alexander explicitly authorizes the relevant step.

Task-design guidance: future task prompts and deliverables must be framed from the physician perspective or physician voice, even when supporting sources come from pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources. This is a task-layer rule only; it does not reopen Governance Package v1 or change source-of-truth hierarchy.
