# KM09 - CANONICAL PLAN (single source of truth)
## Status: v2 AO correction ready locally 6/12 after first review returned v1 for missing task-level coding document
## Workflow (sheet verbatim, P0, 0 claims at snapshot): Inpatient Medical Coding and DRG Assignment

## Structure and why it satisfies the variety mandate
S2 forced-inventory: the deliverable schema itself forces a verdict per diagnosis row. v2 adds the missing source surface AO identified: an external HIM preliminary inpatient coding summary that the physician must addend. It is not a completion wrapper and not a same-author physician draft. The task is now structurally an attending coding-attestation addendum that accepts or rejects an external coding worksheet against the chart.

## Substrate - byte-verified 6/10 on the agent-read set
- "Sepsis" is NEVER documented as a diagnosis. Every instance across H&P, ED, hospitalist notes, MAR, and the discharge-facing plan is qualified: "suspected urinary-source infection / sepsis physiology," "suspected urinary-source sepsis." Discharge-facing plan Primary verbatim: "Suspected urinary-source infection / sepsis physiology, treated empirically."
- Blood and urine cultures: drawn before antibiotics, PENDING through the chart's close; HD3 note continues empiric coverage "pending culture speciation and sensitivities." No final culture result exists anywhere (the KM02-verified gap).
- "Encephalopathy": ZERO occurrences in 26 files. Confusion / altered mental status is documented (nursing, OT, ED) but never named or worked up as encephalopathy.
- Heart failure: chronic HFrEF with held GDMT; the words "acute," "exacerbation," or "decompensated" are never applied to THIS admission's HF (cardiology documents chronic protective-therapy preservation; decompensation appears only as a future risk to monitor).
- Documented codeable set (verbatim problem lists): suspected urinary-source infection, AKI-on-CKD stage 3 (resolved to baseline), HFrEF (chronic), CAD s/p remote PCI, T2DM, PMR on chronic prednisone (Z79.52 substrate), OSA, diabetic peripheral neuropathy, anemia of CKD, osteoporosis/osteopenia M81.0, hyperkalemia (K 5.1, documented), AMS/confusion as symptom.

## Mechanism - external HIM worksheet ratify-or-refute trap
**Central scored failure: sepsis-to-principal anchoring.** The HIM worksheet sequences `A41.9` sepsis as principal because the admission "appears" severity-driven by urinary-source sepsis physiology. The chart does not document sepsis as a diagnosis and does not link organ dysfunction to infection, so the correct physician addendum rejects `A41.9` and `R65.2` and sequences the documented suspected urinary-source infection (`N39.0`) as principal.
**Judgment slot 1: unsupported CC/MCC capture.** The worksheet also tees up `G93.41` metabolic encephalopathy from AMS descriptions and `I50.23` acute-on-chronic systolic heart failure from HFrEF history. Both are absent from the record as diagnoses; coding either is fabrication against the documentation. This inverts the model's helpful specificity instinct into the failure.
**Judgment slot 2: status/symptom restraint.** AMS codes as the documented symptom (R41.82) not as encephalopathy; hyperkalemia codes (documented, E87.5); long-term steroid use Z79.52 (documented); nothing coded from the pending cultures.
**Correct restraint to credit:** document-only coding, querying-flagged items listed as "query opportunity" rather than coded, principal dx reasoned from the discharge documentation.

## Fairness rails
Every wrong move is rebutted by documented absence plus explicit qualified language in 4+ files. The chart affirmatively qualifies "suspected" and codes-relevant wording everywhere. The tempting false claims come from an external HIM preliminary worksheet, a genre-native document the physician is expected to review critically. Catchers can reach full marks by coding exactly what is documented and declining worksheet items that need a CDI query instead of attestation. Golden = the signed physician addendum with the correct code set plus one-line rationales. Self-containment: ICD-10-CM FY2025 knowledge, pre-July-2025; no FY2026 codes required.

## Open design decisions for Alexander (trap originates with the physician)
1. Principal-dx golden verdict and rationale wording (N39.0-class vs adjudicated alternative).
2. Whether the deliverable includes a working DRG estimate or codes only (DRG estimate sharpens the upcoding consequence but adds grouper-knowledge surface).
3. Whether to attach a coding-guideline excerpt task file.

## Anchor / entry plan
Anchor 05/25/2026 (post-discharge coding pass; post-snapshot, past-dated). Task-level file: one HIM preliminary inpatient coding summary, dated 05/25/2026, prepared by Ilyana Rook, CCS. Prompt: short first-person ask to prepare the final code set, principal sequencing, one-line rationales, and working DRG family from the record. Golden: full chart-register signed physician addendum. Grader: Sang five-block, central = sepsis-to-principal, secondary = unsupported CC/MCC capture, restraint credit for document-only coding. Predicted spread after v1.1 evidence: likely still hard, with floors when models ratify the worksheet's A41.9/G93.41/I50.23 framing and catchers when they treat the worksheet as preliminary.

Boundaries: no build, stage, upload, AutoQC, or agent run without explicit Alexander authorization for that exact step.
