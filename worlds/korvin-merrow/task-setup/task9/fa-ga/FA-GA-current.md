# KM09 v2 FA/GA - wording-clean rerun 212c496b

Status 2026-06-13: paste-ready local draft for the wording-clean Taiga rerun, based on the single lowest trajectory. Job `212c496b-69e3-44ee-809b-0748c1d24bb0` scored 95, 88, 88, 92, 88, 92, 92, 90, 55, 88. Mean 86.8. FA subject: Attempt 9, run `c365eaf4-b81a-41ac-82e3-7422224b0e29`, trajectory `traj_151bf21`, score 0.55, completed 2026-06-12 at 8:05:59 PM PDT. Recommended grader rating: Great.

Guidance applied: one trajectory only, failure-only prose, no grader-section names, no bullets in the submitted fields, and each field under about 1000 characters.

## Failure Analysis

On trajectory 9, the model left an unsupported A41.9 sepsis principal and MS-DRG 872 septicemia signable inside a final attestation packet, offered as a physician-selectable Option A against N39.0 UTI with MS-DRG 690 as Option B. Even though it labeled the UTI path the default, keeping the sepsis pathway available for signature rather than removing it preserves the worksheet's central upcoding risk and leaves the deliverable non-final.

The output also omitted R41.82 altered mental status after correctly rejecting G93.41 metabolic encephalopathy, leaving the documented altered mental status uncoded at symptom level. Its hedged, decision-tree structure forces the physician to adjudicate a sepsis option the golden requires the answer to decline.

## Grader Analysis

The grader scored this well against the golden, and the score supports a Great rating. It credited the model's correct rejections of severe sepsis, metabolic encephalopathy, acute-on-chronic heart failure, and organism-specific coding, and it identified the central defect, a physician-selectable A41.9 principal and MS-DRG 872 option left signable inside a final attestation packet. It also caught the omitted R41.82 altered mental status as a secondary miss.

The one weakness is phrasing. The grader called the sepsis and UTI paths equally valid, when the output labeled N39.0 UTI the recommended default, which slightly overstates the hedge. A deep floor would overstate the error since sepsis was not the sole recommendation, and a high score would miss that the deliverable stayed non-final with the sepsis DRG still signable, so the mid-band 0.55 is well placed.
