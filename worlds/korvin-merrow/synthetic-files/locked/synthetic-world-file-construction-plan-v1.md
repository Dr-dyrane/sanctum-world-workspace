# Synthetic World-Level File Construction Plan v1

Date created: 2026-06-01

Status: LOCKED

Purpose: define the controlled construction strategy for the 22 locked world-level files in File Inventory v1 before any synthetic chart content is created.

This artifact is construction planning only. It does not create synthetic files, filenames, file contents, chart notes, discharge summaries, consultant recommendations, lab values, vital signs, medication lists, medication schedules, task prompts, expected outputs, golden responses, grader guidance, AutoQC responses, DOCX artifacts, or submission materials.

## Source Constraints

Use only locked and canonical materials:

- Locked World Spec v1.
- Locked File Inventory Architecture v1.
- Locked File Inventory v1.
- Ratified Governance Package v1.
- Locked Provider Roster Package v1.
- Locked Daily Hospital Course Framework v1.
- Locked Medication Expansion Package v1.
- Locked Comorbidity Expansion Package v1.
- Locked Surgical History Package v1.

File Inventory v1 is the authoritative source for all planned file rows. This plan must not introduce new world facts, diagnoses, workflows, traps, frictions, providers, medications, timelines, or task concepts.

## 1. Construction Philosophy

### Closed-World Discipline

The world-level file set must close at 05/23/2026 18:00. Files FI-W01 through FI-W22 may contain information available within the world by that timestamp only.

Post-world anchors remain outside world-level construction:

- 05/24/2026 discharge anchor.
- 05/31/2026 +7 post-discharge anchor.
- 06/23/2026 +30 post-discharge anchor.

Those anchors belong to future task-level context only. They must not leak into world-level synthetic files.

### Source-Of-Truth Preservation

The file set must preserve provenance instead of collapsing the chart into one omniscient summary. Factual conflicts should remain traceable to their source channel:

- attending documentation
- verified medication reconciliation
- pharmacy history
- consultant documentation
- primary care documentation
- family report
- patient recollection

Prednisone-specific conflicts must preserve the locked hierarchy:

1. Rheumatology attending recommendation.
2. Verified medication reconciliation.
3. Pharmacy / refill history.
4. Family report.
5. Patient recollection.

### Trap Preservation

Each trap must be constructed as a synthesis problem across multiple files. No single file should fully explain the correct answer, reconcile every source, or state the intended failure mode.

Evidence should be visible enough for a careful clinician to find it, but distributed enough that superficial reading can plausibly miss it.

### Friction Preservation

Frictions must remain human or perspective conflicts, not hidden data conflicts. Each side should have reasonable support:

- Cardiology vs Nephrology should remain a timing and risk-balancing problem.
- Family vs Primary Team should remain a discharge-readiness judgment problem.
- Endocrinology vs Primary Team should remain a steroid-risk interpretation problem.

No file should make one side obviously careless, ignorant, or automatically correct.

### No Answer-File Doctrine

No world-level file may function as an answer key. In particular:

- no final medication plan should solve the HF/AKI restart problem by itself
- no steroid document should prove a hidden single diagnosis
- no discharge artifact should fully resolve discharge safety
- no nursing, PT, OT, or family note should explicitly declare the final disposition answer
- no consultant note should automatically override the rest of the chart

### Temporal Integrity Requirements

Synthetic file construction must preserve clinical sequence:

- early sepsis framing is reasonable
- partial improvement occurs before discharge tension dominates
- consultant disagreements evolve over time
- functional concerns become clearer after stabilization
- discharge-facing artifacts remain pre-close and incomplete

Later construction must make timestamps and source chronology legible enough that a reviewer can audit temporal reasoning without needing external context.

## 2. Construction Batching Strategy

