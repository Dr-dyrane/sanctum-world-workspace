# Next-World Selection Proposal (Internal Medicine) - verbatim record

Provenance: proposed by Alexander in session, 2026-06-12. Recorded verbatim (formatting normalized to markdown only). Answered by `next-world-candidate-scorecard.md` in this folder; planning surface is `internal-medicine-world-planning-canvas.md`. No world build follows from this document until Alexander explicitly authorizes it.

---

I want to narrow the next world from ten high-complexity US internal medicine case archetypes using the lessons from Korvin Merrow, the current task-design guardrails, and the newer source-of-truth guidance. The goal is not just to pick an interesting diagnosis. The goal is to pick the case that can support a comprehensive, chaotic, realistic hospital world with many moving parts: multiple services, attendings, residents, medical students, consultants, nursing, pharmacy, case management, CDI, HIM, payer pressure, family conflict, and raw-source contradictions.

The selection should prioritize worlds that can support at least 10 tasks across 5 or more task structures, with fair but difficult traps. We should avoid another world where the chart is built first and the tasks are forced in later. The case needs to be complex enough that the model has to reconcile many variables, but fair enough that failures come from available evidence, not hidden or planted misinformation.

## Selection Criteria

1. Supports at least 5 task structures, not mostly draft-and-finalize.
2. Uses raw source complexity rather than answer-key summary files.
3. Allows realistic external adversarial documents, such as CDI queries, payer denials, HIM worksheets, pharmacy rejections, and signouts.
4. Has forced slots: med disposition, principal diagnosis, CDI stance, payer appeal, discharge safety, quality abstraction, or safety review.
5. Has many legitimate stakeholders with conflicting but plausible priorities.
6. Can carry cold traps, not just obvious headline traps.
7. Allows off-text or low-salience evidence, such as photos, scanned forms, medication bottles, handwritten logs, or nursing uploads, if visible to both agent and grader.
8. Is reviewer-safe under recent guardrails: no false same-author draft content unless there are placeholders or explicit correction instructions.
9. Can create real clinical, safety, coding, documentation, or coverage failures, not cosmetic misses.
10. Feels like actual internal medicine hospital work in the United States.

## US Data Anchor

This shortlist is grounded in major US complexity and burden signals: AHRQ HCUP identifies septicemia, heart failure, acute MI, diabetes with complications, stroke, respiratory failure, renal failure, UTI, and CKD as major cost or readmission drivers. CMS emphasizes that medically complex chronic-condition patients require coordination across clinicians, specialists, facilities, testing, and therapy. CDC highlights chronic disease burden and diabetes-related amputation risk.

Sources: [AHRQ HCUP 2022 inpatient costs](https://hcup-us.ahrq.gov/reports/statbriefs/sb316-most-expensive-conditions-by-payer-2022.pdf), [AHRQ HCUP readmissions](https://hcup-us.ahrq.gov/reports/statbriefs/sb307-readmissions-2020.jsp), [CMS chronic condition SNPs](https://www.cms.gov/medicare/enrollment-renewal/special-needs-plans/chronic-conditions), [CDC chronic disease](https://www.cdc.gov/chronic-disease/about/index.html), [CDC diabetes amputations](https://www.cdc.gov/diabetes/diabetes-complications/preventing-diabetes-related-amputations.html).

## Ten Candidate Worlds

1. **Diabetic foot infection with limb threat.** Diabetes, PAD, CKD, sepsis, possible osteomyelitis, wound photo, vascular studies, antibiotics, renal dosing, offloading, amputation risk, discharge equipment, payer and SNF conflict. This is the strongest candidate for maximal task variety and real chaos.
2. **Obstructing stone urosepsis with AKI and anticoagulation bleeding.** Urosepsis, urgent stent, AKI on CKD, hematuria, AFib anticoagulation, delirium, discharge pressure, coding, CDI, payer denial, medication restart timing.
3. **Heart failure exacerbation with CKD, AFib, COPD/OSA overlap.** Diuresis versus renal injury, oxygen qualification, anticoagulation, CPAP, steroid or infection confounding, discharge weight, readmission risk.
4. **NSTEMI or acute MI with CKD, anemia, AFib, and HF.** Cath timing, contrast risk, bleeding risk, antithrombotic decisions, anemia workup, cardiac rehab, payer and coding tension.
5. **Respiratory failure from pneumonia versus COPD versus HF.** Oxygen need, steroid hyperglycemia, antibiotics, sepsis criteria, volume status, CPAP/O2 equipment, discharge safety.
6. **Cerebral infarction with AFib, dysphagia, fall risk, and rehab conflict.** Anticoagulation timing, aspiration risk, POA status, inpatient rehab versus SNF, caregiver disagreement, functional documentation.
7. **Cirrhosis decompensation with AKI, encephalopathy, infection, and malnutrition.** Lactulose, SBP, hepatorenal ambiguity, GI bleed, pressure injury, nutrition, CDI overreach, transplant-social constraints.
8. **Cancer patient with neutropenic fever, PE, thrombocytopenia, and goals-of-care pressure.** Antibiotics, cultures, anticoagulation threshold, platelet risk, oncology versus hospitalist priorities, palliative care conflict.
9. **Medical device or procedure complication.** Infected line, prosthetic joint infection, pacemaker or TAVR complication, anticoagulation confusion, procedure notes, ID, cardiology, surgery, and payer complexity.
10. **Alcohol use disorder or serious mental illness with medical decompensation.** Withdrawal, aspiration, malnutrition, infection, capacity, medication safety, unsafe discharge, Medicaid or self-pay readmission pressure.
