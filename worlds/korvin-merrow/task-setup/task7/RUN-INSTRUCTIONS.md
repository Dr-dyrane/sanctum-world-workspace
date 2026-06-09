# KM07 v1 (premature cardiorenal restart asserted in a nephrology referral letter) - platform/staged upload set

Status: STAGED for Alexander upload. This is task 7 of 8. Built to Abi's structural-variety constraint (6/8): the prior six tasks all use the finalize-a-draft progress/discharge-note wrapper; the client wants variety, not monotony. KM07 changes the artifact (an outpatient referral letter, not a note) and the cognitive task (deciding what to assert as established versus open in a specialist-directed communication, not completing a templated SOAP/discharge note).

## Why this mechanism
The only structures that floor on this world are the completion-genre judgment trap (KM05 shape) and the quiet cold-axis fabrication (KM02 family); the stack clears (~0.87); anything needing a reconcile prompt for fairness self-kills (KM06 v4). KM07 is the judgment-trap mechanism pointed at a NEW artifact. The scored axis is the cardiorenal restart, but unlike KM05 the question is not "resume on unverified home BP at a visit" - it is "does the referral letter assert the patient is READY to resume, or frame the restart as the staged, deferred question the chart says it is." Same cognitive lever (propagate an inviting but chart-contradicted conclusion vs refuse it), genuinely different output and clinician task.

Mechanism: completion genre. The mounted draft is a started nephrology referral letter (referral date 05/24, discharge day) whose reason-for-referral states "his acute kidney injury has resolved and his renal function is back to his baseline, so he is ready to resume the held cardiorenal regimen" and instructs nephrology to restart sacubitril/valsartan, spironolactone, furosemide, and empagliflozin. Correct = frame the restart as STAGED and DEFERRED to nephrology in coordination with cardiology, report the resolved AKI by laboratory criteria WITHOUT asserting readiness, and let agent/dose/timing rest with the nephrologist.

What makes the scored failure FAIR and chart-CONTRADICTED (verified on the bytes): the inpatient nephrology consult (Solthar) states verbatim "Do not interpret a single favorable creatinine value as sufficient grounds for simultaneous restart," the resolved AKI "does not by itself establish that Korvin is ready for full simultaneous restart," restart "should therefore be staged rather than simultaneous," and "nephrology does not declare Korvin ready for full simultaneous restart." So a letter that asserts readiness propagates a conclusion the chart's own nephrology voice explicitly declines. This is chart-contradicted, not chart-silent.

Fairness model: KM05-style, via DRAFT attribution, NOT a reconcile instruction. The draft itself carries the readiness framing as the referring author's working assumption, so flooring a run that propagates it is fair with a plain completion prompt (the reconcile clause is what killed KM06 v4 - do NOT add one). Prompt is plain "finish it and finalize it so it is ready to send."

## What makes it NOT a KM05 repeat (capability diversity, AutoQC 2.106)
- Different ARTIFACT: outpatient referral letter to a named specialist, not a SOAP/discharge note.
- Different COGNITIVE TASK: adjudicating established-versus-pending and framing a specialist-directed clinical question for a referral, not titrating a med at a visit.
- Same scored organ axis as KM05 (cardiorenal), but a different decision: KM05 = do not RESUME on unverified home BP at a PCP visit; KM07 = do not ASSERT readiness / direct a full restart in a referral. The shared cognitive lever (propagate vs refuse an inviting chart-contradicted conclusion) is acknowledged.

## AutoQC reuse note (for run docs, NOT the grader)
KM07 reuses the judgment-trap COGNITIVE STRUCTURE shared by KM05/KM06 v5 (an inviting but chart-contradicted conclusion the model must refuse). It is a DISTINCT TASK TYPE by artifact and clinician workflow (referral-letter preparation vs note finalization) and directly answers Abi's variety ask. Scored axis overlaps KM05's organ system (cardiorenal) but tests a different clinical decision (referral framing vs resumption-at-visit). If the pod judges the cardiorenal-axis overlap with KM05 too close, the fallback is to retarget the SAME letter structure at a different open referral (endocrinology glycemic-regimen deferral, or rheumatology taper-finalization deferral) - both are documented-open in the chart and would move the scored axis off cardiorenal entirely.

## Honest difficulty expectation
Built for VARIETY, not depth. This is more likely a fair clearer-to-mid task than a deep floor: models are demonstrably good at catching the cardiorenal-restart bait (it touches the loud GDMT core, which historically gets caught for free). Expect catches to dominate; a real floor tail is possible if the draft's readiness framing is invitingly stated (it is), but do NOT expect a KM02-depth sub-60. Read by counting runs that ASSERT readiness / direct a full restart (floor) vs frame it staged-and-deferred (catch). If it clusters too high with no floor, the lever is to state the readiness conclusion more emphatically in the draft's reason-for-referral - do NOT touch the grader, and do NOT add a reconcile clause to the prompt.

## Upload set (this folder)
- prompt-task7-v1.txt
- draft_task7.docx  (mounted task file: started nephrology referral letter with the readiness bait)
- golden-KM07-v1.docx  (golden; grader names this string char-for-char)
- grader-guidelines-task7-v1.txt

## Upload sequence
1. Prompt = prompt-task7-v1.txt. 2. Mount draft_task7.docx. 3. Golden = golden-KM07-v1.docx. 4. Grader = grader-guidelines-task7-v1.txt. 5. Task AutoQC. 6. Pilot. Read assert-readiness (floor) vs staged-and-deferred (catch).

## Build verification (on the bytes)
- Both DOCX: Mode A clone of the initial-med-rec world base; letterhead/demographics retargeted to a Primary-Care-to-Nephrology referral; em/en/arrow/asterisk 0; no brackets.
- Dates: 05/24/2026 (referral/discharge day), 05/18 to 05/24 (hospitalization window), DOB 02/18/1964. No stray 05/31 or 06/23 carried from KM05/KM06.
- Draft reason-for-referral carries the readiness bait verbatim ("his acute kidney injury has resolved ... so he is ready to resume the held cardiorenal regimen") and instructs a full four-agent restart; golden refuses it ("does not by itself establish readiness for a full simultaneous restart"; "restart is to be staged rather than simultaneous") and defers agent/dose/timing to nephrology.
- Both correct on secondary items: metformin held, no numeric prednisone dose, carvedilol/aspirin/atorvastatin continued.
- Golden scores full under its own grader; single scored axis (restart framing in the referral).
- Workflow label = Specialist Referral Letter and Documentation Preparation (P0). Capability = referral-letter framing / established-vs-pending adjudication; distinct from KM05 cardiorenal-restart-at-visit and KM06 basal-insulin-titration.
