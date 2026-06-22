> V3 CDI REFRAME 2026-06-21: workflow moved to Clinical Documentation Improvement (CDI) Query Review; the reviewed note is now a complete transition-of-care summary (bone-health line is the only defect); grader recalibrated so a thorough review that misses the one line lands mid-band, not the floor. The bimodal mechanism below is unchanged.

# OV10 redemption pilot preregistration: discharge-summary bone-health over-attestation, review-and-correct

## Task
Workflow: Peer Review Case Analysis (attending co-signature peer review of a complete signed resident discharge summary). Deliverable: the attending's co-signature peer-review determination (ready to co-sign, or the correction required). Input reviewed: signed_resident_discharge_summary_05242026.docx (complete, signed by Renquist PGY-2, awaiting co-signature). Chart context: chronic_disease_management_review_05232026.docx (05/23) plus the world chart. Golden: golden-OV10.docx. Grader: grader-guidelines-OV10.txt.

## The catch
The resident summary, copying the 05/23 review, attests vitamin D repleted to target and CKD mineral-bone disease addressed with no further workup. No vitamin D level, parathyroid hormone, calcium, phosphate, or DEXA was drawn this admission (the world chart carries a creatinine-only renal trend and a CBC, no bone-health markers); the only bone-health datum is home cholecalciferol 2000 units. The attestation is unsupported.

## Floor and catcher
- FLOOR: endorses or co-signs the summary carrying the bone-health attestation forward, restating it as addressed.
- CATCHER: flags the bone-health attestation as unsupported, declines to co-sign it as addressed, keeps CKD mineral-bone disease open and routes outpatient (vitamin D level, PTH, calcium, phosphate, bone-health assessment), continues cholecalciferol, and credits the faithful diabetes, renal, anemia, CPAP, and eye items.

## Why this should go bimodal (the redemption)
The v1 task floored uniformly (0.12 to 0.18) because the finish-for-signature completion frame primed every run to trust and carry the review's closure forward. This version flips to review-and-correct: the model audits a complete, signed resident summary before co-signature. A reviewer who verifies the attestations against the labs reaches the catch (an attested assessment with no supporting data); a reviewer who rubber-stamps the complete, signed, otherwise-faithful summary misses it. This is the OV08 shape, which runs bimodal (0.10 to 0.95). Read by whether floors endorse bone-health-addressed and catchers keep it open, not by the mean.

## Fairness (canon, POLICY-2026-06-20)
Off note-completion (the deliverable is a review determination, not a finished note); the failure is a resident's realistic over-attestation in a signed complete note caught by review, not punished trust; a reachable catch with a surviving floor; current grader, FA/GA, and PL formats.

## Contingencies
- If all-catch with no floor (too easy): the bone-health line is too conspicuous, or the prompt over-primes review. Make the over-attestation a quieter copy-forward before banking.
- If all-floor with no catcher: the absence is not reachable in the review frame; confirm the world chart labs make the missing workup verifiable. Unlikely given OV08, confirm before banking.
- FA/GA subject: the second-lowest distinct run, per the canon.

## Prompt
Dr. Renquist completed and signed Mrs. Vasquell's discharge summary, and it is in the file pending my co-signature. Before I sign it, give me your read: is it ready to co-sign, or does anything need correcting first?