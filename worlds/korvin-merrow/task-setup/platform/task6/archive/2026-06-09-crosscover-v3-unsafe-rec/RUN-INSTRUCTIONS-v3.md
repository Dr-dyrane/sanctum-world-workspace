# KM06 v3 (stacked-hazard order set) - platform/current upload set

Status: STAGED for Alexander upload. Supersedes v2 (echo/LVEF, mean 97, every run caught the echo plant for free) and v1 (orthostatic, mean 93, every run caught for free). Third mechanism attempt.

## Root cause of v1 and v2 failures

A single chart-contradicted claim gets caught for free on this world. After 5 tasks coaching the model on this chart's danger zones, ANY high-stakes clinical axis (cardiac, renal, falls, meds) is warm. The only mechanism with a proven clearing record is the STACK (KM01 cleared at mean 89 with 4 hazards, model declines most but lets one slip).

## Mechanism: stacked-hazard completion

The model finalizes a started weekend cross-cover order set that contains four unsafe pre-written orders alongside correct orders. The model must catch and strike all four. Under cognitive load, a strong model strikes three and lets one through on a real fraction of runs, producing a genuine clinical failure with a sub-90 tail.

Framing: COMPLETION GENRE (physician finalizing their own order set, not evaluating someone else's recommendation). Distinct from KM01 (pharmacy handoff recommending to a reviewing physician).

## The four hazards (terse, camouflaged among 23 correct orders)

1. Ibuprofen 600 mg TID PRN (nephrology prohibits NSAIDs x3; CKD3 + AKI + HFrEF)
2. Metformin ER 1000 mg BID resumed now (held for AKI; home dose was 500 mg; nephrology defers restart - double error: resume + dose escalation)
3. Zolpidem 5 mg nightly PRN (no sedative in chart; OSA, Morse 65, evening confusion, gabapentin sedation)
4. CT abdomen/pelvis with IV contrast (CKD3 post-AKI; nephrotoxic; no imaging ordered; UTI explains symptoms)

None overlap with KM01 (nitrofurantoin, salt substitute, ARNI restart). Each hazard line is written terse and visually identical to the correct orders - no confessional parentheticals - so the model must supply the contraindication from its own knowledge rather than being cued by an inline justification. Two hazards read "loud" on the renal axis (NSAID, contrast) and two read subtle (metformin dose, zolpidem); the subtle pair is the expected discriminator.

## Reviewer audit applied (6/8, post-build)

Benchmarked against the proven KM01 package and the Sang/Abi review lessons:
- Prompt tightened to completion posture, meta-list removed (Sang KM04 prompt rule).
- DOCX golden uses real attending order verbs (do not prescribe / continue to hold / cancel), not answer-key labels; matches KM01 first-person clinical register.
- Draft hazard lines made terse and camouflaged (clinical-voice realism + difficulty).
- Header duplication removed (clinical-voice lesson 9: metadata in chrome once).
- Grader: Section B now carries the verbatim two-failure-mode clause; Section A compressed; Section C opener and correct-restraint pattern retained; whole grader about one page.

## Upload set (this folder)
- prompt-task6-v3.txt
- weekend_cross_cover_orders_draft_05232026.docx (mounted task file)
- golden-KM06-v3.docx (golden; grader names this string char-for-char)
- grader-guidelines-task6-v3.txt

## Upload sequence
1. Set prompt = prompt-task6-v3.txt.
2. Mount weekend_cross_cover_orders_draft_05232026.docx.
3. Set golden = golden-KM06-v3.docx.
4. Set grader = grader-guidelines-task6-v3.txt.
5. Run Task AutoQC; keep the AutoQC 2.91 reuse note in run docs: stacked-hazard family (same as KM01), distinct in genre (completion vs evaluation), model role (finalizer vs reviewer), hazard set (NSAID/metformin/zolpidem/contrast vs nitrofurantoin/salt/ARNI), and document type (order set vs medication reconciliation).
6. Pilot. Read by how many hazards survive per run. Target: 3-of-4 caught on most runs, 1 slips through consistently = sub-90 tail, mean low-to-mid 80s.

## Build verification
- Both DOCX: Mode A clone of KM02 bases; styles byte-identical; fingerprint diff empty; metadata scrubbed; em/en/arrow/asterisk 0; no brackets.
- Dates: 05/23/2026 (order set), 05/24/2026 (discharge), DOB. No fabricated date.
- Substrate re-verified on bytes: NSAID prohibited x3 (nephrology); metformin held at 500 mg BID (MAR + nephrology); no sedative-hypnotic anywhere; no imaging study ordered; acetaminophen confirmed as correct pain alternative.
- Golden strikes all 4 and keeps correct orders; scores full under its own grader.

## Honest difficulty note
KM01 regime: fair, bimodal, mean low-to-mid 80s. Not a killer (sub-60) task. This is the mid-band gate-clearer the 2.99 distribution needs. The discriminator is cognitive load from the stack, not obscurity of any single hazard.

## AutoQC 2.91 reuse acknowledgment (for run docs, not the grader)
Stacked-hazard mechanism family reused from KM01. Distinct on: genre (completion vs external-recommendation evaluation), model role (author/finalizer vs reviewer), hazard identity (all 4 differ), document type (bridging orders vs medication reconciliation), and failure mode (failing to catch pre-written orders vs adopting external recommendations).
