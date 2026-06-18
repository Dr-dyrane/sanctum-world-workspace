# OV04 v3 PREREGISTRATION (off-text CPAP-adherence finding on the OSA axis, KM08-v7 pattern) - locked before build/bench
Supersedes v1 (propagation, unfair - QA jqxv7246) and v2 (disclosed duty, CEILING - job f52553ce). Replaces the interim v3 med-rec-photo sketch: that idea is RESERVED for a future slot (see end), not burned on OV04. Does not change after the v3 pilot lands.

## Why v3 (KM08 ledger + keep the OSA axis)
KM08 ran this exact search: propagation = unfair (v4.1); pure placeholder = too easy (v5); placeholder + external text hint = too easy (v6); placeholder + an OFF-TEXT finding = fair + hard (v7, the Raising-Task-Difficulty worked example). Dyrane: ideas are scarce, do not discard the OSA axis - make it fair+hard and reserve the med-rec idea. The v7 resolution keeps the axis and adds an off-text signal; OSA's natural off-text artifact is the CPAP device compliance report.

## Mechanism (keeps the OSA axis; fair + hard via off-text device data)
- The draft's OSA bullet reverts to a plain, TRUE line (obstructive sleep apnea, continue home CPAP). Nothing is over-claimed and nothing is pre-written false, so there is no correction duty and Gate 0 is not triggered: the PROMPT stays plain ("finish it from her chart so I can sign it"), no reconcile clause, no telegraph.
- A TASK-LEVEL image is added: the patient's CPAP compliance report / app dashboard (daughter brought the unit at transfer) showing POOR adherence and undertreatment - proposed values (Alexander to confirm): average use ~1.4 hours/night, used 9 of the last 30 nights, residual AHI ~31/hour (severe, undertreated). ONE quiet nursing breadcrumb: "daughter brought the patient's CPAP unit; device compliance report added to the chart." NO numbers or description in prose.
- The chart (problem list, home-med list) says only "OSA on home CPAP, used nightly," which the model TRUSTS (un-primed: it assumes adherence and control). The compliance report (off-text, in an image) contradicts it.
- FLOOR = the model misses the report and writes "continue home CPAP, OSA stable/controlled," carrying the assumed control forward. CATCHER = it reads the report, catches the poor adherence and elevated residual AHI, documents OSA as NOT controlled this stay, and arranges sleep-medicine follow-up to address adherence and settings.
- FAIR: plain prompt; the report is a real chart document the model should integrate; missing it is the model's own failure to read available data (like missing the infected PICC in the worked example), not a planted-falsehood correction.
- DISTINCT: OV01 = carried-forward enoxaparin; OV02 = line-site infection via text synthesis (vision-independent); OV04 = image-data miss on a CPAP compliance report. Different axis, artifact, and lever type.

## Reuse (no wasted work)
Most of the OSA golden and grader carry over. The golden conclusion is unchanged in shape (OSA control not established this stay; continue home CPAP; arrange outpatient sleep-medicine follow-up), re-anchored from "no review documented" to "the compliance report shows poor adherence and an elevated residual AHI." The grader's central capped failure shifts from "propagating the OSA over-closure" to "missing the compliance-report finding and documenting OSA as controlled/adequate."

## Cold design-bench (pre-build, reasoning)
KM08 v7 precedent + un-primed principle: models read dense/image data poorly and trust the "uses CPAP nightly" text, so a fraction MISS the report (floor) while careful ones open and read it and catch the poor adherence (catcher) -> bimodal, mirroring KM08 v7. The grader does NOT need to read the image (the finding is specified in the grader from the golden), so the grader side is safe; the agent missing the image IS the floor. Risks: too-easy if the breadcrumb over-nudges (keep it a passing nursing line); uniform-floor if the report is unreadable to all (use a clean, legible dashboard with the key numbers prominent). Verdict: build, then a real pilot.

## Forecast
Bimodal, miss-heavy. Floor below ~0.30 = the finished note documents OSA as stable/controlled and continues home CPAP with no adherence concern. Catcher above ~0.85 = reads the report, flags poor adherence + undertreated OSA, keeps OSA open with sleep-medicine follow-up.

## Read rules
- FLOOR = note does not surface the poor CPAP adherence / undertreatment; treats OSA as controlled on home CPAP.
- CATCHER = identifies the poor adherence and elevated residual AHI from the report, documents OSA as not controlled this stay, arranges sleep-medicine follow-up for adherence/settings.
- Identify-without-action (notes the report but still calls OSA controlled) = partial, caps below midline.
- Anti-paralysis: refusing to finish the note = no credit.
- Grader: missing the compliance-report finding is a HARD error / immediate low cap (worked-example move 4), however complete the rest.
- FA/GA from the 2nd-lowest distinct run; plain prompt; failure-only; two paragraphs each; no grader-rating line.

## Build set (next steps)
1. IMAGE (Codex, codex-image-prompts style): a CPAP compliance dashboard/printout; clearly legible key fields (avg use ~1.4 h/night, 9/30 nights used, residual AHI ~31/h); realistic app/report look; no patient identifiers; no caption naming the trap.
2. DRAFT: revert the OSA bullet to the plain "continue home CPAP" line; keep Medications/Follow-up as the open sections; add the quiet nursing breadcrumb.
3. GOLDEN: reuse the OSA catch, re-anchored to the compliance report (poor adherence + residual AHI; OSA not controlled; sleep-medicine follow-up).
4. GRADER: hard-error on the missed adherence finding; five-block; chart-aware; <=540 words.
5. verify_ondina + presubmit gate; cold bench on the built bytes; then pilot.

## Mount / workflow / stopping rule
Task files: the started draft + a transfer-day nursing note (breadcrumb) + ONE image (the CPAP compliance report); plus the world chart. Workflow: Medical Transcription and Clinical Documentation Completion (confirm live). First-trajectory find /docs must show exactly the draft + the one image, no /docs/.apps_data, no stale/collision. Stopping rule: if it ceilings, tighten/quiet the breadcrumb; if it floors uniformly with no catcher, make the report cleaner/more legible so a careful read can catch it. One pilot after a clean cold bench on the built bytes.

## RESERVED IDEA (for a future OV slot - do not burn on OV04)
Med-reconciliation-by-photo: the daughter brings the home-medication bottles; a task-level photo reveals a drug the chart's verified list omits and that is dangerous here (e.g., OTC ibuprofen vs the chart's "NSAIDs avoided," or a hidden potassium/salt-substitute for an acute hyperkalemia hazard). Off-text, un-primed, distinct from OV01/OV02. Hold for a later task.

NOTE: v3 build is IN PROGRESS. The current draft/golden/grader docx still carry v1 OSA content - DO NOT PILOT until the rebuild above is done and verified.
