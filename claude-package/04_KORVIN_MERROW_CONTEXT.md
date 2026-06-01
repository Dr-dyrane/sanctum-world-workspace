# Korvin Merrow Context

Purpose: compressed Claude context for a fresh Project Sanctum session. Use this as operational context only; the full source of truth remains local under `reference/` and `worlds/korvin-merrow/`.

Boundary: Brainstorm is approved after SEND BACK remediation. Clinical Story Skeleton v1 is ratified. Identity Package v1 is locked. Governance Package v1 is ratified. Physician Architecture Layer is complete. Key Milestones Calendar Skeleton v1 is locked. Baseline Anchor Package v1 is locked. World Spec drafting is not authorized until Alexander explicitly authorizes drafting.

## Current World Concept

Working title: Korvin Merrow World.

Clinical domain: Emergency Medicine / Internal Medicine / acute hospital medicine.

Core idea: a realistic multi-day hospitalization for a medically complex 62-year-old man who presents from home with altered mental status, progressive weakness, poor oral intake, reduced activity, borderline hypotension, AKI on CKD, possible urinary symptoms, and subjective fever.

Initial management as suspected urinary-source sepsis is appropriate. The case becomes difficult because infection improves but the patient does not return cleanly to baseline. The world tests whether an AI can reassess evolving information rather than using the initial sepsis diagnosis as a total explanation.

Design philosophy:

- Do not create a rare disease puzzle.
- Do not make adrenal insufficiency the hidden answer.
- Complexity should come from common hospital medicine: messy documentation, medication changes, consultant tension, functional decline, and discharge safety.
- The AI should demonstrate prioritization, synthesis across documents, uncertainty handling, medication reasoning, source-of-truth reasoning, and safe decision-making when reasonable clinicians disagree.

## Approved Brainstorm Summary

Brainstorm submitted in RL Studio and passed final Brainstorm AutoQC 51/51 before Human Review. Human Review returned SEND BACK requiring synthetic identity, World Type declaration, comorbidity expansion, and medication specificity. Remediation was applied, the Korvin Merrow Brainstorm was reuploaded, AutoQC passed 51/51, and Stacey S approved the Brainstorm.

World setup:

- Multi-day ED-to-inpatient hospitalization.
- World closes on Hospital Day 6 at 18:00 during discharge planning.
- Patient is clinically improved but not clearly back to baseline.
- Persistent concerns include weakness, intermittent cognitive concerns, borderline BP, renal recovery, medication changes, steroid timeline uncertainty, and safe discharge planning.

Patient seed:

- 62-year-old male.
- Long-standing type 2 diabetes mellitus.
- Hypertension.
- CKD stage 3.
- HFrEF and CAD history.
- Hyperlipidemia.
- Anemia of CKD.
- Osteoporosis/osteopenia from chronic steroid exposure.
- Obstructive sleep apnea.
- Diabetic peripheral neuropathy.
- Polypharmacy with a specific approved medication list.
- Polymyalgia rheumatica previously treated with chronic prednisone and recent tapering.
- Lives at home with spouse/family.
- Baseline: independent ADLs, ambulates without major assistance, manages some medications with family support.

Approved compact medication list:

- Sacubitril/valsartan 24/26 mg BID.
- Carvedilol 12.5 mg BID.
- Furosemide 40 mg daily.
- Spironolactone 25 mg daily.
- Empagliflozin 10 mg daily.
- Aspirin 81 mg daily.
- Atorvastatin 40 mg nightly.
- Metformin ER 500 mg BID.
- Insulin glargine 18 units nightly.
- Prednisone with inconsistent documented taper/dose.
- Alendronate 70 mg weekly.
- Calcium/vitamin D daily.
- Ferrous sulfate 325 mg every other day.
- Gabapentin 300 mg nightly.

## Locked Primary Frictions

1. Nephrology vs Cardiology

- Nephrology prioritizes renal recovery, avoiding recurrent AKI, preventing hypotension, and holding unsafe medications during AKI/hypotension.
- Cardiology prioritizes HFrEF/CAD guideline-directed therapy, avoiding unnecessary withdrawal of protective therapy, preventing HF decompensation, and reducing readmission risk.
- Core tension: immediate renal/hemodynamic safety vs long-term cardiovascular optimization.

