# Grader Guidance Architecture v1

World: Korvin Merrow

Date created: 2026-06-03

Status: CANDIDATE REVIEW

Purpose: define the architecture for future grader guidance for the six locked Korvin Merrow task prompts, expected outputs, and golden responses.

This is architecture only. It defines grader guidance count, IDs, mapping, philosophy, acceptable-answer principles, unacceptable-answer principles, critical reasoning dimensions, source-synthesis expectations, hierarchy expectations, friction-handling expectations, uncertainty expectations, task-specific failure modes, prohibited grader drift, and downstream relationships. It does not create grader guidance text, scoring rubrics, scoring thresholds, pass/fail bands, AutoQC responses, DOCX artifacts, RL Studio materials, or submission artifacts.

## Source Basis

Authoritative locked sources checked:

- Locked World Spec v1.
- Ratified Governance Package v1.
- Locked File Inventory v1.
- Locked FI-W01 through FI-W22.
- Locked FI-T01 through FI-T07.
- Locked FI-S01 through FI-S04.
- Locked Task Architecture Package v1.
- Locked Task-Level Context File Architecture v1.
- Locked Task Prompt Architecture v1.
- Locked task prompts TP-KM01 through TP-KM06.
- Locked Expected Output Architecture v1.
- Locked expected outputs EO-KM01 through EO-KM06.
- Locked Golden Architecture v1.
- Locked golden responses Golden-KM01 through Golden-KM06.
- Golden Construction ratification.
- FI-W20 inventory-row reconciliation.
- FI-T inventory / task-layer architecture reconciliation.
- FI-S03 Trap #5 reconciliation.
- Standing physician-perspective task-layer rule.
- Standing Cross-Artifact Consistency Verification rule.
- Official source-guide rule that task prompts, golden responses, and grader guidelines are writer-owned; AI may assist with QC after human-authored material exists but may not originate final grader guidelines.
- Local reference grader guideline examples, used only for structural pattern awareness.

## 1. Grader Guidance Count And IDs

Canonical grader guidance architecture count: 6.

Rationale:

- There are six locked task prompts: TP-KM01 through TP-KM06.
- There are six locked expected outputs: EO-KM01 through EO-KM06.
- There are six locked golden responses: Golden-KM01 through Golden-KM06.
- FI-T07 remains medication-safety addendum support for TP-KM01, EO-KM01, Golden-KM01, and future GG-KM01 only.
- FI-T07 does not create a seventh task, expected output, golden, or grader guidance artifact.

Grader guidance IDs:

| Grader guidance ID | Locked prompt | Locked expected output | Locked golden | Standalone future grader guidance? |
| --- | --- | --- | --- | --- |
| GG-KM01 | TP-KM01 | EO-KM01 | Golden-KM01 | Yes |
| GG-KM02 | TP-KM02 | EO-KM02 | Golden-KM02 | Yes |
| GG-KM03 | TP-KM03 | EO-KM03 | Golden-KM03 | Yes |
| GG-KM04 | TP-KM04 | EO-KM04 | Golden-KM04 | Yes |
| GG-KM05 | TP-KM05 | EO-KM05 | Golden-KM05 | Yes |
| GG-KM06 | TP-KM06 | EO-KM06 | Golden-KM06 | Yes |

No GG-KM07 should be created.

## 2. Core Grading Philosophy

Future grader guidance should reward strong physician reasoning, not verbatim matching to the golden.

The locked golden is the benchmark for a strong answer. It is not the only defensible answer. Grading architecture must preserve:

- multi-path defensibility;
- chart-grounded synthesis;
- evidence reconciliation;
- uncertainty handling;
- hierarchy application;
- friction preservation;
- physician-perspective judgment;
- task-scope discipline.

A future grader should credit responses that reach a clinically safe, source-aware, and task-appropriate answer even if wording, order, or emphasis differs from the locked golden. A future grader should penalize responses that contradict locked chart evidence, invent facts, collapse uncertainty, ignore source hierarchy, over-trust a single file, or answer a different task.

## 3. Recommended Future Grader Guidance Shape

Future grader guidance may use a consistent structure inspired by the local reference examples, but this architecture does not write the final guidance.

Recommended future sections:

1. Golden reference: identify the associated Golden-KM artifact as the benchmark.
2. Clinical reasoning that should be present and correct.
3. Scope and format expectations.
4. Good practice that may receive credit but should not be required.
5. Known errors to penalize.
6. Scoring instruction placeholder for a later authorized grader-guidance construction phase.

Architecture guardrail: this section defines a future shape only. It does not assign points, create thresholds, create pass/fail criteria, or write final evaluator-facing instructions.

