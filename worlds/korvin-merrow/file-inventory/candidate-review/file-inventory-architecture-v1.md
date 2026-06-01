# File Inventory Architecture v1

Date created: 2026-06-01

Status: CANDIDATE REVIEW

Purpose: define the planned file ecosystem for the Korvin Merrow world before synthetic file creation, final Section 3 file rows, task prompts, expected outputs, goldens, grader guidance, DOCX population, AutoQC responses, or submission packaging.

This package answers: what kinds of documents must exist so the locked World Spec v1 can support the approved workflows, traps, frictions, source-of-truth reasoning, and temporal architecture?

This is not the final World File Plan. It creates no filenames, file IDs, file contents, note text, lab values, vital signs, medication lists, medication schedules, discharge summaries, task prompts, expected outputs, goldens, grader guidance, reference files, templates, DOCX artifacts, or RL Studio submission materials.

## Source Constraints

Use only locked/current materials:

- Locked World Spec v1.
- Locked World Spec Skeleton v1.
- Locked Daily Hospital Course Framework v1.
- Locked Task Architecture Package v1.
- Locked Provider Roster Package v1.
- Ratified Governance Package v1.
- Locked Key Milestones Calendar Skeleton v1.
- Locked Medication Expansion Package v1.
- Locked Comorbidity Expansion Package v1.
- Locked Surgical History Package v1.
- Current clinical logic.

## 1. File Ecosystem Overview

### World-Level Files

World-level files are chart materials that exist at or before the closed-world snapshot:

- World close: 05/23/2026 18:00.
- No world-level file may be dated after 05/23/2026 18:00.
- These files establish the hospitalization, outpatient provenance, consultant disagreements, source conflicts, medication history, functional evidence, and discharge-planning state available to every future task.

World-level architecture should include:

- ED/admission documentation.
- Inpatient progress documentation.
- Consultant documentation.
- Medication reconciliation / pharmacy history.
- Nursing observations.
- PT/OT assessments.
- Case Management / Social Work documentation.
- Discharge-planning artifacts through world close.
- Outpatient provenance files when needed for source-of-truth reasoning.
- Objective trend source types when needed later, without values in this package.

### Task-Level Files

Task-level files are materials introduced only for a specific future task context after world close. They may use the locked post-world anchors:

- Discharge anchor: 05/24/2026.
- +7 anchor: 05/31/2026.
- +30 anchor: 06/23/2026.

Task-level files must not retroactively change the world. They should contextualize the requester, post-world workflow, or task-specific deliverable surface.

### Supplementary / Noise Files

Supplementary files are optional low-stakes materials that create realistic chart texture without carrying required answers. They should be used sparingly.

Rules:

- Do not create noise for its own sake.
- Do not hide critical evidence only in noise.
- Do not introduce new diagnoses, new workflows, new frictions, or new traps through supplementary files.
- Every supplementary file must either support realism, source hierarchy, or task navigation without increasing reviewer confusion.

## 2. World-Level File Architecture

