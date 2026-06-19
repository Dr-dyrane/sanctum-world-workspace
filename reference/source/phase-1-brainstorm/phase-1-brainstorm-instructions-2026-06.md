# Part 1: Brainstorm (official instruction-document transcription)

Source: Project Sanctum instruction document, "Part 1: Brainstorm" (World Setup writing standards, Rough Task Ideas writing standards, Common Mistakes, and the Studio upload/AutoQC/submit flow). Transcribed from screenshots shared 2026-06-19. Faithful content capture for internal reference; punctuation normalized (em and en dashes rendered as commas, hyphens, or periods) to satisfy the repo no-dash rule, wording otherwise preserved. Visual source: screenshots/ (to be filed).

Note: all brainstorm work is meant to be done in Sanctum Coach, which walks you through these concepts. This file is the static reference. The local derived checklist is reference/checklists/brainstorm-checklist.md.

Anonymization warning (verbatim intent): all patient names, dates, MRNs, hospital names, and other identifying details must be anonymized. AI agents have training data, so real cases from literature or case reports risk model leakage.

There is a linked "Example of a strong Brainstorm document" in the source.

## World Setup: Writing Standards
1. Patient clearly defined (fictional). A specific fictional patient with enough identifying detail (demographics, comorbidities, presenting condition, care setting) that any writer or reviewer could anchor a chart around them. Do not use character names from movies, TV shows, video games, celebrity figures, etc.
2. Generates a mix of document types. The scenario should naturally produce the full range of clinical documents: progress notes, consult notes, lab reports, medication lists, nursing flowsheets, patient-provided documents, etc.
3. Realistically supports 10+ tasks. Substantial enough that 10+ distinct clinical tasks could plausibly arise. Too narrow and the world cannot support enough tasks; too sprawling and the chart cannot stay coherent.
4. Contains multi-stakeholder friction. Stakeholder conflicts, disagreements between people, not just discrepancies between documents: specialist vs specialist, family vs medical team, primary vs consultant, patient vs provider.
5. Contains information-level traps. Chart-level traps, pieces of information that could mislead a careful clinician if not contextualized: contradictory EMR entries, buried significant findings, missing data, source-of-truth ambiguity, SDOH constraints, temporal or sequencing complexity. Standard 4 is about people; this is about information (stale med list vs pill-bottle photo, aspiration event buried in a nursing note).
6. World and tasks do not take place after July 31, 2025. The model being tested cannot use information after July 31, 2025, so the world must end before this date. No clinical guidelines, drugs, or standards released after July 31, 2025. All required knowledge must come before this date.

## Rough Task Ideas: Writing Standards
1. Maps to an approved workflow. Every task maps to one workflow on Sanctum's approved workflow list (a category that produces a concrete deliverable). If you cannot point to a specific approved workflow, it is not a Sanctum task. Every world must contain 10+ tasks spanning at least three workflows, and at least one P0 workflow. Workflows are prioritized: P0 = high priority (start here), P1 = medium, P2 = low (acceptable only if P0 and P1 are exhausted).
2. Requires reasoning, not just extraction. The task requires synthesizing and reasoning across multiple files, not just extracting facts. If it can be answered by pulling facts (even from multiple documents) without reasoning over them, it is too easy. Reasoning plus extraction, not just extraction.
3. Concrete, evaluable deliverable. Names a specific deliverable in a gradeable format. Not "tell me what you think" or "summarize", but a specific work product a reviewer could grade against a Golden Response.
4. Tasks are INDEPENDENT of each other. A common mistake is thinking Task 1's output must feed Task 2's design. That is not what we want.
5. Anchored after the world's last event, not in the distant future. Every task is anchored at a specific date and time after the world's most recent event, but not so far out that guidelines or labels may have changed. Example: world ends May 11, 2026 at 2:30 PM EST, a task at May 11, 2026 at 4:00 PM EST is fine. A task dated before the world's last event, or in the distant future, breaks this.

## Common Mistakes in Brainstorm
- Mistake 1a: Clinical knowledge from August 1, 2025 or later being required. The world and tasks must end before July 31, 2025.
- Mistake 1b: Rough task ideas that did not map to any workflow from the workflow list.
- Mistake 2: Patient name not realistic. Do not use character names from movies, TV shows, video games, celebrity figures.
- Mistake 3: Patient information too generic (weak example: "a middle-aged man with high blood pressure and some heart issues presents with shortness of breath", no demographics, comorbidities, medication baseline, or as-of moment, so the scenario cannot anchor).
- Mistake 4: Temporality. You cannot create a scenario in the middle of the world. The task must take place temporally after what has already happened. The world represents everything that has already happened; the tasks represent the work occurring next. (Weak example: world records 2020 through March 2025, task dated January 2023.)
- Mistake 5: Tasks not from the clinician's perspective. Frame every task from the perspective of a clinician, not an OT, nurse, social worker, or other role. Reframe toward the physician-owned equivalent (progress note, discharge summary, consult note, medication reconciliation, etc.).

## Upload and AutoQC Brainstorm in Studio
- Studio access: work.mercor.com, contract page, Okta Account, Apps, Studio. In Studio, Dashboards, then My World Building Tasks. Note: Studio is not supported on Safari; use Chrome. Clear cache and cookies if loading problems persist, then tag the tech-issues slack channel.
- Create the brainstorm: Dashboards, My World Building Tasks, Create Task (top right). Upload your Writer's Input Template (the brainstorm document), then Run AutoQC (bottom right).
- Disagreeing with AutoQC flags: before moving past AutoQC, every criterion must be a green check, OR you write an explanation for each criterion marked with a red X (thumbs-down, then fill the text field with your response). Any failing flag left unaddressed sends the task back, so justify each failing criterion before moving on.
- Final submission: click "Submit plan for review." You are notified when it is approved or sent back with detailed notes. Keep all brainstorm communication in your Slack thread. Check status under Dashboards, My World Building Tasks.

## What this confirms for our readiness checks
- Brainstorm submission = upload the brainstorm document, Run AutoQC, address or justify every flag, then Submit plan for review. No Claude transcript is part of the brainstorm-stage submission per this guide.
- The AutoQC "maps to an approved workflow" criterion is the mechanical check that catches non-verbatim or invented workflow strings (Mistake 1b).
- Priority (P0/P1/P2) is a per-workflow attribute; the world must carry at least one P0.
