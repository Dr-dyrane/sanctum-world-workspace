# OV09 design and grounding - contrast imaging order in AKI on CKD (embedded commission)

Date: 2026-06-17. Engine chosen by Dyrane: embedded-wrong commission (the proven floor profile; OV01/OV06 family). Lane: Diagnostic Test Result Review and Follow-Up Documentation (fresh, verify the exact string on the live 06/13 tracker at Step 10). This is the next live build after OV08; numbering is the live build sequence, not the spec OV01-10 mapping in reference/approved-workflows-and-guidance-2026-06-13.md.

## The mechanism
A started perfusion follow-up / diagnostic plan (resident-drafted, attending to finalize for signature) pre-lists, as a routine carried item, an order to obtain CT angiography of the lower extremity with IV contrast to settle the perfusion and revascularization question. The model finalizing the plan must catch and remove or substitute that order. It is wrong on two independent axes:
- RENAL: baseline eGFR 38 (CKD stage 3b) with active AKI on CKD, creatinine peaked 2.1 on admission and is still resolving toward baseline 1.5 (currently about 1.6, eGFR mid-30s). IV iodinated contrast risks contrast-induced nephropathy; gadolinium risks NSF at low eGFR. Contrast for a non-urgent indication here is avoidable harm.
- DISPOSITION: the signed vascular consult (05/19) left perfusion unresolved, made NO revascularization decision, and deferred angiography to OUTPATIENT, conditional on the wound failing to progress. The wound is currently granulating. Non-contrast perfusion data already exists (the 05/19 ABI/TBI study: toe pressure 55, TBI 0.50). So an inpatient contrast angiogram now is premature as well as renally unsafe.

## Floor vs catch
- FLOOR: the model finalizes the plan carrying the contrast CT-angiography order forward (to definitively answer the open perfusion question), never integrating the renal contraindication or the consult's outpatient-deferred plan.
- CATCH: the model removes or substitutes the contrast order. Reasoning: active AKI on CKD 3b makes IV contrast unsafe; the signed consult already deferred angiography to outpatient and made no revascularization decision; non-contrast duplex (or the existing ABI/TBI) answers the inpatient need; follow the consult's outpatient perfusion plan.

## Why this floors (against-the-grain, cold, embedded)
The completion frame asks the model to finalize an open perfusion workup, and the natural move is to order the definitive study (contrast angiography). The renal contraindication and the consult's outpatient-deferral are secondary to the "assess perfusion" headline, so a satisficing finalize carries the pre-listed order forward. This is the OV06 v2 profile: a routine pre-listed wrong item the completion frame rubber-stamps. The axis is renal safety (distinct from OV06's perfusion-interpretation catch).

## Fairness
Embedded-wrong in a started draft the attending finalizes, de-telegraphed (the order is a routine carried line, no reconcile clause), resident-authored (different author than the golden's attending), in a genre where an attending is expected to review and correct a started order before signing. This is the OV06 v2 fair form (which floored and is banking). The correction is reachable from the mounted chart alone (renal trend, vascular consult, ABI/TBI study). No outside or post-cutoff knowledge: contrast-in-AKI caution is long-established.

## Forecast (lock in prereg)
Bimodal. Floors 0.10-0.35 (finalize with the contrast order kept). Catchers 0.80-0.95 (remove/substitute on renal + outpatient-deferral grounds). Mean roughly 0.40-0.55. Floor if >=4/10 keep the contrast order. KNOWN RISK: contrast-in-renal-impairment is a semi-standard safety reflex, so it may ceiling (the model catches it like a standard check). Per the OV03 lesson, bench is a screen, not a verdict: build and pilot. If all-catch, the standby is to make the order an off-text item or move the catch to the purely-disposition axis.

## Files (to build)
- Deliverable: started_perfusion_followup_plan_05242026.docx (resident-drafted, contrast order pre-listed, attending to finalize).
- Golden: golden-OV09-v1.docx (attending finalization that removes/substitutes the contrast order).
- Grader: grader-guidelines-OV09.txt. Prompt: prompt-OV09.txt. Build: build/build_ov09.py through build_one.
- Full OV chart mounted; decisive files = renal_lab_trend, vascular_consult_note, abi_tbi_study_report.

## COLD-BENCH RESULT 2026-06-17 - 3/3 CAUGHT, RETIRE (contrast axis is chart-loud, not cold)
Three harness-matched cold readers all cancelled the contrast CT-angiography order. Decisive finding I missed in grounding: the FROZEN admission H&P explicitly states "avoid nephrotoxins and contrast." So the resident's contrast order contradicts an explicit chart directive, not a quiet axis. All three caught it instantly by matching the order against that directive plus the AKI status and the consult's outpatient deferral. This is the swatted-away / self-incriminating profile (Edmund/OV06 fairness bar) and a will-ceiling stop sign (red-team rule: a cold-caught catch-and-reverse trap ceilings). Unlike OV06 v2 (whose catch needed multi-step synthesis the harness satisficed past), OV09's catch is a one-line chart contradiction, so the bench is reliable here. The contrast axis is DEAD on OV, the frozen chart pre-empts it, like the heel/offloading axis. Do NOT pilot. Re-center the OV09 slot.

PILOT CONFIRMATION 2026-06-17 (job 21e12fc3): piloted anyway; CEILINGED all-catch (0.88,0.88,0.88,0.92,0.90,0.90,0.95,0.85,0.92,0.85; mean 0.89, no floor). Every run removed the contrast order; Attempt 10 cited the admission H&P "avoid nephrotoxins and contrast" verbatim. The cold-bench prediction held exactly. RETIRED, not bankable. Record: results/OV09-v1-pilot-2026-06-17-job-21e12fc3.md.
