# Expected Output Architecture v1

World: Korvin Merrow

Status: CANDIDATE REVIEW

Purpose: define the expected-output system for the six locked Korvin Merrow task prompts before any expected outputs, golden responses, grader guidance, AutoQC responses, DOCX artifacts, or submission artifacts are created.

This is architecture only. It defines expected-output count, IDs, deliverable surfaces, reasoning domains, source-synthesis requirements, hierarchy handling, and downstream boundaries. It does not write expected-output text, ideal answers, golden responses, grading criteria, rubrics, AutoQC responses, DOCX artifacts, RL Studio materials, or new clinical facts.

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
- Task Prompt Construction ratification.
- FI-W20 inventory-row reconciliation.
- FI-T inventory / task-layer architecture reconciliation.
- FI-S03 Trap #5 reconciliation.
- Standing physician-perspective task-layer rule.
- Standing Cross-Artifact Consistency Verification rule.

## 1. Expected Output Count And IDs

Canonical expected-output architecture count: 6.

Rationale:

- Locked Task Prompt Architecture v1 defines six standalone task prompts.
- TP-KM01 through TP-KM06 are locked.
- FI-T07 remains an addendum source for TP-KM01, not a seventh task prompt and not a seventh expected output.
- One expected-output architecture should map to each locked task prompt.

Expected-output IDs:

| Expected output ID | Locked prompt | Expected output family | Standalone expected output? |
| --- | --- | --- | --- |
| EO-KM01 | TP-KM01 | Discharge medication reconciliation / medication-safety recommendation | Yes |
| EO-KM02 | TP-KM02 | Hospital discharge summary | Yes |
| EO-KM03 | TP-KM03 | Discharge-readiness / care-coordination assessment | Yes |
| EO-KM04 | TP-KM04 | Consultant synthesis / interdisciplinary care plan | Yes |
| EO-KM05 | TP-KM05 | Early post-discharge follow-up assessment | Yes |
| EO-KM06 | TP-KM06 | Patient-safety / readmission-risk review | Yes |

## 2. Expected Output Inventory

| Expected output ID | Prompt ID | Locked workflow | Deliverable type | Output-shape architecture |
| --- | --- | --- | --- | --- |
| EO-KM01 | TP-KM01 | Discharge Medication Reconciliation | Physician medication reconciliation recommendation | Should be a clinically justified medication-safety recommendation that addresses continue/hold/stop/taper/restart logic at a reasoning level. It must not become a copied medication list, discharge prescription set, dosing schedule, or golden final regimen. |
| EO-KM02 | TP-KM02 | Hospital Discharge Summary Generation | Physician discharge summary | Should be a coherent discharge-summary-style clinical narrative organized around presentation, hospital course, active problems, consultant input, discharge planning concerns, and follow-up needs. It must not become a complete final submission-ready discharge document or a copied problem list. |
| EO-KM03 | TP-KM03 | Discharge Planning Documentation | Physician-facing discharge-readiness / care-coordination assessment | Should assess practical discharge coherence, functional and cognitive risk, home support, service needs, family concerns, and visible-plan limitations. It must not issue a final disposition order or service authorization. |
| EO-KM04 | TP-KM04 | Interdisciplinary Care Plan Development and Documentation | Hospitalist-led interdisciplinary care plan | Should synthesize consultant recommendations and stakeholder priorities into a physician-led care-plan frame. It must not automatically defer to a single consultant or resolve all uncertainty. |
| EO-KM05 | TP-KM05 | Discharge Planning Documentation | Early post-discharge follow-up assessment | Should identify follow-up priorities and monitoring/clarification needs based only on locked hospitalization evidence. It must not invent new +7 symptoms, vitals, labs, visits, outcomes, or recovery course. |
| EO-KM06 | TP-KM06 | Discharge Planning Documentation | Retrospective patient-safety / readmission-risk review | Should identify risk signals visible before discharge planning closed and explain why they mattered. It must not create a readmission, adverse event, RCA, blame assignment, or new post-discharge outcome. |

## 3. Required Clinical Reasoning Domains

