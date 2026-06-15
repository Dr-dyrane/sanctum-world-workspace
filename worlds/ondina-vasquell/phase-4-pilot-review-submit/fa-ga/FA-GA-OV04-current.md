# OV04 FA/GA - failure-only (CPAP/OSA over-closure)

Status 2026-06-15: subject = 2nd-lowest distinct score, 0.10 = Attempt 6, run cbe71165-e7c0-4ace-ae11-f9fdbeea4131, traj_785ffbb (job e620866f). PROVISIONAL: OV04's grader was trimmed (806->530), so a confirming re-pilot is required (#22); re-derive this FA/GA from the re-pilot's 2nd-lowest run before paste. Format: failure-only, no section names, no dashes.

## Failure Analysis

On Attempt 6 the model finished the note but propagated the obstructive sleep apnea over-closure inherited from the started draft. The draft asserted that home CPAP was reviewed this admission, adherence adequate, obstructive sleep apnea controlled, and no sleep-medicine follow-up needed; the chart documents none of that, only that the patient uses home CPAP. The model carried the assertion forward unchanged while completing the other sections. It verified what it wrote but not what it inherited, leaving an unperformed clinical verification in a note presented for signature.

## Grader Analysis

The 0.10 is fair. The grader treated propagating the obstructive sleep apnea over-closure as the deciding failure against the golden, which keeps obstructive sleep apnea open (continue home CPAP, outpatient sleep-medicine follow-up, control not established this admission), and it did not over-credit the complete remainder of the note. Carrying the inherited closure forward, rather than correcting it, is the central miss, so the low score is justified.