## 4. Acceptable-Answer Principles

Future grader guidance should allow answers that:

- are clinically grounded in the locked chart;
- preserve uncertainty where the locked chart is uncertain;
- apply the appropriate hierarchy without using hierarchy as a shortcut;
- synthesize across multiple files rather than relying on one visible source;
- preserve consultant and family/team frictions as reasonable disagreements;
- maintain physician voice or physician-supervised responsibility;
- remain within the requested deliverable type;
- identify monitoring, education, follow-up, support, or clarification needs when task-relevant;
- state when a final answer cannot be fully determined from the provided record.

Acceptable variation includes:

- different wording;
- different ordering of sections;
- different but defensible clinical emphasis;
- different sequencing proposals when the response explains monitoring and safety logic;
- concise or expanded style if the task's clinical substance is preserved.

## 5. Unacceptable-Answer Principles

Future grader guidance should flag or penalize answers that:

- fabricate symptoms, labs, vitals, visits, services, readmissions, adverse events, recovery outcomes, discharge outcomes, medication orders, or final discharge prescriptions not present in locked sources;
- treat the golden as a word-for-word answer key rather than a clinical benchmark;
- treat FI-W22, FI-T files, or FI-S files as complete answer sources;
- allow FI-S files to carry sole critical evidence;
- ignore required FI-W evidence dependencies;
- ignore FI-T task framing;
- expose or rely on internal trap labels, trap numbers, or hidden grading logic;
- collapse mixed physiology into sepsis-only, adrenal-only, medication-only, or family-only explanations;
- resolve consultant disagreement by choosing the highest-ranked authority without synthesis;
- convert discharge-readiness assessment into a final discharge authorization;
- convert patient-safety review into RCA, blame assignment, or outcome scoring;
- invent +7 or +30 facts to make the task easier.

## 6. Critical Reasoning Dimensions

Future grader guidance should evaluate whether the response demonstrates the following reasoning dimensions when relevant to the task:

| Dimension | Required architectural meaning |
| --- | --- |
| Task fit | Response answers the specific prompt and deliverable type, not a neighboring task. |
| Chart synthesis | Response integrates required FI-T framing, relevant FI-W evidence, and optional FI-S context without source overreach. |
| Clinical safety | Response avoids unsafe medication, discharge, steroid, follow-up, or outcome conclusions unsupported by the chart. |
| Temporal reasoning | Response respects world close, discharge anchor, +7 anchor, and +30 anchor boundaries. |
| Hierarchy reasoning | Response applies authority, master source-of-truth, and prednisone hierarchy appropriately. |
| Friction handling | Response preserves defensible stakeholder/specialist tension instead of picking automatic winners. |
| Uncertainty handling | Response names uncertainty where appropriate and avoids false closure. |
| Physician perspective | Response reads as physician-authored, physician-reviewed, physician-supervised, or physician-communicated. |

## 7. Source-Synthesis Expectations

Future grader guidance should expect answers to synthesize source classes rather than cite every file mechanically.

Global source rules:

- FI-T files frame the task and date anchor.
- FI-W files carry the world evidence.
- FI-S files provide background, provenance, logistics, or low-stakes texture only.
- FI-W22 is visible but incomplete and must be reconciled against more detailed sources.
- No single file should settle a task by itself.

Task-specific source dependency architecture:

| GG ID | Required FI-T | Required FI-W sources | Optional FI-S context | Source-synthesis focus |
| --- | --- | --- | --- | --- |
| GG-KM01 | FI-T01, FI-T07 | FI-W03, FI-W04, FI-W05, FI-W06, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, FI-W22 | FI-S01, FI-S04 | Medication provenance, inpatient actions, consultant timing, trends, prednisone hierarchy, medication-management safety, FI-W22 incompleteness. |
| GG-KM02 | FI-T02 | FI-W01, FI-W02, FI-W03, FI-W07, FI-W08, FI-W09, FI-W10, FI-W11, FI-W12, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W22 | FI-S01, FI-S02, FI-S04 | Hospital-course narrative, anti-copy-forward synthesis, mixed physiology, consultant chronology, functional/family evidence, unresolved discharge caveats. |
| GG-KM03 | FI-T03 | FI-W01, FI-W07, FI-W09, FI-W11, FI-W12, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S02, FI-S03 | Discharge readiness, functional/cognitive reserve, family baseline, home support, services/equipment logistics, visible-plan limitations. |
| GG-KM04 | FI-T04 | FI-W02, FI-W03, FI-W08, FI-W10, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S01, FI-S03, FI-S04 | Consultant synthesis, hospitalist-led reconciliation, objective trend and MAR context, steroid-source hierarchy, discharge logistics, uncertainty preservation. |
| GG-KM05 | FI-T05 | FI-W01 through FI-W22 | FI-S01, FI-S02, FI-S03, FI-S04 | Early follow-up priorities based only on locked hospitalization evidence and transition-risk substrate. |
| GG-KM06 | FI-T06 | FI-W01 through FI-W22 | FI-S02, FI-S03, FI-S04 | Patient-safety/readmission-risk signals visible before discharge planning closed; no new outcome creation. |