| Expected output ID | Required clinical reasoning domains |
| --- | --- |
| EO-KM01 | Medication reconciliation reasoning; HF/CAD benefit vs AKI/CKD safety; potassium/BP/renal trend interpretation; prednisone-history uncertainty; inpatient-only vs outpatient medication distinction; functional/cognitive medication-management safety; monitoring and follow-up needs. |
| EO-KM02 | Presentation synthesis; mixed-physiology hospital-course reconstruction; daily evolution; sepsis framing without anchoring; medication holds/reassessment; consultant chronology; steroid-source ambiguity; functional/cognitive status; family concerns; unresolved discharge issues. |
| EO-KM03 | Discharge readiness; functional reserve; ADL/IADL needs; cognition and medication-management risk; home support/caregiver capacity; service and follow-up coherence; family baseline knowledge; difference between medical improvement and transition safety. |
| EO-KM04 | Consultant recommendation synthesis; hospitalist-synthesizes-not-defers governance; renal/cardiac medication sequencing tension; steroid-risk interpretation; functional and family evidence integration; trend/MAR interpretation without over-resolution; discharge-plan caveats. |
| EO-KM05 | Transition follow-up reasoning; trajectory reconstruction from hospitalization evidence; medication monitoring; renal/cardiac safety follow-up; steroid-plan clarification; functional/cognitive/support vulnerability; discharge-source hierarchy risk. |
| EO-KM06 | Safety signal recognition; readmission-risk reasoning from pre-discharge evidence; medication-restart uncertainty; buried functional/cognitive evidence; family/support integration; visible discharge-source over-trust risk; consultant-tension synthesis; hierarchy preservation. |

## 4. Source-Synthesis Domains

| Expected output ID | Required FI-T | Required FI-W dependencies | Optional FI-S dependencies | Source-synthesis requirements |
| --- | --- | --- | --- | --- |
| EO-KM01 | FI-T01, FI-T07 | FI-W03, FI-W04, FI-W05, FI-W06, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, FI-W22 | FI-S01, FI-S04 | Must synthesize med rec, pharmacy history, rheumatology correspondence, PCP medication context, MAR/actions, trends, consultants, functional/family evidence, and the incomplete discharge-facing snapshot. |
| EO-KM02 | FI-T02 | FI-W01, FI-W02, FI-W03, FI-W07, FI-W08, FI-W09, FI-W10, FI-W11, FI-W12, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W22 | FI-S01, FI-S02, FI-S04 | Must synthesize early presentation, admission framing, progress notes, trends, consultant chronology, nursing/therapy/family/care-management evidence, and discharge planning without copying forward stale framing. |
| EO-KM03 | FI-T03 | FI-W01, FI-W07, FI-W09, FI-W11, FI-W12, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S02, FI-S03 | Must synthesize baseline, functional/cognitive trajectory, nursing/therapy/family/care-management documentation, objective improvement, and visible discharge-plan limitations. |
| EO-KM04 | FI-T04 | FI-W02, FI-W03, FI-W08, FI-W10, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-S01, FI-S03, FI-S04 | Must synthesize hospitalist course, med provenance, objective trends, MAR/actions, consultant recommendations, functional/family evidence, care planning, and discharge-facing caveats. |
| EO-KM05 | FI-T05 | FI-W01 through FI-W22 | FI-S01, FI-S02, FI-S03, FI-S04 | Must reconstruct hospitalization and discharge-risk substrate from locked world files; optional supplementary files may add background texture but cannot supply sole critical evidence. |
| EO-KM06 | FI-T06 | FI-W01 through FI-W22 | FI-S02, FI-S03, FI-S04 | Must synthesize risk signals distributed across the full world; optional supplementary files may add low-stakes context but cannot become safety answers. |

## 5. Trap-Handling Domains

Future expected outputs must handle trap domains as clinical reasoning problems without exposing trap labels, trap numbers, or grading logic in the output text.

