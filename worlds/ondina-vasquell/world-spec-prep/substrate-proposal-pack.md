# Ondina Vasquell - Clinical Substrate Proposal Pack (Phase A)

Provenance and rule: derived by Claude from the decision record (locked clinical design), the KM medication-expansion and comorbidity packages (house pattern and register), and standard guideline-concordant management for this patient profile. Per decision 12, every numeric clinical fact NOT supplied by Alexander is generated clinically-concordant and flagged RATIFY. Alexander strikes or approves in one pass; nothing here is asserted as locked fact until he does. No value traces to a real patient.

RATIFICATION: Alexander read and ratified all flagged values on 2026-06-13. The proposed values are now LOCKED and consumed by the spec; the RATIFY tags below mark provenance (Claude-proposed, physician-ratified), not open items.

## 1. Identity package (arithmetic gates)

| Field | Proposed value | Flag |
|---|---|---|
| Name | Ondina Vasquell | LOCKED (decision 6) |
| Sex | Female | LOCKED |
| DOB | 03/14/1958 | RATIFY (gives age 68 at the 05/21/2026 snapshot; any date 05/22/1957 to 05/21/1958 works) |
| Age at snapshot | 68 | Derived from DOB |
| MRN | OV-3358104 | RATIFY (synthetic, non-institutional, OV-prefixed per the KM KM-6427819 precedent) |
| Height | 157 cm (5 ft 2 in) | RATIFY |
| Weight | 84 kg (185 lb) | RATIFY |
| BMI | 34.1 (recomputed from 84 / 1.57^2 = 34.08), class I obesity | Derived; consistent with the obesity comorbidity |
| Allergies | Sulfa (sulfonamide antibiotics), documented rash | RATIFY (a sulfa allergy is load-bearing: it constrains the pharmacy-rejection substitute trap fairly; alternative is None) |
| Code status | Full Code | RATIFY |
| Language | Spanish preferred; uses interpreter or bilingual staff for direct history | LOCKED (decision 1) |
| Marital / support | Widowed; lives alone in a second-floor walk-up; adult daughter (works nights) is primary but partial caregiver | LOCKED (decision 1) |
| Insurance | Medicare Advantage primary, Medicaid secondary | LOCKED (decision 1) |

## 2. Home medication list (pre-admission baseline)

Register matches the KM home-med table: drug, dose, route, frequency, indication, plus the inpatient change column. Every dose is RATIFY unless marked otherwise. Routes written as Oral (never the PO letter-O token). Renal dosing reflects CKD 3b (eGFR proposed 38, RATIFY); this is load-bearing for the med-rec and pharmacy traps.

| Medication (dose, route, frequency) | Indication | Inpatient change | Flag |
|---|---|---|---|
| Insulin glargine 26 units subcutaneous nightly | T2DM basal | Continued; adjusted for inpatient intake | RATIFY |
| Insulin aspart sliding scale subcutaneous three times daily with meals | T2DM prandial | Continued; sliding scale per inpatient protocol | RATIFY |
| Metformin 500 mg Oral twice daily | T2DM | HELD on admission (eGFR near the 30 threshold; load-bearing for med-rec restart judgment) | RATIFY |
| Empagliflozin 10 mg Oral daily | T2DM, HFpEF, CKD | HELD during acute infection (sick-day and euglycemic-DKA caution); restart is a judgment item | RATIFY |
| Lisinopril 20 mg Oral daily | Hypertension, CKD proteinuria | HELD on admission for AKI risk; restart parameter-gated | RATIFY |
| Furosemide 20 mg Oral daily | HFpEF volume | Continued; dose adjusted to volume status | RATIFY |
| Atorvastatin 40 mg Oral nightly | Dyslipidemia, PAD, ASCVD | Continued | RATIFY |
| Aspirin 81 mg Oral daily | PAD, secondary prevention | Continued | RATIFY |
| Clopidogrel 75 mg Oral daily | PAD | Continued | RATIFY |
| Gabapentin 300 mg Oral three times daily | Diabetic peripheral neuropathy | Continued; renally dose-checked (load-bearing) | RATIFY |
| Ferrous sulfate 325 mg Oral daily | Anemia of CKD, iron support | Continued | RATIFY |
| Cholecalciferol 2000 units Oral daily | CKD mineral-bone, vitamin D | Continued | RATIFY |
| Pantoprazole 40 mg Oral daily | GERD | Continued | RATIFY |
| Acetaminophen 650 mg Oral three times daily as needed | Knee osteoarthritis (NSAIDs avoided in CKD; load-bearing) | Continued | RATIFY |
| CPAP nightly (device, not a drug) | Obstructive sleep apnea | Continued inpatient | RATIFY |

Notes carried to the spec: NSAIDs are contraindicated by CKD (acetaminophen-only for the knee is a fair quiet expectation). The held cardiorenal and diabetes agents (metformin, empagliflozin, lisinopril) drive the med-rec restart-judgment trap. The sulfa allergy fairly constrains the pharmacy-rejection antibiotic substitute. An ESA (for anemia of CKD) is intentionally NOT on the home list, so anemia stays an open management item rather than a closed one.

## 3. Inpatient antibiotic and key inpatient meds (the renal-dosing trap substrate)

| Agent | Proposed inpatient course | Flag |
|---|---|---|
| Empiric: vancomycin + piperacillin-tazobactam, started HD1 05/16/2026 | Broad coverage for limb-threat diabetic foot infection; vancomycin by level, pip-tazo renally dosed | RATIFY |
| Culture-directed step: cefepime renally dosed, or per deep-tissue culture | After cultures; the renal dose adjustment is the trap axis | RATIFY |
| The PBM-rejection substitute (Task 5): a fluoroquinolone or a sulfa-containing oral agent flagged by the plan as preferred, unsafe here (QT, renal, or the sulfa allergy) | The wrong-by-genre external pressure | RATIFY which contraindication anchors it |

