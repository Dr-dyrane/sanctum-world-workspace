# Task-Level Context File Architecture v1

World: Korvin Merrow

Date created: 2026-06-02

Status: CANDIDATE REVIEW

Purpose: define the structure, responsibilities, constraints, and governance of future task-level context files before any FI-T files are created.

This is an architecture and boundary-setting artifact only. It does not create FI-T files, FI-S files, task prompts, expected outputs, goldens, grader guidance, AutoQC responses, DOCX artifacts, RL Studio submission artifacts, final task outputs, or new clinical facts.

## Source Basis

Authoritative sources:

- Locked World Spec v1.
- Locked File Inventory Architecture v1.
- Locked File Inventory v1.
- Locked Synthetic World-Level File Construction Plan v1.
- Ratified Governance Package v1.
- Locked Task Architecture Package v1.
- Locked FI-W01 through FI-W22.
- Batch 1 through Batch 5 ratifications.
- World-Level Synthetic File Layer Closure Audit.
- Current clinical logic and physician-perspective task-layer guidance.

## 1. Scope

Task-level context files are compact, post-world requester/context artifacts that frame a future task after the world-level chart has closed.

They may:

- establish the requester, task date, workflow frame, and deliverable surface;
- point the agent toward the kind of work being requested;
- clarify what world files the agent may need to synthesize;
- preserve task independence by giving each future task its own context;
- use locked post-world anchors when appropriate: 05/24/2026 discharge anchor, 05/31/2026 +7 anchor, and 06/23/2026 +30 anchor.

They are not:

- world-level chart files;
- final task prompts;
- expected outputs;
- goldens;
- grader guidance;
- final clinical answers;
- final discharge summaries;
- final medication lists;
- final disposition decisions;
- substitute source-of-truth files;
- vehicles for backfilling missing world evidence.

Relationship to world-level files:

- FI-W01 through FI-W22 remain the clinical world substrate.
- Task-level context files must require use of world files rather than replacing them.
- Task-level context files may not revise, override, or complete locked world facts.
- Any evidence needed to solve a task must remain traceable to the world files or to explicitly authorized task-context framing.

Relationship to future prompts:

- FI-T files may later support prompts, but they are not prompts.
- Prompt wording, scoring expectations, and output requirements remain blocked until separate authorization.

Relationship to future expected outputs:

- FI-T files may indicate the kind of deliverable requested, but they must not draft, outline, grade, or answer that deliverable.
- Expected outputs, goldens, and grader guidance remain separate future phases.

## 2. FI-T Inventory Architecture

The following entries define future FI-T architecture only. They do not construct the files.

