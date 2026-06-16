# Abi Review Protocol ("Abi mode")

> Voice: reviews follow the Dr. Alexander standard (`docs/alexander-voice-dna.md`) - omission, clinical significance, consequence; no process narration. Enforced by `tools/verify/verify_voice.py`.

Date: 2026-06-11, extended 2026-06-12 after AO's KM08 first review. Owner: Alexander. Maintainer note: extend this file every time a real Abi review lands; every lens below is grounded in a recorded catch, and the protocol's value is that grounding. Companion docs: `docs/task-difficulty-lessons.md` (sections 5 and 6 hold the fairness doctrine), `docs/reviewer-response-protocol.md`, `docs/clinical-voice-lessons.md`, `DO-NOT-REPEAT.md`.

## What this is

A pre-review gate that simulates Abimbola O's review patterns against any task packet BEFORE it is declared ready or sent for human review. The goal is to catch in-house what she has caught from outside: every lens here is reverse-engineered from a documented send-back or correction, with the source cited. This is not a style guide. It is a reconstruction of how a fresh, accountable, clinically fluent reviewer reads a packet cold.

How to invoke with Claude: "run Abi mode on the taskN packet" (or any phrasing naming Abi mode plus a target). The review covers the full staged set: prompt, provided files, golden, grader guidelines, run instructions, plus FA/GA if drafted. Output goes to `task-setup/taskN/qa/abi-mode-review-YYYY-MM-DD.md` using the template at the end of this file.

## Operating posture

Read cold, once, whole, in this order: prompt first, then the provided files, then ask what the most defensible completion is, and only then open the golden and grader. Read as three people in sequence: the model at run time (what do I actually know?), the clinician named in the artifact (would I write this, dated this way, citing these sources?), and the client (would I pay for this floor?). Never read as the designer. The designer already knows where the trap is and is therefore the one person who cannot review it.

## The nine lenses

Each lens: the question, the test, and the recorded catch it comes from.

### 1. Model's-seat fairness (the planted-claim class)
Question: if the model fails, is the failure genuinely the model's fault?
Test: read only what the model receives. If the most defensible completion (trusting the draft it was handed, following the file it was given) is the behavior that floors, the construction is unfair. Canonical AO rule for any finalize-the-draft task: either the prompt tells the model to correct errors in the draft, or the draft uses true placeholders for the model to complete in the finalized version. Re-attribution is only for external or weak-source documents, not for false content in a same-author started draft. Use placeholders first when difficulty matters; reconcile-and-correct is fair but often kills propagation difficulty.
Source: KM05 (home-BP attribution), KM06 (false closures), KM07 v2 (planted bone-health closure, retired despite flooring 9 of 10), KM08 first review (draft-finalize SOAP task with a pre-written gabapentin order and no correction instruction). Treat every new reviewer flag as a class on day one.

### 1a. The built-artifact rule (the gate with teeth)
Question: was lens 1 run against the built draft, or against a description of it?
Test: the fairness pass extracts the built draft's text from the bytes and QUOTES its verbatim lines about the scored item in the review record (if the item appears nowhere, the quote is "none", stated explicitly). Reviewing a design plan's description is not reviewing the task. Corollaries proven on the bytes: looking routine is asserting; a status disclaimer does not un-assert membership; a categorization (current versus held) is an assertion about every item it places; a pre-written plan order is an assertion the model is asked to countersign. A placeholder is only true if the draft leaves the scored decision blank for the model to complete. The uploaded file tree is also part of the artifact: inspect `/docs/filesystem`, `/docs/.apps_data`, duplicate preloaded volumes, and filenames. A filename such as clean, fixed, corrected, reviewer, or v4_clean can pre-answer the trap. If a task file appears under `.apps_data/calendar`, fix the Studio volume config rather than renaming files. Run the gate cold, by a non-builder. When any construction fails this lens, run the gate on the built bytes and agent-visible mounts of every staged or in-review sibling the same day.
Source: KM07 v3 (the plan said placeholder; the built draft listed alendronate as current beside a held list; first review trusted the plan and called it fair); KM08 v4.1 and AO first review (the de-telegraph pass removed the finalize pointer but left the pre-written uptitration order; AO required either a correct-errors prompt or placeholders); KM07 v4 job 6b687360 (main filesystem draft plus unexpected `.apps_data/calendar` draft disagreed on alendronate, and the `v4_clean` filename added a second leak; env_linter caught it); KM10 v2 job 138e90a2 (first trajectory showed the CDI query memo under both `/docs/filesystem` and `/docs/.apps_data/calendar`). Mechanics: TASK-RUNBOOK gate A0.5.

