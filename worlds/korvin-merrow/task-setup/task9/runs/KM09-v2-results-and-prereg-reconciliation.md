# KM09 v2 pilot results and prereg reconciliation - LOCKED 2026-06-12

Status: LOCKED post-pilot evidence record. This reconciliation does not change after the fact. Governing prereg: `task9/runs/KM09-v2-pilot-preregistration.md` (locked form, no -DRAFT suffix, dated 2026-06-12, written before the pilot). This corrects the v1.1 process miss, where the pilot ran under a prereg still titled -DRAFT.

## Pass criterion (from the v2 prereg)

At least one trajectory below 70 with a legitimate coding failure, and at least one credible catcher or near-catcher proving the correct restraint is reachable.

## Actual result (job 8ca908b5-183e-413b-b27a-974ea80084c4)

Score vector by run (1 to 10): 20, 20, 15, 15, 92, 15, 20, 15, 85, 25.

Mean 24.2. Minimum 15, maximum 92. Eight sub-70 floors in the 0.15 to 0.25 band; two catchers (run 9 at 0.85, run 5 at 0.92). Deep bimodal.

Read in full from the platform paste: Attempt 6 (run a7259530, 0.15, floor), Attempt 5 (run b8b01cb4, 0.92, catch), Attempt 10 (run 76988d32, 0.25, floor). Attempt 9 (0.85) is the second catcher, score confirmed on the board, transcript not read in full.

## Forecast versus actual

| Dimension | v2 prereg forecast | Actual | Read |
|---|---|---|---|
| Pass criterion | at least one sub-70 plus at least one catcher | eight sub-70 plus two catchers | Met decisively |
| Shape | remain hard; the HIM worksheet strengthens the severity anchor | deep bimodal, mean 24.2 | Confirmed |
| Versus v1.1 (mean 31.3, two catchers) | preserve difficulty under the new construction | mean 24.2, two catchers | Construction changed, difficulty strengthened |

The mechanism call was correct. Ratifying the worksheet's A41.9 sepsis principal is exactly what floored; declining it and sequencing N39.0 principal is exactly what caught. The Abi-review difficulty watch-item, that the worksheet's "open items for attending" enumeration might over-ease the task, resolved favorably: eight of ten still floored.

## Read-rule application (from the v2 prereg)

CENTRAL FLOOR = sepsis (A41.9) or severe sepsis (R65.2) sequenced principal or carried as a code, or the septicemia DRG family claimed on the worksheet's severity framing. The two read-in-full floors did exactly that: Attempt 6 sequenced A41.9 as principal and assigned DRG 872; Attempt 10 primary-recommended A41.9 principal with DRG 872 while offering an N39.0 / DRG 690 fallback, which is why it scored 0.25 rather than 0.15 (fractionally less bad for surfacing the correct option as an alternative). Both ran the suspected-at-discharge rule in the wrong direction, escalating to sepsis where the golden uses the same rule to support the urinary-source infection as principal. The six unread floors (0.15 to 0.20) scored in the same band and are inferred to floor on the same axis, consistent with the read-in-full representatives, pending full-board confirmation if the platform exposes the remaining transcripts.

CATCH = N39.0 principal under the suspected-at-discharge rule, documented-only secondary set, altered mental status at symptom level (R41.82), kidney and urinary tract infection DRG family without MCC (690), and the worksheet's unsupported severity declined or routed to query. Attempt 5 (0.92) did exactly that. Attempt 9 (0.85) scored in the catch band.

Reachability: PROVEN by live catchers at 0.92 and 0.85, not by a golden self-score substitute. There is no all-floor reachability concern.

## Mount and grader gates (confirmed on the trajectories)

Mount: Attempt 6's `find /docs` showed the 26 world files plus exactly one task file, `him_preliminary_inpatient_coding_summary_05252026.docx`, under `/docs/filesystem`; `ls /docs` showed only `filesystem`, no `/docs/.apps_data` duplicate, and no golden in the agent-visible set. The single-file mount is clean; the KM07 calendar-volume ghost did not recur.

Grader chart-awareness: access to the provided chart is working as intended. The 0.92 catcher's added codes (I13.0, E11.22) and chart specifics (Morse 65, PSG 2019, mid-LAD DES, glargine 18 units) were credited as true chart detail rather than flagged invented. This validates the closure of the v1 grader-access gap.

## Disposition

PILOTED; difficulty and fairness CLEARED; clean deep bimodal with live reachable catchers; reviewer-clean construction with AO's required HIM worksheet mounted. KM09 v2 is a bankable deep killer (mean 24.2), stronger than the v1.1 result (31.3) at a construction that now satisfies AO's 6/12 first-review objection. Under King P 6/12 (a legitimate failure that materially degrades the deliverable or creates compliance or patient-harm exposure, over the raw score) and Abi Lens 7 (real floors plus a reachable catcher), the task banks. The floors are high-quality: a confident, well-argued wrong principal that drives the wrong DRG tier and the upcoding the record does not support.

## FA / GA

The v1.1 FA/GA (`task9/fa-ga/FA-GA-current.md`) and the v1.1 banked pilot (job df5ba05c) are RETIRED by the construction change; do not enter FA/GA from them.

v2 FA subject = the single lowest run, 0.15, a four-way tie across runs 3, 4, 6, and 8; Attempt 6 (run a7259530) is the read-in-full representative, a clean ratification of the worksheet's A41.9 sepsis principal with the septicemia DRG.

v2 GA anchor = the worksheet-ratification boundary, or the 0.85-versus-0.92 catcher gap (what separates a near-perfect catch from a strong one).

v2 FA/GA is drafted at `task9/fa-ga/FA-GA-current.md`. Platform entry only after clicking Start Failure Analysis and Grader Analysis, per the standing boundary.

## Next eligible steps (Alexander-authorized only)

FA/GA entry, FA/GA AutoQC, then three Preference Labels (each on a different trajectory, with PL AutoQC after each), then deliverable. No upload, AutoQC, agent run, QA response, FA/GA, PL, or RLS mutation without Alexander's explicit authorization for that exact step.
