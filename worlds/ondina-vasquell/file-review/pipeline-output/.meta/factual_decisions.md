# Factual Decisions — Invented Facts and Rationale

This log records every fact NOT explicitly fixed in the spec or reference files, with a brief
rationale for the chosen value. Every invented fact preserves internal consistency with the
spec-fixed canon (MRN, DOB, allergies, lab values, snapshot time, provider roster, file
inventory, perfusion findings, pathology, ID stance, PT/OT findings).

## Institution

- **Hospital name: Harbor Crest Regional Medical Center** — Already established in every
  reference file letterhead. NOT invented; canon.
- **Hospital address: 2400 Mariners Bay Boulevard, Cypress Harbor, FL 33421** — Invented.
  Florida placement is consistent with the implied "general US setting" with Spanish-preferred
  Hispanic patient population and Medicare Advantage HMO prevalence; coastal mid-sized
  metro reads plausibly with "Harbor Crest" name.
- **Hospital main phone (561) 555-0100** — Invented. 561 area code is South Florida (Palm
  Beach County), consistent with the implied location.
- **EIN 59-3027841** — Invented. 59-prefix EINs are common for Florida-issued entities.
- **Facility NPI 1023881744** — Invented, format-valid 10-digit Type-2 NPI.
- **Unit 6 South Medicine / Room 6S-214** — From reference file headers; canon.

## Patient additions

- **Patient address: 1418 Calle del Mar, Apt 2B, Cypress Harbor, FL 33421** — Invented.
  Spanish street name acknowledges Spanish preference and Hispanic neighborhood; Apt 2B is
  consistent with the spec-fixed second-floor walk-up.
- **Patient home phone (561) 555-0274** — Invented; consistent area code.
- **Late husband Joaquín Vasquell, died 2023-11-18** — Invented. Spec states "her late
  husband had been her main support." A modest grief window (about 2.5 years) is plausible
  and explains why the daughter has become the primary partial caregiver. Spanish given
  name consistent with family.

## Daughter (Marisela Vasquell)

- **Phone (561) 555-0388** — Invented.
- **Address 247 Egret Cove Lane, Cypress Harbor, FL 33421** — Invented; same city consistent
  with daytime helper role.
- **Occupation: Certified Nursing Assistant, night shift, Bayside Skilled Care** — Invented.
  CNA role plausibly explains the night-shift schedule, bilingual capacity, and willingness
  but partial availability; deepens the irony of the SNF discussion (she works at one but
  cannot deliver care at home overnight).

## Insurance

- **Primary plan name: Crestline Medicare Advantage HMO** — Invented. Spec fixes "Medicare
  Advantage primary."
- **Member ID CMA-7728-4416-02; group FL-MA-2026** — Invented format-plausible identifier.
- **Secondary: Florida Medicaid, member FL-MCD-883204117** — Invented; Florida placement
  consistent with hospital.
- **PBM: Meridian Rx Benefit Solutions, RxBIN 610591, RxPCN MRBS, RxGroup CMA2026FL** —
  Invented PBM identifiers in standard format.

## Preferred pharmacy

- **Cypress Harbor Community Pharmacy, 812 Marina Way** — Invented. A community pharmacy is
  the realistic dispense channel for an oral discharge antibiotic.

## Care team additions (not in spec roster but implied)

- **Florencia Beltrán, certified Spanish medical interpreter** — Invented. Spec states
  interpreter used throughout but does not name them.
- **Dr. Vivienne Karras, physician advisor** — Invented. Task 6 is requested by "the
  physician advisor" with no name in the spec roster.
- **Annaliese Pintar, RN, BSN — quality / HEDIS abstraction nurse** — Invented. Task 7 is
  requested by "the quality abstraction nurse."
- **Mateo Quiñones, MHA, CPPS — patient safety officer** — Invented. Task 9 is requested by
  "the patient safety officer." CPPS credential is appropriate.
- **PCP: Esmeralda Torres-Hidalgo, MD — Bayfront Community Internal Medicine, 915 Pelican
  Drive** — Invented. Outpatient PCP summary references "Primary Care" without naming.
- **Ophthalmologist: Sergio Maldonado, OD — Harbor Vista Eye Care** — Invented. Eye exam
  report references "Ophthalmology" without naming.

## Provider NPIs and pagers

- All NPIs (1457629831 etc.) and pagers (561 555-05xx) are invented in format-valid form.
  Pagers cluster in a single hospital block; NPIs are unique per provider.

## Accession numbers (already in references)