| Batch | File IDs | Source family | Construction role | Dependencies | Review checkpoint |
| --- | --- | --- | --- | --- | --- |
| Batch 1 | FI-W01 through FI-W07 | ED, admission, medication provenance, outpatient provenance | Build the presentation, baseline context, medication-history uncertainty, prednisone provenance, and outpatient baseline substrate. | Locked File Inventory v1, Governance Package, Provider Roster, baseline and timeline packages. | Confirm no post-world facts, no final diagnosis reveal, and no single-source prednisone answer. |
| Batch 2 | FI-W08 through FI-W13 | Hospitalist course, objective trends, MAR/action sources | Build the inpatient spine from early stabilization through discharge-planning tension and preserve objective/MAR source channels without creating answer lists. | Batch 1 should be drafted first so daily evolution can inherit baseline and provenance correctly. | Confirm HD1-HD6 sequence, source-vs-tool separation, and no values or schedules outside the authorized synthetic-file phase. |
| Batch 3 | FI-W14 through FI-W16 | Consultant documentation | Build specialty viewpoints for nephrology, cardiology, and endocrinology while preserving time-sensitive disagreement. | Batches 1 and 2 should exist so consultants respond to the same clinical spine. | Confirm each consultant is defensible, no consultant becomes an answer key, and steroid physiology stays important but not dominant. |
| Batch 4 | FI-W17 through FI-W21 | Nursing, PT, OT, family, case management / social work | Build functional, cognitive, family, and transition-safety substrate while preserving buried-evidence logic. | Batches 1 and 2 should exist so functional decline is interpreted against baseline and hospital course. | Confirm Trap #3 and Trap #5 remain distinct and family/team friction remains balanced. |
| Batch 5 | FI-W22 | Discharge-facing artifact | Build the visible reassuring but incomplete pre-close discharge-facing source. | Batches 1 through 4 should be available first; FI-W22 must synthesize incompletely rather than replace them. | Confirm FI-W22 is useful but not sufficient, remains before 05/23/2026 18:00, and does not solve all tasks. |

Batch 5 should be constructed last because FI-W22 is the highest risk for answer-file drift. It must be credible as a discharge-facing artifact while still forcing the clinician to reconcile broader evidence.

## 3. Trap Preservation Plan

| Trap | Where evidence should live | What must remain hidden or diffuse | What must remain visible | What must never become an answer file |
| --- | --- | --- | --- | --- |
| Trap #1: Prednisone source-of-truth | FI-W04, FI-W05, FI-W06, FI-W16, FI-W20, with support from FI-W03, FI-W10, and FI-W13 | The exact recent prednisone exposure and taper interpretation must require source hierarchy reconstruction. Patient/family recollection, pharmacy evidence, med rec, and rheumatology provenance must not all match too cleanly. | PMR history, chronic prednisone exposure, recent taper concern, Endocrinology attention, and rheumatology authority must be discoverable. | No note should say the steroid answer outright, prove adrenal suppression as the central reveal, or provide a final taper plan that removes synthesis. |
| Trap #2: HF/AKI medication reconciliation and time-sensitive consultant logic | FI-W04, FI-W05, FI-W12, FI-W13, FI-W14, FI-W15, FI-W22, with support from FI-W03, FI-W08, FI-W10, and FI-W11 | Restart timing and medication safety must depend on trends, holds/actions, consultant timing, and patient status rather than a single latest note. | Cardiorenal medication tension, renal recovery, HF/CAD protective concerns, and medication action history must be visible. | No file should contain a final complete medication plan that is obviously correct without reconciling nephrology, cardiology, MAR/action evidence, and trend context. |
| Trap #3: Buried functional/cognitive status | FI-W17, FI-W18, FI-W19, FI-W20, with support from FI-W07, FI-W09, FI-W11, and FI-W21 | Important functional and cognitive evidence should live in less prominent nursing, therapy, family, and care-coordination sources rather than only in physician summaries. | Weakness, intake, ambulation tolerance, cognition, ADL/medication-management concerns, and family deviation-from-baseline concerns must be findable. | No single functional note should explicitly declare the final discharge answer or convert the task into "find the unsafe discharge note." |
| Trap #4: Sepsis anchoring after partial improvement | FI-W01, FI-W02, FI-W03, FI-W08, FI-W09, FI-W10, FI-W12, with support from FI-W16, FI-W17, and FI-W20 | Noninfectious contributors should emerge gradually and remain multi-factorial. The early infection frame must not be retrospectively invalidated. | Early suspected urinary-source sepsis framing, initial treatment response, improving infection markers/clinical status, and persistent weakness/disposition concerns must be visible. | No file should say "sepsis was wrong," "adrenal insufficiency explains everything," or "infection fully explains the hospitalization." |
| Trap #5: Discharge source-hierarchy | FI-W11, FI-W14, FI-W15, FI-W16, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22, with support from FI-W07, FI-W12, and FI-W13 | The discharge-facing artifact should appear useful and reassuring but incomplete if trusted alone. Missing caveats should be found across consultants, functional sources, family, objective trends, and medication actions. | Medical improvement, discharge planning, follow-up availability, consultant concerns, family concern, functional reserve, and medication uncertainty must be visible. | FI-W22 must not contain all necessary caveats, final medication safety resolution, definitive disposition answer, or complete consultant synthesis. |

