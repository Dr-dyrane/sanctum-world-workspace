# Korvin Merrow World Brainstorm

Document date: May 29, 2026

## 1. World Setup

World Type: Typical Clinical World

This is an Emergency Medicine / Internal Medicine acute hospital world built around a multi-day hospitalization that begins with ED evaluation of an undifferentiated patient and follows inpatient admission, evolving workup, consultant involvement, treatment changes, and discharge planning.

Korvin Merrow is a 62-year-old male with long-standing type 2 diabetes mellitus, hypertension, CKD stage 3, HFrEF, CAD history, hyperlipidemia, anemia of CKD, osteoporosis/osteopenia from chronic steroid exposure, obstructive sleep apnea, diabetic peripheral neuropathy, polypharmacy, and polymyalgia rheumatica previously treated with chronic prednisone with recent tapering. He lives at home with spouse/family, was independent with ADLs before illness, ambulated without major assistance, and managed some medications himself with family support.

His medication complexity is concrete and central to the world. His chronic medication list includes sacubitril/valsartan 24/26 mg BID, carvedilol 12.5 mg BID, furosemide 40 mg daily, spironolactone 25 mg daily, empagliflozin 10 mg daily, aspirin 81 mg daily, atorvastatin 40 mg nightly, metformin ER 500 mg BID, insulin glargine 18 units nightly, prednisone with inconsistent documented taper/dose, alendronate 70 mg weekly, calcium/vitamin D daily, ferrous sulfate 325 mg every other day, and gabapentin 300 mg nightly. These medications support the HF-AKI medication trap, the steroid source-of-truth trap, and the discharge safety/reconciliation complexity without changing the central clinical arc.

He presents after several days of poor oral intake, weakness, confusion, reduced activity, possible urinary symptoms, and subjective fever. Initial ED and inpatient findings support treating suspected urinary-source sepsis: abnormal vitals, inflammatory findings, possible UTI, AKI on CKD, and altered mental status. Treating possible sepsis initially is appropriate.

The complexity develops over time. Infection markers improve and the patient becomes more stable, but not every symptom resolves. Persistent weakness, intermittent confusion, borderline blood pressure, evolving renal function, medication changes, functional decline, and unclear steroid timeline force reassessment of overlapping contributors: infection, dehydration/AKI, medication effects, endocrine risk from recent steroid exposure, and chronic disease burden.

The World closes on Hospital Day 6 at 18:00 during discharge planning. At that point, the patient is clinically improved: vitals are better, infection appears controlled, renal function is improving, and acute issues appear addressed. But he is not clearly back to baseline: he remains weaker, family reports intermittent cognitive concerns, and the medication plan has changed significantly. The central clinical question is whether the patient is medically stable on paper or actually safe leaving the hospital.

## 2. Major Friction Points

1. Nephrology vs Cardiology

This is the strongest medication-management friction. The patient has AKI on CKD stage 3 with hypotension during admission. Nephrology prioritizes renal recovery, avoiding recurrent AKI, preventing worsening hypotension, and temporarily holding unsafe medications. Cardiology is focused on established HFrEF/CAD and wants to avoid unnecessary withdrawal of long-term protective therapy that prevents heart failure decompensation and readmission.

The conflict is immediate renal/hemodynamic safety vs long-term cardiovascular optimization. Both positions are clinically reasonable.

2. Family vs Inpatient Medicine

This is the discharge-readiness friction. Family understands the patient's baseline: independent ADLs, usual ambulation without major assistance, medication self-management, cognition, and real-world home function. They see that infection markers and vitals have improved, but he remains weaker, intermittently confused, and now has a substantially changed medication plan. They advocate for more observation, safer transition planning, and possible rehab/support evaluation.

The inpatient team sees objective stabilization: improved vitals, controlled infection, improving renal function, and acute issues addressed. They believe discharge with follow-up may be reasonable.

The conflict is medical stability on paper vs functional readiness and real-world safety.

3. Emergency/Inpatient Medicine vs Endocrinology

This is not a missed-diagnosis reveal. It is a difference in risk interpretation after stabilization. ED and inpatient medicine appropriately prioritize suspected sepsis, fluids, antibiotics, hemodynamic support, and avoiding unnecessary prolonged steroid exposure once acute infection appears improved.