| Expected output ID | Required trap-handling domains | Forbidden trap exposure/collapse |
| --- | --- | --- |
| EO-KM01 | Prednisone source reconstruction; HF/AKI medication timing; FI-W22 incompleteness; medication-management safety. | Do not label traps. Do not declare an algorithmic restart rule. Do not treat latest consultant note or FI-W22 as automatically authoritative. |
| EO-KM02 | Sepsis anchoring avoidance; clinical evolution beyond early framing; functional/cognitive evidence; discharge-source limitations. | Do not label traps. Do not say infection was false, steroids explain everything, or discharge snapshot is the complete summary. |
| EO-KM03 | Buried functional/cognitive evidence; visible-but-incomplete discharge plan; family vs team evidence balance. | Do not label traps. Do not make the visible discharge plan or any single functional note the complete answer. |
| EO-KM04 | Prednisone source hierarchy; medication timing tension; consultant disagreement; discharge-source hierarchy. | Do not label traps. Do not make one consultant the hidden correct authority or collapse hospitalist synthesis into deference. |
| EO-KM05 | Mixed-physiology trajectory; medication/steroid follow-up uncertainty; discharge-source hierarchy risk. | Do not label traps. Do not add new +7 clinical facts or solve the hospitalization retrospectively with a single cause. |
| EO-KM06 | Buried functional/cognitive evidence; visible discharge-source over-trust; medication-restart uncertainty; source hierarchy preservation. | Do not label traps. Do not invent a readmission/outcome or turn risk review into RCA/golden answer text. |

## 6. Friction-Handling Domains

Future expected outputs must treat frictions as defensible human/perspective disagreements, not as documentation defects.

| Expected output ID | Required friction-handling domains | Prohibited friction handling |
| --- | --- | --- |
| EO-KM01 | Cardiology vs Nephrology; Endocrinology vs Primary Team; secondary Family vs Primary Team through medication-management safety. | Do not make one consultant careless or automatically correct. Do not turn family concerns into a medication answer. |
| EO-KM02 | Secondary Endocrinology vs Primary Team; secondary Family vs Primary Team; consultant chronology. | Do not erase consultant tensions or imply all disagreements were resolved by discharge. |
| EO-KM03 | Family vs Primary Team as primary; secondary medication and support tensions. | Do not make family concerns independently dispositive or make primary team discharge planning obviously unsafe. |
| EO-KM04 | Cardiology vs Nephrology; Endocrinology vs Primary Team; Family vs Primary Team. | Do not resolve by hierarchy alone. The output must synthesize timing, trends, status, and discharge safety. |
| EO-KM05 | Family vs Primary Team; Endocrinology vs Primary Team; secondary Cardiology vs Nephrology. | Do not create new follow-up evidence that resolves the frictions. |
| EO-KM06 | Family vs Primary Team; Cardiology vs Nephrology; secondary Endocrinology vs Primary Team. | Do not assign blame or create an adverse outcome. |

## 7. Hierarchy-Handling Domains

| Expected output ID | Required hierarchy handling |
| --- | --- |
| EO-KM01 | Must distinguish verified medication reconciliation, pharmacy/refill history, rheumatology prednisone authority, consultant recommendations, MAR/actions, family report, and patient recollection. |
| EO-KM02 | Must respect attending/hospitalist documentation while integrating consultants, objective trends, therapy/nursing/care-management sources, family report, and lower-authority recollection without copy-forward errors. |
| EO-KM03 | Must use authority hierarchy for disposition evidence and source-of-truth hierarchy for factual conflicts; must not treat FI-W22 as complete. |
| EO-KM04 | Must distinguish source-of-truth hierarchy from consultant-recommendation disagreement; hierarchy resolves factual conflicts but does not erase clinical disagreement. |
| EO-KM05 | Must preserve discharge-source hierarchy and prednisone hierarchy while using +7 only as a task anchor, not new evidence. |
| EO-KM06 | Must identify hierarchy-sensitive risk signals while preserving source boundaries; no post-world outcome may outrank locked world evidence. |

Global hierarchy rules:

- Authority hierarchy resolves role-based governance and decision ownership.
- Source-of-truth hierarchy resolves factual conflicts.
- Prednisone hierarchy remains: rheumatology attending recommendation, verified medication reconciliation, pharmacy/refill history, family report, patient recollection.
- Consultant disagreements require evidence synthesis, timing, trends, patient status, and discharge safety; they are not resolved automatically by authority rank.
- Physician-perspective rule governs final deliverable voice and responsibility.