| Proposed file type | Purpose | Likely author / source | Approximate temporal anchor | Classification | Supported traps | Supported frictions | Supported workflows | Source-of-truth role | Essential? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ED triage / initial intake documentation | Establish presenting symptoms, family concern, near-fall/lightheadedness, possible urinary symptoms, altered baseline mental status, and initial acuity. | ED nursing / triage source | HD1 / 05/18/2026 | World-level | Trap #4; Trap #3 seeded | Family vs Primary Team seeded | Discharge Summary; Discharge Planning | Early presentation source; lower than attending documentation for final synthesis | Essential |
| ED provider assessment | Establish suspected urinary-source sepsis frame as clinically reasonable and document early stabilization logic. | Emergency Medicine provider | HD1 / 05/18/2026 | World-level | Trap #4 | Primary Team stabilization perspective | Discharge Summary; Interdisciplinary Care Plan | Early diagnostic/management source; not final explanation of whole stay | Essential |
| Admission history and physical | Convert ED presentation into inpatient working problem list, acute stabilization plan, baseline history, comorbidities, and initial medication concerns. | Hospitalist service / attending or supervised resident | HD1 / 05/18/2026 | World-level | Trap #1; Trap #2; Trap #4 | Family vs Primary Team latent; Cardiology vs Nephrology seeded | Discharge Summary; Discharge Medication Reconciliation | Attending documentation high in master hierarchy | Essential |
| Initial medication reconciliation source | Capture home medication claims, uncertainty, family/patient report, and early medication status. | Pharmacy / med-rec pharmacist with patient/family input | HD1 / 05/18/2026 | World-level | Trap #1; Trap #2 | Cardiology vs Nephrology; Endocrinology vs Primary Team | Discharge Medication Reconciliation; Discharge Summary | Verified medication reconciliation; high medication-history source | Essential |
| Pharmacy / refill-history source type | Provide external medication-history provenance for chronic HF, diabetes, prednisone, supplements, and supportive medications. | Pharmacy history / refill source | Pre-admission to HD1 review | World-level provenance | Trap #1; Trap #2 | Cardiology vs Nephrology; Endocrinology vs Primary Team | Discharge Medication Reconciliation | Pharmacy history; prednisone hierarchy level 3 | Essential |
| Outpatient rheumatology provenance | Carry the highest-authority PMR/prednisone taper recommendation and older steroid exposure context. | Dr. Soren Halvek / outpatient rheumatology | Pre-admission provenance, available by HD4 at latest | World-level provenance | Trap #1 | Endocrinology vs Primary Team | Discharge Medication Reconciliation; Interdisciplinary Care Plan; Discharge Summary | Highest prednisone-specific source | Essential |
| Primary care / outpatient baseline provenance | Carry baseline function, chronic disease context, outpatient medication continuity, and follow-up context. | Dr. Talia Quenor / primary care documentation | Pre-admission provenance, available during hospitalization | World-level provenance | Trap #2; Trap #3; Trap #5 | Family vs Primary Team | Discharge Planning; Discharge Summary | Primary care documentation in master hierarchy | Essential |
| HD1-HD6 hospitalist progress documentation | Show evolving primary-team reasoning, improvement trajectory, discharge-readiness interpretation, and potential copy-forward risk. | Dr. Elian Vossmere / Hospitalist Service | HD1-HD6 through 05/23/2026 18:00 | World-level | Trap #4; Trap #5; Trap #2 | All three frictions | Discharge Summary; Discharge Planning; Interdisciplinary Care Plan | Attending documentation, highest master hierarchy source for inpatient facts | Essential |
| Objective renal / infection / hemodynamic trend source type | Carry the fact of improvement versus persistence later without writing values in this package. | Lab/vital data source type | HD1-HD6 through world close | World-level | Trap #2; Trap #4; Trap #5 | Cardiology vs Nephrology; Family vs Primary Team | All four workflows | Objective trend evidence; must be interpreted with clinical context | Essential later, no values here |
| Medication administration / inpatient medication action source type | Later show medication holds, continuations, and reassessment opportunities without creating medication orders now. | MAR / inpatient medication source type | HD1-HD6 through world close | World-level | Trap #2; Trap #1 | Cardiology vs Nephrology; Endocrinology vs Primary Team | Discharge Medication Reconciliation; Interdisciplinary Care Plan | Medication action evidence; must be reconciled against orders/notes | Essential later, no medication list here |
| Nephrology consultation documentation | Represent renal recovery, AKI-on-CKD safety, hypotension/volume risk, and time-sensitive medication recommendations. | Dr. Iven Solthar / Nephrology | HD2-HD6, strongest HD4-HD6 | World-level | Trap #2; Trap #5 | Cardiology vs Nephrology | Discharge Medication Reconciliation; Interdisciplinary Care Plan | Consultant documentation; time-sensitive recommendation source | Essential |
| Cardiology consultation documentation | Represent HFrEF/CAD protective therapy, GDMT restart concerns, and readmission/decompensation risk. | Dr. Maris Caldrane / Cardiology | HD2-HD6, strongest HD4-HD6 | World-level | Trap #2; Trap #5 | Cardiology vs Nephrology | Discharge Medication Reconciliation; Interdisciplinary Care Plan | Consultant documentation; time-sensitive recommendation source | Essential |
| Endocrinology consultation documentation | Represent steroid/adrenal risk interpretation, prednisone exposure concerns, and safe taper/evaluation planning. | Dr. Nerea Veylorn / Endocrinology | HD2-HD6, strongest HD4-HD6 | World-level | Trap #1; Trap #4; Trap #5 | Endocrinology vs Primary Team | Interdisciplinary Care Plan; Discharge Medication Reconciliation; Discharge Summary | Consultant documentation; interprets but does not outrank rheumatology for prednisone history | Essential |
| Bedside nursing observation stream | Carry cognition, intake, ambulation tolerance, weakness, family concerns, and practical safety observations that may be easy to miss. | Bedside nursing team | HD1-HD6 | World-level | Trap #3; Trap #5 | Family vs Primary Team | Discharge Planning; Discharge Summary; Readmission-risk reasoning inside Discharge Planning | Functional/cognitive evidence source; not always prominent in physician summaries | Essential |
| Physical Therapy assessment | Establish mobility, transfer safety, endurance, assistance needs, and discharge functional recommendations. | Physical Therapy | HD3-HD6 | World-level | Trap #3; Trap #5 | Family vs Primary Team | Discharge Planning Documentation; Discharge Summary | PT/OT functional assessment in authority hierarchy | Essential |
| Occupational Therapy assessment | Establish ADL safety, medication-management ability, cognitive/functional home tasks, and support needs. | Occupational Therapy | HD3-HD6 | World-level | Trap #3; Trap #5 | Family vs Primary Team | Discharge Planning Documentation; Discharge Medication Reconciliation | PT/OT functional assessment in authority hierarchy | Essential |
| Family communication / care-conference documentation | Carry Mara Merrow's baseline knowledge, home safety concerns, and family disagreement with superficial discharge readiness. | Hospitalist, nursing, case management, or social work documentation of family communication | HD3-HD6 | World-level | Trap #3; Trap #5 | Family vs Primary Team | Discharge Planning Documentation; Discharge Summary | Family report in authority/source hierarchy | Essential |
| Case Management discharge-planning documentation | Establish discharge services, home support, equipment/placement considerations, and transition logistics. | Case Management | HD5-HD6 through world close | World-level | Trap #5; Trap #3 as secondary | Family vs Primary Team | Discharge Planning Documentation | Transition/disposition source; visible artifact may be incomplete | Essential |
| Social Work / caregiver-support documentation | Establish caregiver capacity, psychosocial barriers, and home-support concerns without making discharge one-sided. | Social Work | HD5-HD6 through world close | World-level | Trap #3; Trap #5 | Family vs Primary Team | Discharge Planning Documentation | Case/social evidence in authority hierarchy | Optional-to-essential depending final tasks |
| Discharge-facing planning artifact through world close | Provide a visible, reassuring but incomplete discharge-facing artifact available before the world snapshot. | Hospitalist / case management / interdisciplinary team | HD5-HD6, no later than 05/23/2026 18:00 | World-level | Trap #5 | Family vs Primary Team; Cardiology vs Nephrology; Endocrinology vs Primary Team | Discharge Planning; Discharge Summary; Discharge Medication Reconciliation | Visible source that must be reconciled, not trusted alone | Essential |
| Remote procedural history provenance source type | Carry remote PCI and sleep study only if final file plan needs provenance beyond admission history. | PCP/cardiology/sleep history source | Pre-admission provenance | World-level supplementary/provenance | Trap #2 support only | Cardiology vs Nephrology indirectly | Discharge Summary; Discharge Medication Reconciliation | Background provenance; should stay quiet | Optional |

