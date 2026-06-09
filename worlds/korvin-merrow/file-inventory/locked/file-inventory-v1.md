# File Inventory v1

Date created: 2026-06-01

Status: LOCKED

Purpose: convert the locked File Inventory Architecture v1 into the first AutoQC v6.3-compatible planned file inventory table for the Korvin Merrow world.

This is inventory planning only. It is not synthetic file creation, note writing, task construction, final Section 3 submission packaging, AutoQC response drafting, or RL Studio upload.

## Source Constraints

Use only locked and canonical materials:

- Locked World Spec v1.
- Locked World Spec Skeleton v1.
- Locked Daily Hospital Course Framework v1.
- Locked Task Architecture Package v1.
- Locked Provider Roster Package v1.
- Ratified Governance Package v1.
- Locked Medication Expansion Package v1.
- Locked Comorbidity Expansion Package v1.
- Locked Surgical History Package v1.
- Locked File Inventory Architecture v1.

Do not introduce new world facts, diagnoses, workflows, traps, frictions, medication schedules, clinical notes, lab values, vital signs, task prompts, expected outputs, goldens, grader guidance, synthetic files, DOCX artifacts, or submission materials.

## 1. File Inventory Table

AutoQC v6.3-compatible columns are preserved exactly as planning fields:

1. File ID.
2. File Type.
3. Level.
4. Approximate Date / Anchor.
5. Author / Source.
6. Tool / Origin.
7. Purpose.
8. Supported Workflow(s) / Trap(s) / Friction(s).

Source and Tool / Origin are intentionally separated.

### World-Level Files

All world-level files are dated at or before the world close: 05/23/2026 18:00.

