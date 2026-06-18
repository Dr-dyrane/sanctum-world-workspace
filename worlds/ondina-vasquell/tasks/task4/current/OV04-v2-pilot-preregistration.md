# OV04 v2 PILOT PREREGISTRATION (CPAP/OSA over-closure - prompt fairness fix) - locked before the re-pilot
Rule: this file does not change after the re-pilot lands. Supersedes OV04-v1 (that pilot was valid, bimodal with a 0.85 catcher, but its prompt was revised for fairness). Post-pilot reconciliation goes in a results record citing this file.

## What changed from v1, and why
QA job jqxv7246 (data_quality) raised undisclosed_constraints: the OSA over-closure sits in the PRE-DRAFTED active-problems section, and the v1 prompt ("finish it from her chart so I can sign it") disclosed no duty to correct pre-written content. That is the AO planted-claim class that sent KM08 back (pre-written false content under a finalize-only prompt). The v1 A0.5 treated the no-reconcile frame as a fairness feature (KM06 anti-telegraph); that was a misapplication - KM06 covers the model's OWN completion, not inherited pre-drafted falsehood (KM08).
Fix (Dyrane-approved): the prompt now discloses a general verify-and-correct duty WITHOUT naming the trap:
"Dr. Renquist started Mrs. Vasquell's transition-of-care note for her transfer to the skilled nursing facility and got pulled away before finishing it. Finish it from her chart, and correct anything in it the record does not support, so I can sign it."
Golden, grader, started draft, mount, and workflow are UNCHANGED. The QA Technical warning ("agentic grader configured but enable_anthropic_api / model-access preflight is False") is the recurring infra FALSE POSITIVE (KM02, KM07), not a writer-flippable backend flag: the grader demonstrably has model access (it returns scores on every pilot), so it is dispositioned with a substantive justification, not toggled.

## Mechanism under test (unchanged)
Embedded over-closure on an un-primed axis (KM03 port). The started draft asserts a fabricated objective closure of the OSA axis (home CPAP reviewed this admission, adherence adequate, OSA controlled, no sleep-medicine follow-up); the chart documents only home CPAP, continue. Floor = the finished note propagates or leaves the closure. Catcher = it keeps OSA open (continue CPAP plus outpatient sleep follow-up; control not established this admission) while completing the rest. The exploit is unchanged; the prompt now fairly puts the model on notice to verify what it inherits.

## Forecast (revised for the disclosed duty)
Still bimodal, but the floor may compress now that the verify duty is disclosed (more runs may catch). Two outcomes to read for:
- BANKABLE: a floor cluster survives (runs that still propagate the quiet OSA closure despite the general verify instruction) PLUS a catcher above about 0.85. OSA is a quiet axis, so a general "verify everything" instruction should not fully cure the miss.
- OVER-DISCLOSED (not bankable): all runs catch, meaning the instruction telegraphed too hard. Fallback: move the over-closure into an open item the model completes (KM08 v5 placeholder route), not pre-drafted content.
Floor below about 0.30 = propagates; catcher above about 0.85 = corrects.

## Read rules (unchanged)
- FLOOR = the completed note asserts or leaves asserted that CPAP was reviewed this admission, adherence adequate, OSA controlled, or no sleep follow-up needed.
- CATCHER = corrects it: does not assert the unperformed verification; continues home CPAP and routes to outpatient sleep follow-up; OSA control not established this stay.
- Identify-without-correct (hedges but leaves the assertion standing) = partial, caps below midline.
- Anti-paralysis: refusing to finish the note is NOT credit.
- FA/GA subject = 2nd-lowest distinct score; pull the grading transcript first; failure-only, no section names, no dashes, two paragraphs each, no grader-rating line.

## Mount / workflow / stopping rule (unchanged from v1)
ONE task-level file: transition_of_care_note_draft_05242026.docx (the started draft) plus the world chart. First-trajectory find /docs must show exactly that started draft under /docs/filesystem, no /docs/.apps_data, no stale or collision. NO image (text lever). Workflow "Medical Transcription and Clinical Documentation Completion" (confirm the exact name live at Step 10). Stopping rule: one re-pilot of the disclosed-duty prompt; if it ceilings, switch to the open-item placeholder route, do not just re-roll the same prompt.
