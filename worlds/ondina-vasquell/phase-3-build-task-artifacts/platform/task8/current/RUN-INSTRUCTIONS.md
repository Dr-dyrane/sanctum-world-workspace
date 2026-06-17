STATUS 2026-06-17 (v1): OV08 = de-telegraphed carry-forward on the Utilization Review Concurrent Stay lane (5th distinct lane, fresh P1). OV03/OV06 family. The deliverable is a finalized concurrent stay review for the Medicare Advantage payer. The started review leans discharge home; the decisive miss is a pure omission on the antibiotic route. The patient is on active IV antibiotics with no safe oral conversion (sulfa allergy) and no OPAT, and home-health wound nursing does not administer IV antibiotics, so discharge home is unsafe. Floor = carries the discharge-home disposition forward; catcher = declines discharge on the antibiotic-route barrier. The paused 06-15 OV08 packet (vascular referral plus disposition table, an OV06 duplicate on the perfusion-over-closure ceiling) is retired and superseded; this is a different lane and engine.

## Studio task setup
- Prompt: prompt-OV08.txt (plain "finalize it for submission", no telegraph).
- Task files to mount: started_concurrent_stay_review_05222026.docx, plus the full OV world chart.
- Golden: golden-OV08-v1.docx. Grader: grader-guidelines-OV08.txt (model grader).
- Run 10 trajectories.

## Build / regen
- python3 worlds/ondina-vasquell/phase-3-build-task-artifacts/build/build_ov08.py renders the started review and the golden into platform/task8/current/. No images.

## Pilot read
- Expect bimodal: floors clear discharge home (drop the antibiotic-route barrier), catchers hold on it. Target floor 0.10-0.35 with a catcher above 0.80. Floor if >=4/10 carry the discharge-home disposition forward.
- This is piloted DESPITE a 3/3 cold-bench catch, per the OV03 precedent (binding): the bench reads an unhurried reviewer and over-predicts catching; OV03 cold-benched 3/3 ceiling and the harness floored it 0.10-0.15. The fabrication telegraph the bench legitimately caught is removed; the ceiling verdict is not trusted.
- KNOWN RISK: UR disposition is a loud, model-strong axis. If the pilot is all-catch (>0.80, no floor), retire the carry-forward on UR and pivot OV08 to the off-text image engine (standby). Do not re-roll endlessly.
- If all-floor with no catcher, confirm the antibiotic-route catch is reachable (golden self-score or a catcher) before banking.
- Prereg: OV08-pilot-preregistration.md. Design and grounding: OV08-DESIGN-grounding.md.
