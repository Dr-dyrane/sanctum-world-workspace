STATUS 2026-06-17 (v4): OV09 = embedded-wrong carry-forward on the Post-Acute Care Coordination lane (6th lane), no image. v3 (embedded-wrong on the disposition headline) CEILINGED 0.84, range 0.72-0.92, no floor (job e9c38261): disposition is the handoff's headline, so the model corrected it in every run. v4 moves the embedded wrong to a high-stakes BACKGROUND axis: the routine discharge-medication line resumes the three held oral agents (metformin, empagliflozin, lisinopril) at discharge; disposition is now drafted correctly and open. Floor = carry the resume forward. Catcher = keep the three held per the hold orders, restart deferred.

Prior retirements: v1 contrast order (ceilinged, job 21e12fc3), v2 off-text osteo image (report-as-image fairness). See OV09-DESIGN-grounding.md.

## Workflow type
Post-Acute Care Coordination Documentation. Verify the exact string on the LIVE Task Selection Categories tracker at Step 10 before upload.

## Studio task setup
- Prompt: prompt-OV09.txt (plain "finish it from her chart so it is ready for my signature"; no reconcile clause).
- Task files to mount: started_post_acute_coordination_note_05242026.docx plus the full OV world chart. No image.
- Golden: golden-OV09.docx. Grader: grader-guidelines-OV09.txt (538 words).
- First-trajectory find /docs gate: exactly one started note, no image, no stale v1/v2/v3 deliverable, no .apps_data duplicate.
- Run 10 trajectories.

## The embedded-wrong element and its refutation (decisive chart files)
- "resume the home oral regimen at discharge: metformin 500 mg twice daily, empagliflozin 10 mg daily, lisinopril 20 mg daily" -> medication_hold_orders_05162026 holds all three for AKI on CKD with "no restart order is entered"; renal_lab_trend shows the AKI resolving (creatinine 1.6 from 2.1). Resuming risks lactic acidosis (metformin), euglycemic ketoacidosis during an active infection (empagliflozin), and worsening AKI (lisinopril).

## Build
- python3 worlds/ondina-vasquell/phase-3-build-task-artifacts/build/build_ov09.py renders the deliverable and golden into platform/task9/current/ through build_one. No image.

## Pilot read
- Expect bimodal (OV06/OV08 parity). Floors carry the resume forward; catchers hold the three agents. Target floor 0.10-0.40 with a catcher above 0.85.
- KNOWN RISK: the hold orders are explicit, so a cross-checking model catches the resume; the floor depends on the completion frame suppressing the medication cross-check. v3 already ceilinged on this lane, so if v4 also all-catches, move the slot to a fresh idea rather than a v5.
- Prereg: OV09-pilot-preregistration.md. Design and the v1/v2/v3 history: OV09-DESIGN-grounding.md.
