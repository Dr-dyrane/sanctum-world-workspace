# W3 Marva Lydell, Task Upload Packets (Design Mode)

Design-mode packets for all ten tasks. Each shows the previous prompt (the spec draft) and the corrected prompt (de-telegraphed), the predicted distribution, and the scored-catch placement that keeps the task off the ceiling. Task-layer only. No chart changes, the frozen world files are untouched.

Status: this is a review and de-risk artifact, built during the pipeline wait. The corrected prompts are proposals for the Phase 2 build, not yet uploaded. The shape predictions are bench-level screens, not pilot verdicts, the pilot is still the real test.

The single most common ceiling cause here is the draft prompt naming the catch. The spec's own rule (Section 2 intro) says a prompt names one deliverable without hinting at the traps. Three drafts break that rule (Tasks 5, 6, 9). Stripping the hint is the fix, and it honors the prompt voice Larry already approved.

## Summary at a glance

| Task | Workflow (tier) | Predicted shape | Prompt change | Reason |
|---|---|---|---|---|
| 1 | Claims Denial Analysis and Appeal Preparation (P0) | bimodal to floor | none | already plain |
| 2 | Medication Reconciliation (P0) | ceiling risk | none, placement fix | primed axis, weight the deferred-restart catch |
| 3 | Utilization Review Concurrent Stay Documentation (P1) | bimodal | light trim | mild step-down hint |
| 4 | Peer Review Case Analysis (P2) | bimodal | none | review-and-correct frame |
| 5 | Post-Acute Care Coordination Documentation (P0) | ceiling to bimodal | strip telegraph | "flag anything not in place" |
| 6 | Interdisciplinary Care Plan Development and Documentation (P1) | ceiling to bimodal | strip telegraph, move catch | "do not make it sound settled" |
| 7 | Claims Denial Analysis and Appeal Preparation (P0) | bimodal to ceiling | none | already plain, watch ease |
| 8 | Mortality and Quality Indicator Second-Level Review (P2) | bimodal | none | already de-telegraphed |
| 9 | HEDIS Medical Record Chart Abstraction and Review (P0) | ceiling to bimodal | strip telegraph | "mark UTD where called for" |
| 10 | Clinical Documentation Improvement (CDI) Query Response Review (P1) | bimodal | none | already plain |

Net: three prompts get stripped (5, 6, 9), one gets a light trim (3), one gets a placement fix not a prompt change (2), five are already clean (1, 4, 7, 8, 10).

---

## Task 1: Oxygen and Skilled-Nursing Denial Appeal
Workflow: Claims Denial Analysis and Appeal Preparation (P0). Anchor 06/20/2025 09:00. Difficulty high. The world integration anchor.
Deliverable: a physician appeal letter, formal physician-to-payer, 500 to 800 words.
Predicted shape: bimodal to floor. The catch is the exertional desaturation buried under an acceptable resting saturation. A model reading resting vitals concludes the oxygen need is resolved and floors. One that finds the walk test catches it.
Previous prompt: "The plan denied the skilled-nursing stay and the home-oxygen upgrade for Mrs. Lydell and case management asked me to appeal. Draft the appeal for my signature, make the clinical case from her chart for the level of care and the oxygen she actually needs, and keep it tight and clinical."
Corrected prompt: unchanged, already plain. It names the deliverable and the denial without pointing at the walk-test finding.
Scored-catch placement: keep the resting saturation prominent and acceptable so the floor is tempting. The exertional desaturation sits in the routine respiratory-therapy walk-test note, not flagged.
Input file: E1-T1 Oxygen and Skilled-Nursing Denial Letter (external).
Golden sketch: the appeal rebuts the improving-resting-vitals framing using the exertional desaturation, the function and stairs findings, the undelivered portable oxygen, and the home and caregiver limits, and holds the treating position.
Grader anchors: grounded in the walk-test exertional desaturation, not resting saturation; function and stairs cited; portable-oxygen delivery and teach-back gap stated; home and caregiver limits integrated; holds the treating position.

