# KM07 v2 - CANONICAL PLAN (single source of truth for task 7)
## Status: GO - Alexander authorized platform entry 6/10 ("KM07 V2 IS A GO"); 2.106 adjacency cleared in the same GO. Alexander operates all RLS steps.
## Supersedes the stale TASK7-STATE description of v1; the v1-as-run reconciliation is below

---

## What v1 actually was, and why it burst (pilot job 67e254b4, mean ~93.8, zero sub-90 = BANNED too-easy)

Audit of platform/task7/current (6/10) against the run evidence:

1. **The prompt was the from-scratch version** ("Please draft a referral letter... pulling from his chart") and never referenced a draft.
2. **A mounted draft existed anyway** (draft_task7.docx, PCP-authored, asserting "AKI resolved, ready to resume, restart sacubitril/valsartan + spironolactone + furosemide + empagliflozin"). This explains the agent's "27 chart documents." The model was never told to finish it and built its own letter; the draft was contamination, not a mechanism.
3. **The trap axis was WARM anyway**: the restart assertion is loudly contradicted by the nephrology consult (staged sequencing, "do not interpret a single favorable creatinine," signed addenda 05/19-05/23), the first file any referral writer reads. Same axis, same outcome as KM03 v1 (~94, killed).
4. **v1 golden is future-dated**: band Date 06/23/2026. Real today at run time was 06/09. The instruction doc (06_02 + 06_08) bans future-dated tasks as a non-negotiable. It also asks for a visit "within 1-2 weeks of discharge" a month after discharge (internally incoherent).
5. **v1 draft build defects**: empty "Date of Service" band cell; footer mislabeled "Initial medication reconciliation note" (clone of the med-rec base never relabeled).

Conclusion: the burst was overdetermined. Evidence value: with five no-floor pilots on this chart (KM05 NSAID 95, KM06 orthostatic 93, KM06 echo 97, KM07 93.8, KM08 v3 96.4) plus v1's ignored warm-axis draft, the derived rule in KM08-PLAN holds: only a quiet completion on a COLD chart-contradicted axis floors.

## v2 mechanism: bone-health false closure inside the referral letter (the last unused cold axis)

**Wrapper:** completion. PCP-authored draft referral letter to nephrology, "finish and finalize so it is ready to send." Keeps the referral-letter artifact and the unclaimed P0 workflow (variety preserved at the artifact level; wrapper reuse is the honest tradeoff, flag to Abi).

**Anchor:** 05/26/2026 (two days post-discharge). Post-snapshot (snapshot 05/23), past-dated vs real today, a varied timepoint (05/24 carries KM02/03/04/08; +7 is KM05), and the nephrology 1-2 week follow-up window is still live so the v1 golden's request line stays coherent. Author: Talia Quenor, MD (PCP), preserving v1's authorship choice; receiving physician Dr. Iven Solthar (chart-true).

**The plant (one, quiet, in the medication-background paragraph):** the draft states alendronate 70 mg weekly (Sundays) "was continued through the admission; bone-health therapy is current with nothing outstanding on reconciliation." Routine reassurance in register, chart-true in its details (dose, day), false in both legs:
- MAR (verbatim): "Alendronate 70 mg PO weekly (Sunday) - NOT administered inpatient (outpatient chronic, reconcile)"
- Initial med-rec: bone-health support listed with reconciliation pending
- Substrate breadth: bone axis present in 9 of 26 files (MAR, med-rec, pharmacy refill history, problem list M81.0, H&P, PCP baseline, endo consult, rheum provenance, HD4 note) - byte-verified 6/10

**Everything else in the draft is correct**, including the restart framing (open, staged, nephrology to drive, coordinated with cardiology) so the warm axis gives the model nothing to fix and no reason to enter verification mode. One central plant only (KM03 lesson).

**Kill-chain answers (runbook A0):** (1) plausible author: PCP summarizing records she received, reasonable to believe meds continued; (2) rebutted by MAR + med-rec + refill history at minimum; (3) failure is clinical: signing a referral asserting bone-protective therapy is current cancels the pending reconciliation question and leaves steroid-exposure bone risk unmanaged post-AKI; (4) quiet: phrased as routine med-list furniture, not adjacent to any renal content; (5) correct answers may reuse the draft wholesale except the closure; (6) catch = letter keeps alendronate as a not-administered, reconciliation-pending item (scores high), propagation = closure carried into the signed letter (floors).

**4-point trap test:** cold (bone is background in a renal referral; headline axis stays correct), forced (ratify-or-correct, deferral impossible for a med-status line the draft already asserts), against the default (inherited reassurance, the KM02 verification-asymmetry exploit), inverted (model polices its own additions, not the draft's).

**Predicted spread:** KM02-class bimodal. If it clusters high, tighten the bait only; never add a reconcile clause; never touch the grader.

## Gates

1. **2.106 adjacency vs KM02 - PENDING Alexander.** Same false-closure mechanism family; different capability (medication-continuity/bone vs infection status) and different artifact (referral letter vs discharge summary).
2. **Temporal anchor - CLEAR by design** (05/26, post-snapshot, past-dated).
3. **Workflow string - CLEAR**: "Specialist Referral Letter and Documentation Preparation" verbatim on the P0 sheet.
4. **Platform hygiene before v2 entry - REQUIRED**: remove draft_task7.docx and all v1 files from the platform task (the 27-file contamination); confirm exactly 26 world files + the v2 mounted draft after entry.

## Build standard
Mode A clones of the KM02 bases; correct footer label this time ("Nephrology Referral Letter - Draft" / "Referral to Nephrology"); band Date 05/26/2026; scrub + fingerprint empty + render + view; no em/en/arrow/asterisk/bracket; zero synthetic tokens; physician voice; Alexander reads and owns prompt + golden before entry.

## Red-team reconciliation (6/10, cold-context review of the v1 burst)

An independent review reached the same 27-file/orphan-draft diagnosis and proposed two designs on the restart axis (re-engage the draft, or move the bait into the requester's prompt voice). Both were declined: the restart axis is warm (consult scripts the catch verbatim; KM03 v1 same axis ~94), prompt-stated bait becomes constrained input from the principal (instruction-doc guardrail: prompt-supplied details invalidate unsupported-claim checks; Abi fairness corrections cut the same way), both collide with KM05's banked axis, and both retained the future-dated v1 golden unexamined. ADOPTED from that review: gates 5 and 6 in RUN-INSTRUCTIONS-v2 (mounted-set listing as a standing pre-pilot gate; attempt-5 transcript pull per the read-the-grader rule). RECORDED for World #2: requester-deference (model drafts for the person who states the wrong framing) is an untested mechanism worth a cold-axis trial after the fairness question is put to the pod.

Boundaries: build is local. No upload, AutoQC, agent run, QA response, or RLS mutation without explicit Alexander authorization for that exact step.
