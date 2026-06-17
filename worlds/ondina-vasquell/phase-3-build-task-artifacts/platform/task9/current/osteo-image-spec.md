# OV09 v2 task-level image spec - transfer-day foot radiograph with osteomyelitis (Codex / Nanobanana)

This is a TASK-LEVEL image for OV09 v2 (not a world file). Like OV04's CPAP report and OV07's wound photo, this image IS the scored off-text finding. Generate it, then mount it with the OV09 task files as `foot_radiograph_05242026.jpg`. The finding values MUST match the golden (golden-OV09-v1.docx) and the started note's breadcrumb ("A transfer-day left foot radiograph was obtained on 05/24 and added to the chart imaging").

Lane / mechanism: Post-Acute Care Coordination Documentation. Off-text image miss, OV04/OV07 family. The chart's prose frames the infection as soft-tissue with osteomyelitis NOT established (MRI 05/18 equivocal marrow edema, no frank cortical destruction; pathology 05/20 no bone). FLOOR = the model finishes the transfer handoff from the prose and misses this transfer-day radiograph, transferring a bone infection on a short soft-tissue antibiotic course. CATCHER = opens it, surfaces the osteomyelitis, and escalates to a prolonged IV/OPAT course and a parenteral-capable setting.

Shared rules:
- No banned characters in any overlay text (no em dash, en dash, arrow, asterisk, bracket).
- No real patient identifiers, no real institution marks, no real accession numbers.
- Clinically faithful: a plantar forefoot diabetic foot infection, debrided, the bone finding localized to the second metatarsal head (matches the equivocal MRI marrow edema at the first to second metatarsal heads). The NEW finding is the cortical destruction.
- The finding must be LEGIBLE (it is the scored catch) but shown as a plain transfer-day study, not highlighted or interpreted beyond the impression line.

## foot_radiograph_05242026.jpg

Genre: a grayscale plain radiograph of the left forefoot taken at transfer on 05/24/2026 and added to the chart, the kind obtained before a level-of-care transfer when bone involvement is in question.

Generation prompt (give to Codex imagegen):
"A grayscale plain radiograph, anteroposterior view, of an adult left forefoot, documentary medical-imaging style. The second metatarsal head shows cortical irregularity and bone destruction with a moth-eaten lucent appearance and loss of the normal cortical margin, distinct from the intact adjacent metatarsals. Soft-tissue swelling over the plantar forefoot. A plain typed white annotation strip across the bottom reads exactly: FOOT RADIOGRAPH 05/24/2026  Cortical destruction at the second metatarsal head, new compared with prior. Consistent with osteomyelitis. Even radiographic exposure, true grayscale, sharp focus, no patient name, no identifiers."

Hard constraints / negative prompt:
- The annotation strip text MUST be present and legible (cortical destruction at the second metatarsal head; new compared with prior; consistent with osteomyelitis; dated 05/24/2026). It is the scored finding.
- Localize the destruction to the SECOND metatarsal head; keep the other bones intact so the finding is specific.
- No interpretive words beyond the impression line (no "urgent", "severe", "limb-threatening", "do not transfer"); the clinical escalation is the model's job.
- No patient identifiers, no real hospital or device marks; clinical-documentation realism, not a sensational image.

Trap-discipline note: this image carries the OV09 scored finding (osteomyelitis means a prolonged parenteral antibiotic course and a parenteral-capable post-acute setting, not a short soft-tissue course). The grader does NOT read the image; it scores the model's handoff text against golden-OV09-v1.docx. Make it a plain transfer-day study, legible-but-easy-to-skip, so a careful read catches the osteomyelitis (catcher) and a cursory "finish the handoff" completion misses it (floor). The finding (cortical destruction at the second metatarsal head, consistent with osteomyelitis, dated 05/24/2026) must match golden-OV09-v1.docx exactly.

Placement: mount as a task-level file with the OV09 task files as `foot_radiograph_05242026.jpg`. The started note carries one quiet transfer-day breadcrumb ("a transfer-day left foot radiograph was obtained on 05/24 and added to the chart imaging"), so the finding is fair to reach but not forced.
