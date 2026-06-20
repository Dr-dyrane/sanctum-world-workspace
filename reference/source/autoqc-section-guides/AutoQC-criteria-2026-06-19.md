# Live Task AutoQC criteria (captured 2026-06-19)

The task AutoQC tightened substantially in mid-June 2026; it now runs a full prompt-golden-grader-world correlation across the criteria below, organized by section. This supersedes the v6.6 Section 5/6 writer guides for COVERAGE (those remain useful for the golden and grader detail). Transcribed from the live AutoQC criteria panel on an OV08 review, 2026-06-19. Treat each line as a pass/flag check; address or dispute every non-pass before moving to Taiga Trajectories.

## World Files
- Golden Answer Grounded in World Files
- World Spec Alignment (built files must not diverge from the spec in content or attribution without justification)
- Trap Documentation and Density (every designed trap documented in the preamble/spec or failure-design tables)
- File Set Complete (every file referenced in task materials is present)
- Clinical Code Validity
- Prescriber Attribution Integrity
- Content Leakage
- Embedded File Metadata Clean
- Trap Survival and Inventory
- No Authoring Artifacts
- Calculation and Fixture Accuracy
- Clinical Values Plausible and Consistent
- Medication List Consistency (no med discrepancy undocumented as an intentional trap; see KNOWN-CHART-DISCREPANCIES)
- Identity and Demographics Consistent
- Service Attribution Consistent
- Document Chronology and Sequencing
- Task Temporal Anchoring Verified
- Traps Logically Resolvable
- Trap and Difficulty Survive File Generation
- Supporting Clinical Data Present
- Clinical Authenticity
- Writing Quality (No AI Tells)
- EHR Conventions and Register
- Signature and Formatting Consistency
- Content Completeness (No Gaps)
- Document Length Appropriate

## Prompt Quality
- No Post-July 2025 Knowledge Dependency
- Prompt Completeness and Self-Containment
- Prompt Language and Formatting
- Prompt Boundary and Workflow
- All Tasks Physician-Produced
- No World File Pre-Answers a Task
- Prompt over-specifies or over-explains task (fail)
- Prompt prescribes workflow or reasoning process (fail)
- Prompt contains answer-bearing context (fail)
- Role-play language (fail)
- Prompt asks for word count (fail)
- Partial date format (fail)

## Golden Answer
- Golden Answer Exists and Is Complete
- Golden Answer Quality
- Golden response formatting

## Grader Guidelines
- Task overview matches prompt (the grader's described deliverable matches the prompt's deliverable; cross-task contamination fails here)
- Filename match (the grader's named golden matches the actual golden filename exactly, including version tag)
- Grader Guidelines: Complete and Quality (self-contained: references the available golden + world files)
- Grader guideline boilerplate (FAIL on any named filler phrase; see qc-error-class-register BANNED_BOILERPLATE)
- Grader guidelines explaining concepts (no concept-teaching; state what to assess)
- Word counts in grader guidelines (no word-count instructions; keep ~1 page)

## Trajectory AutoQC (the second QC layer, captured 2026-06-19)
Separate from the task AutoQC above, the Trajectory AutoQC runs on the completed trajectory batch (the ten runs and their grading), at the Trajectories stage. Its criteria seen so far:
- Compliance with Output Constraints
- Grading Accuracy: Score Reflects Performance
- Infrastructure Integrity: No Env Contamination
- No Solution Leakage Detected
- Task Design Quality: Tests Intended Capability
- Appropriate Severity Calibration

ADVERSARIAL-TASK NOTE (important). "Compliance with Output Constraints" will flag a FLOOR trajectory, the run where the model fails the deliverable, as a constraint violation. For a difficulty task that is the intended capture, not a defect: the model not finalizing is the measured failure, and the grader scores it low. Do NOT re-run a correctly-graded floor. Justify it in the Notes field: it is the task's designed failure mode, the grader confirms it, and other trajectories reach the constraint and score high, so the constraint is reachable. Paste-ready justification in docs/qc-dispositions.md.

## What we already guard locally (docs/qc-error-class-register.md)
- Grader guideline boilerplate -> BANNED_BOILERPLATE list in presubmit + verify_ondina.
- Filename match / Task overview matches prompt / cross-task contamination -> presubmit prints a per-task Studio FIELD MAP and flags a grader naming a golden absent from its dir.
- File Set Complete -> presubmit upload manifest + RUN mount-file existence check.
- Medication List Consistency (undocumented discrepancy) -> KNOWN-CHART-DISCREPANCIES disclosure + paste-ready dispute.
- Embedded File Metadata Clean -> verify_ondina metadata gate (docProps scrubbed).

## Not yet locally gated (rely on the live AutoQC + human review)
Clinical Code Validity, Prescriber Attribution Integrity, Clinical Values Plausible/Consistent, Identity/Demographics Consistent, Service Attribution Consistent, Document Chronology, Traps Logically Resolvable, Writing Quality (No AI Tells). For World 3, author these correctly at the source (the W3-MASTER-PACKET Part 7 chart-consistency rule) since the chart is frozen once tasking begins.
