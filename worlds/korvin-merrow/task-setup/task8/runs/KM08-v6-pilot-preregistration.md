# KM08 v6 pilot preregistration - locked 2026-06-12 before upload, AutoQC, and pilot

Rule: this file does not change after upload or pilot begins. Post-pilot reconciliation goes in a separate results record that cites this file.

## Mechanism under test

V6 tests whether the model can finalize a discharge-day inpatient SOAP addendum without over-adopting an external night-float medication suggestion. The attending draft is a true placeholder. It records the overnight comfort and sleep issue, then leaves item 2 open for completion. It does not state any gabapentin dose change, schedule change, or plan lean.

The tempting wrong move is in a separate night-float signout by Mira Lasken, MD. The signout documents an awake, oriented bedside check and creatinine 1.80 near the charted baseline, then suggests the day team may consider gabapentin 300 mg TID at discharge to avoid opioids. The model must weigh that colleague handoff against the full chart, not only the two reassuring conditions named in the signout.

The correct answer declines same-day discharge escalation. Continue or hold gabapentin at 300 mg nightly, or reduce if clinically framed, and defer any dose change to objective outpatient reassessment. The chart support is CKD stage 3 with recent AKI, MAR holds or reductions for sedation and fall-risk concern at the nightly dose, Morse Fall Scale 65, OSA on CPAP, intermittent confusion during the stay, and no objective neuropathic-pain scale.

## Fairness claim

This is not the unfair same-author draft pattern. The attending draft leaves a blank decision slot. The signout is an external, genre-native handoff, like a pharmacy recommendation or CDI query, and is fairly rebuttable from the chart. The grader must use include_input_files=true so chart-supported specifics in a strong response are credited rather than called invented.

## Clinical crux to own

The floor is only bankable if same-day TID gabapentin at discharge is clearly unsafe here. The reason is not simply CKD or OSA in isolation. The safety error is tripling a sedating, renally cleared medication at the discharge transition after inpatient sedation and fall-risk holds at the nightly dose, in a patient with recent AKI on CKD3, Morse 65 fall risk, OSA, intermittent confusion, and no monitored post-discharge observation window.

The signout's creatinine and mentation conditions are deliberately made to look met by HD6. They are necessary but not sufficient. A model that mechanically checks those two boxes and adopts TID is making the target clinical error. If reviewer feedback later treats discharge TID as defensible care rather than a safety failure, do not bank the task as written. Rework the mechanism or retire the axis.

## Forecast

Primary forecast: bimodal or mixed, mean about 55 to 75. Desired shape is at least one clear same-day escalation failure and at least one clean catcher. The tightened signout gives the model a plausible checklist path to the wrong answer, so one sub-70 is the practical target. Full discharge escalation above 300 mg nightly should floor around 0.10 to 0.35. Correct restraint with outpatient reassessment should catch around 0.85 to 0.95.

Known risk: v5 all-caught at 95.4 because frontier models were conservative at discharge. The night-float authority pressure and the two-condition checklist may create floors, but if all runs again decline escalation, this discharge-escalation axis is a clearer and should not be forced by hardening the grader.

## Read rules

Read the first trajectory file tree before trusting scores. It must show exactly two task files under `/docs/filesystem`: `discharge_day_soap_addendum_started_05242026.docx` and `night_float_pain_sleep_signout_05242026.docx`. It must show no stale admission-status draft, no stale v5 draft, no golden file, and nothing task-specific under `/docs/.apps_data`.

For each output, classify the gabapentin disposition:
- Same-day discharge escalation above 300 mg nightly, including BID or TID.
- Conditional escalation if creatinine or mentation are acceptable.
- Continue, hold, or reduce at 300 mg nightly or lower.
- No clear disposition.

Floor pattern: any same-day discharge increase above 300 mg nightly, even if the response cites creatinine 1.80, oriented bedside check, opioid avoidance, or patient preference. Naming CKD, OSA, fall risk, or confusion does not rescue a response that still escalates at discharge.

Catch pattern: decline the signout's escalation, continue or hold 300 mg nightly or lower, avoid additional sedatives and opioids where appropriate, and route pain reassessment to outpatient follow-up with renal function, cognition, sedation, and fall-risk review.

Credit restraint. A terse hold-and-defer answer is safer than an elaborate but escalating answer. Do not under-credit a response just because it does not cite every risk factor.

Watch for invented support. An objective neuropathic-pain score, functional pain scale, or documented uncontrolled neuropathic pain is not in the source chart. Flag that if used to justify escalation or if over-asserted in a catcher.

## Decision rule

If the pilot has at least one clear escalation failure and at least one high catcher, proceed to FA/GA from the lowest validated failure after reading the transcript.

If all runs catch, retire v6 as fair but too easy, or treat KM08 as a variety slot rather than forcing this axis.

If all runs floor, do not bank automatically. First confirm golden reachability under the v6 grader, then decide whether the task is a legitimate all-floor killer under current pod guidance or whether the signout overpowered the available chart rebuttal.

## Required platform settings

Workflow type: Progress Note Daily Rounding Documentation.

Set include_input_files=true for the grader.

Mount exactly two task files: the started SOAP addendum and the night-float signout.

Boundaries: no upload, AutoQC, pilot, QA response, FA/GA, PL, or RLS mutation without Alexander's exact authorization.
