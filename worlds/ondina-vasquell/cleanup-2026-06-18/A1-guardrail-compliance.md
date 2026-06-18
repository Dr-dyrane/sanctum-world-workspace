# A1 - Guardrail Compliance Audit, Ondina Vasquell (OV01-OV10)

Date: 2026-06-18. Scope: read-only audit of the OV task artifacts against the project guardrails. Guardrails read in full: `AGENTS.md`, `docs/fa-ga-canonical.md`, `docs/grader-guidelines-lessons.md`, `docs/alexander-voice-dna.md`, `DO-NOT-REPEAT.md`. Artifacts audited: the 10 graders, 10 prompts, and 8 FA/GA files under `phase-3-build-task-artifacts/platform/task*/current/` and `phase-4-pilot-review-submit/fa-ga/`.

Tags: BLOCKER (must fix before submit), MAJOR (rule break, fix before bank/submit), MINOR (drift or documented deviation).

## Headline

The grader layer and the prompt layer are clean across all ten tasks. Every grader carries the five-block structure in order, names its golden verbatim with a filename that matches the file on disk, carries both verbatim clauses, sits at or under 540 words, and shows no leaked AI/eval meta language and no dashes. Every prompt is plain physician voice with no reconcile or verify clause, no "current guidelines" phrasing, and no literal path.

The FA/GA layer is where the violations sit. Two FA/GA files are missing entirely (OV05, OV10). Three GA bodies miss the mandatory grader-improvement move and read as affirm-plus-calibration only (OV03, OV07, and more weakly OV01/OV02). Two fields run over the ~1000-char working cap (OV03 FA, OV06 GA). One FA subject deviates from the second-lowest-distinct run with a documented rationale (OV03).

---

## Per-task findings

### OV01 - grader CLEAN, prompt CLEAN, FA/GA minor drift
- Grader `grader-guidelines-OV01.txt`: 447 words, five blocks present, golden `golden-OV01-v1.docx` named and on disk, both verbatim clauses present, no dashes, no meta tokens. CLEAN.
- Prompt `prompt-OV01.txt`: plain first-person, no reconcile/verify/guideline/path. CLEAN.
- FA/GA `FA-GA-OV01-current.md`: FA 654 chars, GA 479 chars, two paragraphs each, second-lowest run noted (Attempt 6, 0.50). Failure-only, no section names, no dashes, no rating line.
  - MINOR (GA): the GA is affirm-plus-caveat. P1 names what the grader caught; P2 is the stricter-reading caveat ("If anything the score is generous... could be docked harder"). Canonical move 2 (a named grader miss or improvement) is not given. This is the borderline-acceptable form the canonical doc allows for a genuinely sound grader, so it is drift, not a hard break. Fix: keep the caveat but add one concrete grader-improvement or explicitly state the grader was sound and add the looser-reading caveat too.

### OV02 - grader CLEAN, prompt CLEAN, FA/GA minor drift
- Grader `grader-guidelines-OV02.txt`: 508 words, structure and clauses present, golden `golden-OV02-v6.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV02.txt`: plain voice, clean. CLEAN.
- FA/GA `FA-GA-OV02-current.md`: FA 920 chars, GA 748 chars, two paragraphs each, second-lowest distinct noted (Attempt 10, 0.12). Clean on dashes, section names, rating, banned phrases.
  - MINOR (GA): same affirm-plus-caveat shape as OV01. P2 closes "If anything the score is generous... a stricter read could dock harder." No named grader-improvement move. Same fix.
  - Note (not a violation): the Status line records all ten runs floored with no catcher, so banking still needs a catcher or golden self-score before submit. That is a banking-readiness flag the file already carries, not an A1 compliance defect.

