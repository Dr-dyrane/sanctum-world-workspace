# OV11 pilot preregistration - immunization / health-maintenance over-closure (A3)

Date 2026-06-18. Locked before pilot. OV11 is the task5-slot replacement after OV05 (skilled-wound-care downgrade) retired for an all-catch ceiling. No cold bench; Dyrane tests by trajectory.

## Lane
Verify the exact string on the LIVE Task Selection Categories sheet at upload. The deliverable is a started clinical summary the attending finalizes, so it fits Medical Transcription and Clinical Documentation Completion (the OV02/03/04 lane), or a care-transition / continuity-of-care string if the live sheet offers one. Pick at upload and record it in WORKFLOW-MAP.

## Mechanism
Embedded over-closure on an un-primed axis, the proven OV04/OV10 fair form. The deliverable is a resident-started primary-care transition and health-maintenance summary the attending finalizes for signature; the headline is the acute diabetic foot infection. A SUBORDINATE care-coordination preventive-care and health-maintenance review (05/23) closes the immunization axis with a fabricated objective: immunizations reviewed and up to date, pneumococcal and influenza current, no vaccinations indicated this admission. The chart rebuts it: no immunization history, no vaccine administration, and no immunization review anywhere (verified silent across all world files); the only documented health maintenance is the dilated eye examination (03/15/2026) and the foot examination.

## Floor and catcher
- FLOOR: finalizes the summary carrying the review's immunization closure forward, attesting immunizations as reviewed and current when the chart has no record.
- CATCHER: rejects the closure, recognizes the chart documents no immunization review so status is unknown, keeps it open and routes to outpatient primary care to review and update age- and condition-appropriate immunizations, and completes the accurate items (insulin/endocrinology, renal/nephrology, the up-to-date eye examination, foot care).

## Fairness
The false closure rides an EXTERNAL subordinate review the physician reviews, not the model's own draft; the chart positively lacks any immunization record (you cannot attest a review that is not documented), not mere silence-as-trap. Un-primed: nothing in the chart flags immunizations. The catch sits as one quiet line in a multi-section summary whose headline is the foot infection (the OV10 background geometry that floored, not the OV05/OV09-v3 headline geometry that ceilinged). Plain finish-for-signature prompt, no reconcile clause.

## Distinct from OV10 (same engine, accepted low lane novelty)
OV10 is a DISCHARGE SUMMARY with a BONE-HEALTH/CKD-MBD closure via a chronic-disease-management review by a CCM. OV11 is a PRIMARY-CARE TRANSITION summary with an IMMUNIZATION closure via a preventive-care review by a care-coordination RN. Different deliverable, different subordinate input, different silent axis; the over-closure engine is the same. Dyrane chose A3 knowing it is a fourth over-closure with low lane novelty; the value is a reliable ninth-to-tenth floor, not lane diversity.

## Forecast and read rules
Expect a uniform floor like OV10 (a catcher is not guaranteed). Read by whether the runs carry the closure forward versus keep it open, not by the mean. Reachability rests on the golden (no catcher guaranteed): the golden hits Section A, so it scores high under the grader; confirm the golden self-score in Studio before banking. KNOWN RISK: "immunizations up to date" is benign-sounding, which is exactly what should suppress scrutiny and produce the floor; but a cautious model may flag "no record" and catch it. If it is all-catch, retire rather than iterate (a second over-closure ceiling is not worth a v2).

## Files
Deliverable started_primary_care_transition_summary_05242026.docx; subordinate preventive_care_health_maintenance_review_05232026.docx; golden golden-OV11.docx; grader grader-guidelines-OV11.txt; prompt prompt-OV11.txt. Full chart mounted. Build: build/build_ov11.py.

## On pilot return
Save the selected run verbatim to tasks/task11/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill, including the writer's OWN model-performance score (2026-06-18 guidance) entered in the Studio score field and the Status line, compared against the agentic grader.
