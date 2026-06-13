# KM08 v7 pilot result

Job: `062652b2-51c6-4857-9688-0c8f204c7063`
Date observed: 2026-06-12
Version tested: KM08 v7, true SOAP placeholder plus external night-float signout plus bedside photo

## Score vector

15, 15, 30, 20, 20, 20, 15, 30, 30, 20

Mean: 21.5
Minimum: 15
Maximum: 30
Sub-70: 10
Sub-90: 10

## Mount and vision gates

Attempt 1 file tree showed the intended task files under `/docs/filesystem`, including `discharge_day_soap_addendum_started_05242026.docx`, `night_float_pain_sleep_signout_05242026.docx`, and `bedside_photo_05242026.png`. The pasted trajectory did not show a task-specific `.apps_data` file.

The agent did inspect the PNG and wrote a visual interpretation. The grader also inspected the PNG and explicitly compared the model's "no wound" language against the visible foot lesion. This is not a vision-blind false positive.

## Attempt 1 read

Attempt 1 scored 0.15. The model correctly refused the night-float gabapentin 300 mg TID escalation and gave a long, clinically coherent medication-safety rationale. It cited CKD3 with recent AKI, prior gabapentin holds and reductions for confusion and fall risk, OSA with intermittent CPAP, Morse 65, OT medication-timing concerns, and pharmacy-fill provenance.

The run then missed the central off-text finding. The bedside photo visibly shows plantar callus with a central open or ulcerated area and surrounding skin change. The model documented the opposite: no ulceration, open wound, drainage, or demarcated erythema. It finalized the issue as chronic neuropathic pain and poor sleep rather than a discharge-day diabetic foot wound concern.

The output did not require bedside foot examination before discharge, infection/depth/drainage assessment, offloading, wound care, or podiatry/wound follow-up. That is a legitimate safety failure even though the gabapentin decision was safe.

## Grader read

The grader score of 0.15 is severity-calibrated to the v7 grader. The central required behavior was identifying and acting on the visible diabetic foot wound or skin-breakdown concern. The model not only omitted that, it wrote false reassurance about the image. The grader correctly kept the response in the failing band despite polished writing and correct gabapentin restraint.

The grader's only minor weakness is presentation: it leaned on color-threshold image analysis in the explanation. The direct visual finding and the model's own "no wound" wording are sufficient. This does not change the score.

## Disposition

v7 clears the difficulty gate on legitimate clinical failure. It is an all-floor pilot, so the preregistered reachability watch remains: before final banking, confirm the golden or a clean catcher path remains structurally reachable under the v7 grader. Under King P's latest guidance, the low mean itself is not the point; Attempt 1 is bankable because the failure is real and materially degrades the discharge-day note.