Endocrinology focuses on chronic prednisone exposure for PMR, unclear taper history, persistent weakness, borderline hypotension, and nonspecific symptoms that overlap with adrenal insufficiency. They want careful interpretation of steroid history, adrenal evaluation, and a safe steroid management/taper plan.

The conflict is risk of premature steroid withdrawal vs risk of unnecessary steroid continuation.

This remains a friction only because Endocrinology is expected to leave an explicit consult recommendation or documented position. The conflicting steroid records themselves are a trap, not the friction.

## 3. Major Traps

1. Steroid timeline/source-of-truth trap

Type: temporal + source-of-truth. Older rheumatology documentation shows long-term prednisone use for PMR, but a later outpatient plan recommended gradual tapering because symptoms were controlled. The outpatient medication list was not fully updated, admission medication reconciliation pulls older information, family is unsure of the exact dose, and inpatient notes copy forward inconsistent steroid status. The clinician must reconstruct whether recent exposure is enough that adrenal suppression risk should influence acute management and discharge planning. Requires synthesis across rheumatology notes, outpatient medication list, admission medication reconciliation, family history, and inpatient course. World-level.

Guardrail: this is not a hidden adrenal insufficiency reveal. Steroid evidence stays scattered and partly contradictory, and adrenal risk remains one contributor among infection, AKI/dehydration, medication effects, deconditioning, and chronic disease.

2. HF-AKI medication reconciliation and time-sensitive consultant trap

Type: medication reconciliation + temporal + source hierarchy. Sacubitril/valsartan, furosemide, spironolactone, empagliflozin, carvedilol, and other heart failure/CAD therapies are appropriately held or adjusted during AKI/hypotension. Early "hold medication" recommendations remain visible later, while cardiology and nephrology recommendations occur at different points in the admission and the patient's renal function and blood pressure evolve. A wrong answer either restarts everything too early despite instability or discharges the patient without reassessing appropriate long-term cardiac therapy after recovery. Requires synthesis across dated nephrology notes, cardiology notes, creatinine trend, blood pressure trend, active orders, and medication administration record. World-level.

3. Buried functional/cognitive status trap

Type: buried information. Physician notes describe the patient as clinically improved and medically stable, but nursing, PT, and family documentation contains intermittent confusion, weakness with ambulation, needing more assistance than baseline, and concern about managing new medications. The failure is assuming improved labs equal discharge readiness. Requires synthesis across progress notes, nursing notes, PT assessment, and family communication. World-level.

4. Sepsis anchoring after partial improvement trap

Type: diagnostic anchoring + temporal reasoning. Early documents correctly emphasize suspected UTI/sepsis: ED assessment, admission note, early labs, and initial treatment response. Later documents show infection markers improving and the culture/treatment course clarified, but persistent weakness, borderline BP, renal recovery not yet at baseline, evolving electrolyte issues, medication changes, functional decline, and steroid timeline questions remain. The failure is assuming the initial diagnosis explains the entire hospitalization or making day 5-7 decisions from day 1 snapshots. Correct reasoning recognizes sepsis was real or reasonable initially while avoiding premature closure after partial improvement. Requires synthesis across early ED/admission documents, serial labs/vitals, culture/treatment updates, medication records, nursing/PT findings, and steroid-related documentation. World-level.

5. Discharge plan source-hierarchy trap

Type: transition-of-care + source hierarchy. A draft discharge plan or routine discharge planning note may imply a straightforward home discharge because vitals, infection markers, and renal function are improving. That document is misleading if read alone because medication changes, unresolved follow-up needs, family concerns, and functional/cognitive observations live elsewhere. This is distinct from the buried functional/cognitive trap: Trap 3 asks whether the clinician finds the hidden evidence; this trap asks whether the clinician recognizes that a reassuring discharge planning artifact is not the full source of truth. Requires synthesis across discharge planning documents, medication plan, consultant recommendations, PT/nursing notes, and family communication. World-level.

## 4. Rough Task Ideas

1. Discharge medication reconciliation / medication safety review

Workflow mapping: P0: Discharge Medication Reconciliation.

