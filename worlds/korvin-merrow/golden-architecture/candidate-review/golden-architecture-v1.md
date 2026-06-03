# Golden Architecture v1

World: Korvin Merrow

Status: CANDIDATE REVIEW

Purpose: define the architecture for future golden responses to the six locked Korvin Merrow task prompts and expected outputs.

This is architecture only. It defines golden count, IDs, mapping, deliverable types, reasoning requirements, evidence requirements, synthesis requirements, hierarchy requirements, quality standards, traceability expectations, and prohibition classes. It does not create golden response text, grader guidance, scoring rubrics, AutoQC responses, DOCX artifacts, submission artifacts, final medication decisions, final discharge decisions, final risk conclusions, new clinical facts, or new workflows.

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
- Locked Supplementary File Architecture v1.
- Locked Task Prompt Architecture v1.
- Locked task prompts TP-KM01 through TP-KM06.
- Locked Expected Output Architecture v1.
- Locked expected outputs EO-KM01 through EO-KM06.
- Task Prompt Construction ratification.
- Expected Output Construction ratification.
- FI-W20 inventory-row reconciliation.
- FI-T inventory / task-layer architecture reconciliation.
- FI-S03 discharge-source reconciliation.
- Standing physician-perspective task-layer rule.
- Standing Cross-Artifact Consistency Verification rule.

## 1. Golden Count And IDs

Canonical golden architecture count: 6.

Rationale:

- Locked Task Prompt Architecture v1 defines six standalone prompts.
- Locked Task Prompt Construction created TP-KM01 through TP-KM06.
- Locked Expected Output Architecture v1 defines six expected-output slots.
- Locked Expected Output Construction created EO-KM01 through EO-KM06.
- FI-T07 remains medication-safety addendum support for TP-KM01, EO-KM01, and future Golden-KM01 only. It does not create a seventh golden.

Golden IDs:

| Golden ID | Locked prompt | Locked expected output | Future golden family | Standalone golden? |
| --- | --- | --- | --- | --- |
| Golden-KM01 | TP-KM01 | EO-KM01 | Discharge medication reconciliation / medication-safety response | Yes |
| Golden-KM02 | TP-KM02 | EO-KM02 | Hospital discharge summary response | Yes |
| Golden-KM03 | TP-KM03 | EO-KM03 | Discharge-readiness / care-coordination response | Yes |
| Golden-KM04 | TP-KM04 | EO-KM04 | Consultant synthesis / interdisciplinary care-plan response | Yes |
| Golden-KM05 | TP-KM05 | EO-KM05 | Early post-discharge follow-up assessment response | Yes |
| Golden-KM06 | TP-KM06 | EO-KM06 | Patient-safety / readmission-risk review response | Yes |

## 2. Core Design Principle

A future golden should represent a strong physician answer, not the only possible physician answer.

Golden construction must protect:

- multiple defensible reasoning paths;
- uncertainty acknowledgement;
- evidence reconciliation;
- hierarchy application;
- consultant and stakeholder friction preservation;
- clinically realistic synthesis rather than hidden-answer retrieval.

Goldens should demonstrate what a senior physician would notice, reconcile, and communicate. They should not imply that every defensible clinician must choose identical wording, sequencing, or emphasis when the locked chart supports more than one reasonable path.

## 3. Golden Deliverable Inventory

| Golden ID | Deliverable type | Required stance | Boundary protection |
| --- | --- | --- | --- |
| Golden-KM01 | Senior-physician medication reconciliation / medication-safety response | Risk-balanced medication recommendation with explicit sequencing, monitoring, source reconciliation, and medication-management safety. | Must prevent medication algorithm drift, preserve Cardiology vs Nephrology tension, preserve prednisone hierarchy, and avoid a final prescription set unless later authorized. |
| Golden-KM02 | Senior-physician discharge summary response | Clinically coherent hospitalization narrative organized by evolution, consultant chronology, mixed physiology, function, family concerns, and unresolved transition needs. | Must avoid copy-forward summary logic, single-cause closure, new diagnoses, or final post-discharge outcomes. |
| Golden-KM03 | Senior-physician discharge-readiness / care-coordination assessment | Practical transition-safety synthesis that balances medical improvement against functional, cognitive, support, service, medication, and family evidence. | Must prevent discharge-authorization drift and avoid final disposition orders or service approvals. |
| Golden-KM04 | Senior-physician interdisciplinary care-plan response | Hospitalist-led synthesis of consultant recommendations, objective trends, medication actions, steroid-source hierarchy, family evidence, and discharge logistics. | Must avoid consultant-winner logic, final medication list creation, final prednisone taper creation, and final disposition authorization. |
| Golden-KM05 | Senior-physician early follow-up assessment response | Follow-up priority assessment based only on the locked hospitalization and discharge-risk substrate. | Must prevent invented follow-up facts, including symptoms, vitals, labs, visits, recovery course, readmission, or outcomes. |
| Golden-KM06 | Senior-physician patient-safety / readmission-risk review response | Retrospective risk-signal synthesis grounded in pre-discharge evidence and planning vulnerabilities. | Must prevent RCA drift, blame assignment, adverse-event creation, readmission creation, recovery outcome creation, and standalone patient-risk-stratification workflow drift. |