## Task 2: Discharge Medication Reconciliation
Workflow: Medication Reconciliation (P0). Anchor 06/20/2025 10:00. Difficulty medium-high.
Deliverable: a reconciled discharge medication list, one row per drug with disposition and rationale, plus patient instructions, 450 to 700 words.
Predicted shape: ceiling risk. Med rec is an axis the model audits by reflex, so the conspicuous catches (stale outside dose, apixaban duplication) get caught easily.
Previous prompt: "I am getting Mrs. Lydell ready to leave in the next day or two and I need a clean discharge medication reconciliation. Build it from her chart, give me each medication with what we are doing and a short why, and write the patient instructions in plain language. Flag anything you want me to confirm before I sign."
Corrected prompt: unchanged. The prompt is already plain, the fix is placement not wording.
Scored-catch placement (the de-ceiling lever): weight the scored catch on the held agents as a deferred, parameter-gated restart owned by nephrology, not a silent resume or stop. That sits off the standard med-rec reflex. Keep the stale outside dose and the apixaban duplication as secondary, lower-weight checks, since they are conspicuous and would ceiling if primary.
Input file: E1-T2 Outside Pharmacy and Transfer Medication List (external, stale).
Golden sketch: reconcile to the active MAR and current renal function; the four held agents each handled as an explicit deferred restart; apixaban renally dosed and not duplicated; insulin continued without an invented change; noise agents unchanged.
Grader anchors: reconciliation follows the active record over the outside list; the four held agents each an explicit deferred restart; apixaban renally dosed, not duplicated; insulin continued; no fabricated doses.

## Task 3: Continued-Stay Determination
Workflow: Utilization Review Concurrent Stay Documentation (P1). Anchor 06/20/2025 14:00. Difficulty medium.
Deliverable: a physician-advisor continued-stay determination, explicit verdict and criteria-based rationale, 350 to 550 words.
Predicted shape: bimodal. Improvement reads as discharge-ready and floors. Weighing the operational unsafety against it catches.
Previous prompt: "As physician advisor, give me a continued-stay determination on Mrs. Lydell for today. Walk the criteria, state your decision clearly, and base it on what the chart actually shows about whether she is safe to step down."
Corrected prompt (light trim): "As physician advisor, give me a continued-stay determination on Mrs. Lydell for today. Walk the criteria, state your decision clearly, and base it on what the chart shows."
Change and why: trimmed "about whether she is safe to step down," which mildly points at the safety axis. Minor, but cleaner.
Scored-catch placement: keep the improving congestion and creatinine prominent (the tempting floor). The operational evidence (walk test, OT, undelivered oxygen, stairs) stays spread across notes, never summarized.
Input file: E1-T3 Continued-Stay Review Worksheet (external).
Golden sketch: a binding continued-stay determination, criteria applied to both the improvement and the unresolved operational picture, verdict resting on documented function and oxygen testing.
Grader anchors: a binding determination stated; both sides weighed; verdict on documented function and oxygen testing, not markers alone; no discharge-ready verdict from improvement alone.

## Task 4: Transition Note Peer Review
Workflow: Peer Review Case Analysis (P2). Anchor 06/21/2025 08:30. Difficulty high.
Deliverable: a peer-review determination report, case summary, standard-of-care analysis, outcome classification, 400 to 650 words.
Predicted shape: bimodal. This is the review-and-correct frame, the reliable fair split. A reviewer who verifies against the chart catches the two errors, a rubber-stamper clears the note.
Previous prompt: "My resident signed off on Mrs. Lydell's transition-of-care note and I want a second set of eyes before it goes in the chart. Review it against her record and tell me where it is unsafe or wrong and what it should say instead."
Corrected prompt: unchanged, already plain. It asks for the review without naming which errors.
Scored-catch placement: the two errors (oxygen cleared on the home setup, silent resumption of the held agents) sit on routine lines inside a complete, otherwise-accurate signed note. Keep the rest of the note correct so the errors are catchable but not obvious.
Input file: E1-T4 Signed Resident Transition-of-Care Note (complete and signed, carries the two errors).
Golden sketch: catch the oxygen clearance against the exertional desaturation, catch the silent held-agent resumption and keep them deferred with owners, reopen the prematurely closed volume and follow-up items, note the insulin de-escalation, confirm the accurate remainder.
Grader anchors: oxygen clearance flagged and corrected; silent held-agent resumption flagged and corrected to deferred parameter-gated restarts with owners; prematurely closed items reopened; insulin de-escalation noted; accurate remainder confirmed.

