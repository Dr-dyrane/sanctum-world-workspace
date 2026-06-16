# OV04 FA/GA - failure-only (off-text CPAP-adherence finding, v3)

Status 2026-06-15: subject = 2nd-lowest distinct score, 0.20 = Attempt 9, run bad52e0a-7096-45fb-b4b3-8d544669226b, traj_907e6e9 (job 517aa586-9c65-4ab8-b539-2adc370e64d6). The v3 confirming pilot is a clean BIMODAL: floors 0.15/0.15/0.20/0.20, catchers 0.80/0.80/0.85/0.88/0.90/0.95 (6 of 10), mean ~0.59 - fair and hard; the KM08-v7 off-text lever works. Catcher read DONE: Attempt 10 (0.95, run 73e9bdba) is a genuine catch (OCR'd the CPAP report, found 9 of 30 nights used and residual AHI 31, surfaced poor adherence and sleep-medicine follow-up). Before paste: select Attempt 9 in Studio and bind the FA/GA box to run bad52e0a. Format: failure-only, no section names, no dashes.

## Failure Analysis

On Attempt 9 the model completed the note competently from the chart prose, reconciling the medications and building the follow-up, but it missed the central off-text finding. The CPAP compliance report was mounted as an image (cpap_compliance_report_05242026.jpg); the model saw the file in the directory listing but never opened or read it, so it never learned that adherence was poor and obstructive sleep apnea undertreated this stay.

It therefore carried the chart's quiet on home CPAP forward, documenting nightly CPAP with no adherence concern and no sleep-medicine follow-up. The finding lived only in the device report, and a note built from the prose alone treats the patient as stable on home CPAP. The result signs off on an undertreated, unaddressed obstructive sleep apnea axis.

## Grader Analysis

The 0.20 is fair. The grader treated missing the CPAP adherence finding as the deciding failure against the golden, which surfaces the poor adherence from the device report and keeps obstructive sleep apnea open with outpatient sleep-medicine follow-up. It confirmed from the transcript that the model never opened the compliance image, so the miss is real, and it did not over-credit the otherwise complete and accurate note.

The residual credit reflects the faithfully completed remainder (medications, antibiotic de-escalation, follow-up), which cannot lift the score once the central off-text finding is missed. Recording obstructive sleep apnea as continuing on home CPAP with no adherence concern is the central miss, so the floor score is well placed.
