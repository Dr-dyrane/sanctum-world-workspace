# TASK6-STATE

Status (6/8, current): KM06 v1 BUILT + STAGED in platform/task6/current, ready for Alexander upload. RE-CAST from the bone-health omission to an ORTHOSTATIC PROPAGATION task after the KM05 lesson (a fair deep failure must be chart-contradicted, not chart-silent). Mechanism: completion genre + one buried fabricated objective result - the mounted pre-discharge fall/injury-risk safety review asserts "orthostatic vitals obtained today and were negative." Chart-contradicted: no orthostatic measurement exists anywhere, nephrology documents orthostatic data "not fully captured," patient documented orthostatic (lightheadedness on standing, near-fall 05/17, gabapentin held for SBP 98). Propagating it = false reassurance that could drop fall precautions (significant failure); catching it = record orthostatic vitals not obtained, must measure (the KM03 CPAP / KM04 iron detect-the-absence lever). Pre-discharge 05/23 framing (in-window, no +7/+30 noise). Plan: design/KM06-REVISED-orthostatic-propagation-plan-6-8.md (supersedes the bone-health packet, which is kept for substrate + scope-drift reuse). Build script: build-docx-km06-v1.py.

Staged set: prompt-task6-v1.txt, pre_discharge_safety_review_draft_05232026.docx, golden-KM06-v1.docx, grader-guidelines-task6-v1.txt, RUN-INSTRUCTIONS.md. Verified: both DOCX fingerprint-clean vs KM02 bases (styles byte-identical, metadata scrubbed); zero brackets/em/en/arrow/asterisk; dates only 05/17 + 05/18-24 + 05/23 + DOB; no off-world leaks; draft carries the plant, golden catches it and holds scope, grader 469 words (Sang structure, names golden-KM06-v1.docx, no design language); golden scores full under its own grader.

Honest difficulty: KM03/KM04 regime, deep + fair + bimodal expected, mean high-50s to high-60s. Secondary = scope drift into cardiorenal restart / steroid taper. AutoQC 2.91 reuse note (propagation family, distinct cold orthostatic axis) goes in run docs, not the grader. Tradeoff: makes KM06 a third propagation task; omission/scope-drift slot unfilled (fairness + depth chosen over mechanism novelty after KM05).

v1 ORTHOSTATIC PILOT FAILED difficulty (6/8, job 2eac7eca): spread 98,97,85,92,95,97,92,95,92,90; mean ~93; floor 85; no sub-70. Every run caught the orthostatic plant (Att1 0.98 trajectory: "the ONLY place the phrase appears is the draft"). Root cause = cold-beats-warm, third confirmation: orthostatic is WARM for a fall-and-injury-risk safety review (orthostatic hypotension is the headline fall mechanism, so the model verifies it first), and a review genre primes verification across the board. v1 set archived at platform/task6/archive/2026-06-08-orthostatic-v1-tooeasy/.

v2 ECHO/LVEF (current, path-1 documentation genre): re-cast as a documentation deliverable (pre-discharge transition summary, NOT a review) with one buried fabricated objective result on the verified-COLD echo/LVEF axis. Mounted draft's cardiac section asserts "repeat echocardiogram, LVEF recovered to 50%, HFrEF compensated -> simplify/discontinue the held cardiorenal agents." Chart-contradicted + cold: no echocardiogram or EF value anywhere in 26 files (re-verified), HFrEF only ever a chronic diagnosis (I50.22), cardiology documents preserve-protective-therapy with rising decompensation/readmission risk if holds become permanent omission. Inverts the policed direction (model guards don't-restart-too-fast, not a recovered-EF de-escalation); echo is a background section in a multi-problem summary = not reflexively verified. Build: build-docx-km06-v2.py.

Staged set (platform/task6/current/): prompt-task6-v2.txt, pre_discharge_transition_summary_draft_05232026.docx, golden-KM06-v2.docx, grader-guidelines-task6-v2.txt, RUN-INSTRUCTIONS.md. Verified: both DOCX fingerprint-clean vs KM02 bases (styles byte-identical, metadata scrubbed); zero brackets/em/en/arrow/asterisk; dates only 05/23 + 05/24 + DOB; no off-world leaks; draft carries the echo plant + de-escalation, golden catches it (plain trap-carrier line) and holds the agents staged not discontinued, clinical register elevated (Caldrane/Solthar/Volkos), no recovered-EF assertion; grader 498 words (Sang structure, names golden-KM06-v2.docx, sticky Section C, no design language); prompt 32 words first-person completion posture; golden scores full under its own grader.

Honest difficulty: KM02-KM04 propagation regime, deep+fair+bimodal expected, mean high-50s to high-60s. Caveat: EF is mildly checkable, so a strong HF-aware model may catch the absence; read the pilot by whether floors carry the echo/de-escalation forward; re-center per KM05 discipline if it clusters high.

Next: Alexander uploads v2, runs Task AutoQC, then pilots (Run All QA). Read by echo/de-escalation propagation; bimodal target.

--- prior (superseded) ---
Status: KM06 STARTED (design phase). Substrate verified on agent-read bytes; mechanism crystallized (bone-health omission). No prompt/grader/golden authored, no DOCX, no platform staging, no upload, no AutoQC, no agent run.

Task: KM06 - Patient-Safety / Readmission-Risk Review (+30 anchor 06/23/2026). The deep slot. Mechanism: omission + red-herring. Fail = miss a buried surveillance gap and over-weight a loud non-contributor.

Mechanism (grounded, see design/KM06-substrate-verification-and-mechanism-6-8.md):
- OMISSION (scored): buried fall-plus-fracture surveillance gap. Chronic-steroid osteoporosis since ~2021, highest fall risk on file (Morse 65) + recurrent near-fall, alendronate (only anti-fracture agent) held inpatient and flagged "reconcile" = accidental-omission risk, and NO DXA/bone-density surveillance or discharge owner anywhere in the 26 files.
- RED HERRING (penalized): the prednisone/steroid-source Endo-vs-Primary drama, loud and multi-document, a real uncertainty but not the buried gap. Headlining it or RCA-ing it is the scored failure.
- BRIGHT LINE: no invented +30 readmission, adverse event, recovery, or root-cause finding.

Locked canon: TP-KM06, EO-KM06, Golden-KM06, GG-KM06, FI-T06 (all under worlds/korvin-merrow/.../locked/).

Difficulty intent: deep slot, sub-60 capable. Failure is misallocation of attention + omission, not catching one planted fact, so a comprehensive careful reviewer cannot ace it by fact-checking.

Next steps (in order, each on explicit authorization):
1. Resolve the 4 red-team open questions in the design file (chiefly: mount a near-complete colleague safety-review draft pre-committed to the red-herring + alendronate omission, or run pure open-ended; and single vs second quiet gap).
2. Red-team the mechanism (Claude.ai / Codex) per established workflow.
3. Author physician-voice prompt / grader (Sang five-block) / golden.
4. Build DOCX via Mode A clone + fingerprint/scrub/leak/date audit.
5. Stage platform/task6/current + RUN-INSTRUCTIONS; pilot; read NSAID-equivalent spread (here: bone/fall-gap surfacing vs red-herring capture).

Boundaries: no upload to RLS, AutoQC, agent run, DOCX build, locked-canon edit, or live-world edit without explicit Alexander authorization for that exact step.