2. Family vs Inpatient Medicine

- Family knows baseline function and cognition and worries the patient is weaker, intermittently confused, and unsafe with a changed medication plan.
- Inpatient team sees improved vitals, controlled infection, improving renal function, and acute stabilization.
- Core tension: medically stable on paper vs functionally safe in the real world.

3. Endocrinology vs Primary Team

- ED/inpatient medicine appropriately treated suspected sepsis and wants to avoid unnecessary prolonged steroids once acute infection appears improved.
- Endocrinology recognizes chronic prednisone exposure for PMR, unclear taper history, persistent weakness, borderline hypotension, and overlapping symptoms.
- Core tension: risk of premature steroid withdrawal vs risk of unnecessary steroid continuation.
- Guardrail: this is a risk-interpretation disagreement, not "Endocrinology finds the missed diagnosis."
- Documentation is evidence for the steroid trap, not a friction participant.

## Locked World-Level Traps

1. Steroid timeline/source-of-truth trap

- Older rheumatology documentation shows chronic prednisone.
- Later outpatient plan recommended tapering.
- Outpatient med list was not fully updated.
- Admission med rec pulls older information.
- Family is unsure of exact dose.
- Inpatient notes copy forward inconsistent steroid status.
- Correct reasoning reconstructs whether recent steroid exposure creates adrenal suppression risk relevant to management and discharge.

2. HF-AKI medication reconciliation and time-sensitive consultant trap

- Sacubitril/valsartan, furosemide, spironolactone, empagliflozin, carvedilol, and other HFrEF/CAD therapies are held or adjusted during AKI/hypotension.
- Early "hold" recommendations may persist visually after renal function and BP evolve.
- Correct reasoning avoids both premature restart and inappropriate long-term omission.

3. Buried functional/cognitive status trap

- Physician notes say clinically improved.
- Nursing, PT, and family documentation carry weakness, intermittent confusion, assistance needs, and medication-management concerns.
- Correct reasoning does not equate improved labs with safe discharge.

4. Sepsis anchoring after partial improvement trap

- Early ED/admission documents correctly emphasize UTI/sepsis.
- Later records show infection improvement but persistent weakness, borderline BP, evolving renal/electrolyte issues, medication changes, functional decline, and steroid timeline questions.
- Correct reasoning recognizes sepsis was real/reasonable initially while avoiding premature closure.

5. Discharge plan source-hierarchy trap

- Draft discharge planning can imply straightforward home discharge.
- Important qualifiers live in medication plan, consultant recommendations, PT/nursing notes, and family communication.
- Correct reasoning understands a reassuring discharge artifact is not the whole source of truth.

## Approved Rough Task Concepts

Use these as rough concepts only. Do not write final prompts, golden responses, or grader guidance.

1. Discharge medication reconciliation / medication safety review
   - Current tracker mapping: P0 Discharge Medication Reconciliation.
   - Requester: hospitalist.
   - Anchor: Hospital Day 7, after world close.
   - Competency: medication action reasoning.

2. Hospital discharge summary generation
   - Current tracker mapping: P0 Hospital Discharge Summary Generation.
   - Requester: attending physician.
   - Anchor: Hospital Day 7, after world close.
   - Competency: narrative fidelity and temporal sequence.

3. Transition-of-care / discharge readiness plan
   - Current tracker mapping: P0 Discharge Planning Documentation.
   - Requester: case manager and hospital medicine team.
   - Anchor: Hospital Day 7, after world close.
   - Competency: disposition safety.

4. Post-hospital follow-up assessment note
   - Current tracker mapping: P0 Transitional Care Management Documentation (TCM).
   - Requester: primary care physician.
   - Anchor: 7 days after discharge.
   - Competency: reassessment after transition.

5. Consultant recommendation synthesis / care coordination note
   - Current tracker mapping: P1 Interdisciplinary Care Plan Development and Documentation.
   - Requester: hospital care team.
   - Anchor: Hospital Day 7, after world close.
   - Competency: consultant-priority synthesis.

