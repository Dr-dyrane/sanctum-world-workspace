# KM02 red-team brief - for claude.ai (red team); Codex is the final black-team gate

Roles: claude.ai red-teams this package and returns problems + proposed fixes. Codex then runs the final black-team gate (last verification) before any pilot. Physician (Dyrane) owns and signs.

## Verify on the AGENT-READ layer only (this is non-negotiable, it already cost two corrections)
The world has three layers; only one is what the task agent reads. Red-team against the AGENT-READ docx, not the markdown and not the reference copies.
- AGENT-READ world = world/ in this bundle, copied verbatim from file-review/upload/filesystem/ (26 docx). Extract with python-docx iterating paragraphs AND table rows/cells. The MAR antibiotic rows and the culture status live in TABLE cells.
- Do NOT conclude from the FI-W markdown (thin layer; omits content the docx carries) or from the .meta/references / drive-package copies (same filenames, DIFFERENT bytes).
- Canary hashes (sha256 prefix) so you know you are on the right bytes:
  - medication_administration_record_05232026.docx = cf90ceb048ed
  - hospitalist_progress_hd1_hd2_05192026.docx = 42d8ccdfade3
  - admission_history_and_physical_05182026.docx = 059993d4307e
  If your MAR grep does not return "Ceftriaxone 1 g IV q24h" and "Oral step-down: cefpodoxime 200 mg PO BID", you are on the wrong file.

## What this task is
KM02 = Hospital Discharge Summary Generation. Deliverable: a discharge summary synthesizing Korvin Merrow's hospitalization (admit 05/18, discharge anchored 05/24) from the full chart, by clinical evolution, without copying the day-1 sepsis framing forward.

## Current state (what to red-team)
- PROMPT: prompt-task2-v1-DRAFT.txt. Neutral attending-voice ask; deliberately does not feed the reasoning. (claude.ai earlier: well-calibrated.)
- GOLDEN (ceiling): golden-KM02-v4.docx, built from golden-KM02-source.md through the world builder, then banner-stripped, date label = plain "Date". Blue/navy Epic chrome, no synthetic banner (matches the agent-read world), Epic clinical outline (Reason for Admission / HPI / Hospital Course / Active Problems / Discharge Planning).
- DESIGN + DISCRIMINATOR + GRADER SCOPE: KM02-design-plan-for-review.md. Read the CORRECTION block at the very top first; it supersedes earlier statements.
- LOCKED CANON: canon/ (TP-KM02, GG-KM02, EO-KM02, FI-T02).
- CONTINUITY: continuity/ (THE LAW + the build gate that this task taught).

## The discriminator (post-correction, verify it holds)
The chart documents an OPEN infection picture: empiric ceftriaxone -> cefpodoxime step-down with "completion vs continuation to be reconciled at discharge"; urine culture preliminary growth, speciation and sensitivities pending, never narrowed; blood cultures pending; nothing finalized. So:
- Reporting the preliminary/pending culture status and the named antibiotic is CORRECT and creditable.
- The fabrication that bites (the discriminator) = a FINALIZED organism, a sensitivity profile, a no-growth / "cultures negative" closure, or NARROWING antibiotics by culture. Plus the broader over-closure (final med rec, final disposition, discharge condition) the chart flags as pending.
- Open structural question: this chart is relentlessly disciplined about its own uncertainty (every closure is flagged pending somewhere), so a clean pilot likely lands high (80-85%), not the 60% target. The colleague-draft escalation (a half-finished summary that plants the snapshot-silent closures, e.g. a finalized organism) is held in reserve.

## Questions for the red team
1. Golden as ceiling: does golden-KM02-v4 score full marks under GG-KM02, with no over-closure, no fabrication, and the culture/antibiotic stated exactly as the agent-read chart states them? Any line an agent output could legitimately beat?
2. Discriminator: is "finalize/narrow the culture" the right uncoached forced error now that the chart's open status is richer than we first thought? Is there a stronger snapshot-silent closure to target?
3. Grader scope: does the corrected scope (credit the pending status + the named antibiotic; penalize only finalized closure / narrowing) translate cleanly into GG-KM02 without tripping the Task-AutoQC "No Weight Distribution" / "No Scoring Framework" flags?
4. Prompt: still neutral, still not feeding, not over-pressing closure beyond a normal attending ask?
5. Clean pilot first vs build the colleague-draft now? If clean is expected high, is the draft the right lever, and what exactly should it plant (keep to airtight snapshot-silent items)?
6. Integrity guardrail check: would any proposed path reach 60% only by penalizing reasonable openness-preserving answers? If so, flag it as unfair.

## Integrity guardrail (hard line)
60% must come from real over-closure and fabrication failures, never from tightening what counts as a correct summary. If the task only reaches 60% by penalizing reasonable openness-preserving answers, report the honest clean pass rate instead.

## Bundle contents
- RED-TEAM-BRIEF-KM02.md (this file)
- golden-KM02-v4.docx + golden-KM02-source.md
- prompt-task2-v1-DRAFT.txt
- KM02-design-plan-for-review.md (read the top CORRECTION block first)
- canon/ : TP-KM02, GG-KM02, EO-KM02, FI-T02
- world/ : the 26 AGENT-READ docx (verify against these, by hash)
- continuity/ : reasoning-discipline.md (THE LAW + build gate)
