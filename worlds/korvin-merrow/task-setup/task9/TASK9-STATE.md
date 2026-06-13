# TASK9-STATE

## CURRENT (6/13 KM board export): READY FOR DELIVERY on platform. The current packet removes the amended-document ambiguity and keeps the task framed as physician review of the HIM preliminary inpatient coding summary for final attestation. New Taiga job `212c496b-69e3-44ee-809b-0748c1d24bb0` scored 95, 88, 88, 92, 88, 92, 92, 90, 55, 88, mean 86.8. The selected FA/GA subject is the single lowest run: Attempt 9, run `c365eaf4-b81a-41ac-82e3-7422224b0e29`, trajectory `traj_151bf21`, score 0.55. The failure is narrower than the old 0.15 floor: the model recommends N39.0 UTI by default but still leaves A41.9 sepsis principal and MS-DRG 872 as a signable Option A, and it omits R41.82 altered mental status. FA/GA and the three post-rerun PLs are complete on the platform path. Prior Taiga job `8ca908b5-183e-413b-b27a-974ea80084c4` and its three local PL backups remain historical pre-wording-clean evidence.

Active local v2 files in `platform/task9/current/`:
- `prompt-task9-v2.txt`
- `him_preliminary_inpatient_coding_summary_05252026.docx`
- `golden-KM09-v2.docx`
- `grader-guidelines-task9-v2.txt`
- `RUN-INSTRUCTIONS-v2.md`

Design stance: keep the v1.1 central clinical axis. The correct physician attestation sequences `N39.0` urinary tract infection as principal, does not attest `A41.9` sepsis or `R65.2` severe sepsis, codes altered mental status only at symptom level, and rejects metabolic encephalopathy, acute-on-chronic systolic heart failure, organism-specific codes, and malnutrition as undocumented. The worksheet deliberately carries the severity-forward HIM framing so the model must refute unsupported coding, not merely fill a blank.

Pilot result after wording clean: v2 remains a clean reseed candidate but is now much easier. Job `212c496b` has one sub-70 run and nine high runs, proving reachability. The selected low run, Attempt 9, read the chart well enough to reject severe sepsis, metabolic encephalopathy, acute-on-chronic heart failure, and organism coding. It still failed the final attestation task by leaving the unsupported sepsis principal and septicemia DRG as a checkbox option instead of removing that pathway.

FA/GA and PL status after 6/13 wording fix: `fa-ga/FA-GA-current.md` is the local record for Attempt 9 from job `212c496b`. It follows the current Abi rule: one trajectory, failure-only prose, no grader-section names, and under about 1000 characters per field. The three post-rerun PL recommendations completed in sequence were A+, B+, and A++.

Build verification completed locally 6/12 and wording-clean patch rebuilt 6/13: Mode A clone from approved Epic UI artifacts, python-docx extraction including tables, core metadata scrubbed, styles.xml byte-identical to the base, fills and borders identical, no em dash, no en dash, no arrow in the v2 prompt/grader/run instructions/builder/generated DOCX text, no amended-document wording in the active prompt, grader, worksheet, or golden, and Quick Look rendered the worksheet and golden as one clean page each. The `Ilyana Rook` HIM author name does not collide with existing world or task files outside this v2 packet.

Studio mount gate: PASSED on v2 job `8ca908b5` and reconfirmed on wording-clean job `212c496b`. The earlier first trajectory `find /docs` showed exactly one Task 9 task file under `/docs/filesystem`, `him_preliminary_inpatient_coding_summary_05252026.docx`, with no task-specific `.apps_data` copy and no golden in the agent-visible set. The new Attempt 1 grading transcript again showed the HIM summary mounted under `/docs/filesystem`.

Abi-mode byte review 6/12: PASS with no blocking findings, recorded at `qa/KM09-v2-abi-mode-review-2026-06-12.md`. The v2 preregistration is locked pre-pilot at `runs/KM09-v2-pilot-preregistration.md` and must not be edited after the pilot starts. The v2 result record is `runs/KM09-v2-results-and-prereg-reconciliation.md`. v1.1 FA/GA and job `df5ba05c` are retired for submission purposes and remain difficulty evidence only.

[RECOVERY NOTE 6/10 late: this file, prompt-task9-v1.txt, grader-guidelines-task9-v1.txt, and the RUN-INSTRUCTIONS floor rules were truncated by an interrupted write during the v1.1 re-center pass; repaired 6/10 from the v1.0 parallel structure + v1.1 staged content. Grader final two blocks and this tail are reconstructions - Alexander's read-and-own pass must cover them verbatim. PREREG GAP FOUND AT AUDIT: runs/KM09-v1-pilot-preregistration.md preregisters the v1.0 MCC-central design and its read rules contradict v1.1 (it exempts simple-sepsis from flooring). v1.1 supersession draft staged at runs/KM09-v1.1-pilot-preregistration-DRAFT.md - Alexander must review and lock it BEFORE upload; v1 file kept unedited per the lock rule.]

Boundaries: no delivery action, submission, additional platform mutation, or RL Studio action from the repo side without explicit Alexander authorization for that exact step.
