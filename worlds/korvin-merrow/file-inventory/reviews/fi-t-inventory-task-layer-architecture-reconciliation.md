# FI-T Inventory / Task-Layer Architecture Reconciliation

Status: COMPLETE

Date: 2026-06-02

Purpose: record the authorized reconciliation between locked File Inventory v1, locked Task Architecture Package v1, and candidate Task-Level Context File Architecture v1 before Task-Level Context File Architecture v1 ratification.

This record does not create FI-T files, supplementary files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, or task outputs.

## Inputs

- Locked File Inventory v1: `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`
- Locked Task Architecture Package v1: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`
- Candidate Task-Level Context File Architecture v1: `worlds/korvin-merrow/task-layer-architecture/candidate-review/task-level-context-file-architecture-v1.md`
- Reconciliation review outcome: Task-Level Context File Architecture v1 is ready for ratification after a small reconciliation update.

## Issue

Independent review identified cross-artifact metadata discrepancies:

1. FI-T04 Trap #4 secondary and FI-T05 Trap #3 secondary were present in the candidate architecture but not fully reflected in locked File Inventory metadata.
2. FI-T02, FI-T05, and FI-T06 friction coverage was more granular in the candidate architecture than in FI-T row metadata.
3. P0/P1/P2 labels in the candidate architecture risked appearing as governing task architecture rather than tracker-provenance metadata.

## Analysis

Locked Task Architecture Package v1 supports the disputed secondary trap mappings:

- Trap #4 is supported by Hospital Discharge Summary Generation, Discharge Planning Documentation, and Interdisciplinary Care Plan Development and Documentation.
- Trap #3 is supported by Discharge Planning Documentation, Hospital Discharge Summary Generation, and follow-up/readmission reasoning inside Discharge Planning Documentation.

Locked Task Architecture Package v1 also supports the disputed secondary friction mappings:

- Cardiology vs Nephrology appears in Discharge Medication Reconciliation, Interdisciplinary Care Plan Development and Documentation, and Discharge Planning Documentation.
- Family vs Primary Team appears in Discharge Planning Documentation, Hospital Discharge Summary Generation, and transition/follow-up/readmission reasoning inside Discharge Planning Documentation.
- Endocrinology vs Primary Team appears in Interdisciplinary Care Plan Development and Documentation, Discharge Medication Reconciliation, and Hospital Discharge Summary Generation.

P0/P1/P2 labels are supported as tracker-provenance and historical validation metadata, not as the governing source for task-layer architecture. The locked governing workflow structure remains the four-workflow Task Architecture Package v1 framework.

## Resolution

Canonical resolution: expand locked File Inventory metadata and clarify candidate architecture provenance wording.

The File Inventory update is metadata-only:

- FI-T02 row now records secondary Endocrinology vs Primary Team and Family vs Primary Team support.
- FI-T04 row now records Trap #4 secondary.
- FI-T05 row now records Trap #3 secondary and Endocrinology vs Primary Team support through steroid-plan coherence.
- FI-T06 row now records Cardiology vs Nephrology secondary support through medication-restart safety/readmission-risk review.
- Trap Coverage Matrix now includes FI-T05 as Trap #3 secondary and FI-T04 as Trap #4 secondary.
- Friction Coverage Matrix now includes FI-T06 secondary under Cardiology vs Nephrology, FI-T02/FI-T04 secondary under Family vs Primary Team, and FI-T02 secondary under Endocrinology vs Primary Team.

The candidate architecture update is provenance-only:

- P0/P1/P2 labels are identified as tracker-provenance metadata.
- The locked four-workflow architecture remains governing.
- P0/P1/P2 labels may not create new workflow categories, reopen workflow count, promote historical/superseded labels, or override File Inventory / Task Architecture Package source hierarchy.

## Verification

- FI-T01 through FI-T07 were not constructed.
- FI-S01 through FI-S04 were not constructed.
- No task prompts were created.
- No expected outputs were created.
- No goldens were created.
- No grader guidance was created.
- No AutoQC responses were created.
- No DOCX artifacts were created.
- No RL Studio submission artifacts were created.
- No synthetic world-level files were modified.
- No source-of-truth hierarchy changed.
- No authority hierarchy changed.
- No prednisone hierarchy changed.
- No workflow category was added.
- No candidate artifact was ratified or locked.

## Standing Governance Note

Future architecture, inventory, matrix, mapping, coverage table, workflow table, trap table, friction table, hierarchy table, and governance work must perform explicit cross-artifact consistency verification before creation, modification, ratification, or lock. Do not silently broaden, narrow, redistribute, relabel, or reclassify coverage or hierarchy metadata. If locked artifacts disagree, identify the likely authoritative source and create a reconciliation review before ratification or lock.