| File ID | Intended role | Intended information scope | Relationship to world files | Permitted content classes | Prohibited content classes |
| --- | --- | --- | --- | --- | --- |
| FI-T01 | Discharge medication reconciliation request context. | 05/24/2026 medication-safety review request from hospitalist, pharmacist, or discharge clinician. Frames reconciliation of continuation, hold, restart, stop, taper, and follow-up logic. | Must force synthesis across FI-W03, FI-W04, FI-W05, FI-W06, FI-W11, FI-W12, FI-W13, FI-W14, FI-W15, FI-W16, FI-W19, and FI-W22. | Requester identity, task date, medication-safety concern, list of issues to review at a high level, reminder that world files govern evidence. | Final medication list, restart algorithm, prednisone answer, discharge prescription set, medication schedule, consultant winner, new post-world clinical event. |
| FI-T02 | Discharge summary drafting request context. | 05/24/2026 attending/discharging-service request to synthesize the hospitalization accurately. | Must require review of ED/admission documents, hospitalist course, objective trends, consultant chronology, functional evidence, and FI-W22 without trusting any one source alone. | Request to draft/synthesize, intended audience, summary scope, caution against copy-forward anchoring. | Actual discharge summary, final diagnoses beyond locked facts, hidden diagnosis reveal, post-discharge outcome, complete course narrative answer. |
| FI-T03 | Discharge readiness / care coordination request context. | 05/24/2026 discharge-planning or care-coordination framing around safe transition planning. | Must require synthesis of FI-W01, FI-W07, FI-W09, FI-W11, FI-W12, FI-W17, FI-W18, FI-W19, FI-W20, FI-W21, and FI-W22. | Requester role, care-coordination frame, home-support questions, functional-readiness focus, documentation surface. | Final disposition order, final services authorization, definitive safe/unsafe discharge answer, replacement for PT/OT/family/CM evidence. |
| FI-T04 | Consultant synthesis / interdisciplinary care plan request context. | 05/24/2026 hospitalist-led interdisciplinary request to reconcile consultant and stakeholder priorities. | Must require reconciliation of hospitalist, Cardiology, Nephrology, Endocrinology, pharmacy/MAR, objective trends, family, PT/OT, and discharge planning evidence. | Requester frame, care-plan scope, instruction to synthesize competing recommendations, list of specialties/stakeholders to consider. | Completed care plan, final medication authority, final steroid taper, final disposition decision, consultant override, new evidence. |
| FI-T05 | Early post-discharge follow-up assessment request context. | 05/31/2026 +7 transition/follow-up framing for reassessment of recovery, medication tolerance, steroid plan coherence, function, cognition, and support. | Must preserve world necessity by requiring reconstruction from FI-W01 through FI-W22 rather than adding a solved follow-up story. | Follow-up requester, date anchor, reason for review, domains needing reassessment, connection back to discharge and world evidence. | New diagnosis reveal, proof of adrenal insufficiency, completed readmission outcome, new labs/vitals unless separately authorized, final explanation for hospitalization. |
| FI-T06 | Patient-safety / readmission-risk review request context. | 06/23/2026 +30 retrospective safety-review frame inside Discharge Planning Documentation workflow. | Must require review of world-level discharge-readiness, functional, medication, consultant, family, and source-hierarchy evidence. | Safety-review requester, retrospective frame, domains to assess, reason for readmission-risk review. | Standalone Patient Risk Stratification workflow, RCA/golden answer, actual adverse event unless authorized, blame assignment, new post-world clinical course. |
| FI-T07 | Medication safety handoff / task-context addendum. | 05/24/2026 focused medication-safety handoff narrowing attention to holds, restarts, taper ambiguity, and medication-management safety. | Must support FI-T01-style medication reasoning without adding missing medication facts; should point back to med rec, pharmacy, MAR, consultants, trends, and FI-W22. | Handoff requester, focused medication-safety questions, cross-reference frame, uncertainty reminders. | Final medication reconciliation, final home regimen, insulin-lispro outpatient addition, prednisone-source override, consultant winner, medication answer key. |

Global FI-T construction guardrails:

- Do not make any FI-T file necessary because the world files are incomplete.
- Do not hide a critical world fact only in an FI-T file.
- Do not make an FI-T file the answer source for its task.
- Do not use FI-T files to resolve final disposition, final medication restart timing, final prednisone taper, final consultant disagreement, or final family/team conflict.
- Do not create FI-T files until Task-Level Context File Construction is separately authorized.

## 3. Trap Coverage Matrix

| Trap | Primary future FI-T coverage | Secondary future FI-T coverage | Forbidden trap collapse patterns |
| --- | --- | --- | --- |
| Trap #1: Prednisone source-of-truth | FI-T01, FI-T04, FI-T07 | FI-T05 | Do not let Endocrinology, family report, patient recollection, FI-W22, or any FI-T file replace outpatient rheumatology as the highest prednisone-history authority. Do not prove adrenal insufficiency as the hidden answer. |
| Trap #2: HF/AKI medication reconciliation and time-sensitive consultant logic | FI-T01, FI-T04, FI-T07 | FI-T02, FI-T05, FI-T06 | Do not make latest consultant note automatically correct. Do not create a final restart algorithm inside task context. Do not make Cardiology or Nephrology careless. |
| Trap #3: Buried functional/cognitive status | FI-T03, FI-T06 | FI-T05 | Do not summarize all functional evidence inside task context. Do not collapse buried evidence into a visible one-file answer. Preserve the need to read nursing, PT, OT, family, and care coordination sources. |
| Trap #4: Sepsis anchoring after partial improvement | FI-T02, FI-T05 | FI-T04 | Do not say sepsis was wrong, infection fully explains the admission, or steroids explain everything. Preserve mixed physiology and the reasonableness of early sepsis framing. |
| Trap #5: Discharge source-hierarchy | FI-T03, FI-T04, FI-T06 | FI-T01, FI-T02, FI-T05 | Do not let FI-W22 or an FI-T file become the visible source that replaces chart review. Do not merge Trap #5 with Trap #3. |

