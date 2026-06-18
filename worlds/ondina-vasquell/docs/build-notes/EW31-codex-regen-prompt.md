# EW31 Codex regeneration prompt (fixes 2 audit gaps, 2026-06-13)

Hand this to Codex imagegen. It replaces the current abi_tbi_tracing_05192026.jpg, which failed the eye-audit on two points: a stale ordering-clinician initial ("M. Everet") and a measurable right-ankle index that contradicts the report's "noncompressible bilaterally."

## Prompt

Regenerate the scanned vascular-lab page `abi_tbi_tracing_05192026.jpg` (grayscale, portrait, scanned-document look with light scan noise and a faint photocopy gradient, thin grid lines, sans-serif form text, no logos). Overwrite the existing file with the same filename.

Header (must match the chart exactly):
- Harbor Crest Regional Medical Center, Vascular Laboratory, Lower Extremity Arterial Study. Study Date 05/19/2026.
- Patient: Ondina Vasquell | MRN OV-3358104 | DOB 03/14/1958 | Sex F
- CSN-308852140 | Location 6 South Medicine 6S-214 | Accession HCR-VAS-05193320
- Procedure: ABI/TBI with toe pressures | Indication: DFI perfusion assessment | Status: Final
- Ordered by: Lillian Everet, MD   (FIX 1: not "M. Everet" - use Lillian Everet, MD)
- Tech: Vascular Lab

Segmental pressures and indices table:
- Brachial: right 110, left 110.
- High thigh / low thigh / calf: keep plausible indices in the 1.2 to 1.4 range, both legs.
- Ankle PT and ankle DP: BOTH LEGS read "NC" (noncompressible) for pressure and index. (FIX 2: do NOT print a measurable right-ankle index; the report states ankle indices noncompressible bilaterally.)
- Ankle-brachial index line: Noncompressible (greater than 1.3) on BOTH sides.
- Toe pressure: right 92 mmHg, left 55 mmHg.
- Toe-brachial index: right 0.84, left 0.50.

Doppler waveforms (four stacked per leg: thigh, calf, ankle, toe): ankle and toe tracings monophasic/dampened, left more dampened than right.

Hard constraints:
- No interpretation sentence anywhere on the page. No "adequate perfusion," "inadequate," or "revascularization" text. The page shows raw values only; interpretation lives in the consult.
- No real hospital logo, no face, no real identifiers. Synthetic chart identifiers only, exactly as above.
- All in-image dates at or before 05/21/2026. Strip EXIF (no camera, GPS, author, or software tags).

## After regeneration (eye-check before staging)
1. Ordered by reads "Lillian Everet, MD" (no "M. Everet").
2. BOTH ankle indices read NC / noncompressible; no measurable right-ankle number.
3. Toe values: right 92 / 0.84, left 55 / 0.50. Header matches the chart.
4. No interpretation text; grayscale scanned look; EXIF stripped.
Place at world-files/abi_tbi_tracing_05192026.jpg (and the synthetic-files staging copy), then rerun tools/verify/verify_ondina.py (docx unaffected) and confirm against EW9.
