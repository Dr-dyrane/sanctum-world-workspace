**SYNTHETIC TRAINING DOCUMENT | FICTIONAL PATIENT | NOT A REAL MEDICAL RECORD**

---

**MERCY VALE REGIONAL MEDICAL CENTER** — Medical Records | Confidential

5 Harbor Crest Way, Bridgehollow, PA 15211 | Main (412) 555-0143 | Medical Records (412) 555-0188

---

**PATIENT:** KORVIN MERROW, 62 y, Male | DOB 02/18/1964 | **MRN** KM-6427819 | **FIN** KM-2026-051877

**Date / Anchor:** 2026-05-18 (HD1 / pre-admission chart import)
**Source:** Chart problem-list import — Medical Records
**Allergy on file:** Lisinopril (cough) — interpreted as ACE-inhibitor intolerance
**Document type:** Problem list / past-history snapshot (supplementary background)

---

# PROBLEM LIST / PAST HISTORY SNAPSHOT

This snapshot is a supplementary background view of the carried-forward chart problem list and prior medical/surgical history as it appears in the imported electronic record at the time of admission. It is a low-authority orientation source intended for quick clinician scan. It is NOT an attending assessment, consultant assessment, verified medication reconciliation, pharmacy history, rheumatology source, discharge summary, or final problem list, and must not be used as sole critical evidence for any clinical decision.

---

## ACTIVE PROBLEM LIST (CARRIED-FORWARD CHART ENTRIES)

