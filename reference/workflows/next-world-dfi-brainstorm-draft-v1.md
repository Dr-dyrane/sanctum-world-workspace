# Brainstorm Draft v1: Limb-Threat Diabetic Foot Infection (World #2)

Status: DRAFT for Alexander's read-and-own pass. Markdown only; no DOCX, no submission, no platform action. Built strictly from Alexander's decision record (`next-world-dfi-decision-record-2026-06-12.md`), the ratified scorecard, and the filled canvas. Official template: four elements, concept-pitch scope. Strip the Draft Notes section before any DOCX is authorized.

World type: typical clinical (inpatient with post-discharge encounters). Snapshot: HD6 evening, date TBD at spec stage.

## 1. World setup

This is an inpatient hospital medicine world: a 6-day admission for a limb-threatening diabetic foot infection in a 68-year-old Spanish-preferred woman with long-standing insulin-dependent type 2 diabetes, CKD stage 3b, peripheral arterial disease, diabetic peripheral neuropathy, HFpEF, and limited mobility. She presents after roughly three weeks of outpatient wound deterioration. The course runs ED presentation, admission for IV antibiotics, podiatry soft-tissue debridement, vascular evaluation with perfusion questions still open, and steady improvement in infection markers. She lives in a second-floor walk-up; her adult daughter helps but works nights; insurance is Medicare Advantage with Medicaid secondary.

The world snapshot closes on hospital day 6 in the evening, at the point of maximal realistic tension: medically improving but operationally unsafe. Perfusion is not fully resolved, offloading is not reliably teach-backed, the home setup is poor, and payer, SNF, and DME issues are all active. Every task is an independent encounter anchored strictly after the snapshot: discharge-day work immediately after, administrative and payer surfaces 2 to 5 days out, and quality, referral, and safety-review work 1 to 3 weeks out.

## 2. Major friction points

- Hospital medicine versus the Medicare Advantage medical director (central): the payer reads improving markers after debridement as ready for home with home health; the treating team reads the same chart as unsafe without SNF-level wound care, offloading training, and equipment in place.
- Daughter versus PT/OT and case management (central): the daughter wants her mother home and offers real but night-shift-limited support; PT/OT findings, the second-floor walk-up, and wound-care frequency say home is not yet safe.
- Podiatry versus vascular surgery: debride, offload, and advance wound care now versus settle perfusion adequacy and revascularization sequencing before setting healing expectations.
- HIM/CDI versus the treating team: severity-capture pressure toward acute osteomyelitis and POA specificity versus the treating clinicians' documented restraint.
- Pharmacy benefit manager versus infectious disease: formulary substitution pressure versus a renal-safe antibiotic regimen at her eGFR.

## 3. Major traps

- Renal antibiotic dosing under a shifting eGFR. Contradictory/buried information: the MAR, creatinine trend, and ID note contradict a dose carried from admission renal function, and the tempting formulary substitute is unsafe at her eGFR. Lives in the med rec and pharmacy rejection tasks.
- Equivocal osteomyelitis with unsupported specificity. Insufficient/uncertain information: MRI shows marrow edema and says early osteomyelitis cannot be excluded; podiatry documents no exposed bone; no bone specimen; ID treats deep diabetic foot infection without signing acute osteomyelitis. Supported coding is diabetic foot ulcer with cellulitis/deep soft tissue infection; acute osteomyelitis requires treating-clinician clarification. World-level; primary in the coding and CDI tasks.
- Diabetic foot ulcer versus pressure injury code family, plus POA status. Source-of-truth ambiguity across wound care nursing, podiatry, and nursing skin assessments. Lives in the coding attestation and abstraction tasks.
- Vascular adequacy overstated. Contradictory EMR information: a palpable-pulse or Doppler-signal note reads reassuring while ABI/TBI values (noncompressible vessels) and the vascular consult keep perfusion genuinely open. World-level; bites the payer appeal, determination, and referral tasks.
- Offloading, teach-back, stairs, and DME readiness gaps. Buried significant information spread across PT/OT evaluations, nursing teaching notes, and case management; no single source states the disposition conclusion. World-level; bites the payer appeal, determination, safety review, and discharge-instruction tasks.
- Quiet quality-measure lookback disqualifier. Temporal complexity: one date or exclusion in the outpatient record contradicts naive numerator/denominator capture. Lives in the abstraction task.
- Culture provenance hierarchy. Source-of-truth ambiguity: superficial swab, deep tissue, and blood culture results carry different authority for antibiotic rationale. Lives in the med rec, CDI, and pharmacy tasks.
- SDOH context (language preference, night-shift caregiver, walk-up housing) is deliberately load-bearing context across discharge-safety tasks but never itself the scored trap.

