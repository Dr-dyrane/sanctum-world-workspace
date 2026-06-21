| Field | Value |
|---|---|
| Codename | HEALTHCARE_CardiorenalTransition_Marva |
| Title | Navigating Transition Readiness and Discharge Safety in Decompensated Heart Failure with Cardiorenal and Respiratory Complexity |
| Patient | Marva Lydell (fictional) |
| World Type | Typical Clinical |
| Setting | Inpatient hospital medicine with post-discharge administrative and transition encounters |
| Workflows | Claims Appeal, Medication Reconciliation, Utilization Review, Transition Documentation, Acute Care Discharge Planning, Specialist Referral, Root Cause Analysis, Quality Abstraction, Clinical Documentation Query |
| Specialty | Hospital Medicine |
| Total Tasks | 10 |
| Project | Project Sanctum |
| Version | 1.0 |
| Document date | 06/27/2025 |

# 1. Clinical Scenario

## 1.1 Big Picture Summary

Marva Lydell is a 72-year-old woman with heart failure with preserved ejection fraction, atrial fibrillation on anticoagulation, CKD stage 3b to 4, COPD, and obstructive sleep apnea who is admitted for acute decompensated heart failure with hypoxemia and a cardiorenal acute kidney injury and who is medically improving but operationally unsafe to transition home at the world snapshot. Over a 7-day admission she is diuresed, her oxygenation is reassessed, cardiology and nephrology balance decongestion against kidney recovery and potassium safety, respiratory therapy testing documents that she desaturates with exertion even though her resting saturation looks acceptable, and physical and occupational therapy find she cannot yet manage her stairs or her own oxygen logistics. Congestion and creatinine improve while the transition plan stays unsafe: portable oxygen is not reliably delivered or teach-backed, held cardiorenal and diabetes medications are a restart judgment rather than an automatic resume, her interior stairs and full-time-working daughter make home support partial, and payer, skilled-nursing, and equipment issues are all active.

The world carries ten independent post-snapshot tasks spanning payer appeals, discharge medication reconciliation, a utilization determination, a transition-note peer review, post-acute coordination, a specialist referral handoff, a safety corrective-action review, quality abstraction, and a documentation-integrity query response. The integration anchor is Task 1, the oxygen and skilled-nursing denial appeal, which draws the widest synthesis across resting versus exertional oxygen, functional tolerance, equipment delivery, and home support. File-plan composition: 32 essential world-level files plus 11 essential task-level files plus 4 supplementary world-level files, for 47 unique files supporting the ten tasks.

## 1.2 Patient Profile

| Field | Value |
|---|---|
| Name / DOB / Age / Sex | Marva Lydell / 04/22/1953 / 72 / Female |
| Race / Height / Weight / BMI | Black / 160 cm (5 ft 3 in) / 88 kg (194 lb) at dry weight / 34.4 (class I obesity) |
| Code Status | Full Code, confirmed on admission |
| Marital / Dependents | Widowed; lives alone in a two-story home with interior stairs and a bedroom on the upper floor; adult daughter lives nearby but works full time |
| Additional demographics | Retired school cafeteria worker; Medicare primary with a Medicare Advantage plan; home oxygen and home CPAP at baseline; limited mobility at baseline |
| Allergies / MRN | Lisinopril and ACE inhibitors, documented angioedema (she is maintained on an angiotensin receptor blocker instead) / ML-7782304 |
| Pre-existing conditions | Heart failure with preserved ejection fraction; atrial fibrillation on anticoagulation; coronary artery disease with prior percutaneous coronary intervention; CKD stage 3b to 4; COPD; obstructive sleep apnea on CPAP; type 2 diabetes with peripheral neuropathy; hypertension; obesity; anemia of chronic kidney disease; vitamin D deficiency; hypothyroidism; gastroesophageal reflux; chronic constipation |
| Active problem list | Acute decompensated heart failure with preserved ejection fraction, improving with diuresis; acute kidney injury on CKD stage 3b to 4, improving; hypoxemia with exertional desaturation, resting saturation acceptable; atrial fibrillation, rate-controlled, anticoagulated; held cardiorenal and diabetes oral agents pending renal recovery; deconditioning with an unsafe home-transition picture |
| Baseline clinical anchors | Outpatient baseline creatinine 1.7 mg/dL, eGFR about 30 (CKD 3b to 4); baseline hemoglobin about 10.0 (anemia of CKD); HbA1c 7.8 percent; dry weight about 88 kg; home oxygen 2 L per minute nocturnal and with exertion at baseline; ambulates indoors with a cane and limited endurance at baseline. These are comparators, not admission or discharge values, and separate chronic disease from the acute episode |

### Home medication list (pre-admission baseline, with inpatient status)

| # | Medication | Dose | Route | Frequency | Indication | Inpatient status |
|---|---|---|---|---|---|---|
| 1 | Empagliflozin | 10 mg | Oral | Daily | HFpEF, CKD, diabetes | Held on admission, acute illness and AKI |
| 2 | Spironolactone | 25 mg | Oral | Daily | HFpEF, mineralocorticoid antagonist | Held on admission, AKI and potassium |
| 3 | Torsemide | 20 mg | Oral | Daily | Heart failure volume | Continued, converted to IV then back, dose-adjusted |
| 4 | Metoprolol succinate | 100 mg | Oral | Daily | Atrial fibrillation rate, CAD | Continued |
| 5 | Losartan | 50 mg | Oral | Daily | Hypertension (ACE intolerant) | Held on admission for AKI |
| 6 | Apixaban | 5 mg | Oral | Twice daily | Atrial fibrillation anticoagulation | Continued, renal dose reviewed |
| 7 | Aspirin | 81 mg | Oral | Daily | CAD secondary prevention | Continued |
| 8 | Metformin | 1000 mg | Oral | Twice daily | Type 2 diabetes | Held on admission, AKI |
| 9 | Insulin glargine | 24 units | Subcutaneous | Nightly | Type 2 diabetes, basal | Continued, intake-adjusted |
| 10 | Insulin aspart | Sliding scale | Subcutaneous | With meals | Type 2 diabetes, prandial | Continued per inpatient sliding scale |
| 11 | Atorvastatin | 40 mg | Oral | Nightly | CAD, dyslipidemia | Continued |
| 12 | Tiotropium | 18 mcg | Inhaled | Daily | COPD maintenance | Continued |
| 13 | Albuterol | 90 mcg | Inhaled | As needed | COPD rescue | Continued |
| 14 | Gabapentin | 300 mg | Oral | Three times daily | Diabetic peripheral neuropathy | Continued, renally dose-checked |
| 15 | Ferrous sulfate | 325 mg | Oral | Daily | Anemia of CKD | Continued |
| 16 | Cholecalciferol | 2000 units | Oral | Daily | Vitamin D deficiency | Continued |
| 17 | Levothyroxine | 75 mcg | Oral | Daily | Hypothyroidism | Continued |
| 18 | Pantoprazole | 40 mg | Oral | Daily | Gastroesophageal reflux | Continued |
| 19 | Senna | 8.6 mg | Oral | Nightly as needed | Chronic constipation | Continued |
| 20 | Home oxygen | 2 L/min | Nasal cannula | Nocturnal and with exertion | Chronic hypoxemia | Continued, titration under review |
| 21 | CPAP | Device | Mask | Nightly | Obstructive sleep apnea | Continued |

### Care Team Roster