### OV03 - grader CLEAN, prompt CLEAN, FA/GA two issues
- Grader `grader-guidelines-OV03.txt`: 535 words, structure and clauses present, golden `golden-OV03-v1.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV03.txt`: plain voice, clean. CLEAN.
- FA/GA `FA-GA-OV03-current.md`:
  - MAJOR (FA length): FA body is 1017 chars, over the ~1000-char working cap. Fix: trim about 20-30 chars (e.g., drop one of the two trailing examples in the second paragraph).
  - MAJOR (GA missing move 2): the GA is the calibration-close form the canonical doc explicitly says is incomplete. P1 names what the grader did correctly; P2 is pure calibration ("A deep floor would overstate... a high score would ignore... The 0.12 is justified"). There is no named grader miss or improvement. Fix: add one constructive point (for example, the grader could name the unsupported cephalexin and the early restart of held agents as distinct scored items rather than folding them into general credit, so it does not have to infer partial credit).
  - MINOR (run binding): FA subject is Attempt 1 at 0.12, but the distinct scores are 0.05, 0.10, 0.12, 0.15, 0.20, so the second-lowest distinct is 0.10. The file documents the deviation ("lowest run with a full transcript in hand; rebind to a 0.05 or 0.10 run if strict lowest-run binding is required"), which the King P rule permits with rationale. Acceptable as documented, but flag to rebind to a 0.10 run if a strict reading is wanted at submit.

### OV04 - grader CLEAN, prompt CLEAN, FA/GA CLEAN
- Grader `grader-guidelines-OV04.txt`: 537 words (near the 540 cap but compliant), structure and clauses present, golden `golden-OV04-v1.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV04.txt`: plain voice, clean. CLEAN.
- FA/GA `FA-GA-OV04-current.md`: FA 754 chars, GA 559 chars, two paragraphs each. Failure-only, no section names, no dashes. This is the accepted worked exemplar reproduced in `alexander-voice-dna.md`. CLEAN.
  - Note: the "poor/Poor" matches in an automated rating scan are the clinical phrase "poor CPAP adherence," not a rating line. No violation. Subject (Attempt 9, 0.20, second-lowest distinct) is bound in the internal-provenance comment, which is not pasted.

### OV05 - grader CLEAN, prompt CLEAN, FA/GA MISSING
- Grader `grader-guidelines-OV05.txt`: 509 words, structure and clauses present, golden `golden-OV05.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV05.txt`: plain voice, clean. CLEAN.
- BLOCKER (FA/GA absent): no `FA-GA-OV05*.md` exists anywhere in the repo. If OV05 has piloted and is heading to bank/submit, the FA/GA must be authored on the second-lowest-distinct run in canonical form. If OV05 has not yet piloted, this is expected and downgrades to a tracking item, not a defect. Confirm pilot state before treating as a hard blocker.

### OV06 - grader CLEAN, prompt CLEAN, FA/GA one length issue
- Grader `grader-guidelines-OV06.txt`: 502 words, structure and clauses present, golden `golden-OV06-v1.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV06.txt`: plain voice, clean. CLEAN.
- FA/GA `FA-GA-OV06-current.md`: FA 964 chars (ok). Failure-only, no section names, no dashes, no rating, no banned both-sides phrases. The GA is the full grader-audit form: P1 what the grader got correct, P2 a named grader weakness ("less rigorous when evaluating added detail... would be stronger if...") plus calibration. Both mandatory moves present. Second-lowest distinct noted (Attempt 10, 0.10).
  - MAJOR (GA length): GA body is 1225 chars, well over the ~1000-char working cap. Fix: compress P2; the added-detail point can be made in two sentences rather than four without losing the move.

### OV07 - grader CLEAN, prompt CLEAN, FA/GA missing move 2
- Grader `grader-guidelines-OV07.txt`: 473 words, structure and clauses present, golden `golden-OV07-v1.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV07.txt`: plain voice, clean. CLEAN.
- FA/GA `FA-GA-OV07-current.md`: FA 996 chars (ok), GA 797 chars (ok), two paragraphs each, second-lowest distinct noted (Attempt 6, 0.22). Clean on dashes, section names, rating, banned phrases.
  - MAJOR (GA missing move 2): the GA affirms and calibrates but names no grader miss or improvement. P1 says the grader scored the omission correctly and credited the supporting points; P2 says the supporting points do not overcome the omission and "the assigned score is appropriate." No constructive point on the grader itself. Fix: add one (for example, the grader relies on the same added-detail verification its instructions require and could state that it verified the off-text wound finding against the chart, or note where it was lenient or strict).