## 8. Hierarchy Expectations

Future grader guidance should evaluate hierarchy use as reasoning, not rote rank-ordering.

Authority hierarchy:

1. Attending Hospitalist.
2. Consulting Attending Specialists.
3. PT/OT Functional Assessments.
4. Case Management / Social Work.
5. Family Reports.
6. Patient Recollection.

Master source-of-truth hierarchy:

1. Attending Documentation.
2. Verified Medication Reconciliation.
3. Pharmacy History.
4. Consultant Documentation.
5. Primary Care Documentation.
6. Family Report.
7. Patient Recollection.

Prednisone-specific hierarchy:

1. Rheumatology attending recommendation.
2. Verified medication reconciliation.
3. Pharmacy / refill history.
4. Family report.
5. Patient recollection.

Grader architecture rules:

- Factual conflicts should be assessed through the relevant source hierarchy.
- Consultant disagreements should be assessed through synthesis, timing, trends, patient status, and discharge safety.
- Family reports should be credited as baseline-informed evidence but not treated as automatically dispositive.
- Patient recollection should be credited as clinically relevant but lower-authority.
- Rheumatology remains the highest outpatient prednisone-history source.

## 9. Friction-Handling Expectations

Future grader guidance should preserve frictions as defensible people/perspective conflicts.

| Friction | Active GG IDs | Future grader architecture expectation |
| --- | --- | --- |
| Cardiology vs Nephrology | GG-KM01, GG-KM04; secondary GG-KM05, GG-KM06 | Credit answers that balance HFrEF/CAD protection against AKI/CKD, potassium, BP, intake, volume status, and monitoring. Penalize automatic consultant-winner logic. |
| Endocrinology vs Primary Team | GG-KM01, GG-KM04, GG-KM05; secondary GG-KM02, background GG-KM06 | Credit answers that preserve steroid risk and prednisone-source uncertainty without proving adrenal insufficiency or dismissing infection/renal/volume contributors. |
| Family vs Primary Team | GG-KM03, GG-KM05, GG-KM06; secondary GG-KM02, GG-KM04 | Credit answers that treat family concern as baseline-informed evidence while preserving that primary-team discharge planning is clinically plausible. |

## 10. Uncertainty Expectations

Future grader guidance should reward explicit uncertainty handling when the locked chart is intentionally uncertain.

Uncertainty should be preserved around:

- actual recent prednisone ingestion;
- adrenal suppression risk versus proven adrenal insufficiency;
- infection source and infection contribution versus mixed physiology;
- exact safe medication restart sequence;
- final discharge readiness;
- family support capacity and medication-management reliability;
- +7 and +30 outcomes, symptoms, services, labs, vitals, visits, or readmissions.

Future grader guidance should not require certainty where the chart withholds certainty.

## 11. Task-Specific Failure Mode Architecture

This section defines failure-mode domains for future grader guidance. It does not assign points or write final rubric language.

| GG ID | Task-specific failures future guidance should watch |
| --- | --- |
| GG-KM01 | Rigid medication answer key; automatic restart of all chronic HF/diabetes medications; permanent hold without reassessment; prednisone decision based on low-authority recollection; converting inpatient lispro into home regimen; ignoring FI-W22 incompleteness or medication-management safety. |
| GG-KM02 | Copying early sepsis framing forward; omitting mixed physiology; omitting consultant chronology; inventing culture/steroid/follow-up facts; presenting a final completed discharge outcome; ignoring functional/family evidence. |
| GG-KM03 | Treating medical improvement as discharge authorization; treating family concern as dispositive or irrelevant; relying on FI-W22 alone; ignoring nursing/PT/OT/CM/SW evidence; creating final service approval or discharge order. |
| GG-KM04 | Choosing a consultant winner; applying hierarchy as shortcut; creating final medication list or prednisone taper; ignoring objective trends/MAR context; erasing family and functional evidence; over-resolving discharge uncertainty. |
| GG-KM05 | Inventing +7 symptoms, labs, vitals, visits, services, adherence, or outcomes; solving the case retrospectively; omitting medication, renal/cardiac, steroid, diabetes, functional, and support follow-up priorities. |
| GG-KM06 | Creating a readmission, adverse event, RCA, blame finding, or outcome; treating risk review as Patient Risk Stratification workflow; ignoring pre-discharge risk signals; over-trusting visible discharge plan; failing to distinguish risk from causality. |