| Provider | Role / Service | Appears in |
|---|---|---|
| Dr. Marcus Thorne, MD | Hospitalist attending, attending of record | World notes, Tasks 1, 2, 4, 6, 7 |
| Dr. Aileen Costa, MD | Hospital medicine resident, PGY-2 | World progress notes |
| Dr. Sunil Varma, MD | Cardiology | HFpEF consult, Tasks 4, 6 |
| Dr. Beatrix Lund, MD | Nephrology | AKI and CKD consult, Tasks 2, 4, 6 |
| Dr. Idris Quayle, MD | Pulmonology | COPD and oxygen consult, Tasks 1, 10 |
| Tomas Reynel, RRT | Respiratory therapy | Oxygen titration and walk test, Tasks 1, 7 |
| Wendola Pryce, PT, DPT | Physical therapy | Mobility and stairs evaluation, Tasks 1, 4, 7, 8 |
| Garrick Olom, OT | Occupational therapy | ADL and oxygen-logistics teach-back, Tasks 1, 4, 7, 8 |
| Priya Anand, PharmD | Inpatient pharmacy | Renal dosing and anticoagulation, Tasks 2, 5 |
| Delphine Carrow, RN, CCM | Case management | Disposition, DME, payer, Tasks 1, 5, 7 |
| Hollis Bramwell, RN, CCDS | Clinical documentation integrity | Task 10 |
| Noreen Vassal, RN | Quality abstraction | Task 9 |
| Dr. Edmund Hale, MD | Physician advisor, utilization review | Task 3 |
| Dr. Coralie Naismith, MD | Patient safety officer | Task 8 |
| Dr. Sterling Ovid, MD | Medicare Advantage medical director, external | Tasks 1, 7 |
| Tanielle Lydell | Daughter and caregiver | Family and discharge-planning notes |

### Decision Friction Table

| Friction | Party A position | Party B position | Anchor / resolution |
|---|---|---|---|
| Transition disposition (central) | Medicare Advantage medical director (Dr. Ovid): improving resting vitals and diuresis support home with home health | Treating team (Dr. Thorne, case management): unsafe without reliable portable oxygen, functional tolerance, and post-acute support | Resolves toward continued skilled-level need; Tasks 1, 3, 7 |
| Cardiology versus nephrology | Cardiology (Dr. Varma): decongest, protect the heart, restart guideline therapy | Nephrology (Dr. Lund): protect kidney recovery and potassium, time the restarts carefully | Both defensible and incomplete; restart is a judgment, not automatic; Tasks 2, 4, 6 |
| Oxygen need versus equipment status | Respiratory therapy and pulmonology (Reynel, Dr. Quayle): exertional desaturation needs reliable portable oxygen | Case management and DME vendor: equipment described as arranged | Formal testing and delivery status govern; Tasks 1, 5 |
| Patient and family versus therapy | Daughter (Tanielle): wants mother home, offers help around work | PT and OT (Pryce, Olom): stairs, oxygen logistics, fatigue, and medication complexity exceed that support | Documented functional limits govern; Tasks 4, 5, 7 |
| Outside list versus inpatient chart | Outside pharmacy and SNF intake: carry a stale renal dose or a duplicate anticoagulant | Inpatient record (MAR, pharmacy): active orders reflect current renal function | Active record governs over outside list; Tasks 2, 5 |
| Quality reviewer versus clinician author | Administrative review (abstraction, CDI): a clean, fully closed transition | Treating author: leave oxygen, volume, and follow-up ownership explicitly open | Treating record governs; Tasks 8, 9, 10 |

### Data Hierarchy Note

When sources conflict, authority runs highest first: the active medication administration record and signed orders for what was given and ordered; then the attending or specialist consult note for clinical rationale; then the floor or progress note; then any outside, intake, or patient-reported information. Two conflicts resolve by this order specifically: oxygen adequacy follows the formal respiratory therapy titration and six-minute walk test over a reassuring resting saturation in routine vitals, and medication readiness follows the nephrology and cardiology restart judgment against current renal function over any outside or skilled-nursing intake list that carries a stale dose or a duplicate agent.

## 1.3 Clinical History and Context

Marva Lydell is a 72-year-old woman with a long history of heart failure with preserved ejection fraction, atrial fibrillation for which she takes an oral anticoagulant, coronary artery disease with a prior percutaneous coronary intervention, and CKD stage 3b to 4 with a baseline estimated GFR near 30 and an anemia of chronic kidney disease. She also carries COPD and obstructive sleep apnea, for which she uses home oxygen and CPAP, type 2 diabetes with peripheral neuropathy, hypertension managed with an angiotensin receptor blocker because she had angioedema on an ACE inhibitor, obesity, and the quieter background of hypothyroidism, reflux, and chronic constipation. She lives alone in a two-story home with her bedroom upstairs. Her late husband had been her main support; her adult daughter, Tanielle, lives nearby but works full time, so day-to-day help at home is real but incomplete. At baseline she walks indoors with a cane, tires quickly, and already uses low-flow oxygen at night and with exertion.

Over the week before admission she gained weight, her legs swelled, she became more short of breath climbing her stairs, and she slept sitting up. She presented to the emergency department on June 13, 2025 with dyspnea, lower-extremity edema, a weight about 7 kg above her dry weight, a resting oxygen saturation of 88 percent on room air, and a creatinine of 2.6 against her CKD baseline of about 1.7, consistent with a cardiorenal acute kidney injury on chronic disease. She was admitted to hospital medicine under Dr. Thorne for acute decompensated heart failure with hypoxemia. Intravenous diuresis was started, supplemental oxygen was titrated, and her empagliflozin, spironolactone, losartan, and metformin were held for the acute illness and kidney injury while her torsemide was continued and adjusted, her rate control and anticoagulation were continued, and her insulin, inhalers, statin, and the rest of her chronic agents were continued with renal dose checks.

On hospital day two, cardiology under Dr. Varma confirmed preserved ejection fraction with grade II diastolic dysfunction on echocardiography and framed the admission as a volume problem to decongest while protecting the kidneys. On hospital day three, nephrology under Dr. Lund attributed the kidney injury to cardiorenal physiology and diuresis, kept the renin-angiotensin agent and the mineralocorticoid antagonist held until potassium and creatinine settled, and explicitly framed restart timing as a careful outpatient judgment rather than an automatic resume; telemetry over these days recorded rate-controlled atrial fibrillation. On hospital day four, pulmonology under Dr. Quayle addressed the COPD contribution to dyspnea and asked respiratory therapy to characterize her oxygen needs. On hospital day five, respiratory therapy under Mr. Reynel performed an oxygen titration and a six-minute walk test that showed an acceptable resting saturation but a clear desaturation into the low 80s with ambulation that corrected only with portable oxygen, and physical and occupational therapy documented that she could not yet manage her stairs or reliably set up and carry her own oxygen, with teach-back not achieved. On hospital day six, case management began screening disposition with the plan and the durable medical equipment vendor, and the family meeting recorded the daughter's willingness within the limits of her work schedule. By the evening of hospital day seven her weight was down about 5 kg, her creatinine had improved to 1.9, and her resting saturation sat at an acceptable level at rest, but she still desaturated with exertion, portable oxygen was not yet reliably delivered or teach-backed, the held cardiorenal and diabetes agents remained a deliberate restart judgment, and her stairs and caregiver schedule left the home plan unsafe.

The world snapshot freezes the chart at 18:00 on June 19, 2025, hospital day seven, at this medically improving but operationally unsafe point. Every task in the world is an independent encounter that occurs strictly after this snapshot.

Procedural history is intentionally limited for this admission: there is no new cardiac catheterization, no intubation, no dialysis, and no new device this stay. The prior percutaneous coronary intervention is historical and stable, and her atrial fibrillation has been managed medically with rate control and anticoagulation rather than ablation.

## 1.4 Key Milestones (Compressed Timeline)