| File ID | File Type | Level | Approximate Date / Anchor | Author / Source | Tool / Origin | Purpose | Supported Workflow(s) / Trap(s) / Friction(s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FI-W01 | ED triage / initial intake documentation | World-Level | 05/18/2026 / HD1 | ED triage nursing | Planned synthetic chart file in future phase | Establish presenting symptoms, family concern, near-fall/lightheadedness, possible urinary symptoms, altered baseline mental status, and initial acuity. | Hospital Discharge Summary Generation; Discharge Planning Documentation; Trap #4; Trap #3 seed; Family vs Primary Team seed |
| FI-W02 | ED provider assessment | World-Level | 05/18/2026 / HD1 | Emergency Medicine provider | Planned synthetic chart file in future phase | Establish the suspected urinary-source sepsis frame as clinically reasonable and document early stabilization logic. | Hospital Discharge Summary Generation; Interdisciplinary Care Plan Development and Documentation; Trap #4 |
| FI-W03 | Admission history and physical | World-Level | 05/18/2026 / HD1 | Dr. Elian Vossmere / Hospitalist Service | Planned synthetic chart file in future phase | Convert ED presentation into inpatient working problem list, baseline history, acute stabilization plan, comorbidity context, and initial medication concerns. | Hospital Discharge Summary Generation; Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Traps #1, #2, #4; Cardiology vs Nephrology seed |
| FI-W04 | Initial medication reconciliation note | World-Level | 05/18/2026 / HD1 | Pharmacy / medication reconciliation pharmacist with patient and family collateral | Planned synthetic chart file in future phase | Capture home medication claims, medication-history uncertainty, family/patient report, and early medication status. | Discharge Medication Reconciliation; Hospital Discharge Summary Generation; Traps #1, #2; Cardiology vs Nephrology; Endocrinology vs Primary Team |
| FI-W05 | Pharmacy / refill-history report | World-Level | Pre-admission provenance reviewed by 05/18/2026 / HD1 | Pharmacy history source | Planned synthetic provenance file in future phase | Provide external medication-history provenance for chronic HF, diabetes, prednisone, supplements, and supportive medications. | Discharge Medication Reconciliation; Traps #1, #2; Cardiology vs Nephrology; Endocrinology vs Primary Team |
| FI-W06 | Outpatient rheumatology prednisone provenance | World-Level | Pre-admission provenance available by HD4 | Dr. Soren Halvek / outpatient rheumatology | Planned synthetic outpatient provenance file in future phase | Carry the highest-authority PMR and prednisone taper recommendation plus older steroid-exposure context. | Discharge Medication Reconciliation; Hospital Discharge Summary Generation; Interdisciplinary Care Plan Development and Documentation; Trap #1; Endocrinology vs Primary Team |
| FI-W07 | Primary care outpatient baseline summary | World-Level | Pre-admission provenance available during hospitalization | Dr. Talia Quenor / primary care documentation | Planned synthetic outpatient provenance file in future phase | Carry baseline function, chronic disease context, outpatient medication continuity, and follow-up context. | Discharge Planning Documentation; Hospital Discharge Summary Generation; Traps #2, #3, #5; Family vs Primary Team |
| FI-W08 | HD1-HD2 hospitalist progress documentation | World-Level | 05/18/2026-05/19/2026 / HD1-HD2 | Dr. Elian Vossmere / Hospitalist Service | Planned synthetic chart file in future phase | Show early response, stabilization, evolving diagnostic frame, and early medication-safety reasoning. | Hospital Discharge Summary Generation; Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Traps #2, #4 |
| FI-W09 | HD3 hospitalist progress documentation | World-Level | 05/20/2026 / HD3 | Hospitalist Service | Planned synthetic chart file in future phase | Show the transition from acute stabilization toward functional/cognitive and discharge-readiness concerns. | Hospital Discharge Summary Generation; Discharge Planning Documentation; Traps #3, #4 |
| FI-W10 | HD4 hospitalist progress documentation | World-Level | 05/21/2026 / HD4 | Hospitalist Service | Planned synthetic chart file in future phase | Surface consultant tensions, steroid-history inconsistency, and primary-team synthesis burden. | Hospital Discharge Summary Generation; Interdisciplinary Care Plan Development and Documentation; Traps #1, #2, #4; all three frictions |
| FI-W11 | HD5-HD6 hospitalist discharge-planning progress documentation | World-Level | 05/22/2026-05/23/2026 before 18:00 / HD5-HD6 | Hospitalist Service | Planned synthetic chart file in future phase | Show medical improvement while preserving discharge uncertainty, medication-restart uncertainty, and unresolved family/consultant concerns. | Hospital Discharge Summary Generation; Discharge Planning Documentation; Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Trap #5; all three frictions |
| FI-W12 | Objective renal / infection / hemodynamic trend summary source | World-Level | HD1-HD6 through 05/23/2026 18:00 | Laboratory and vital-sign data source | Planned synthetic data source in future phase; values not created here | Provide trend evidence for improvement versus persistence without creating values in this artifact. | All four workflows; Traps #2, #4, #5; Cardiology vs Nephrology; Family vs Primary Team |
| FI-W13 | Medication administration / inpatient medication action source | World-Level | HD1-HD6 through 05/23/2026 18:00 | MAR / inpatient medication source | Planned synthetic data source in future phase; medication orders and schedules not created here | Later show medication holds, continuations, and reassessment opportunities without creating medication lists now. | Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Traps #1, #2; Cardiology vs Nephrology; Endocrinology vs Primary Team |
| FI-W14 | Nephrology consultation documentation | World-Level | HD2-HD6, strongest HD4-HD6 | Dr. Iven Solthar / Nephrology | Planned synthetic consultant file in future phase | Represent AKI-on-CKD recovery, hypotension/volume risk, renal medication safety, and time-sensitive medication recommendations. | Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Traps #2, #5; Cardiology vs Nephrology |
| FI-W15 | Cardiology consultation documentation | World-Level | HD2-HD6, strongest HD4-HD6 | Dr. Maris Caldrane / Cardiology | Planned synthetic consultant file in future phase | Represent HFrEF/CAD protective therapy, GDMT restart concerns, and decompensation/readmission risk. | Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Traps #2, #5; Cardiology vs Nephrology |
| FI-W16 | Endocrinology consultation documentation | World-Level | HD2-HD6, strongest HD4-HD6 | Dr. Nerea Veylorn / Endocrinology | Planned synthetic consultant file in future phase | Represent steroid/adrenal risk interpretation, prednisone exposure concerns, and safe taper/evaluation planning. | Interdisciplinary Care Plan Development and Documentation; Discharge Medication Reconciliation; Hospital Discharge Summary Generation; Traps #1, #4, #5; Endocrinology vs Primary Team |
| FI-W17 | Bedside nursing observation notes / flowsheet summary | World-Level | HD1-HD6 through 05/23/2026 18:00 | Bedside nursing team | Planned synthetic chart file in future phase | Carry cognition, intake, ambulation tolerance, weakness, family concerns, and practical safety observations that may be easy to miss. | Discharge Planning Documentation; Hospital Discharge Summary Generation; Traps #3, #5; Family vs Primary Team |
| FI-W18 | Physical Therapy assessment | World-Level | HD3-HD6 through 05/23/2026 18:00 | Physical Therapy service | Planned synthetic chart file in future phase | Establish mobility, transfer safety, endurance, assistance needs, and discharge functional recommendations. | Discharge Planning Documentation; Hospital Discharge Summary Generation; Traps #3, #5; Family vs Primary Team |
| FI-W19 | Occupational Therapy assessment | World-Level | HD3-HD6 through 05/23/2026 18:00 | Occupational Therapy service | Planned synthetic chart file in future phase | Establish ADL safety, medication-management ability, cognitive/functional home-task concerns, and support needs. | Discharge Planning Documentation; Discharge Medication Reconciliation; Traps #3, #5; Family vs Primary Team |
| FI-W20 | Family communication / care-conference documentation | World-Level | HD3-HD6 through 05/23/2026 18:00 | Hospitalist, nursing, case management, or social work documentation of Mara Merrow's report | Planned synthetic chart file in future phase | Carry family baseline knowledge, home safety concerns, medication-management concerns, and disagreement with superficial discharge readiness. | Discharge Planning Documentation; Hospital Discharge Summary Generation; Traps #3, #5; Family vs Primary Team; secondary/collateral support for Trap #1 and Endocrinology vs Primary Team through lower-authority family report without overriding rheumatology prednisone authority |
| FI-W21 | Case Management / Social Work discharge-planning note | World-Level | HD5-HD6 through 05/23/2026 18:00 | Case Management / Social Work | Planned synthetic chart file in future phase | Establish services, home support, caregiver capacity, equipment or placement considerations, and transition logistics. | Discharge Planning Documentation; Trap #5; Trap #3 secondary; Family vs Primary Team |
| FI-W22 | Discharge-facing plan snapshot before world close | World-Level | 05/23/2026 before 18:00 / HD6 | Hospitalist / interdisciplinary discharge-planning source | Planned synthetic chart file in future phase | Provide a visible, reassuring but incomplete discharge-facing artifact available before the world snapshot. | Discharge Planning Documentation; Hospital Discharge Summary Generation; Discharge Medication Reconciliation; Interdisciplinary Care Plan Development and Documentation; Trap #5; all three frictions |

### Task-Level Files

Task-level files are post-world context files only. They frame requests and anchors; they must not supply missing world evidence.

| File ID | File Type | Level | Approximate Date / Anchor | Author / Source | Tool / Origin | Purpose | Supported Workflow(s) / Trap(s) / Friction(s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FI-T01 | Discharge medication reconciliation request context | Task-Level | 05/24/2026 / discharge anchor | Hospitalist, pharmacist, or discharge clinician requester | Planned task-context file in future phase | Frame a medication-safety review using world files without creating the final medication list or answer. | Discharge Medication Reconciliation; Traps #1, #2, #5; Cardiology vs Nephrology; Endocrinology vs Primary Team |
| FI-T02 | Discharge summary drafting request context | Task-Level | 05/24/2026 / discharge anchor | Attending hospitalist / discharging service requester | Planned task-context file in future phase | Ask for accurate hospital-course synthesis without copying early diagnosis framing forward. | Hospital Discharge Summary Generation; Traps #2, #4, #5; secondary Endocrinology vs Primary Team and Family vs Primary Team support through consultant chronology, functional/family concerns, and copy-forward avoidance |
| FI-T03 | Discharge readiness / care coordination request context | Task-Level | 05/24/2026 / discharge anchor | Hospital team / case management requester | Planned task-context file in future phase | Frame transition planning and the administrative deliverable around safe discharge coordination. | Discharge Planning Documentation; Traps #3, #5; Family vs Primary Team |
| FI-T04 | Consultant synthesis / interdisciplinary care plan request context | Task-Level | 05/24/2026 / discharge anchor | Hospitalist-led interdisciplinary team requester | Planned task-context file in future phase | Frame synthesis of consultant recommendations and stakeholder priorities without creating the care plan output. | Interdisciplinary Care Plan Development and Documentation; Traps #1, #2, #5; Trap #4 secondary; all three frictions |
| FI-T05 | Early post-discharge follow-up assessment request context | Task-Level | 05/31/2026 / +7 from discharge | Primary care or transition team requester | Planned task-context file in future phase | Frame follow-up reassessment of recovery, medication tolerance, renal/cardiac safety, steroid plan coherence, function, cognition, and support. | Discharge Planning Documentation; Traps #1, #2, #4, #5; Trap #3 secondary; Family vs Primary Team; Endocrinology vs Primary Team support through steroid-plan coherence without replacing prednisone hierarchy |
| FI-T06 | Patient-safety / readmission-risk review request context | Task-Level | 06/23/2026 / +30 from discharge | Quality, safety, or transition team requester | Planned task-context file in future phase | Frame retrospective safety review inside Discharge Planning Documentation without creating a standalone risk-stratification workflow. | Discharge Planning Documentation; Traps #2, #3, #5; Family vs Primary Team; Cardiology vs Nephrology secondary support through medication-restart safety/readmission-risk review |
| FI-T07 | Medication safety handoff / task-context addendum | Task-Level | 05/24/2026 / discharge anchor | Pharmacy / discharge team requester | Planned task-context file in future phase | Narrow attention to holds, restarts, taper ambiguity, and medication-management safety without adding missing world evidence. | Discharge Medication Reconciliation; Traps #1, #2; Cardiology vs Nephrology; Endocrinology vs Primary Team |

### Supplementary Files

No critical evidence may live exclusively in supplementary files.

| File ID | File Type | Level | Approximate Date / Anchor | Author / Source | Tool / Origin | Purpose | Supported Workflow(s) / Trap(s) / Friction(s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FI-S01 | Remote PCI / coronary stent provenance summary | Supplementary | Pre-admission provenance | Cardiology or PCP history source | Planned supplementary provenance file in future phase | Support CAD/procedure background and chronic cardiovascular prevention without creating an acute procedure arc. | Hospital Discharge Summary Generation; Discharge Medication Reconciliation; Trap #2 indirect support |
| FI-S02 | Remote sleep-study / OSA provenance summary | Supplementary | Pre-admission provenance | PCP or sleep-history source | Planned supplementary provenance file in future phase | Support OSA background and chronic reserve context without explaining the acute presentation. | Hospital Discharge Summary Generation; Discharge Planning Documentation; background functional reserve support |
| FI-S03 | Home support / equipment logistics reference | Supplementary | HD5-HD6 through 05/23/2026 18:00 | Case Management / Social Work | Planned supplementary administrative file in future phase | Add transition-planning texture around equipment, services, and home support without carrying sole discharge-safety evidence. | Discharge Planning Documentation; Trap #5 secondary; Family vs Primary Team secondary |
| FI-S04 | Problem list / past history snapshot | Supplementary | HD1 or pre-admission import | Chart problem-list source | Planned supplementary chart file in future phase | Provide background comorbidity/procedure texture while keeping authoritative facts in stronger sources. | Hospital Discharge Summary Generation; Discharge Medication Reconciliation; source-hierarchy texture |

## 2. Workflow Coverage Matrix

| Locked workflow | Supporting file IDs | Coverage assessment |
| --- | --- | --- |
| Discharge Medication Reconciliation | FI-W03, FI-W04, FI-W05, FI-W06, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, FI-W22, FI-T01, FI-T07, FI-S01, FI-S04 | Strong. Medication history, pharmacy provenance, MAR/action evidence, consultant timing, steroid provenance, and discharge-facing context are all represented. |
| Hospital Discharge Summary Generation | FI-W01, FI-W02, FI-W03, FI-W07, FI-W08, FI-W09, FI-W10, FI-W11, FI-W12, FI-W16, FI-W17, FI-W18, FI-W20, FI-W22, FI-T02, FI-S01, FI-S02, FI-S04 | Strong. ED/admission frame, hospital-course evolution, consultant chronology, function, family concern, and discharge-source hierarchy are represented. |
| Discharge Planning Documentation | FI-W01, FI-W07, FI-W09, FI-W11, FI-W12, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22, FI-T03, FI-T05, FI-T06, FI-S02, FI-S03 | Strong. Functional status, family baseline, care coordination, home support, visible discharge planning, +7 follow-up, and +30 safety review are supported. |
| Interdisciplinary Care Plan Development and Documentation | FI-W02, FI-W03, FI-W08, FI-W10, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W20, FI-W22, FI-T04 | Strong. The table supports synthesis across hospitalist, Cardiology, Nephrology, Endocrinology, pharmacy, objective trends, family, and discharge planning. |

## 3. Trap Coverage Matrix

| Trap | Primary supporting file IDs | Secondary supporting file IDs | Coverage assessment |
| --- | --- | --- | --- |
| Trap #1: Prednisone source-of-truth | FI-W04, FI-W05, FI-W06, FI-W16, FI-W20 | FI-W03, FI-W10, FI-W13, FI-T01, FI-T04, FI-T05, FI-T07 | Strong. Rheumatology, med rec, pharmacy history, family/patient collateral, and Endocrinology interpretation remain separate source channels. |
| Trap #2: HF/AKI medication reconciliation and time-sensitive consultant logic | FI-W04, FI-W05, FI-W12, FI-W13, FI-W14, FI-W15, FI-W22 | FI-W03, FI-W08, FI-W10, FI-W11, FI-T01, FI-T04, FI-T06, FI-T07, FI-S01 | Strong. Early holds, trend context, consultant timing, pharmacy evidence, and discharge-facing review are represented without making latest note automatically correct. |
| Trap #3: Buried functional/cognitive status | FI-W17, FI-W18, FI-W19, FI-W20 | FI-W07, FI-W09, FI-W11, FI-W21, FI-T03, FI-T05, FI-T06 | Strong. Important evidence lives in nursing/PT/OT/family sources and is easy to miss if the reviewer only reads physician summaries. FI-T05 may frame +7 functional/cognitive reassessment as secondary task context but must not summarize all buried evidence. |
| Trap #4: Sepsis anchoring after partial improvement | FI-W01, FI-W02, FI-W03, FI-W08, FI-W09, FI-W10, FI-W12 | FI-W16, FI-W17, FI-W20, FI-T02, FI-T04, FI-T05 | Strong. Early infection framing is supported, and later mixed-physiology evidence prevents premature closure. FI-T04 may frame interdisciplinary synthesis against premature anchoring but must not make any specialty interpretation the hidden answer. |
| Trap #5: Discharge source-hierarchy | FI-W11, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22 | FI-W07, FI-W12, FI-W13, FI-T01, FI-T02, FI-T03, FI-T04, FI-T05, FI-T06, FI-S03 | Strong. A visible discharge-facing artifact exists but requires reconciliation against consultants, functional sources, family, medication evidence, and trends. |

Trap #3 is not Trap #5:

- Trap #3: buried functional/cognitive evidence. The issue is whether the clinician finds important evidence in less-prominent sources.
- Trap #5: reassuring but incomplete discharge/source-hierarchy artifact. The issue is whether the clinician over-trusts a visible discharge-facing source without reconciling it against the broader chart.

## 4. Friction Coverage Matrix

| Friction | Supporting file IDs | Coverage assessment |
| --- | --- | --- |
| Cardiology vs Nephrology: medication restart timing | FI-W04, FI-W05, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W22, FI-T01, FI-T04, FI-T06 secondary, FI-T07, FI-S01 | Strong. Both services have defensible sources, and the hospitalist/pharmacy/trend context prevents automatic deference to one side. FI-T06 may surface this friction secondarily when readmission/safety review includes medication-restart risk. |
| Family vs Primary Team: discharge readiness | FI-W01, FI-W07, FI-W09, FI-W11, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22, FI-T02 secondary, FI-T03, FI-T04 secondary, FI-T05, FI-T06, FI-S03 | Strong. Family baseline knowledge and functional evidence coexist with medically improving primary-team documentation and discharge-planning artifacts. FI-T02 and FI-T04 may carry this friction secondarily through discharge-summary chronology and interdisciplinary synthesis. |
| Endocrinology vs Primary Team: steroid interpretation and risk | FI-W04, FI-W05, FI-W06, FI-W10, FI-W11, FI-W13, FI-W16, FI-W20, FI-W22, FI-T01, FI-T02 secondary, FI-T04, FI-T05, FI-T07 | Strong. Steroid source ambiguity is represented as an information trap, while Endocrinology vs Primary Team remains a human disagreement about risk interpretation. FI-T02 may carry this friction secondarily through summary accuracy and consultant chronology. |

## 5. Source-Of-Truth Coverage Matrix

### Authority Hierarchy

| Authority element | Supporting file IDs | Coverage |
| --- | --- | --- |
| Attending Hospitalist | FI-W03, FI-W08, FI-W09, FI-W10, FI-W11, FI-W22 | Covered. Attending documentation carries inpatient synthesis but does not automatically resolve consultant disagreements. |
| Consulting Attending Specialists | FI-W14, FI-W15, FI-W16 | Covered. Consultant recommendations are time-sensitive and require context. |
| PT/OT Functional Assessments | FI-W18, FI-W19 | Covered. Functional evidence supports discharge-readiness reasoning. |
| Case Management / Social Work | FI-W21, FI-S03 | Covered. Transition logistics and caregiver capacity are represented. |
| Family Reports | FI-W01, FI-W04, FI-W20 | Covered. Mara Merrow's baseline knowledge is represented through documented reports. |
| Patient Recollection | FI-W03, FI-W04, FI-W20 | Covered. Patient recollection remains lower-authority but clinically relevant. |

### Master Source-Of-Truth Hierarchy

| Source hierarchy element | Supporting file IDs | Coverage |
| --- | --- | --- |
| Attending Documentation | FI-W03, FI-W08, FI-W09, FI-W10, FI-W11, FI-W22 | Covered. |
| Verified Medication Reconciliation | FI-W04, FI-T01, FI-T07 | Covered. |
| Pharmacy History | FI-W05 | Covered. |
| Consultant Documentation | FI-W14, FI-W15, FI-W16 | Covered. |
| Primary Care Documentation | FI-W07 | Covered. |
| Family Report | FI-W01, FI-W04, FI-W20 | Covered. |
| Patient Recollection | FI-W03, FI-W04 | Covered. |

### Prednisone-Specific Hierarchy

| Prednisone hierarchy element | Supporting file IDs | Coverage |
| --- | --- | --- |
| Rheumatology attending recommendation | FI-W06 | Covered. Highest prednisone-history source. |
| Verified medication reconciliation | FI-W04, FI-T01, FI-T07 | Covered. |
| Pharmacy / refill history | FI-W05 | Covered. |
| Family report | FI-W04, FI-W20 | Covered. |
| Patient recollection | FI-W03, FI-W04 | Covered. |

## 6. Temporal Validation

World-level file boundary:

- World close: 05/23/2026 18:00.
- All world-level rows FI-W01 through FI-W22 are anchored on or before 05/23/2026 18:00.
- No world-level row uses 05/24/2026, 05/31/2026, or 06/23/2026.

Task-level post-world anchors:

- FI-T01, FI-T02, FI-T03, FI-T04, and FI-T07 use 05/24/2026.
- FI-T05 uses 05/31/2026.
- FI-T06 uses 06/23/2026.
- All post-world rows are classified as Task-Level.

Supplementary rows:

- FI-S01, FI-S02, and FI-S04 are pre-admission or HD1 background/provenance support.
- FI-S03 is anchored no later than 05/23/2026 18:00.
- No supplementary file carries sole critical evidence.

Temporal safety assessment: locked.

## 7. File Count Review

| File class | Count | Target | Assessment |
| --- | ---: | ---: | --- |
| World-Level | 22 | 18-24 | Within target. Count is justified by ED/admission, hospitalist course, three consultants, pharmacy/med-rec, objective/MAR source types, nursing, PT/OT, family, case/social, outpatient provenance, and discharge-facing source hierarchy. |
| Task-Level | 7 | 6-10 | Within target. Seven compact task-context files support six task concepts while preserving a distinct medication handoff context. |
| Supplementary | 4 | 3-6 | Within target. Supplementary rows support procedural, OSA, home-support, and problem-list texture without carrying sole critical evidence. |
| Total | 33 | Not specified | Proportionate to a 6-day complex inpatient world while avoiding daily-note inflation. |

Count rationale:

- The world-level file count is intentionally at the middle-high end because all four workflows, five traps, three frictions, three source hierarchies, and six future task concepts need support.
- Daily notes are consolidated where possible to avoid redundant inflation.
- Task-level rows frame tasks only; they do not backfill evidence.
- Supplementary rows are capped and quiet.

## File Inventory Consistency Review

### VERIFIED

Finding: File Inventory v1 preserves World Spec fidelity.

Evidence: rows map directly to the locked World Spec's patient profile, HD1-HD6 course, provider roster, frictions, traps, source hierarchies, medication architecture, and task architecture.

Impact: no locked world fact is reopened.

Action required: locked; preserve as canonical planned file inventory unless Alexander explicitly reopens it.

### VERIFIED

Finding: architecture fidelity is preserved.

Evidence: the table converts locked File Inventory Architecture v1 into the requested 8-column file-plan structure while preserving Source vs Tool / Origin separation.

Impact: supports AutoQC v6.3 file-plan readiness.

Action required: preserve this column structure during later lock or DOCX preparation.

### VERIFIED

Finding: all four workflows are covered.

Evidence: Discharge Medication Reconciliation, Hospital Discharge Summary Generation, Discharge Planning Documentation, and Interdisciplinary Care Plan Development and Documentation each have world-level and task-level support.

Impact: future task solvability is structurally supported.

Action required: later task construction must not add new workflows without authorization.

### VERIFIED

Finding: all five traps have planned source substrates.

Evidence: trap matrix maps every trap to primary and secondary file IDs, with Trap #3 and Trap #5 explicitly distinguished.

Impact: synthesis difficulty comes from planned source patterns rather than random clutter.

Action required: preserve the Trap #3 / Trap #5 distinction during synthetic file construction.

### VERIFIED

Finding: all three frictions have two-sided file support.

Evidence: Cardiology vs Nephrology, Family vs Primary Team, and Endocrinology vs Primary Team each map to files supporting both clinically defensible positions.

Impact: frictions remain human/perspective conflicts rather than one-sided conclusions.

Action required: later file content must keep both sides plausible.

### VERIFIED

Finding: source-of-truth hierarchies are covered.

Evidence: authority hierarchy, master source hierarchy, and prednisone-specific hierarchy each map to planned file IDs.

Impact: future traceability and factual conflict resolution can be checked row by row.

Action required: do not collapse Source and Tool / Origin fields.

### VERIFIED

Finding: temporal safety is preserved.

Evidence: all world-level rows are anchored no later than 05/23/2026 18:00; all 05/24/2026, 05/31/2026, and 06/23/2026 rows are task-level.

Impact: protects closed-world boundary and post-world task anchor discipline.

Action required: none unless Alexander explicitly reopens File Inventory v1.

### PLAUSIBLE

Finding: 33 planned rows is readable for this world.

Evidence: 22 world-level, 7 task-level, and 4 supplementary rows stay within requested targets and cover a complex 6-day hospitalization without one-row-per-day/per-service inflation.

Impact: reviewer checks accepted the row density as lock-ready.

Action required: locked; future changes require explicit Alexander authorization.

### PLAUSIBLE

Finding: FI-W12 and FI-W13 are necessary as future data-source rows.

Evidence: medication timing, renal/infection/hemodynamic trends, and MAR action evidence are central to locked traps, but this phase cannot create values, orders, or schedules.

Impact: keeping these as source-type rows preserves future construction space without crossing boundaries.

Action required: future synthetic-file construction must decide exact representation only when authorized.

### DISPUTED

Finding: task-level files should provide missing clinical evidence.

Evidence: locked architecture and task-independence doctrine require post-world task context to frame requests, not backfill world evidence.

Impact: using task-level files to supply missing world facts would weaken self-containment.

Action required: keep required evidence in world-level files.

### NO ISSUE

Finding: this artifact creates no prohibited downstream content.

Evidence: it contains no synthetic file contents, note prose, discharge summaries, medication lists, medication schedules, lab values, vital signs, consultant recommendation text, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.

Impact: phase boundary remains intact.

Action required: stop before downstream construction.

## Final Status

File Inventory v1

Status: LOCKED