Note: objective trend and medication action source types are file architecture categories only. They do not create lab values, vital signs, medication orders, medication lists, or schedules in this package.

## 3. Task-Level File Architecture

Task-level files may be needed later to frame specific tasks after the world closes. These are future task-context materials only; none is created here.

| Locked workflow | Potential task-level file type later | Potential anchor | Purpose | Boundary |
| --- | --- | --- | --- | --- |
| Discharge Medication Reconciliation | Discharge-medication-review request context | 05/24/2026 or later | Frame a clinician/pharmacist/hospitalist request to reconcile final medication safety from world files. | Do not create the final med list, med-rec output, medication schedule, or answer here. |
| Discharge Medication Reconciliation | Task-specific medication-safety handoff context | 05/24/2026 or later | Provide a narrow reason for reviewing holds/restarts/taper status without changing world facts. | Must not introduce new post-world clinical events unless authorized later. |
| Hospital Discharge Summary Generation | Discharge-summary drafting request context | 05/24/2026 | Ask for accurate hospital-course synthesis using world files. | Do not draft the discharge summary in this package. |
| Discharge Planning Documentation | Discharge-readiness / care-coordination request context | 05/24/2026 | Frame the administrative deliverable around safe transition planning. | Must preserve Family vs Primary Team balance. |
| Discharge Planning Documentation | Early post-discharge follow-up context | 05/31/2026 | Support +7 transition/reassessment reasoning without making a new diagnosis. | Must not turn follow-up into a hidden adrenal-insufficiency reveal. |
| Discharge Planning Documentation | Patient-safety / readmission-risk review context | 06/23/2026 | Support +30 retrospective safety review inside Discharge Planning Documentation workflow. | Must not create a standalone Patient Risk Stratification workflow. |
| Interdisciplinary Care Plan Development and Documentation | Consultant-synthesis request context | 05/24/2026 or later | Ask the care team to reconcile Cardiology, Nephrology, Endocrinology, hospitalist, PT/OT, family, pharmacy, and discharge planning evidence. | Do not create the care plan or expected output here. |