Trap architecture principles:

- FI-T files frame the trap exposure; they do not solve traps.
- Each future task should vary trap centrality so no single trap dominates all work.
- Trap #3 and Trap #5 must remain separate: buried functional/cognitive evidence versus over-trust of visible discharge-facing sources.

## 4. Friction Coverage Matrix

| Friction | Where it should appear | Where it must not be resolved |
| --- | --- | --- |
| Cardiology vs Nephrology: medication restart timing | FI-T01, FI-T04, FI-T07, with secondary relevance in FI-T06 when reviewing safety/readmission risk. | No FI-T file may declare Cardiology or Nephrology finally correct. Resolution must require trend evidence, MAR/action evidence, timing, clinical status, and hospitalist synthesis. |
| Endocrinology vs Primary Team: steroid interpretation and risk | FI-T01, FI-T04, FI-T05, FI-T07, with secondary relevance in FI-T02. | No FI-T file may prove adrenal insufficiency, finalize prednisone adherence, or make Endocrinology the hidden diagnosis authority. |
| Family vs Primary Team: discharge readiness | FI-T03, FI-T05, FI-T06, with secondary relevance in FI-T02 and FI-T04. | No FI-T file may make family concerns independently dispositive or make the Primary Team obviously careless. |

Friction principles:

- Frictions remain people/perspective conflicts, not documentation defects.
- Hospitalist-synthesizes-not-defers governance remains active.
- Consultant disagreement must remain time-sensitive and clinically defensible.

## 5. Physician Workflow Mapping

Locked workflow architecture uses four approved workflow categories:

- Discharge Medication Reconciliation.
- Hospital Discharge Summary Generation.
- Discharge Planning Documentation.
- Interdisciplinary Care Plan Development and Documentation.

Future FI-T mapping:

Priority family is tracker-provenance metadata only. It records the historical approved workflow-priority context used during Brainstorm/task architecture validation, but it does not supersede the locked four-workflow architecture, create a new workflow category, or promote historical/superseded tracker labels into governing task-layer architecture.

| Future file | Workflow category | Priority family | Physician-perspective implementation |
| --- | --- | --- | --- |
| FI-T01 | Discharge Medication Reconciliation | P0 tracker provenance | Physician, pharmacist, or discharge clinician request must preserve physician review and final clinical ownership. |
| FI-T02 | Hospital Discharge Summary Generation | P0 tracker provenance | Attending/discharging-service frame; final deliverable should be physician-authored, physician-reviewed, or physician-supervised when later authorized. |
| FI-T03 | Discharge Planning Documentation | P0 tracker provenance | Administrative/care-coordination deliverable remains physician-facing or physician-supervised, even when case management, social work, PT/OT, nursing, and family evidence support it. |
| FI-T04 | Interdisciplinary Care Plan Development and Documentation | P1 tracker provenance | Hospitalist-led interdisciplinary synthesis; physician remains responsible for reconciling specialty recommendations. |
| FI-T05 | Discharge Planning Documentation | P0-derived tracker provenance folded into Discharge Planning Documentation | +7 follow-up context may involve primary care or transition team, but final requested reasoning remains physician-facing. |
| FI-T06 | Discharge Planning Documentation | Historical P0/P1 safety provenance folded into Discharge Planning Documentation | Readmission/safety review remains inside discharge-planning workflow, not a standalone Patient Risk Stratification workflow. |
| FI-T07 | Discharge Medication Reconciliation | P0 tracker provenance | Medication-safety addendum may be pharmacy-framed, but physician review responsibility and discharge safety remain explicit. |

P0 tracker-provenance workflows represented within locked workflow architecture:

- Discharge Medication Reconciliation.
- Hospital Discharge Summary Generation.
- Discharge Planning Documentation.

P1 tracker-provenance workflow represented within locked workflow architecture:

- Interdisciplinary Care Plan Development and Documentation.

P2 tracker-provenance handling:

- P2 medication/readmission-related ideas remain allowable as secondary reasoning texture only.
- No P2 workflow becomes a separate primary workflow in this architecture.
- P0/P1/P2 labels must not be used to reopen the locked workflow count, create a standalone Patient Risk Stratification workflow, or override the File Inventory / Task Architecture Package source hierarchy.

