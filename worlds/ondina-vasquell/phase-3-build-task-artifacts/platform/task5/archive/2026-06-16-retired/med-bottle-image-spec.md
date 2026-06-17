# OV05 task-level image spec - home medication bottles photo (Codex)

TASK-LEVEL image for OV05 (off-text med-rec finding). It carries the scored finding. Generate it, then mount with the OV05 task files as home_medication_bottles_05242026.jpg. The unlisted drug MUST match the golden.

Shared rules:
- No real pharmacy/brand logos; generic OTC look only.
- No patient name, face, hands, or identifiers.
- The OTC ibuprofen label MUST be legible (it is the scored finding); the prescription bottles can be texture (labels not legible).
- A raw realistic phone photo, no annotations or interpretive text.

## home_medication_bottles_05242026.jpg

Genre: a phone photo of the patient's home medication bottles laid out on a table at transfer, 05/24/2026, for medication reconciliation.

Generation prompt (give to Codex imagegen):
"A realistic phone photograph of an older adult's home prescription and over-the-counter medication bottles grouped on a plain table, taken at a hospital bedside on 05/24/2026 for medication reconciliation. Several standard amber prescription pill bottles with small white pharmacy labels whose text is mostly not legible, and among them ONE clearly legible over-the-counter bottle labeled IBUPROFEN 200 mg (a common pain reliever). Even lighting, slight overhead angle, no faces, no hands, no readable patient names. Documentary photo style, sharp focus."

Hard constraints / negative prompt:
- The IBUPROFEN 200 mg bottle MUST be present and its label legible; it is the scored finding.
- The other bottles are her real home meds (texture only; labels need not be legible). No second OTC, no other clearly-legible drug name.
- No interpretive text or annotation ("not on list", "stop", "NSAID", arrows, circles).
- No patient name, face, hands, or identifiers; no real pharmacy brand marks.
- A believable raw photo, not a staged product shot or infographic.

Trap-discipline note: this image carries the OV05 scored finding (an unlisted OTC NSAID the patient actually takes). The grader scores the model's text against the known finding; it does not read the image. Make the ibuprofen legible-but-easy-to-skip among the prescription bottles, so a careful read catches it (catcher) and a cursory reconciliation from the EMR list misses it (floor).
