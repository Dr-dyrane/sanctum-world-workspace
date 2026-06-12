# Ondina Vasquell World (World #2) - Cockpit

Status: PHASE 1 SUBSTANTIALLY COMPLETE. Brainstorm v1.1 at the DOCX gate. World folder authorized by Alexander 6/12 late, superseding the planning-canvas scope lock. No substrate file, task artifact, DOCX, image, upload, AutoQC run, or platform action without Alexander's explicit authorization for that exact step.

Patient: Ondina Vasquell, 68F, Spanish-preferred, insulin-dependent T2DM, CKD 3b, PAD, diabetic neuropathy, HFpEF, limited mobility; second-floor walk-up; daughter support limited by night work; Medicare Advantage with Medicaid secondary. World: limb-threat diabetic foot infection, 6-day admission, snapshot May 21, 2026 at 18:00 (HD6 evening), medically improving but operationally unsafe. Branch posture: decision 7, stay on korvin-merrow-brainstorm until KM closes; cut ondina-vasquell-brainstorm at that boundary.

## Read order for this world

1. reference/workflows/next-world-dfi-decision-record-2026-06-12.md (physician-originated decisions 1 to 10)
2. reference/workflows/next-world-dfi-brainstorm-draft-v1.1.md (Brainstorm of record, twice reviewed, residuals fixed)
3. reference/workflows/next-world-dfi-hour-prep-packet.md (options history, worksheet sources, live-guidance gate)
4. reference/workflows/live-guidance-delta-memo-2026-06-12.md (live doc and sheet verification; Phase 2+ residual gates)
5. This folder's phase files in numbered order.

## Standing build doctrine for this world (Alexander, 6/12)

1. TRANSCRIPT (decision 8): the submission transcript is assembled at the end from git history plus the decision records. Every design decision must therefore land in a committed file with provenance; the git log is the capture mechanism. Sanitize at assembly per KM lessons: no dashes, no internal workspace labels, no benchmark register.
2. REFERENCE FILE ORIGIN (decision 9): default origin token is Custom Made for writer-drafted document templates; we maintain the KM Mode A HIM/EMR design system (worlds/korvin-merrow/reference-file-design/epic-note-design-system.md) across all world files. Writer-produced media keep the Writer Produced File token and final upload filenames at spec time.
3. DOCX GENERATION: every DOCX uses the EVOLVED KM doctrine, never first-principles building. Brainstorm DOCX clones worlds/korvin-merrow/submission/Korvin_Merrow_Brainstorm.docx Mode A. STRUCTURE MAP, verified on the base bytes 6/12: title paragraph (Ondina Vasquell World Brainstorm), date paragraph, then ONE 5x3 table with header Element / Ondina Vasquell submission content / Submission details. The four elements are cell text, not document sections: numbered items in-cell, traps with Type: prefixes, tasks as numbered blocks carrying Workflow mapping plus requester, structure, forced slot, task-level trap, and anchor lines; the World Type: Typical Clinical World declaration is the first line of the World setup cell; column 3 carries one-line per-row summaries; no nested tables. Content source is the submission markdown; assembly only translates layout. World files clone the locked KM bases. styles.xml byte-identical, core metadata scrubbed, fingerprint diff to zero, banned-character scan across ALL xml parts including footers, render to PNG and visually verify, integrity gate after every save. Full method: docs/docx-generation-method.md, AGENTS guardrail 1.
4. IMAGES (decision 10): image creation is delegated to Codex imagegen, which has file access and world context. We hand it a detailed per-image prompt spec (media section of phase-2-world-spec-and-substrate/2b-spec-prep-checklist.md). Every image must be temporally anchored, workflow-realistic, free of identifying features, supported by a minimal chart clue, and verified agent-visible AND grader-visible before any pilot leans on it (KM08 v7 vision-gate precedent).

## Deliverable map

| Deliverable | State |
|---|---|
| Brainstorm content, 4 elements, 10 tasks, 7 structures | v1.1 of record; awaiting Alexander read-and-own word and DOCX authorization |
| Brainstorm DOCX | Gated; Mode A clone build plan in doctrine item 3 |
| Brainstorm self-QC + AutoQC + pod review | After DOCX; Section 1 AutoQC prompt self-QC first |
| Claude transcript | Decision 8: assembled from git history at the end |
| World Spec | Phase 2; checklist at phase-2-world-spec-and-substrate/2b-spec-prep-checklist.md |
| AutoQC 2.5 intentional-ambiguity defenses | Drafted same-day per KM lesson: phase-2-world-spec-and-substrate/2c-autoqc-25-defense-notes.md |
| Reference templates, Custom Made, Mode A HIM/EMR | Phase 2/3 |
| Writer-produced media | Codex imagegen prompt specs at file-plan time |
| 30+ world files, 90/10 mix, 4 modalities | Source geometry board in the DFI canvas; arming map 2a at spec stage |