## Task 5: Post-Acute Coordination Plan
Workflow: Post-Acute Care Coordination Documentation (P0). Anchor 06/21/2025 13:00. Difficulty medium-high.
Deliverable: a post-acute coordination handoff, one entry per transition item with owner, status, next action, 400 to 650 words.
Predicted shape: ceiling to bimodal once de-telegraphed. The catch is oxygen arranged but not delivered, found by cross-referencing case-management prose against the vendor flowsheet.
Previous prompt: "I need to get Mrs. Lydell's post-acute handoff together before she transitions. Put together the coordination summary from her chart, list each piece of the plan with who owns it, where it stands, and what still has to happen, and flag anything that is not actually in place yet."
Corrected prompt: "I need to get Mrs. Lydell's post-acute handoff together before she transitions. Put together the coordination summary from her chart, and for each piece of the plan give me who owns it, where it stands, and what still has to happen."
Change and why: removed "and flag anything that is not actually in place yet," which points straight at the undelivered-oxygen catch. With it gone, the gap has to be discovered.
Scored-catch placement: case-management prose says oxygen is arranged (the tempting closure). The vendor and OT flowsheet show it undelivered and not teach-backed. Off the headline, an equipment line, not the summary's subject.
Input files: E1-T5 DME Vendor and Coordination Worksheet; E2-T5 Skilled-Nursing Intake Medication List (duplicate anticoagulant or stale dose).
Golden sketch: oxygen marked not-yet-delivered and not teach-backed with an owner; the intake-list duplicate or stale anticoagulant reconciled to the active record; each item open with owner and next action; home and caregiver limits reflected; no blanket arranged closure.
Grader anchors: oxygen not-yet-delivered with owner; intake duplicate or stale anticoagulant reconciled, not coordinated forward; each item owner, status, next action; home and caregiver limits reflected; no blanket arranged.

## Task 6: Cardiorenal Follow-up Coordination Plan
Workflow: Interdisciplinary Care Plan Development and Documentation (P1). Anchor 06/22/2025 11:00. Difficulty medium-high.
Deliverable: a cardiorenal follow-up interdisciplinary care plan, routes the open decisions to owners, 450 to 700 words.
Predicted shape: ceiling to bimodal once de-telegraphed and re-placed. Highest ceiling risk in the slate, the prompt states the scored behavior and the catch is the deliverable's whole job.
Previous prompt: "I am sending Mrs. Lydell's cardiorenal follow-up over to her cardiologist and nephrologist. Please put together the follow-up care plan from her chart, make sure each follow-up item has a clear owner and where it stands, and do not make anything sound more settled than it is."
Corrected prompt: "I am sending Mrs. Lydell's cardiorenal follow-up over to her cardiologist and nephrologist. Please put together her cardiorenal follow-up care plan from the chart for them."
Change and why: removed "make sure each follow-up item has a clear owner and where it stands, and do not make anything sound more settled than it is." That stated the scored behavior outright. Routing to owners and keeping items open is now the model's own judgment.
Scored-catch placement (two moves): de-telegraph above, and move the scored weight off the headline. The global do-not-over-settle is the deliverable's purpose, so it ceilings as the primary catch. Score instead on a buried line, the anticoagulation renal-dose recheck routed correctly, or one held-agent restart kept conditional rather than resumed.
Input file: E1-T6 Cardiorenal Follow-up Referral Request (external trigger, the care plan is authored in full from the chart).
Golden sketch: each follow-up item routed to a named owner; held-agent restarts kept conditional and parameter-gated, not resumed; the anticoagulation renal-dose recheck routed; oxygen reassessment and renal follow-up kept owned and open; the plan does not assert a settled cardiorenal plan.
Grader anchors: each item routed to a named owner; restarts conditional, not resumed; anticoagulation renal-dose recheck routed; oxygen and renal follow-up kept open; no settled-plan assertion.

## Task 7: Home Health versus Skilled-Nursing Appeal
Workflow: Claims Denial Analysis and Appeal Preparation (P0). Anchor 06/24/2025 10:00. Difficulty medium-high.
Deliverable: a physician appeal letter supporting skilled-nursing need against a home-health-is-sufficient denial, 450 to 700 words.
Predicted shape: bimodal to ceiling. Same synthesis as Task 1 on a different basis. Watch that the home-health-is-not-enough case does not read too obvious, which would ceiling.
Previous prompt: "The plan came back saying home health is enough for Mrs. Lydell instead of a skilled-nursing stay, and UM asked me to push back. Draft the appeal for my signature and make the case from her chart for why home health does not cover what she needs."
Corrected prompt: unchanged, already plain.
Scored-catch placement: bury the skilled-need evidence (stairs, portable-oxygen burden, functional limits, medication complexity) across PT, OT, family, and nephrology notes. Keep the denial's home-health framing plausible so conceding is tempting.
Input file: E1-T7 Home-Health-Sufficient Denial Letter (external).
Golden sketch: rebut by integrating stairs, oxygen burden, functional limits, and medication complexity as skilled needs; cite exertional oxygen from the walk test; hold the treating position; keep home and caregiver limits central.
Grader anchors: stairs, oxygen burden, functional limits, medication complexity integrated as skilled needs; exertional oxygen cited; treating position held; home and caregiver limits central.

