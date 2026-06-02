# Handoff State

Purpose: enable a brand-new Claude session to resume accurately without stale assumptions.

## Where We Are

Project Sanctum onboarding is in Phase 1 World Building. Alexander has explicitly authorized local construction beyond the earlier steps through Batch 3 synthetic world-level file construction. Batch 1 and Batch 2 are locked. Batch 3 is in candidate review and is not locked.

The Brainstorm for Korvin Merrow World has been completed, passed AutoQC, uploaded to RL Studio, returned SEND BACK from Human Review, remediated, reuploaded, resubmitted, and approved by Stacey S.

RL Studio:

- Task ID: `cyau8803`
- Status: Brainstorm approved / ready for World Spec transition
- Brainstorm AutoQC: revised run `0 failed / 51 passed`
- Diagnostics reviewed: yes
- Human Review: GO from Stacey S
- Approval source: Slack / Stacey S
- Reviewer message: "great job! I approved your brainstorm. Next steps are to move forward with world spec and file template development."

Current state: Batch 3 Synthetic World-Level File Construction / Candidate Review. World Spec Skeleton v1 is locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`. World Spec v1 is locked at `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`, with ratification recorded at `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`. World Spec Construction is complete. File Inventory Architecture v1 is locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-architecture-v1.md`, with ratification recorded at `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-architecture-ratification.md`. Phase 3 File Inventory Architecture is complete. File Inventory v1 is locked at `worlds/korvin-merrow/file-inventory/locked/file-inventory-v1.md`, with ratification recorded at `worlds/korvin-merrow/file-inventory/ratifications/file-inventory-v1-ratification.md`. File Inventory Planning is complete. Synthetic World-Level File Construction Plan v1 is locked at `worlds/korvin-merrow/synthetic-files/locked/synthetic-world-file-construction-plan-v1.md`, with ratification recorded at `worlds/korvin-merrow/synthetic-files/ratifications/synthetic-world-file-construction-plan-v1-ratification.md`. Synthetic File Construction Governance is complete. Batch 1 synthetic world-level files FI-W01 through FI-W07 are locked at `worlds/korvin-merrow/synthetic-files/locked/batch-1/`, with ratification recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-1-ratification.md` and validation recorded at `worlds/korvin-merrow/synthetic-files/locked/batch-1/batch-1-validation-review.md`. Batch 1 Construction is complete. Batch 2 synthetic world-level files FI-W08 through FI-W13 are locked at `worlds/korvin-merrow/synthetic-files/locked/batch-2/`, with ratification recorded at `worlds/korvin-merrow/synthetic-files/ratifications/batch-2-ratification.md` and validation recorded at `worlds/korvin-merrow/synthetic-files/locked/batch-2/batch-2-validation-review.md`. Batch 2 Construction is complete. Batch 3 candidate synthetic world-level files FI-W14 through FI-W16 are in candidate review at `worlds/korvin-merrow/synthetic-files/candidate-review/batch-3/`, with candidate validation review recorded at `worlds/korvin-merrow/synthetic-files/candidate-review/batch-3/batch-3-validation-review.md`. FI-W17 through FI-W22, tasks, prompts, expected outputs, goldens, grader guidance, DOCX submission packaging, AutoQC, and RL Studio upload remain gated on explicit Alexander authorization for the relevant step.

Repository collaboration readiness note: a new Codex session reconstructed the repository state from repository files alone. The repository is collaboration-ready because `project/STATUS.md`, `docs/status-dashboard.md`, `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`, `project/WORKSPACE_FILE_MAP.md`, and this handoff converge on Batch 3 candidate review / Batch 3 review and ratification next eligible. The canonical file map is `project/WORKSPACE_FILE_MAP.md`.

## Locked Decisions

Locked from approved Brainstorm:

- Acute hospital medicine world, ED to inpatient admission.
- Multi-day hospitalization ending at Hospital Day 6 at 18:00 during discharge planning.
- Patient seed: 62-year-old male with T2DM, HTN, CKD stage 3, HFrEF, CAD, hyperlipidemia, anemia of CKD, osteoporosis/osteopenia from chronic steroid exposure, obstructive sleep apnea, diabetic peripheral neuropathy, polypharmacy, PMR with prior chronic prednisone and recent taper.
- Presentation: AMS, progressive weakness, poor oral intake, reduced activity, borderline hypotension, AKI on CKD, possible urinary-source infection.
- Initial suspected sepsis treatment is appropriate.
- Complexity evolves from overlapping common hospital contributors, not from a single rare diagnosis.

Locked primary frictions:

1. Nephrology vs Cardiology.
2. Family vs Inpatient Medicine.
3. Emergency/Inpatient Medicine vs Endocrinology.

Locked world-level traps:

1. Steroid timeline/source-of-truth trap.
2. HF-AKI medication reconciliation and time-sensitive consultant trap.
3. Buried functional/cognitive status trap.
4. Sepsis anchoring after partial improvement trap.
5. Discharge plan source-hierarchy trap.

Approved rough task concepts:

1. Discharge medication reconciliation / medication safety review.
2. Hospital discharge summary generation.
3. Transition-of-care / discharge readiness plan.
4. Post-hospital follow-up assessment note.
5. Consultant recommendation synthesis / care coordination note.
6. Readmission risk / patient safety review.

Reserve only:

- Future ED reassessment after return visit.

Approved Brainstorm remediation additions:

- World Type: Typical Clinical World.
- Medication list: sacubitril/valsartan 24/26 mg BID; carvedilol 12.5 mg BID; furosemide 40 mg daily; spironolactone 25 mg daily; empagliflozin 10 mg daily; aspirin 81 mg daily; atorvastatin 40 mg nightly; metformin ER 500 mg BID; insulin glargine 18 units nightly; prednisone with inconsistent documented taper/dose; alendronate 70 mg weekly; calcium/vitamin D daily; ferrous sulfate 325 mg every other day; gabapentin 300 mg nightly.
- Active DOCX: `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`.

Post-kickoff physician-locked decisions:

- Temporal architecture: 6-day hospitalization; HD6 18:00 world close; discharge anchor; +7 day anchor; +30 day anchor.
- Underlying clinical story: mixed physiology world with infection, steroid issues, CKD/HF, and polypharmacy interaction. Not a single-diagnosis world.
- Presentation trigger: progressive weakness, poor oral intake, near-fall/lightheadedness, family-noticed confusion, possible urinary symptoms.
- Clinical evolution: approximately 3-week decline before presentation.
- World tone: medically improving but operationally dangerous discharge.
- Primary failure target: functional decline, disposition safety, discharge readiness reasoning.
- Complexity targets: exceed reviewer minimums; target 12-15 comorbidities and 18-22 medications.
- Durable record: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`.

