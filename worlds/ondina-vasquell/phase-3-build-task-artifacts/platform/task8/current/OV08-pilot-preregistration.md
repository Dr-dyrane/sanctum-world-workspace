# OV08 pilot preregistration - Utilization Review continued-stay determination

Date: 2026-06-17. Locked before pilot. Lane: Utilization Review Concurrent Stay Documentation (5th distinct lane). Built on the EXISTING canonical deliverable (task_data.T6), not a new invented draft.

## Deliverable (existing, canonical)
continued_stay_determination_worksheet_05252026.docx - the first-level UR continued-stay determination worksheet from the task set (task_data.T6, rendered through the canonical Epic builder). The model deliverable is the PHYSICIAN-ADVISOR final determination completing that worksheet. Prompt: complete the final determination from the chart. Golden: golden-OV08-v1.docx (physician-advisor determination). Grader: grader-guidelines-OV08.txt.

## Mechanism (conflicting-authority / carry-forward hybrid on the antibiotic route)
The first-level worksheet recommends discharge to home and rests it on a FALSE clinical-course entry: "tolerating oral intake and transitioned to oral antibiotics. Acute inpatient medical-necessity criteria no longer met." This is wrong. The MAR shows ongoing IV vancomycin, piperacillin-tazobactam, and cefepime through 05/21; no oral regimen is established (the sulfa allergy excludes TMP-SMX; ID never finalized an oral step-down, the 05/19 plan note disclaims being a final discharge antibiotic synthesis); no OPAT or home infusion is arranged. Home-health wound nursing does not administer IV antibiotics. The worksheet also pre-argues the loud barriers as home-manageable (perfusion outpatient, wound care in home-health scope, home support arranged), so the antibiotic route is the load-bearing factual error.

## Floor and catcher
- FLOOR: adopts the worksheet's preliminary discharge determination, carrying the false oral-antibiotics claim forward. Rubber-stamps step-down to home.
- CATCHER: rejects it. Recognizes the patient is still on IV antibiotics with no oral conversion (sulfa allergy) and no OPAT, that home-health cannot administer IV antibiotics, and holds continued facility-level or skilled-level stay until the antibiotic route is resolved.

## Why pilot despite the UR-lane ceiling history (the OV03 precedent, binding)
The UR decisiveness family cold-benched as a ceiling (OV06-UR-decisiveness-bench), and my own carry-forward variant cold-benched 3/3 catch. But our binding rule is: do not retire on a cold-bench ceiling. OV03 cold-benched 3/3 ceiling and the real harness FLOORED it 0.10-0.15 (job cb628a70); the harness satisfices across the file load under a completion prompt while the unhurried bench reviewer runs the synthesis. This design improves on the prior worksheet+golden, which caught only on the loud operational barriers (model-strong axis) and never flagged the worksheet's antibiotic lie; the golden now makes the quiet antibiotic-route error load-bearing.

## Forecast and read rules
- Expected: bimodal. Floors 0.10-0.35 (adopt the discharge determination, carry the oral-antibiotics claim). Catchers 0.80-0.95 (hold continued stay on the IV-antibiotic/OPAT route). Mean roughly 0.40-0.55. Floor if >=4/10 adopt the discharge determination.
- Read by whether the floors adopt discharge and the catchers reject it on the antibiotic route, not by the mean.
- KNOWN RISK (ceiling): UR disposition is loud and model-strong; the worksheet asserts a checkable false fact, which the model may verify against the MAR. If the pilot is all-catch (>0.80, no floor), the verify reflex dominates; do not re-roll endlessly - retire the carry-forward on UR and pivot OV08 to the off-text image engine (standby).
- If all-floor with no catcher, confirm the antibiotic-route catch is reachable (golden self-score or a catcher) before banking.

## Files
- Deliverable: continued_stay_determination_worksheet_05252026.docx (task_data.T6, existing).
- Golden: golden-OV08-v1.docx. Grader: grader-guidelines-OV08.txt. Prompt: prompt-OV08.txt.
- Full OV world chart mounted as backdrop; the decisive contradiction is in mar_05162026_05212026.docx and antibiotic_plan_note_05192026.docx.
- Build/regen: build/build_ov08.py renders the existing worksheet (via build_task_files._to_world_spec(task_data.T6())) and the golden into platform/task8/current/.
