# pipeline-output/ removed 2026-06-14

The abandoned Stage-9 pipeline run (the one that embellished writer files and
leaked task files) was deleted. We never used it: the live world is the
writer-produced restore at `file-review/revision/filesystem/` (34 clean files).

It was removed because its stale `preliminary_discharge_order_set_05212026.docx`
copies caused repeated confusion during OV01 mount debugging. Historical
references in SECOND-PASS-STYLE-AUDIT.md and STAGE-9-FILE-REVIEW-PLAN.md point
here for provenance only; the conclusions in those docs stand.