### 2. Genre purpose (the instrument test)
Question: does each artifact's logic survive what the instrument is FOR in real workflow?
Test: state in one sentence what the document is for (a CDI query is a retrospective pre-bill instrument; a referral letter hands open questions to a specialist; an attestation certifies coding from the record). Then check whether the golden's reasoning would make the instrument pointless.
Source: KM10 v1. The FA argued a diagnosis cannot be added after discharge, which would make every CDI query purposeless. The decline had to rest on clinical grounds, not the calendar.

### 3. Answer the question (the WHY test)
Question: does the golden actually answer what was asked, or restate the observation that prompted the question?
Test: for every item the prompt or query raises, the golden must give the reasoning a physician would give. Restating that symptoms exist and no diagnosis was made is not an answer; explaining why the course does not establish the diagnosis is.
Source: KM10 v1, item 2. The response repeated what the coder already noted and stopped.

### 4. Voice anchor (whose record speaks)
Question: is the golden anchored on the speaker's own documented assessment?
Test: identify who the golden speaks as. Their own team's notes must be the primary citation. An attending citing nursing and OT about his own patient's mental status while omitting his hospitalist's documented assessment is implausible as a person, even if every citation is technically true.
Source: KM10 v1 golden (omitted the hospitalist assessment the FA itself quoted). Register companion: `docs/clinical-voice-lessons.md`.

### 5. Structural realism (the chart-literal read)
Question: could this exact artifact exist in a real chart?
Test: scan every date against the anchor (no file dated after the event that requests it; no pre-snapshot encounters), every field against real clinical formatting (DOB, MRN, allergies, signature blocks present where the genre demands them), and every phrase against the chart register (no architecture words, anchor labels, trap language, or project metadata in any platform-facing document).
Source: Task 1 first review (files dated 05/24 for a 05/23 task; "Date / Anchor" fields in a clinical handoff; golden lacking demographic and signature blocks). Also the final-review demographics-placement fix.

### 6. Answer-giving scaffolding (the inflation test)
Question: does any provided file teach the answer or duplicate the reasoning the model is supposed to perform?
Test: for each task-context file ask three things: realistic, necessary, not duplicative. A file that tells the model how to perform the scored task inflates scores and gets deleted. Fewer files beat richer files.
Source: Task 1 first review (both task files deleted; the reconciliation request told the hospitalist exactly how to reconcile).

### 7. Difficulty and symmetric spread (the two-sided gate)
Question: is the task hard, and is the floor matched by proof a strong model can pass?
Test: all ten runs at or above 90 means no significant clinical failure and the task is not ready. All-floor with no catcher reads as an unfair gotcha and gets bounced. A bankable deep task is bimodal: real floors plus a catcher near 0.85 to 0.95, or failing a catcher, a structural proof that the golden itself scores high under its own grader. Read a catcher transcript, not just the mean.
Source: Task 1 second review (all ten at 90 or above, sent back); KM10 v1 (all-floor, reachability flagged); KM07 v3 (no catcher, golden self-score check required before banking).

### 8. Alignment after change (the surviving-artifact audit)
Question: after any reseed, deletion, or reframing, do all artifacts still agree, and do their settings still fit the new task?
Test: any file deletion or rename forces a prompt scan. Any framing change forces a grader re-audit for fit, not just wording: a golden-only grader is only safe when the scored axis is fully checkable against the golden; a synthesis task needs a chart-aware grader.
Source: Task 1 first review (prompt referred to deleted files); KM07 v3 pilot 1 (surviving golden-only grader flagged verbatim MAR detail as invented, 40-point noise on identical behavior).

