STATUS 2026-06-21: OV10 CDI REFRAME (v3) = bone-health / CKD-MBD over-attestation, documentation-integrity review on the CDI lane. Per Larry's 2nd OV10 review (6/21): Peer Review Case Analysis is the wrong lane (peer review is retrospective) and the reviewed note was an incomplete discharge summary. This version moves to Clinical Documentation Improvement (CDI) Query Review, makes the reviewed note a COMPLETE transition-of-care summary so the bone-health line is the only defect, and recalibrates the grader to credit the faithful production (a thorough review that misses the one line lands mid-band, not at the floor).

## Workflow type
Clinical Documentation Improvement (CDI) Query Review (P0). Verify the exact string on the LIVE Task Selection Categories tracker before upload, and confirm it is distinct from OV08 and the other OV tasks. Replaces Peer Review Case Analysis per the 6/21 review.

## Studio task setup
- Prompt: prompt-OV10.txt (plain documentation-integrity review framing; no trap hint, nothing primes bone-health, no reconcile clause).
- Task files to mount: signed_resident_transition_summary_05242026.docx, chronic_disease_management_review_05232026.docx, plus the full OV world chart. The v2 signed_resident_discharge_summary is superseded (moved to _v2-cosign-superseded); do NOT mount it.
- Golden: golden-OV10.docx (attending documentation-integrity review). Grader: grader-guidelines-OV10.txt.
- First-trajectory find /docs gate: one signed resident transition summary, one chronic disease review, no stale discharge-summary duplicate, no .apps_data duplicate.
- Run 10 trajectories.

## The over-attestation and its refutation (decisive)
The signed resident transition summary attests "vitamin D repleted to target and metabolic bone disease addressed and stable; no further metabolic bone workup indicated" (copied from chronic_disease_management_review_05232026). The chart rebuts it: the only bone-health datum is cholecalciferol 2000 units (home_med_list, admission_hp); no vitamin D level, PTH, calcium, phosphate, or DEXA exists (renal_lab_trend carries creatinine, eGFR, BUN, and potassium only). A reviewer who verifies the attestation against the labs catches it; one who rubber-stamps the complete, signed, otherwise-faithful summary misses it.

## Larry-fix mapping (6/20 + 6/21)
- Workflow: CDI Query Review (concurrent documentation validation), not peer review (retrospective) or the retired discharge-summary lane.
- Complete note: the reviewed summary now carries hospital course, active problems, a full medication list, the ID plan, and a disposition, so the bone-health attestation is the only defect.
- Grader credit: a thorough review that confirms the supported items but misses the bone-health line lands mid-band; the floor is for a rubber-stamp that engages with nothing. No 15 percent universal floor.
- New formats: current grader guidelines and FA/GA on resubmission.

## Pilot read
- Expect bimodal (OV08 parity). Floors endorse the bone-health attestation; catchers flag it unsupported and keep CKD-MBD open. Read by the split, not the mean.
- Contingency: if all-catch, the bone-health line is too conspicuous or the prompt over-primes; make the over-attestation a quieter copy-forward. If all-floor, confirm the world chart labs make the missing workup verifiable.
- FA/GA subject: the second-lowest distinct run.
- Prereg: OV10-pilot-preregistration.md.

## Build note
The v3 deliverables (transition summary, golden, grader, prompt) were reframed in place via MODE A clone preserving the OV house styles.xml. If a canonical re-render is wanted, update build_ov10.py to the CDI framing and rebuild through build_one.
