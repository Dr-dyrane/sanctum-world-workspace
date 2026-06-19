#!/usr/bin/env python3
"""
OV07 wound-photo annotation compositor (NON-AI).

Purpose: take a license-cleared REAL diabetic foot ulcer photograph and composite
a plain typed chart-annotation strip onto it, producing the OV07 off-text finding
image. This is pure PIL image compositing (text on a strip), NOT generative AI, so
it replaces the retired Codex/Nanobanana wound-photo-image-spec.md per Larry's
2026-06-18 send-back on AI-generated images.

GATING (do not run until BOTH are true):
  1. Larry confirms the image's license tier is acceptable (CC BY 4.0 with recorded
     attribution, or strictly CC0/public domain). If strictly CC0 is required and no
     faithful CC0 photo exists, abandon this path and use the rendered scanned
     wound-assessment form instead (Path B), which has no license question.
  2. Alexander authorizes the OV07 rebuild.

After running: record the source image attribution (author, title, URL, license) in
the OV07 task spec / provenance, re-pilot the task (DO-NOT-REPEAT #22), then redo the
FA/GA from the new run set to the latest fa-ga-canonical guidance.

The scored finding is the TYPED ANNOTATION below; the photo only needs to be a faithful
plantar-forefoot diabetic foot ulcer (granulating base, no exposed bone, no face). The
annotation text must match golden-OV07-v1.docx and build_ov07.py exactly. No banned
characters (no em dash, en dash, arrow, asterisk, bracket). No interpretive words.

Usage:
  python3 composite_ov07_wound_annotation.py --input cleared_wound.jpg --output wound_photo_05242026.jpg
"""

import argparse
import os
from PIL import Image, ImageDraw, ImageFont

# The exact scored annotation. Must match golden-OV07-v1.docx and build_ov07.py.
ANNOTATION_DATE = "05/24/2026"
ANNOTATION_BODY = "Undermining 2.0 cm at 12 oclock, tracks proximally. Probe to bone negative."

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "DejaVuSans.ttf",
    "Arial.ttf",
]


def load_font(size):
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def wrap(draw, text, font, max_width):
    words = text.split()
    lines, line = [], ""
    for w in words:
        trial = (line + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="license-cleared real wound photo")
    ap.add_argument("--output", default="wound_photo_05242026.jpg")
    ap.add_argument("--date", default=ANNOTATION_DATE)
    ap.add_argument("--max-width", type=int, default=1100,
                    help="resize the photo to at most this width before annotating")
    args = ap.parse_args()

    if not os.path.exists(args.input):
        raise SystemExit("input image not found: " + args.input)

    img = Image.open(args.input).convert("RGB")

    # Normalize width so the strip text is legible at a predictable size.
    if img.width > args.max_width:
        h = int(img.height * (args.max_width / img.width))
        img = img.resize((args.max_width, h), Image.LANCZOS)

    w = img.width
    pad = max(10, w // 80)
    font_size = max(16, w // 42)
    font = load_font(font_size)

    header = "WOUND PHOTO " + args.date
    scratch = ImageDraw.Draw(img)
    body_lines = wrap(scratch, ANNOTATION_BODY, font, w - 2 * pad)
    all_lines = [header] + body_lines

    line_h = font.getbbox("Ag")[3] + max(4, font_size // 4)
    strip_h = pad * 2 + line_h * len(all_lines)

    canvas = Image.new("RGB", (w, img.height + strip_h), "white")
    canvas.paste(img, (0, 0))
    d = ImageDraw.Draw(canvas)
    # thin separator rule above the strip
    d.line([(0, img.height), (w, img.height)], fill=(120, 120, 120), width=2)

    y = img.height + pad
    for i, ln in enumerate(all_lines):
        d.text((pad, y), ln, fill=(20, 20, 20), font=font)
        y += line_h

    canvas.save(args.output, "JPEG", quality=90)
    print("wrote " + args.output + " (" + str(canvas.width) + "x" + str(canvas.height) + ")")
    print("REMINDER: record the source image attribution in the OV07 spec, then re-pilot.")


if __name__ == "__main__":
    main()
