# OV04 task-level image spec - CPAP compliance report (Codex / Nanobanana)

This is a TASK-LEVEL image for OV04 v3 (not a world file). Unlike EW30/EW31 (substrate-only), this image IS the scored off-text finding. Generate it, then mount it with the OV04 task files as `cpap_compliance_report_05242026.jpg`. The numbers MUST match the golden (golden-OV04-v1.docx) and build_ov04.py.

Shared rules:
- No banned characters in any overlay text (no em dash, en dash, arrow, asterisk, bracket).
- Manufacturer-neutral: no real brand logos (no ResMed, Philips, etc.).
- No real patient identifiers; if a header name is shown keep it generic or match the chart minimally.
- The three key numbers must be LEGIBLE (they are the scored finding) but shown as a plain raw report, not highlighted or interpreted.

## cpap_compliance_report_05242026.jpg

Genre: a scanned one-page CPAP therapy compliance report printout (the kind a DME company or sleep clinic prints), added to the patient's chart on 05/24/2026.

Generation prompt (give to Codex imagegen):
"A scanned one-page CPAP therapy compliance report, plain clinical document style, black text on white, dated 05/24/2026. Header reads CPAP THERAPY COMPLIANCE REPORT. A usage summary table shows: Reporting period 30 days; Average nightly usage 1.4 hours; Nights device used 9 of 30; Nights with usage at least 4 hours 3 of 30; Residual AHI 31 per hour. Below the table, a small simple bar chart of nightly usage hours with many bars at or near zero and a few short bars. Manufacturer-neutral layout, generic fonts, slightly off-angle scan with a faint shadow. No photographs, no logos."

Hard constraints / negative prompt:
- The numbers (average usage about 1.4 hours per night, 9 of 30 nights used, residual AHI about 31 per hour) MUST be present and legible; they are the scored finding.
- No interpretive words on the report (no "poor adherence", "non-adherent", "undertreated", "abnormal"). Raw numbers only; the clinical interpretation is the model's job.
- No patient face or photo; minimal or no identifiers; no real brand marks.
- A believable raw device report, not a polished infographic.

Trap-discipline note: this image carries the OV04 v3 scored finding (poor CPAP adherence / undertreated OSA). The grader does NOT read it; it scores the model's text output against the golden. Make the numbers legible-but-easy-to-skip (raw report, no highlighting), so a careful read catches it (catcher) and a cursory completion misses it (floor). Numbers must match golden-OV04-v1.docx and build_ov04.py exactly.
