# Task Prompt Architecture Validation Review

World: Korvin Merrow

Date created: 2026-06-03

Status: CANDIDATE REVIEW

Scope: validation of Task Prompt Architecture v1 only. This is not ratification, lock, prompt construction, expected-output construction, golden construction, grader-guidance construction, AutoQC, DOCX packaging, or submission work.

## Validation Summary

Task Prompt Architecture v1 creates an architecture for six future task prompt families and preserves all locked boundaries.

## Cross-Artifact Consistency Verification

Checked against:

- World Spec v1.
- Governance Package v1.
- File Inventory Architecture v1.
- File Inventory v1.
- Task Architecture Package v1.
- Task-Level Context File Architecture v1.
- Supplementary File Architecture v1.
- FI-W01 through FI-W22.
- FI-T01 through FI-T07.
- FI-S01 through FI-S04.
- Ratification records for world-level batches, task-context files, and supplementary files.
- FI-W20, FI-T, and FI-S03 reconciliation records.

Result: aligned.

The architecture does not broaden or narrow locked workflow coverage, trap coverage, friction coverage, hierarchy rules, task responsibilities, or authority hierarchy. It converts the locked six-task-concept architecture and seven FI-T support files into six prompt families, preserving FI-T07 as an addendum/support file for TP-KM01 rather than a separate prompt.

## Coverage Verification

| Requirement | Result | Notes |
| --- | --- | --- |
| Task inventory defined | PASS | Six prompt families defined as TP-KM01 through TP-KM06. |
| Task naming convention defined | PASS | Architecture-only naming convention defined without creating prompt files. |
| Task family structure defined | PASS | Each task family has a distinct workflow surface and differentiation guardrail. |
| Workflow coverage complete | PASS | All four locked workflows are represented. No new workflow created. |
| Trap coverage complete | PASS | All five traps mapped. Trap #3 / Trap #5 distinction preserved. |
| Friction coverage complete | PASS | All three frictions mapped. No friction resolved. |
| File mappings complete | PASS | Required FI-T and FI-W dependencies defined; FI-S limited to optional/supporting use. |
| Physician-document-generation tasks identified | PASS | Matrix records document-generation task status. |
| Physician-reasoning tasks identified | PASS | Matrix records reasoning expectations at architecture level. |
| Medication-management tasks identified | PASS | TP-KM01 primary; secondary medication roles preserved elsewhere. |
| Discharge-safety tasks identified | PASS | TP-KM03, TP-KM05, and TP-KM06 primary; secondary roles preserved. |
| Prompt packaging rules defined | PASS | Packaging architecture defined without prompt text. |

## Boundary Verification

| Prohibited artifact | Created? | Result |
| --- | --- | --- |
| Actual task prompts | No | PASS |
| Prompt text | No | PASS |
| Expected outputs | No | PASS |
| Golden responses | No | PASS |
| Grader guidance | No | PASS |
| AutoQC responses | No | PASS |
| DOCX artifacts | No | PASS |
| RL Studio submission artifacts | No | PASS |
| New FI-W files | No | PASS |
| New FI-T files | No | PASS |
| New FI-S files | No | PASS |
| New clinical facts | No | PASS |
| Locked artifact edits | No | PASS |

## Reference Study Handling

Reference world observations were used only for high-level packaging lessons:

- prompt families should be short, naturalistic, and workflow-facing;
- one task package should map cleanly to one prompt family;
- future packages should avoid duplicate/old folders and ambiguous labels;
- grader/golden architecture remains a future phase.

Reference worlds did not override Korvin canon, source-of-truth hierarchy, task count, workflow count, trap coverage, friction coverage, or file dependencies.

## Watch Items For Review

- Confirm six prompt families is accepted, with FI-T07 preserved as TP-KM01 addendum support rather than a seventh prompt.
- Confirm TP-KM03, TP-KM05, and TP-KM06 remain sufficiently differentiated within Discharge Planning Documentation.
- Confirm TP-KM01 vs FI-T07 differentiation remains explicit before later prompt construction.
- Confirm no prompt wording is accidentally introduced during review edits.

## Final Status

Task Prompt Architecture v1

Status:

CANDIDATE REVIEW

Next Eligible Phase:

Task Prompt Architecture Review
