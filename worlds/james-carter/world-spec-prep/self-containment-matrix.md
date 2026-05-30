# Self-Containment Matrix

## Already Locked From Brainstorm

Core self-containment burden:

- The agent must solve tasks from the planned world chart, task prompt, and any task-level files.
- The world should test synthesis across documents rather than outside medical lookup.
- Major recurring information domains:
  - Steroid timeline
  - HF/AKI medication changes
  - Functional/cognitive status
  - Consultant timing
  - Infection improvement versus persistent symptoms
  - Discharge safety

## Needs Physician Decision

- For each task, define the exact facts a correct answer needs.
- For each fact, identify whether it comes from Clinical History, world-level files, task-level files, or prompt context.
- Identify facts that should remain uncertain and how a correct response should acknowledge uncertainty.
- Determine whether any task requires a task-level file.

## Source-Of-Truth Rule

- Every clinical fact in any task's expected output must trace to the Clinical History narrative or a file in the World File Plan.
- Anything not traceable should be acknowledged as uncertain.
- The Expected Output for each task must be precise enough for consistent grading.

## Reviewer / AutoQC Risk

- A reviewer may reject a task if a seasoned clinician could not solve it from supplied files alone.
- If a correct answer relies on unstated clinical judgment or missing facts, the task becomes unfair.
- If one file contains all answer-critical facts, synthesis burden may be too weak.

