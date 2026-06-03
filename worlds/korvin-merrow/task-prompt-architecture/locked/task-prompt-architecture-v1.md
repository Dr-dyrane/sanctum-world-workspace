# Task Prompt Architecture v1

World: Korvin Merrow

Date created: 2026-06-03

Status: CANDIDATE REVIEW

Purpose: define the future task-prompt system for the locked Korvin Merrow file ecosystem before any task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission artifacts are created.

This is architecture only. It does not write prompt text, expected-output text, golden-response text, grader-guidance text, AutoQC text, task specifications, DOCX artifacts, RL Studio submission artifacts, or new clinical facts.

## Source Basis

Authoritative sources checked:

- Locked World Spec v1.
- Ratified Governance Package v1.
- Locked File Inventory Architecture v1.
- Locked File Inventory v1.
- Locked Task Architecture Package v1.
- Locked Task-Level Context File Architecture v1.
- Locked Supplementary File Architecture v1.
- Locked FI-W01 through FI-W22.
- Locked FI-T01 through FI-T07.
- Locked FI-S01 through FI-S04.
- Batch 1 through Batch 5 ratifications.
- Task-Level Context File Architecture ratification.
- Task-Level Context File Construction ratification.
- Supplementary File Architecture ratification.
- Supplementary File Construction ratification.
- FI-W20 inventory-row reconciliation.
- FI-T inventory / task-layer architecture reconciliation.
- FI-S03 Trap #5 reconciliation.
- Standing Cross-Artifact Consistency Verification rule.
- Reference World Comparative Study observations, used only for prompt-family and packaging pattern awareness.

## 1. Task Prompt Count

Canonical task-prompt count: 6.

Rationale:

- Locked Task Architecture Package v1 targets six task concepts across four workflows.
- Locked File Inventory v1 includes seven FI-T files because FI-T07 is a focused medication-safety handoff / task-context addendum.
- FI-T07 must not become a second near-duplicate medication reconciliation prompt.
- FI-T07 supports the medication-management prompt family as a primary addendum source, not a standalone prompt family.

## 2. Task Inventory

Prompt IDs use the architecture label `TP-KM##` until a later prompt-construction phase authorizes final prompt artifacts.

| Prompt ID | Task family | Primary workflow | Primary FI-T file(s) | Prompt role | Standalone prompt? |
| --- | --- | --- | --- | --- | --- |
| TP-KM01 | Discharge Medication Reconciliation / Medication Safety Review | Discharge Medication Reconciliation | FI-T01 plus FI-T07 addendum | Medication-management task requiring reconciliation of home meds, inpatient actions, consultant timing, prednisone history, functional medication-management safety, and FI-W22 incompleteness. | Yes |
| TP-KM02 | Hospital Discharge Summary Generation | Hospital Discharge Summary Generation | FI-T02 | Physician-facing discharge-summary synthesis task requiring accurate course reconstruction and anti-copy-forward reasoning. | Yes |
| TP-KM03 | Discharge Readiness / Care Coordination Documentation | Discharge Planning Documentation | FI-T03 | Discharge-safety and administrative/care-coordination task requiring functional, family, support, service, and source-hierarchy synthesis. | Yes |
| TP-KM04 | Consultant Synthesis / Interdisciplinary Care Plan | Interdisciplinary Care Plan Development and Documentation | FI-T04 | Physician-led interdisciplinary synthesis task requiring consultant and stakeholder reconciliation without deferring to one source. | Yes |
| TP-KM05 | Early Post-Discharge Follow-Up Assessment | Discharge Planning Documentation | FI-T05 | +7 transition/follow-up reasoning task requiring reconstruction from the locked world without adding new post-world clinical facts. | Yes |
| TP-KM06 | Patient-Safety / Readmission-Risk Review | Discharge Planning Documentation | FI-T06 | +30 retrospective safety/readmission-risk review inside discharge-planning workflow, not a standalone RCA or Patient Risk Stratification workflow. | Yes |

## 3. Task Naming Convention

Future prompt artifacts should use:

- Prompt ID: `TP-KM01` through `TP-KM06`.
- Human-readable family name: concise workflow name from the table above.
- Anchor: discharge anchor, +7 anchor, or +30 anchor as defined by the FI-T source.
- Primary FI-T source in filename or package metadata.

Architecture-only naming pattern:

- `TP-KM01_discharge-medication-reconciliation-medication-safety`
- `TP-KM02_hospital-discharge-summary-generation`
- `TP-KM03_discharge-readiness-care-coordination`
- `TP-KM04_consultant-synthesis-interdisciplinary-care-plan`
- `TP-KM05_early-post-discharge-follow-up-assessment`
- `TP-KM06_patient-safety-readmission-risk-review`

