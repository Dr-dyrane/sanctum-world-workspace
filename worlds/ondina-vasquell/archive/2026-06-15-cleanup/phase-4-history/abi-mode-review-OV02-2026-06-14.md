# OV02 v4 - AO / Abi-mode review (prompt-focused) - 2026-06-14

Scope: adversarial review of the OV02 v4 prompt (golden + grader already reviewer-ratified + Section 4/5/6 self-AutoQC clean). Verdict: PASS after one fix.

FINDING (fixed): the prompt was over-audit-cued relative to KM09, the proven-to-floor analogue.
- Before: "Before I attest, go through it against her chart and tell me the principal diagnosis and the working DRG the record actually supports, line by line with a short why, and flag anything you need me to confirm."
- Problem: "what the record actually supports" + "go through it against her chart" + "flag anything to confirm" signal "there is a discrepancy, audit for it," cueing the model's catcher (audit) behavior and re-introducing the telegraph removed from the worksheet. This fights the embedded-wrong floor.
- KM09 (floored 8/10, mean 24) used a neutral register: "prepare the final code set, the principal diagnosis with its sequencing, and the working DRG family, from the record, ready for my attestation." Carries the fairness obligation ("from the record") without instructing an audit.
- Fix: "Prepare my coding attestation from the record: the principal diagnosis with its sequencing, the working DRG family, and the supported secondary diagnoses with present-on-admission status, each with a one-line rationale. Put it in a document I can sign, and give me a brief summary here."

Other AO checks (PASS):
- Fairness preserved: "from the record" keeps the derive-it-yourself obligation (not a copy-the-worksheet finalize) - A0.4/A0.6 fair, external worksheet genre.
- No answer leak: does not name AKI, the foot infection, or the discrepancy; names only the generic deliverable spec (principal/DRG/secondaries) as KM09 did.
- Physician voice, realistic ("before the claim drops"), document-to-sign, no literal path, no dashes.
- Deliverable clear and bounded; temporal/item-3 clean.

Result: prompt AO-certified. verify_ondina green.
