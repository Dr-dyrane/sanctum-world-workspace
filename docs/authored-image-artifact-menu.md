# Authored off-text-image artifact menu (cross-world doctrine)

Forward-carried knowledge for World 3 (Marva) and beyond. The off-text-image floor (OV04 CPAP
report, OV12 afib ECG) needs a mounted IMAGE whose finding the model misses by never opening the
file. This is the menu of medical images we can AUTHOR ourselves, license-clean and ban-compliant,
so the engine is available on any lane in any world.

## The rule that decides what is authorable

Larry 06/18 bans AI-GENERATED images (generated photos and films). Image policy also bars
copyrighted or sourced images (PD/CC0 only). The always-safe intersection is a PROGRAMMATIC RENDER
we generate ourselves, a data plot or a structured printout drawn with matplotlib, reportlab, or
LibreOffice. It is not a generated photo (deterministic plotting, not a generative model), not
sourced (no copyright, no PHI, no attribution), and reproducible from a committed script (the
provenance travels with it).

- AUTHORABLE = anything natively a TRACING, a PRINTOUT of numbers, or a FORM or CHART.
- NOT AUTHORABLE = anything natively a PHOTOGRAPH or a grayscale DIAGNOSTIC IMAGE (camera or
  scanner physics). For those findings, mount the REPORT instead, which is always authorable.

## A. Waveform / tracing plots (matplotlib) - finding in the morphology + raw fields

ECG, 12-lead or rhythm strip (new afib [OV12]; also ischemia / ST shift, AV block, long QT, paced
rhythm, prior-MI Q waves); telemetry or monitor strip (pauses, ectopy runs); capnography EtCO2;
spirometry flow-volume loop with a numeric PFT block; arterial-line or CVP pressure tracing; fetal
cardiotocograph with decelerations (OB worlds).

## B. Device / numeric printouts - finding in the numbers

CPAP / BiPAP adherence report (OV04, proven); CGM or glucometer download (time-in-range, hypos);
pacemaker / ICD interrogation (AF burden, lead alert); Holter or event-monitor summary; ABI / TBI
vascular study; INR or anticoagulation meter log; blood-gas slip; infusion or PCA pump log;
dialysis run sheet; ventilator settings printout; audiometry; visual-field / perimetry chart.

## C. Structured forms / scanned documents / charts

Lab, pathology, microbiology, or radiology REPORT printouts (the universal substitute, see below);
immunization-registry printout; scored screening questionnaire (PHQ-9 and similar); outside-records
fax; pharmacy or bottle-label printout (caveat: a medication-reconciliation deliverable forces
reading every med source, so a med image is NOT off-axis there, which is why the OV05 bottle photo
ceilinged); trend graphs (labs, growth chart, weight, ins-and-outs).

## Off-menu (needs generative AI or a real image, BANNED) - mount the REPORT instead

Wound / skin / derm photos (the OV07 photo was sent back), fundus photos, gross-pathology photos,
endoscopy stills; radiographs, CT, MRI, ultrasound or echo images, histopathology slides. For any
finding that lives on one of these, the off-text artifact is the dictated REPORT (radiology,
pathology, echo), authored as a printout. The report is always on-menu even when the image is not.

## Floor discipline (every authored-image floor)

1. OFF the deliverable's headline axis (un-primed): OV04 put a sleep finding in a foot transfer
   note; OV12 puts a rhythm finding in a renal consult.
2. RAW data, no printed interpretation: OV04 showed numbers only; OV12 stripped the printed
   "ATRIAL FIBRILLATION" and left the rate plus raw fields. The catch is read-and-know, not OCR a
   label, which keeps both the no-open and the open-but-glance failures inside the floor.
3. A quiet prose breadcrumb (a nursing note) points to the file without stating the finding.
4. Render in-repo from a committed script carrying a provenance docstring; save metadata-clean.

Floor = the model completes the deliverable from prose and never opens the file. Catcher = it opens
the file, interprets the raw finding, and acts on it.

## Related canon

- Render method + the "why is this an image" fairness test: worlds/ondina-vasquell/docs/FLOOR-MECHANISM-LIBRARY.md (off-text image section) and docs/docx-generation-method.md section 5.
- Per-world sourcing and licensing order (in-repo render > in-house simulator > verified public-domain): worlds/marva-lydell/docs/IMAGE-SOURCING-CHECKLIST.md.
- Proven instances: OV04 (CPAP adherence report), OV12 (pre-discharge ECG, new-onset afib).