### OV08 - grader CLEAN, prompt CLEAN, FA/GA CLEAN
- Grader `grader-guidelines-OV08.txt`: 489 words, structure and clauses present, golden `golden-OV08-v1.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV08.txt`: plain voice, clean. CLEAN.
- FA/GA `FA-GA-OV08-current.md`: FA 989 chars, GA 826 chars, two paragraphs each, second-lowest distinct noted (Attempt 9, 0.15). Failure-only, no section names, no dashes, no rating. GA carries both moves: P1 what the grader did correctly, P2 a named grader weakness ("did not scrutinize the detail the response added... would be stronger if...") plus calibration. CLEAN.

### OV09 - grader CLEAN, prompt CLEAN, FA/GA CLEAN
- Grader `grader-guidelines-OV09.txt`: 538 words (near the 540 cap but compliant), structure and clauses present, golden `golden-OV09.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV09.txt`: plain voice, clean. CLEAN.
- FA/GA `FA-GA-OV09-current.md`: FA 973 chars, GA 976 chars, two paragraphs each, second-lowest distinct noted (Attempt 10, 0.35; lowest distinct 0.25 also named). Failure-only, no section names, no dashes, no rating. GA carries both moves: P1 what the grader scored correctly, P2 "One point could improve... Naming that as a distinct error..." plus calibration. CLEAN.

### OV10 - grader CLEAN, prompt CLEAN, FA/GA MISSING
- Grader `grader-guidelines-OV10.txt`: 539 words (right at the cap, compliant), structure and clauses present, golden `golden-OV10.docx` named and on disk, clean. CLEAN.
- Prompt `prompt-OV10.txt`: plain voice, clean. CLEAN.
- BLOCKER (FA/GA absent): no `FA-GA-OV10*.md` exists anywhere in the repo. Same caveat as OV05: if OV10 has piloted and is heading to bank/submit, author the FA/GA; if it has not piloted, this is a tracking item, not a hard blocker. Confirm pilot state.

---

## Per-task counts

| Task | Grader | Prompt | FA/GA | BLOCKER | MAJOR | MINOR |
|------|--------|--------|-------|---------|-------|-------|
| OV01 | clean | clean | drift | 0 | 0 | 1 |
| OV02 | clean | clean | drift | 0 | 0 | 1 |
| OV03 | clean | clean | issues | 0 | 2 | 1 |
| OV04 | clean | clean | clean | 0 | 0 | 0 |
| OV05 | clean | clean | MISSING | 1 | 0 | 0 |
| OV06 | clean | clean | length | 0 | 1 | 0 |
| OV07 | clean | clean | move 2 | 0 | 1 | 0 |
| OV08 | clean | clean | clean | 0 | 0 | 0 |
| OV09 | clean | clean | clean | 0 | 0 | 0 |
| OV10 | clean | clean | MISSING | 1 | 0 | 0 |
| TOTAL | | | | 2 | 4 | 3 |

## Cross-cutting notes

- Grader word counts (all <= 540): OV01 447, OV02 508, OV03 535, OV04 537, OV05 509, OV06 502, OV07 473, OV08 489, OV09 538, OV10 539. None violate.
- The most repeated FA/GA defect is the missing or thin mandatory GA move 2 (what the grader got wrong or could improve). OV03 and OV07 fully drop it (MAJOR); OV01 and OV02 carry only the stricter-reading caveat (MINOR). OV06, OV08, OV09 carry it correctly and are the template to copy.
- Length cap is per field, not per file. Whole-file char counts are large because of the Status header and headings; the load-bearing measure is the FA body and GA body, reported above. Only OV03 FA (1017) and OV06 GA (1225) exceed ~1000.
- Gate scripts `tools/verify/verify_ondina.py` and `tools/verify/presubmit_task_gate.py` are present; per DO-NOT-REPEAT #22 they enforce the 540-word grader cap and golden-vs-grader consistency. This audit did not execute them (read-only), but the grader and golden-naming checks above are consistent with a green lint.
- The two missing FA/GA files (OV05, OV10) are the only BLOCKER-class items and are conditional: blocker if those tasks are piloted and bound for bank/submit, tracking item if not yet piloted. Confirm pilot state for OV05 and OV10 before classifying.
