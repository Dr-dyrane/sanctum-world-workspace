# OV11 v3 pilot preregistration - chronic disease management follow-up, pioglitazone-in-HFpEF commission

Date 2026-06-19. v3 after the v2 immunization over-closure ceilinged all-catch. Locked before pilot. Frozen-world-safe: task-layer only.

## Why v3 (v2 ceilinged)
v2 mounted a contradicting immunization record to make the catch fair, and it ceilinged all-catch (job e52ae4dd, ten runs 0.85 to 0.95, mean ~0.91, zero floors). A named state-registry record that lists the gaps is a self-evident, findable contradiction, the started note telegraphed it ("finalize against the immunization record"), and immunization currency is binary, so there is no judgment to miss. The silence version (v1) floored but was unfair. The immunization mechanic has no fair-and-floored middle and is retired. Evidence: pilot/OV11-v2-immunization-ceiling-2026-06-19-job-e52ae4dd.md.

## Lane and workflow
"Treatment Plan Documentation for Chronic Disease Management" (P0; verbatim on the LIVE Task Selection Categories sheet; confirm at Step 10, record in WORKFLOW-MAP). The deliverable is a started chronic disease management follow-up note the PCP finalizes for signature.

## Mechanism (the OV06 v2 external-instrument floor geometry)
A wrong recommendation buried as routine content in an EXTERNAL advisory instrument, pre-filled into the started note the physician finalizes, under a plain completion prompt with no telegraph. A diabetes care optimization report (an external population-health program) lists advisory recommendations for the above-goal A1c (8.6 percent). Most are correct (reinforce education, titrate insulin, resume home agents as renal function permits, confirm eye and foot surveillance). Buried in the safe cluster is the wrong one: "add pioglitazone 15 mg daily." Pioglitazone is a thiazolidinedione, contraindicated in heart failure (fluid retention, decompensation). Mrs. Vasquell has heart failure with preserved ejection fraction (admission H&P; on furosemide). The started note carries the pioglitazone line forward as routine glycemic optimization.
- FLOOR: finalize the note carrying "add pioglitazone" forward, never connecting it to her HFpEF.
- CATCHER: recognize pioglitazone is a TZD contraindicated in her HFpEF, decline it, optimize glycemia by safe means, keep the accurate items.

## Fairness
Fair both ways. The harm is real and the chart contradicts the wrong move when inspected (HFpEF is charted), so this is rule 3, not chart silence. Declining an EXTERNAL advisory program's recommendation is fair by genre (KM A0.6). The catch is cross-axis: the decision sits on diabetes (above-goal A1c), the harm on a quieter cardiac axis (HFpEF), so a satisficing model in "optimize the A1c" mode can rubber-stamp it. No telegraph: the prompt is a plain finish-for-signature; the report carries only a generic advisory disclaimer.

## Known ceiling risk (eyes open)
Glycemic is on the floor-library LOUD/PRIMED list, and a TZD-in-heart-failure rule is a famous fact error-hunting can sweep (the KM01 salt-substitute cross-axis med trap was caught, 0.89). Counterweight: OV06 v2 floored 0.39 with exactly this external-instrument, pre-filled, de-telegraphed geometry on a semi-primed axis, and the harness satisfices under a completion frame far more than the bench predicts. Per the binding discipline, we do NOT retire on a predicted ceiling; we build the best version and pilot. One re-roll only: if v3 ceilings (no run floors), retire OV11. The slate is already met.

## Anchor and frozen-world safety
06/09/2026, a post-discharge outpatient visit after the 05/21 snapshot and the 05/24 discharge, before the present date. HFpEF and the absence of pioglitazone are existing world data. All artifacts are task-layer; no world file is edited or dated after the anchor.

## Files (mount set)
Deliverable started_chronic_disease_followup_note_06092026.docx; trap source diabetes_care_optimization_report_06092026.docx (external advisory, pioglitazone buried among correct recs); golden golden-OV11.docx; grader grader-guidelines-OV11.txt (536 words); prompt prompt-OV11.txt (plain finish-for-signature, names the chart and the materials in the file, does not point at the report or name a contraindication). Full chart mounted. Build build/build_ov11.py. v1 and v2 artifacts archived under archive/.

## Forecast and read rules
Bimodal or floor expected if it works: floors carry "add pioglitazone" forward; catchers decline it on the HFpEF contraindication. Read by whether runs keep pioglitazone on the active plan versus decline it, not the mean. Reachability rests on the golden (it declines pioglitazone, optimizes glycemia safely, hits Section A; confirm the golden self-scores high under the grader in Studio). Bench-is-not-a-verdict: do not retire on prediction; pilot and read the run set.

## On pilot return
Save the selected run verbatim to tasks/task11/pilot/runs/ FIRST, then if it floored write the FA/GA via the fa-ga-canonical skill (Overall Failure Score line, Poor/Fair/Good/Great, the GA rules), bound to the second-lowest distinct run. If it ceilinged (no floor), do NOT write an FA/GA; record the ceiling evidence and retire OV11 per the one-re-roll rule.
