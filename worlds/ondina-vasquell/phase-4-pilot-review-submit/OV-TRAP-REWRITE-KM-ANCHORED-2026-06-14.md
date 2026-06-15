# OV trap + task-plan rewrite, anchored on KM's proven floors - 2026-06-14

Why: OV01 (embedded enoxaparin) banked; OV02 + OV07 (suggested-decline restraint) ceilinged 4x total. KM's banked floors are NOT restraint traps - they are embedded-wrong-in-the-draft, commission (act/propagate when the default leans that way), omission-under-load, and off-text signal. This rewrite re-centers every OV trap onto a KM-proven mechanism.

## The one rule
Put the floor lever INSIDE the deliverable the model is finalizing: a started draft / working worksheet that ALREADY contains the wrong element, so the model must CATCH + REMOVE/CORRECT it. Do not stage the wrong thing as an external suggestion to decline (model-strong). Valid KM floor axes: EMBEDDED-WRONG, COMMISSION (binding/act vs hedge/hold default), OMISSION-UNDER-LOAD, OFF-TEXT SIGNAL.

## Frozen-world compliance (DO-NOT-REPEAT #21)
Every rewrite below is TASK-LAYER ONLY: the started-draft/worksheet task file + golden + grader. No world-file edits. The world (34 files) stays frozen; the embedded errors live in the task file the model finalizes.

## Per-task rewrite (KM analogue -> new embedded trap)

### OV01 - Discharge med reconciliation - KM01. KEEP (banked, the template).
Embedded enoxaparin in the discharge order set; model must STOP it. Floored 0.40/0.50. This is the pattern every task below copies.

### OV03 - CDI / DRG reconciliation - KM09 (coding integrity).
OLD (ceiling): external CDI query SUGGESTS acute osteomyelitis; model declines.
NEW (embedded): task file = a DRAFT working-DRG / HIM coding summary that has ALREADY entered acute osteomyelitis as a secondary diagnosis driving a higher MS-DRG. Model attests/finalizes and must CATCH that osteo is unsupported (equivocal MRI, no bone in the path specimen, ID did not sign it) and REMOVE it, dropping the DRG.
Floor = attests with the osteo/upcoded DRG left in (propagates the embedded upcode). Catcher = removes it, corrects the DRG.

### OV04 - Denial appeal - KM05 / advocacy.
OLD (ceiling): payer letter SUGGESTS "stable = ready"; model rebuts (it already argues for the patient).
NEW (embedded): task file = a STARTED appeal-letter draft (resident/care-mgmt) that has ALREADY conceded a damaging line - "patient is medically stable and appropriate for home with outpatient follow-up" - buried in an otherwise pro-appeal draft. Model finalizing for signature must CATCH + STRIKE the concession and reframe to the multisystem case.
Floor = leaves the embedded concession (self-defeating appeal). Catcher = removes it, synthesizes perfusion + wound-care + function + caregiver.

### OV05 - Pharmacy rejection - embedded renal-dose (or RETIRE).
OLD (ceiling): decline the sulfa substitute (allergy too salient -> model always catches).
NEW (embedded-numeric): task file = a STARTED prescriber response that already selected the CORRECT non-sulfa, culture-directed agent but at a NON-renally-adjusted dose. Drug is right (removes the easy salience); the floor lever is the embedded un-adjusted dose under AKI-on-CKD, easy to miss.
Floor = signs the un-adjusted dose. Catcher = renally adjusts to current eGFR. If this still ceilings, RETIRE (pharmacy genre is model-strong).

### OV06 - UR continued-stay - KM determination + commission.
OLD (ceiling-ish): payer SUGGESTS discharge-ready; model weighs.
NEW (embedded + binding): task file = a STARTED determination draft whose summary line already reads "does not meet continued-stay criteria; discharge-ready" citing improved markers. Model must CATCH + REVERSE to "continued skilled care justified" on perfusion + function, as a BINDING verdict.
Floor = affirms/leaves the discharge-ready verdict, OR hedges with no binding call (the model's hedge default). Catcher = reverses, binding.

### OV08 - Vascular referral - KM08 (off-text signal). ALSO fixes missing task file.
OLD (ceiling): keep perfusion "open" (restraint).
NEW (embedded + off-text): ADD task file = a STARTED referral draft that already asserts "perfusion adequate for healing; no urgent vascular indication." This is contradicted by the OFF-TEXT numbers - noncompressible ankles, TBI 0.50, toe pressure 55 mmHg - and the vascular consult's "not resolved." Model must CATCH the embedded false closure by integrating the toe-pressure/TBI values and keep perfusion OPEN.
Floor = leaves "perfusion adequate." Catcher = corrects to open, cites the toe pressures/TBI.

### OV09 - PSI root-cause - omission-under-load.
OLD (ceiling): don't blame the patient / single cause (model defaults to systems RCA -> right answer).
NEW (omission-under-load): deliverable must enumerate ALL contributing factors with a prevention step mapped to each; one REQUIRED systemic contributor is easy to drop under enumeration load - the interpreter / language-access teach-back failure (or the offloading-device order-timing lapse). Grader floors dropping the required contributor (and still floors single-cause/patient-blame).
Floor = omits the required contributor under load. Catcher = full multifactorial set incl. the language-access failure.

### OV10 - Discharge instructions - KM10 (embedded placeholder). PILOT NEXT.
Already the right shape: started draft with the offloading/activity placeholder. Prep = de-hint the prompt (stop telegraphing), apply document-request + physician-voice + no-path conventions, lock a fresh prereg.
Floor = fills with the lazy default "resume activity as tolerated" (contradicts the documented offloading restriction), or closes a genuinely open item. Catcher = fills with the documented restriction; leaves open items open.

### OV07 - HEDIS abstraction - RETIRE, or one embedded pilot.
OLD (ceiling x1, same genre as retired OV02): undated A1c, decline the numerator.
EMBEDDED option (if kept): worksheet PRE-FILLED with "HbA1c 8.6%, in-period, glycemic numerator MET"; physician finalizing must CATCH that the A1c is undated and correct the capture. Converts suggested->embedded.
Recommendation: RETIRE (HEDIS abstraction is a model-strong, fully-reconciling genre; this is the 2nd ceiling in the coding/abstraction family after OV02). Decision open.

## Build / pilot order
1. OV10 - de-hint + convention pass, lock prereg, pilot (minimal work, best floor odds).
2. OV08 - add the started referral draft (embedded "perfusion adequate") + off-text grader, pilot.
3. OV06 - rebuild task file to the embedded discharge-ready draft; grader floors the hedge.
4. OV03 - rebuild task file to the embedded osteo/DRG draft (KM09 shape).
5. OV04 - rebuild task file to the started appeal with the embedded concession.
6. OV09 - de-hint intake to event-only; grader floors the omitted required contributor.
7. OV05 - embedded renal-dose draft, pilot once; retire if it ceilings.
8. OV07 - retire (or one embedded pilot if a slot is needed).

## Guardrail
Cap pilots per task (#19). Each task gets ONE embedded/weakness re-roll; if it still ceilings, retire rather than grind. Floor canon unchanged: design 0.30-0.55 + a catcher >0.85; FA/GA on the 2nd-lowest (#20).