- **HCR-VAS-05193320 (ABI/TBI), HCR-IMG-05181844 (MRI; corrected from prior typo
  HCR-IMG-05261844 — see QA-correction subsection below for MMDD-convention rationale),
  HCR-MIC-26-51744 (deep tissue), HCR-MIC-26-51621 (superficial), HCR-SP-26-0517
  (pathology), FIN-2207733** — All from reference file headers; canon, not invented.

## External correspondence identifiers

- **CMA case reference CMA-UM-2026-447128** — Invented format-plausible.
- **PBM claim number MRX-2026-RX-991274** — Invented.
- **PBM rejection code 75 (Prior Authorization Required)** — Standard NCPDP rejection code
  family; chosen because it routes to a prescriber response (Task 5 expected output).
- **PBM preferred substitute: TMP-SMX DS oral** — Inferred from spec's "payer-preferred
  antibiotic substitute unsafe on renal or allergy grounds" + culture susceptibilities
  showing TMP-SMX as "susceptible" alongside the sulfa-allergy flag. This is the only
  substitute that satisfies (a) susceptibility per deep-tissue culture, (b) oral discharge
  formulary appeal, (c) sulfa-allergy and renal trap design.
- **Appeal deadline 2026-06-22 (30 days from 2026-05-23 issue)** — Standard Medicare
  Advantage appeal window.

## Non-clinical narrative connective tissue

- Spanish-language patient-facing register is preserved as a stylistic note, not a
  fabrication.
- Hospital department list is consistent with what appears in reference files.

## QA-review corrections (applied 2026-06-14)

The following notes record edits made in response to QA review feedback. None of
them invents new facts that contradict spec canon; they resolve gaps or
typos identified in the initial pass.

- **MRI accession corrected to HCR-IMG-05181844.** The original value
  `HCR-IMG-05261844` embedded "0526" but the MRI was performed on 2026-05-18.
  The accession-number convention across imaging/vascular/pathology IDs is
  HCR-{modality}-MMDDxxxx (HCR-VAS-05193320 = 05/19; HCR-SP-26-0517 = 05/17),
  so 0518 is the correct MMDD prefix. The trailing "1844" sequence is retained.

- **Procedural history added to the spine as spec canon, not invention.**
  Spec §1.3 paragraph 4 explicitly states: "the only procedure this admission
  is the hospital-day-two podiatry soft-tissue debridement. There is no prior
  amputation, no revascularization or bypass, no dialysis access, and no
  other major surgical history; the absence of a prior amputation is itself
  relevant, because this is her first limb-threat presentation." This is now
  encoded under the new top-level key `procedural_history` so it can be
  surfaced in the Task 8 vascular referral letter and the Task 4 SNF appeal,
  both of which depend on the "first limb-threat" framing. NOT invented.