6. Readmission risk / patient safety review
   - Current tracker mapping: P0 Patient Risk Stratification Assessment.
   - Requester: quality and patient safety team.
   - Anchor: 30 days after discharge.
   - Competency: retrospective safety analysis.

Reserve only:

- Future ED reassessment after return visit. Do not use unless Alexander later chooses it.

## Current Reviewer Risks

These are World Spec preparation risks, not authorization to change Brainstorm:

- World Spec patient name must be unmistakably synthetic under AutoQC v6.3 Check 2.2. Reviewer SEND BACK requested replacing the prior common name with Korvin Merrow.
- World Spec task suite must use 3-5 distinct catalog workflows under Check 2.107; current rough mapping has more distinct workflows than allowed.
- Typical clinical/medical director worlds should include both clinical and healthcare administration work products where appropriate under Check 2.108.
- Decision Friction Table is required if the world depends on 2+ specialty conflicts or embedded diagnostic conflicts under Check 2.14.
- Source-of-truth hierarchy must be documented when authority traps are present under Check 2.65.
- Fact-to-file traceability is a hard requirement under Checks 2.18, 2.48, 2.49, and 2.60.
- Temporal architecture is a blocker gate under Check 2.41.
- Prompts must not telegraph traps under Check 2.31.
- Task independence is a blocker under Check 2.40.
- Failure Design tables need at least 5 grounded traps per task under Check 2.34, without inappropriate duplication under Check 2.91.

## Governance Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/governance-package-v1.md`

Clarification artifact: `worlds/korvin-merrow/world-spec-prep/reviews/governance-package-clarification.md`

Status: RATIFIED.

Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/governance-package-ratification.md`

Care team roster:

- Hospitalist Service.
- Cardiology.
- Nephrology.
- Endocrinology.
- Physical Therapy.
- Occupational Therapy.
- Case Management.
- Social Work.
- Patient.
- Family/Caregiver.
- Primary Care Physician.

Authority hierarchy: attending hospitalist > consulting attending specialists > PT/OT functional assessments > Case Management / Social Work > family reports > patient recollection.

Master source-of-truth hierarchy for clinical facts: attending documentation > verified medication reconciliation > pharmacy history > consultant documentation > primary care documentation > family report > patient recollection.

Preserve prednisone-specific hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.

Hierarchy clarification: Authority Hierarchy is used for role-based governance, disposition interpretation, functional/discharge evidence, stakeholder input, and decision ownership. Source-of-Truth Hierarchy is used for factual conflict resolution. If both appear relevant, the World Spec must state which hierarchy governs the task or trap.

Operational rule: authority hierarchy resolves factual/documentation conflicts. It does not resolve clinical recommendation disagreements. Consultant disagreements must be reconciled through evidence synthesis, timing, trends, patient status, and discharge safety.

Confirmed conditions: HFrEF, CKD Stage 3, Type 2 Diabetes, CAD, Hypertension, Hyperlipidemia, OSA, Diabetic Neuropathy, PMR, Anemia of CKD, Osteoporosis/Osteopenia.

Presumed / active questions: current infection source, steroid contribution, adrenal suppression contribution, degree of dehydration, relative medication contribution, discharge readiness.

Steroid-related bone disease clarification: confirmed osteoporosis/osteopenia reflects cumulative chronic steroid exposure but does not prove current symptoms are primarily caused by adrenal suppression. Current adrenal/steroid contribution remains an active interpretive question.

Final friction table: Cardiology vs Nephrology for medication restart timing; Family vs Primary Team for discharge readiness; Endocrinology vs Primary Team for steroid interpretation and risk.

Administrative deliverable decision: yes. At least one future task should involve transition of care, discharge planning, care coordination, or follow-up planning.

Workflow umbrella: Acute Hospital Management, with subdomains of diagnosis, medication management, consultant synthesis, functional assessment, and disposition planning. Exact future task workflow lines must still use official tracker names.

Deferred task-architecture watch items: AutoQC 2.107 workflow count and 2.108 administrative deliverable must be resolved during task architecture, not inside Governance Package v1.

Completed Architecture Layers: Brainstorm APPROVED; Temporal Architecture LOCKED; Clinical Story Skeleton RATIFIED; Identity Package LOCKED; Governance Package RATIFIED.

Physician Architecture Layer Status: COMPLETE.

## Key Milestones Calendar Skeleton v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/key-milestones-calendar-skeleton-v1.md`