| Date | Event |
|---|---|
| 05/30/2025 | Outpatient cardiology and primary care summary, baseline creatinine 1.7 and eGFR about 30, baseline hemoglobin about 10.0, dry weight about 88 kg, home oxygen 2 L nocturnal and exertional, baseline functional status (quiet baselines) |
| 06/01/2025 | Prior outpatient echocardiogram, preserved ejection fraction, grade II diastolic dysfunction (baseline comparator) |
| 06/13/2025 | ED presentation and admission, hospital day 1; weight 7 kg over dry, resting SpO2 88 percent, creatinine 2.6; IV diuresis, oxygen, medication holds |
| 06/14/2025 | Cardiology consult and inpatient echocardiogram, hospital day 2; HFpEF confirmed |
| 06/15/2025 | Nephrology consult, anticoagulation renal-dosing note, telemetry atrial fibrillation, hospital day 3 |
| 06/16/2025 | Pulmonology consult, endocrine glycemic note, hospital day 4 |
| 06/17/2025 | Respiratory therapy oxygen titration and six-minute walk test (exertional desaturation), PT and OT evaluations, hospital day 5 |
| 06/18/2025 | Case management screen, family communication note, social work note, nursing oxygen-use flowsheet, hospital day 6 |
| 06/19/2025 18:00 | World snapshot, hospital day 7, chart frozen, improving but operationally unsafe |
| 06/20/2025 08:00 | External oxygen and SNF denial letter issued |
| 06/20/2025 09:00 | Task 1, oxygen and skilled-nursing denial appeal |
| 06/20/2025 10:00 | Task 2, discharge medication reconciliation |
| 06/20/2025 14:00 | Task 3, continued-stay determination |
| 06/21/2025 08:30 | Task 4, transition note peer review |
| 06/21/2025 13:00 | Task 5, post-acute coordination plan |
| 06/22/2025 11:00 | Task 6, cardiorenal follow-up referral handoff |
| 06/24/2025 10:00 | Task 7, home health versus skilled-nursing appeal |
| 06/25/2025 09:00 | Task 8, post-readmission corrective-action safety review |
| 06/26/2025 09:00 | Task 9, heart-failure transition quality abstraction |
| 06/26/2025 12:00 | Task 10, documentation-integrity query response |

## 1.5 Clinical Complexity Overview

This world is hard for an AI agent because almost every task offers a locally reasonable wrong answer that can only be rejected by synthesizing across documents and respecting a documented source-of-truth order. The heart failure and the kidney injury are genuinely improving, which makes the single most available inference, that the patient is therefore ready to go home, the wrong one. The operational picture that contradicts it is spread across the respiratory therapy walk test, physical and occupational therapy, case management, the durable medical equipment status, and the family note, with no single document stating the conclusion. The central buried finding is that an acceptable resting oxygen saturation coexists with a clear exertional desaturation, so a model that reads routine vitals alone will conclude the oxygen problem is solved.

Three further dimensions interact. First, medication readiness under renal recovery: a baseline GFR near 30 with an improving acute injury makes the held cardiorenal and diabetes agents a judgment about when and whether to restart rather than an automatic resume, and an outside or skilled-nursing intake list can carry a stale renal dose or a duplicate anticoagulant that conflicts with the active record. Second, equipment and home reality: case management prose can describe oxygen as arranged while the vendor record leaves portable oxygen undelivered or not teach-backed, and the interior stairs and a full-time-working daughter make home support partial in a way that is documented but never summarized. Third, documentation restraint under closure pressure: a quality abstraction worksheet and a documentation-integrity query both reward a clean, fully closed transition, while the treating record leaves oxygen control, volume status, and follow-up ownership legitimately open, so the correct behavior is reasoned restraint rather than capture. The patient's stairs, caregiver schedule, and oxygen logistics are deliberately load-bearing context for the transition tasks without ever being the scored trap themselves. Difficulty distribution across the ten tasks is roughly three harder synthesis or determination tasks, five mid-range forced-judgment tasks, and two lighter but still discriminating tasks.

Terminology note: traps are informational obstacles embedded in the source files that test reasoning through noisy, contradictory, or incomplete data, and they are cataloged in each task's Failure Design. Frictions are conflicts between people or perspectives that the chart presents openly, and they are cataloged in the Decision Friction Table in Section 1.2.

# 2. Task Specifications

Each task is an independent encounter anchored strictly after the 06/19/2025 18:00 snapshot. Draft prompts are written in the requesting clinician's voice, assume chart access, and name a single deliverable without hinting at the traps. Expected outputs name the format, register, length, and the specific clinical anchors a grader verifies. Failure Design lists the highest-yield traps with remediations grounded in dated chart documents. The ten tasks map to ten approved workflows across eight structural categories, with Task 1 as the integration anchor. Every deliverable is physician-produced or physician-supervised.

## Task 1: Oxygen and Skilled-Nursing Denial Appeal

Capability: multi-source synthesis into a binding payer appeal, the world integration anchor.
Workflow: Claims Denial Analysis and Appeal Preparation, requested by the hospitalist attending at case management request.
Anchor: 06/20/2025 at 09:00. Priority: P0. Difficulty: high. Time estimate: 30 to 40 minutes, synthesizing the respiratory therapy, PT, OT, equipment, and home documentation against the denial.

Expected Output: a physician appeal letter rebutting the Medicare Advantage denial of the skilled-nursing stay and the home-oxygen upgrade, with a clear appeal position and clinical rationale. Format: a physician appeal letter. Register: formal physician-to-payer. Length: 500 to 800 words. Correct responses rebut the improving-resting-vitals-equals-home framing by synthesizing the exertional desaturation on the respiratory therapy walk test, the physical and occupational therapy findings on stairs and oxygen logistics, the undelivered portable oxygen, the two-story home, and the work-limited caregiver, and do not over-defer to the payer's authority. Grader anchors: appeal grounded in the exertional desaturation from the formal walk test, not the resting saturation; functional and stairs findings cited; portable-oxygen delivery and teach-back gap stated; home and caregiver limits integrated; the appeal holds the treating position rather than conceding to the denial.

Failure Design

| Key Trap | Remediation |
|---|---|
| Denial frames an acceptable resting saturation as a resolved oxygen need (shared world-level trap; primary here) | Cite the respiratory therapy titration and six-minute walk test showing exertional desaturation corrected only with portable oxygen (06/17; respiratory therapy walk test) |
| Over-deference to payer authority | Hold the treating position; the denial is rebuttable from the chart (denial letter E1-T1) |
| Functional tolerance and stairs omitted | Make the PT and OT findings and the two-story home central (06/17 to 06/18; PT, OT, case management) |
| Portable oxygen treated as in place (shared world-level trap; primary in Task 5) | Cite the undelivered and not-teach-backed portable oxygen (06/17 to 06/18; OT, nursing oxygen flowsheet, case management) |
| Volume improvement read as transition readiness (shared world-level trap; primary in Task 3) | Weigh the unresolved operational items against the improving congestion (06/17 to 06/19; progress notes, weights) |

Task-level files: E1-T1 Oxygen and Skilled-Nursing Denial Letter (external).

Draft Prompt: The plan denied the skilled-nursing stay and the home-oxygen upgrade for Mrs. Lydell and case management asked me to appeal. Draft the appeal for my signature, make the clinical case from her chart for the level of care and the oxygen she actually needs, and keep it tight and clinical.

## Task 2: Discharge Medication Reconciliation

Capability: medication reconciliation against a documented source-of-truth hierarchy under renal recovery.
Workflow: Discharge Medication Reconciliation, requested by the hospitalist attending.
Anchor: 06/20/2025 at 10:00. Priority: P0. Difficulty: medium-high. Time estimate: 25 to 35 minutes, reconciling the home list, the MAR, the renal trend, and the outside list.

Expected Output: a reconciled discharge medication list, one row per drug with a disposition of continue, hold, change, stop, or defer and a short rationale, plus patient-facing instructions. Format: a headed reconciliation note with a disposition-per-medication structure. Register: hospitalist and pharmacist professional. Length: 450 to 700 words. Correct responses reconcile against the active MAR and current renal function rather than the stale outside list, treat the held cardiorenal and diabetes agents (empagliflozin, spironolactone, losartan, metformin) as deliberate deferred-restart judgments tied to renal recovery and follow-up rather than silently resuming or stopping them, keep apixaban at a renally correct dose without antiplatelet-anticoagulant duplication beyond the documented aspirin indication, and continue the noise agents unchanged. Grader anchors: reconciliation follows the active record over the outside list; the four held agents each handled as an explicit deferred restart, not a silent continue or stop; apixaban renally dosed and not duplicated; insulin continued without an invented change; no fabricated doses.

Failure Design