| # | Condition | ICD-10 | Onset (approximate) | Status | Notes |
|---|-----------|--------|---------------------|--------|-------|
| 1 | Heart failure with reduced ejection fraction (HFrEF) | I50.22 | approx. 2019 | Active, chronic | Documented after remote ischemic event; chronic guideline-directed therapy on home list. |
| 2 | Coronary artery disease with remote PCI / drug-eluting stent (mid-LAD) | I25.10 | approx. 2018 (PCI 09/12/2018) | Active, chronic | Single-vessel PCI / DES at Mercy Vale Regional 2018-09-12 (legacy cath record). |
| 3 | Essential (primary) hypertension | I10 | longstanding (prior to chart establishment) | Active, chronic | Carried forward across primary-care problem-list entries. |
| 4 | Mixed hyperlipidemia | E78.2 | longstanding (prior to chart establishment) | Active, chronic | On chronic high-intensity statin therapy. |
| 5 | Chronic kidney disease, stage 3 | N18.30 | approx. 2020 | Active, chronic | Stage classification carried forward; baseline creatinine and eGFR documented separately in primary care record. |
| 6 | Type 2 diabetes mellitus | E11.9 | approx. 2012 | Active, chronic | Long-duration; combined oral + basal insulin regimen on home list. |
| 7 | Diabetic peripheral neuropathy | E11.42 | approx. 2017 | Active, chronic | Symptomatic lower-extremity distribution; contributes to baseline mobility vulnerability. |
| 8 | Obstructive sleep apnea | G47.33 | approx. 2019 (PSG 04/22/2019) | Active, chronic | Diagnosed by polysomnography at Mercy Vale Sleep Center; CPAP prescribed; adherence variable per prior outpatient notes. |
| 9 | Polymyalgia rheumatica | M35.3 | several-year history (per outpatient rheumatology) | Active, chronic | Multi-year course with multiple prior flares and taper attempts; chronic steroid exposure history; followed by Riverbend Rheumatology Associates. |
| 10 | Anemia of chronic kidney disease | D63.1 | approx. 2021 | Active, chronic | Coded against CKD context; chronic supportive iron therapy on home list. |
| 11 | Osteoporosis / osteopenia related to chronic steroid exposure | M81.0 | approx. 2021 | Active, chronic | Coded in association with cumulative steroid exposure; chronic bone-health therapy on home list. |
| 12 | Class I obesity by BMI | E66.9 | longstanding | Active, chronic | BMI 30.6 (height 178 cm / 5'10", weight 97 kg / 214 lb). |
| 13 | Chronic gastroesophageal reflux disease | K21.9 | longstanding | Active, chronic | Acid-suppression indication on chronic medication list. |
| 14 | Chronic constipation tendency | K59.00 | longstanding | Active, chronic | Bowel-regimen therapy (osmotic + stimulant PRN) on home list. |

---

## ALLERGIES / INTOLERANCES

| Agent | Reaction | Interpretation | Source |
|-------|----------|----------------|--------|
| Lisinopril | Cough | ACE-inhibitor intolerance (class) | Carried-forward chart allergy entry |
| No known food allergies | — | — | Patient / family report carried forward |
| No known environmental allergies | — | — | Patient / family report carried forward |

---

## PROCEDURAL / SURGICAL HISTORY (CARRIED FORWARD)

| Procedure | Date | Facility | Notes |
|-----------|------|----------|-------|
| Percutaneous coronary intervention with drug-eluting stent placement (single vessel, mid-LAD) | 2018-09-12 | Mercy Vale Regional Medical Center | Legacy cardiology record; pre-Caldrane era. |
| Diagnostic polysomnography (PSG) | 2019-04-22 | Mercy Vale Sleep Center | Confirmed OSA; CPAP prescribed. |

---

## EXPLICIT NEGATIVES (CHART PROBLEM-LIST AND PROCEDURAL HISTORY)

The following are documented as **not present** on the imported problem list / procedural history at the time of this snapshot:

| Item | Status |
|------|--------|
| Implantable cardioverter-defibrillator (ICD) | no ICD |
| Cardiac resynchronization therapy (CRT) device | no CRT |
| Permanent pacemaker | no pacemaker |
| Coronary artery bypass grafting (CABG) | no CABG |
| Dialysis access (AV fistula, AV graft, tunneled catheter, peritoneal catheter) | no dialysis access |
| Major orthopedic repair (hip / knee / spine arthroplasty or fusion) | no major orthopedic repair |
| Amputation (any level) | no amputation |
| Temporal artery biopsy | no temporal artery biopsy |
| Major rheumatologic procedure | no major rheumatologic procedure |

---

## SOURCE-AUTHORITY AND HANDLING NOTES

This is a supplementary chart problem-list snapshot only. Interpretation guidance:

- Background texture only. Does not create new diagnoses and is not a final diagnosis hierarchy.
- Does not contain a medication list, dosing, or refill data. Does not establish home medication truth, final medication reconciliation, discharge medication list, GDMT restart timing, diabetes discharge regimen, or prednisone taper truth.
- Where PMR, chronic steroid exposure, or related items appear on this list, the wording is carried-forward problem-list language and does not outrank the locked prednisone source-of-truth hierarchy (rheumatology attending recommendation → verified medication reconciliation → pharmacy / refill history → family report → patient recollection).
- Onset dates are approximate import values carried forward from prior primary-care and specialty records. They are orientation values, not validated event dates.
- Where this snapshot conflicts with attending documentation, verified medication reconciliation, pharmacy history, consultant documentation, primary care documentation, family report, or patient recollection, the stronger source governs.

---

## GUARDRAILS

This supplementary problem-list snapshot must not be used to:

- create or finalize a discharge problem list;
- resolve PMR / prednisone ambiguity;
- replace rheumatology provenance;
- replace verified medication reconciliation;
- introduce new diagnoses or procedures not validated elsewhere in the chart;
- carry sole critical evidence for any disposition, restart, or safety decision.

No post-world information, discharge outcome, follow-up findings, task prompt, expected output, or grading material is contained in this snapshot.

---

*Electronically signed by Chart problem-list import | Medical Records | Mercy Vale Regional Medical Center | 2026-05-18*

---

**SYNTHETIC TRAINING DOCUMENT | FICTIONAL PATIENT | NOT A REAL MEDICAL RECORD**