Locked Clinical Story Skeleton v1:

- Patient: Korvin Merrow, 62-year-old male, Typical Clinical World.
- Baseline: lives with family; independent but slowed by chronic illness; occasional cane use; mild age-related forgetfulness only; chronic diseases generally stable before current decline.
- PMR/prednisone: several-year PMR history, chronic prednisone exposure, multiple prior flares and taper attempts, recent taper due to controlled symptoms, and reconstructable source-of-truth inconsistencies.
- Pre-hospital decline: approximately 3 weeks of reduced stamina, reduced activity, poor appetite, reduced fluid intake, increasing weakness, increasing family dependence, possible urinary symptoms, progressive unsteadiness, and progressive cognitive slowing.
- Escalation: medication-management mistakes, increased dependence, lightheadedness, near-fall event, and family recognition of meaningful deviation from baseline.
- ED presentation: suspected urinary-source infection, dehydration, AKI risk, altered baseline mental status, functional decline, and reasonable sepsis-oriented management. Infection is a contributor, not the entire explanation.
- Hospital course: HD1 admission/stabilization; HD2 partial improvement and consultant involvement begins; HD3 PT/OT identify functional concerns; HD4 consultant tensions emerge and steroid-history inconsistencies are recognized; HD5 medical improvement continues and disposition questions become dominant; HD6 patient appears medically improved but discharge remains debatable.
- Discharge state: infection, AKI, hemodynamics, mental status, and oral intake improved, while functional reserve, medication restart strategy, steroid interpretation, family concern, and disposition risk remain unresolved.
- Primary failure target: disposition safety, functional decline recognition, and discharge-readiness reasoning.
- Near-fall framework: multi-factorial and not attributable to a single cause.
- Review artifact: `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`.
- Lock record: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`.
- Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`.

Ratified governance/story-logic guardrails:

- Endocrine friction label is Endocrinology vs Primary Team.
- Do not use Endocrinology vs Documentation. Documentation is evidence, not a friction participant.
- Steroid-record discrepancy remains a trap.
- Prednisone Source-of-Truth Hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Family vs Primary Team is balanced: family concern is defensible, and primary team discharge reasoning is also defensible.
- Near-fall is intentionally multi-factorial with no single intended explanation.

