# 2b - Spec-prep checklist with KM reviewer-correction inheritance (Ondina Vasquell world)

Purpose: the complete World Spec preparation map, pre-loaded with every correction a reviewer or AutoQC actually issued on World #1, so World #2 pays for none of them twice. Clinical values are Alexander's; cells marked OPEN FOR ALEXANDER stop the build until he supplies them. Companions: reference/checklists/spec-autoqc-preflight.md (the 113-check map), reference/world-spec-guidelines/09 (writer playbook), 2c in this folder (2.5 defenses).

## A. Inherited reviewer corrections (each cost KM a round; pre-satisfied or pre-planned here)

| # | KM correction (source) | World #2 inheritance | Status |
|---|---|---|---|
| A1 | Patient name unmistakably fictional (Stacey A1; James Carter rejected) | Ondina Vasquell locked, consistent everywhere, non-generic, non-trademarked | DONE 6/12 |
| A2 | Comorbidity expansion (Stacey send-back: approved expansion required) | Brainstorm patient profile expanded beyond 10 interacting common conditions: insulin-dependent T2DM, diabetic peripheral neuropathy, mild diabetic retinopathy, CKD 3b, anemia of CKD, PAD, HFpEF, hypertension, dyslipidemia, obesity, OSA, knee osteoarthritis, and limited mobility. Spec phase must keep these coherent and common, with no rare-diagnosis stack and no invented medication doses | DONE 6/12 |
| A3 | Medication specificity (Stacey send-back: every med with dose, route, frequency, indication; KM medication-expansion package precedent) | Full home list with dose/route/frequency/indication for every drug, insulin regimen in full detail, temporally labeled lists (home baseline vs inpatient MAR vs discharge). No invented doses: any value not supplied by Alexander is flagged NEEDS APPROVAL and blocks (workspace-guardrails lesson 5) | OPEN FOR ALEXANDER |
| A4 | World-type and identity fixes (Stacey) | Header table single values: typical clinical world; Ondina Vasquell; inpatient; hospital medicine; 10 tasks; version; date | Templated, fill at spec |
| A5 | No project-artifact field names in clinical files (Abi, Task 1: the Date / Anchor lesson) | Mode A HIM/EMR templates use real clinical headers only (Date of Service, Hospital Day, Encounter Date) | Doctrine locked (decision 9) |
| A6 | Task files must not teach the answer (Abi, Task 1) | Task-context files exist only when realistic, necessary, non-duplicative; defaults to none | Carried into 1c/1d |
| A7 | Golden as realistic clinical document (Abi, Task 1: DOB, MRN, allergies, signature blocks) | Inherited into Phase 3 per-task checklist | Carried |
| A8 | FA/GA failure-only, no section names; three PLs per task; descriptive QA annotations (Abi 6/9 onward) | Inherited into Phase 4 gates | Carried |

## B. Identity package (arithmetic gates 2.8 to 2.15, 2.100)

- DOB consistent with age 68 at the 5/21/2026 snapshot: born between 5/22/1957 and 5/21/1958. Exact DOB: OPEN FOR ALEXANDER.
- MRN clearly synthetic, non-institutional format (KM precedent KM-6427819 style; suggest OV-prefixed). OPEN FOR ALEXANDER.
- Anthropometrics arithmetically self-consistent (height, weight, BMI recomputed, not asserted). OPEN FOR ALEXANDER.
- Allergies row populated (or explicit None). OPEN FOR ALEXANDER.
- Code status populated; if reaffirmed at a family meeting, date it in milestones. OPEN FOR ALEXANDER.
- Language and interpreter realism: Spanish-preferred documented consistently; interpreter use or bilingual provider noted where notes imply direct history-taking.

## C. Care team roster (2.26, 2.27, 2.97)

- Every named provider: Name with consistent Dr.-period formatting, credentials, role, service; primary team plus every consulting service named anywhere (hospital medicine, podiatry, vascular surgery, ID, nephrology if consulted, endocrine or diabetes educator, wound care RN, PT, OT, pharmacy, case management, CDI specialist, HIM coder, payer medical director as external correspondent, daughter as caregiver).
- All names unmistakably synthetic, collision-checked across this world AND the KM corpus (grep both); no near-duplicates.
- Names: OPEN FOR ALEXANDER (Claude may propose candidate sets for his pick, mirroring the patient-name flow).