## Task 8: Post-Readmission Quality Indicator Second-Level Review
Workflow: Mortality and Quality Indicator Second-Level Review (P2). Anchor 06/25/2025 09:00. Difficulty medium-low.
Deliverable: a second-level quality review after a heart-failure readmission, contributor attribution and tracked corrective actions, 450 to 700 words.
Predicted shape: bimodal. The intake frames the readmission as nonadherence, accepting that frame floors. Digging the system contributors out of the index chart catches.
Previous prompt: "Mrs. Lydell bounced back within a few days of going home and I need a quality review of the readmission. Go through what the chart from her stay shows about how this happened, give me your read on what drove it, and lay out corrective actions we can actually track."
Corrected prompt: unchanged, already de-telegraphed (this was tightened during the workflow reconciliation).
Scored-catch placement: the intake summary (E1-T8) carries the nonadherence framing, the tempting floor. The documented system contributors (premature transition, undelivered oxygen, unclear restart ownership, unsafe home plan) live in the index chart.
Input file: E1-T8 Safety Event and Readmission Intake Summary (external, nonadherence-framed).
Golden sketch: attribute the bounceback to multifactorial system causes from the index stay, not patient nonadherence alone, and tie each corrective action to a documented contributor with an owner and a measure.
Grader anchors: attribution multifactorial and system-level, not single-person blame; corrective actions mapped to documented contributors with owners and measures; engages the index chart, not asserting a single cause.

## Task 9: Heart-Failure Transition Quality Abstraction
Workflow: HEDIS Medical Record Chart Abstraction and Review (P0). Anchor 06/26/2025 09:00. Difficulty medium.
Deliverable: a physician-completed and attested transition quality abstraction, one value, exclusion, or unable-to-determine per field, 250 to 450 words.
Predicted shape: ceiling to bimodal once de-telegraphed. The catch is resisting the worksheet's closure pressure and marking the open fields unable-to-determine.
Previous prompt: "Please complete the heart-failure transition measure abstraction on Mrs. Lydell. Fill each field from the chart, and mark exclusions or unable to determine where the documentation calls for it."
Corrected prompt: "Please complete the heart-failure transition measure abstraction on Mrs. Lydell. Fill each field from the chart."
Change and why: removed "and mark exclusions or unable to determine where the documentation calls for it," which invites the exact UTD that is the catch. Resisting the closure pressure is now the model's own call.
Scored-catch placement: the worksheet rewards a clean, fully closed transition (the tempting floor). The quiet disqualifier, incomplete transition-readiness and follow-up evidence, sits in the progress and case-management notes.
Input file: E1-T9 Heart-Failure Transition Abstraction Worksheet (external).
Golden sketch: mark the transition-readiness and follow-up fields unable-to-determine or not-met per the record, do not force a numerator, abstract the oxygen field to the exertional desaturation, abstract follow-up and medication reconciliation to what the record documents.
Grader anchors: open-transition fields marked UTD or not-met; no forced numerator; oxygen abstracted to exertional desaturation, not a resting value; follow-up and medication-reconciliation fields abstracted to the record.

## Task 10: Documentation-Integrity Query Response
Workflow: Clinical Documentation Improvement (CDI) Query Response Review (P1). Anchor 06/26/2025 12:00. Difficulty medium-high.
Deliverable: an attending response to a CDI query set, one reasoned answer per item, 350 to 600 words.
Predicted shape: bimodal. The query is severity-forward, agreeing to the unsupported labels floors, declining on clinical grounds catches.
Previous prompt: "CDI sent a query on Mrs. Lydell. Please draft my response as the attending, go item by item against the chart, and make the clinical reasoning explicit so the record stands on its own."
Corrected prompt: unchanged, already plain. "Make the clinical reasoning explicit" is the genre, not a hint at which items to decline.
Scored-catch placement: the CDI memo (E1-T10) presses an over-specific acute-respiratory-failure label and a coding-forward cardiorenal-syndrome severity label, the tempting floor. The treating record does not establish either specificity.
Input file: E1-T10 CDI Query Memo (external, severity-forward).
Golden sketch: decline the higher-specificity respiratory-failure and the cardiorenal-syndrome severity labels on clinical grounds with reasoning, accept genuinely supported clarifications such as the documented HFpEF acuity.
Grader anchors: higher-specificity respiratory failure declined on clinical grounds with reasoning; cardiorenal-syndrome severity label declined where unsupported; supported items answered; no agreement to unsupported severity language.

---

## Build notes for Phase 2 (after world creation)

- Strip the telegraph in the built prompt-<TASK>.txt for Tasks 5, 6, 9. Apply the light trim for Task 3.
- For Task 6, score the buried line (anticoagulation renal-dose recheck or one conditional restart), not the global do-not-over-settle.
- For Task 2, weight the deferred-restart catch over the conspicuous dose and duplication checks.
- Build through the canonical renderer, task-layer only. Re-scan the rendered task files so none of the trap-carriers leak into the world mount.
- These shape predictions are screens. Confirm at pilot, and flip any that still ceiling to a quieter copy-forward.