Locked Identity Package v1:

- Name: Korvin Merrow.
- DOB: 1964-02-18.
- Age: 62.
- MRN: KM-6427819.
- Height: 178 cm (5'10").
- Weight: 97 kg (214 lb).
- BMI: 30.6.
- Allergy: Lisinopril (cough).
- Code Status: Full Code.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`.
- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with 97 kg and 178 cm.
- Review addendum: `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`.
- Addendum notes are carry-forward implementation notes only: lisinopril cough is ACE-inhibitor intolerance; later medication history should explain prior ACE-inhibitor/ARNI transition coherently; baseline function, baseline creatinine, dry weight, and similar baseline anchors should be placed during Patient Profile / Clinical History design.
- Do not reopen Identity Package v1.

Governance Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`.
- Clarification artifact: `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`.
- Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`.
- Status: RATIFIED.
- Care team roster: Hospitalist Service; Cardiology; Nephrology; Endocrinology; Physical Therapy; Occupational Therapy; Case Management; Social Work; Patient; Family/Caregiver; Primary Care Physician.
- Authority hierarchy: attending hospitalist > consulting attending specialists > PT/OT functional assessments > Case Management / Social Work > family reports > patient recollection.
- Master clinical source-of-truth hierarchy: attending documentation > verified medication reconciliation > pharmacy history > consultant documentation > primary care documentation > family report > patient recollection.
- Preserve prednisone-specific hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Authority Hierarchy and Source-of-Truth Hierarchy are distinct. Authority Hierarchy governs role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership. Source-of-Truth Hierarchy governs factual conflict resolution.
- Authority hierarchy does not resolve clinical recommendation disagreements. Consultant disagreements require evidence synthesis, timing, trends, patient status, and discharge safety.
- Confirmed conditions: HFrEF, CKD Stage 3, Type 2 Diabetes, CAD, Hypertension, Hyperlipidemia, OSA, Diabetic Neuropathy, PMR, Anemia of CKD, Osteoporosis/Osteopenia.
- Presumed / active questions: current infection source, steroid contribution, adrenal suppression contribution, degree of dehydration, relative medication contribution, discharge readiness.
- Steroid-related osteoporosis/osteopenia reflects cumulative chronic steroid exposure but does not prove current symptoms are primarily caused by adrenal suppression.
- Final friction table: Cardiology vs Nephrology for medication restart timing; Family vs Primary Team for discharge readiness; Endocrinology vs Primary Team for steroid interpretation and risk.
- Administrative deliverable decision: yes.
- Workflow umbrella: Acute Hospital Management. Exact future task workflow lines must still use official tracker names.
- AutoQC 2.107 workflow count and 2.108 administrative deliverable remain deferred task-architecture watch items.

Completed Architecture Layers:

- Brainstorm: APPROVED.
- Temporal Architecture: LOCKED.
- Clinical Story Skeleton: RATIFIED.
- Identity Package: LOCKED.
- Governance Package: RATIFIED.

Physician Architecture Layer Status: COMPLETE.

Key Milestones Calendar Skeleton v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`.
- Status: LOCKED.
- Approximate decline begins: 04/27/2026.
- Admission / HD1: 05/18/2026.
- World snapshot / world close: 05/23/2026 18:00.
- Discharge anchor: 05/24/2026.
- +7 day anchor: 05/31/2026.
- +30 day anchor: 06/23/2026.
- Locked doctrine: +7 and +30 anchors are measured from discharge anchor 05/24/2026, not from HD6 world close.
- Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`.
- Date framework only; not a final milestone table, task architecture, file inventory, or World Spec draft.

Baseline Anchor Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`.
- Status: LOCKED.
- Physician sign-off completed.
- Locked anchors include baseline creatinine, eGFR, hemoglobin, A1c, dry weight approximately 97 kg, mobility, cognition, medication-management ability, and home support.
- Baseline functional status remains part of the approved baseline framework through mobility, cognition, medication-management ability, and home support.
- Baseline blood pressure may be considered as a future candidate anchor during construction only; do not create a numeric value at this stage.
- These are not admission labs, hospital-course trends, final file inventory, task architecture, or World Spec prose.

Clinical Story Timeline Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`.
- Status: LOCKED.
- Purpose: canonical story-evolution framework from pre-admission decline through HD1-HD6, discharge, +7, and +30 anchors.
- It does not create labs, vitals, medication doses, medication schedules, hospital notes, file inventory, task architecture, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic documents.
- Carry-forward note: preserve Trap #3 as buried functional/cognitive evidence and Trap #5 as reassuring but incomplete discharge/source-hierarchy artifact during later file construction.

Task Architecture Interview v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`.
- Status: COMPLETE / SUPERSEDED BY LOCKED TASK ARCHITECTURE PACKAGE.
- Purpose: interview-only framework for resolving AutoQC 2.107 workflow-count constraints, AutoQC 2.108 administrative-deliverable requirements, final task distribution, and workflow consolidation strategy.
- Boundary: does not create tasks, task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, reference templates, synthetic files, or new workflows not already implied by approved architecture.

Task Architecture Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`.
- Status: LOCKED.
- Purpose: formal task-architecture framework defining six task concepts across four workflows before task drafting.
- Physician decisions: target task count 6; target workflow count 4; administrative deliverable Discharge Planning / Care Coordination; TCM folded into transition/discharge workflow; consultant synthesis distinct; readmission-risk reasoning kept inside existing workflow structures; coding, billing, and prior authorization not preferred unless later required.
- Candidate workflows: Discharge Medication Reconciliation; Hospital Discharge Summary Generation; Discharge Planning Documentation; Interdisciplinary Care Plan Development and Documentation.
- AutoQC 2.108 remains a documented reviewer-risk bet, not a blocker. Utilization Review is contingency only if challenged later and should not be added now.
- TCM and readmission-risk reasoning are embedded inside Discharge Planning Documentation rather than standalone workflow categories.
- Medicine Team Lead task-design guidance is future task-layer framing only, not source-of-truth hierarchy and not governance redesign. Source-of-truth hierarchy answers: "When sources disagree, which evidence source is authoritative?" Task-design guidance answers: "Who is the final deliverable written by or for?" Later task prompts, expected outputs, goldens, and grader guidance must frame final deliverables from the physician perspective or physician voice, even when supporting sources are pharmacy, nursing, PT/OT, case management, social work, family, or administrative sources. Do not redesign the world, reopen Governance Package v1, or alter source-of-truth hierarchy because of this guidance.
- Boundary: does not create task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, templates, reference files, or synthetic documents.

Medication Expansion Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`.
- Decision addendum: `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md`.
- Status: LOCKED.
- Purpose: candidate baseline medication architecture targeting approximately 18-22 medications.
- Physician decision: insulin lispro removed from baseline medication architecture and reserved as future inpatient-only candidate medication. Baseline medication count is 20.
- Boundary: does not create doses, frequencies, schedules, medication timelines, reconciliation outputs, hospital medication changes, admission medication lists, discharge medication lists, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, World Spec prose, templates, reference files, or synthetic documents.

Comorbidity Expansion Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`.
- Status: LOCKED.
- Purpose: baseline chronic-condition architecture targeting approximately 12-15 comorbidities.
- Final baseline condition count: 14.
- Preserves all already-approved conditions and retains only secondary additions: class I obesity by locked BMI, chronic gastroesophageal reflux / chronic acid-suppression indication, and chronic constipation tendency.
- Boundary: does not create labs, vitals, medication doses, medication schedules, hospital-course events, provider names, surgical history, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, World Spec prose, templates, reference files, or synthetic documents.

Provider Roster Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`.
- Status: LOCKED.
- Purpose: provider/care-team and stakeholder architecture before note authorship, file planning, task drafting, synthetic documents, or World Spec drafting.
- Locked named high-authority roles: Dr. Elian Vossmere, Dr. Maris Caldrane, Dr. Iven Solthar, Dr. Nerea Veylorn, Dr. Talia Quenor, Dr. Soren Halvek, and Mara Merrow.
- Shared Merrow surname is intentional.
- Resident and pharmacy remain role-based.
- No additional provider naming is authorized.
- Boundary: does not create clinical notes, provider-authored documents, file inventory, task prompts, expected outputs, goldens, grader guidance, medication schedules, hospital-course events, labs, vitals, World Spec prose, templates, reference files, or synthetic documents.

Surgical History Package v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`.
- Status: LOCKED.
- Purpose: pre-world surgical/procedural history architecture before Daily Hospital Course Framework, World Spec construction, file inventory planning, synthetic documents, task prompts, expected outputs, goldens, or grader guidance.
- Confirmed procedural anchors: remote percutaneous coronary intervention with coronary stent placement and remote diagnostic sleep study confirming obstructive sleep apnea.
- Excluded/noise-controlled procedures: ICD/CRT/pacemaker, CABG, dialysis access, major orthopedic fracture repair or joint replacement, limb amputation/major diabetic foot surgery, temporal artery biopsy/rheumatologic diagnostic procedure, and screening colonoscopy for v1 purposes.
- Boundary: does not create operative reports, procedure notes, hospital-course events, labs, vitals, file inventory, tasks, synthetic files, or World Spec prose.

Daily Hospital Course Framework v1:

- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`.
- Status: LOCKED.
- Purpose: major bridge artifact defining architecture-level HD1-HD6 daily evolution before World Spec/file/task construction.
- Captures primary clinical state, what changed, what improved, what remains concerning, active frictions, active traps, relevant provider groups, and disposition readiness for each hospital day.
- Boundary: does not create labs, lab trends, vitals, medication doses, medication schedules, orders, notes, discharge summaries, file inventory, tasks, prompts, expected outputs, goldens, grader guidance, synthetic files, World Spec prose, templates, or reference files.

Preparation Layer:

- Status: COMPLETE.
- Completed artifacts: Brainstorm, Temporal Architecture, Clinical Story Skeleton, Identity Package, Governance Package, Key Milestones Calendar Skeleton, Baseline Anchor Package, Clinical Story Timeline Package, Task Architecture Package, Medication Expansion Package, Comorbidity Expansion Package, Provider Roster Package, Surgical History Package, and Daily Hospital Course Framework.

World Spec Skeleton v1:

- Artifact: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md`.
- Status: LOCKED.
- Purpose: structural map for final World Spec section order, source-package mapping, construction boundaries, Studio alignment, AutoQC readiness, and construction order.
- Boundary: does not create final World Spec prose, synthetic files, file inventory rows, clinical notes, labs, vitals, task prompts, expected outputs, goldens, grader guidance, reference files, or templates.

World Spec v1:

- Artifact: `worlds/korvin-merrow/world-spec-construction/locked/world-spec-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-v1-ratification.md`.
- Status: LOCKED.
- Purpose: first complete World Spec candidate built from locked architecture only.
- Boundary: does not create file inventory rows, synthetic files, clinical notes, labs, vitals, medication schedules, task prompts, expected outputs, golden responses, grader guidance, AutoQC responses, reference files, templates, DOCX submission artifacts, or RL Studio upload.

Fetched World Spec source examples:

- Alexander added source/reference examples under `reference/word-spec-examples/`.
- Treat them as source/reference material only, not authored Korvin Merrow content or the Korvin Merrow World File Plan.

## Decisions Remaining

Do not answer these without Alexander.

Identity/compliance:

- Identity Package v1 is locked.
- Identity Package review addendum is recorded and does not reopen identity values.
- Later calendar skeleton must preserve DOB/age consistency unless Alexander explicitly reopens DOB or age.

Clinical scenario:

- Final key milestone list for the eventual World Spec template.
- Source-of-truth hierarchy for conflicting evidence.

Task architecture:

- Task Architecture Package v1 is locked.
- Later task construction must differentiate the three Discharge Planning Documentation concepts by requester, time anchor, reasoning emphasis, and deliverable surface.
- Final task independence, requester, anchor, and one-deliverable discipline remain to be applied during authorized task specification work.

Traceability/file strategy:

- Evidence provenance workflow.
- Later file modalities.
- Later trap substrate planning.
- File Inventory v1 is locked; later work must preserve its rows unless Alexander explicitly reopens it.

## Verified World Spec Risks

Use these as future World Spec priorities only after Brainstorm GO:

- AutoQC 2.2: patient name must be unmistakably synthetic.
- AutoQC 2.3: MRN must be clearly synthetic.
- AutoQC 2.14: Decision Friction Table required when 2+ conflicts exist.
- AutoQC 2.18 and 2.48: clinical facts and Expected Output facts must trace to narrative or file rows.
- AutoQC 2.41: temporal architecture is a blocker gate.
- AutoQC 2.65: source-of-truth hierarchy required when authority traps are present.
- AutoQC 2.98: workflow names must match approved tracker exactly.
- AutoQC 2.107: final world must use 3-5 distinct catalog workflows.
- AutoQC 2.108: typical clinical/medical director worlds should include clinical and healthcare administration work products where appropriate.

## Next Legal Action

Use `worlds/korvin-merrow/world-spec-construction/locked/world-spec-skeleton-v1.md`, `worlds/korvin-merrow/world-spec-construction/ratifications/world-spec-skeleton-ratification.md`, `worlds/korvin-merrow/world-spec-prep/WORLD_SPEC_KICKOFF.md`, `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`, `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`, `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`, `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`, `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`, `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`, `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`, `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`, `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`, `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`, `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`, `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`, and `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md` for orientation.

Review Batch 3 candidate files FI-W14 through FI-W16 and decide whether to revise, ratify, and lock them.

For the next preparation step:

1. Read `project/STATUS.md`, `project/PASS_PLAN.md`, `WORLD_SPEC_KICKOFF.md`, `physician-decision-log-02.md`, `clinical-story-skeleton-ratification.md`, `identity-package-v1.md`, `identity-package-review-addendum.md`, `governance-package-v1.md`, `governance-package-clarification.md`, `governance-package-ratification.md`, `key-milestones-calendar-skeleton-v1.md`, `key-milestones-calendar-ratification.md`, `baseline-anchor-package-v1.md`, `clinical-story-timeline-package-v1.md`, `clinical-story-timeline-ratification.md`, `task-architecture-interview-v1.md`, `task-architecture-package-v1.md`, `task-architecture-ratification.md`, `medication-expansion-package-v1.md`, `comorbidity-expansion-package-v1.md`, `comorbidity-expansion-ratification.md`, `provider-roster-package-v1.md`, `provider-roster-ratification.md`, `surgical-history-package-v1.md`, `daily-hospital-course-framework-v1.md`, `world-spec-skeleton-v1.md`, and `world-spec-skeleton-ratification.md`.
2. Use only locked physician decisions, the ratified Clinical Story Skeleton, locked Identity Package, ratified Governance Package v1, locked calendar skeleton, locked baseline anchor package, and approved Brainstorm material.
3. Do not populate the official World Spec template until Alexander authorizes template population.

Until Alexander authorizes the next construction unit:

1. Continue only explicitly authorized World Spec construction or review activities.
2. Do not revise the locked Clinical Story Skeleton.
3. Do not revise locked World Spec v1 without Alexander approval.
4. Do not lock Batch 3, create FI-W17 through FI-W22, or create downstream file/task outputs without explicit authorization.

Before ending any working session:

1. Leave the working tree clean, or explicitly document uncommitted state.
2. Update current phase and next eligible phase.
3. Preserve locked artifacts unless Alexander explicitly authorized reopening or editing them.
4. Locate and status-label candidate artifacts.
5. Move newly locked artifacts to locked paths and create/reference ratifications.
6. Update continuity surfaces and Claude handoff files.
7. Remove or explicitly mark stale active candidate paths as historical.
8. Avoid unauthorized files.
9. Record carry-forward watch items and future task-layer guidance.
10. Commit completed work unless Alexander explicitly instructs not to commit.
11. Final report must state what changed, what did not change, current status, next eligible phase, and whether the repository is safe for another collaborator.

## Hard Boundaries

Do not:

- draft the World Spec before explicit Alexander authorization;
- revise the locked Clinical Story Skeleton without explicit Alexander approval;
- revise Identity Package v1 without explicit Alexander approval;
- change Governance Package v1 without Alexander approval;
- populate the World Spec template before explicit Alexander authorization;
- create Section 3 file inventory before explicit authorization;
- create milestones before explicit authorization;
- lock Batch 3 or create FI-W17 through FI-W22 before explicit authorization;
- invent labs, vitals, medications, doses, dates, provider names, MRN, or patient name;
- write final task prompts;
- write golden responses;
- write grader guidelines;
- do failure analysis;
- change Brainstorm clinical content unless new reviewer feedback arrives and Alexander approves the response plan.

## Current Best Claude Task

If asked to help now, Claude should only support preparation:

- summarize current state;
- audit against AutoQC v6.3;
- prepare or refine Governance Package interview questions;
- critique proposed physician decisions;
- help maintain consistency with the approved Brainstorm.

## Workspace Doctrine Note

The workspace contains overlapping prep and guideline docs. This is intentional but should now be treated as supporting reference material. The active cockpit for the World Spec transition is `WORLD_SPEC_KICKOFF.md`; the live state source is `project/STATUS.md`; exact AutoQC checks live in `reference/world-spec-guidelines/08_autoqc_master_index.md`; practical authoring flow lives in `reference/world-spec-guidelines/09_world_spec_writer_playbook.md`.