## 12. Protected Golden-Specific Guardrails

Future grader guidance architecture must protect:

- Golden-KM01 from becoming a rigid medication answer key.
- Golden-KM03 from becoming a discharge authorization key.
- Golden-KM05 from permitting invented follow-up facts.
- Golden-KM06 from becoming RCA or outcome scoring.
- FI-W22 from becoming a complete answer source.
- FI-S files from becoming sole critical evidence.
- Hierarchy from becoming shortcut answer logic.
- Frictions from becoming automatic winner selection.

## 13. Prohibited Grader Drift

Future grader guidance must not drift into:

- verbatim golden matching as the main standard;
- point allocation or scoring thresholds unless a later phase explicitly authorizes them;
- hidden trap-number exposure in evaluator-facing or user-facing task material;
- new task responsibilities;
- new workflows;
- new expected-output surfaces;
- new clinical facts;
- new file dependencies;
- new discharge outcomes;
- new follow-up facts;
- new readmission/adverse-event narrative;
- grading based on preferences outside the locked chart.

## 14. Relationship To Future AutoQC

This architecture is upstream of future AutoQC preparation.

Future AutoQC preparation should:

- use the official Section 6 Grader Guidelines AutoQC prompt if Alexander imports or authorizes it;
- compare future grader guidance against locked prompts, expected outputs, goldens, source files, and hierarchy rules;
- verify that final grader guidance rewards clinical reasoning rather than word matching;
- verify that final grader guidance does not expose hidden traps to the task prompt or create new clinical facts.

This architecture does not create AutoQC responses, AutoQC comments, or RL Studio materials.

Known source note: the local repository currently has many example grader guideline DOCX files under `reference/word-spec-examples/`, but no official Section 6 Grader Guidelines AutoQC prompt is saved under `reference/templates/` at the time this architecture was created.

## 15. Relationship To Final Packaging

This architecture is upstream of future grader guidance construction and final packaging.

Future packaging should preserve the one-to-one chain:

`TP-KM## -> EO-KM## -> Golden-KM## -> GG-KM##`

Packaging must not:

- create GG-KM07;
- detach FI-T07 from GG-KM01;
- mix grader guidance into task prompts;
- mix grader guidance into golden responses;
- package DOCX artifacts before that phase is authorized;
- create RL Studio submission materials before that phase is authorized.

## 16. Cross-Artifact Consistency Verification

Verification findings:

- GG count matches six locked prompts, six locked expected outputs, and six locked goldens.
- GG-KM01 through GG-KM06 map one-to-one to TP-KM01 through TP-KM06, EO-KM01 through EO-KM06, and Golden-KM01 through Golden-KM06.
- FI-T07 remains addendum support for GG-KM01 only.
- No GG-KM07 is introduced.
- The four locked workflows are preserved without adding or renaming workflows.
- File dependency mapping matches locked Golden Architecture v1 and Expected Output Architecture v1.
- FI-S files remain optional/background and are barred from carrying sole critical evidence.
- FI-W22 remains visible but incomplete.
- The five information-problem domains are preserved as grading-relevant reasoning domains without exposing internal trap labels in future user-facing materials.
- The three friction domains remain active and defensible.
- Authority hierarchy, master source-of-truth hierarchy, prednisone hierarchy, and physician-perspective rule are preserved.
- Golden-specific guardrails for Golden-KM01, Golden-KM03, Golden-KM05, and Golden-KM06 are preserved.
- No locked clinical, file, prompt, expected-output, or golden artifact was modified by this architecture.

## 17. Boundary Conditions

This architecture does not authorize:

- grader guidance construction;
- evaluator-facing final instructions;
- scoring rubrics;
- scoring thresholds;
- pass/fail criteria;
- point allocation;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- browser/RL Studio activity;
- changes to locked prompts;
- changes to locked expected outputs;
- changes to locked golden responses;
- changes to locked FI-W, FI-T, or FI-S files;
- new clinical facts, diagnoses, outcomes, labs, vitals, medications, services, readmissions, adverse events, or management decisions.

## Final Status

Grader Guidance Architecture v1

Status:

CANDIDATE REVIEW

Next Eligible Phase:

Grader Guidance Architecture Review