This section does not create filenames, prompt files, DOCX files, or submission packages.

## 4. Task Family Structure

| Prompt ID | Family structure | Differentiation guardrail |
| --- | --- | --- |
| TP-KM01 | Medication reconciliation plus medication-safety handoff. | Must include FI-T07 as addendum support without creating a separate second medication-reconciliation task. |
| TP-KM02 | Discharge-summary synthesis. | Must emphasize clinical evolution and anti-transcription logic, not copied problem-list transcription. |
| TP-KM03 | Discharge readiness / care coordination. | Must stay operational and disposition-safety focused without becoming final safe/unsafe discharge answer text. |
| TP-KM04 | Consultant synthesis / interdisciplinary care plan. | Must preserve hospitalist-synthesizes-not-defers governance and keep all consultants defensible. |
| TP-KM05 | Early post-discharge follow-up assessment. | Must use the +7 anchor as a review frame only; no new +7 clinical facts may be invented. |
| TP-KM06 | Patient-safety / readmission-risk review. | Must remain inside Discharge Planning Documentation; no adverse event, RCA, or new outcome is authorized. |

## 5. Workflow Coverage Matrix

| Locked workflow | Prompt families | Coverage assessment |
| --- | --- | --- |
| Discharge Medication Reconciliation | TP-KM01 | Covered as a primary medication-management prompt family. FI-T07 is used to sharpen medication-safety focus without creating another prompt. |
| Hospital Discharge Summary Generation | TP-KM02 | Covered as a primary physician-document-generation prompt family. |
| Discharge Planning Documentation | TP-KM03, TP-KM05, TP-KM06 | Covered through discharge readiness, +7 follow-up reassessment, and +30 safety/readmission-risk review. These must be differentiated by anchor, requester, and deliverable surface. |
| Interdisciplinary Care Plan Development and Documentation | TP-KM04 | Covered as a distinct consultant-synthesis and care-plan prompt family. |

No new workflow is introduced. P0/P1/P2 labels remain tracker-provenance metadata only.

## 6. Trap Coverage Matrix

| Trap | Primary prompt families | Secondary prompt families | Forbidden collapse patterns |
| --- | --- | --- | --- |
| Trap #1: Prednisone source-of-truth | TP-KM01, TP-KM04 | TP-KM05 | Do not make Endocrinology, family report, patient recollection, FI-W22, FI-T05, or FI-T07 the prednisone authority. Rheumatology remains highest outpatient prednisone-history source. |
| Trap #2: HF/AKI medication reconciliation and time-sensitive consultant logic | TP-KM01, TP-KM04 | TP-KM02, TP-KM05, TP-KM06 | Do not make latest consultant note automatically correct. Do not create a restart algorithm in prompt architecture. Do not collapse Cardiology vs Nephrology. |
| Trap #3: Buried functional/cognitive status | TP-KM03, TP-KM06 | TP-KM05, TP-KM02 | Do not summarize all functional evidence in the prompt. Preserve need to review nursing, PT, OT, family, CM/SW, and related world files. |
| Trap #4: Sepsis anchoring after partial improvement | TP-KM02, TP-KM05 | TP-KM04 | Do not say sepsis was false, infection explains everything, or steroids explain everything. Preserve mixed physiology. |
| Trap #5: Discharge source-hierarchy | TP-KM03, TP-KM04, TP-KM06 | TP-KM01, TP-KM02, TP-KM05 | Do not let FI-W22, any FI-T file, or any prompt become the visible answer file. Preserve Trap #3 vs Trap #5 distinction. |

## 7. Friction Coverage Matrix

| Friction | Prompt families where active | Must not be resolved by architecture |
| --- | --- | --- |
| Cardiology vs Nephrology | TP-KM01, TP-KM04; secondary in TP-KM06 and TP-KM05 | Prompt architecture may require synthesis of renal recovery, potassium, BP reserve, HFrEF/CAD benefit, MAR actions, and trends, but may not choose a final medication-restart authority. |
| Endocrinology vs Primary Team | TP-KM01, TP-KM04, TP-KM05; secondary in TP-KM02 | Prompt architecture may require steroid-risk interpretation but may not prove adrenal insufficiency or replace rheumatology as prednisone-history authority. |
| Family vs Primary Team | TP-KM03, TP-KM05, TP-KM06; secondary in TP-KM02 and TP-KM04 | Prompt architecture may require family/baseline/support synthesis but may not make family concerns independently dispositive or make the Primary Team careless. |

## 8. File Dependency Matrix

Required means the future prompt package must make the file available and the task design must expect review of that evidence. Optional/supporting means the file may be included when packaging needs background texture but must not carry sole critical evidence.

