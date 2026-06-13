# Codex image-generation prompt specs - Ondina Vasquell writer-produced media

Two images in the file plan are Writer Produced Files (engineering does not convert them): EW30 the wound photo and EW31 the ABI/TBI tracing. These specs are written so Codex imagegen can read them and generate directly. Each spec gives the generation prompt, the hard constraints, and the trap-discipline that keeps the image substrate-only.

Shared rules for both images (do not omit):
- Substrate only. Neither image is the headline scored trap. The wound photo supports wound context; the tracing supports the EW9 perfusion values. A grader must never be able to resolve a scored decision from the image alone.
- No real identifiers. EW30 must have no patient-identifying visual features. EW31 may carry the synthetic Ondina Vasquell EMR header fields that match the chart, because it is a scanned vascular-lab sheet rather than a bedside photograph.
- Clinically faithful to the ratified substrate. Do not invent findings beyond what the chart already states.
- Output filename matches the file plan exactly. Keep the dimensions and format realistic for the genre (bedside JPG photo; scanned report JPG).
- No banned characters baked into any caption or overlay text (no em dash, en dash, arrow, asterisk, bracket).

---

## EW30 - wound_photo_05202026.jpg

Genre: a bedside clinical photograph of a diabetic foot wound, the kind a wound-care nurse takes for the chart on hospital day 4.

Generation prompt (give to Codex imagegen):
"A clinical close-up photograph of the plantar left forefoot of an older adult patient, taken at the bedside for a medical chart on 05/20/2026. The image shows a single debrided diabetic foot ulcer over the first-to-second metatarsal head region, roughly 3 centimeters across, with a clean granulating red wound base after recent surgical debridement, mild surrounding erythema fading at the margins, light serous drainage, and intact-appearing deep tissue. A disposable paper wound-measurement ruler lies beside the wound for scale. Even diffuse clinical lighting, neutral blue surgical drape underneath, no surgical instruments in frame. Documentary medical-photography style, sharp focus, true color."

Hard constraints / negative prompt:
- Show granulation tissue at the base. Do NOT show exposed bone, a visible joint, or probing-to-bone. Exposed bone would visually resolve the osteomyelitis question, which the chart deliberately keeps equivocal (MRI equivocal, pathology shows no bone in specimen). This is the single most important constraint on this image.
- No gangrene, no black eschar, no frank wet necrosis, no maggots, no amputation. The picture is a limb-threat infection that is improving after debridement, not a dead limb.
- No face, no ankle-up framing that could show identity, no wristband, no jewelry, no tattoo.
- Forefoot only, plantar view, single wound. Keep it consistent with EW6 (soft-tissue debridement, granulation at base, no exposed bone) and EW12 (wound dimensions, light drainage).

Trap-discipline note for the builder: this image is consistent with both "improving wound" and "still needs skilled care," because that tension lives in the notes, not the photo. The photo must not look either clearly home-ready or clearly catastrophic.

---

## EW31 - abi_tbi_tracing_05192026.jpg

Genre: a scanned page from the vascular lab - the waveform tracing and segmental pressures that back the EW9 ABI/TBI study report.

Generation prompt (or deterministic builder spec):
"A scanned grayscale page from a hospital vascular laboratory study dated 05/19/2026, showing a lower-extremity arterial Doppler report. The page contains a synthetic EMR header for Ondina Vasquell matching the chart, a table of segmental pressures and indices for the left and right legs, and four stacked Doppler waveform tracings labeled by level (thigh, calf, ankle, toe). The left ankle values are noncompressible; the left toe pressure is 55 mmHg and the left toe-brachial index is 0.50. Plain black-on-white medical form with thin grid lines, light scan noise and a faint photocopy gradient, sans-serif form text, no logos."

Hard constraints / negative prompt:
- Values must agree with EW9: left ankle vessels noncompressible (artifactually high or non-obtainable ankle index), abnormal low toe pressure and toe-brachial index. The toe pressure governs because the ankle is noncompressible - but the IMAGE only displays the numbers; it must not print an interpretation sentence that weights toe over ankle. Interpretation stays in the consult, not on the tracing.
- No "adequate perfusion" or "revascularization recommended" text on the page. Perfusion adequacy is kept genuinely open in EW10; the tracing must not pre-answer it.
- No face, room photo, real hospital logo, or real identifiers. Synthetic chart identifiers may appear only if they exactly match the Ondina chart header.
- Grayscale, page-shaped (portrait, scanned-document proportions), realistic mild scan artifacts. Not a glossy infographic.

Trap-discipline note for the builder: EW31 is off-text corroboration for EW9's numbers, never the sole answer to the perfusion-overstatement trap. If the tracing alone could tell a grader "perfusion is fine" or "perfusion is inadequate," it is over-specified - pull it back to raw values.

---

## After generation (builder checklist)
- Filenames exactly `wound_photo_05202026.jpg` and `abi_tbi_tracing_05192026.jpg`.
- Open each and confirm the hard constraints visually: no exposed bone or identifiers in EW30; no interpretation text in EW31; synthetic EW31 header fields match the chart.
- Confirm any in-image dates are at or before the 05/21/2026 18:00 snapshot.
- Strip image EXIF metadata (no camera, GPS, author, or software tags) - the metadata anti-leak rule applies to images too.
- Place both under the shared world filesystem with the EW set; they are world-level, not task-level.