## 4. Prompt And Expected-Output Mapping

| Golden ID | Prompt ID | Expected output ID | Locked workflow | Primary task context |
| --- | --- | --- | --- | --- |
| Golden-KM01 | TP-KM01 | EO-KM01 | Discharge Medication Reconciliation | FI-T01 plus FI-T07 addendum |
| Golden-KM02 | TP-KM02 | EO-KM02 | Hospital Discharge Summary Generation | FI-T02 |
| Golden-KM03 | TP-KM03 | EO-KM03 | Discharge Planning Documentation | FI-T03 |
| Golden-KM04 | TP-KM04 | EO-KM04 | Interdisciplinary Care Plan Development and Documentation | FI-T04 |
| Golden-KM05 | TP-KM05 | EO-KM05 | Discharge Planning Documentation | FI-T05 |
| Golden-KM06 | TP-KM06 | EO-KM06 | Discharge Planning Documentation | FI-T06 |

Workflow preservation:

- Discharge Medication Reconciliation maps to Golden-KM01 only.
- Hospital Discharge Summary Generation maps to Golden-KM02 only.
- Discharge Planning Documentation maps to Golden-KM03, Golden-KM05, and Golden-KM06 through distinct anchors and deliverable surfaces.
- Interdisciplinary Care Plan Development and Documentation maps to Golden-KM04 only.
- No Patient Risk Stratification, RCA, coding, billing, prior authorization, or new workflow is introduced.

## 5. File Dependency Mapping

Required means a future golden must demonstrate synthesis from those sources when the evidence is relevant to the task. Optional/supporting means the source may add background texture but may not carry sole critical evidence.

| Golden ID | Required FI-T | Required FI-W files | Optional/supporting FI-S files |
| --- | --- | --- | --- |
| Golden-KM01 | FI-T01, FI-T07 | FI-W03, FI-W04, FI-W05, FI-W06, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, FI-W22 | FI-S01, FI-S04 |
| Golden-KM02 | FI-T02 | FI-W01, FI-W02, FI-W03, FI-W07, FI-W08, FI-W09, FI-W10, FI-W11, FI-W12, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W22 | FI-S01, FI-S02, FI-S04 |
| Golden-KM03 | FI-T03 | FI-W01, FI-W07, FI-W09, FI-W11, FI-W12, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S02, FI-S03 |
| Golden-KM04 | FI-T04 | FI-W02, FI-W03, FI-W08, FI-W10, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S01, FI-S03, FI-S04 as background only if packaging requires |
| Golden-KM05 | FI-T05 | FI-W01 through FI-W22 | FI-S01, FI-S02, FI-S03, FI-S04 as background only |
| Golden-KM06 | FI-T06 | FI-W01 through FI-W22 | FI-S02, FI-S03, FI-S04 as background only |

File dependency safeguards:

- FI-T files frame the task and must not replace chart review.
- FI-T07 is an addendum for Golden-KM01 only.
- FI-W22 must remain visible but incomplete.
- FI-S files must never carry sole critical evidence.
- No golden may depend on future artifacts not already locked.

## 6. Required Reasoning Domains

| Golden ID | Required reasoning domains |
| --- | --- |
| Golden-KM01 | Medication provenance; inpatient actions vs discharge decisions; HFrEF/CAD benefit vs AKI/CKD, potassium, BP, intake, and volume safety; prednisone-source reconstruction; inpatient-only medication separation; functional/cognitive medication-management safety; monitoring and accountable education needs. |
| Golden-KM02 | Presentation synthesis; clinically reasonable early infection framing; mixed-physiology hospital evolution; daily course reconstruction; consultant chronology; medication reassessment; steroid-source ambiguity; functional/cognitive evidence; family concerns; unresolved discharge caveats. |
| Golden-KM03 | Medical improvement vs operational discharge safety; baseline comparison; ADL/IADL and mobility needs; cognition and medication-management risk; caregiver capacity; services/equipment/follow-up coherence; family baseline evidence; visible-plan limitations. |
| Golden-KM04 | Hospitalist-led consultant synthesis; renal/cardiac medication sequencing; objective trend and MAR interpretation; steroid-risk reasoning; family and functional evidence integration; discharge logistics; uncertainty preservation. |
| Golden-KM05 | Follow-up priority setting from locked evidence; medication monitoring; renal/cardiac reassessment needs; prednisone/steroid-plan clarification; functional/cognitive/support vulnerability; discharge-source hierarchy risk; escalation considerations without new findings. |
| Golden-KM06 | Visible pre-discharge risk signals; medication-restart uncertainty; distributed functional/cognitive evidence; family/support integration; consultant-synthesis needs; source-hierarchy risks; visible-plan over-trust risk; safety considerations without outcomes or blame. |

