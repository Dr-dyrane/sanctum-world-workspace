# The Korvin Merrow Story - how this world was built and how we got here

One readable end-to-end account of the Korvin Merrow world: the build, Task 1's three rounds, the mistakes and how each was caught, and what changed because of them. It connects the subdocs scattered across the repo; each section points to the canonical source for detail. Written 6/6/2026, after Task 1 cleared final review.

Canonical sources this narrative ties together:
- World build: `docs/claude-transcript-formatted.md` (construction transcript), `README.md` (lifecycle map), the `*/locked/` + `*/ratifications/` trail.
- Task 1: `task-setup/task1-lifecycle-log.md` (blow-by-blow + day retrospective), `task-setup/reviews/task1-first|second|final-human-review-*.md`.
- Lessons: `docs/reasoning-discipline.md`, `docs/clinical-voice-lessons.md`, `docs/docx-generation-method.md`, `docs/world-pipeline-playbook.md`, `task-setup/TASK-RUNBOOK.md`, `task-setup/CHECKPOINT-AUDIT-pre-task2.md`.

---

## 0. What this is

Project Sanctum builds clinical-reasoning evaluation tasks for reinforcement learning: a synthetic patient "world" (a full inpatient chart), and tasks that ask an AI agent to do real physician work against that chart, scored by an agentic grader against a physician-authored golden answer. The job of a task is to make a strong model fail in a way a senior physician would recognize as a genuine clinical error. Alexander (Internal Medicine) is the physician-author. Claude helps organize, draft structure, review, and stress-test when authorized; it does not replace Alexander's clinical authorship. Abimbola (Abi), the pod lead, reviews.

The world is Korvin Merrow: a 62-year-old man admitted for a suspected urinary-source infection with sepsis physiology, on a background of HFrEF, CAD with a remote stent, CKD stage 3, type 2 diabetes, and polymyalgia rheumatica on chronic prednisone of unverified dose. He is medically improving but not back to baseline, and his discharge is the setting for six tasks.

---

## 1. The build (Phases 1 to 4)

Detail: `docs/claude-transcript-formatted.md`, `README.md`, `active/brainstorm.md`.

The world began as a brainstorm. The design fixed Korvin's comorbidity stack and, more importantly, five world-level traps that every task would draw on: a steroid source-of-truth trap (no verifiable home prednisone dose anywhere), an HF-AKI medication-reconciliation trap (cardiorenal agents held during AKI, consultants speaking at different timestamps), a buried functional and cognitive decline trap (physician notes say stable, nursing and therapy say not), a sepsis-anchoring trap (day-1 framing versus day-7 reality), and a discharge-snapshot source-hierarchy trap (a reassuring summary that is not the full truth). Six task ideas were sketched on top, each with its own task-level discriminator.

The preparation layer was not ceremony. Calendar, baseline anchors, clinical-story timeline, task architecture, medication expansion, comorbidity expansion, provider roster, surgical history, and daily hospital course were each built and locked before the spec. Those layers prevented later drift: the prednisone hierarchy stayed intact, the HF/AKI restart conflict stayed time-sensitive, Trap #3 (buried functional/cognitive evidence) stayed distinct from Trap #5 (reassuring but incomplete discharge-facing artifact), and the discharge-safety target stayed primary.

The world spec turned the brainstorm into a full specification, then into a file ecosystem: 22 world chart files, 7 task-context files, and 4 supplementary references, each authored, validated, and locked through a deliberately heavy lifecycle of architecture documents, construction packages, validation reviews, and physician ratifications. The same discipline produced the internal task layer: prompts (TP-KM01 to 06), expected outputs (EO), golden responses (Golden-KM01 to 06), and grader guidance (GG), all locked.

That internal lock mattered, but Task 1 later proved it was not the same thing as platform-ready. Locked architecture gave us canon, coverage, and safety boundaries. RL Studio still required natural clinical prompts, realistic chart-format goldens, native grader-guideline structure, and platform-specific FA/GA/PL formatting.

The World Spec itself had its own painful lesson: content quality and document quality are separate problems. The approved submission had to be regenerated inside the official `World_Spec_Template_05_06.docx`, preserving styles, numbering, theme, section order, table styling, fonts, colors, spacing, and visual hierarchy. The method that survived is now `docs/docx-generation-method.md`: recon the target first, build through the document object model, use content-based locators rather than positional guesses, run integrity gates after every save, render to PDF/PNG, visually inspect, and numerically diff until the artifact converges. Driven by measurements, the DOCX converged; driven by taste, it did not.