Task-level file principles:

- Each task remains independently solvable from the shared world files plus its own task context.
- Task-level files may anchor requester/persona and date, but must not backfill missing world evidence.
- TCM and readmission-risk reasoning remain inside Discharge Planning Documentation rather than standalone workflows.
- Any task-level material after 05/23/2026 18:00 must be classified as task-level or post-world, not world-level.

## 4. Trap-To-File Coverage Matrix

| Trap | Required file ecosystem support | Primary carrying file types | Secondary support | Coverage assessment |
| --- | --- | --- | --- | --- |
| Trap #1: Prednisone Source-of-Truth | Multiple inconsistent steroid-history sources with a resolvable hierarchy. | Rheumatology provenance, verified med rec, pharmacy/refill history, endocrinology consult, admission/progress documentation. | Family communication, patient recollection as documented by clinicians. | Strong. Must preserve rheumatology as highest prednisone-history source while Endocrinology interprets inpatient risk. |
| Trap #2: HF/AKI Medication Reconciliation | Time-sensitive holds/restarts and consultant recommendations that change in relevance as condition evolves. | Medication reconciliation, pharmacy history, MAR/action source type, nephrology consults, cardiology consults, hospitalist progress documentation, objective trend source type. | Discharge-facing planning artifact, discharge med-rec task context later. | Strong. Must avoid making latest note automatically correct. |
| Trap #3: Buried Functional/Cognitive Status | Important functional/cognitive evidence exists but is easy to miss because it lives outside prominent physician summaries. | Nursing observations, PT assessment, OT assessment, family communication, social work/case management documentation. | Hospitalist progress notes may understate or summarize incompletely. | Strong. This is the hidden-evidence problem. |
| Trap #4: Sepsis Anchoring After Partial Improvement | Early documents correctly emphasize suspected urinary-source sepsis, later documents show improvement but persistent noninfectious concerns. | ED provider assessment, admission H&P, hospitalist progress documentation, objective trend source type, consultant notes. | Nursing/PT/family evidence and steroid/medication sources. | Strong. Must preserve "sepsis was reasonable initially" while avoiding premature closure. |
| Trap #5: Discharge Source-Hierarchy | A visible discharge-facing artifact looks sufficient but is incomplete unless reconciled against the broader chart. | Discharge-facing planning artifact through world close, case management documentation, hospitalist discharge-planning note, consultant notes. | Nursing/PT/OT/family/pharmacy sources that complicate the artifact. | Strong. This is the visible-but-incomplete-source problem. |

