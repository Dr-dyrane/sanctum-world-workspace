
## 2026-06-20 - W3 submission preflight fixes (Alexander)
Acting on the readiness audit, five writer items:
1. CMS WS2 form (discharge_rights_notice_06192025.pdf): download guidance given to the writer (CMS-R-193 Important Message from Medicare, public domain). Writer downloads, scrubs metadata, names it, drops it in world-files/files. Not placeable from here (file-download restriction; cannot curl/wget).
2. Task 4 tier conflict resolved: Priority P0 -> P2 to match the Peer Review Case Analysis category. Distribution now 7 P0 / 2 P1 / 1 P2 (at least one P0 holds). Task 6 stays P0.
3. Section 1.3 long-form dates -> MM/DD/YYYY (06/13/2025, 06/19/2025).
4. World Summary trimmed 6 -> 4 sentences (preflight wants 3-5); redesign note condensed to one sentence.
5. File-plan Pearls/Traps column: added the exact "Anchors Task N <trap> trap" annotations on the 14 trap-carrying world-level rows (rubric cross-checks Failure Design anchors against this column).
Spec rebuilt, gate clean (fingerprint matches base), 0 dashes. Commits 6bdec26, b67c3cb. Pushed origin/korvin-merrow-brainstorm.

## 2026-06-20 - WS2 reference file placed
Writer uploaded the CMS-R-193 Important Message from Medicare (public domain). It is the January 2003 OMB version (OMB 0938-0692), whose only printed date is the form revision "January 2003", pre-cutoff, so no post-June-2025 date appears on the artifact. Scrubbed PDF metadata (removed XMP stream and the document-info Author/Creator/Producer/2003 CreationDate/ModDate), saved with a deterministic id, named discharge_rights_notice_06192025.pdf, placed in world-files/files. world-files/files now holds 23 reference files; the Reference Templates folder is complete.

## 2026-06-20 - W3 Spec AutoQC round 1: 2/28 fails cleared
AutoQC (2.4) returned Fail 2/28. Both resolved in the spec and docx:
1. Temporal Architecture / Date Format: Section 3 intro carried one ISO date "(Template Curation, 2026-06-20)". Reformatted to MM/DD/YYYY (06/20/2026). No other ISO dates anywhere in the document.
2. Task Portfolio / Workflow Labels and Distribution: the header Table 0 workflow list was stale after the Task 4 redesign. It still listed retired labels "Transition Documentation" and "Acute Care Discharge Planning" (unused) and omitted Task 4 "Peer Review Case Analysis" and Task 5 "Post-Acute Care Coordination". Reconciled the header list to the nine distinct lanes the ten tasks actually run (Claims Appeal serves Tasks 1 and 7) and corrected the "ten approved workflows" claim to "nine". Header now lists nine, each maps to a task, none unused.
Rebuilt, gate clean (fingerprint matches base), zero dashes, zero ISO dates. Commit 474e7a9. Writer re-uploads the docx and uses Rerun 2 failing.