Trap #3 and Trap #5 must stay separate:

- Trap #3 is about whether important functional/cognitive evidence is found.
- Trap #5 is about whether a visible discharge-facing source is over-trusted.

## 4. Friction Preservation Plan

| Friction | Evidence distribution strategy | Balancing requirements | Anti-collapse guardrails |
| --- | --- | --- | --- |
| Cardiology vs Nephrology: medication restart timing | Distribute cardiorenal evidence across FI-W04, FI-W05, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W22, and later medication task context. | Cardiology must have real HF/CAD protective rationale; Nephrology must have real AKI, renal recovery, hemodynamic, and medication-safety rationale. | Do not make either consultant outdated, careless, or obviously wrong. Do not let "latest note wins" solve the disagreement. |
| Family vs Primary Team: discharge readiness | Distribute baseline and home-safety evidence across FI-W01, FI-W07, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, FI-W22, and hospitalist progress sources. | Family concern must be clinically meaningful; the Primary Team's medical-improvement reasoning must also be defensible. | Do not make discharge obviously unsafe or obviously safe. Preserve "medically improving but operationally dangerous." |
| Endocrinology vs Primary Team: steroid interpretation and risk | Distribute steroid evidence across FI-W04, FI-W05, FI-W06, FI-W10, FI-W13, FI-W16, FI-W20, and FI-W22. | Endocrinology must reasonably worry steroid contribution is underappreciated; the Primary Team must reasonably avoid over-attributing the entire course to steroid physiology. | Do not turn documentation into a friction participant. Do not make adrenal insufficiency the hidden central reveal. |

## 5. Source-Of-Truth Preservation Plan

### Authority Hierarchy

| Authority element | Planned files | Construction rule |
| --- | --- | --- |
| Attending Hospitalist | FI-W03, FI-W08, FI-W09, FI-W10, FI-W11, FI-W22 | Hospitalist documentation carries inpatient synthesis and decision ownership, but it must not erase consultant disagreement or lower-visibility functional evidence. |
| Consulting Attending Specialists | FI-W14, FI-W15, FI-W16 | Consultant files should carry specialty authority within their domains and remain time-sensitive. |
| PT/OT Functional Assessments | FI-W18, FI-W19 | Functional assessments should carry high relevance for discharge readiness without becoming disposition answer keys. |
| Case Management / Social Work | FI-W21, with support from FI-W20 and later supplementary logistics if authorized | Transition logistics should clarify feasibility and support needs without solving medical discharge reasoning alone. |
| Family Reports | FI-W01, FI-W04, FI-W20 | Family reports should carry baseline context and safety concerns while remaining below clinical documentation for factual conflict resolution. |
| Patient Recollection | FI-W03, FI-W04, FI-W20 | Patient recollection should remain clinically relevant but lower authority for factual conflicts. |

### Master Source-Of-Truth Hierarchy