Trap #3 vs Trap #5 protected distinction:

- Trap #3 asks whether the clinician finds important functional/cognitive evidence buried in less-prominent sources.
- Trap #5 asks whether the clinician over-trusts a visible discharge-facing source that appears sufficient but is incomplete.
- Later file construction must make these two traps live in different source patterns.

## 5. Friction-To-File Coverage Matrix

| Friction | File ecosystem support | Key source types | Coverage assessment |
| --- | --- | --- | --- |
| Cardiology vs Nephrology: medication restart timing | Cardiology and Nephrology each need defensible, time-sensitive recommendations, with primary-team synthesis and objective trend context. | Cardiology consults, Nephrology consults, hospitalist progress documentation, medication reconciliation, pharmacy history, medication action source type, objective trend source type. | Strong. Files must avoid making either service obviously correct across the whole stay. |
| Family vs Primary Team: discharge readiness | Family concern must be grounded in baseline knowledge and bedside/functional evidence, while Primary Team discharge reasoning remains clinically defensible. | Family communication, nursing observations, PT/OT assessments, case management, social work, hospitalist progress/discharge-planning artifact. | Strong. Files must preserve gray-zone discharge judgment. |
| Endocrinology vs Primary Team: steroid interpretation and risk | Endocrinology needs credible steroid-risk concerns, while Primary Team needs credible anti-overattribution reasoning after infection improvement. | Endocrinology consult, rheumatology provenance, medication reconciliation, pharmacy/refill history, hospitalist progress documentation, objective trend source type. | Strong. Files must prevent hidden-adrenal-insufficiency drift. |

## 6. Source-Of-Truth Coverage Matrix

### Authority Hierarchy

| Hierarchy element | Planned file support | Notes |
| --- | --- | --- |
| Attending Hospitalist | Admission/progress/discharge-planning documentation. | Highest inpatient synthesis source, but not automatic winner over consultants for recommendation disagreements. |
| Consulting Attending Specialists | Cardiology, Nephrology, Endocrinology consultation documentation. | Time-sensitive recommendations must be reconciled by timing and clinical status. |
| PT/OT Functional Assessments | PT and OT assessments. | High value for functional/discharge-readiness evidence. |
| Case Management / Social Work | Discharge planning, home-support, caregiver-capacity, services/equipment documentation. | Important for administrative deliverable and transition planning. |
| Family Reports | Family communication/care-conference documentation. | Lower factual authority than clinician documentation but high baseline-function relevance. |
| Patient Recollection | Admission history, med-rec, clinician-documented patient report. | Lowest hierarchy level but still clinically relevant. |

### Master Source-Of-Truth Hierarchy

| Hierarchy element | Planned file support | Notes |
| --- | --- | --- |
| Attending Documentation | Admission H&P, progress notes, discharge-planning assessment. | Governs many inpatient facts. |
| Verified Medication Reconciliation | Initial med-rec and later med-rec support. | Central for medication facts. |
| Pharmacy History | Refill/pharmacy history source type. | Supports medication and prednisone-source reconstruction. |
| Consultant Documentation | Cardiology, Nephrology, Endocrinology notes. | Important but must be interpreted by timestamp/context. |
| Primary Care Documentation | PCP/outpatient baseline provenance. | Supports longitudinal baseline, chronic disease, and follow-up context. |
| Family Report | Family communication documentation. | High baseline relevance; lower factual authority for medication details than verified sources. |
| Patient Recollection | Documented patient statements. | Useful but lowest source level for conflicting facts. |