| Key Trap | Remediation |
|---|---|
| Outside list carries a stale renal dose or continues a held agent | Reconcile to the active MAR and current renal function, not the outside list (06/20; outside medication list E1-T2; MAR, renal trend) |
| Held oral agents read as auto-continue or discontinue (shared world-level trap; primary in Task 4) | Treat empagliflozin, spironolactone, losartan, metformin as parameter-gated restart decisions deferred to renal recovery and follow-up (06/13, 06/15; hold orders, nephrology note) |
| Apixaban dosed at the admission renal value or duplicated (shared world-level trap; primary in Task 5) | Dose apixaban to current renal function and avoid anticoagulant duplication beyond the documented aspirin (06/15; anticoagulation note, MAR) |
| Insulin regimen altered without basis | Continue home basal with the inpatient prandial scale de-escalated to the home regimen, no invented change (MAR, endocrine note) |
| Noise agents reconciled as if load-bearing | Continue levothyroxine, pantoprazole, senna unchanged; they are distractors, not the decision (1.2 home meds) |

Task-level files: E1-T2 Outside Pharmacy and Transfer Medication List (external, stale).

Draft Prompt: I am getting Mrs. Lydell ready to leave in the next day or two and I need a clean discharge medication reconciliation. Build it from her chart, give me each medication with what we are doing and a short why, and write the patient instructions in plain language. Flag anything you want me to confirm before I sign.

## Task 3: Continued-Stay Determination

Capability: a binding level-of-care determination on a designed borderline.
Workflow: Utilization Review Concurrent Stay Documentation, requested by the physician advisor.
Anchor: 06/20/2025 at 14:00. Priority: P1. Difficulty: medium. Time estimate: 20 to 30 minutes, applying criteria across the improvement and the unresolved-operational evidence.

Expected Output: a physician-advisor continued-stay determination with an explicit verdict and criteria-based rationale. Format: a physician-advisor continued-stay determination. Register: utilization-review. Length: 350 to 550 words. Correct responses find continued skilled-level need justified because the operational picture (exertional oxygen need, undelivered equipment, unsafe stairs and offloading of oxygen logistics, and partial home support) outweighs the improving congestion and creatinine, and apply criteria to both sides rather than reading improvement alone as readiness. Grader anchors: a binding determination is stated; both the improvement and the unresolved-operational criteria are weighed; the verdict rests on documented function and oxygen testing, not markers alone; no discharge-ready verdict from improvement alone.

Failure Design

| Key Trap | Remediation |
|---|---|
| Improvement read as discharge readiness (shared world-level trap; primary here) | Weigh the unresolved operational criteria against the improving markers (06/17 to 06/19; respiratory therapy walk test, PT, OT, case management) |
| Verdict avoided or hedged | State a binding continued-stay determination (physician-advisor role) |
| One-sided criteria | Apply criteria to both the improvement and the unsafety (full chart) |
| Worksheet treats post-diuresis improvement as readiness | Use the external continued-stay worksheet as the prompt, not the answer (E1-T3) |
| Exertional oxygen treated as resolved (shared world-level trap; primary in Task 1) | Keep the oxygen need open per the respiratory therapy testing (06/17; walk test) |

Task-level files: E1-T3 Continued-Stay Review Worksheet (external).

Draft Prompt: As physician advisor, give me a continued-stay determination on Mrs. Lydell for today. Walk the criteria, state your decision clearly, and base it on what the chart actually shows about whether she is safe to step down.

## Task 4: Transition Note Peer Review

Capability: a physician peer review of Mrs. Lydell's transition care that adjudicates whether the documented decisions met the standard of care, catching two deficiencies a complete signed resident note carries.
Workflow: Peer Review Case Analysis (06/19 approved task categories), requested by the peer review committee. The category is classified P2 in that list; held at P0 here per the locked eight-P0 distribution, for lead reconciliation.
Anchor: 06/21/2025 at 08:30. Priority: P0. Difficulty: high. Time estimate: 25 to 35 minutes, reviewing the signed note against the respiratory, renal, and medication documentation.

Expected Output: a peer-review determination report on Mrs. Lydell's transition care, with a case summary, a standard-of-care analysis, and an outcome classification of appropriate care versus opportunity for improvement. Format: a peer-review determination report. Register: peer review committee. Length: 400 to 650 words. The resident note (E1-T4) is complete and signed, but it clears the patient on oxygen as stable on the home setup and silently resumes the held cardiorenal and diabetes agents at discharge. Correct responses catch the oxygen error against the documented exertional desaturation and portable-oxygen requirement, catch the silent resumption of empagliflozin, spironolactone, losartan, and metformin and keep them as deferred restarts assigned to named owners, flag the volume status and follow-up ownership the note closes that the chart leaves open, note the home sliding-scale insulin de-escalation, and confirm the rest of the note is accurate rather than re-litigating it. Grader anchors: the oxygen clearance flagged and corrected to the exertional-desaturation and portable-oxygen reality; the silent held-agent resumption flagged and corrected to deferred, parameter-gated restarts with owners; the prematurely closed volume and follow-up items reopened; the home sliding-scale insulin de-escalation noted; the accurate remainder confirmed.

Failure Design

| Key Trap | Remediation |
|---|---|
| The signed note silently resumes the held agents and the review lets it stand (shared world-level trap; primary here) | Catch the resumption; keep empagliflozin, spironolactone, losartan, metformin as deferred restarts assigned to nephrology and primary care, not resumed by default (06/13, 06/15; hold orders, nephrology note) |
| The note clears oxygen as adequate on the home setup | Catch it against the documented exertional desaturation and the portable-oxygen requirement (06/17; respiratory therapy walk test, OT) |
| The review accepts the note's closure of a still-open decision | Reopen volume status and follow-up ownership where the chart leaves them open (full chart) |
| Home sliding-scale insulin carried into the discharge regimen | Flag the de-escalation of the inpatient prandial sliding scale to the home regimen the record supports (MAR, endocrine note) |
| The review re-litigates the accurate parts of the note | Confirm the accurate remainder; the review targets the unsafe items, not the whole note (E1-T4 note) |

Task-level files: E1-T4 Signed Resident Transition-of-Care Note (complete and signed; clears oxygen on the home setup and resumes the held agents, the two common errors to catch).

Draft Prompt: My resident signed off on Mrs. Lydell's transition-of-care note and I want a second set of eyes before it goes in the chart. Review it against her record and tell me where it is unsafe or wrong and what it should say instead.

## Task 5: Post-Acute Coordination Plan

Capability: coordination synthesis that surfaces an undelivered-equipment gap and reconciles an outside list.
Workflow: Post-Acute Care Coordination Documentation, requested by the hospitalist attending coordinating with case management.
Anchor: 06/21/2025 at 13:00. Priority: P0. Difficulty: medium-high. Time estimate: 25 to 35 minutes, mapping each transition item to owner, status, and next action across the equipment, intake, and home documentation.

Expected Output: a post-acute coordination handoff, one entry per transition item with owner, status, and next action. Format: a structured coordination handoff. Register: hospitalist and care-coordination. Length: 400 to 650 words. Correct responses surface that portable oxygen is arranged but not delivered and not teach-backed, reconcile the skilled-nursing intake medication list's duplicate anticoagulant or stale renal dose against the active record, keep each unresolved item open with a named owner and next action, and reflect the documented home and caregiver limits. Grader anchors: oxygen equipment marked not-yet-delivered and not teach-backed with an owner; the intake-list duplicate or stale anticoagulant reconciled to the active record, not coordinated forward; each item carries owner, status, and next action; home and caregiver limits reflected; no blanket "arranged" closure.

Failure Design

| Key Trap | Remediation |
|---|---|
| Case-management prose says DME arranged while the vendor status leaves portable oxygen undelivered (shared world-level trap; primary here) | Mark oxygen equipment not-yet-delivered and not teach-backed, with owner and next action (06/17 to 06/18; nursing oxygen flowsheet, OT, vendor worksheet E1-T5) |
| Skilled-nursing intake list carries a duplicate anticoagulant or a stale renal dose (shared world-level trap; primary here) | Reconcile to the active record; do not coordinate a duplicate or stale anticoagulant forward (06/21; intake list E2-T5; MAR, anticoagulation note) |
| Items closed prematurely | Keep each unresolved item open with owner and next action, not a blanket arranged (full chart) |
| Home support overstated (shared world-level trap; primary in Task 7) | Reflect the stairs and the work-limited caregiver in the plan (06/18; family note, PT, OT) |
| Oxygen-logistics teach-back assumed (shared world-level trap; primary in Task 1) | Record that setup and carry teach-back was not achieved (06/17; OT) |

