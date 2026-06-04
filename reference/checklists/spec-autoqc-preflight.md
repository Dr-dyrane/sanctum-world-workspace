# Spec AutoQC v109 Preflight Checklist (distilled from Korvin Merrow, 5 remediation rounds)

Run this BEFORE the first AutoQC of any future world. Korvin went 26 fails -> 108/109 only after discovering these by fire. Next world should pass round one.

## Document identity & formatting
- [ ] Filename: `Writer_World_Patient_latest_M_D.docx` (e.g., Alexander_World_Merrow_latest_6_4.docx). Writer token first; latest_M_D suffix mandatory.
- [ ] Header table at top with: World Title/Number, Patient Name (fictional), World Type, Setting, Specialty/Workflow, Total Tasks, Project, Version.
- [ ] All display dates MM/DD/YYYY everywhere (incl. DOB - no YYYY-MM-DD).
- [ ] ZERO em dashes, en dashes, arrow characters (->, ->) in spec AND transcript AND all uploads. Use hyphens, commas, "then".
- [ ] No "PO" letter-O token anywhere - write medication routes as "Oral" (the rubric's P0-vs-PO regex hits per-os abbreviations).
- [ ] American English.

## Section 1
- [ ] 1.1 Big Picture: max 2 paragraphs AND states file-plan composition ("X world-level + Y task-level + Z supplementary = N unique files supporting M tasks").
- [ ] 1.2 contains: Patient Profile table, home-med list (EVERY med with dose/route/frequency/indication - any intentional gap needs a 2.5 note ready), Decision Friction Table (in 1.2, not 1.5), Care Team Roster table with Name/Credentials/Role/Service.
- [ ] Multiple med lists temporally labeled (which list, which date, which scope).
- [ ] 1.5 includes difficulty distribution sentence.

## Section 2 (per task - all of these, every task)
- [ ] Title, Workflow line with EXACT tracker name + "- requested by <persona>".
- [ ] Anchor: single MM/DD/YYYY. Priority: P0/P1/P2 (digit!). Capability: named reasoning skill. Time estimate + justification. Difficulty label.
- [ ] Draft Prompt: short, natural colleague voice. NO "anchor"/"without assuming"/rubric-speak; NO meta vocabulary ("physician-facing"); NO domain checklists; NO trap hints (don't mention family concerns, consultant disagreement, or whatever the trap is - the agent must discover it).
- [ ] Expected Output: format AND register AND length range AND specific clinical anchors.
- [ ] Failure Design: >= 5 traps, each remediation anchored to specific file ID + MM/DD/YYYY date; shared traps marked "(shared world trap; primary in Task N)".
- [ ] Task-level files line; single deliverable per task; sequential numbering; no Task N+1 implied by file IDs.

## Section 3 (file plan)
- [ ] ID convention: EW# (world essential) / E#-T# (task-level, suffix = real task) / WS# (world supplementary). NOT FI-*.
- [ ] Filenames: lowercase_underscores_MMDDYYYY.ext - no spaces, date embedded, extension present; matches uploaded 2.2 filenames EXACTLY.
- [ ] Description column builder-ready: required content + structure + key facts + exclusions per row (not topic labels).
- [ ] Pearls/Traps/Friction column EXPLICITLY names every trap that anchors to that row ("Anchors Task N <trap name> trap") - the rubric cross-checks Failure Design anchors against this column.
- [ ] Total line: "Total file count: X + Y + Z = N unique files."
- [ ] File dates within milestone window; IDs monotonic, no collisions.

## Section 4
- [ ] World Summary: 3-5 sentences EXACTLY, covering what it tests + why trap architecture works + explicitly why hard for an AI agent. No 1.5 duplication.

## Uploads & process
- [ ] 2.2 reference files uploaded BEFORE first AutoQC run, names matching the spec file plan exactly.
- [ ] 2.3 transcript: dash/arrow-sanitized DOCX; covers brainstorm AND spec phases; share URL retained.
- [ ] RL Studio task card placeholder prompt replaced.
- [ ] After first run: use "Rerun N failing" only - never full reruns (LLM-grader variance can flip green dimensions).
- [ ] Notes (2.5): quote exact flag text, then reasoned response. Keep only live-flag notes + a one-paragraph resolution history.
- [ ] Auditor false positives happen (extraction artifacts, confabulated locations) - but verify against the FULL document (all table cells, not just paragraphs) before claiming the auditor is wrong. Korvin lesson: the "letter-O PO" was real, just mislocated.

## Design-stage choices that prevent flags entirely
- [ ] Decide intentional ambiguities (like prednisone) at brainstorm; write the 2.5 defense the same day.
- [ ] Use the EW/E#-T#/WS convention and date-stamped filenames from file-inventory day one.
- [ ] Write draft prompts in persona voice from the start; keep all rubric/design language out of Sections 1 and 4 prose.