Status: LOCKED.

Canonical anchors:

- Approximate decline begins: 04/27/2026.
- Final pre-admission week begins: 05/11/2026.
- Day before presentation: 05/17/2026.
- Admission / HD1: 05/18/2026.
- HD2: 05/19/2026.
- HD3: 05/20/2026.
- HD4: 05/21/2026.
- HD5: 05/22/2026.
- HD6: 05/23/2026.
- World snapshot / world close: 05/23/2026 18:00.
- Discharge anchor: 05/24/2026.
- +7 day anchor: 05/31/2026.
- +30 day anchor: 06/23/2026.

This is a date framework only. It is not a World Spec draft, final milestone table, task architecture, or file inventory.

Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/key-milestones-calendar-ratification.md`

Locked doctrine: +7 and +30 anchors are measured from discharge anchor 05/24/2026, not from HD6 world close.

## Baseline Anchor Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/baseline-anchor-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/baseline-anchor-ratification.md`

Status: LOCKED.

Locked baseline anchors:

- Baseline creatinine.
- Baseline eGFR.
- Baseline hemoglobin.
- Baseline A1c.
- Dry weight approximately 97 kg.
- Baseline mobility.
- Baseline cognition.
- Baseline medication-management ability.
- Baseline home support.

Physician sign-off completed. Baseline functional status remains part of the approved baseline framework through mobility, cognition, medication-management ability, and home support.

Baseline blood pressure may be considered as a future candidate anchor during construction only. Do not create a numeric baseline blood pressure value at this stage.

This package does not create admission labs, hospital-course lab trends, file inventory, task architecture, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic files.

## Clinical Story Timeline Package v1

Artifact: `worlds/korvin-merrow/world-spec-prep/locked/clinical-story-timeline-package-v1.md`