### Prednisone-Specific Hierarchy

| Hierarchy element | Planned file support | Notes |
| --- | --- | --- |
| Rheumatology attending recommendation | Outpatient rheumatology provenance. | Highest prednisone-history source. |
| Verified medication reconciliation | Med-rec source. | High-value current medication source if verified. |
| Pharmacy / refill history | Pharmacy/refill source. | Confirms fills/exposure but may not prove actual use. |
| Family report | Family communication or med-rec collateral. | Useful collateral but imperfect dose/taper detail. |
| Patient recollection | Admission/med-rec patient statement. | Clinically relevant but unreliable under illness/confusion. |

## 7. Temporal Coverage Review

World-level temporal boundary:

- All world-level files must be dated on or before 05/23/2026 18:00.
- The final world-level state is HD6 at 18:00 during discharge planning.

Post-world anchors:

- 05/24/2026 is the discharge anchor.
- 05/31/2026 is the +7 anchor measured from discharge.
- 06/23/2026 is the +30 anchor measured from discharge.

Rules:

- Any file dated 05/24/2026, 05/31/2026, or 06/23/2026 must be task-level or post-world context unless Alexander explicitly reopens the world snapshot.
- No world-level discharge summary, post-discharge note, or follow-up note should be dated after 05/23/2026 18:00.
- Future task materials may use post-world anchors without changing world-level facts.
- Future Section 3 must distinguish world-level files from task-level files.

## 8. AutoQC v6.3 File Plan Readiness

The future Section 3 World File Plan must follow AutoQC v6.3 requirements, including the 8-column file-plan structure and Source/Tool separation.

Readiness implications:

- This package defines file categories and coverage only; it does not create final Section 3 rows.
- Future file inventory table construction must convert this architecture into the official file-plan columns.
- Every final file row must have a clear role, level, date/timestamp, provenance/source, creation tool/origin, and task/trap relevance as required by the official prompt.
- Every task must be traceable to the files required to solve it.
- Every major world fact used by tasks must be supported by at least one planned file.
- No final file may appear in Section 3 without a reason tied to scenario realism, task solvability, trap support, friction support, or source hierarchy.

AutoQC watch items:

- 2.42 file-plan table column mismatch / Source + Tool issue.
- 2.48 fact-to-file traceability.
- 2.65 source-of-truth hierarchy.
- 2.107 workflow-count discipline.
- 2.108 administrative deliverable.
- 2.113 Source/Tool and file origin convention.

## 9. File Count Strategy

Recommended target ranges for later final file inventory construction:

| File class | Target range | Rationale | Guardrail |
| --- | --- | --- | --- |
| Essential world-level files | 18-24 final files | A 6-day hospitalization with ED/admission, hospitalist, three consultants, pharmacy, nursing, PT/OT, family, case/social, outpatient provenance, and trend sources needs enough documents to support synthesis. | Do not create daily notes for every service unless needed. Avoid padding. |
| Essential task-level files | 6-10 final files | Six task concepts may need compact requester/context files after world close. | Task-level files should frame tasks, not supply missing world evidence. |
| Supplementary / noise files | 3-6 final files if needed | Limited noise can make the chart realistic and prevent one-click answers. | Noise must not carry sole critical evidence or create new arcs. |

Overall principle:

- Prefer the smallest file ecosystem that still supports all six tasks, all five traps, all three frictions, source hierarchy, and temporal reasoning.
- Increase file count only when a missing evidence channel would weaken task solvability or reviewer confidence.
- Keep the world readable enough that difficulty comes from synthesis, not random clutter.

## 10. Future Construction Order After Package Lock

Recommended sequence after File Inventory Architecture v1 locks:

1. File Inventory v1 table construction.
2. File Inventory review.
3. File Inventory lock.
4. Synthetic world-level file construction.
5. Task-level file construction.
6. Task specifications.
7. Task prompts.
8. Expected outputs.
9. Goldens.
10. Grader guidance.
11. AutoQC preparation.

