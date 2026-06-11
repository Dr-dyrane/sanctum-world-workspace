# Abi-mode review: KM08 v4.1 staged packet - 2026-06-11

Scope: platform/task8/current/ read cold in protocol order: prompt-task8-v4.txt, neuropathic_pain_sleep_addendum_draft_05242026.docx (text extracted from the built bytes), golden and grader axis from the design record. Protocol: docs/abi-review-protocol.md. Trigger: the KM07 v3 post-mortem cleared KM10 by genre but never re-checked KM08, the other same-author completion task in the review queue.
Posture confirmations: read cold before opening golden/grader: yes. Built artifact read directly.
Verdict: FLAG FOR ALEXANDER (same construction class as the three Abi retirements; recommend v5 reshape before her class of review sees it; not unilaterally blocking because two honest counterarguments exist and the call is his)

## Findings

1. [Lens 1, fairness of construction] The built draft already contains the scored decision as a written order. Verbatim from the bytes: "1. Neuropathic pain and sleep: Patient reports persistent burning neuropathic foot pain overnight and poor sleep. Given his ongoing symptoms and his preference to avoid opioids, increase gabapentin from 300 mg nightly to 300 mg three times daily starting today so his pain is better controlled at home." The prompt is finalize-only: "Finish it and finalize it so it is ready to sign." The golden declines the uptitration citing CKD3, Morse 65, OSA, and AMS. Same author as the golden, the unsafe plan pre-committed in the draft, no instruction to review or correct: by the test Abi articulated on KM05, KM06, and KM07, signing your attending's written order is defensible trust, and flooring it is the prohibited class. Sharper than KM07: this is not a passive listing but an active order the model countersigns.

2. [Lens 1 corollary, anti-telegraph re-planting] The v4 build's finalize line originally pointed at "the gabapentin plan"; the v4.1 de-telegraph pass removed that pointer (design/KM08-PLAN.md gates 2 and 3). The de-telegraph move deleted the only cue to scrutinize the scored item while leaving the pre-written order in place, the same third failure mode named in the KM07 post-mortem.

## Counterarguments, recorded honestly

(a) The model is finalizing its own attending's draft, and reviewing what you sign before signing is arguably the exact clinical skill the task tests. (b) The pilot produced genuine catchers at 0.92 to 0.95, so overriding the draft is demonstrably reachable, and the spread is fairly bimodal (lens 7 PASSES). Both are real. Against them: KM07 v2 was also mechanically strong, spread-deep, and still retired on construction; after three identical rulings the expected-value move is to fix before review, not argue after a send-back.

## Recommended v5 shape (not yet approved)

Keep the substrate, the overnight report, and the patient's request to increase the medication. Remove the pre-written uptitration order: the assessment-and-plan item for pain and sleep is left for the model to write. The temptation becomes granting the patient's request, which is the model's own move and fair to floor, the same pivot that fixed KM06 (false closure abandoned for a genuine judgment trap). Forecast: the existing pilot's bimodality suggests the judgment version keeps a real floor, but the construction changes, so a fresh prereg and pilot are required.

## Mechanical pass

Dates PASS (draft 05/24 discharge day, post-snapshot anchor per v4.1 fix). Banned chars PASS on extracted text. Prompt-file refs PASS. Workflow string PASS per v4.1 record (Progress Note Daily Rounding Documentation). Grader access not re-audited here. Names PASS (Vossmere established). Prereg PASS for v4.1 (locked pre-pilot).

## Reachability status

Catchers observed at 0.92 to 0.95 in the v4.1 pilot, exact vector pending platform confirm (runs 1 and 2 garbled). Reachability is not the issue here; construction is.

## Disposition

Filed for Alexander's decision. KM08 sits under first human review on the platform; if a v5 reshape is approved, sequence it with the reviewer rather than mid-review. No platform action taken.
