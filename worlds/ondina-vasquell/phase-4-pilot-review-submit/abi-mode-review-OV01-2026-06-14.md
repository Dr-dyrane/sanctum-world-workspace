# Abi-mode review: OV01 v2 packet (de-telegraphed) - 2026-06-14

Scope, in cold-read order: prompt-OV01.txt -> task_data.py T1 (the mounted order set, read on the built bytes) -> OV01-v2-pilot-preregistration.md -> build_goldens.py OV01 golden -> OV01_GRADER. Reviewer posture: read cold before opening golden/grader: yes.
Verdict: SEND BACK (one de-telegraph residual) + difficulty UNPROVEN (re-pilot required).

## Findings (blocking)

1. [Lens 1a / 5 - built-artifact + structural realism] The filename telegraphs what the content de-telegraph removed.
The agent-visible path is `/docs/filesystem/preliminary_discharge_order_set_05212026.docx`. We scrubbed the loud strings from the body (DRAFT, NOT RECONCILED, carried-forward) but "preliminary" in the filename re-advertises that this is a draft to audit. Lens 1a is explicit that filenames (clean, fixed, reviewer, v4_clean, and by the same logic preliminary/unreconciled) can pre-answer the trap. A careful model lists the mount and reads the path before the body.
Forward rule: de-telegraph filenames, not just content. Rename to `discharge_medication_orders_05212026.docx`. Cascade: task_data.py T1 filename, TASK_FILE_MAP["task1"], the golden source line, the platform copy, and remove the old-named artifact from git. The approved spec file-plan still lists the old name; that becomes a task-layer divergence (acceptable per KM precedent that shipped tasks diverge from spec), reconcile only if the spec is resubmitted.

## Findings (resolved this pass)

2. [Lens 8 - alignment after change] The golden's SOURCES REVIEWED line still called it "the preliminary unreconciled discharge order set," contradicting the de-telegraphed surface. Hidden from the model (golden is grader-only) so it did not telegraph, but it was a stale post-change reference. FIXED: changed to "the discharge medication order set pending signature."

## Difficulty (Lens 7) - UNPROVEN, high ceiling risk

v1 ceilinged (mean ~92, zero sub-70; sent back by this lens). v2 adds the cold enoxaparin-VTE-prophylaxis propagation trap, de-telegraphed surface. But the prompt is a row-level disposition ("sign / change / stop each, with a why") - a reconcile-and-correct posture, and the Abi doctrine records that a reconcile-and-correct clause is a difficulty-killer (KM06 v4 -> ~0.98). A med-rec is already an inherently reconcile-everything genre (KM01 = 89, soft). So a strong model dispositioning every row is likely to catch the enoxaparin too. The cold trap is the right mechanism and the best available bet, but a ceiling on re-pilot would not be surprising.
Reachability: golden discontinues enoxaparin and engages the chart -> catcher reachable; if it floors it will be bimodal.
Status: cannot mark difficulty PASS until the re-pilot shows a real propagation floor (>=1 sub-70 with the legitimate continued-prophylaxis failure). Standing rule holds: if it still all-catches, retire OV01 as the first floor probe and pilot OV07 (colder source geometry); do NOT tighten the grader.

## Fairness (Lens 1 / 1a) - PASS

The order set is an external pending-signature document, not a same-author finalize-only draft, and the prompt licenses correction (sign / change / stop). So flooring on "continue enoxaparin" or "resume the held agents" is the model's own fault, not a planted-lie gotcha. Built-bytes quotes of the scored items:
- enoxaparin row, verbatim: `Enoxaparin | 40 mg Subcutaneous daily | Continue until mobility returns to baseline`
- held agents, verbatim: `Metformin / Empagliflozin / Lisinopril | ... | Resume`
These are external orders proposing wrong actions, fair to rebut from the chart. No telegraph strings present (draft / not reconciled / carried forward / pending reconciliation all = 0).

## Other lenses

- Lens 2 genre purpose: PASS. A discharge order set pending signature is a real instrument; the golden's dispositions fit it.
- Lens 3 answer-the-question: PASS. Golden gives a per-row why and the patient instructions the prompt asked for.
- Lens 4 voice anchor: PASS. Golden speaks as the hospitalist attending (Lillian Everet) on her own patient, citing her own team's chart.
- Lens 6 answer-giving scaffolding: PASS. The order set proposes the wrong actions; no mounted file teaches "stop enoxaparin." Not inflated.
- Lens 9 mechanism + self-standing records: PASS. Grader described as scoring output against golden+guidelines with chart access; FA/GA not yet drafted (post-pilot).

## Mechanical pass

- dates: PASS. Order set 05/21/2026 1830 and golden 05/22/2026 0830 are after the 05/21 18:00 snapshot; no future dates.
- banned chars: PASS (verify_ondina gate green; no em/en dash/arrows).
- fingerprints / metadata: PASS (gate green, scrub_all_metadata + make_deterministic).
- prompt-to-file refs: PASS (prompt names no files).
- workflow string: PASS pending live confirmation = "Medication Reconciliation at Care Transitions" (WORKFLOW map); confirm at Step 10.
- grader chart access: PASS = chart-aware (include_input_files true) for the synthesis task; expect/justify the Self-Contained Guidelines flag.
- names: PASS (no new-to-world names introduced).
- prereg: PASS (OV01 v2 prereg locked; not edited).
- mount hygiene: DEFERRED to first re-pilot trajectory = run `find /docs -type f`, confirm one task file, no `.apps_data/calendar` duplicate, no extra volume, and (after rename) no `preliminary` in the path.

## Reachability status

Catcher: golden discontinues enoxaparin and is correct on the warm axes -> reachable. Golden self-score under its own grader: not yet run for v2; do it as the reachability anchor before banking. Open items: rename (finding 1) decision; re-pilot for the propagation floor; mount-hygiene gate on the first trajectory.