| Source hierarchy element | Planned files | Construction rule |
| --- | --- | --- |
| Attending Documentation | FI-W03, FI-W08, FI-W09, FI-W10, FI-W11, FI-W22 | Use for inpatient facts and synthesis, but not as automatic resolution of all conflicts. |
| Verified Medication Reconciliation | FI-W04 | Use for initial home-medication claims and uncertainty; future task contexts may ask about it but cannot add missing evidence. |
| Pharmacy History | FI-W05 | Preserve as an independent medication provenance source. |
| Consultant Documentation | FI-W14, FI-W15, FI-W16 | Preserve specialty-specific recommendations and timing. |
| Primary Care Documentation | FI-W07 | Preserve outpatient baseline and continuity context. |
| Family Report | FI-W01, FI-W04, FI-W20 | Preserve baseline and home safety knowledge. |
| Patient Recollection | FI-W03, FI-W04 | Preserve as lower-authority but relevant history. |

### Prednisone Source-Of-Truth Hierarchy

| Prednisone hierarchy element | Planned files | Construction rule |
| --- | --- | --- |
| Rheumatology attending recommendation | FI-W06 | Highest authority for outpatient PMR/prednisone taper intent. |
| Verified medication reconciliation | FI-W04 | Important reconciliation source, but it must be tested against rheumatology and pharmacy history. |
| Pharmacy / refill history | FI-W05 | Independent fill/refill provenance; should not perfectly settle clinical intent by itself. |
| Family report | FI-W04, FI-W20 | Useful collateral, especially around home administration and patient behavior, but not top authority. |
| Patient recollection | FI-W03, FI-W04 | Lowest-authority source for taper details; should remain plausible but imperfect. |

Operational rule: hierarchy resolves factual or documentation conflicts. It does not automatically resolve clinical recommendation disagreements. Consultant disagreements must be reconciled through evidence synthesis, timing, trends, patient status, and discharge safety.

## 6. Temporal Preservation Plan

World-level construction must remain inside the closed chart boundary.

| File group | Allowed temporal boundary | Prohibited content |
| --- | --- | --- |
| FI-W01 through FI-W03 | 05/18/2026 / HD1 | Post-HD1 hindsight that would make early reasoning look obviously right or wrong. |
| FI-W04 through FI-W07 | Pre-admission provenance available during hospitalization, no later than world close | Post-discharge medication outcomes, later outpatient clarification, or retrospective correction. |
| FI-W08 through FI-W13 | HD1-HD6 through 05/23/2026 18:00 | Discharge-day outcomes, +7 or +30 findings, final reconciliation outputs, or post-world clinical course. |
| FI-W14 through FI-W16 | HD2-HD6 through 05/23/2026 18:00 | Later consultant updates after world close or definitive post-discharge conclusions. |
| FI-W17 through FI-W21 | HD1-HD6 through 05/23/2026 18:00 | Post-discharge functional outcome, readmission information, or task-specific framing. |
| FI-W22 | 05/23/2026 before 18:00 / HD6 | Final discharge outcome, completed discharge medication list, post-world follow-up, or any answer key. |

Temporal validation requirements:

- All FI-W rows must remain at or before 05/23/2026 18:00.
- 05/24/2026, 05/31/2026, and 06/23/2026 remain task-level anchors only.
- No post-world information may be introduced into world-level files.
- No synthetic file should reveal what later task requesters ask or what later reviewers should conclude.

## 7. Construction Readiness Review

### Batch Readiness

| Batch | Readiness | Dependency order | Review checkpoint |
| --- | --- | --- | --- |
| Batch 1: FI-W01-FI-W07 | PLAUSIBLE | First. These files establish presentation, baseline, medication provenance, and outpatient context. | Check baseline fidelity, prednisone source hierarchy, no hidden single-diagnosis reveal, no invented external sources. |
| Batch 2: FI-W08-FI-W13 | PLAUSIBLE | Second. These files inherit Batch 1 context and build the hospital-course spine. | Check HD1-HD6 sequence, objective/MAR source separation, no final medication list, no unauthorized values if not yet approved. |
| Batch 3: FI-W14-FI-W16 | PLAUSIBLE | Third, after the clinical spine exists. | Check consultant disagreement balance, time sensitivity, authority hierarchy, and steroid non-dominance. |
| Batch 4: FI-W17-FI-W21 | PLAUSIBLE | Third or fourth after baseline and hospital-course spine exist. | Check functional evidence distribution, family/team balance, and Trap #3 vs Trap #5 distinction. |
| Batch 5: FI-W22 | PLAUSIBLE | Last. This file depends on all prior world-level sources. | Check no answer-file drift, no complete source hierarchy resolution, no post-world leakage. |

