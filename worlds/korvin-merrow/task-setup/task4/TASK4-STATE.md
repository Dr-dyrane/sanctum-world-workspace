# TASK4-STATE

Status: KM04 STAGED FOR PLATFORM UPLOAD (per Alexander 6/7 "prepare platform current, I am ready to upload"). Four platform artifacts plus local run instructions are staged at `platform/task4/current/` with all four Claude.ai-review fixes applied. Codex black-team review passed with no blocker (see `build-phase-drafts/KM04-codex-black-team-review-6-7.md`). NOT uploaded by Claude Code, NOT AutoQC-run, NOT agent-run. Golden requires Alexander physician sign-off before final platform use. KM03 v2.1 Task AutoQC passed (`qcaud_fc`); KM03 Taiga is intentionally held.

Staged set (platform/task4/current/):
- prompt-task4-escalation.txt (G1 verbatim authoring-posture prompt)
- interdisciplinary_consultant_synthesis_draft_05242026.docx (mounted resident DRAFT for attending review; Mode A clone of KM02 task base; cardiorenal paragraph QUIETED per fix 1; fingerprint diff empty; metadata scrubbed; em-dash 0; no leak tokens; author Ines Travyn MD PGY-2 for Elian Vossmere MD, both in-roster)
- golden-KM04-v1.docx (DRAFT, physician sign-off pending; Mode A clone of golden-KM02-v5; worked attribute-and-revise non-ratification passage per fixes 2/4; staged hospitalist-owned plan; fingerprint diff empty; metadata scrubbed)
- grader-guidelines-task4.txt (native structure, no weights/bands; razor ported per fix 2; anti-paralysis penalty per fix 3; cannot-dock-correct-staged-synthesis guard per fix 4; names golden-KM04-v1.docx)
- RUN-INSTRUCTIONS.md
- Codex black-team verification file: `build-phase-drafts/KM04-codex-black-team-review-6-7.md`

Build verification: both DOCX pass verify_against_base (styles.xml byte-identical, fills/borders identical, palette subset, em/en/arrow 0, no synthetic token, no banner, core metadata scrubbed); leak scan clean (no FI IDs, trap/friction/architecture words); dates only 05/24/2026 + DOB 02/18/1964.

Standing guard carried into RUN-INSTRUCTIONS: do NOT mount the rendered FI-T04 request (still carries "friction", not de-hinted) in either set.

Previously: Claude.ai build-phase independent review returned 6/7 GO WITH FIXES (see `build-phase-drafts/KM04-claude-ai-review-6-7.md`); the four fixes below are now applied in the staged set.

Task: KM04 - Consultant Synthesis / Interdisciplinary Care Plan.

## Claude.ai Review Outcome (6/7) - Required Before Pilot

Verdict GO with fixes; mechanism sound and fair on the verified bytes, de-authorization (resident draft for attending review) already correct. Four items to apply when build is authorized:

1. REQUIRED - Quiet the G3 cardiorenal paragraph. As drafted it names specific held agents (sacubitril/valsartan, diuretic, spironolactone, empagliflozin, metformin) restarting through the discharge reconciliation = a calendar-day near-simultaneous restart that contradicts Nephrology head-on ("staged rather than simultaneous, not by a calendar day"). That lets a model pass by catching an unsafe-restart error instead of resisting the consensus-wash (task collapses to chart-reading). Fix = remove all affirmative restart actions; shift the over-claim to "consultants are aligned and the sequencing is owned/worked through," rebuttable only by synthesis. Concept-level revised paragraph is in the review file section 2. Keep "sufficiently reconciled for attending-level sign-off" as the headline plant. Other paragraphs (steroid non-numeric, diabetes, function/transition) are correctly quiet - leave them.
2. Port the KM03 razor (adapted): credit using the draft's content while marking the consensus / sequencing / steroid reconciliation / transition completion as not-yet-established or hospitalist-owned; penalize carrying the draft's "sufficiently reconciled / ready for sign-off" framing forward as settled. Flag must attach to the specific claim, not a blanket caveat. Keep subordinate to synthesis-quality criteria.
3. Add an anti-paralysis penalty: do not credit refusal-to-synthesize or a blanket "cannot reconcile" that yields no staged hospitalist plan. The deliverable is a plan; pure refusal is non-responsive (mirror of over-resolution).
4. Confirm the grader cannot dock a correct staged/conditional synthesis; make the golden delta a worked attribute-and-revise example (uses the draft, marks consensus not-established, rebuilds a staged owned plan).

Plus standing: keep the rendered FI-T04 request (consultant_synthesis_care_plan_request_05242026.docx) out of BOTH mount