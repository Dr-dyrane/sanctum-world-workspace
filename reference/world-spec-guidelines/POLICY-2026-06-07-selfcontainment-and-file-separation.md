# Pod policy 2026-06-07: self-containment (July-2025 cutoff) + world/task file separation

Source: pod-lead @channel announcement, 6/7/2026. Two rules that bind all new worlds and tasks.

## 1. Self-containment / knowledge cutoff (July 2025)
Treat the model as knowing nothing published after July 2025; platform real-time web search is OFF until further notice.
- A task's ASK and DELIVERABLE must NOT require public-domain knowledge published August 2025 or later (new clinical guidelines, FDA approvals, etc.). Example of what to avoid: a task that needs the model to know an FDA approval dated 01/12/2026, or to apply the 2026 AHA Acute Ischemic Stroke guidelines from memory.
- World-level and task-level FILES may still be dated in 2026 (progress notes, discharge summaries dated 01/01 to 06/07/2026 are fine). The restriction is on what the task requires the model to KNOW, not the dates stamped on documents.
- Workaround (use only when it reflects a realistic workflow): upload the actual post-cutoff source yourself as a world- or task-level file, then test whether the model can (1) extract the relevant information, (2) apply it correctly, and (3) justify the clinical reasoning. Good: "compare the 2026 and 2018 AHA stroke guidelines for my APPs, both attached." Bad: "treat this March-2026 patient using the latest guidelines" without attaching them (not self-contained, and self-attaching the guideline is not a realistic workflow there).
- Korvin Merrow check: KM01/KM02/KM03 are self-contained. They are standard multimorbid inpatient medicine (HFrEF, CAD, CKD, suspected urosepsis, prednisone-source reconstruction, discharge readiness) with no dependency on any guideline or approval published after July 2025. Future tasks must be checked against this before building.

## 2. World-level vs task-level file separation (now official; we lived this)
- When RLS asks for world-level files, upload ONLY world-level files, never task-level files. Keep the two in separate folders from the moment engineering hands the synthesized files back; the production pipeline may generate task-level files alongside world files, and it is on the writer to separate them.
- Upload task-level files ONLY during the tasking phase, inside their own task, and only after you have vetted them, made your revisions, and the reviewer or pod lead has signed off.
- Once finalized, world-level files do not change. If they are flagged with major concerns during tasking, tasking may be paused while they are fixed, because a world-level change forces every downstream step (trajectory runs, AutoQC, later pipeline phases) to be redone.
- This validates our holdback discipline: the 7 FI-T request files were correctly held out of the world (file-review/task-files-holdback/), the final world is 26 files, and Abi's "task files in the world" flag on 6/7 turned out to be a stale view, not a real contamination. Our instinct to verify against the live world before deleting, and to keep request files in non-upload holdback, was the right call and is now policy.
