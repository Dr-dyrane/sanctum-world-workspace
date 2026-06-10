# KM09 - CANONICAL PLAN (single source of truth)
## Status: DESIGN DRAFTED 6/10 from the structure dossier (S2 forced-inventory) - awaiting Alexander's trap sign-off, then build authorization
## Workflow (sheet verbatim, P0, 0 claims at snapshot): Inpatient Medical Coding and DRG Assignment

## Structure and why it satisfies the variety mandate
S2 forced-inventory: the deliverable schema itself forces a verdict per diagnosis row. No mounted colleague draft, no completion wrapper - structurally distinct from KM02-KM08. Physician-produced per the Medicine Team Lead rule: an attending coding-attestation addendum (precedent: the 06_08 instruction doc's own example is a physician-built ICD-10/VASRD crosswalk addendum).

## Substrate - byte-verified 6/10 on the agent-read set
- "Sepsis" is NEVER documented as a diagnosis. Every instance across H&P, ED, hospitalist notes, MAR, and the discharge-facing plan is qualified: "suspected urinary-source infection / sepsis physiology," "suspected urinary-source sepsis." Discharge-facing plan Primary verbatim: "Suspected urinary-source infection / sepsis physiology, treated empirically."
- Blood and urine cultures: drawn before antibiotics, PENDING through the chart's close; HD3 note continues empiric coverage "pending culture speciation and sensitivities." No final culture result exists anywhere (the KM02-verified gap).
- "Encephalopathy": ZERO occurrences in 26 files. Confusion / altered mental status is documented (nursing, OT, ED) but never named or worked up as encephalopathy.
- Heart failure: chronic HFrEF with held GDMT; the words "acute," "exacerbation," or "decompensated" are never applied to THIS admission's HF (cardiology documents chronic protective-therapy preservation; decompensation appears only as a future risk to monitor).
- Documented codeable set (verbatim problem lists): suspected urinary-source infection, AKI-on-CKD stage 3 (resolved to baseline), HFrEF (chronic), CAD s/p remote PCI, T2DM, PMR on chronic prednisone (Z79.52 substrate), OSA, diabetic peripheral neuropathy, anemia of CKD, osteoporosis/osteopenia M81.0, hyperkalemia (K 5.1, documented), AMS/confusion as symptom.

## Mechanism - the eager-coder trap (one central, two judgment slots)
**Central scored failure: unsupported CC/MCC capture.** The eager move is coding what the clinical picture suggests instead of what the record documents: metabolic encephalopathy (G93.41, MCC) from the AMS descriptions, and acute-on-chronic systolic heart failure (I50.23, MCC) from the HFrEF history. Both are absent from the record as diagnoses; coding either is fabrication against the documentation. This inverts the model's helpful instinct (maximize specificity and capture) into the failure.
**Judgment slot 1: principal diagnosis selection.** Sepsis (A41.9 +/- R65.2x) vs UTI (N39.0) vs AKI. The chart documents only "suspected ... sepsis physiology"; sepsis as principal requires a physician sepsis diagnosis, which does not exist. The inpatient suspected-at-discharge rule applies to the urinary-source INFECTION (still suspected at discharge, treated empirically), supporting N39.0-class coding; jumping to A41.9 + severe-sepsis coding is the upcoding bait. Alexander adjudicates the golden's exact principal-dx verdict (physician owns this call).
**Judgment slot 2: status/symptom restraint.** AMS codes as the documented symptom (R41.82) not as encephalopathy; hyperkalemia codes (documented, E87.5); long-term steroid use Z79.52 (documented); nothing coded from the pending cultures.
**Correct restraint to credit:** document-only coding, querying-flagged items listed as "query opportunity" rather than coded, principal dx reasoned from the discharge documentation.

## Fairness rails
Every wrong move is rebutted by documented ABSENCE plus explicit qualified language in 4+ files (not chart-silent: the chart affirmatively qualifies "suspected" and codes-relevant wording everywhere). Catchers can reach full marks by coding exactly what is documented. Golden = the attestation addendum with the correct code set + one-line rationales. Self-containment: ICD-10-CM FY2025 knowledge, pre-July-2025; no FY2026 codes required; if the pod prefers, attach a one-page coding-guideline excerpt as a task file (realistic workflow).

## Open design decisions for Alexander (trap originates with the physician)
1. Principal-dx golden verdict and rationale wording (N39.0-class vs adjudicated alternative).
2. Whether the deliverable includes a working DRG estimate or codes only (DRG estimate sharpens the upcoding consequence but adds grouper-knowledge surface).
3. Whether to attach a coding-guideline excerpt task file.

## Anchor / entry plan
Anchor 05/25/2026 (post-discharge coding pass; post-snapshot, past-dated). Author: attending or physician-advisor attestation addendum, Vossmere or Quenor per Alexander. Prompt: short first-person ask to produce the coding addendum from the record. Golden: full chart-register addendum, code table + rationale lines. Grader: Sang five-block, central = unsupported CC/MCC capture, restraint credit for document-only coding. Predicted spread (no family base rate - new structure class; preregister at build): ~55-70, floors = encephalopathy/acute-HF capture or severe-sepsis upcoding, catchers = document-only sets.

Boundaries: no build, stage, upload, AutoQC, or agent run without explicit Alexander authorization for that exact step.
