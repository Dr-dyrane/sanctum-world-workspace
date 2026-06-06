# Task 1 Failure Analysis & Grader Analysis - FINAL (SUBMITTED)

STATUS (6/6): SUBMITTED on platform, batch v2, run aef58074. FA finding saved (Details = full text below; title/severity = physician metadata, polish optional). GA saved, rated GREAT. Only remaining platform action: Run Failure Analysis & Grader Analysis AutoQC. The calibration line (below) is an OPTIONAL physician enhancement, NOT a blocker; the GA is complete without it. This file is FINAL - do not treat as pending.

Date: 2026-06-06. Physician-authored (Alexander), chart-register voice, NO em dashes (project rule). Converged across working-Claude draft + independent claude.ai review + physician edit. Evidence basis: batch v2 (job 476e281a); grading transcripts for runs 564d568d (0.72) and aef58074 (0.78); local output greps in trajectories/low-runs/.

## Headline finding (the discriminator)
Score separation tracks plain medication-list completeness, NOT trap reasoning. All 10 runs handled the designed traps (prednisone provenance, cardio/nephro staging, buried OT/nursing evidence, inpatient-only separation, snapshot reconciliation). The two low runs (0.72, 0.78) silently dropped METFORMIN (a held diabetes agent the golden carries with its own restart line) from the 19-item list and both still wrote "eighteen of nineteen verified, prednisone the sole unverified item" without catching the miss. Verified in outputs: 564d568d (0.72) = 0 metformin mentions; 5037a531 (90s cluster) = 4 metformin + 4 gabapentin. 0.78 run also under-dispositioned gabapentin.

## Failure Analysis (submitted)
All ten runs handled the traps I built into this case. Even the two lowest, at 0.72 and 0.78, got the prednisone right (no made-up home dose, a non-abrupt bridge with the taper left to rheumatology), staged the cardiology and nephrology restart instead of picking a side, pulled the buried OT and nursing findings into a safety plan, kept the inpatient-only meds out of the home regimen, and treated the discharge snapshot as incomplete rather than copying it.

So the traps are not what separated the scores. What separated them was plain completeness across a 19-item list. Both low runs dropped metformin entirely, a held diabetes med that the golden carries with its own restart line, and both still wrote "eighteen of nineteen verified, prednisone the sole unverified item" without catching that one was missing. The higher-scoring runs included it. I checked the outputs directly: the 0.72 run never mentions metformin, while a 90s run covers both metformin and gabapentin. The score tracks medication coverage, not anything hidden in the reasoning.

The real failure mode here is a coverage and self-check miss on a long list, separate from the harder reasoning the case is built around. That is fine for an entry reconciliation task. The traps do not stump this model, but the task still tests something that matters clinically, and dropping a held med while claiming the list is complete is a useful signal. The model does the hard thinking well and then misses a routine medication and miscounts its own work.

## Grader Analysis (submitted) - Rating: Great
The grading is solid and it is catching something real. On both low runs the grader went into the chart, confirmed metformin is a verified home med held HD1 through HD6, saw it is in the golden as a held agent, saw it is missing from the answer, and even caught that the note claims eighteen of nineteen while leaving one out. Then it scored an otherwise strong note down for a real omission. That is a correct call, not the grader being harsh, and it caught something I missed on my own first read. It also treated the chart-sourced numbers like the creatinine and potassium trends as supported rather than made up, which is exactly what I want. The golden is not in the run container and nothing looks gamed.

Optional physician calibration line (Alexander's discretion, not required for submission): whether 0.72-0.78 is fair or slightly generous for fully omitting a held medication. If added: "If anything I would dock a full omission of a held medication harder, since that is the miss that actually reaches the patient, but the score is defensible."

## Lessons for Tasks 2-6 FA/GA
1. PULL THE GRADING TRANSCRIPTS for the low runs before writing GA. Do not infer the failure mode from the output alone (working-draft guessed 4 wrong failure modes; the real miss was metformin only). The transcript shows exactly what the grader docked.
2. Grep the low-run vs a high-run output for each golden-required medication/element to find the discriminator fast.
3. A "too easy" mean (no sub-70) is not automatically a weak task - check whether the SPREAD tracks a real clinical competency (here: medication coverage). If it does, the task discriminates and is worth keeping.
4. FA/GA is physician-authored, chart-register voice, NO em dashes (hyphens/periods only), first person where natural.
5. GA can legitimately rate the grader "Great" when it does independent primary-source verification and catches a real miss; affirming a correct grader IS the analysis, not only flagging errors.