This sequence is planning only. It does not authorize any downstream artifact without Alexander's explicit approval.

## File Inventory Architecture Consistency Review

### VERIFIED

Finding: architecture is consistent with locked World Spec v1.

Evidence: file categories map to the World Spec's patient profile, HD1-HD6 course, frictions, traps, source hierarchies, medication architecture, and task architecture.

Impact: future Section 3 can be built from this package without reopening the World Spec.

Action required: physician/reviewer review before lock.

### VERIFIED

Finding: all four locked workflows have file ecosystem support.

Evidence: Discharge Medication Reconciliation, Hospital Discharge Summary Generation, Discharge Planning Documentation, and Interdisciplinary Care Plan Development and Documentation each have world-level and possible task-level source types.

Impact: task solvability is structurally supported.

Action required: later task-specific files must not create new workflows.

### VERIFIED

Finding: all five traps have planned source substrates.

Evidence: Trap #1 maps to rheumatology/med-rec/pharmacy/family/patient sources; Trap #2 maps to med-rec/MAR/consultant/trend sources; Trap #3 maps to nursing/PT/OT/family sources; Trap #4 maps to ED/admission/progress/trend sources; Trap #5 maps to visible discharge-facing planning artifacts reconciled against broader evidence.

Impact: trap coverage is adequate without creating synthetic content.

Action required: preserve Trap #3 vs Trap #5 distinction during actual file construction.

### VERIFIED

Finding: all three frictions have planned document support.

Evidence: Cardiology vs Nephrology, Family vs Primary Team, and Endocrinology vs Primary Team each have distinct file-source channels and defensible evidence patterns.

Impact: file ecosystem supports human-to-human disagreements rather than collapsing them into documentation problems.

Action required: later file contents must keep both sides defensible.

### VERIFIED

Finding: source-of-truth hierarchy is covered.

Evidence: authority hierarchy, master source hierarchy, and prednisone-specific hierarchy each map to planned file supports.

Impact: later Section 3 traceability can distinguish factual conflicts from recommendation disagreements.

Action required: future file rows must preserve source/tool/provenance conventions.

### VERIFIED

Finding: temporal safety is preserved.

Evidence: world-level files are constrained to 05/23/2026 18:00 or earlier; discharge, +7, and +30 anchors are classified as task/post-world anchors.

Impact: reduces post-world world-file risk.

Action required: future file inventory table must enforce this boundary row by row.

### PLAUSIBLE

Finding: proposed file-count range is realistic.

Evidence: a 6-day inpatient world with multiple consultants, functional assessment, medication reconciliation, nursing observations, discharge planning, and outpatient provenance likely needs around 18-24 essential world-level files plus compact task-level context.

Impact: enough density for synthesis without intentional clutter.

Action required: refine exact count during File Inventory v1 table construction.

### PLAUSIBLE

Finding: objective trend source types are necessary later.

Evidence: AKI improvement, infection improvement, hemodynamic stability, and sepsis anchoring require trend evidence, but this package intentionally creates no values.

Impact: future file inventory must eventually decide how objective trends are represented.

Action required: do not add values until the authorized synthetic file or final file-plan construction step.

### DISPUTED

Finding: task-level files should supply missing world facts.

Evidence: task independence and closed-world logic require task-level files to frame the task, not patch missing evidence.

Impact: using task-level files to backfill world facts would weaken self-containment.

Action required: keep required world evidence in world-level files.

### NO ISSUE

Finding: this package creates no prohibited downstream artifacts.

Evidence: it contains no actual synthetic files, notes, labs, vitals, medication lists, discharge summaries, prompts, expected outputs, goldens, grader guidance, final Section 3 rows, DOCX artifacts, submission materials, reference files, templates, or RL Studio actions.

Impact: phase boundary remains intact.

Action required: stop before downstream construction.

## Final Status

File Inventory Architecture v1

Status: CANDIDATE REVIEW