Stacey's World Spec review closed the onboarding arc. The final Spec AutoQC board was 108/109, with prednisone dose/frequency as the sole intentional note-justified flag. That flag was accepted as designed because the uncertain prednisone dose is the central source-of-truth trap, not a missing medication value.

Engineering's pipeline then generated the synthetic chart from the spec. Reviewing that output taught a lesson that shaped everything after: the rewrite engine, in polishing the clinical voice, tended to perform the task's own synthesis on the trap carriers, a consult note that enumerated its restart-gating parameters, a progress note that declared the buried findings central. Polished clinical voice loves to weigh and conclude, which is exactly what kills a trap. The rule we wrote (`docs/clinical-voice-lessons.md`): trap carriers get the plainest prose in the world; never let a document do the weighting the task is meant to test.

Step 9 file review included a messy but important operational layer: duplicate platform controls, quota/outage behavior, generated-file drift, source/tool/origin semantics, and a large finding-triage pass that separated real content defects from platform mechanics. The final file review cleared 78 of 78. The repo retained the complete 33-file ecosystem, but the live RL Studio world was created with the 26-file world upload set. The 7 task-context files were held back or used at the task layer by design. That distinction matters: 33 files are repository canon; 26 files were synced into the live world. The world went live as Healthcare_247_Merrow.

---

## 2. Task 1, round by round

Detail: `task-setup/task1-lifecycle-log.md`, the three review records in `task-setup/reviews/`.

Task 1 (TP-KM01) is a discharge medication reconciliation and medication-safety review. It took three human-review rounds.

Round 1 (Abi, first review). The task shipped with two task files, a request memo and a pharmacy handoff. Abi sent it back: the files leaked the answer (they enumerated the solution step by step), they were dated 05/24 when the task was 05/23, they carried "Date / Anchor" project artifacts, the golden was body-only prose rather than a real chart document, and the FA/GA analyzed two runs instead of one and made claims about the grader's mechanism. The correction was deeper than formatting. A task file must feel like a plausible chart artifact, not an instruction sheet to the model. We deleted the files, rebuilt the golden as a full chart document with patient identifiers, date, hospital context, and signature lines, and reformatted the analyses.

Abi also corrected our grader mental model: the grader does not independently "go into the chart" in the way we had described. It grades the model's output against the golden response and grader guidance. The safe doctrine is mechanism-agnostic: write grader guidance that rewards chart-grounded physician reasoning without making claims about hidden grader access.

Round 2 (Abi, second review). With the leaking files gone, the model scored at or above 90 on all ten runs. Too easy, no significant clinical failure. This was the key realization: removing the files had removed the leakage AND the difficulty, which are different axes. Abi's bar to clear: a significant clinical failure and at least one trajectory under 90, ideally under 70. She suggested re-adding the handoff with a trap.

The hardening loop. This is the part that cost the day, and most of the cost was learning. We built and retired a spironolactone "premature restart" trap because the chart already coaches against it (a chart-coached wrong recommendation is not a trap). We introduced an ARNI validity bug by building the grader on a nephrology "conditional door" that existed only in the pipeline markdown, not the finalized world, the exact anchor-on-the-primary-artifact failure our own backbone warns about, committed again. We tried a TMP-SMX antibiotic trap and found it was not airtight, because the correct answer holds the RAAS agents and that defuses the hyperkalemia mechanism the trap depended on. We hand-built the handoff from a blank document and drifted off the world's fingerprint, introducing Calibri where the world is Arial and assuming a standard chrome band was an outlier. Each of these was caught, several by independent cold-context reviews, and each became a rule.

What finally worked was an insight from the red-team: a medication-safety task primes the model to hunt for errors, so anything that looks like an error gets caught. The only things that bite are a forced-choice ambiguity where the complete answer is unavoidable and the truth is unknowable, or a hazard disguised as routine that does not look like an error. The hardened handoff carried three planted errors, a nitrofurantoin switch and a home-dose ARNI restart as the visible anchors, and a potassium salt substitute buried in the diet line as the disguised-integration trap, built Mode A from the held-back original so it matched the world exactly. The pilot finally produced real spread: 97, 95, 95, 95, 92, 92, 90, 87, 82, 78.

How it cleared. The decisive finding was that the model caught every planted trap on the low runs; the spread was driven by the prednisone item, the model committing to "5 mg daily" off the most recent fill, the dispensing-equals-dose inference the case is built to discourage. Rather than chase a sub-70 the model would not give, we used Abi's pre-check. She approved, and the reason matters: "you specifically said a dose must not be written," the deliberately strict line in the golden is what made the failure gradeable and significant. Abi's final minor realism check, the hospital/location header, was also satisfied without requiring a rerun.

