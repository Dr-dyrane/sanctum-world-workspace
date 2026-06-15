# OV03 text-reachable floor hunt - result: NO-GO (2026-06-15)

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

## Root cause (confirms the substrate limit, third time)
The 34-file chart states every contradiction, judgment, and required factor plainly and consistently, so the model (strong at cross-checking) catches anything loud. Only two failure shapes survive on this chart: COLD outside-knowledge (OV01 enoxaparin) and OFF-TEXT synthesis manufactured at the task layer (OV02 line infection). Both are used. The one remaining mechanism that could add a de-correlated floor - a CONFLICTING AUTHORITY (Edmund/Chen) - ceilings here because nothing is buried; that worked in Edmund/Chen only because their 80-file chart spread the rebuttals across competing sources. OV's chart does not.

## Recommendation
Close OV at its two real floors (OV01 + OV02 Path A). The high-value next move is the next world built conflict-first (buried, competing authorities + decoys + noise as the substrate from day one), which yields many fair, text-reachable floors by construction - the Edmund/Chen lesson. A third OV task is only available as a knowingly-correlated cold-med-rec catch, which adds no independent signal and risks a redundancy flag at review; not recommended.

## Note
No candidate survived the design filter, so no cold bench was spent (nothing to screen). This is a clean negative result, not an unscreened guess.
