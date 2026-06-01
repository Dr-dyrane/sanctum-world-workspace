# Korvin Merrow World Spec Kickoff

Status: World Spec Construction / Preparation Layer complete.

Purpose: mark the transition from approved Brainstorm to World Spec preparation without drafting the World Spec, populating the template, creating a final file inventory, or inventing clinical values.

## 1. Current State

- Brainstorm approved.
- Reviewer GO received from Stacey S.
- RL Studio task ID: `cyau8803`.
- World Spec phase is authorized for kickoff and preparation.
- World Spec construction is authorized.
- World Spec drafting, file inventory, tasks, prompts, goldens, grader guidance, notes, labs, vitals, and synthetic files have not started.
- Clinical Story Skeleton v1 is locked and ratified.
- Clinical Story Skeleton review completed with GO recommendation.
- Clinical Story Skeleton ratification completed after Claude hostile review minor findings.
- Identity Package v1 is locked.
- Official Claude World Spec session is still pending.
- Post-kickoff physician decision record: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-01.md`.
- Latest skeleton lock record: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`.
- Clinical Story Skeleton review: `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`.
- Clinical Story Skeleton ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`.
- Identity Package v1: `worlds/korvin-merrow/world-spec-prep/locked/identity-package-v1.md`.
- Identity Package review addendum: `worlds/korvin-merrow/world-spec-prep/reviews/identity-package-review-addendum.md`.
- Governance Package v1 candidate: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`.
- Governance Package clarification: `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`.
- Governance Package ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`.
- Key Milestones Calendar Skeleton v1: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`.
- Key Milestones Calendar ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`.
- Baseline Anchor Package v1: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`.
- Clinical Story Timeline Package v1: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`.
- Clinical Story Timeline ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`.
- Task Architecture Interview v1: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`.
- Task Architecture Package v1: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`.
- Task Architecture ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`.
- Medication Expansion Package v1: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`.
- Medication Expansion ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`.
- Comorbidity Expansion Package v1: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`.
- Comorbidity Expansion ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`.
- Provider Roster Package v1: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`.
- Provider Roster ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`.
- Surgical History Package v1: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`.
- Surgical History ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`.
- Daily Hospital Course Framework v1: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`.
- Daily Hospital Course Framework ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`.
- Preparation Layer status: COMPLETE.
- Next allowed substantive action: Alexander's explicit next World Spec construction instruction.

## Workspace Bloat And Doctrine Audit

Finding: the workspace has accumulated a lot of useful but overlapping planning documents. This is controlled bloat, not a doctrine breach, as long as we now treat this kickoff file as the active cockpit and avoid re-litigating older prep artifacts unless needed.

Current bloat risks:

- `reference/world-spec-guidelines/04`, `08`, `09`, `10`, `11`, `12`, and `13` overlap around World Spec QC, upload, transcript, and Claude workflow.
- `worlds/korvin-merrow/world-spec-prep/*` contains multiple planning maps that overlap by design.
- `frictions.md` and `traps.md` are still thin placeholders; the approved Brainstorm remains the authoritative source for locked frictions/traps until those files are intentionally updated.
- `tmp/docs/korvin-brainstorm-render/` contains generated render artifacts; these are not authored project logic.

Doctrine check:

- No World Spec draft has been created.
- No official World Spec template has been populated.
- No final Section 3 World File Plan or file inventory has been created.
- No synthetic chart files have been created.
- No final task prompts, golden responses, grader guidelines, or failure analysis have been created.
- Clinical decisions remain physician-originated and Brainstorm-locked.
- Claude remains an official drafting assistant, not the clinical source of truth.

Correction going forward:

1. Use this kickoff file for immediate orientation.
2. Use `project/STATUS.md` for live state.
3. Use `project/WORKSPACE_FILE_MAP.md` to prevent duplicate files.
4. Use `post-go-interview-plan.md` for the interview sequence.
5. Use `08_autoqc_master_index.md` for exact AutoQC checks and `09_world_spec_writer_playbook.md` for practical authoring flow.
6. Use `10`, `11`, `12`, and `13` only when preparing upload package, transcript handling, or Claude workflow.

## 2. Approved Foundation

Patient identity: Korvin Merrow.

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

Identity consistency:

- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with 97 kg and 178 cm.
- Later calendar skeleton must preserve age-62 consistency unless Alexander explicitly reopens DOB or age.
- Identity Package review addendum carries forward implementation notes only: lisinopril cough should be treated as ACE-inhibitor intolerance; later medication history should explain prior ACE-inhibitor/ARNI transition coherently; baseline function, baseline creatinine, dry weight, and similar baseline anchors should be placed during Patient Profile / Clinical History design.

World Type: Typical Clinical World.

Clinical domain: Emergency Medicine / Internal Medicine / acute hospital medicine, following an ED presentation into inpatient hospitalization and discharge planning.

Approved comorbidity burden:

- Type 2 diabetes mellitus, long-standing.
- Hypertension.
- CKD stage 3.
- HFrEF.
- CAD history.
- Hyperlipidemia.
- Anemia of CKD.
- Osteoporosis/osteopenia from chronic steroid exposure.
- Obstructive sleep apnea.
- Diabetic peripheral neuropathy.
- Polymyalgia rheumatica with chronic prednisone exposure and recent taper.
- Polypharmacy.

Approved compact medication list:

- sacubitril/valsartan 24/26 mg BID.
- carvedilol 12.5 mg BID.
- furosemide 40 mg daily.
- spironolactone 25 mg daily.
- empagliflozin 10 mg daily.
- aspirin 81 mg daily.
- atorvastatin 40 mg nightly.
- metformin ER 500 mg BID.
- insulin glargine 18 units nightly.
- prednisone with inconsistent documented taper/dose.
- alendronate 70 mg weekly.
- calcium/vitamin D daily.
- ferrous sulfate 325 mg every other day.
- gabapentin 300 mg nightly.

World close: Hospital Day 6 at 18:00 during discharge planning.

Locked temporal architecture:

- 6-day hospitalization.
- HD6 18:00 world close.
- Discharge anchor after world close.
- +7 day post-discharge anchor.
- +30 day post-discharge anchor.

Locked underlying clinical story:

- Mixed physiology world.
- Infection, steroid issues, CKD/HF, and polypharmacy interact.
- Not a single-diagnosis world.

Locked presentation trigger:

- Progressive weakness.
- Poor oral intake.
- Near-fall/lightheadedness.
- Family-noticed confusion.
- Possible urinary symptoms.

Locked clinical evolution:

- Approximately 3-week decline before presentation.

Locked world tone:

- Medically improving.
- Operationally dangerous discharge.

Locked primary failure target:

- Functional decline.
- Disposition safety.
- Discharge readiness reasoning.

Locked complexity targets:

- Exceed reviewer minimums.
- Target 12-15 comorbidities.
- Target 18-22 medications.

Locked Clinical Story Skeleton v1:

- Baseline: lives with family; independent but slowed by chronic illness; occasional cane use; mild age-related forgetfulness only; chronic diseases generally stable before current decline.
- PMR/prednisone: several-year PMR history with chronic prednisone exposure, multiple prior flares and taper attempts, recent taper due to controlled symptoms, and reconstructable source-of-truth inconsistencies.
- Pre-hospital decline: approximately 3 weeks of reduced stamina, reduced activity, poor appetite, reduced fluid intake, increasing weakness, increasing family dependence, possible urinary symptoms, progressive unsteadiness, and progressive cognitive slowing.
- Escalation: medication-management mistakes, increased dependence, lightheadedness, near-fall event, and family recognition of meaningful deviation from baseline.
- ED presentation: suspected urinary-source infection, dehydration, AKI risk, altered baseline mental status, functional decline, and clinically reasonable sepsis-oriented management. Infection is a contributor, not the entire explanation.
- Hospital course: HD1 admission/stabilization; HD2 partial improvement and consultant involvement begins; HD3 PT/OT identify functional concerns; HD4 consultant tensions emerge and steroid-history inconsistencies are recognized; HD5 medical improvement continues and disposition questions become dominant; HD6 patient appears medically improved but discharge remains debatable.
- Discharge state: infection, AKI, hemodynamics, mental status, and intake improve, while functional reserve, medication restart strategy, steroid interpretation, family concern, and disposition risk remain unresolved.
- Near-fall framework: multi-factorial, not attributable to a single cause.

Ratified governance/story-logic guardrails:

- Endocrine friction wording: Endocrinology vs Primary Team.
- Do not use "Endocrinology vs Documentation." Documentation is evidence, not a friction participant.
- Steroid-record discrepancy remains a trap.
- Prednisone Source-of-Truth Hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Family vs Primary Team remains balanced: family concern is defensible because he is not back to baseline and functional/safety concerns remain; primary team discharge reasoning is also defensible because infection, AKI, mental status, and oral intake are improving and follow-up is available.
- Near-fall remains intentionally multi-factorial, with no single intended explanation. Potential contributors include poor intake, volume depletion, medication effects, neuropathy, deconditioning, infection physiology, and steroid-related physiology.

Governance Package v1:

- Care Team Roster: Hospitalist Service; Cardiology; Nephrology; Endocrinology; Physical Therapy; Occupational Therapy; Case Management; Social Work; Patient; Family/Caregiver; Primary Care Physician.
- Authority Hierarchy: attending hospitalist > consulting attending specialists > PT/OT functional assessments > Case Management / Social Work > family reports > patient recollection.
- Master Source-of-Truth Hierarchy for clinical facts: attending documentation > verified medication reconciliation > pharmacy history > consultant documentation > primary care documentation > family report > patient recollection.
- Confirmed Conditions: HFrEF, CKD Stage 3, Type 2 Diabetes, CAD, Hypertension, Hyperlipidemia, OSA, Diabetic Neuropathy, PMR, Anemia of CKD, Osteoporosis/Osteopenia.
- Presumed / Active Questions: current infection source, steroid contribution, adrenal suppression contribution, degree of dehydration, relative medication contribution, discharge readiness.
- Final Friction Table: Cardiology vs Nephrology for medication restart timing; Family vs Primary Team for discharge readiness; Endocrinology vs Primary Team for steroid interpretation and risk.
- Administrative Deliverable Decision: yes, at least one future task should involve transition of care, discharge planning, care coordination, or follow-up planning.
- Workflow umbrella: Acute Hospital Management, with subdomains of diagnosis, medication management, consultant synthesis, functional assessment, and disposition planning.
- Governance clarification: authority hierarchy resolves factual/documentation conflicts but does not resolve clinical recommendation disagreements. Consultant disagreements require evidence synthesis, timing, trends, patient status, and discharge safety.
- Governance clarification: confirmed steroid-related osteoporosis/osteopenia reflects cumulative chronic steroid exposure but does not prove current symptoms are primarily caused by adrenal suppression.
- Task-architecture watch items remain deferred: AutoQC 2.107 workflow count and 2.108 administrative deliverable must be resolved during task architecture, not inside Governance Package v1.
- Governance Package v1 status: RATIFIED.

Completed Architecture Layers:

- Brainstorm: APPROVED.
- Temporal Architecture: LOCKED.
- Clinical Story Skeleton: RATIFIED.
- Identity Package: LOCKED.
- Governance Package: RATIFIED.

Physician Architecture Layer status: COMPLETE.

Key Milestones Calendar Skeleton v1:

- Approximate decline begins: 04/27/2026.
- Admission / HD1: 05/18/2026.
- HD2: 05/19/2026.
- HD3: 05/20/2026.
- HD4: 05/21/2026.
- HD5: 05/22/2026.
- HD6 and world snapshot day: 05/23/2026.
- World snapshot / world close: 05/23/2026 18:00.
- Discharge anchor: 05/24/2026.
- +7 day anchor: 05/31/2026.
- +30 day anchor: 06/23/2026.
- Status: LOCKED.

Baseline Anchor Package v1:

- Status: LOCKED.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`.
- Physician sign-off completed.
- Locked anchors include baseline creatinine, eGFR, hemoglobin, A1c, dry weight approximately 97 kg, mobility, cognition, medication-management ability, and home support.
- Baseline functional status remains part of the approved baseline framework through mobility, cognition, medication-management ability, and home support.
- Baseline blood pressure may be considered later as a non-numeric future candidate anchor during construction.
- Locked package does not create admission labs, hospital-course trends, file inventory, task architecture, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic files.

Clinical Story Timeline Package v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`.
- Purpose: canonical story-evolution framework answering what changes over time from pre-admission decline through +30 anchor.
- It does not create labs, vitals, medication doses, medication schedules, hospital notes, file inventory, task architecture, milestones beyond locked dates, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic documents.
- Carry-forward file-construction note: preserve the distinction between Trap #3, where important functional/cognitive evidence exists but is easy to miss, and Trap #5, where a visible discharge/source-hierarchy artifact appears sufficient if trusted alone.

Completed construction-preparation chain:

- Key Milestones Calendar Skeleton: LOCKED.
- Baseline Anchor Package: LOCKED.
- Clinical Story Timeline Package: LOCKED.

Task Architecture Interview v1:

- Status: COMPLETE / SUPERSEDED BY LOCKED TASK ARCHITECTURE PACKAGE.
- Artifact: `worlds/korvin-merrow/world-spec-prep/planning-scaffolds/task-architecture-interview-v1.md`.
- Purpose: interview-only framework for resolving AutoQC 2.107 workflow-count constraints, AutoQC 2.108 administrative-deliverable requirements, final task distribution, and workflow consolidation strategy.
- It does not create tasks, task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, reference templates, synthetic files, or new workflows not already implied by approved architecture.

Task Architecture Package v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/task-architecture-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/task-architecture-ratification.md`.
- Purpose: formal task-architecture framework defining six task concepts across four workflows before task drafting.
- Physician decisions recorded: target task count 6, target workflow count 4, administrative deliverable Discharge Planning / Care Coordination, TCM folded into transition/discharge workflow, readmission-risk reasoning kept inside existing workflow structures, consultant synthesis preserved as distinct reasoning area, coding/billing/prior authorization not preferred unless later required.
- `worlds/korvin-merrow/active/task-map.md` has been reconciled; old Brainstorm-level workflow mappings are superseded by this locked package.
- It does not create task prompts, expected outputs, goldens, grader guidance, file inventory, World Spec sections, templates, reference files, or synthetic documents.

Completed construction-preparation chain:

- Key Milestones Calendar Skeleton: LOCKED.
- Baseline Anchor Package: LOCKED.
- Clinical Story Timeline Package: LOCKED.
- Task Architecture Package: LOCKED.

Task Architecture carry-forward watch items:

- AutoQC 2.108 administrative-deliverable reviewer-risk contingency.
- Differentiate three Discharge Planning Documentation task concepts later by requester, time anchor, reasoning emphasis, and deliverable surface.
- Utilization Review is contingency only if challenged later; do not add it now.

Medication Expansion Package v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/medication-expansion-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/medication-expansion-ratification.md`.
- Decision addendum: `worlds/korvin-merrow/world-spec-prep/reviews/medication-expansion-decision-addendum.md`.
- Purpose: candidate baseline medication architecture targeting approximately 18-22 baseline medications before medication schedules, reconciliation outputs, hospital medication changes, discharge lists, file inventory, or World Spec drafting.
- Physician decision resolution: insulin lispro removed from baseline architecture and reserved as a future inpatient-only candidate medication. Baseline medication count is 20.
- Retained medication decisions: nitroglycerin, polyethylene glycol, senna, and cholecalciferol remain in the baseline architecture.
- It does not create doses, frequencies, schedules, medication timelines, admission medication lists, discharge medication lists, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, templates, reference files, or synthetic documents.

Comorbidity Expansion Package v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/comorbidity-expansion-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/comorbidity-expansion-ratification.md`.
- Purpose: baseline chronic-condition architecture targeting approximately 12-15 comorbidities before labs, hospital-course events, task drafting, file planning, or World Spec drafting.
- Ratified baseline comorbidity count: 14 conditions.
- Retained secondary additions: class I obesity by locked BMI, chronic gastroesophageal reflux / chronic acid-suppression indication, and chronic constipation tendency.
- Preserved architecture: all approved conditions, mixed physiology model, presumed/active questions, discharge-safety reasoning, and source-of-truth design.
- It does not create labs, vitals, medication doses, medication schedules, hospital-course events, provider names, surgical history, tasks, prompts, expected outputs, goldens, grader guidance, file inventory, templates, reference files, synthetic documents, or World Spec prose.

Provider Roster Package v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/provider-roster-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/provider-roster-ratification.md`.
- Purpose: provider/care-team and stakeholder architecture before note authorship, file planning, task drafting, synthetic documents, or World Spec drafting.
- Named high-authority roles are locked for attending hospitalist, cardiology, nephrology, endocrinology, PCP, outpatient rheumatology, and family/caregiver stakeholder.
- Shared Merrow surname for Korvin Merrow and Mara Merrow is intentionally approved.
- Minor or rotating contributors remain service-role placeholders to avoid over-naming.
- It does not create clinical notes, provider-authored documents, file inventory, task prompts, expected outputs, goldens, grader guidance, medication schedules, hospital-course events, labs, vitals, templates, reference files, synthetic documents, or World Spec prose.

Surgical History Package v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/surgical-history-package-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/surgical-history-ratification.md`.
- Purpose: pre-world surgical/procedural history architecture before Daily Hospital Course Framework, World Spec construction, file inventory planning, synthetic documents, task prompts, expected outputs, goldens, or grader guidance.
- Confirmed procedural anchors: remote percutaneous coronary intervention with coronary stent placement and remote diagnostic sleep study confirming obstructive sleep apnea.
- Excluded/noise-controlled procedures: ICD/CRT/pacemaker, CABG, dialysis access, major orthopedic fracture repair or joint replacement, limb amputation/major diabetic foot surgery, temporal artery biopsy/rheumatologic diagnostic procedure, and screening colonoscopy for v1 purposes.
- Guardrail: surgical/procedural history should remain background realism and provenance support; it must not create a new disease arc, reveal the cause of the presentation, collapse mixed physiology, or weaken frictions/traps.
- Carry-forward: keep PCI remote so aspirin-only baseline remains consistent; decide procedural provenance during file inventory; File Inventory Architecture remains deferred.

Daily Hospital Course Framework v1:

- Status: LOCKED.
- Artifact: `worlds/korvin-merrow/world-spec-prep/locked/daily-hospital-course-framework-v1.md`.
- Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/daily-hospital-course-framework-ratification.md`.
- Purpose: canonical HD1-HD6 evolution model that bridges locked architecture and later World Spec/file/task construction.
- It defines primary clinical state, changes, improvements, remaining concerns, active frictions, active traps, relevant provider groups, and disposition readiness status for each hospital day.
- It does not create labs, lab trends, vitals, medication doses, medication schedules, medication orders, clinical notes, file inventory, tasks, prompts, expected outputs, goldens, grader guidance, synthetic files, World Spec prose, templates, or reference files.
- Guardrail: this is a major bridge artifact, not a small package. Treat it as the daily construction spine while preserving mixed physiology, no reveal-drift, and medically improving but operationally dangerous discharge logic.

Preparation Layer:

- Status: COMPLETE.
- Completed artifacts: Brainstorm, Temporal Architecture, Clinical Story Skeleton, Identity Package, Governance Package, Key Milestones Calendar Skeleton, Baseline Anchor Package, Clinical Story Timeline Package, Task Architecture Package, Medication Expansion Package, Comorbidity Expansion Package, Provider Roster Package, Surgical History Package, and Daily Hospital Course Framework.
- World Spec Construction status: AUTHORIZED.
- Boundary: World Spec drafting, file inventory, synthetic files, tasks, prompts, expected outputs, goldens, grader guidance, notes, labs, vitals, and hospital-course documentation remain unstarted until Alexander explicitly authorizes the relevant next step.

Fetched World Spec source examples:

- Alexander added World Spec example source documents under `reference/word-spec-examples/`.
- These are source/reference artifacts only. Preserve them separately from authored Korvin Merrow work and do not treat them as generated project content or as the Korvin Merrow file inventory.

Primary frictions:

1. Nephrology vs Cardiology: renal/hemodynamic safety during AKI/hypotension vs HFrEF/CAD long-term protective therapy.
2. Family vs Inpatient Medicine: medical stability on paper vs functional readiness and real-world discharge safety.
3. Endocrinology vs Primary Team: risk of premature steroid withdrawal vs risk of unnecessary steroid continuation.

World-level traps:

1. Steroid timeline/source-of-truth trap.
2. HF-AKI medication reconciliation and time-sensitive consultant trap.
3. Buried functional/cognitive status trap.
4. Sepsis anchoring after partial improvement trap.
5. Discharge plan source-hierarchy trap.

Rough task concepts:

1. Discharge medication reconciliation / medication safety review.
2. Hospital discharge summary generation.
3. Transition-of-care / discharge readiness plan.
4. Post-hospital follow-up assessment note.
5. Consultant recommendation synthesis / care coordination note.
6. Readmission risk / patient safety review.

Reserve only:

- Future ED reassessment after return visit.

## 3. Required World Spec Workflow

1. Physician decision interview first.
2. Official Claude World Spec prompt/session.
3. Codex consolidation against physician intent and source rules.
4. Official World Spec template population only after Alexander authorizes drafting.
5. Claude QC with the appropriate World Spec AutoQC prompt/checklist and supplemental materials.
6. RL Studio World Spec AutoQC.
7. Submission package assembly.

Workflow guardrails:

- The official Claude World Spec session should use a fresh Claude Project chat.
- Claude should load the approved Brainstorm, interview section by section, run audit before drafting, and draft only after confirmation.
- Codex should preserve Claude outputs separately from authored/submission work.
- RL Studio/browser activity requires explicit authorization.

## 4. Pending Physician Decisions

Identity and demographics:

- Identity Package v1 is locked.
- Identity Package review addendum is recorded and does not reopen Identity Package v1.
- Calendar date skeleton v1 is locked and preserves DOB/age consistency.

Clinical structure:

- Key Milestones.
- Confirmed vs presumed condition split.
- Care team roster.
- Source-of-truth hierarchy. Prednisone hierarchy is already ratified; broader chart hierarchy still pending.
- Decision Friction Table details.
- Governance Package v1 is ratified and contains the care team roster, broader source-of-truth hierarchy, confirmed vs presumed condition split, Decision Friction Table, administrative deliverable decision, and workflow umbrella.
- Clinical Story Skeleton v1 is ratified. Do not reopen unless Alexander explicitly does so.
- Medication Expansion Package v1 is locked at 20 baseline medication items.
- Comorbidity Expansion Package v1 is locked at 14 baseline conditions.

Task architecture:

- Workflow consolidation to 3-5 catalog workflows.
- Administrative deliverable decision.
- Task anchors.
- Task independence discipline.

Traceability:

- Traceability workflow.
- Which facts belong in Clinical History vs later chart files.
- How each trap will eventually map to file evidence without creating the final file inventory yet.

## 5. AutoQC Watch Items

- 2.2 synthetic name already addressed.
- 2.3 synthetic MRN pending.
- 2.14 Decision Friction Table.
- 2.22/2.23 milestone superset/no orphan milestones.
- 2.41 temporal architecture.
- 2.42 file-plan table column mismatch / Source + Tool issue.
- 2.48 fact-to-file traceability.
- 2.65 source-of-truth hierarchy.
- 2.101 no Section D/E or higher.
- 2.107 3-5 distinct workflows.
- 2.108 clinical + administrative work product question.
- 2.113 Source/Tool and file origin convention.

## 6. Submission Package Watch Items

- Final World Spec `.docx`.
- Template/reference files.
- Custom-made files if used.
- Writer-produced files if used.
- Claude transcripts if requested by RL Studio/upload flow.
- No zip; upload files individually.

Known unresolved package questions:

- Source text references a "Claude Transcript" in a World Spec upload tutorial title, but local text does not define transcript scope or format.
- Source text contains a tension between older onboarding language saying "spec only" and later May 20 guidance saying new writers curate template/reference files. Confirm from RL Studio/pod guidance before upload.

## 7. Stop Conditions

Stop before:

- Revising the locked Clinical Story Skeleton unless Alexander explicitly reopens it.
- Revising Identity Package v1 unless Alexander explicitly reopens it.
- Governance Package work unless Alexander explicitly starts that phase.
- World Spec drafting unless Alexander explicitly authorizes drafting.
- Milestone creation.
- Final file inventory.
- Task prompts.
- Golden responses.
- Grader guidelines.
- Invented clinical values, dates, lab values, vitals, provider names, MRN, or file names.
- Synthetic file generation.
- RL Studio upload/submission without explicit authorization.

If any requested step appears to cross these boundaries, pause and ask Alexander.