---

## 3. The evaluation stage (FA, GA, PL)

Detail: `task-setup/task1/FA-GA-final.md`, `task-setup/task1/preference-label-task1-A-vs-B.md`.

The Failure Analysis and Grader Analysis were written on the single lowest run (trajectory 5, 0.78), in Abi's prose form, after two format corrections (single paragraph tripped a length check; they had to be two short paragraphs, no headers). Preference Labeling compared two strong runs (A 0.90, B 0.97); both were clinically correct and both declined every trap, so the honest verdict was B1, slightly better on clarity, not a clinical gap. The preference writeup used the labeled-plus-Summary format the appendix example actually shows. It did not import the FA failure into PL, did not invent a major gap, and did not use plus-sign notation. The preference AutoQC cleared after fixing a tech-issue dismissal field with both the required response and a brief reason. Task 1 then passed final review.

---

## 4. What we carry forward

Detail: `docs/reasoning-discipline.md`, `task-setup/TASK-RUNBOOK.md`, `task-setup/CHECKPOINT-AUDIT-pre-task2.md`.

The backbone lesson is the reasoning-discipline gate: at any expensive or irreversible step, or any claim about why a system behaved a certain way, read the primary artifact (the live world file, the grading transcript, the config) before committing, rather than deferring to the most recent authority. We violated this twice on the same fact and it cost two rounds; it is now the governing rule. The 06/02 instruction guide reinforced the same rule in a different form: the golden sets the ceiling for what the grader can reward, so if the model beats the golden, improve the golden before blaming the grader.

The task-design lesson: clean and realistic is not enough; every task needs an engineered failure mode, and the only failures a frontier model gives on this kind of task are forced-choice ambiguities and disguised-integration traps, verified uncoached against the live world. The deep stumping belongs in the synthesis tasks (KM04, KM06), not the med-rec-adjacent ones.

The craft lessons: build task files Mode A from the pipeline original so they match the world fingerprint; never duplicate live world files into task-file names in a way that confuses RL Studio; write grader guidelines in the native "Task context / Must be present / Acceptable variation / Penalize for" structure with no weighting language (the doc's A/B/C trips the live gate); FA and GA are header-free prose on the single lowest run; PL uses labeled sections plus a Summary; tech-issue dismissals need both the exact "tech issue" response and a one-sentence reason in the dedicated field; keep backups as workspace files and log every stage as it happens.

The repository lesson is that workspace structure is not clerical overhead. The candidate-review, locked, ratifications, reviews, planning-scaffolds, task-setup, platform, and source/reference folders made the project cold-startable after every context break. The local repository remains canonical; the Drive mirror is reviewer-convenience sync material unless Alexander explicitly promotes a Drive file to source of truth. Google Drive mutation should use versioning when possible, not duplicate uploads.

The honest part, recorded on purpose: Task 1 took most of a day and three rounds, much of it off-clock, and several of the dead ends were ours. But it was the whole world's task-design tuition paid once. Tasks 2 through 6 inherit all of it, and the pre-flight in `CHECKPOINT-AUDIT-pre-task2.md` exists so none of it repeats. Do not start Task 2 or mutate RL Studio again until Alexander explicitly authorizes that exact step.

---

## 5. Where everything lives (index)

- The build story: `docs/claude-transcript-formatted.md`; structural map: `README.md`; decision trail: every `*/locked/` and `*/ratifications/`.
- Task 1 record: `task-setup/task1-lifecycle-log.md` (canonical); reviews: `task-setup/reviews/`.
- Lessons and rules: `docs/reasoning-discipline.md`, `docs/clinical-voice-lessons.md`, `docs/docx-generation-method.md`, `docs/world-pipeline-playbook.md`, `task-setup/TASK-RUNBOOK.md`.
- Task 2 pre-flight: `task-setup/CHECKPOINT-AUDIT-pre-task2.md`.
- Source/reference updates: `reference/source/World 004 QA + Failure + Grader Analysis.docx` and the 05/24 + 06/02 instruction materials inform the current task-stage doctrine.
- Forward: Tasks 2 to 6 (KM02 discharge summary is partly drafted in `task-setup/platform/task2/`), run per the runbook, deep stumping concentrated in KM04 and KM06. Task 2 remains blocked until Alexander authorizes the exact platform step.