## 8. Anti-Overanswer Protections

Future expected outputs must not:

- expose trap labels, trap numbers, grading logic, or hidden rubric language;
- present a complete golden answer;
- invent clinical facts not present in locked files;
- create new post-discharge symptoms, labs, vitals, visits, recovery, readmission, adverse event, or outcome;
- convert inpatient-only medication logic into outpatient regimen by default;
- create final medication schedules or discharge prescription sets unless a later phase explicitly authorizes that surface;
- declare final safe/unsafe disposition as a standalone answer when the task asks for assessment;
- resolve consultant disagreement by choosing a winner without synthesis;
- make FI-W22, FI-T files, or FI-S files answer files;
- collapse mixed physiology into a single dominant diagnosis;
- convert safety review into RCA, blame assignment, or adverse-event narrative.

## 9. Anti-Underanswer Protections

Future expected outputs must not:

- ignore required FI-T context;
- ignore required FI-W source dependencies;
- rely only on FI-W22 or a task context file;
- omit consultant tensions when relevant;
- omit family/support/functional evidence when relevant;
- omit medication timing, renal/cardiac safety, steroid ambiguity, or monitoring needs when relevant;
- omit hierarchy reasoning where source conflict is present;
- provide generic recommendations without chart-grounded synthesis;
- provide only a bullet list when a narrative clinical synthesis is required by the deliverable type;
- treat medical improvement as equivalent to operational discharge safety.

## 10. Relationship To Future Golden Responses

This architecture is upstream of golden responses.

It may later inform golden-response construction by defining:

- expected output count and IDs;
- deliverable type per prompt;
- required reasoning domains;
- required source-synthesis domains;
- required trap/friction/hierarchy handling;
- prohibited overanswer and underanswer patterns.

It must not:

- write ideal answer text;
- decide exact phrasing;
- define scoring thresholds;
- assign points;
- disclose trap labels in future user-facing output;
- replace physician-authored golden construction.

## 11. Relationship To Future Grader Guidance

This architecture is upstream of grader guidance.

It may later inform grader-guidance construction by identifying:

- what clinical reasoning must be present;
- what source synthesis must be expected;
- what overanswer and underanswer risks must be watched;
- where hierarchy and physician-perspective rules matter.

It must not:

- create a rubric;
- create pass/fail criteria;
- create scoring bands;
- create AutoQC responses;
- create grading text for RL Studio;
- expose hidden-answer logic to task prompts or expected outputs.

## 12. Cross-Artifact Consistency Verification

Verification findings:

- Expected output count matches the six locked task prompts.
- EO-KM01 through EO-KM06 map one-to-one to TP-KM01 through TP-KM06.
- FI-T07 remains an addendum source for EO-KM01 and does not create EO-KM07.
- The four locked workflows are preserved without adding Patient Risk Stratification, RCA, coding, billing, or prior authorization workflows.
- Required FI-T and FI-W dependencies match locked Task Prompt Architecture v1.
- FI-S dependencies remain optional/supporting and do not carry sole critical evidence.
- The five trap domains are preserved without exposing trap labels in future expected-output text.
- The three frictions remain active and defensible.
- Master source-of-truth hierarchy, prednisone hierarchy, and physician-perspective rule are preserved.
- No locked clinical artifacts were modified.

## 13. Boundary Conditions

This architecture does not authorize:

- expected-output text;
- golden responses;
- grader guidance;
- rubrics;
- scoring logic;
- AutoQC responses;
- DOCX artifacts;
- RL Studio submission artifacts;
- browser/RL Studio activity;
- changes to locked prompts;
- changes to locked FI-W, FI-T, or FI-S files;
- new clinical facts, diagnoses, outcomes, labs, vitals, medications, or management decisions.

## Final Status

Expected Output Architecture v1

Status:

CANDIDATE REVIEW

Next Eligible Phase:

Expected Output Architecture Review
