# OV05 PREREGISTRATION (off-text med-reconciliation finding via a home-med-bottle photo) - locked before build/bench
Next floor (#4 toward 8). Reuses the PROVEN OV04-v3 / KM08-v7 off-text-image engine. Slot task5; the old paused task5 design is superseded (kept in _paused). Does not change after the OV05 pilot lands.

## Mechanism (off-text finding; fair via construction; un-primed)
The deliverable is a SNF transfer medication reconciliation the model completes and verifies from the chart. A task-level PHOTO of the patient's home-medication bottles (the daughter brought them in at transfer) is in the chart, with ONE quiet nursing breadcrumb ("daughter brought the patient's home medications; photo added to the chart for reconciliation"), no contents described. The bottles include an OTC ibuprofen the chart's "verified" home-med list OMITS. Ibuprofen is an active nephrotoxin in her AKI-on-CKD, and the chart explicitly states "NSAIDs avoided given CKD," so her actually taking it is a documented contradiction that the reconciliation must capture and stop. (Clinical finding is Claude's proposal; Alexander to confirm ibuprofen vs a hidden potassium / salt-substitute for a sharper acute hyperkalemia hazard.)
- FAIR: plain prompt ("reconcile her home medications for the SNF transfer so I can sign it"); the photo is a real chart source any reconciliation must use; missing it is the model's own failure to read available data. Nothing pre-written is false; the trap is not in the prompt. Gate 0 satisfied by construction.
- UN-PRIMED: the EMR home-med list is "verified," so the model trusts it and may never examine the bottle photo. OFF-TEXT: the unlisted drug lives only in the image plus one quiet breadcrumb.
- DISTINCT: OV01 = continue inpatient enoxaparin (cold knowledge, text); OV02 = line infection (off-text text synthesis); OV04 = CPAP adherence (off-text image, device report); OV05 = an unlisted home drug surfaced by a med-bottle photo (off-text image, med-rec discrepancy). Different finding and artifact; same proven engine.

## Cold design-bench (pre-build, reasoning)
OV04-v3 precedent + un-primed principle: models reconcile from the trusted EMR list and read images poorly, so a fraction MISS the ibuprofen (floor, carry "no NSAIDs" forward) while a careful one OCRs the bottle photo and catches it (catcher) -> bimodal, like OV04. Keep the breadcrumb quiet and the prompt generic (do NOT say "reconcile the brought-in bottles") to avoid over-nudging. Use a clearly labeled OTC ibuprofen bottle so a careful read can catch it. Grader scores the model's text vs the known finding (does not need to read the image). Verdict: build + real pilot.

## Forecast / Read rules
Bimodal, miss-heavy. FLOOR below ~0.30 = the reconciliation omits the home ibuprofen or states no NSAID use. CATCHER above ~0.85 = identifies the unlisted ibuprofen from the photo, flags it as a nephrotoxin to stop in AKI/CKD, reconciles the discrepancy. Identify-without-action (notes it, does not stop/flag) = partial, caps below midline. Anti-paralysis: refusing to finish = no credit. Grader: missing the ibuprofen is a HARD error / low cap. FA/GA from the 2nd-lowest distinct run; failure-only; two paragraphs each; no grader-rating line.

## Build set (next steps)
1. IMAGE (Codex): photo of home-med bottles incl. a clearly labeled OTC ibuprofen 200 mg bottle + her real home meds; realistic, no identifiers (med-bottle-image-spec.md).
2. STARTED med-rec deliverable (a transfer medication-reconciliation form/note, EMR-reconciled with an open verify step) + the quiet nursing breadcrumb.
3. GOLDEN: the reconciliation captures, flags, and stops the unlisted ibuprofen; rest faithful to the chart.
4. GRADER: hard-error on the missed ibuprofen; five-block; chart-aware; <=540 words. A0.5 fairness check.
5. verify_ondina + presubmit + cold bench on bytes; then pilot.

## Mount / workflow / stopping rule
Task files: the started med-rec deliverable + the med-bottle image + the world chart. Workflow: Medical Transcription and Clinical Documentation Completion (or a med-reconciliation category; confirm live). First-trajectory find /docs must show exactly the deliverable + the one image, no /docs/.apps_data, no stale/collision. Stopping rule: if it ceilings (over-nudged or too-readable), quiet the breadcrumb; if it floors uniformly with no catcher, make the ibuprofen label cleaner. One pilot after a clean cold bench on the built bytes.