Requester and anchor: Hospitalist requests this on Hospital Day 7, after the World close.

Task-level trap: The final medication list contains a copied-forward inconsistency from an earlier medication hold, requiring the clinician to distinguish intentional discharge changes from outdated inpatient orders.

The clinician reconciles the final medication plan. The distinct competency is medication action reasoning: determine what should continue, restart, stop, or require follow-up without blindly copying admission medications or early inpatient holds. It draws on the HF-AKI medication reconciliation trap and steroid timeline/source-of-truth trap.

2. Hospital discharge summary generation

Workflow mapping: P0: Hospital Discharge Summary Generation.

Requester and anchor: Attending physician requests this on Hospital Day 7, after the World close.

Task-level trap: The summary must avoid copying the early sepsis-only framing into the final hospital course after later documents clarify persistent noninfectious contributors.

The clinician creates an accurate discharge summary from the completed hospitalization. The distinct competency is narrative fidelity: summarize the true hospital course, including suspected sepsis treatment, AKI course, medication changes, consultant recommendations, unresolved follow-up issues, and discharge considerations without importing outdated assumptions. It draws on source-of-truth reasoning, temporal sequence, and avoiding copy-forward errors.

3. Transition-of-care / discharge readiness plan

Workflow mapping: P0: Discharge Planning Documentation.

Requester and anchor: Case manager and hospital medicine team request this on Hospital Day 7, after the World close.

Task-level trap: Discharge planning documents conflict about whether home discharge, home health, or rehab-level support is safest, requiring synthesis rather than accepting the most reassuring note.

The clinician evaluates discharge needs and creates a safe transition plan. The distinct competency is disposition safety: integrate family concerns, PT/nursing information, functional status, medication complexity, and follow-up needs when the patient is medically improved but not clearly back to baseline. It draws on the buried functional/cognitive status trap and discharge plan source-hierarchy trap.

4. Post-hospital follow-up assessment note

Workflow mapping: P0: Transitional Care Management Documentation (TCM).

Requester and anchor: Primary care physician requests this 7 days after discharge, after the World close.

Task-level trap: The follow-up note must distinguish symptoms present before discharge from new or persistent post-discharge problems rather than treating all weakness and blood pressure concerns as a new event.

The distinct competency is reassessment after transition: review the hospitalization and determine what ongoing issues need attention, including weakness, blood pressure, medication tolerance, steroid plan, and renal recovery. The task tests temporal clinical reasoning and avoidance of sepsis anchoring after partial improvement.

5. Consultant recommendation synthesis / care coordination note

Workflow mapping: P1: Interdisciplinary Care Plan Development and Documentation.

Requester and anchor: Hospital care team requests this on Hospital Day 7, after the World close.

Task-level trap: Consultant recommendations occur at different timestamps, so the clinician must identify which recommendations were time-limited and which remain applicable after renal function, blood pressure, and steroid plan changed.

The clinician reconciles recommendations from nephrology, cardiology, and endocrinology into one coherent plan. The distinct competency is consultant-priority synthesis: determine which recommendations remain applicable, which were time-limited, and how to handle reasonable but competing specialist priorities. It draws on time-sensitive consultant recommendations and stakeholder friction.

6. Readmission risk / patient safety review

Workflow mapping: P0: Patient Risk Stratification Assessment.

Requester and anchor: Quality and patient safety team requests this 30 days after discharge, after the World close.

Task-level trap: The review must identify subtle preventable risk factors, including medication confusion, incomplete functional recovery, and follow-up fragility, rather than focusing only on whether infection treatment was completed.

The clinician reviews the hospitalization to identify preventable readmission risks. The distinct competency is retrospective safety analysis: recognize vulnerabilities around medication confusion, functional decline, incomplete follow-up, complex chronic disease management, and family concerns. It draws on discharge safety, medication reconciliation, and transition-of-care traps without requiring a new diagnosis.

Reserve option: future ED reassessment after return visit. Several days after discharge, the patient could return with weakness/lightheadedness. This should not be framed as "missed adrenal insufficiency"; it would test broad reassessment of medication effects, volume status, renal function, infection recurrence, and steroid-related risk. Keep as reserve rather than primary.
