# OV10 redemption plan: discharge-summary bone-health over-closure

Status: PLAN for approval. Nothing built yet. OV10 stays parked until Alexander approves a direction. Governed by reference/world-spec-guidelines/POLICY-2026-06-20-deprecated-workflows-and-task-fairness.md (Larry's OV10 correction, now canon).

## 1. Why OV10 floored (diagnosis)
Pilot job a611e19f: ten runs 0.12 to 0.18, mean about 0.15, no high outlier. A universal floor, the unfair pattern Larry flagged.
The clinical catch is sound. The 05/23 chronic-disease review attests vitamin D repleted to target and CKD mineral-bone disease assessed, but no vitamin D level, parathyroid hormone, calcium, phosphate, or DEXA was drawn this admission; the only bone-health entry is home cholecalciferol 2000 units. The attestation is unsupported.
The failure is the FRAME, not the catch. The prompt is "finish the started discharge summary for my signature." A finish-for-signature frame primes the model to trust and carry the source review's closure forward rather than audit each line. Every run satisficed and carried the closure. The preregistration predicted bimodal but got all-floor, and named the cause itself: the floor depends on the completion frame suppressing the cross-check.
This is Larry's two problems at once: P1, a note-completion workflow; and P2, the model scored to the floor for carrying forward something the chart stated, which he says must not by itself earn about 15 percent.

## 2. Redemption thesis
Keep the clinical catch, change the frame from completion to review-and-correct. Ask the model to REVIEW a complete, signed resident summary that already carries the bone-health over-attestation, and catch it. A review frame primes the audit the completion frame suppressed. This is Larry's own endorsed shape (a signed, complete resident note that makes a common mistake, with the task being to catch it) and the exact structure that makes OV08 bimodal.

## 3. The proof this goes bimodal: OV08
OV08 (continued-stay worksheet review) is the same review-and-correct shape, and its distribution is clearly bimodal: floors at 0.10 and 0.30 rubber-stamp the worksheet, catchers at 0.72 to 0.95 enter the corrected determination. OV10 redeemed is the discharge-summary analog of OV08: review a complete signed note, catch the one unsupported line.

## 4. The redesigned task
- Frame: review-and-correct, not completion.
- Deliverable: a documentation-integrity review, an attending pre-cosignature review (the findings, the corrections required, and the sign-or-hold decision). NOT a discharge summary, which sidesteps the discharge-summary deprecation entirely.
- Input reviewed: a COMPLETE, SIGNED resident discharge or transition summary that carries the bone-health over-attestation, a common and realistic copy-forward from the 05/23 review.
- The catch: the bone-health line attests vitamin D repleted to target and CKD mineral-bone disease assessed, with no measured workup anywhere in the chart this admission. A correct review flags the line, keeps CKD mineral-bone disease open for outpatient workup (vitamin D level, PTH, calcium, phosphate, bone-health assessment), continues cholecalciferol, and credits the faithful diabetes, renal, anemia, CPAP, and eye-exam items.
- Workflow lane (DECISION, see section 8): a review lane. Candidates are Peer Review Case Analysis (proven on W3 Task 4) or a Clinical Documentation Improvement review. The verbatim approved name must be confirmed against the live tracker and be distinct from OV08 (utilization review) and the other OV tasks.

## 5. The bimodal mechanism (the part the request turns on)
- Reachable catcher path: the chart contains no bone-health workup, so a reviewer who cross-checks each attestation against the labs and orders finds the unsupported line and flags it. The catch is an ABSENCE the reviewer notices, an attested assessment with no supporting data, not a planted falsehood to distrust.
- Surviving floor path: the summary is otherwise complete and faithful, and the bone-health line reads as a routine closure, so a reviewer who rubber-stamps the polished note misses it. Nothing in the prompt or chart may flag bone-health as open.
- Why bimodal, not the old universal floor: the review frame makes auditing the job, so capable models reach the catch instead of all satisficing. OV08 confirms the shape discriminates.
- Tuning to hold the spread: keep the over-attestation plausible (a real consultant line copied forward) so careless reviewers still miss it; keep the contradiction reachable (the workup is simply absent and verifiable in the labs) so careful reviewers still find it.

## 6. Fairness mapping (Larry's canon)
- P1 off note-completion: the deliverable is a review determination, not a finished or authored note.
- P2 realistic catchable error: a resident over-attested a consultant's bone-health closure in a signed, complete summary; the model is tasked to catch it, not punished for trusting it.
- P3 no universal floor: the review frame plus a reachable catch produces a spread; pilot is read by whether floors rubber-stamp and catchers flag, not by the mean.
- P4 new formats: grader guidelines, FA/GA, and PL on the current instructions at build.

## 7. Cold-bench prediction and contingencies
- Predict bimodal: rubber-stampers carry the bone-health attestation, careful reviewers flag it. Read by the split, not the mean.
- If all-catch with no floor (too easy): the bone-health line is too conspicuous. Make it a quieter copy-forward, or raise the stakes axis, before banking. (Prereg ceiling risk, carried forward.)
- If all-floor with no catcher: the catch is not reachable in the review frame; re-examine the input so the absence of workup is verifiable. Unlikely given OV08, but confirm at pilot before banking.

## 8. Open decisions for Alexander (before build)
1. Workflow lane: Peer Review Case Analysis vs a CDI or documentation-integrity review vs an attending pre-cosignature review. Confirm the verbatim approved name against the live tracker and that it is distinct from OV08 and the other OV tasks.
2. The reviewed note: a discharge or transition summary carries the bone-health line naturally, but if the discharge-summary category itself is being phased out (Larry correction 4), the reviewed note can be a hospital-course or transition note instead; the model's deliverable is the review either way.
3. Reuse vs rebuild the chart: the existing chronic-disease review and chart support the catch; the new artifact is the complete signed resident summary, plus a confirmation that the chart shows no bone-health workup.

## Build sequence (Phase 2, after approval)
Build the complete signed resident summary (input), then confirm the chart shows no bone-health workup (reachability), then the golden (flag plus keep-open plus the faithful items), then the five-block grader (central failure is missing the over-attestation; anti-paralysis credited not penalized; credit the faithful items), then the plain review prompt (no trap hint, nothing primes bone-health), then the prereg with a bimodal read, then the gates, then the pilot, then FA/GA on the second-lowest distinct, then the PLs. All on the current formats.
