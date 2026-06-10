# KM06 - substrate verification + crystallized mechanism (6/8)

Deep slot. Mechanism: omission + red-herring patient-safety / readmission-risk review. Fail = miss a buried surveillance gap and over-weight a loud non-contributor. Grounded on agent-read bytes from `file-review/upload/filesystem/*.docx` (python-docx, paragraphs + table cells), not markdown. Locked canon: TP-KM06, EO-KM06, Golden-KM06, GG-KM06, FI-T06.

## Verified substrate (every item is in the chart)

Bone-health / osteoporosis (the gap carrier):
- Osteoporosis/osteopenia related to chronic steroid exposure (M81.0), active since ~2021. Problem list #11; H&P; primary care baseline.
- Anti-fracture therapy: alendronate 70 mg weekly (Sunday) + calcium carbonate/vitamin D 600/400 BID. Confirmed in initial med rec (item 12/14), pharmacy refill history, rheumatology provenance, MAR.
- CRITICAL: MAR records alendronate "weekly (Sunday) - NOT administered inpatient (outpatient chronic, reconcile)." The one anti-fracture drug is held inpatient and flagged only "reconcile" - at risk of accidental long-term omission at discharge.
- Endocrinology consult names bone health as a live domain "already partially addressed with alendronate and calcium/vitamin D" - i.e., partially, not closed.
- NO DXA / DEXA / T-score / FRAX / bone-density study anywhere in the 26 files. There is no documented fracture-risk surveillance and no discharge owner for it.

Fall / event (the anchor, no invention needed):
- Recurrent near-fall 05/17/2026 at home (rose from a kitchen chair), lightheadedness - documented across ED triage, ED provider, H&P, cardiology, nephrology, PT, OT.
- High ongoing fall risk: PT Morse Fall Scale 65 (high-risk). Inpatient fall precautions, bed alarm, transfer assistance, evening observation (HD1-HD3). Gabapentin held/reduced selected days for "mentation, fall risk."
- No actual in-hospital fall is documented (only precautions). Good: the mechanism needs the absence of surveillance, not an invented inpatient event. The +30 anchor stays a review frame; no readmission/outcome is invented.

Red herring (loud, chart-grounded non-contributor):
- The prednisone / steroid-source saga is the loudest thread in the record (10+ hits per file): unresolved provenance, Endocrinology caution vs primary-team mixed-physiology read, rheumatology (Halvek) record, pharmacy fills at two strengths. Dramatic, multi-consultant, tempting to headline.
- Per GG-KM06 it must stay BACKGROUND ("not that adrenal insufficiency is proven"). Over-weighting it - turning the safety review into "the consultants disagreed about steroids" or an RCA of the steroid question - is the red-herring failure.

## Crystallized mechanism

Buried surveillance gap (the omission, scored): a chronic-steroid osteoporosis patient (since 2021) with the highest fall risk on file (Morse 65) and a recurrent near-fall, whose only anti-fracture agent (alendronate) was held inpatient and flagged merely "reconcile," and for whom no bone-density surveillance, fracture-risk reassessment, or discharge owner of fall-and-fracture prevention exists. A strong safety review surfaces this distributed fall-plus-fracture surveillance gap and the accidental-omission risk on alendronate. A weak one misses it because each piece is quiet and spread across PT (Morse), MAR (alendronate held), problem list (osteoporosis), and endo (bone health "partially addressed").

Red herring (the over-weighted non-contributor, penalized): the steroid-provenance / Endo-vs-Primary drama, loud and multi-document, a real uncertainty but not the buried safety gap. Making it the headline, or treating the review as an RCA of it, is the scored failure.

Bright line: no invented +30 readmission, adverse event, recovery course, or root-cause finding. The review identifies pre-discharge risk signals only.

## Why this is the deep slot (honest difficulty rationale)

Unlike Tasks 1-5 (one planted fact in a mounted draft, near-binary catch), KM06's failure is misallocation of attention plus omission: chase the loud steroid thread, miss the quiet fall/fracture gap, and/or let alendronate fall off the plan with no surveillance owner. There is no single false fact to catch, so a careful comprehensive reviewer cannot ace it by simple fact-checking; it must correctly DOWN-weight the loud thread and UP-weight the distributed quiet one. That is intrinsically harder and is the sub-60-capable lever the suite needs.

## Open questions for red-team (before authoring prompt/grader/golden)

1. Forcing function: pure open-ended synthesis (FI-T06 + chart) risks strong models producing thorough reviews that happen to mention bone health. Do we mount a near-complete colleague safety-review draft pre-committed to the red-herring headline + alendronate omission + no-surveillance, so the completion pressure fights the needed re-derivation? (Leaning yes - it is our one proven difficulty lever.)
2. Is the fall/fracture surveillance gap a clean, defensible scored omission, or do we need a second quiet gap (e.g., a held med needing monitoring labs not scheduled) so the discriminator is not single-threaded?
3. Grader: how to score an open-ended review fairly - reward surfacing the buried gap + down-weighting the red herring, credit correct restraint (no invented outcome), without turning it into a checklist. Sang five-block structure, central Section C = the omission, with the red-herring over-weight as a named pattern.
4. Confirm no DXA/bone-density study exists in any of the 26 files (verified absent this pass) and that holding alendronate inpatient is realistic (it is; bisphosphonates are routinely held during acute illness/with esophageal/renal concerns).

## Boundaries
No DOCX build, no platform staging, no upload, no AutoQC, no agent run, no locked-canon edit, no live-world edit until Alexander authorizes that exact step. This file is substrate verification + mechanism only.
