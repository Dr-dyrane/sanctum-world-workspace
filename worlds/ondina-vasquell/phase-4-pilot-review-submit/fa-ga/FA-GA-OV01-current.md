# OV01 FA/GA - failure-only (Abi 6/09 + King P 6/14)

Status 2026-06-15: subject = 2nd-lowest run, job aa949641-e849-4d84-8a60-4d4642eb61ed, Attempt 6, run 28a61869-fdee-465f-a59a-ca65cf8f4bd0, score 0.50. Before paste: select Attempt 6 in Studio and bind the FA/GA box to run 28a61869; confirm its saved output (/tmp/outputs/Vasquell_discharge_med_review.md). Format: failure-only, no section names, no dashes.

## Failure Analysis

On Attempt 6 the model carried inpatient-only enoxaparin into the discharge regimen. The order set listed enoxaparin 40 mg daily; the chart supports it only as inpatient venous-thromboembolism prophylaxis, and at discharge it should be stopped, especially with aspirin and clopidogrel already on board.

The model did not stop it. It left enoxaparin as a confirmation item, asked for a home injection plan, and in the patient instructions described it as a shot to take while she was moving less, treating prophylaxis as reasonable to continue. The result carries an inpatient-only anticoagulant into the home regimen on top of dual antiplatelet therapy.

## Grader Analysis

The 0.50 is fair and the grader caught the deciding error. It scored the note down for the failure to stop inpatient-only enoxaparin at discharge, consistent with the golden, which stops it, and it did not over-credit the model's hedging (a confirmation item and a bleeding caution) because the deliverable still continued prophylaxis.

If anything the score is generous: a full continuation of an inpatient-only anticoagulant on dual antiplatelet therapy could be docked harder. Recommended grader rating: Good.