Task-level files: E1-T5 DME Vendor and Coordination Worksheet (external); E2-T5 Skilled-Nursing Intake Medication List (external, duplicate anticoagulant or stale dose).

Draft Prompt: I need to get Mrs. Lydell's post-acute handoff together before she transitions. Put together the coordination summary from her chart, list each piece of the plan with who owns it, where it stands, and what still has to happen, and flag anything that is not actually in place yet.

## Task 6: Cardiorenal Follow-up Referral Handoff

Capability: a full specialist referral letter authored from the chart that routes the open decisions to owners without over-settling the plan.
Workflow: Specialist Referral Letter and Documentation Preparation, requested by the hospitalist attending.
Anchor: 06/22/2025 at 11:00. Priority: P0. Difficulty: medium-high. Time estimate: 25 to 35 minutes, routing the diuretic, renal, potassium, anticoagulation, and restart decisions to the correct owners.

Expected Output: a cardiorenal follow-up referral letter authored in full from the chart that routes the open decisions to cardiology, nephrology, and primary care. Format: a specialist referral letter with a follow-up routing block. Register: referral and handoff. Length: 450 to 700 words. Correct responses route diuretic titration and weight monitoring, renal labs and potassium monitoring, the held-agent restart timing, and the anticoagulation renal-dose recheck to named owners and keep each conditional item explicitly open rather than letting the letter read as a settled plan. Grader anchors: each follow-up item routed to a named owner; the held-agent restarts kept conditional and parameter-gated, not resumed; the anticoagulation renal-dose recheck routed; oxygen reassessment and renal follow-up kept owned and open; the letter does not assert a settled cardiorenal plan.

Failure Design

| Key Trap | Remediation |
|---|---|
| The letter reads as a settled plan (shared world-level trap; primary here) | Keep the handoff a true open routing; do not assert the cardiorenal plan is finalized (06/19; progress note, nephrology note) |
| Held-agent restart routed as a resume (shared world-level trap; primary in Task 4) | Route empagliflozin, spironolactone, losartan, metformin restart timing to nephrology and primary care as conditional, parameter-gated decisions (06/15; nephrology note) |
| Anticoagulation handed off without the renal-dose recheck (shared world-level trap; primary in Task 5) | Route the apixaban renal-dose recheck to the owner and flag any outside duplicate (06/15; anticoagulation note) |
| Volume and diuretic titration omitted | Assign torsemide titration and weight monitoring to a named owner (06/19; progress note, weights) |
| Letter closes a follow-up ownership the chart leaves open | Keep oxygen reassessment and renal follow-up explicitly owned and open (full chart) |