### Dependency Order

Recommended construction order:

1. Batch 1 foundation and provenance.
2. Batch 2 hospital-course spine and source-type data channels.
3. Batch 3 consultants.
4. Batch 4 functional, family, and transition-safety substrate.
5. Batch 5 discharge-facing pre-close artifact.

Batch 3 and Batch 4 may be reviewed in parallel after Batch 2 exists, but FI-W22 should remain last.

### Review Checkpoints

For each future construction batch:

1. Confirm every file maps to its locked FI-W row.
2. Confirm no file introduces new diagnoses, workflows, traps, frictions, providers, or post-world facts.
3. Confirm source and tool/origin remain conceptually separated.
4. Confirm no single file functions as an answer key.
5. Confirm trap evidence is distributed but discoverable.
6. Confirm both sides of each active friction remain defensible.
7. Confirm all world-level content remains at or before 05/23/2026 18:00.
8. Confirm future file content does not pre-write task prompts, expected outputs, goldens, or grader guidance.

### VERIFIED

Finding: File Inventory v1 provides a complete authorized row set for this plan.

Evidence: FI-W01 through FI-W22 are locked as world-level planned files and are the only files in scope for this construction plan.

Impact: planning can proceed without inventing new files.

Action required: preserve FI-W IDs and row purposes exactly unless Alexander explicitly reopens File Inventory v1.

### VERIFIED

Finding: the plan preserves the world close boundary.

Evidence: every batch is constrained to information available no later than 05/23/2026 18:00, and post-world anchors are explicitly prohibited from world-level files.

Impact: protects temporal gate compliance and closed-world reasoning.

Action required: future synthetic-file construction must timestamp or anchor each file accordingly.

### VERIFIED

Finding: Trap #3 and Trap #5 remain distinct.

Evidence: Trap #3 is assigned to buried functional/cognitive sources; Trap #5 is assigned to visible but incomplete discharge/source-hierarchy artifacts.

Impact: prevents the two discharge-safety traps from collapsing into the same mechanism.

Action required: review FI-W17 through FI-W22 carefully during future construction.

### VERIFIED

Finding: source-of-truth hierarchy is preserved as provenance rather than a single summary.

Evidence: attending, pharmacy, consultant, PCP, family, patient, and prednisone-specific source roles map to separate FI-W files.

Impact: supports factual conflict resolution and traceability.

Action required: do not collapse these into one synthetic summary file.

### PLAUSIBLE

Finding: five construction batches are a workable sequence.

Evidence: the batches follow clinical dependency order from presentation and provenance to hospital course, consultants, functional/disposition sources, and final discharge-facing artifact.

Impact: should reduce drift during later construction.

Action required: ratification review should confirm whether Batch 3 and Batch 4 may be built in parallel or should be strictly sequential.

### PLAUSIBLE

Finding: FI-W22 is the highest-risk file for answer-file drift.

Evidence: it is a visible discharge-facing artifact supporting all workflows, Trap #5, and all three frictions.

Impact: constructing it last is likely safer.

Action required: future FI-W22 review should explicitly test for over-completeness.

### DISPUTED

Finding: this phase should create filenames or synthetic file contents.

Evidence: the authorized scope is construction planning only and explicitly prohibits filenames, chart notes, discharge summaries, labs, vitals, medication lists, consultant recommendations, and downstream task artifacts.

Impact: creating files now would cross the phase boundary.

Action required: create no synthetic file contents in this phase.

### NO ISSUE

Finding: this artifact does not reopen locked clinical architecture.

Evidence: it uses existing FI-W rows, locked traps, locked frictions, locked source hierarchies, and locked temporal boundaries without adding new clinical facts.

Impact: no locked package is changed by this plan.

Action required: stop at candidate review.

## Final Status

Synthetic World-Level File Construction Plan v1

Status: LOCKED
