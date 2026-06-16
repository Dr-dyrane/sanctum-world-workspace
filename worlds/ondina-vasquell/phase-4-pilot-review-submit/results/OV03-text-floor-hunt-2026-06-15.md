# OV03 text-reachable floor hunt - result: NO-GO (2026-06-15)

> SUPERSEDED (2026-06-15): the "no de-correlated third floor / world substrate-capped" conclusion below is WRONG. This hunt searched the FROZEN CHART for a buried gap and never tried the KM over-closure recipe on an UN-PRIMED axis; that recipe (CPAP/OSA over-closure) then bench-floored 3/3. The candidate-by-candidate analysis is kept for history. Canonical: worlds/ondina-vasquell/OV-FLOOR-MECHANISM-LIBRARY.md.

User chose "hunt a text-reachable OV03" after the image-miss OV03 draft was rejected (blind harness). I read the full canonical chart (build/clinical_data.py, all 29 world files + 3 supplementary) and looked for a floor that is: text-reachable (no image dependence), fair (penalizing the miss is defensible), reliably missed by a cold text reviewer (reviewer-miss = floor; reviewer-catch = ceiling), and de-correlated from OV01 (cold drug-stop) and OV02 (off-text line-infection synthesis).

Result: no candidate clears all four bars.

## Candidates examined and why each fails
- Stop vancomycin / pip-tazo (MSSA not MRSA; de-escalate): borderline-fair (MAR shows all three "active" during an in-progress de-escalation; ID frames narrowing as ongoing), pilot behavior was mixed (some runs de-escalated), and it is the same med/antibiotic-reasoning event as OV01/OV02. Not a reliable de-correlated floor.
- Cefepime too broad / narrow to cefazolin: ID explicitly frames narrowing as future ("a narrower agent is appropriate as the course continues"), so not-narrowing-now is not a current error -> unfair to penalize; stewardship-aware models catch it -> ceiling risk.
- Gabapentin 300 mg TID at eGFR 36: 900 mg/day is within the accepted CrCl 30-59 range -> not an error -> unfair.
- Clopidogrel (DAPT) without prior intervention: established home regimen; DAPT in PAD is a real clinical debate, not a clear error -> unfair to flag; med-rec (OV01 family).
- Empagliflozin amputation-risk / permanent reconsideration: signal is weaker for empagliflozin than canagliflozin and contested; chart already holds it with "restart later" -> covered/fuzzy -> unfair.
- Anemia of CKD / ESA / iron studies: chart explicitly flags it as an open item -> model copies it -> not missed -> ceiling.
- Osteomyelitis duration / soft-tissue course: chart states "not established, soft-tissue, duration not finalized" plainly -> model copies -> ceiling (already bench-killed as OV-ABX).
- Culture hierarchy (superficial mixed flora vs deep MSSA+GBS): model reliably catches this (demonstrated in the OV02 pilots) -> ceiling.
- Conflicting-authority covering note ("infection resolved, de-escalate and discharge home"): every rebuttal (osteo not excluded, perfusion unresolved, teach-back failed, home unsafe) is LOUD in the chart, so the model cross-checks and catches -> ceiling. This is the OV04/OV06 profile, already proven to ceiling.
- Silent home-med omission (ferrous sulfate / cholecalciferol absent from the MAR): minor materiality and OV01 med-rec family -> correlated, low value.
- Enoxaparin stop: this is OV01's lever -> excluded by de-correlation.

## Root cause (bounds the FROZEN-CHART hunt, not the world)
The 34-file chart states every contradiction, judgment, and required factor plainly and consistently, so the model (strong at cross-checking) catches anything loud on the frozen chart. The chart-resident failure shapes found are COLD outside-knowledge (OV01 enoxaparin) and OFF-TEXT synthesis manufactured at the task layer (OV02 line infection). Both are used. A CONFLICTING AUTHORITY (Edmund/Chen) ceilings here because nothing is buried in the chart; that worked in Edmund/Chen only because their 80-file chart spread the rebuttals across competing sources. This bounds the levers hunted on the frozen chart, not the world: additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY).

## Recommendation
Manufacture the next OV floors at the task layer rather than hunting them on the frozen chart. Buried, competing authorities + decoys + noise as a TASK-LEVEL substrate (the Edmund/Chen lesson) yields many fair, text-reachable floors by construction. Additional floors are manufactured at the task layer, not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY). A purely chart-gap third OV task is only available as a knowingly-correlated cold-med-rec catch, which adds no independent signal and risks a redundancy flag at review; not recommended.

## Task-layer lever TESTED (not just chart-gaps): cross-talk contamination -> CEILINGS
After the chart-gap no-go, reopened the hunt at the TASK LAYER (where OV02's floor was manufactured), per the correct objection that the frozen chart is not the whole lever space. Designed and cold-benched the strongest untried Edmund/Chen mechanism: WRONG-PATIENT / CROSS-TALK CONTAMINATION. A task-level antimicrobial-stewardship cross-cover sheet covers three 6-South patients interleaved; the 6S-216 neighbor is near-identical (also a diabetic-foot infection) but carries MRSA bacteremia on vancomycin with a penicillin allergy. Vasquell (6S-214) is MSSA+GBS, cefepime, sulfa allergy, and her chart has an open slot (ED blood cultures drawn, no result recorded). Intended floor: the model fills her empty blood-culture slot with the neighbor's MRSA bacteremia and escalates to vancomycin (wrong-patient safety error).

Cold bench (2 independent strong models, harness-matched, no golden/grader): BOTH segregated cleanly. Neither contaminated; both used only Vasquell's MSSA/cefepime/sulfa, both left the blood cultures as no-result/pending, and BOTH SPONTANEOUSLY FLAGGED the cross-talk as a hazard ("confirm this is filed under 6S-214, not the 6S-216 MRSA-bacteremia neighbor"). That is a clean unprompted reviewer-CATCH = CEILING (the OV04 rule). The model actively guards against labeled patient mix-ups; cross-talk is not a blind spot on a clean-chart world. Killed on the bench, no pilot spent.

## Converging conclusion (three independent lines)
(1) chart-gap hunt = no-go; (2) cross-talk task-layer lever = bench-ceiling; (3) conflicting-authority = ceilings because this world's rebuttals are all loud (OV04/OV06 proven). The chart-resident blind spots this model shows on this clean 34-file world are COLD outside-knowledge (OV01) and COMPLETION-FRAME off-text synthesis (OV02). Both are used. A de-correlated third floor was not found by hunting the frozen chart on current evidence. The mechanisms that would add one (cross-talk, conflicting-authority, buried rebuttal) are manufactured at the task layer, where the index data is NOT cleanly available in the task-level artifact - additional floors are not capped by the chart (see OV-FLOOR-MECHANISM-LIBRARY).