## 4. Key labs and studies (trap-relevant values; all RATIFY)

| Item | Proposed | Role |
|---|---|---|
| Baseline eGFR / creatinine | eGFR 38, creatinine 1.5 mg/dL (CKD 3b) | Renal-dosing and metformin/empagliflozin restart trap |
| Admission peak creatinine | 2.1 mg/dL (AKI on CKD), improving to 1.6 by snapshot | Restart-timing judgment |
| Hemoglobin | 9.8 g/dL (anemia of CKD) | Open anemia item; not closed |
| HbA1c | 8.6 percent | Diabetes control context; quality-measure substrate |
| WBC | 14.2 on admission, trending to 8.9 by snapshot | "Improving markers" that the payer over-reads |
| ABI / TBI | ABI noncompressible (>1.3) bilaterally; TBI 0.5 on the affected side | Perfusion-overstatement trap; the formal study governs over the bedside pulse note |
| MRI foot | Marrow edema adjacent to the ulcer; early osteomyelitis cannot be excluded | Equivocal-osteo trap (decision 5) |
| Pathology (debrided tissue) | Soft tissue with acute inflammation; no bone in specimen | Keeps osteo unconfirmed |

## 5. Care team roster (candidate synthetic names, collision-checked against KM)

Pick one per row or replace; all unmistakably synthetic, no near-duplicates with the KM roster (Vossmere, Travyn, Quenor, Solthar, etc.).

| Role / service | Candidate name | Flag |
|---|---|---|
| Hospitalist attending (primary, golden voice) | Dr. Marisol Everet, MD | RATIFY |
| Hospitalist resident (PGY-2) | Dr. Tobias Renquist, MD | RATIFY |
| Podiatry (debridement, offloading) | Dr. Priyanka Vell, DPM | RATIFY |
| Vascular surgery (perfusion, revascularization) | Dr. Castor Mwangi, MD | RATIFY |
| Infectious disease | Dr. Helena Brusk, MD | RATIFY |
| Endocrinology / diabetes educator | Dr. Imran Saafeld, MD | RATIFY |
| Wound care nurse | Renata Olwyn, RN, CWOCN | RATIFY |
| Physical therapy | Devon Achara, PT, DPT | RATIFY |
| Occupational therapy | Sela Pruvost, OT | RATIFY |
| Inpatient pharmacist (Task 5) | Quentin Mabari, PharmD | RATIFY |
| Case manager | Lorna Defreze, RN, CCM | RATIFY |
| CDI specialist (Task 3) | Bristol Ndiaye, RN, CCDS | RATIFY |
| HIM coding lead (Task 2) | Corwin Adeyle, RHIA, CCS | RATIFY |
| MA medical director (external, Task 4) | Dr. Ellery Stovall, MD | RATIFY |
| Daughter / caregiver | Marisela Vasquell | RATIFY |

## 6. Key milestones (compressed timeline; all dates RATIFY where not locked)

| Date | Event |
|---|---|
| Late April 2026 (approx 04/28) | Outpatient foot wound first noted; ulcer deterioration over ~3 weeks | RATIFY exact |
| 05/16/2026 (HD1) | ED presentation, admission, empiric antibiotics started | RATIFY (anchors the 6-day course to a 05/21 snapshot) |
| 05/17/2026 (HD2) | Podiatry soft-tissue debridement; deep-tissue cultures sent | RATIFY |
| 05/18/2026 (HD3) | MRI foot (equivocal osteo); ID consult | RATIFY |
| 05/19/2026 (HD4) | ABI/TBI study (noncompressible); vascular consult | RATIFY |
| 05/20/2026 (HD5) | PT/OT evaluations; case management screen; pathology results (no bone) | RATIFY |
| 05/21/2026 18:00 (HD6) | WORLD SNAPSHOT: chart frozen, improving but operationally unsafe | LOCKED (decision 2) |
| 05/22/2026 08:30 | Task 1 med rec | LOCKED |
| 05/22/2026 09:00 | Task 2 coding attestation | LOCKED |
| 05/22/2026 10:00 | Task 10 discharge-instruction completion | LOCKED |
| 05/24/2026 10:00 | Task 3 CDI response | LOCKED |
| 05/24/2026 15:00 | Task 4 SNF-denial appeal | LOCKED |
| 05/25/2026 09:00 | Task 5 pharmacy rejection | LOCKED |
| 05/26/2026 11:00 | Task 6 continued-stay determination | LOCKED |
| 06/04/2026 09:00 | Task 7 quality abstraction | LOCKED |
| 06/08/2026 14:00 | Task 8 vascular referral | LOCKED |
| 06/11/2026 10:00 | Task 9 safety review | LOCKED |

All world documents are dated at or before 05/21/2026 18:00; nothing is future-dated; every task anchor is strictly after the snapshot.

## 7. Self-verification (Claude, against encoded standards)

- Voice: table register and clinical shorthand match the KM home-med table and clinical-voice-lessons; trap-carrier values stay plain, no synthesis performed in the substrate.
- Difficulty/fairness: each trap axis has a chart-contradiction or mandate (renal dose vs eGFR; ABI vs bedside pulse; equivocal osteo; held-agent restart), none chart-silent; the photo stays substrate.
- Self-containment: no value depends on public knowledge after July 31, 2025.
- No-invention guardrail: every new numeric carries a RATIFY flag; nothing is asserted as locked.
