# Task Prompt Construction Validation Review

World: Korvin Merrow

Date created: 2026-06-03

Status: CANDIDATE REVIEW

Scope: validation of Task Prompt Package v1 construction only. This is not ratification, lock, expected-output construction, golden construction, grader-guidance construction, AutoQC, DOCX packaging, or submission work.

## Validation Summary

Task Prompt Package v1 constructs six physician-authored task prompts (TP-KM01 through TP-KM06) compliant with locked Task Prompt Architecture v1, Task Architecture Package v1, File Inventory v1, and Task-Level Context File Architecture v1. No prohibited artifacts were created.

## Cross-Artifact Consistency Verification

Checked against:

- Locked Task Prompt Architecture v1.
- Locked Task Architecture Package v1.
- Locked File Inventory v1.
- Locked Task-Level Context File Architecture v1.
- Locked FI-T01 through FI-T07.
- Locked Governance Package v1.
- Locked Supplementary File Architecture v1.

Result: aligned.

The construction does not broaden or narrow locked workflow coverage, trap coverage, friction coverage, hierarchy rules, task responsibilities, or authority hierarchy. Each prompt follows the assigned workflow, trap assignment, friction assignment, dependency matrix, differentiation guardrails, and anti-answer-file protections from Task Prompt Architecture v1.

## Construction Verification

| Requirement | Result | Notes |
| --- | --- | --- |
| Six prompts created | PASS | TP-KM01 through TP-KM06 created in candidate-review/. |
| TP-KM01 constructed | PASS | Discharge Medication Reconciliation / Medication Safety Review. FI-T01 + FI-T07 addendum. Discharge anchor. |
| TP-KM02 constructed | PASS | Hospital Discharge Summary Generation. FI-T02. Discharge anchor. |
| TP-KM03 constructed | PASS | Discharge Readiness / Care Coordination Documentation. FI-T03. Discharge anchor. |
| TP-KM04 constructed | PASS | Consultant Synthesis / Interdisciplinary Care Plan. FI-T04. Discharge anchor. |
| TP-KM05 constructed | PASS | Early Post-Discharge Follow-Up Assessment. FI-T05. +7 anchor. No new facts beyond world. |
| TP-KM06 constructed | PASS | Patient-Safety / Readmission-Risk Review. FI-T06. +30 anchor. No RCA workflow. |
| Validation review created | PASS | This document created. |

## Architecture Compliance Verification

| Requirement | Result | Notes |
| --- | --- | --- |
| Workflow assignment compliance | PASS | All four locked workflows represented. No new workflow introduced. |
| Trap assignment compliance | PASS | All five traps mapped per Task Prompt Architecture v1. Trap #3 vs Trap #5 distinction preserved. |
| Friction assignment compliance | PASS | All three frictions mapped per Task Prompt Architecture v1. No friction resolved. |
| Dependency matrix compliance | PASS | Required FI-T and FI-W dependencies per Task Prompt Architecture v1. FI-S not included in prompts (architecture allows optional/supporting use only). |
| Differentiation guardrails preserved | PASS | TP-KM01 includes FI-T07 addendum without creating second medication task. TP-KM03/05/06 differentiated by anchor and requester. |
| Anti-answer-file protections preserved | PASS | No prompt reveals traps, frictions, hierarchy rules, or expected outputs. |

## Specific Guardrail Verification

| Guardrail | Prompt | Result | Notes |
| --- | --- | --- | --- |
| FI-T07 addendum relationship | TP-KM01 | PASS | FI-T01 and FI-T07 both referenced as context files. No second medication task created. |
| No medication restart algorithm | TP-KM01 | PASS | Prompt asks for reconciliation recommendation, not algorithm. Consultant tensions preserved. |
| No Cardiology vs Nephrology resolution | TP-KM01 | PASS | Prompt acknowledges multiple consultant perspectives without choosing winner. |
| Discharge-readiness anchor only | TP-KM03 | PASS | Prompt asks for assessment, not final disposition answer. |
| No final discharge answer | TP-KM03 | PASS | Prompt asks for discharge-readiness assessment, not safe/unsafe determination. |
| +7 day follow-up anchor | TP-KM05 | PASS | Prompt uses +7 anchor as task date. |
| No new facts beyond world | TP-KM05 | PASS | Prompt explicitly states not to invent new symptoms, labs, or outcomes. |
| +30 day retrospective safety anchor | TP-KM06 | PASS | Prompt uses +30 anchor as review date. |
| No RCA workflow | TP-KM06 | PASS | Prompt frames as retrospective risk assessment, not root-cause analysis. |
| No new workflow | TP-KM06 | PASS | Prompt stays inside Discharge Planning Documentation workflow. |

## Boundary Verification

| Prohibited artifact | Created? | Result |
| --- | --- | --- |
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

## Prompt Style Verification

| Style requirement | Result | Notes |
| --- | --- | --- |
| Realistic clinical work | PASS | All prompts read like clinician requests, not exam questions. |
| Clinician-facing requester | PASS | Hospitalist, pharmacy, case management, primary care, quality team requesters used. |
| Workflow-based framing | PASS | Each prompt frames a specific clinical workflow. |
| Chart-review expectation | PASS | All prompts explicitly require chart review. |
| No trap disclosure | PASS | No prompt mentions traps, frictions, or hierarchy rules. |
| No answer hints | PASS | No prompt reveals expected outputs or grading expectations. |

## Watch Items For Review

- Confirm TP-KM03, TP-KM05, and TP-KM06 remain sufficiently differentiated by requester, time anchor, reasoning emphasis, and deliverable surface during later expected-output construction.
- Confirm FI-T07 addendum relationship remains explicit during golden construction to avoid creating a second near-duplicate medication reconciliation task.
- Confirm no prompt wording inadvertently leaks trap/friction/hierarchy language during later phases.

## Final Status

Task Prompt Construction

Status: CANDIDATE REVIEW

Files Constructed: TP-KM01 through TP-KM06

Next Eligible Phase: Task Prompt Construction Review