Task-level files: E1-T6 Cardiorenal Follow-up Referral Request (external; the hospitalist's request to refer to cardiology and nephrology, the trigger; the letter is authored in full from the chart).

Draft Prompt: I am sending Mrs. Lydell's cardiorenal follow-up over to her cardiologist and nephrologist. Please write the referral letter from her chart, make sure each follow-up item has a clear owner and where it stands, and do not make anything sound more settled than it is.

## Task 7: Home Health versus Skilled-Nursing Appeal

Capability: multi-source synthesis into a second payer appeal on a different denial basis.
Workflow: Claims Denial Analysis and Appeal Preparation, requested by the hospitalist attending for utilization management.
Anchor: 06/24/2025 at 10:00. Priority: P0. Difficulty: medium-high. Time estimate: 25 to 35 minutes, assembling the functional, oxygen, home, and medication-complexity case.

Expected Output: a physician appeal letter supporting skilled-nursing need against the plan's home-health-is-sufficient position. Format: a physician appeal letter. Register: formal physician-to-payer. Length: 450 to 700 words. Correct responses rebut the home-health-is-enough framing by synthesizing the interior stairs, the portable-oxygen burden, the functional limits, and the medication complexity (the held-agent restart judgment and the renally dosed anticoagulation), and do not over-defer to the payer. Grader anchors: the appeal integrates stairs, oxygen burden, functional limits, and medication complexity as skilled needs; exertional oxygen cited from the walk test; the treating position held against the denial; the home environment and caregiver limits kept central.

Failure Design

| Key Trap | Remediation |
|---|---|
| Denial treats home health as sufficient despite the documented burden (shared world-level trap; primary here) | Rebut by integrating stairs, portable-oxygen burden, functional limits, and medication complexity (06/17 to 06/18; PT, OT, case management, family note) |
| Over-deference to payer authority | Hold the treating position; the denial is rebuttable (denial letter E1-T7) |
| Exertional oxygen omitted (shared world-level trap; primary in Task 1) | Cite the exertional desaturation and portable-oxygen requirement (06/17; respiratory therapy walk test) |
| Medication complexity understated | Cite the held-agent restart judgment and the renally dosed anticoagulation as skilled needs (06/15; nephrology, anticoagulation notes) |
| Home environment softened | Keep the two-story home and the work-limited caregiver central (06/18; family note, case management) |

Task-level files: E1-T7 Home-Health-Sufficient Denial Letter (external).

Draft Prompt: The plan came back saying home health is enough for Mrs. Lydell instead of a skilled-nursing stay, and UM asked me to push back. Draft the appeal for my signature and make the case from her chart for why home health does not cover what she needs.

## Task 8: Post-Readmission Corrective-Action Safety Review

Capability: investigation with a system-versus-individual attribution judgment.
Workflow: Corrective Action Plan (CAP) Development and Tracking, requested by the patient safety officer.
Anchor: 06/25/2025 at 09:00. Priority: P1. Difficulty: medium-low. Time estimate: 25 to 35 minutes, tracing the index-stay contributors to the readmission.

Expected Output: a corrective-action plan after a heart-failure readmission, with a root-cause attribution and tracked corrective actions, each with an owner and a measure. Format: a structured corrective-action plan. Register: patient-safety and quality. Length: 450 to 700 words. Correct responses attribute the bounceback to multifactorial system causes documented at the index stay (a premature transition against documented unsafety, undelivered portable oxygen, unclear held-medication restart ownership, and an unsafe home plan) rather than to patient nonadherence alone, and tie each corrective action to a documented contributor. Grader anchors: attribution is multifactorial and system-level, not single-person blame; corrective actions map to documented contributors with owners and tracking measures; the review engages the index chart rather than asserting a cause.

Failure Design

| Key Trap | Remediation |
|---|---|
| The intake summary frames the readmission as patient nonadherence (shared world-level trap; primary here) | Attribute to documented system and process contributors from the index stay (06/17 to 06/19 findings; safety event intake E1-T8) |
| Single-cause conclusion | Keep the attribution multifactorial (full chart) |
| Corrective actions generic | Map each action to a documented contributor with an owner and a tracking measure (index findings) |
| Undelivered portable oxygen missed as a contributor (shared world-level trap; primary in Task 5) | Include the oxygen-delivery and teach-back gap (06/17 to 06/18; OT, nursing oxygen flowsheet) |
| Held-medication restart ownership gap missed (shared world-level trap; primary in Task 4) | Include the unclear restart ownership as a contributor (06/15; nephrology note) |

Task-level files: E1-T8 Safety Event and Readmission Intake Summary (external, nonadherence-framed).

Draft Prompt: Mrs. Lydell bounced back within a few days of going home and I need a corrective-action review. Go through what the chart from her stay shows about how this happened, give me your root-cause read, and lay out corrective actions we can actually track.

## Task 9: Heart-Failure Transition Quality Abstraction

Capability: extraction-to-schema with a quiet open-transition disqualifier.
Workflow: HEDIS Medical Record Chart Abstraction and Review, requested by the quality abstraction nurse for physician completion and attestation.
Anchor: 06/26/2025 at 09:00. Priority: P0. Difficulty: medium. Time estimate: 20 to 30 minutes, abstracting the transition documentation against the measure logic.

Expected Output: a physician-completed and attested heart-failure transition quality abstraction, one value, exclusion, or unable-to-determine per field, signed by the attending as the abstracting reviewer. Format: a completed structured abstraction form. Register: quality-abstraction. Length: 250 to 450 words across the fields. Correct responses apply the measure logic honestly, catch that the transition-readiness and follow-up evidence is incomplete in the record and mark those fields accordingly, and do not force a numerator the documentation does not support. Grader anchors: the open-transition fields marked unable-to-determine or not-met per the record; no forced numerator; the oxygen-status field abstracted to the documented exertional desaturation, not a resting value; the follow-up and medication-reconciliation fields abstracted to what the record actually documents.

Failure Design

| Key Trap | Remediation |
|---|---|
| The worksheet rewards a clean, fully closed transition (shared world-level trap; primary here) | Mark the transition-readiness and follow-up fields unable-to-determine or not-met where the record leaves them open (06/19; progress note, case management) |
| Numerator forced | Mark unable-to-determine where the record does not support capture (abstraction fields) |
| Oxygen-status field over-read as resolved (shared world-level trap; primary in Task 1) | Abstract the documented exertional desaturation, not a resting value (06/17; respiratory therapy walk test) |
| Follow-up field captured without evidence | Capture only the documented, owned follow-up, not an assumed one (06/19; transition documentation) |
| Medication-reconciliation field flattened | Abstract the held-agent restart status as documented, not as completed (06/15; nephrology note) |

Task-level files: E1-T9 Heart-Failure Transition Abstraction Worksheet (external).

Draft Prompt: Please complete the heart-failure transition measure abstraction on Mrs. Lydell. Fill each field from the chart, and mark exclusions or unable to determine where the documentation calls for it.

## Task 10: Documentation-Integrity Query Response

Capability: documentation-integrity judgment, reasoned clinical decline in the treating voice.
Workflow: Clinical Documentation Improvement (CDI) Query Response Review, requested by the CDI specialist.
Anchor: 06/26/2025 at 12:00. Priority: P0. Difficulty: medium-high. Time estimate: 20 to 30 minutes, weighing the documented respiratory and cardiorenal picture against the query items.

Expected Output: an attending response to a CDI query set, one reasoned answer per item, agreeing where the record supports it and declining on clinical grounds where it does not. Format: an item-by-item attending query response. Register: treating attending. Length: 350 to 600 words. Correct responses decline to add an over-specific acute respiratory failure or a coding-forward cardiorenal-syndrome label that the treating record does not establish, engage the indicators rather than restating their absence, anchor the reasoning on the team's own documentation, and accept any genuinely supported clarification. Grader anchors: the higher-specificity respiratory failure declined on clinical grounds with reasoning, not a bare or procedural decline; the cardiorenal-syndrome severity label declined where unsupported; supported items such as documented HFpEF acuity answered; no agreement to unsupported severity language.

Failure Design

| Key Trap | Remediation |
|---|---|
| The query presses acute respiratory failure specificity (shared world-level trap; primary here) | Decline on clinical grounds; the record documents hypoxemia with exertional desaturation on low-flow oxygen, not a signed acute respiratory failure (06/13 to 06/17; ED note, respiratory therapy walk test, pulmonology note) |
| Bare or procedural decline | Give the clinical reasoning, why the documented picture fits and the higher-specificity label is not established (06/13 to 06/17) |
| The query presses a coding-forward cardiorenal-syndrome severity label | Decline where the treating record frames a cardiorenal AKI without that specificity (06/15; nephrology note) |
| Over-correction, declining a supported item | Accept genuinely supported clarifications, such as the documented HFpEF acuity (full chart) |
| Severity-capture framing accepted | Treat the reflect-full-severity language as not a license to add an unsupported diagnosis (query memo E1-T10) |

Task-level files: E1-T10 CDI Query Memo (external, severity-forward).

Draft Prompt: CDI sent a query on Mrs. Lydell. Please draft my response as the attending, go item by item against the chart, and make the clinical reasoning explicit so the record stands on its own.

# 3. World File Plan

Files are designed after the tasks; each essential file exists because a task needs it for a correct answer. World-level files provide raw material, never an answer-key synthesis: there is no shared discharge summary, no final disposition statement, no settled cardiorenal plan, and no transition conclusion at world level. The severity-forward and administrative external surfaces (the two payer denials, the continued-stay worksheet, the DME and intake worksheets, the safety-event intake, the abstraction worksheet, the CDI query) are task-level so they cannot pre-answer their tasks. Task 4's task-level input is a complete signed resident transition note that carries two realistic errors for the attending review to catch; Task 6's is a referral request that triggers a letter authored in full from the chart. Neither is a placeholder to be finished. ID convention: EW for essential world-level, E#-T# for essential task-level keyed to the task, WS for supplementary world-level. Filenames are lowercase with underscores and an MMDDYYYY stamp matching the milestones. The file table uses seven columns: number, ID, filename.type, date or hospital-day anchor, Reference File Origin, description, and pearls, traps, and friction. Origins are curated against the DataBank (Template Curation, 2026-06-20): sixteen DataBank-template files cover the clinical notes, consults, flowsheets, reports, and forms; five custom templates cover the lab and MAR flowsheet, the order set, the pharmacy note, the shift note, and the telemetry summary; one notice is a public-domain form; and a single twelve-lead ECG tracing is the one writer-produced media file (rendered, license-clean, engineering does not convert it). Each row carries its document date so the reviewer can verify temporal anchoring at a glance.

## 3.1 Essential Files (World-Level)

| # | ID | Filename.type | Date | Reference File Origin | Description | Pearls, Traps, and Friction |
|---|---|---|---|---|---|---|
| 1 | EW1 | ed_physician_note_06132025.docx | 06/13/2025 / HD1 | Databank Template (001_ED_PHYSICIAN_NOTE.docx; ED physician note) | ED presentation: dyspnea, edema, weight 7 kg over dry, resting SpO2 88 percent on room air, creatinine 2.6 over CKD baseline; acute decompensated HFpEF with cardiorenal AKI; diuresis and oxygen started | Index event and AKI on CKD; admission renal, weight, and resting-saturation values that later tasks must not carry forward as baseline or as the resolved state |
| 2 | EW2 | admission_hp_06132025.docx | 06/13/2025 / HD1 | Databank Template (002_ADMISSION_HP.docx; inpatient admission H and P) | Admission history and physical, full comorbidity profile, home medications, the holds of empagliflozin, spironolactone, losartan, metformin | Held-agent restart substrate; ACE-angioedema and ARB rationale; baseline functional limits |
| 3 | EW3 | hospitalist_progress_hd2_06142025.docx | 06/14/2025 / HD2 | Databank Template (003_PROGRESS_NOTE.docx; inpatient hospitalist progress note) | Hospital day 2 progress note, early diuresis, decongestion plan | Improving-markers narrative begins; no disposition conclusion |
| 4 | EW4 | hospitalist_progress_hd4_06162025.docx | 06/16/2025 / HD4 | Databank Template (003_PROGRESS_NOTE.docx; inpatient hospitalist progress note) | Hospital day 4 progress note, continued diuresis, oxygen question raised | Carries the oxygen-open thread without resolving it |
| 5 | EW5 | hospitalist_progress_hd6_06182025.docx | 06/18/2025 / HD6 | Databank Template (003_PROGRESS_NOTE.docx; inpatient hospitalist progress note) | Hospital day 6 progress note, disposition screening underway, still on oxygen with activity | Improving but not safe; no closure |
| 6 | EW6 | hospitalist_progress_hd7_06192025.docx | 06/19/2025 / HD7 (snapshot) | Databank Template (003_PROGRESS_NOTE.docx; inpatient hospitalist progress note) | Hospital day 7 snapshot note, weight down about 5 kg, creatinine 1.9, resting saturation acceptable, exertional desaturation persists | The exact improving-but-unsafe tension; no closure |
| 7 | EW7 | cardiology_consult_note_06142025.docx | 06/14/2025 / HD2 | Databank Template (006_CONSULT_NOTE.docx; subspecialty consult, reused across cardiology, nephrology, pulmonology, endocrine) | Cardiology HFpEF consult, echo correlation, decongest and protect the kidney, guideline therapy restart caution | HFpEF confirmation; restart-caution substrate; cardiology-versus-nephrology friction |
| 8 | EW8 | nephrology_consult_note_06152025.docx | 06/15/2025 / HD3 | Databank Template (006_CONSULT_NOTE.docx; subspecialty consult, reused across cardiology, nephrology, pulmonology, endocrine) | Nephrology consult, cardiorenal AKI, RAAS and mineralocorticoid antagonist held for potassium and creatinine, restart timing framed as a careful judgment | The deferred-restart anchor; held-agent substrate; cardiology-versus-nephrology friction |
| 9 | EW9 | pulmonology_consult_note_06162025.docx | 06/16/2025 / HD4 | Databank Template (006_CONSULT_NOTE.docx; subspecialty consult, reused across cardiology, nephrology, pulmonology, endocrine) | Pulmonology consult, COPD contribution to dyspnea, asks respiratory therapy to characterize oxygen needs | Dyspnea-attribution; sets up the oxygen testing; respiratory restraint substrate |
| 10 | EW10 | respiratory_therapy_walk_test_06172025.docx | 06/17/2025 / HD5 | Databank Template (061_RESPIRATORY_THERAPY_NOTE.docx; respiratory therapy note, oxygen titration and walk test) | Respiratory therapy oxygen titration and six-minute walk test: acceptable resting saturation, exertional desaturation into the low 80s corrected only with portable oxygen | The central buried finding, resting versus exertional oxygen, off-text from routine vitals; primary substrate for Tasks 1, 3, 7, 9, 10 |
| 11 | EW11 | pt_evaluation_06172025.docx | 06/17/2025 / HD5 | Databank Template (059_PT_OT_SPEECH_THERAPY_EVALUATION.docx; combined PT, OT, speech therapy evaluation) | Physical therapy evaluation, gait, stairs not safe, exertional intolerance, endurance | Stairs and functional tolerance central to disposition; safety-review substrate |
| 12 | EW12 | ot_evaluation_06172025.docx | 06/17/2025 / HD5 | Databank Template (059_PT_OT_SPEECH_THERAPY_EVALUATION.docx; combined PT, OT, speech therapy evaluation) | Occupational therapy evaluation, ADLs, oxygen setup and carry teach-back not achieved, energy conservation | Teach-back failure; oxygen-logistics substrate |
| 13 | EW13 | case_management_note_06182025.docx | 06/18/2025 / HD6 | Databank Template (063_CASE_MANAGEMENT_NOTE.docx; case management and discharge planning note) | Case management screen, two-story home, work-limited daughter, durable medical equipment pending, disposition barriers | Home and caregiver limits; the DME arranged-versus-delivered substrate |
| 14 | EW14 | mar_06132025_06192025.docx | 06/13-06/19/2025 / HD1-HD7 | Custom Made (Custom_Clinical_Flowsheet_Template.docx) | Medication administration record across the stay, diuretic, insulin, the held agents, anticoagulation | The administered-truth source for reconciliation; held-agent and anticoagulation substrate |
| 15 | EW15 | renal_lab_trend_06132025.docx | 06/13-06/19/2025 / HD1-HD7 | Custom Made (Custom_Clinical_Flowsheet_Template.docx) | Renal flowsheet, creatinine, eGFR, potassium from admission (2.6) through snapshot (1.9), baseline 1.7 | Current-versus-admission renal dosing; restart-timing substrate |
| 16 | EW16 | cardiac_biomarker_trend_06132025.docx | 06/13-06/19/2025 / HD1-HD7 | Custom Made (Custom_Clinical_Flowsheet_Template.docx) | Natriuretic peptide and basic cardiac marker trend, falling with decongestion | The improving markers the payer over-reads |
| 17 | EW17 | daily_weights_io_flowsheet_06132025.docx | 06/13-06/19/2025 / HD1-HD7 | Databank Template (056_NURSING_FLOWSHEET_SUMMARY.docx; nursing flowsheet, vitals, weights, intake-output, oxygen) | Daily weights and intake and output, from 7 kg over dry toward 2 kg over dry | Volume trend; volume-versus-readiness substrate |
| 18 | EW18 | vital_signs_flowsheet_06132025.docx | 06/13-06/19/2025 / HD1-HD7 | Databank Template (056_NURSING_FLOWSHEET_SUMMARY.docx; nursing flowsheet, vitals, weights, intake-output, oxygen) | Vitals across the stay, resting saturation improving to acceptable at rest on low-flow oxygen | The reassuring resting saturation the model over-reads; contrast with the walk test |
| 19 | EW19 | echocardiogram_report_06142025.docx | 06/14/2025 / HD2 | Databank Template (045_ECHOCARDIOGRAM_REPORT.docx; echocardiogram report) | Inpatient echocardiogram report, preserved ejection fraction 60 percent, grade II diastolic dysfunction | HFpEF confirmation |
| 20 | EW20 | chest_xray_report_06132025.docx | 06/13/2025 / HD1 | Databank Template (044_RADIOLOGY_REPORT.docx; radiology report) | Chest radiograph report, pulmonary congestion and small effusions on admission | Congestion evidence at admission |
| 21 | EW21 | ecg_report_06132025.docx | 06/13/2025 / HD1 | Databank Template (048_ECG_INTERPRETATION.docx; 12-lead ECG report) | Twelve-lead ECG report, atrial fibrillation, rate-controlled | Atrial fibrillation documentation; rate-control substrate |
| 22 | EW22 | ecg_12lead_06152025.jpg | 06/15/2025 / HD3 | Writer-produced (12-lead ECG tracing, ECG generator) | Repeat twelve-lead ECG, atrial fibrillation, rate-controlled, with a lead II rhythm strip; machine fields only with no printed interpretation | Off-text rhythm substrate consistent with EW21; supports, never the sole scored trap; rendered authored image, license-clean, engineering does not convert |
| 23 | EW23 | home_medication_list_06132025.docx | 06/13/2025 / HD1 | Databank Template (012_EMR_MEDICATION_LIST.docx; system-generated EMR medication list) | EMR pre-admission home medication list with dose, route, frequency, indication | The before-state for reconciliation; ARB-not-ACE rationale |
| 24 | EW24 | medication_hold_orders_06132025.docx | 06/13/2025 / HD1 | Custom Made (Custom_Order_Set_Template.docx) | Signed admission hold orders for empagliflozin, spironolactone, losartan, metformin with reasons | Makes the holds explicit decisions, not silent gaps |
| 25 | EW25 | anticoagulation_renal_dosing_note_06152025.docx | 06/15/2025 / HD3 | Custom Made (Custom_Pharmacy_Note_Template.docx) | Pharmacy anticoagulation note, apixaban dose reviewed against current renal function, single agent, no duplication | Renal anticoagulation dosing; the duplicate-anticoagulant substrate the outside and intake lists will conflict with |
| 26 | EW26 | endocrine_glycemic_note_06162025.docx | 06/16/2025 / HD4 | Databank Template (006_CONSULT_NOTE.docx; subspecialty consult, reused across cardiology, nephrology, pulmonology, endocrine) | Endocrine glycemic note, basal insulin continued, metformin held, the prandial sliding scale inpatient only | Insulin continuity; sliding-scale de-escalation substrate |
| 27 | EW27 | nursing_oxygen_use_flowsheet_06182025.docx | 06/18/2025 / HD6 | Databank Template (056_NURSING_FLOWSHEET_SUMMARY.docx; nursing flowsheet, vitals, weights, intake-output, oxygen) | Nursing flowsheet, home-oxygen use, ambulation saturation with activity, portable-oxygen setup attempts | Off-text oxygen-with-activity evidence and the equipment and teach-back contributors |
| 28 | EW28 | outpatient_summary_05302025.docx | 05/30/2025 / pre-admission | Databank Template (024_OFFICE_VISIT_NOTE.docx; outpatient office visit note) | Pre-admission cardiology and primary care summary: baseline creatinine 1.7 and eGFR about 30, baseline hemoglobin 10.0, dry weight about 88 kg, home oxygen 2 L nocturnal and exertional, baseline function | The quiet baselines; the comparators the model must use over admission or discharge values |
| 29 | EW29 | prior_echocardiogram_report_06012025.docx | 06/01/2025 / pre-admission | Databank Template (045_ECHOCARDIOGRAM_REPORT.docx; echocardiogram report) | Prior outpatient echocardiogram, preserved ejection fraction, grade II diastolic dysfunction | Baseline cardiac comparator; HFpEF chronicity |
| 30 | EW30 | family_communication_note_06182025.docx | 06/18/2025 / HD6 | Databank Template (003_PROGRESS_NOTE.docx; inpatient hospitalist progress note) | Family meeting with the daughter, willingness within work-schedule limits, two-story home | Caregiver limits and home realism for the appeals |
| 31 | EW31 | social_work_sdoh_note_06182025.docx | 06/18/2025 / HD6 | Databank Template (062_SOCIAL_WORK_NOTE.docx; social work note) | Social work note, home environment, stairs, transportation, support resources | Home-environment substrate; SDOH context, never the scored trap itself |
| 32 | EW32 | telemetry_summary_06172025.docx | 06/15-06/17/2025 / HD3-HD5 | Custom Made (Custom_Telemetry_Summary_Template.docx) | Telemetry summary, rate-controlled atrial fibrillation across the monitored days | Rate-control documentation; supports EW21 and EW22 |

## 3.2 Essential Files (Task-Level)

| # | ID | Filename.type | Date | Reference File Origin | Description | Pearls, Traps, and Friction |
|---|---|---|---|---|---|---|
| 1 | E1-T1 | oxygen_snf_denial_letter_06202025.docx | 06/20/2025 | Custom Made (Custom_Payer_Denial_Letter_Template.docx) | External payer denial of the skilled-nursing stay and the home-oxygen upgrade, framing the acceptable resting saturation and diuresis as home readiness | Task 1 |
| 2 | E1-T2 | outside_medication_list_06202025.docx | 06/20/2025 | Custom Made (Custom_Outside_Medication_List_Template.docx) | External outside pharmacy and transfer medication list carrying a stale renal dose and a held agent shown as continued | Task 2 |
| 3 | E1-T3 | continued_stay_review_worksheet_06202025.docx | 06/20/2025 | Custom Made (Custom_Utilization_Review_Worksheet_Template.docx) | External continued-stay worksheet treating post-diuresis improvement as readiness | Task 3 |
| 4 | E1-T4 | signed_resident_transition_note_06212025.docx | 06/21/2025 | Custom Made (Custom_Transition_Note_Template.docx) | Complete signed resident transition note that clears oxygen on the home setup and silently resumes the held cardiorenal and diabetes agents, the two common errors the peer review must catch | Task 4 |
| 5 | E1-T5 | dme_vendor_coordination_worksheet_06212025.docx | 06/21/2025 | Custom Made (Custom_Care_Coordination_Worksheet_Template.docx) | External durable medical equipment and case-management worksheet, oxygen described as arranged while the portable unit is not delivered | Task 5 |
| 6 | E2-T5 | snf_intake_medication_list_06212025.docx | 06/21/2025 | Custom Made (Custom_SNF_Intake_Medication_List_Template.docx) | External skilled-nursing intake medication list carrying a duplicate anticoagulant or a stale renal dose | Task 5 |
| 7 | E1-T6 | cardiorenal_referral_request_06222025.docx | 06/22/2025 | Custom Made (Custom_Referral_Request_Template.docx) | Hospitalist referral request to cardiology and nephrology for cardiorenal follow-up; the trigger, the letter is authored in full from the chart | Task 6 |
| 8 | E1-T7 | home_health_sufficient_denial_letter_06242025.docx | 06/24/2025 | Custom Made (Custom_Payer_Denial_Letter_Template.docx) | External denial framing home health as sufficient instead of a skilled-nursing stay | Task 7 |
| 9 | E1-T8 | safety_event_readmission_intake_06252025.docx | 06/25/2025 | Custom Made (Custom_Safety_Event_Intake_Template.docx) | External safety-event intake describing the heart-failure readmission, framed as patient nonadherence | Task 8 |
| 10 | E1-T9 | hf_transition_abstraction_worksheet_06262025.docx | 06/26/2025 | Custom Made (Custom_Quality_Abstraction_Worksheet_Template.docx) | External heart-failure transition measure abstraction form, fields to value, exclude, or mark undetermined | Task 9 |
| 11 | E1-T10 | cdi_query_memo_06262025.docx | 06/26/2025 | Custom Made (Custom_CDI_Query_Memo_Template.docx) | External CDI query pressing acute respiratory failure specificity and a cardiorenal-syndrome severity label | Task 10 |

## 3.3 Supplementary Files

| # | ID | Filename.type | Date | Reference File Origin | Description | Pearls, Traps, and Friction |
|---|---|---|---|---|---|---|
| 1 | WS1 | heart_failure_education_handout_06192025.docx | 06/19/2025 / HD7 | Databank Template (058_PATIENT_EDUCATION_DOCUMENTATION.docx; patient education documentation) | Generic heart-failure self-care education handout | Removing it changes no medication, appeal, coordination, or determination answer |
| 2 | WS2 | discharge_rights_notice_06192025.pdf | 06/19/2025 / HD7 | Public Domain (Important Message from Medicare, CMS) | Standard Medicare discharge and appeal-rights notice, generic | Removing it changes no correct answer |
| 3 | WS3 | nursing_shift_narrative_06162025.docx | 06/16/2025 / HD4 | Custom Made (Custom_Nursing_Shift_Note_Template.docx) | Generic shift narratives, turns, intake, family at bedside, no load-bearing fact | Removing it changes no correct answer |
| 4 | WS4 | hospital_admission_consent_06132025.pdf | 06/13/2025 / HD1 | Databank Template (009_INFORMED_CONSENT.docx; informed consent documentation) | Generic hospital admission consent and paperwork | Removing it changes no correct answer |

Total file count: 32 essential world-level (EW1 to EW32) plus 11 essential task-level plus 4 supplementary world-level equals 47 unique files. World-level files total 36 (32 essential plus 4 supplementary), which meets the 30-file minimum. Modalities span clinical notes, specialty consults, radiology and diagnostic reports, laboratory and flowsheet data, medication records, external correspondence and worksheets, and one twelve-lead ECG image, which is at least four distinct types. Essential-to-supplementary mix is about 89 percent essential at world level. Origins: the 36 world-level rows resolve to 21 reference templates (16 DataBank extractions, 5 custom drafts), one public-domain notice (WS2, the Medicare message), and one writer-produced twelve-lead ECG tracing (EW22).

# 4. World Summary

This world evaluates whether a clinician can hold two true things at once, that the heart failure and the kidney injury are improving and that the patient is not safe to transition home, and act on the second across ten independent payer, documentation, coordination, and safety encounters. The trap architecture works because every scored judgment has a documented contradiction or a documented restraint behind it: an acceptable resting oxygen saturation against a formal walk test that shows exertional desaturation, case-management prose that says equipment is arranged against a vendor record that shows portable oxygen undelivered, held cardiorenal and diabetes agents that read as automatic resumes against a nephrology note that frames restart as a careful judgment, and a stale outside or intake medication list against the active record. The world is hard for an AI agent because the safe answer is almost never the most available one: the reassuring resting saturation, the improving weight and creatinine, the tidy arranged-equipment line, and the resumed home regimen are all locally reasonable and all wrong here, and rejecting them requires synthesizing across the walk test, therapy evaluations, flowsheets, consult notes, and external documents while honoring a stated source-of-truth order rather than the single most recent or most reassuring line. Task 4 is an attending peer review of a complete signed resident note that makes two common, realistic errors, an oxygen clearance despite the documented exertional desaturation and a silent resumption of the held agents, so the model is tested on catching a documented, realistic mistake rather than on completing a placeholder. Task 6 is authored in full from the chart. Neither relies on a planted falsehood in the patient's own record.

Self-Containment Principle: every claim in a task's correct answer is traceable to the task prompt, the task-level files, and the world-level files. A seasoned clinician could solve every task from the intended files alone, no task requires medical knowledge published after the model's knowledge cutoff because every judgment rests on long-established heart-failure, renal, and respiratory standards of care, and any fact not supported by those sources is either fabrication if asserted or must be acknowledged as uncertain. This principle governs golden-response construction and grader-guideline calibration downstream.

