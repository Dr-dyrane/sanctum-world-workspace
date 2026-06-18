# KM tasking-stage playbook (for OV tasking) - 2026-06-14

> Voice: FA/GA and preference labels follow the Dr. Alexander standard in `docs/alexander-voice-dna.md` - state what was missed, why it mattered, the consequence; no process narration. Enforced by `tools/verify/verify_voice.py`.

Distilled from the Korvin Merrow task-setup tree (TASK-RUNBOOK, TASKn-STATE, runs/, fa-ga/, preference-labeling/, qa/, reviews/, performance report). This is the operational flow AFTER a package is built. Apply task-by-task as OV enters tasking. Reflects the King P 2026-06-14 office-hours updates.

## 1. End-to-end sequence + gates
Step 10 entry -> Task AutoQC -> Trajectories (10) + Taiga QA -> Trajectory AutoQC + Taiga QA Feedback -> FA/GA -> 3 Preference Labels -> reviewer round -> delivery.
- Step 10 entry: paste prompt; upload task file and click the SEPARATE "Save File Changes" (not just top Save); upload golden as a file; paste grader; Save; refresh; confirm all four survive untruncated and the task file shows UPLOADED (not staged). Mount gate on first trajectory: `find /docs` = one task file under /docs/filesystem, nothing under /docs/.apps_data, no name collision with a world file (blank trajectories otherwise).
- Task AutoQC: rerun only N failing, never full reruns. Expected justifiable residuals on synthesis tasks: "Self-Contained Guidelines" when the grader needs the provided chart, and sometimes "No Weight Distribution" for clinical-severity language. Justify with the exact flagged text; never flatten the grader to chase a clean board.
- Trajectories: 10 completed with scores; read by mechanism, not score. GATE (legitimate-failure, King P 6/12): at least one trajectory shows a defensible critical/material failure. No numeric <70/<60 requirement; do not bank a cosmetic/unfair miss.
- Taiga QA / EnvLinter: respond to EVERY flag with a fact-referenced rebuttal (cite job id + per-run scores); never a bare "tech issue"/"known issue"/"reviewer said ok" (KM07 6/11). For QC/Taiga errors, first decide whether the writer can fix the task. If not, route to `taiga-envlinter-autoqc-clarifications`. Use `#sanctumhelp` for account/general help and `sanctum-rls-tech-issues` for RLS tech issues not related to Taiga or AutoQC.
- FA/GA: see section 3.
- Preference Labels: see section 2.
- Reviewer round + delivery: section 4. Nothing advances without explicit reviewer APPROVAL and Alexander's authorization for the exact next step.

## 2. Preference labels (3 per task)
- THREE PLs, each a DIFFERENT trajectory (three separate A-vs-B pairs), since the 6/7 pod update (KM01/02 predate it at 1 PL).
- Read BOTH responses end to end vs the golden; never decide from score.
- Seven sections: Preferred output, Justification, Prompt adherence, Correctness, Completeness, Methodology, Quality/clarity, Summary. Natural clinical prose, varied structure across the three (avoid AI-prose tells; Abi 6/7 flagged 3+ patterns).
- Verdict tiers: A1/B1 slightly better, A2/B2 better, A3/B3 much better. Use the matching platform button: plain, one plus, or two plus. Do not use A4/B4 or three-plus language unless new pod guidance restores it. Tier must match the gap: if both handle the central item and differ only in clarity or one detail, it is A1/B1, not A2/B2.

## 3. FA/GA (UPDATED King P 2026-06-14; Larry E 2026-06-18)
- SUBJECT = the 2nd-LOWEST % trajectory, NOT the lowest (the lowest is often the noisy outlier). It must still be a legitimate material failure; if the 2nd-lowest is cosmetic/noise, record rationale and pick the nearest legitimate failure with Alexander. (DO-NOT-REPEAT #20.)
- If Taiga trajectories and QA are rerun, the old FA/GA is stale. Redo FA/GA from the latest valid run set.
- PULL THE GRADING TRANSCRIPT for that run before writing (KM01: inferring from output alone produced 4 wrong failure modes; the real miss was a silent metformin omission).
- Studio binds the FA/GA text box to the selected run. Select the subject run first, then verify the visible or downloaded output. If the selected run has no visible answer, write the FA/GA on that missing deliverable rather than borrowing another run.
- FA = failure-only, what the model did poorly. It includes Alexander's own score, not the trajectory score, and ends with `Overall Failure Score: X.XX / 1.0`. GA audits how the grader scored that run: what it identified correctly, what it missed, what it mis-scored, and whether calibration holds. No praise paragraph, no grader-section names (state the content), two paragraphs each, ~<=1000 chars, physician voice, NO em/en dashes.
- Recommended grader rating (Great/Good/etc.) goes only in the Studio field, never in the FA/GA file. Larry's guidance says FA/GA cannot be AI-authored; Codex can organize evidence, but Alexander must own final paste text.

## 4. Reviewer patterns (who sends back what)
- Abi O (pod lead, structural realism + fairness): task files too answer-giving, golden missing chart chrome, FA/GA scope/format, mechanism claims in GA, and the draft-fairness gate (planted claim needs a true placeholder OR an error-correction prompt). Send-back usually local rework, often no re-pilot.
- Sang N (grader discipline): rebuild grader to the five-block, golden in human physician voice, trim verbose prompts. Re-pilot (spread can change).
- Janette S (clinical realism): med interactions, discharge appropriateness, workflow/role realism. Approves on substance.
- Rahul Pai (synthesis/care-coordination): consultant integration, ownership per item.
- Fred M (specialist letters/coding): deliverable fit-for-workflow.
- King P (equity/fairness + bank decisions): the legitimate-failure-over-score rulings.
- Send-back classes: STRUCTURAL (local, no re-pilot) | MECHANISM (rebuild grader/golden, re-pilot) | FAIRNESS (reseed design, re-pilot) | CONTENT (clinical fix, re-pilot).

## 5. Bank vs reshape
- BANK when: >=1 legitimate material failure in a trajectory (now read on the 2nd-lowest); fairness gates pass (true placeholder or correct-errors prompt for same-author drafts; external-query genre is fair on its own); grader is symmetric (catch high, floor low) OR reachability is otherwise defensible.
- A catcher is NOT required (King P 6/12): an all-floor task is bankable if the failure is legitimate and the construction is fair (KM08 v7 photo-miss, KM10 v3 over-documented dx). Do not reseed just for all-floor.
- RESHAPE when: fairness gate fails; no legitimate failure (all >=90 or only cosmetic); reachability unproven AND golden validity contested; mechanism contradiction.
- External-vs-planted fairness (A0.6): finishing a same-author draft under a finalize-only prompt with a planted false line is UNFAIR (needs placeholder or correct-errors); responding to an EXTERNAL query/worksheet with an unsupported option is FAIR (decline it) - the genre carries the fairness.

## 6. Net-new gotchas (not already obvious in DO-NOT-REPEAT, beyond #16/#18/#19/#20)
- Reachability (can the model do it right) is separate from fairness (is the trap justified). Don't conflate; don't reseed an all-floor that is fair + legitimate.
- On any framing change (date/anchor/prompt rewrite), re-audit ALL surviving surfaces, not just golden + task file: grader Register Note, RUN-INSTRUCTIONS workflow line, prereg forecast/read-rules, README/state log, dated filenames.
- If a variance flag (No Weight Distribution / Self-Contained) fired before a grader rewrite, rerun N on the new version to confirm it clears - do not assume.