Ratification: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-timeline-ratification.md`

Status: LOCKED.

Purpose: canonical story-evolution framework from pre-admission decline through HD1-HD6, discharge, +7, and +30 anchors.

This package preserves mixed physiology, multi-factorial near-fall, medically improving but operationally dangerous discharge tension, functional-decline failure target, prednisone source-of-truth ambiguity, and friction/trap separation.

It does not create labs, vitals, medication doses, medication schedules, hospital notes, file inventory, task architecture, World Spec prose, prompts, goldens, grader guidance, templates, reference files, or synthetic documents.

Carry-forward file-construction note: preserve the distinction between Trap #3, where important functional/cognitive evidence exists but is easy to miss, and Trap #5, where a visible discharge/source-hierarchy artifact appears sufficient if trusted alone.

## Locked Clinical Story Skeleton v1

Status: ratified after review on 2026-05-31.

Review artifact: `worlds/korvin-merrow/world-spec-prep/reviews/clinical-story-skeleton-review.md`

Decision log: `worlds/korvin-merrow/world-spec-prep/decision-logs/physician-decision-log-02.md`

Ratification artifact: `worlds/korvin-merrow/world-spec-prep/ratifications/clinical-story-skeleton-ratification.md`

Core story:

- Korvin Merrow lives with family and was independent but slowed by chronic illness before a 3-week decline.
- Baseline includes occasional cane use and mild age-related forgetfulness only.
- PMR/prednisone history includes several-year PMR, chronic prednisone exposure, prior flares and taper attempts, and a recent taper with reconstructable source-of-truth inconsistency.
- Decline includes reduced stamina, reduced activity, poor appetite, reduced fluid intake, increasing weakness, increased family dependence, possible urinary symptoms, progressive unsteadiness, and cognitive slowing.
- Escalation includes medication-management mistakes, lightheadedness, near-fall, and family recognition of meaningful deviation from baseline.
- ED presentation includes suspected urinary-source infection, dehydration, AKI risk, altered baseline mental status, functional decline, and clinically reasonable sepsis-oriented management.
- Infection is a contributor, not the entire explanation.
- Hospital course: HD1 stabilization; HD2 partial improvement and consultant involvement begins; HD3 PT/OT identifies functional concerns; HD4 consultant tensions and steroid-history inconsistency recognized; HD5 disposition concerns dominate; HD6 medically improved but discharge remains debatable.
- Discharge state: infection, AKI, hemodynamics, mental status, and oral intake improve, but functional reserve, medication restart strategy, steroid interpretation, family concern, and disposition risk remain unresolved.
- Primary failure target: disposition safety, functional decline recognition, and discharge-readiness reasoning.
- Near-fall is multi-factorial, not a single-cause clue.

Ratified governance/story-logic guardrails:

- Endocrine friction label is Endocrinology vs Primary Team.
- Do not use Endocrinology vs Documentation.
- Prednisone Source-of-Truth Hierarchy: rheumatology attending recommendation > verified medication reconciliation > pharmacy / refill history > family report > patient recollection.
- Family vs Primary Team is balanced: family concern is defensible, and discharge is clinically defensible from the primary team's perspective because infection, AKI, mental status, and oral intake are improving and follow-up is available.
- Near-fall remains intentionally multi-factorial with no single intended explanation.

## Locked Identity Package v1

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

Consistency:

- Age 62 is consistent with DOB for a 2026 encounter after 2026-02-18.
- BMI 30.6 is consistent with 97 kg and 178 cm.
- Later calendar skeleton must preserve age-62 consistency unless Alexander explicitly reopens DOB or age.

Identity review addendum:

- Claude hostile-review observations are carry-forward implementation notes only.
- Treat lisinopril cough as ACE-inhibitor intolerance during World Spec construction.
- Later medication history should coherently explain current ARNI therapy in relation to prior ACE-inhibitor use/intolerance.
- Baseline function, baseline creatinine, dry weight, and similar baseline anchors should be explicitly placed during Patient Profile / Clinical History design.
- Do not reopen Identity Package v1.

## Current State

Brainstorm approved. Clinical Story Skeleton v1 ratified. Identity Package v1 locked. Governance Package v1 ratified. Physician Architecture Layer complete. Key Milestones Calendar Skeleton v1 locked. Baseline Anchor Package v1 locked. Clinical Story Timeline Package v1 locked. Do not start World Spec drafting.

Task Architecture Interview v1 is in candidate review at `worlds/korvin-merrow/world-spec-prep/candidate-review/task-architecture-interview-v1.md`. It is interview-only and does not create final tasks, task prompts, expected outputs, file inventory, World Spec sections, reference templates, or synthetic files.

Completed:

1. Korvin Merrow synthetic patient identity.
2. `World Type: Typical Clinical World`.
3. Approved 10+ comorbidity burden.
4. Approved compact medication list with drug names/doses.
5. Regenerated `worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx`.
6. Reuploaded revised Brainstorm to RL Studio.
7. AutoQC passed 51/51.
8. Brainstorm approved by Stacey S.
9. Clinical Story Skeleton v1 locked and reviewed.
10. Clinical Story Skeleton v1 ratified after Claude hostile review minor findings.
11. Identity Package v1 locked.
12. Identity Package review addendum recorded without reopening identity values.
13. Governance Package v1 candidate lock recorded.
14. Governance Package v1 clarification recorded.
15. Governance Package v1 ratified.
16. Physician Architecture Layer completed.
17. Key Milestones Calendar Skeleton v1 locked.
18. Baseline Anchor Package v1 locked after physician review.
19. Clinical Story Timeline Package v1 created and locked.
20. Task Architecture Interview v1 created for candidate review.

Still pending before World Spec drafting:

1. Official Claude World Spec session.
2. Physician review of Task Architecture Interview v1.
3. Alexander authorization to draft the World Spec.

## Claude Use Rules

Claude may:

- organize physician-provided decisions;
- critique against AutoQC and reviewer-risk criteria;
- help prepare decision checklists and consistency audits;
- later help with World Spec drafting only after explicit Alexander approval.

Claude must not:

- invent scenario concept, traps, task ideas, diagnoses, labs, dates, medications, doses, patient identity, MRN, provider names, file inventory, final prompts, golden responses, grader guidance, or failure analysis;
- treat World Spec preparation risks as permission to revise Brainstorm;
- imply World Spec drafting is authorized before Alexander explicitly authorizes it.