## D. Timeline and milestones (2.20 to 2.23, 2.41, 2.76, 2.92)

- Key Milestones table, MM/DD/YYYY, chronological, every date used anywhere in the spec present, zero orphans.
- Required rows already fixed by decisions: roughly 3-week prodrome (late April 2026), admission 5/16/2026 (HD1), debridement day (HD2 or HD3: OPEN FOR ALEXANDER), ABI/TBI study day (OPEN), MRI day (OPEN), snapshot 5/21/2026 18:00 stated explicitly, then the ten task anchors (already locked in Brainstorm v1.1, earliest 5/22 08:30).
- No world document dated after any task anchor it serves; nothing future-dated.

## E. Section 1 content gates

- 1.1 Big Picture: patient-first hook; states 10 tasks; names the integration anchor task explicitly (candidate: Task 4 payer appeal, which draws the widest chart synthesis; OPEN FOR ALEXANDER); states file-plan composition X + Y + Z = N.
- 1.2: home med list (A3), temporally labeled lists (2.13), Decision Friction Table IN 1.2 (KM placement lesson) with Friction/Options/Correct Pathway, data hierarchy note (MAR and signed orders above attending/consult notes above progress notes above outside records above patient or family report; the perfusion conflict resolves by this note).
- 1.3 Clinical History: continuous prose, dense enough for a non-domain builder; covers arrival context, progression, workups, surgical history (explicit none if none), transitions, snapshot status.
- 1.5 Complexity: at least two interacting dimensions; difficulty distribution sentence (from 1d forecasts).

## F. File plan gates (2.42 to 2.52, 2.82 to 2.96, 2.113)

- At least 30 world-level files (in-doc AutoQC rule per the 6/12 delta memo); approximately 90/10 essential to supplementary; at least 4 modalities (carry 4, not the live doc's softer 3).
- Origin tokens per decision 9: Custom Made default; Writer Produced File for media; filenames lowercase_underscores_MMDDYYYY.ext matching milestones; IDs four-way unambiguous, monotonic.
- No answer-key synthesis in shared world files (Raising Task Difficulty rule): no final discharge summary, no ID final antibiotic plan, no vascular final recommendation, no coding/CDI conclusions at world level; those surfaces are task-level where a task needs them.
- Writer-produced media rows carry FINAL upload filenames.

## G. Media prompt specs for Codex imagegen (decision 10; write at file-plan time)

Each image prompt must specify: exact clinical content and severity, anatomic view and framing, lighting and background realism, an embedded or implied date marker where realistic, explicit absence of faces, tattoos, jewelry, and identifying marks, target filename (final, MMDDYYYY), the minimal chart clue that references the image, and the post-generation verification: render check, banned-content check, agent-visible and grader-visible confirmation before any pilot interpretation. Planned images from the canvas: bedside wound photo (substrate only, never the headline trap), scanned ABI/TBI tracing, medication bottle label, home glucose log photo.

## H. Formatting and submission bans (every one bit KM once)

MM/DD/YYYY display dates everywhere including DOB; zero em dashes, en dashes, arrows; no letter-O "PO" token, write Oral; zero asterisks; American English; landscape where wide tables need it; page numbers; single .docx with companion content inline; spec filename Alexander_World_Vasquell_latest_M_D.docx; uploads individually, never zipped; rerun only failing AutoQC checks, never full reruns.

## I. Order of operations from here

1. Alexander supplies A2, A3, B, C, D open values (one sitting, same shape as the Brainstorm blockers).
2. 2a arming map filled from the canvas trap ledger against the now-real timeline.
3. Spec drafted per the official template; self-QC against the v6.3 index; 2.5 notes from 2c held ready.
4. Mode A HIM/EMR reference templates built per doctrine; media prompts handed to Codex imagegen.
5. Upload, AutoQC, remediate, pod review, on Alexander's explicit authorization at each platform step.
