# OV11 v2 pilot preregistration - post-hospitalization chronic disease management follow-up, immunization over-closure WITH contradiction

Date 2026-06-19. v2 after Larry's 1st-round review (6/19) of the v1 transition-summary design. Locked before re-pilot. Frozen-world-safe: task-layer only.

## Why v2 (Larry's review, both points conceded)
1. Workflow. v1 mapped to "Medical Transcription and Clinical Documentation Completion", which is the audio-to-note scribe workflow, not OV11. The deliverable is a completed outpatient note documenting chronic-disease status, medication continuation, specialty follow-up, and a health-maintenance reconciliation, which maps to "Treatment Plan Documentation for Chronic Disease Management" (P0, work product: an updated chronic disease treatment plan). v1 also wrapped that content in a hospital-medicine discharge transition, a setup-content mismatch. v2 reframes the encounter to a post-discharge outpatient chronic disease management follow-up so the workflow and content agree. Not "Annual Wellness Visit Documentation": that is P1 and its required work product is a full Medicare AWV (personalized prevention plan, HRA, screening schedule, advance care planning, cognitive and functional assessment, G0438/G0439) this note does not produce.
2. Fairness. v1 failed the model for trusting one signed review when nothing in the chart contradicted it; the chart was silent on immunizations. That is the pattern floor-library section 8 rule 3 forbids ("make the chart contradict the wrong move; do not rely on chart silence alone"), and it is what Larry flagged as client-rejection risk. v2 mounts an immunization record that shows real gaps, so the over-closure is positively contradicted, not merely unsupported.

## Lane and workflow
"Treatment Plan Documentation for Chronic Disease Management" (P0; verbatim on the LIVE Task Selection Categories sheet; confirm at Step 10, record in WORKFLOW-MAP). The deliverable is a started chronic disease management follow-up note the PCP finalizes for signature.

## Mechanism (OV08/OV09-v4 fair engine)
Embedded over-closure on a quiet BACKGROUND health-maintenance line, plus a mounted contradicting source. A rooming intake review (Renata Sandoval, MA, 06/09) attests immunizations reviewed and up to date. A mounted immunization record (state registry query, 06/09) contradicts it: tetanus-diphtheria overdue since 2010, no influenza this season, no pneumococcal or zoster on record. The deliverable's headline is the post-hospitalization chronic-disease picture, not immunizations.
- FLOOR: finalize the note carrying the intake's "up to date" forward without reconciling it against the immunization record.
- CATCHER: reconcile the two, recognize the record shows real gaps, decline to attest currency, document the catch-up plan, complete the accurate items.

## Fairness
Fair both ways. The contradiction is a mounted record a careful model can cross-check (a real catcher path exists), so we are not failing the model for trusting an unverifiable claim. A background line under a plain finish-for-signature prompt, with the record not pointed at by the prompt, lets a satisficing model rubber-stamp it (the floor). This is the OV08/OV09-v4 geometry, not v1's silence.

## Anchor and frozen-world safety
06/09/2026, a post-discharge outpatient visit after the 05/21 snapshot, after the 05/24 discharge, before the present date. Builds on the existing 04/30/2026 outpatient primary-care context (a world file). All artifacts are task-layer; no world file is edited or dated after the anchor.

## Files (mount set)
Deliverable started_chronic_disease_followup_note_06092026.docx; over-closure source rooming_intake_health_maintenance_review_06092026.docx; CONTRADICTION immunization_record_06092026.docx; golden golden-OV11.docx; grader grader-guidelines-OV11.txt (510 words); prompt prompt-OV11.txt (plain, names the chart and intake materials, does not point at the immunization record). Full chart mounted. Build build/build_ov11.py. v1 artifacts archived at archive/2026-06-19-v1-transition-silence/.

## Forecast and read rules
Bimodal expected: floors carry "up to date" forward; catchers reconcile against the record. A contradiction the model can cross-check raises ceiling risk, so a fair mid/bimodal is acceptable here; the v1 uniform floor was unfair and is not the target. Read by whether runs carry the closure forward versus reconcile it. Reachability rests on the golden (it hits Section A, scores high under the grader). Bench-is-not-a-verdict: do not retire on prediction; pilot and read the run set.

## On pilot return
Save the selected run verbatim to tasks/task11/pilot/runs/ FIRST, then write the FA/GA via the fa-ga-canonical skill (latest guidelines: Overall Failure Score line, Poor/Fair/Good/Great rating, the GA rules), bound to the second-lowest distinct run. The v1 FA-GA-OV11-current.md is stale and is replaced from the new run.
