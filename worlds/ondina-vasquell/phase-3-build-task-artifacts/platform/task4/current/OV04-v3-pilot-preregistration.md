# OV04 v3 PREREGISTRATION (off-text med-rec finding, KM08-v7 pattern) - locked before build/bench
Supersedes v1 (propagation, unfair - QA jqxv7246) and v2 (disclosed duty, CEILING - job f52553ce). Does not change after the v3 pilot lands.

## Why v3 (the KM08 ledger settled the fork)
KM08 ran this exact search: propagation (pre-written false item + plain prompt) = bimodal but UNFAIR (v4.1, AO bounced); pure placeholder = FAIR but too easy (v5, all 0.92-0.97); placeholder + external text hint = still too easy (v6); placeholder + an OFF-TEXT finding = FAIR + HARD (v7, the Raising-Task-Difficulty worked-example pattern). OV04 v1 = unfair, v2 = ceiling. v3 adopts the v7 pattern.

## Mechanism (retires the OSA over-closure)
OSA is retired as the trap: it can only be unfair (propagation) or too easy (placeholder), and it has no natural off-text signal. The OSA bullet reverts to a plain supported line (continue home CPAP). The floor moves to an OFF-TEXT medication-reconciliation discrepancy:
- At transfer the daughter brings in the patient's actual home-medication bottles. A TASK-LEVEL photo is added, plus ONE quiet nursing breadcrumb ("home medications brought in by daughter; photo added to the chart for reconciliation"), with NO text description of the contents.
- The photo shows a bottle the chart's "verified" home-med list OMITS and that is dangerous in her context: OTC ibuprofen (an NSAID). The chart explicitly states "NSAIDs are avoided given chronic kidney disease"; ongoing ibuprofen is an active nephrotoxin in AKI-on-CKD that must be identified and stopped. (Physician-author note: ibuprofen is Claude's proposed finding; Alexander to confirm or swap, e.g. a hidden potassium/salt-substitute for a sharper acute hyperkalemia hazard.)
- FAIR via PLACEHOLDER (Gate 0): the Medications section is "To be completed"; the model performs the med rec from all sources including the photo. Nothing false is pre-written, so the PROMPT REVERTS to plain "finish it from her chart so I can sign it" - no reconcile clause (KM08 derived rule: plain completion + fair attribution + quiet, integration-dependent contradiction). Fairness comes from construction, not disclosure, so it does not telegraph.
- UN-PRIMED: the chart's home-med list is "verified" and says NSAIDs avoided, so the model trusts the text and may never scrutinize the photo. OFF-TEXT: the discrepancy lives only in the image plus one quiet breadcrumb. DISTINCT from OV01 (carried-forward inpatient enoxaparin) and OV02 (line-site infection).

## Cold design-bench (pre-build, reasoning)
KM08 v7 precedent + un-primed principle: a model doing med rec reconciles from the trusted text list and MAR; it reads images poorly (worked example) and may not open or correctly parse the photo, so a fraction MISS the ibuprofen (floor) while a careful one that examines and reads the photo CATCHES it (catcher) -> bimodal, mirroring KM08 v7 (15-30 floor with catchers). Too-easy risk if the breadcrumb over-nudges (keep it a passing nursing line, not "reconcile this photo"). Too-hard/uniform risk if the bottle is unrecognizable (use a clearly labeled OTC ibuprofen). Grader does NOT need to read the image: the planted finding is specified in the grader, so it scores the model's text output against the known discrepancy. Verdict: proceed to build, then a real pilot.

## Forecast
Bimodal, miss-heavy. Floor below ~0.30 = the finished med rec omits the home ibuprofen and carries "NSAIDs avoided" forward as if true. Catcher above ~0.85 = identifies the ibuprofen from the photo, flags it as an active nephrotoxin in AKI/CKD, stops it, and reconciles the discrepancy.

## Read rules
- FLOOR = med rec does not surface the home ibuprofen (NSAID); the note implies no NSAID use.
- CATCHER = identifies the ibuprofen, stops it, flags NSAID-in-CKD/AKI, reconciles the list-vs-photo discrepancy.
- Identify-without-action (notes it but does not stop or flag) = partial, caps below midline.
- Anti-paralysis: refusing to finish the note = no credit.
- Grader: missing the ibuprofen is a HARD error / immediate low cap (worked-example move 4), however complete the rest of the note.
- FA/GA from the 2nd-lowest distinct run; plain prompt; failure-only; two paragraphs each; no grader-rating line.

## Build set (next steps, after this prereg locks)
1. IMAGE (Codex, codex-image-prompts style): transfer-day photo of home-medication bottles in a bag; one clearly an OTC ibuprofen 200 mg bottle; others consistent with her real home meds; realistic bedside/counter shot; no patient identifiers; no caption/overlay text that names the trap.
2. DRAFT: revert the OSA bullet to a supported "continue home CPAP" line (de-weaponized); keep the Medications section "To be completed" (placeholder); add the quiet nursing breadcrumb.
3. GOLDEN: med rec catches the ibuprofen, stops it, flags NSAID-in-AKI/CKD, reconciles the discrepancy.
4. GRADER: hard-error on the missed ibuprofen; five-block; chart-aware; <=540 words.
5. verify_ondina + presubmit gate; cold bench on the built bytes; then pilot.

## Mount / workflow / stopping rule
Task files: the started draft + ONE image (the home-med-bottle photo); plus the world chart. Workflow: Medical Transcription and Clinical Documentation Completion (confirm live). First-trajectory find /docs must show exactly the draft + the one image, no /docs/.apps_data, no stale/collision. Stopping rule: if it ceilings (over-nudged or too readable), tighten the breadcrumb / make the bottle the only off-text route once; if it floors uniformly with no catcher, the photo is too buried - add a faint corroborating breadcrumb. One pilot after a clean cold bench on the built bytes.

NOTE: v3 build is IN PROGRESS. The current draft/golden/grader docx still carry v1 OSA content - DO NOT PILOT until the rebuild above is done and verified.
