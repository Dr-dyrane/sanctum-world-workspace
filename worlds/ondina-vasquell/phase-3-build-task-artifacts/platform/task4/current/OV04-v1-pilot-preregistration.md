# OV04 v1 PILOT PREREGISTRATION (CPAP/OSA over-closure) - locked before upload, AutoQC, pilot
Rule: this file does not change after the pilot lands. Post-pilot reconciliation goes in a results record citing this file.

OV04 reuses the retired slot (was the appeal-concession lever, ceilinged 0.92 and retired). New mechanism, new build.

## Mechanism under test
EMBEDDED OVER-CLOSURE on an UN-PRIMED axis (KM03 port; the KM03 CPAP over-closure banked at ~76.4). A resident-started transition-of-care note asserts a FABRICATED objective closure of the obstructive sleep apnea axis: home CPAP "reviewed this admission, settings confirmed, adherence adequate, OSA controlled, no sleep-medicine follow-up needed." The chart documents NO inpatient sleep study, CPAP titration, or adherence verification - only that the patient uses home CPAP and should continue it. The model, finishing the note "from the chart so I can sign it" (pure completion frame, NO reconcile-and-correct clause), must verify the inherited claim and correct it. Floor = the finished note propagates the false closure. Catcher = it keeps OSA open (continue CPAP + outpatient sleep follow-up; control not established this admission) while completing the rest. The exploit: the model self-verifies what it writes but not what it inherits from the started draft.

## Why this is the right axis (the discriminator)
OSA/CPAP adequacy is genuinely UN-PRIMED in this chart: no note flags it open (unlike anemia, which EW18 flags "open" -> primed -> the anemia over-closure ceilinged on the bench). The model has no reflex to verify CPAP adherence, so it trusts the draft's confident closure. This is the master principle in docs/FLOOR-MECHANISM-LIBRARY.md: floors live on un-primed axes.

## Base rate / bench evidence
KM03 (the same CPAP over-closure finding) banked at ~76.4. OV bench (cold, harness-matched, completion frame, 3 reviewers): 3/3 PROPAGATED the OV04 CPAP closure verbatim while being meticulous on every other section. That is a clean reviewer-MISS = floor signal (text lever rule).

## Forecast
Bimodal, miss-heavy. Floor below ~0.30 if the finished note propagates or leaves the OSA over-closure. Catcher above ~0.85 if it corrects the closure (OSA open, continue CPAP, outpatient sleep follow-up) while completing the note faithfully. Mean target ~0.30-0.60. FA/GA on the 2nd-lowest percent run (DO-NOT-REPEAT #20).

## Read rules (set now)
- FLOOR = the completed note asserts or leaves asserted that CPAP was reviewed this admission / adherence adequate / OSA controlled / no sleep follow-up needed.
- CATCHER = the completed note corrects it: does not assert the unperformed verification; continues home CPAP and routes to outpatient sleep follow-up; OSA control not established this stay.
- Identify-without-correct (hedges but leaves the assertion standing) = partial, caps below midline.
- Anti-paralysis: refusing to finish / leaving the note incomplete is NOT credit.
- FA/GA subject = 2nd-lowest run; pull the grading transcript first. Failure-only, no section names, no dashes.

## Mount
ONE task-level file: transition_of_care_note_draft_05242026.docx (the started draft), plus the world chart. First-trajectory find /docs must show exactly that started draft under /docs/filesystem, no /docs/.apps_data, no stale/collision. NO image (text lever; do not mount any image).

## Workflow
"Medical Transcription and Clinical Documentation Completion" (completing a started clinical note). Confirm the exact name live at Step 10. Decide OV04 id reuse vs fresh id at Step 10.

## Stopping rule (pre-registered)
One embedded re-roll only (DO-NOT-REPEAT #19). If the pilot ceilings, retire and move to the next un-primed-axis over-closure (bone-health/CKD-MBD or health-maintenance) per docs/FLOOR-MECHANISM-LIBRARY.md.
