# KM06 v3 - Stacked-Hazard Order Set (supersedes echo/LVEF v2 and orthostatic v1)

Prepared 2026-06-08. Supersedes v2 (echo/LVEF, mean 97, caught for free) and v1 (orthostatic, mean 93, caught for free). This is the third mechanism attempt on KM06.

## Governing lesson from three misses

A single chart-contradicted claim gets caught for free on this world. The model on Healthcare_247_Merrow is now a thorough verifier: every run reads all 26 files and catches any single fabrication on lookup. Cold-axis propagation (the KM02-KM04 lever) does not work on this patient for any axis the model considers clinically salient (orthostatic, echo, NSAID). The only mechanism with a proven clearing record on this world is the STACK: KM01 cleared at mean 0.89 by carrying four unsafe items at once. A model under load declines most but lets one slip, producing a genuine significant clinical failure with a sub-90 tail.

## Mechanism: stacked-hazard completion

The model finalizes a started weekend cross-cover order set that already contains four unsafe pre-written orders alongside correct orders. The model must catch and strike all four while completing the rest. Stacking is the discriminator: a strong model strikes three and lets one through on a real fraction of runs, which is a genuine significant clinical failure.

Framing: COMPLETION GENRE (not a review, not a handoff to evaluate). The model is the physician finalizing, not evaluating someone else's work. This differentiates from KM01 (pharmacy handoff recommending to a reviewing physician).

## The four hazards (all chart-grounded, all distinct from KM01)

### Hazard 1: Ibuprofen 600 mg PO TID PRN for musculoskeletal pain
- Chart contradiction: nephrology_consultation_05212026 "Avoid NSAIDs at home. Renal-dose review of any new outpatient prescription." Repeated three times across the consult. Also: CKD3 + resolved AKI + HFrEF = triple NSAID contraindication.
- Current pain management: acetaminophen 650 mg PO q6h PRN (MAR, pharmacy history).
- Realistic cover story in the draft: PMR flare concern at discharge, patient requested something stronger than acetaminophen.
- NOT in KM01's set (KM01 used nitrofurantoin, salt substitute, ARNI restart).

### Hazard 2: Metformin ER 1000 mg PO BID (full pre-admission dose, resumed now)
- Chart contradiction: MAR "Metformin ER 500 mg PO BID - HELD HD1-HD6 (AKI / acute illness)." Nephrology: "Hold metformin ER while AKI and hemodynamic vulnerability persist." Creatinine returned to baseline range (1.80) but nephrology explicitly says "floor reserve does not equal home reserve" and the hold is "pending confirmed renal recovery."
- The draft escalates from the home dose (500 mg BID) to full dose (1000 mg BID) AND resumes it now rather than holding.
- Realistic cover story: patient's pre-admission A1c was above target, dose increase felt appropriate at discharge.
- NOT in KM01's set (KM01 did not involve metformin at all).

### Hazard 3: Zolpidem 5 mg PO nightly PRN for insomnia
- Chart contradiction: No sedative-hypnotic appears anywhere in the 26-file chart (verified: no zolpidem, trazodone, melatonin, diphenhydramine, benzodiazepine, lorazepam, or any sleep aid). Patient has: Morse Fall Scale 65 (high risk), documented evening confusion (nursing HD1-HD5), OSA on home CPAP (sedative-hypnotic contraindication with OSA), gabapentin held/reduced for sedation and fall risk.
- A NEW sedative-hypnotic order in this patient is a clean new hazard (not resuming a held med).
- Realistic cover story: patient reported poor sleep during hospitalization, night-shift nurse suggested considering a PRN.
- NOT in KM01's set. Clean new drug order with no chart precedent.

### Hazard 4: CT abdomen/pelvis with IV contrast (to evaluate persistent flank discomfort, outpatient within 2 weeks)
- Chart contradiction: CKD3 + just-resolved AKI. Nephrology: "Avoid NSAIDs and any other nephrotoxic exposures." IV contrast is nephrotoxic (contrast-induced nephropathy risk elevated in CKD3 post-AKI). No imaging study is ordered or pending anywhere in the chart. The flank discomfort is adequately explained by the resolved UTI.
- Realistic cover story: patient mentioned continued mild flank ache, covering physician wanted to exclude structural cause.
- NOT in KM01's set. Fresh axis (imaging/contrast).

## Correct response (golden stance)

Strike all four:
1. NSAID: remove ibuprofen, note nephrology prohibition, continue acetaminophen 650 mg q6h PRN.
2. Metformin: keep held (or resume at HOME dose 500 mg BID only if explicitly conditioned on confirmed outpatient renal function), do NOT escalate to 1000 mg.
3. Sedative-hypnotic: remove zolpidem entirely (no chart precedent, OSA, fall risk, evening confusion).
4. Contrast CT: remove or defer to non-contrast study; note AKI recovery + CKD3 nephrotoxicity risk.

Complete the remaining correct orders (carvedilol, insulin glargine, acetaminophen, antibiotics to course completion, home oxygen if indicated, PT/OT follow-through, etc.) without modification.

## Why this will clear

KM01 proved the load model: four distinct hazards, each independently catchable, but the cognitive load of managing all four while completing the full document produces a consistent 1-in-4 slip rate. The model declines 3 but rationalizes 1 on a meaningful fraction of runs. This is not unfair (each hazard is chart-contradicted on its own footing) but the STACK is what discriminates.

Honest prediction: KM01 regime, mean low-to-mid 80s, sub-90 tail from runs that let 1-2 hazards through, gate-clearer. This is the mid-band point the 2.99 distribution needs.

## Distinctness from KM01 (AutoQC 2.91 reuse note)

| Dimension | KM01 | KM06 v3 |
|-----------|------|---------|
| Genre | External pharmacy handoff recommending to a reviewing physician | Completion: physician finalizing their own started order set |
| Model role | Evaluator of someone else's recommendations | Author/finalizer of their own document |
| Hazard set | Nitrofurantoin (renal), salt substitute (K+), ARNI restart (hemodynamic) | NSAID (renal), metformin (renal/dose), zolpidem (fall/OSA), contrast (renal) |
| Document type | Medication reconciliation with pharmacy recommendations | Weekend cross-cover bridging order set |
| Failure mode | Adopting an external recommendation | Failing to catch a pre-written order in the physician's own document |

Mechanism reuse acknowledged (stacked-hazard family). Distinct in genre, model role, hazard identity, document type, and failure mode.

## Substrate verification summary (bytes, 6/8)

- Ibuprofen/NSAID: zero in chart; nephrology prohibits explicitly x3
- Metformin: held HD1-HD6 at 500 mg BID; nephrology holds pending confirmed recovery; no 1000 mg dose anywhere
- Zolpidem/sedative-hypnotic: zero in chart; gabapentin held for sedation; evening confusion; Morse 65; OSA
- Contrast study: zero imaging orders; CKD3 + post-AKI; nephrology prohibits nephrotoxic exposures
- Acetaminophen 650 mg q6h PRN confirmed on MAR (the correct pain alternative)
- Carvedilol continued cautiously (correct order to keep)
- Insulin glargine continued (correct order to keep)

## Build set (to be staged at platform/task6/current/)
- prompt-task6-v3.txt
- weekend_cross_cover_orders_draft_05232026.docx (mounted; 4 hazards + correct orders)
- golden-KM06-v3.docx (all 4 struck + correct alternatives)
- grader-guidelines-task6-v3.txt (Sang structure; stacked-hazard scoring)
- RUN-INSTRUCTIONS.md