- **Task 7 quiet disqualifier resolved: HEDIS Advanced Illness + Frailty
  member-level exclusion applied per EW23 documentation.** (Revised after
  QA review — the prior framing, which declared uACR absent throughout the
  chart and marked the KED nephropathy field NOT MET, has been withdrawn
  because it contradicted spec §Task-7 Failure Design row "Nephropathy
  capture missed | Capture the documented CKD and proteinuria evidence
  (renal record)" and spec §Task-7 grader anchors "the eye-exam, HbA1c,
  and nephropathy fields are abstracted to the documented evidence.")
  The spec describes the disqualifier as a "lookback-window OR exclusion
  detail that changes capture" (spec §Task-7 Failure Design table, row 1).
  Chosen disqualifier: the HEDIS Comprehensive Diabetes Care (CDC) family —
  Eye Exam for Patients with Diabetes (EED), Glycemic Status Assessment
  (GSD), Kidney Health Evaluation (KED), Blood Pressure Control (BPD),
  and Statin Therapy (SPD) — provides an OPTIONAL member-level exclusion
  for members age 66+ who have BOTH a HEDIS-qualifying advanced-illness
  diagnosis AND a frailty diagnosis documented during the measurement
  year. The patient meets all three criteria simultaneously:
    - Age 68 (≥66 HEDIS threshold).
    - HFpEF documented as a HEDIS-qualifying advanced-illness diagnosis
      in EW23 outpatient PCP summary with the required outpatient
      encounter context inside the measurement year.
    - Frailty per documented "limited mobility at baseline" (spec
      comorbidity rank 14) and abnormal-gait / deconditioning findings,
      consistent with the HEDIS frailty value-set.
  Rationale for picking THIS disqualifier:
    - It is a real, named HEDIS exclusion rule with documented multi-
      component requirements (advanced illness + frailty + age 66+).
    - It uses EW23 (already in the world) as the source of the
      qualifying diagnoses — does not require new world-level evidence.
    - It is genuinely upstream of numerator capture, matching the
      spec's "lookback or exclusion detail that CHANGES capture" framing.
    - It does NOT contradict spec §Task-7 row 5 — proteinuria evidence
      remains in the renal record and the nephropathy field is still
      abstracted to documented CKD + proteinuria per spec.
    - It does NOT contradict the patient's Full Code status: HEDIS
      Advanced Illness + Frailty exclusion is an administrative measure-
      eligibility classification, not a clinical care-preference
      designation. Active treatment continues normally.
    - It does NOT contradict the spec-fixed HbA1c value (8.6%) or eye-
      exam date (03/15/2026); those fields remain capturable and are
      reported per the documented evidence.
  Downstream implication: when E1-T7 (quality_abstraction_worksheet_
  06042026) is authored, the worksheet must include a measure-eligibility
  / exclusion field that the abstractor can mark with the exclusion.
  EW23 outpatient PCP summary (04/30/2026) must document (a) HFpEF with
  the required outpatient encounter context per HEDIS CDC specs (e.g.,
  a HF-related specialist follow-up or visit code within the measurement
  year), (b) a frailty / abnormal-gait diagnosis consistent with the
  HEDIS frailty value-set (e.g., abnormality of gait R26.x, repeated
  falls, or muscle weakness), and (c) proteinuria evidence in the renal
  record (e.g., dipstick or qualitative microalbumin note) per spec
  §Task-7 row 5. EW17 renal trend retains its current eGFR documentation
  and may include a proteinuria flag if appropriate.

- **Care team count clarification.** The narrative summary I returned to the
  user stated "15 named providers + interpreter + daughter," which undercounts
  the spine. The `care_team` array contains 17 named providers (Everet,
  Renquist, Vell, Mwangi, Brusk, Saafeld, Olwyn, Achara, Pruvost, Mabari,
  Defreze, Ndiaye, Adeyle, Stovall, Karras, Pintar, Quiñones) plus the
  interpreter (Beltrán) and the daughter (Marisela) = 19 entries total. The
  three additions beyond the spec's 14-name roster (Karras as physician
  advisor, Pintar as quality nurse, Quiñones as patient safety officer) are
  required for Tasks 6, 7, and 9, which the spec assigns to those roles
  without naming the individuals. All three were invented intentionally and
  recorded above. The correct count statement is "17 named providers +
  interpreter + daughter."

- **GERD added as comorbidity rank 13.** The spec's Comorbidity Profile
  lists 13 items ending at "Limited mobility at baseline." The spine's
  `comorbidity_profile` adds GERD as rank 13 (pushing "Limited mobility at
  baseline" to rank 14) to support the spec-fixed pantoprazole row on the
  home medication list. This is a structural expansion of the spec's
  13-item profile but does not contradict it; pantoprazole 40 mg daily
  requires an indication, and GERD is the only plausible one given the
  rest of the chart. Kept rather than reduced because Task 1's discharge
  medication reconciliation should explain why pantoprazole is continued.

- **Honorific convention documented in global_style.** English clinician-voice
  documents and draft prompts use "Mrs. Vasquell" (consistent with every
  spec draft prompt). Spanish-language patient-facing materials use
  "Sra. Vasquell." The patient.preferred_name field stores the Spanish form
  for patient-facing use; English clinical documents should use "Mrs." This
  is now stated explicitly in `global_style.honorific_convention` so
  downstream writers do not produce mixed-register documents.

## Facts explicitly NOT invented (governed by canon)

- All lab values (Cr, eGFR, WBC, CRP, Hgb, A1c, glucose, BUN, K, temp, HR, BP, RR, SpO2).
- All medication doses, routes, frequencies, indications, and hold/continue status.
- All perfusion findings (ABIs noncompressible, TBI 0.50/0.84, toe pressures 55/92).
- All culture organisms and susceptibilities.
- All MRI findings and impression language (equivocal).
- All pathology findings (no bone in specimen).
- All PT/OT findings (stairs not safe; teach-back not achieved).
- All case management barriers.
- All task anchor dates and times.
- Snapshot at 2026-05-21T18:00:00.
- Provider roles and task assignments.
- File inventory and IDs (EW1-EW31, E1-T1 through E1-T10, WS1-WS3).
- Sulfa allergy with rash.
- DOB 1958-03-14, MRN OV-3358104, FIN-2207733.
- Daughter Marisela; widowed; second-floor walk-up.
- Medicare Advantage primary, Medicaid secondary.
