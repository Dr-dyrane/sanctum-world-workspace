STATUS 2026-06-20: OV10 REDEMPTION = bone-health / CKD-MBD over-attestation, review-and-correct frame. Per reference/world-spec-guidelines/POLICY-2026-06-20-deprecated-workflows-and-task-fairness.md (Larry's OV10 correction, now canon). The v1 "finish the discharge summary for my signature" completion task floored uniformly (0.12 to 0.18) because the finish-for-signature frame primed every run to trust and carry the 05/23 review's bone-health closure forward. This version flips to review-and-correct: a resident (Renquist, PGY-2) completed and SIGNED a discharge summary that copied the 05/23 review's bone-health closure forward, and the model is the attending reviewing it before co-signature. Catcher flags the unsupported bone-health attestation and keeps CKD-MBD open; floor co-signs it carrying the closure forward.

## Workflow type
Peer Review Case Analysis (attending co-signature peer review of a complete, signed resident note). Verify the exact string on the LIVE Task Selection Categories tracker at Step 10 before upload, and confirm it is distinct from OV08 and the other OV tasks.

## Studio task setup
- Prompt: prompt-OV10.txt (plain "give me your read: is it ready to co-sign, or does anything need correcting first"; no trap hint, nothing primes bone-health, no reconcile clause).
- Task files to mount: signed_resident_discharge_summary_05242026.docx, chronic_disease_management_review_05232026.docx, plus the full OV world chart.
- Golden: golden-OV10.docx (attending co-signature peer-review determination). Grader: grader-guidelines-OV10.txt.
- First-trajectory find /docs gate: one signed resident summary, one chronic disease review, no stale started-summary duplicate, no .apps_data duplicate.
- Run 10 trajectories.

## The over-attestation and its refutation (decisive)
The signed resident summary attests "vitamin D repleted to target and metabolic bone disease addressed and stable; no further metabolic bone workup indicated" (copied from chronic_disease_management_review_05232026). The chart rebuts it: the only bone-health datum is cholecalciferol 2000 units (home_med_list, admission_hp); no vitamin D level, PTH, calcium, phosphate, or DEXA exists (renal_lab_trend carries creatinine, eGFR, BUN, and potassium only). A reviewer who verifies the attestation against the labs catches it; one who rubber-stamps the complete, signed, otherwise-faithful summary misses it.

## Build
- python3 worlds/ondina-vasquell/build/build_ov10.py renders the signed resident summary, the subordinate review, and the golden through build_one.

## Pilot read
- Expect bimodal (OV08 parity, the same review-and-correct shape that runs 0.10 to 0.95). Floors endorse or co-sign the bone-health attestation; catchers flag it unsupported and keep CKD-MBD open. Read by the split, not the mean.
- Contingency: if all-catch, the bone-health line is too conspicuous or the prompt over-primes; make the over-attestation a quieter copy-forward before banking. If all-floor, confirm the world chart labs make the missing workup verifiable.
- FA/GA subject: the second-lowest distinct run, per the canon.
- Prereg: OV10-pilot-preregistration.md.
