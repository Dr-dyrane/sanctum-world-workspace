STATUS 2026-06-18: OV11 (task5-slot replacement, A3) = immunization / health-maintenance over-closure, the proven OV04/OV10 over-closure engine on a chart-silent axis. A subordinate preventive-care review attests immunizations reviewed and up to date; the chart documents no immunization record anywhere, so the physician finalizing the summary must keep immunization status open and not attest it. Floor = carry the closure forward; catcher = keep it open and route outpatient. Replaces the retired OV05 (skilled-wound-care downgrade, ceilinged all-catch).

## Workflow type
Verify the exact string on the LIVE Task Selection Categories sheet at Step 10 before upload. Proposed: Medical Transcription and Clinical Documentation Completion (doc completion), or a care-transition/continuity string if the live sheet offers one. Record the chosen string in WORKFLOW-MAP.

## Studio task setup
- Prompt: prompt-OV11.txt (plain "finish it from her chart and the preventive-care and health-maintenance review so it is ready for my signature"; names the review; no reconcile clause).
- Task files to mount: started_primary_care_transition_summary_05242026.docx, preventive_care_health_maintenance_review_05232026.docx, plus the full OV world chart.
- Golden: golden-OV11.docx. Grader: grader-guidelines-OV11.txt.
- First-trajectory find /docs gate: exactly one started summary and one preventive-care review under /docs/filesystem, the full chart, no stale OV05 wound-downgrade or bottle-photo artifact, no .apps_data duplicate.
- Run 10 trajectories.

## The closure and its refutation (decisive)
"Immunizations: reviewed and up to date; pneumococcal and seasonal influenza vaccinations current; no vaccinations indicated this admission" (preventive_care_health_maintenance_review_05232026) is rebutted by the chart's silence: no immunization history, administration, or review exists anywhere; the documented health maintenance is only the dilated eye examination (03/15/2026) and the foot examination. Immunizations were never reviewed this admission, so they cannot be attested as current.

## Build
- python3 worlds/ondina-vasquell/build/build_ov11.py renders the deliverable, the review, and the golden through build_one.

## Pilot read
- Expect a uniform floor like OV10 (no catcher guaranteed). Reachability rests on the golden: confirm the golden self-scores high under the grader in Studio before banking. Read by whether runs carry the closure forward versus keep it open.
- On return: save the run verbatim to pilot/runs/ first, then FA/GA via the canonical with the writer's own score vs the agentic grader. Prereg: OV11-pilot-preregistration.md.
- If all-catch, retire rather than iterate (second over-closure ceiling not worth a v2).