## 7. Evidence And Synthesis Requirements

Future goldens must:

- cite or clearly attribute reasoning to chart evidence classes without turning the response into a file-by-file inventory;
- reconcile objective trend data with clinical context rather than treating a single improvement marker as dispositive;
- distinguish MAR/inpatient actions from outpatient discharge plans;
- distinguish intended prednisone taper from actual recent adherence;
- integrate functional, cognitive, family, nursing, therapy, and care-management evidence when discharge safety or medication-management safety is relevant;
- use FI-W22 as orientation only and reconcile it against higher-detail sources;
- identify open monitoring, education, follow-up, or clarification needs when the locked chart leaves uncertainty;
- preserve mixed physiology and avoid single-cause explanations when the chart supports more than one contributing process.

Traceability expectations:

- Each golden should be traceable to its locked prompt, locked expected output, primary FI-T file, required FI-W evidence classes, relevant optional FI-S background, governing workflow, hierarchy rules, and relevant friction domains.
- Traceability may be documented through concise evidence references or source-aware reasoning.
- Traceability must not expose internal trap labels, trap numbers, scoring logic, or rubric language in the future golden response.

## 8. Uncertainty Requirements

Future goldens must explicitly preserve uncertainty where locked sources preserve uncertainty.

Required uncertainty patterns:

- Do not prove adrenal insufficiency or deny steroid contribution when the chart supports risk but not certainty.
- Do not state that infection was false or that infection explains everything.
- Do not treat improved creatinine, potassium, BP, intake, alertness, or fever burden as independently sufficient for final discharge safety.
- Do not treat consultant disagreement as settled by authority rank alone.
- Do not treat family concern as independently dispositive or irrelevant.
- Do not invent post-discharge outcomes to resolve follow-up or safety-review tasks.
- Do not imply that a future golden is the only defensible physician response.

## 9. Hierarchy Requirements

Future goldens must apply the locked hierarchies as reasoning tools, not as shortcuts.

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

Application rules:

- Authority hierarchy governs role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership.
- Source-of-truth hierarchy governs factual conflict resolution.
- Prednisone-specific hierarchy governs steroid taper and prednisone provenance conflicts.
- Consultant disagreement requires synthesis of evidence, timing, trends, patient status, and discharge safety. It must not be resolved automatically by hierarchy rank.
- Physician-perspective rule governs deliverable voice: future goldens should read as physician-authored, physician-reviewed, physician-supervised, or physician-communicated responses even when evidence comes from pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources.

## 10. Friction-Handling Requirements

Future goldens must preserve frictions as reasonable perspective conflicts.

| Friction domain | Golden IDs where active | Required handling |
| --- | --- | --- |
| Cardiology vs Nephrology medication timing | Golden-KM01, Golden-KM04; secondary in Golden-KM05 and Golden-KM06 | Preserve both HFrEF/CAD protection and renal/potassium/BP/intake/monitoring safety. Require sequencing and monitoring logic instead of consultant-winner logic. |
| Endocrinology vs Primary Team steroid interpretation | Golden-KM01, Golden-KM04, Golden-KM05; secondary in Golden-KM02 and Golden-KM06 | Preserve endocrine concern without proving steroid causality; preserve primary-team improvement framing without dismissing steroid risk. Apply prednisone hierarchy. |
| Family vs Primary Team discharge readiness | Golden-KM03, Golden-KM05, Golden-KM06; secondary in Golden-KM02 and Golden-KM04 | Treat family concern as baseline-informed evidence while preserving that primary-team discharge planning is clinically plausible given improvement. |

## 11. Trap-Handling Requirements

Future goldens must handle the five locked information-problem domains without exposing internal trap labels or numbers.

