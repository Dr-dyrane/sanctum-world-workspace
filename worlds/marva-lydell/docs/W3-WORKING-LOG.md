
## 2026-06-20 - W3 submission preflight fixes (Alexander)
Acting on the readiness audit, five writer items:
1. CMS WS2 form (discharge_rights_notice_06192025.pdf): download guidance given to the writer (CMS-R-193 Important Message from Medicare, public domain). Writer downloads, scrubs metadata, names it, drops it in world-files/files. Not placeable from here (file-download restriction; cannot curl/wget).
2. Task 4 tier conflict resolved: Priority P0 -> P2 to match the Peer Review Case Analysis category. Distribution now 7 P0 / 2 P1 / 1 P2 (at least one P0 holds). Task 6 stays P0.
3. Section 1.3 long-form dates -> MM/DD/YYYY (06/13/2025, 06/19/2025).
4. World Summary trimmed 6 -> 4 sentences (preflight wants 3-5); redesign note condensed to one sentence.
5. File-plan Pearls/Traps column: added the exact "Anchors Task N <trap> trap" annotations on the 14 trap-carrying world-level rows (rubric cross-checks Failure Design anchors against this column).
Spec rebuilt, gate clean (fingerprint matches base), 0 dashes. Commits 6bdec26, b67c3cb. Pushed origin/korvin-merrow-brainstorm.
