# 1b - Internal-medicine trap library (the pick-from menu)

A trap is the forced move the model's competence plays wrong. This is the catalog of internal-medicine trap archetypes proven or scoped across Korvin Merrow, each tagged to the structures it arms and the fairness rule that keeps the floor bankable. Choose one trap per bite-carrying task. Full doctrine: `docs/task-difficulty-lessons.md` (sections 5-6 fairness), `docs/task-structure-dossier.md` (forcing functions).

## How to read each entry

Arms = which structures (S1-S8) the trap fits. Fairness basis = why flooring it is the model's own fault. Clears (too easy) when = the conditions under which the trap stops biting, so you can avoid building those in. KM example = where we have seen it.

## The cardinal fairness law (every trap must pass this)

Floor only on a wrong move that is the MODEL'S OWN fault. The prohibited pattern: a false claim planted in the model's OWN same-author draft with no instruction to correct it. That is unfair and Abi retires it. To use any "contradicted by the chart" trap inside a draft the model finalizes, either (a) the prompt tells the model to correct errors, or (b) the draft uses a true placeholder for the model to complete, or (c) the contradicting claim lives in a DIFFERENT-author, wrong-by-genre document (see trap 6). Prefer (b) and (c); a reconcile-and-correct prompt is a difficulty killer on propagation mechanisms.

---

## 1. Severity-anchoring / over-capture (central KM bite)

The model documents or codes to the most severe framing the chart hints at, rather than what the record establishes. Arms: S2, S3, S5. Fairness basis: the eager, helpful action is the wrong one; the chart documents only the lesser, so the over-reach is the model's own. Clears when: the cautious answer is the free default with no severity pressure, or the over-capture is a loud recall-level contraindication the model declines for free. KM example: KM09 sepsis-to-principal, KM10 metabolic-encephalopathy confirmation.

## 2. Undocumented MCC/CC capture

Adding a complication or comorbidity (metabolic encephalopathy, acute-on-chronic heart failure, hyperkalemia-as-diagnosis) that the chart describes as a symptom or risk but never establishes as a diagnosis. Arms: S2, S3, S5. Fairness basis: documented ABSENCE plus the chart affirmatively qualifying the finding (for example altered mental status coded at symptom level, never escalated). Clears when: the chart is merely silent rather than contradicting; silence is not enough, build an explicit qualification. KM example: KM09/KM10 G93.41, I50.23.

## 3. Premature restart / over-advancement

Resuming a held medication or therapy that the chart explicitly defers to a staged, parameter-gated, or outpatient decision. Arms: S1, S6-with-forced-slot. Fairness basis: the chart explicitly defers (staged restart, consultant sequencing), so advancing it is contradicted. Clears when: the deferral is weak or the model can frame a lab-gated restart as compliant; make the deferral explicit and multi-source. KM example: KM05 cardiorenal restart.

## 4. Suspected-at-discharge mis-application

The model runs a real coding or documentation rule in the WRONG direction, for example using "a condition still suspected at discharge is coded as established" to escalate to sepsis instead of to support the documented urinary-source infection. Arms: S2, S3. Fairness basis: the rule supports the lesser, documented condition; escalation overstates severity and claims an unsupported DRG family. Clears when: the rule's correct application is obvious; bury it behind a tempting higher-severity candidate. KM example: KM09.

## 5. Off-text / multimodal miss

A discharge-relevant finding lives in a non-prose artifact (bedside photo, handwritten list, scanned form, image) while the text frame pulls toward a different, benign narrative. Arms: S1, S3, S6. Fairness basis: the prompt names the artifact (not a hidden gotcha); missing it is an omission under a strong distractor, the model's own under-attention. Clears when: the agent runtime or grader cannot see the artifact (then the task is impossible, not hard) - confirm agent AND grader can perceive it before banking. KM example: KM08 v7 plantar foot-wound photo. Build prerequisite: self-contained artifact, agent-visible, grader-visible.

## 6. External-authority deference (the fair adversarial lever)

An outside party (payer denial, CDI query, HIM coder worksheet, night-float signout, prior-auth reviewer) has committed a wrong-but-plausible position; the model defers to it instead of rebutting from the chart. Arms: S3 natively; S1 via a mounted adversarial input. Fairness basis: the document is wrong-by-genre and authored by a DIFFERENT role, so it needs no placeholder fix and is fairly rebuttable; physician judgment exists precisely to catch it. Clears when: the document's position is obviously wrong, or the chart does not actually rebut it; ground the wrong position in real chart ambiguity. KM example: KM01 pharmacy handoff, KM08 v7 signout, KM09 v2 coder worksheet, KM10 CDI query.

## 7. Result-dependent / pending-data over-assertion

The model asserts a value that the chart shows is still pending (an organism code while cultures are pending, a final lab not yet resulted). Arms: S2, S3, S5. Fairness basis: the chart documents the data as pending; asserting it is fabrication. Clears when: the pending status is ambiguous; make "pending at record close" explicit. KM example: KM09 no organism code.

## 8. Near-miss measure logic

In abstraction, the model applies the wrong exclusion, lookback window, denominator, or numerator because the chart quietly contradicts the obvious read. Arms: S5. Fairness basis: a single quiet disqualifier in the documentation that the measure logic requires. Clears when: there is no quiet disqualifier; build exactly one. KM example: scoped, not yet built.

## 9. False closure of an open item

The model asserts that an unresolved reconciliation item is closed or current (a held home medication "continues on schedule," a bone-health agent "resumed"). Arms: S1, S2. Fairness basis: the chart documents the item as not administered or pending reconciliation. Clears when: the item's open status is not clearly documented. KM example: KM07 alendronate closure.

## 10. Borderline determination

A verdict task (inpatient-vs-observation, LOS, medical necessity) where the model picks the wrong side. Arms: S4 only. Fairness basis: the case is DESIGNED borderline with a genuine criteria split. Clears when: the case is not actually borderline (a fixed, unambiguous world makes the verdict free, KM08 v3 at 0.96). Build prerequisite: design the ambiguity in (two-midnight split, criteria on both sides).

## 11. Single-cause attribution (variety slot, mid-high)

In an investigation or review, the model adopts a single-cause framing that the chart contradicts with a multifactorial picture. Arms: S7. Fairness basis: the chart documents multiple contributors; a single-cause conclusion is unsupported. Clears when: review genres are anti-cold (the whole document is verification mode), so predicted mid-high, not a deep floor. Use as a variety slot.

---

## Cross-cutting build rules for any chosen trap

- Cold/background axis only. The deliverable's own headline subject is warm and the model is already hunting it; put the trap on a cold secondary axis.
- Contradiction or mandate, never silence. Floor only where the chart explicitly contradicts the wrong move or mandates the right one.
- Same-encounter. Put the forced judgment inside the encounter the chart governs; a post-chart +N-day claim is propagated or declined for free.
- One forced slot. The deliverable schema or a mounted adversarial input must force the move; from-scratch synthesis (S6) has no native force.
- Reachability. The correct restraint must be reachable: plan for a live catcher, or prove the golden self-scores high under its own grader.
- Legitimate-failure bar (King). The failure must materially degrade the deliverable or create patient-harm, compliance, or malpractice exposure. Cosmetic misses do not count.

Next: `1c-trap-pairing-and-fairness.md`.
