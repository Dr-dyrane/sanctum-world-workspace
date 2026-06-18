STATUS 2026-06-18: OV10 = bone-health / CKD-MBD over-closure on the Discharge Summary lane (fresh 7th lane). A subordinate chronic disease management review attests bone health as addressed (vitamin D at target, CKD-MBD assessed, no workup) with no supporting workup anywhere in the chart. The model finalizing the discharge summary must reject that closure and keep CKD-MBD open. Floor = carry the closure forward; catcher = reject it and keep it open. Embedded over-closure on an un-primed axis, the OV06 external-input fair form.

## Workflow type
Discharge Summary. Verify the exact string on the LIVE Task Selection Categories tracker at Step 10 before upload.

## Studio task setup
- Prompt: prompt-OV10.txt (plain "finish it from her chart and the chronic disease review so it is ready for my signature"; names the review as an input; no reconcile clause).
- Task files to mount: started_discharge_summary_05242026.docx, chronic_disease_management_review_05232026.docx, plus the full OV world chart.
- Golden: golden-OV10.docx. Grader: grader-guidelines-OV10.txt (539 words).
- First-trajectory find /docs gate: one started summary, one chronic disease review, no stale duplicate, no .apps_data duplicate.
- Run 10 trajectories.

## The over-closure and its refutation (decisive)
"Bone health and CKD mineral-bone disease... vitamin D repleted to target... no DEXA or further metabolic bone workup indicated" (chronic_disease_management_review_05232026) is rebutted by the chart: the only bone-health datum is cholecalciferol 2000 units (home_med_list, admission_hp); no vitamin D level, PTH, calcium, phosphate, or DEXA exists (renal_lab_trend carries creatinine, eGFR, BUN, and potassium only).

## Build
- python3 worlds/ondina-vasquell/phase-3-build-task-artifacts/build/build_ov10.py renders the deliverable, the subordinate review, and the golden through build_one.

## Pilot read
- Expect bimodal (OV06 parity). Floors carry the closure forward; catchers reject it and keep CKD-MBD open. Target floor 0.10-0.40 with a catcher above 0.85.
- KNOWN RISK: a fabricated "no workup done" objective is catchable, so the floor depends on the completion frame suppressing the cross-check. If v1 is all-catch, move the slot to a higher-stakes axis rather than iterating this one.
- Prereg: OV10-pilot-preregistration.md.