### 9. Mechanism precision and self-standing records
Question: do all claims about how the platform, grader, or pipeline works match the actual mechanism, and does every annotation stand on its own reasoning?
Test: describe the grader as scoring output against the golden and guidelines, never as independently investigating. QA dispositions need substantive, fact-referenced rebuttals (cite the job, the runs, the observed behavior), never "the reviewer said it's okay". A bare "tech issue" annotation is situational: it is routinely accepted for the well-known recurring infra flags (the agentic-grader / model-access-preflight false positive, e.g. KM02, where "tech issue" saved and verified), but a bare one failed QA Feedback in KM07, so when a disposition is scrutinized or the finding is not plainly infra, use the substantive form. FA/GA is failure-only, natural prose, complete sentences, no bullets, no headers, no section names, the 2nd-LOWEST scoring run (King P 2026-06-14 / DO-NOT-REPEAT #20; supersedes the earlier "single lowest run"), each part under about 1000 characters, bound to the selected run in Studio.
Source: Task 1 grader-mechanism correction; KM02 agentic-grader flag where a "tech issue" annotation was accepted (counter-example); the Taiga QA Feedback failure on the bare tech-issue annotation (KM07, 6/11); Abi's FA/GA format directions (6/06 and 6/09).

## Mechanical pass (run before the judgment pass)

These are checkable without judgment and catch the cheap failures first: date-anchor scan across every header, footer, table, and signature; banned-character scan (em dash, en dash, arrows); fingerprint and metadata gates per the runbook; prompt-to-file reference scan; uploaded filesystem scan with `find /docs -type f` for duplicate drafts, hidden `.apps_data` copies, stale files, extra volumes, and meta-answer filenames; workflow string matches the tracker sheet exactly; grader chart-access setting matches the task type; new-to-world names checked for collisions and flagged for confirmation; preregistration locked before any pilot, never edited after.

## Verdict format

Write findings the way she writes them: a numbered finding stating what is wrong and why it matters, followed by a forward rule that prevents the class. Verdict is PASS or SEND BACK with the blocking findings named. Non-blocking observations go in a separate improvements section, raised as improvements, not defects.

## Review record template

```
# Abi-mode review: KMNN vX packet - YYYY-MM-DD
Scope: [files read, in cold-read order]
Posture confirmations: read cold before opening golden/grader: yes/no
Verdict: PASS / SEND BACK

Findings (blocking):
1. [Lens N] Finding. Forward rule.

Improvements (non-blocking):
- ...

Mechanical pass: dates / banned chars / fingerprints / prompt-file refs /
workflow string / grader access / names / prereg: each PASS or FAIL with one line.

Reachability status: catcher observed? golden self-score done? open items.
```

## Standing residuals this protocol must keep hot

Carried from the live record on 2026-06-12: KM07 v3 RETIRED as unfair (quiet bait, Abi catch verified on bytes; record at task7/qa/abi-mode-review-2026-06-11.md); KM07 v4 job 6b687360 RETIRED as invalid because Studio mounted two disagreeing draft copies, one under `/docs/filesystem` and one under `/docs/.apps_data/calendar`. The fix is Studio volume cleanup: delete the calendar volume, keep one filesystem draft named `nephrology_referral_letter_started_05262026.docx`, and rerun env_linter until Content Leakage, World Spec Alignment, and Trap Survival are green. No KM07 vector is bankable until a clean single-draft pilot runs and reachability is proven by a catcher or golden self-score. KM08 v4.1 is returned by AO for the same draft-fairness class: the draft pre-wrote the gabapentin uptitration order under a finalize-only prompt, and AO also described the attached draft as an admission-status determination. V5 placeholder-reseed planning is active in task8/design/KM08-PLAN.md; it must use one coherent SOAP-note mount, a true placeholder, and a fresh pilot. KM10 v2 job 138e90a2 is invalid because the first trajectory showed the query memo under both `/docs/filesystem` and `/docs/.apps_data/calendar`; do not bank or enter FA/GA from it. KM10 v3 is now staged locally as the balanced CDI query reachability pass: same clinical golden stance, clearer unsupported / unable-to-determine response paths, and no grader softening. It needs Alexander read-and-own, locked preregistration, authorized upload, first-trajectory mounted-set gate, and a catcher plus critical-failure read before banking. KM07 QA tech-issue annotation belongs to retired v3 evidence and must not be rerun for banking. Remove items from this list only when the underlying artifact closes them.
