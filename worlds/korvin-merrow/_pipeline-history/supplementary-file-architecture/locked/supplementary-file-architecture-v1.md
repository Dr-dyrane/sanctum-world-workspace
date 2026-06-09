# Supplementary File Architecture v1

Date created: 2026-06-02

Status: CANDIDATE REVIEW

## 1. Scope

This artifact designs the FI-S supplementary file layer for the Korvin Merrow world.

It defines:

- whether supplementary files are required;
- exact FI-S count;
- purpose and boundaries for each future FI-S file;
- workflow, trap, friction, hierarchy, and anti-answer-file rules;
- how FI-S files may support FI-T files without replacing world review.

This artifact does not create:

- FI-S files;
- task prompts;
- expected outputs;
- goldens;
- grader guidance;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- new clinical facts.

## 2. Cross-Artifact Consistency Verification

Supplementary File Architecture v1 was checked against the following locked sources:

- World Spec v1;
- Governance Package v1;
- File Inventory Architecture v1;
- File Inventory v1;
- Task-Level Context File Architecture v1;
- locked FI-W01 through FI-W22;
- locked FI-T01 through FI-T07;
- Batch 1 through Batch 5 ratifications;
- Task-Level Context File Construction ratification;
- FI-W20 inventory-row reconciliation;
- FI-T inventory / task-layer architecture reconciliation;
- Cross-Artifact Consistency Verification standing governance rule.

No new workflow, trap, friction, hierarchy, authority assignment, or source-of-truth rule is introduced here. FI-S coverage is limited to coverage already recorded in locked File Inventory v1 and locked File Inventory Architecture v1.

## 3. Supplementary Necessity Determination

Supplementary files are required for the final planned file ecosystem because locked File Inventory v1 contains four FI-S rows and the locked matrices already include those rows in workflow, trap, friction, authority, and temporal coverage.

They remain supplementary, not essential answer sources.

Supplementary files are justified only because they:

- add realistic chart texture;
- support source hierarchy and task navigation;
- make the world less one-click without increasing core ambiguity;
- provide background or logistics context already mapped in locked inventory.

They must not carry sole critical evidence.

## 4. Exact FI-S Count

Exact FI-S count: 4.

This count is fixed by locked File Inventory v1:

- FI-S01: Remote PCI / coronary stent provenance summary.
- FI-S02: Remote sleep-study / OSA provenance summary.
- FI-S03: Home support / equipment logistics reference.
- FI-S04: Problem list / past history snapshot.

No FI-S05 or higher is authorized by this architecture.

## 5. FI-S Inventory Architecture

| File ID | Intended role | Information scope | Relationship to world files | Permitted content classes | Prohibited content classes |
| --- | --- | --- | --- | --- | --- |
| FI-S01 | Remote PCI / coronary stent provenance summary. | Pre-admission coronary history provenance, remote PCI/stent background, chronic CAD/HFrEF prevention context. | May support FI-W07, FI-W14, FI-W15, FI-W22, FI-T01, FI-T02, and FI-T07 as background texture. Must not replace medication history, MAR actions, objective trends, or consultant reasoning. | Remote procedure history, non-acute cardiology/PCP provenance, chronic prevention context, uncertainty around old records if realistic. | Acute coronary event, new PCI, inpatient procedure, final GDMT restart decision, final medication list, Cardiology-vs-Nephrology winner, Trap #2 answer key. |
| FI-S02 | Remote sleep-study / OSA provenance summary. | Pre-admission OSA provenance and background reserve context. | May support FI-W07, FI-W17, FI-W18, FI-W19, FI-W22, FI-T02, FI-T03, FI-T05, and FI-T06 as background context only. Must not explain the admission or dominate functional/discharge reasoning. | Historical sleep-study/provenance details, baseline OSA context, CPAP/background adherence texture if already consistent with locked world facts. | New hypoxemia arc, acute respiratory failure, hidden cause of altered mental status, final discharge-readiness answer, Trap #3 or Trap #5 answer key. |
| FI-S03 | Home support / equipment logistics reference. | HD5-HD6 transition logistics through 05/23/2026 18:00, equipment/services/home support details. | May support FI-W20, FI-W21, FI-W22, FI-T03, FI-T05, and FI-T06 as transition-planning texture. Must not replace nursing/PT/OT/family/case management evidence. | DME logistics, home layout/support details, service coordination status, caregiver-capacity logistics, unresolved authorization or timing uncertainty. | Final safe/unsafe discharge conclusion, final services authorization, complete home-care plan, family concern resolution, Primary Team negligence proof, post-world outcome. |
| FI-S04 | Problem list / past history snapshot. | HD1 or pre-admission imported problem-list/history texture. | May support FI-W03, FI-W04, FI-W07, FI-W22, FI-T01, FI-T02, and FI-T07 as low-authority background. Must not outrank stronger sources or become the discharge summary substrate. | Comorbidity list, remote procedure/problem-list texture, stale or copied-forward problem-list features if clearly non-authoritative. | New diagnosis, final diagnosis list, final discharge problem list, medication-reconciliation answer, prednisone source-of-truth answer, copy-forward answer file. |

