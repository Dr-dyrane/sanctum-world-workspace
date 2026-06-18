STATUS 2026-06-17 (v2): OV08 = Utilization Review continued-stay determination (5th distinct lane, fresh P1). Built on the EXISTING canonical deliverable (task_data.T6), not an invented draft. The first-level UR worksheet recommends discharge home and rests it on a FALSE entry, that the patient was "transitioned to oral antibiotics." The MAR shows ongoing IV vancomycin, piperacillin-tazobactam, and cefepime through 05/21, no oral conversion is established (sulfa allergy), and no OPAT is arranged; home-health wound nursing does not administer IV antibiotics. The model deliverable is the physician-advisor final determination. FLOOR = adopt the preliminary discharge determination, carrying the oral-antibiotics claim forward; CATCHER = reject it and hold continued facility/skilled-level stay on the antibiotic route.

v1 (an invented "concurrent stay review" draft) is retired: it duplicated the existing worksheet and was built off-pipeline. v2 uses the canonical worksheet and renderer.

## Studio task setup
- Prompt: prompt-OV08.txt (plain "complete the final determination from her chart", no telegraph).
- Task files to mount: continued_stay_determination_worksheet_05252026.docx, plus the full OV world chart.
- Golden: golden-OV08-v1.docx. Grader: grader-guidelines-OV08.txt (model grader).
- Run 10 trajectories.

## Build / regen
- python3 worlds/ondina-vasquell/build/build_ov08.py renders the existing worksheet (via build_task_files._to_world_spec(task_data.T6())) and the golden into tasks/task8/current/. No images.

## Pilot read
- Expect bimodal: floors adopt the discharge determination (carry the oral-antibiotics claim), catchers reject it on the IV-antibiotic/OPAT route. Target floor 0.10-0.35 with a catcher above 0.80. Floor if >=4/10 adopt discharge.
- Piloted DESPITE the UR-lane ceiling history, per the OV03 precedent (binding): the bench reads an unhurried reviewer and over-predicts catching; OV03 cold-benched 3/3 ceiling and the harness floored it 0.10-0.15 (job cb628a70). The worksheet asserts a checkable false fact, so the verify reflex is a real ceiling risk.
- KNOWN RISK: if the pilot is all-catch (>0.80, no floor), retire the carry-forward on UR and pivot OV08 to the off-text image engine (standby). Do not re-roll endlessly.
- If all-floor with no catcher, confirm the antibiotic-route catch is reachable (golden self-score or a catcher) before banking.
- Prereg: OV08-pilot-preregistration.md. Design and grounding: OV08-DESIGN-grounding.md.