| Information-problem domain | Golden IDs where active | Required handling | Forbidden collapse |
| --- | --- | --- | --- |
| Prednisone source reconstruction | Golden-KM01, Golden-KM04; secondary in Golden-KM05 | Reconstruct intended taper and recent-use uncertainty through rheumatology, medication reconciliation, pharmacy, family, and patient sources. | Do not make Endocrinology, family report, patient recollection, FI-W22, FI-T05, or FI-T07 the prednisone authority. |
| HF/AKI medication timing and consultant logic | Golden-KM01, Golden-KM04; secondary in Golden-KM02, Golden-KM05, and Golden-KM06 | Reconcile home therapies, inpatient actions, trends, consultant recommendations, and monitoring needs. | Do not create a restart algorithm, treat latest consultant note as automatically correct, or collapse Cardiology vs Nephrology. |
| Buried functional/cognitive evidence | Golden-KM03, Golden-KM06; secondary in Golden-KM02 and Golden-KM05 | Integrate nursing, PT, OT, family, CM/SW, and baseline sources. | Do not summarize all functional evidence from physician notes or FI-W22 alone. |
| Sepsis anchoring after partial improvement | Golden-KM02, Golden-KM05; secondary in Golden-KM04 | Preserve reasonable early infection framing while integrating later mixed physiology. | Do not say sepsis was false, infection explains everything, or steroids explain everything. |
| Discharge-source hierarchy and visible-plan over-trust | Golden-KM03, Golden-KM04, Golden-KM06; secondary in Golden-KM01, Golden-KM02, and Golden-KM05 | Treat FI-W22 as useful but incomplete and reconcile it against broader evidence. | Do not let FI-W22, any FI-T file, or any supplementary file become the answer file. |

## 12. Golden Quality Standards

A future golden should:

- answer the requested deliverable directly and in the voice of a strong physician;
- show chart-grounded reasoning without becoming a citation dump;
- separate what is known, uncertain, plausible, and not established;
- reconcile conflicting evidence rather than ignoring inconvenient sources;
- preserve defensible disagreement among consultants, family, and primary team;
- identify practical next steps, monitoring, education, or clarification needs when the task calls for them;
- remain scoped to the locked task and expected output;
- avoid hidden-rubric language and internal implementation labels;
- avoid excessive certainty when the chart is intentionally uncertain;
- avoid generic textbook advice that could be written without the Korvin Merrow chart.

## 13. Golden Prohibition Classes

Future golden construction must not create:

- golden responses during this architecture phase;
- grader guidance;
- scoring rubrics;
- scoring thresholds;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- new workflows;
- new FI-W, FI-T, or FI-S files;
- new diagnoses, medications, labs, vitals, symptoms, visits, readmissions, adverse events, recovery outcomes, or discharge outcomes;
- final discharge prescriptions or complete final medication schedules unless a later authorized golden-construction phase explicitly defines that surface;
- final discharge authorization or service authorization;
- RCA, blame assignment, adverse-event narrative, or outcome determination;
- trap labels, trap numbers, scoring logic, or hidden grading text in future user-facing golden responses.

## 14. Special Watch Items

Golden-KM01:

- prevent medication algorithm drift;
- preserve Cardiology vs Nephrology tension;
- preserve prednisone hierarchy;
- distinguish inpatient-only medication actions from outpatient regimen decisions;
- preserve functional/cognitive medication-management safety.

Golden-KM03:

- prevent discharge-authorization drift;
- preserve assessment framing rather than final disposition order or service approval;
- keep family concerns meaningful but not independently dispositive.

Golden-KM05:

- prevent invented follow-up facts;
- use the +7 date as a task anchor only;
- base all priorities on locked hospitalization and discharge-risk evidence.

Golden-KM06:

- prevent RCA drift;
- prevent invented outcomes;
- preserve retrospective risk-signal review inside Discharge Planning Documentation.

## 15. Cross-Artifact Consistency Verification

Verification findings:

- Golden count matches the six locked task prompts and six locked expected outputs.
- Golden-KM01 through Golden-KM06 map one-to-one to TP-KM01 through TP-KM06 and EO-KM01 through EO-KM06.
- FI-T07 remains addendum support for Golden-KM01 only; no Golden-KM07 is created.
- The four locked workflows are preserved without adding or renaming workflows.
- File dependency mapping matches locked Task Prompt Architecture v1 and Expected Output Architecture v1.
- FI-W01 through FI-W22, FI-T01 through FI-T07, and FI-S01 through FI-S04 are represented according to locked inventory roles.
- FI-S files remain optional/supporting and do not carry sole critical evidence.
- The five locked information-problem domains are preserved without exposing internal labels or numbers in future golden response expectations.
- The three friction domains remain active and defensible.
- Authority hierarchy, master source-of-truth hierarchy, prednisone hierarchy, and physician-perspective rule are preserved.
- Special watch items for Golden-KM01, Golden-KM03, Golden-KM05, and Golden-KM06 are incorporated without broadening task responsibilities.
- No locked clinical, prompt, expected-output, inventory, or synthetic-file artifact was modified by this architecture.

## 16. Boundary Conditions

This architecture does not authorize:

- golden response construction;
- grader guidance;
- rubrics;
- scoring thresholds;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- browser/RL Studio activity;
- changes to locked expected outputs;
- changes to locked prompts;
- changes to locked FI-W, FI-T, or FI-S files;
- new clinical facts or management decisions;
- Golden Architecture lock or ratification.

## Final Status

Golden Architecture v1

Status:

CANDIDATE REVIEW

Next Eligible Phase:

Golden Architecture Review