## 4. Rough task ideas

Ten tasks, each an independent post-snapshot encounter, each named with its verbatim tracker workflow, structure, and forced slot. Workflow posture is Option A (clinically exact strings) with a standing disagreement note: the live guidance reads "at least 3-5 distinct workflows" as a floor, and consolidation would blur real, distinct physician-facing deliverables.

| # | Deliverable | Workflow (sheet verbatim) | Structure | Forced slot | Draws on | Anchor |
|---|---|---|---|---|---|---|
| 1 | Discharge medication reconciliation safety table | Discharge Medication Reconciliation | S2 forced inventory | Continue/hold/change/stop/defer per row | Renal dosing, culture provenance, insulin transition | Immediate |
| 2 | Physician coding attestation against the HIM preliminary worksheet | Inpatient Medical Coding and DRG Assignment | S2 forced inventory | Principal dx, POA, code family per row | Ulcer-vs-pressure-injury family, osteo POA restraint | Immediate |
| 3 | Attending response to a CDI query | Clinical Documentation Improvement (CDI) Query Response Review | S3 external ratify-or-refute | Agree, decline, or unable-to-determine per item | Osteo specificity, severity language, treating-voice restraint | 2-5 days |
| 4 | Physician appeal of the Medicare Advantage SNF-authorization denial | Claims Denial Analysis and Appeal Preparation | S3 external ratify-or-refute | Appeal, accept, or narrow | PT/OT, stairs, caregiver limits, wound-care frequency, DME timing, perfusion uncertainty | 2-5 days |
| 5 | Response to a pharmacy insurance claim rejection | Pharmacy Insurance Claim Rejection Resolution | S3 external ratify-or-refute | Substitute, appeal, hold, or exception | Renal-unsafe formulary substitute, interactions | 2-5 days |
| 6 | Physician-advisor continued-stay determination | Utilization Review Concurrent Stay Documentation | S4 determination | Binding continued-stay verdict | Designed borderline: improving markers versus unsafe operational picture | 2-5 days |
| 7 | Diabetes quality-measure chart abstraction | HEDIS Medical Record Chart Abstraction and Review | S5 extraction-to-schema | Value, exclusion, or unable-to-determine per field | Quiet lookback disqualifier | 1-3 weeks |
| 8 | Vascular surgery referral letter with required disposition table | Specialist Referral Letter and Documentation Preparation | S6 synthesis with embedded forced table | Table forces source-control, perfusion, antibiotics, offloading, follow-up statuses | Perfusion uncertainty, unresolved limb-threat items | 1-3 weeks |
| 9 | Safety review of a missed-offloading event | Patient Safety Event Investigation and Root Cause Analysis | S7 investigation | Attribution and prevention finding | Multifactorial system causes versus single-person blame | 1-3 weeks |
| 10 | Finalize discharge instructions from a started draft | Medical Transcription and Clinical Documentation Completion | S1 completion (the single allowed) | True placeholder on the scored decision; ratify or refute | Offloading/teach-back gaps; A0.4/A0.5 built-byte fairness gates | Immediate |

Structure spread: S1 x1, S2 x2, S3 x3, S4, S5, S6, S7 (seven distinct structures; completion capped at one). Nine of ten workflows are P0. Cross-cutting self-containment: no task requires public knowledge after July 31, 2025; payer criteria and external positions enter as realistic attached documents, and the world plans at least 30 raw-material world-level files with no answer-key synthesis shared.

## Draft notes (strip before DOCX)

- Cardiac comorbidity written as HFpEF; Alexander's decision allowed HFpEF or stable CAD; final pick (or both) at read-and-own.
- Cross-world rotation honored: photo is substrate only; coding core is ulcer-family/POA, not sepsis-to-principal; CDI core is osteomyelitis specificity, not encephalopathy-style addition.
- Task 6 exists in its own branch where she remains inpatient at day +2; tasks do not share one future timeline.
- Self-QC against `reference/checklists/brainstorm-checklist.md` pending after Alexander's ownership pass; then Brainstorm AutoQC per the official flow.
