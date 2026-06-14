# Anti-hallucination doctrine

Date: 2026-06-14. Why this exists: across the Ondina spec-review and tasking-prep sessions, every factual miss had the same root cause and the same cure. The cause was almost never invention; it was trusting a STALE or SECONDARY reference instead of the LIVE PRIMARY source. This doc concentrates the rules that prevent it. Read with `docs/reasoning-discipline.md` (the verification backbone) and `DO-NOT-REPEAT.md` (the class-level ledger). Referenced from AGENTS.md guardrails 2 and 7.

## The one rule

Before adopting any convention, value, or status, read the LATEST PRIMARY artifact and the correction history, not the oldest document that describes it. State what is verified from bytes versus what is inferred.

## The seven levers

1. Verify against the bytes or the live source, never memory or a summary. Ground every factual claim in the actual artifact: the agent-read docx (python-docx including table cells), the grading transcript for scores, the config for platform behavior, KM's LATEST shipped file for a convention, the LIVE Task Selection Categories sheet for a workflow. A summary, a snapshot, or recollection is not evidence.

2. Treat every reference as stale until dated and re-checked. The dominant hallucination source here is outdated truth, not fabrication: a reference that was once correct and silently changed. Every canonical reference must cite its source and the date verified; anything older than the last guidance change is re-verified before use.

3. Single source of truth plus gates that fail on contradiction. Each value lives in exactly one place (`clinical_data.py`, `task_data.py`, the `WORKFLOW` map). `tools/verify/verify_ondina.py` cross-checks the ratified anchors across every file and FAILS on any contradictory variant. When a value changes, change it once and re-run the gate; grep every source for the old value, including sources the gate does not scan (the spec doc, transcripts, planning docs).

4. Flag derived versus ratified; never assert invented specifics. Every generated clinical value is flagged in the DERIVED registry and stays flagged until the physician ratifies it. No dose, lab, vital, date, organism, or name enters any artifact as fact without a ratified source. Intentional ambiguities stay ambiguous.

5. Distinguish form-checked from true. The local gates and the AutoQC verify STRUCTURE and internal consistency; they explicitly do NOT verify clinical validity or genuine difficulty, which are physician-owned and proven by piloting. A clean gate means well-formed, not correct.

6. Adversarial second pass on high-stakes or one-way-door calls. A cold-context re-read or a subagent audit catches premise errors the working context is anchored to. Run it on contested QC dispositions, format conventions, and anything irreversible.

7. Provenance and determinism. Reproducible builds, live SHAs in the manifest (never hand-copied), and a recorded read receipt of the files and lessons consulted before a build.

## The session case studies (why each lever exists)

- Grader format: adopted the v6.6 writer-doc's A/B/C + five-band scoring, but KM's LATEST shipped grader (task9 v2, 2026-06-13, written after v6.6) uses the five-block with no bands. Reading the actual KM file corrected it instantly. Levers 1, 2.
- Workflow remap: leaned on a 06/10 snapshot of the Task Selection Categories sheet whose priorities had already drifted. Lever 2.
- Spec drift: the attending rename and the baseline ambulation were fixed in `clinical_data.py`, the world files, and the goldens, but not in the spec doc, which the gate does not scan; live Spec AutoQC caught the contradiction. Lever 3.

## The preventing question

If a single check could have caught every miss this session it is this: am I reading the latest primary artifact and its correction history, or a document that merely describes it? If the latter, stop and go to the source.
