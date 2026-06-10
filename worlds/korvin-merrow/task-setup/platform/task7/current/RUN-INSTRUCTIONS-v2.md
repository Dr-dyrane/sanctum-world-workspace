# RUN INSTRUCTIONS - KM07 v2
## Workflow type: Specialist Referral Letter and Documentation Preparation
## Task: KM07 - Nephrology referral letter completion, bone-health false closure (05/26 anchor)

---

## PLATFORM HYGIENE FIRST (required before any v2 entry)

The v1 platform task ran with **27 files visible** (26 world + the orphaned `draft_task7.docx` that the from-scratch prompt never referenced). Before entering v2:

1. Remove `draft_task7.docx` and any other v1 task files from the platform task.
2. Replace prompt, draft, golden, grader with the v2 set below.
3. After entry, confirm the agent-visible file count = 26 world files + 1 mounted draft.

v1 evidence preserved at `archive/2026-06-10-v1-fromscratch-tooeasy-93.8/` (pilot job 67e254b4, mean ~93.8, zero sub-90, BANNED too-easy). v1 defects logged in `task7/design/KM07-v2-PLAN.md`, including the future-dated golden (06/23/2026) - do not reuse any v1 artifact.

---

## Upload sequence (Alexander operates)

1. **Workflow type** = Specialist Referral Letter and Documentation Preparation (P0; verbatim sheet string)
2. **Prompt**: `prompt-task7-v2.txt` (in-world today 5/26)
3. **Mount draft**: `nephrology_referral_letter_draft_05262026.docx`
4. **Golden**: `golden-KM07-v2.docx` (upload as file)
5. **Grader**: `grader-guidelines-task7-v2.txt` (paste)
6. **Task AutoQC** - rerun N failing only
7. **Pilot** (10 trajectories)

---

## How to read the pilot

- **Propagates the bone closure** (letter asserts alendronate continued / bone health current) = scored failure; expect ~0.10-0.40
- **Keeps alendronate open** (not administered inpatient, reconciliation pending, confirm renal trajectory before resumption) = correct catch; expect ~0.85-0.95
- Restart framing should stay open in nearly all runs (the draft already has it correct); a run that flips it to "ready to restart" fails on the secondary pattern

**Target shape:** KM02-class bimodal. If it clusters high, tighten the bait only (quieter phrasing, deeper in the med paragraph); do NOT add a reconcile clause; do NOT touch the grader.

---

## Mechanism summary

PCP (Talia Quenor, MD) starts a referral letter to Dr. Iven Solthar on 05/26 (two days post-discharge; post-snapshot; nephrology's 1-2 week follow-up window still live). The draft is correct everywhere, including the open staged-restart framing, except one quiet line in the medication paragraph: alendronate 70 mg weekly (Sundays) "continued through the admission; bone-health therapy is current with nothing outstanding on reconciliation." The MAR states it was NOT administered inpatient (outpatient chronic, reconcile) and the med-rec keeps bone-health reconciliation pending. Bone axis present in 9 of 26 files; no prior task uses it. Cold axis + quiet plant + completion wrapper = the only mechanism class that floors on this chart (five-pilot evidence in KM07-v2-PLAN).

---

## Gates before entry

1. **2.106 adjacency vs KM02 (false-closure family): PENDING Alexander's explicit call.** Different capability (med continuity/bone vs infection status) and artifact (referral letter vs discharge summary).
2. Anchor: CLEAR (05/26 post-snapshot, past-dated).
3. Workflow string: CLEAR (verbatim on P0 sheet).
4. Abi variety tradeoff: artifact variety preserved, wrapper reused; flag honestly in run notes / pod thread.
5. **MOUNTED-SET LISTING (standing gate, fired twice now): PENDING.** Pull the v1 trajectory's find output or the platform task-file view and confirm the 27th file was draft_task7.docx (records what the 93.8 actually measured). After v2 entry, verify the agent-visible set = 26 world files + nephrology_referral_letter_draft_05262026.docx, BEFORE pilot. No pilot on an unverified mounted set.
6. **ATTEMPT 5 TRANSCRIPT (read-the-grader rule): PENDING.** Pull the 0.90 floor's grading transcript before the v1 record states "no failure mode at all"; at 90 it is near-certainly grader jitter, but confirm and note it in the v1 archive README.

---

## Build hygiene record (v2, 6/10)

- Both DOCX: Mode A clones of KM02 bases; fingerprint diff EMPTY; metadata scrubbed; correct footer labels ("Nephrology Referral Letter - Draft" / "Nephrology Referral Letter"); band Date 05/26/2026; rendered to PNG and visually verified
- Every medication dose byte-verified against the med-rec note; alendronate 70 mg weekly (Sunday) verified against the MAR verbatim
- Build script pattern: /tmp/build_km07_v2.py (heredoc, mount-truncation discipline)

---

## Boundaries

No upload, AutoQC, agent run, QA response, FA/GA, PL, or RLS mutation without explicit Alexander authorization for that exact step. Alexander reads and owns prompt + golden wording before entry.