## 6. Workflow Relationship Matrix

| Locked workflow | FI-S support | Boundary |
| --- | --- | --- |
| Discharge Medication Reconciliation | FI-S01 and FI-S04. | Support chronic CAD/procedure and background history texture only. Final medication reasoning still requires FI-W03, FI-W04, FI-W05, FI-W06, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, FI-W22, FI-T01, and FI-T07. |
| Hospital Discharge Summary Generation | FI-S01, FI-S02, and FI-S04. | Support background history/provenance only. The discharge summary must synthesize ED/admission, hospitalist course, objective trends, consultant chronology, functional/family evidence, and FI-W22. |
| Discharge Planning Documentation | FI-S02 and FI-S03. | Support reserve/logistics context only. Discharge readiness still requires FI-W01, FI-W07, FI-W09, FI-W11, FI-W12, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22, FI-T03, FI-T05, and FI-T06. |
| Interdisciplinary Care Plan Development and Documentation | No primary FI-S file. | FI-S files may provide background only if surfaced by a future prompt. Interdisciplinary synthesis remains grounded in FI-W02, FI-W03, FI-W08, FI-W10, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W20, FI-W22, and FI-T04. |

## 7. Trap Relationship Matrix

| Trap | FI-S relationship | Boundary |
| --- | --- | --- |
| Trap #1: Prednisone source-of-truth | No FI-S file has authorized Trap #1 coverage. FI-S04 may contain background problem-list texture only. | FI-S04 must not become a prednisone source. Rheumatology remains highest outpatient prednisone authority, followed by verified medication reconciliation, pharmacy/refill history, family report, and patient recollection. |
| Trap #2: HF/AKI medication reconciliation and time-sensitive consultant logic | FI-S01 provides indirect secondary support only. | FI-S01 may support remote CAD/stent provenance but must not decide medication restart timing, override FI-W12 trends, convert FI-W13 MAR/action evidence into a final plan, or resolve Cardiology vs Nephrology. |
| Trap #3: Buried functional/cognitive status | No primary FI-S Trap #3 coverage. FI-S02 may provide background reserve context only. | FI-S02 must not explain functional decline. Trap #3 remains buried across nursing, PT, OT, family, and care-coordination world files. |
| Trap #4: Sepsis anchoring after partial improvement | No FI-S coverage. | FI-S files must not reframe the admission, prove a hidden diagnosis, or change mixed physiology. |
| Trap #5: Discharge source-hierarchy | FI-S03 provides secondary support only. | FI-S03 may add logistics texture but must not become a final discharge plan, final services authorization, or visible answer file. FI-W22 remains visible but incomplete, and world review remains necessary. |

## 8. Friction Relationship Matrix

