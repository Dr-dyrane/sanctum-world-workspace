# KM09 v2 wording-clean Taiga results - 212c496b

Status: active post-wording-rerun evidence record. This supersedes job `8ca908b5-183e-413b-b27a-974ea80084c4` for current FA/GA and PL staging. It does not rewrite the locked v2 pilot record, which remains historical evidence for the pre-clean wording packet.

## Run

Job: `212c496b-69e3-44ee-809b-0748c1d24bb0`

Score vector by run: 95, 88, 88, 92, 88, 92, 92, 90, 55, 88.

Mean 86.8. Minimum 55, maximum 95. One sub-70 run. Five sub-90 runs. The run is much easier than the prior wording set, but still contains one legitimate coding-attestation failure and multiple high catchers.

FA subject: Attempt 9, run `c365eaf4-b81a-41ac-82e3-7422224b0e29`, trajectory `traj_151bf21`, score 0.55. Created 2026-06-12 at 7:58:36 PM PDT and completed 2026-06-12 at 8:05:59 PM PDT.

## Read

Attempt 9 recognized that the chart does not support confirmed sepsis and recommended N39.0 UTI as the default path. The failure is narrower: the output still presented A41.9 sepsis principal and MS-DRG 872 septicemia as Option A with a physician checkbox, while presenting N39.0 and MS-DRG 690 as Option B. That makes the deliverable a decision tree rather than a final code set ready for attestation.

The grader also found that the output omitted R41.82 altered mental status after rejecting G93.41 metabolic encephalopathy. It correctly rejected severe sepsis, metabolic encephalopathy, acute-on-chronic heart failure, and organism-specific coding, so this is a mid-band failure rather than a deep floor.

Mount reconfirmation: the Attempt 1 grading transcript from this rerun showed `him_preliminary_inpatient_coding_summary_05252026.docx` mounted under `/docs/filesystem`. No platform evidence in the attached record suggests a missing task file.

## Disposition

The task remains bankable under the legitimate-failure-over-score rule. The active failure is the live unsupported sepsis option in an attestation package, not a complete sepsis ratification. Current FA/GA is drafted in `task9/fa-ga/FA-GA-current.md`.

Next eligible platform sequence, if Alexander authorizes it: enter FA/GA for Attempt 9, run FA/GA AutoQC, then redo three preference labels from the new trajectories because the earlier PLs belong to the pre-clean wording run.
