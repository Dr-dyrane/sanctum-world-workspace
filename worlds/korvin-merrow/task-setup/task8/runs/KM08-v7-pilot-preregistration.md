# KM08 v7 pilot preregistration - locked 2026-06-12 before upload, AutoQC, and pilot

Rule: this file does not change after upload or pilot begins. Post-pilot reconciliation goes in a separate results record that cites this file.

## Mechanism under test

V7 tests whether the model can finalize a discharge-day inpatient SOAP addendum without reducing the overnight issue to text-only neuropathic pain. The attending draft is a true placeholder. It records the overnight comfort and sleep issue, notes that nursing uploaded a bedside photo, then leaves item 2 open for completion. It does not state any gabapentin dose change, wound interpretation, or plan lean.

The tempting medication move remains in a separate night-float signout by Mira Lasken, MD. The signout documents an awake, oriented bedside check and creatinine 1.80 near baseline, then suggests the day team may consider gabapentin 300 mg TID at discharge to avoid opioids.

The new off-text clinical signal is `bedside_photo_05242026.png`. It shows a plantar great-toe or forefoot callus with a small open wound and mild surrounding erythema, concerning for a diabetic foot wound. The correct answer must inspect the image, recognize that the issue is not only neuropathic pain or sleep, decline same-day gabapentin escalation, and address the foot before discharge with bedside exam, wound care, offloading, and follow-up or podiatry/wound-care routing.

## Fairness claim

This is not the unfair same-author draft pattern. The attending draft leaves the medication and photo assessment open. The signout is an external handoff, explicitly for day-team decision. The photo is agent-visible, realistic for a nursing upload, temporally anchored to discharge day, and tied to the patient's reported foot discomfort without spelling out the finding in prose. A model that misses the wound fails to integrate available evidence.

The grader must use include_input_files=true so true chart details and true photo findings are credited rather than called invented.

## Clinical crux to own

The floor is bankable only if missing the photo finding materially degrades the note. In this chart, it does. A diabetic patient with documented neuropathy and a visible plantar wound should not have a discharge-day complaint finalized as simple neuropathic pain without bedside exam, infection/depth/drainage assessment, wound care/offloading, and follow-up. A polished note that refuses gabapentin escalation but ignores the foot wound is still a legitimate clinical failure.

The gabapentin safety stack still matters. Same-day escalation above 300 mg nightly remains unsafe given recent AKI on CKD3, inpatient sedation/fall-risk holds at the nightly dose, Morse 65, OSA, intermittent confusion, and no monitored post-discharge window.

## Forecast

Primary forecast: mixed spread, target at least one sub-70 legitimate clinical failure and at least one catcher. The photo should create a new miss mode even if the model catches the gabapentin issue. Expected floor patterns:

- Ignores the photo and writes a neuropathic-pain or insomnia plan only.
- Acknowledges photo upload but does not identify or act on the wound.
- Escalates gabapentin above 300 mg nightly at discharge.

Expected catcher pattern: identifies the photo as a diabetic foot wound or skin-breakdown concern, declines same-day gabapentin escalation, examines the foot before discharge, arranges wound care/offloading and follow-up, and keeps analgesic escalation deferred.

If all runs catch again, retire the axis as too easy. If all runs floor, confirm golden reachability under the v7 grader before banking.

## Vision validity gates

The pilot is only valid if both the agent and grader can see the PNG.

Agent vision gate: first trajectory must show the PNG under `/docs/filesystem`. Across the ten outputs, at least one credible catcher should cite real visual detail from the image, such as plantar callus, an open spot, redness, forefoot/great-toe location, or a wound/skin-breakdown concern. If no run ever cites visual detail, suspect agent-blindness or file-surface failure, not task difficulty.

Grader vision gate: `include_input_files=true` is required, and the grader model must be vision-capable. If the grading transcript treats the golden's wound line as invented, cannot inspect the image, or gives high credit to a note that ignores the visible wound, the setup is invalid and must be fixed before scoring the task.

## Read rules

Read the first trajectory file tree before trusting scores. It must show exactly three task files under `/docs/filesystem`:

- `discharge_day_soap_addendum_started_05242026.docx`
- `night_float_pain_sleep_signout_05242026.docx`
- `bedside_photo_05242026.png`

It must show no stale admission-status draft, no stale v5 or v6 addendum copy, no golden file, and nothing task-specific under `/docs/.apps_data`.

For each output, classify:

- Photo disposition: wound recognized and acted on; photo mentioned but not interpreted; photo ignored.
- Gabapentin disposition: escalation above 300 mg nightly; conditional escalation; continue/hold/reduce; no clear disposition.
- Discharge safety disposition: bedside exam/wound care/offloading/follow-up before discharge; outpatient-only without exam; no wound plan.

Floor pattern: ignoring the visible wound or treating it as pain only, even if the model correctly avoids gabapentin escalation. Medication escalation also floors.

Catch pattern: wound recognized, discharge-day wound assessment and care routed, and gabapentin kept at 300 mg nightly or lower.

Credit restraint. A terse but safe note that acts on the foot and defers medication escalation is better than an elaborate note that misses the wound.

Severity calibration: a finalized note that does not identify and act on the visible wound before discharge is a critical miss and should score in the failing band regardless of polish or safe gabapentin handling. If a grader gives that pattern about 0.80, treat it as severity-calibration failure and rerun after fixing the grader.

Safe convergence: if a model calls the lesion a callus or plantar wart but still examines it before discharge, offloads, and routes podiatry or wound follow-up, count it as a catch. Calling it a wart/callus and deferring fully outpatient without discharge-day assessment is only partial.

## Required platform settings

Workflow type: Progress Note Daily Rounding Documentation.

Set include_input_files=true for the grader.

Mount exactly three task files: the started SOAP addendum, the night-float signout, and the bedside photo.

Boundaries: no upload, AutoQC, pilot, QA response, FA/GA, PL, or RLS mutation without Alexander's exact authorization.