| Friction | FI-S relationship | Boundary |
| --- | --- | --- |
| Cardiology vs Nephrology: medication restart timing | FI-S01 may provide indirect background support. | FI-S01 must not make Cardiology correct by default, make Nephrology overly cautious by default, or resolve medication restart timing. |
| Family vs Primary Team: discharge readiness | FI-S03 may provide secondary transition-logistics support. | FI-S03 must not make family concerns independently dispositive or make the Primary Team careless. It must not replace FI-W17 through FI-W21 or FI-W22. |
| Endocrinology vs Primary Team: steroid interpretation and risk | No FI-S coverage. | FI-S files must not become steroid-risk interpretation sources or alter prednisone hierarchy. |

## 9. Authority And Source-Hierarchy Constraints

FI-S files must preserve the locked authority hierarchy:

1. Attending Hospitalist.
2. Consulting Attending Specialists.
3. PT/OT Functional Assessments.
4. Case Management / Social Work.
5. Family Reports.
6. Patient Recollection.

FI-S files must preserve the locked master source-of-truth hierarchy:

1. Attending Documentation.
2. Verified Medication Reconciliation.
3. Pharmacy History.
4. Consultant Documentation.
5. Primary Care Documentation.
6. Family Report.
7. Patient Recollection.

FI-S files must preserve the prednisone-specific hierarchy:

1. Rheumatology attending recommendation.
2. Verified medication reconciliation.
3. Pharmacy / refill history.
4. Family report.
5. Patient recollection.

Supplementary files are background/provenance/logistics texture. They do not outrank locked world-level sources, task-context files, or source-of-truth hierarchies.

## 10. Temporal Boundaries

FI-S temporal anchors must follow locked File Inventory v1:

- FI-S01: pre-admission provenance.
- FI-S02: pre-admission provenance.
- FI-S03: HD5-HD6 through 05/23/2026 18:00.
- FI-S04: HD1 or pre-admission import.

FI-S03 must not extend beyond the world close. No FI-S file may add +7, +30, post-discharge outcome, or discharge-finalization facts.

## 11. Prohibited Content Classes

No FI-S file may contain:

- final medication reconciliation;
- final discharge summary;
- final disposition decision;
- final home-services authorization;
- final consultant synthesis;
- final steroid taper;
- new lab values or vital-sign trends;
- new medication schedules;
- new diagnoses;
- new procedures;
- post-world outcomes;
- task prompts;
- expected outputs;
- goldens;
- grader guidance;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts.

## 12. Anti-Answer-File Protections

FI-S files must remain low-stakes support files.

They must not:

- carry sole critical evidence;
- collapse any trap;
- resolve any friction;
- replace FI-W01 through FI-W22;
- replace FI-T01 through FI-T07;
- substitute for FI-W22 or make FI-W22 complete;
- convert lower-authority background into governing source-of-truth;
- make the world easier by collecting dispersed evidence into one file.

## 13. FI-S / FI-T Interaction Rules

FI-S files may help FI-T files by adding background texture or clarifying why a requester might ask a task.

FI-S files may not:

- provide the answer a future FI-T task asks for;
- supply missing world evidence;
- narrow future prompts into one-source review;
- duplicate FI-T request framing;
- replace physician synthesis.

Future task prompts must still require review of locked FI-W files and relevant locked FI-T context files. FI-S files may be supporting context, never the principal evidence base.

## 14. Construction Roadmap

This architecture authorizes no file construction by itself.

Future phases require explicit Alexander authorization:

1. Supplementary File Architecture Review.
2. Supplementary File Architecture Ratification and Lock.
3. FI-S01 through FI-S04 Supplementary File Construction.
4. Supplementary File Construction Review.
5. Supplementary File Construction Ratification and Lock.
6. Task Prompt Architecture.
7. Task Prompt Construction.
8. Expected Output Architecture.
9. Golden Architecture.
10. Grader Guidance Architecture.
11. Packaging.

## 15. Final Architecture Status

Supplementary File Architecture v1:

- Status: CANDIDATE REVIEW.

Next eligible phase:

- Supplementary File Architecture Review.
