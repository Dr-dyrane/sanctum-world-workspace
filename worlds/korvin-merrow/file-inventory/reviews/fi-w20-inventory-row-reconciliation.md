# FI-W20 Inventory Row Reconciliation

Date: 2026-06-01

Status: RECORDED

## Issue

Batch 4 review identified an apparent supported-tags mismatch between the locked File Inventory v1 row for FI-W20 and the already-constructed FI-W20 candidate file.

The locked FI-W20 row listed:

- Discharge Planning Documentation
- Hospital Discharge Summary Generation
- Traps #3 and #5
- Family vs Primary Team

The constructed FI-W20 candidate file also listed Trap #1 and Endocrinology vs Primary Team.

## Analysis

The constructed FI-W20 file is consistent with locked architecture. The locked File Inventory v1 matrices already place FI-W20 in:

- Trap #1: Prednisone source-of-truth
- Trap #3: Buried functional/cognitive status
- Trap #5: Discharge source-hierarchy
- Family vs Primary Team
- Endocrinology vs Primary Team
- Family report / patient recollection source channels

The locked Synthetic World-Level File Construction Plan v1 also maps FI-W20 to Trap #1, Trap #3, Trap #5, Family vs Primary Team, Endocrinology vs Primary Team, family report, and patient recollection roles.

FI-W20 supports Trap #1 only as collateral family reporting about home medication behavior and uncertainty. It does not become a prednisone source-of-truth file, endocrine authority, final steroid answer, discharge answer file, or override source.

The prednisone hierarchy remains unchanged:

1. Rheumatology attending recommendation.
2. Verified medication reconciliation.
3. Pharmacy / refill history.
4. Family report.
5. Patient recollection.

## Resolution

Canonical resolution: expand the locked FI-W20 row rather than reduce the constructed FI-W20 candidate file.

The FI-W20 row's Supported Workflow(s) / Trap(s) / Friction(s) cell now records:

`Discharge Planning Documentation; Hospital Discharge Summary Generation; Traps #3, #5; Family vs Primary Team; secondary/collateral support for Trap #1 and Endocrinology vs Primary Team through lower-authority family report without overriding rheumatology prednisone authority`

## Rationale

Inventory expansion is the correct reconciliation because the row was under-specified relative to the locked matrices and construction plan. Reducing FI-W20 would remove legitimate collateral evidence that the architecture already assigns to family communication and would create inconsistency with locked trap, friction, and source-of-truth mappings.

The reconciliation preserves:

- FI-W20's primary role as Family Communication / Family vs Primary Team / Traps #3 and #5 support.
- FI-W20's secondary collateral role for Trap #1 and Endocrinology vs Primary Team.
- Family report as lower-authority evidence.
- Rheumatology as the highest outpatient prednisone authority.
- Endocrinology as interpretive, not a hidden answer source.
- Hospitalist-synthesizes-not-defers governance.

## Boundaries

This reconciliation does not:

- change FI-W20 content;
- change the Batch 4 synthetic file contents;
- change Batch 1, Batch 2, or Batch 3 locked synthetic files;
- change the source-of-truth hierarchy;
- change the prednisone hierarchy;
- lock Batch 4 by itself; Batch 4 was later locked by `worlds/korvin-merrow/synthetic-files/ratifications/batch-4-ratification.md`;
- create FI-W22;
- create task files, prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.

## Recommendation

Batch 4 is LOCK READY from the FI-W20 inventory reconciliation perspective, pending Alexander's explicit Batch 4 ratification and lock authorization.