Physician-perspective guidance:

- Future prompts, expected outputs, goldens, and grader guidance must frame final deliverables from the physician perspective or physician voice.
- Supporting evidence may come from pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources.
- Source-of-truth hierarchy answers which evidence source is authoritative; task-design guidance answers who authors, reviews, supervises, or communicates the final deliverable.
- This guidance does not reopen Governance Package v1 or change consultant behavior.

## 6. World Necessity Preservation

Safeguards:

- FI-W22 must remain visible, useful, and incomplete.
- No FI-T file may duplicate FI-W22 into a complete discharge summary, final disposition answer, final medication plan, final prednisone plan, or complete consultant synthesis.
- Batch 1 through Batch 4 must remain necessary for provenance, hospital course, trends, consultant disagreement, functional/cognitive evidence, family concern, and transition support.
- FI-T files must point back to the world rather than restating all needed evidence.
- No single task context file can replace the world.
- Task-context wording must preserve uncertainty and require chart synthesis.
- Trap architecture remains active after task-context framing.

Task-layer watch items:

- Preserve FI-W22 over-trust risk without making FI-W22 useless.
- Preserve Trap #3 as buried evidence and Trap #5 as visible-but-incomplete source hierarchy.
- Preserve the distinction between task framing and answer construction.

## 7. Source-of-Truth Preservation

Master hierarchy safeguards:

- Attending documentation, verified medication reconciliation, pharmacy history, consultant documentation, primary care documentation, family report, and patient recollection remain separate evidence channels.
- FI-T files may identify which channels require review but may not reorder them.

Authority hierarchy safeguards:

- Hospitalist/attending synthesis remains responsible for final inpatient/discharge decisions.
- Consultants provide recommendations and interpretations; they do not become final medication, steroid, or disposition authorities by virtue of task context.
- PT/OT, nursing, case management, social work, family, and pharmacy sources retain their evidence roles without becoming final answer files.

Prednisone hierarchy safeguards:

- Rheumatology attending recommendation remains the highest outpatient prednisone-history authority.
- Verified medication reconciliation remains high-authority current medication evidence.
- Pharmacy/refill history supports exposure but does not prove ingestion.
- Family report and patient recollection remain collateral/lower-authority sources.
- Endocrinology interprets inpatient risk but does not replace rheumatology for outpatient prednisone provenance.

Medication-restart safeguards:

- Medication-restart uncertainty remains a time-sensitive synthesis problem.
- FI-T files must not select final restart timing.
- Cardiology and Nephrology remain simultaneously defensible.
- MAR/action evidence and objective trends remain necessary but not self-interpreting.

## 8. Boundary Conditions

Explicitly prohibited until future authorization:

- FI-T01 through FI-T07 construction.
- FI-S01 through FI-S04 construction.
- Task prompts.
- Expected outputs.
- Golden responses.
- Grader guidance.
- AutoQC responses.
- DOCX artifacts.
- RL Studio submission artifacts.
- Browser/RL Studio activity.
- New synthetic chart files.
- Final task specifications.
- Final task answers.

This architecture may be reviewed, revised, ratified, or locked only under explicit Alexander direction.

## 9. Construction Roadmap

Roadmap only:

1. Task-Level Context File Architecture Review.
2. Task-Level Context File Architecture ratification and lock.
3. Task-Level Context File Construction.
4. Task Prompt Architecture.
5. Task Prompt Construction.
6. Expected Output Architecture.
7. Golden Architecture.
8. Grader Guidance Architecture.
9. Packaging.

No roadmap item is authorized by this document except architecture candidate review.

## Verification Record

Architecture created:

- `worlds/korvin-merrow/task-layer-architecture/candidate-review/task-level-context-file-architecture-v1.md`

Confirmed boundaries:

- No FI-T files created.
- No FI-S files created.
- No task prompts created.
- No expected outputs created.
- No goldens created.
- No grader guidance created.
- No AutoQC responses created.
- No submission artifacts created.
- No DOCX artifacts created.
- Locked clinical artifacts unchanged.
- Locked synthetic files unchanged.

## Final Status

Task-Level Context File Architecture v1

Status:

CANDIDATE REVIEW

Next Eligible Phase:

Task-Level Context File Architecture Review