| Prompt ID | Required FI-T | Required FI-W files | Optional/supporting FI-S files |
| --- | --- | --- | --- |
| TP-KM01 | FI-T01, FI-T07 | FI-W03, FI-W04, FI-W05, FI-W06, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, FI-W22 | FI-S01, FI-S04 |
| TP-KM02 | FI-T02 | FI-W01, FI-W02, FI-W03, FI-W07, FI-W08, FI-W09, FI-W10, FI-W11, FI-W12, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W22 | FI-S01, FI-S02, FI-S04 |
| TP-KM03 | FI-T03 | FI-W01, FI-W07, FI-W09, FI-W11, FI-W12, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S02, FI-S03 |
| TP-KM04 | FI-T04 | FI-W02, FI-W03, FI-W08, FI-W10, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S01, FI-S03, FI-S04 as background only if packaging requires |
| TP-KM05 | FI-T05 | FI-W01 through FI-W22 | FI-S01, FI-S02, FI-S03, FI-S04 as background only |
| TP-KM06 | FI-T06 | FI-W01 through FI-W22 | FI-S02, FI-S03, FI-S04 as background only |

File-dependency safeguards:

- FI-W22 must remain visible but incomplete.
- FI-S files may never carry sole critical evidence.
- FI-T files frame the task and do not replace FI-W review.
- No prompt family may depend on a future artifact not already locked.

## 9. Prompt Packaging Rules

Future prompt packages should follow these architecture rules when prompt construction is authorized:

- One primary prompt package per `TP-KM##`.
- Keep prompt wording concise, naturalistic, and clinician-facing.
- Frame the requester and clinical workflow realistically.
- Make the task independent from other tasks.
- Provide the task anchor date without adding unauthorized post-world facts.
- Include the relevant FI-T context file as task framing.
- Include required FI-W files as the clinical world substrate.
- Include FI-S files only as optional/supporting context when appropriate.
- Do not include expected outputs, goldens, grader guidance, or scoring language inside the prompt package unless a future phase explicitly authorizes those artifacts.
- Do not copy full evidence syntheses into prompt text.
- Do not use reference-world folder clutter patterns such as duplicate task folders, old versions, or ambiguous world/task labels.

Style parameters:

- Clinician-facing style: realistic, direct, request-oriented, and physician-centered.
- Workflow framing: each prompt should read like a real clinical work request, not an exam question.
- Handoff style: permitted when a task is a handoff, discharge, transition, or consultant-synthesis workflow.
- Chart-review style: required for all tasks because all tasks must force review of locked world files.
- Request style: concrete deliverable request, but no answer key, rubric, or grading hint.

## 10. Task Classification Matrix

| Prompt ID | Physician-document-generation task | Physician-reasoning task | Medication-management task | Discharge-safety task |
| --- | --- | --- | --- | --- |
| TP-KM01 | Yes, medication reconciliation deliverable when later authorized | Yes | Yes, primary | Yes, secondary through med safety and home medication-management risk |
| TP-KM02 | Yes, discharge summary | Yes | Secondary | Secondary through accurate course and unresolved issues |
| TP-KM03 | Yes, discharge planning / care coordination documentation | Yes | Secondary | Yes, primary |
| TP-KM04 | Yes, interdisciplinary care plan | Yes, primary | Secondary to primary depending on consultant conflict | Yes, secondary |
| TP-KM05 | Yes, follow-up assessment deliverable when later authorized | Yes, primary | Secondary | Yes, primary through transition reassessment |
| TP-KM06 | Yes, safety/readmission-risk review deliverable when later authorized | Yes, primary | Secondary | Yes, primary |

Physician-perspective rule:

- Future prompts and deliverables must remain physician-authored, physician-reviewed, physician-supervised, or physician-communicated.
- Supporting evidence may come from pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources.
- Source-of-truth hierarchy governs factual conflicts; physician-perspective framing governs the final deliverable voice and responsibility.

## 11. Boundary Conditions

This architecture does not authorize:

- task prompt construction;
- prompt text;
- task specification files;
- expected outputs;
- golden responses;
- grader guidance;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- browser/RL Studio activity;
- new FI-W, FI-T, or FI-S files;
- changes to locked clinical, world, task-context, or supplementary artifacts.

## 12. Construction Roadmap

Roadmap only:

1. Task Prompt Architecture Review.
2. Task Prompt Architecture Ratification and Lock.
3. Task Prompt Construction.
4. Expected Output Architecture.
5. Golden Architecture.
6. Grader Guidance Architecture.
7. Packaging.
8. AutoQC / submission activity only when explicitly authorized.

## Final Status

Task Prompt Architecture v1

Status:

CANDIDATE REVIEW

Next Eligible Phase:

Task Prompt Architecture Review
