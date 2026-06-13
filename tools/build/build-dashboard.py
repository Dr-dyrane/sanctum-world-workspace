#!/usr/bin/env python3
"""Build the portable KM dashboard HTML from modular source files."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "dashboard" / "src"
OUT = ROOT / "dashboard" / "km-world-dashboard.html"


def main() -> None:
    index = (SRC / "index.html").read_text(encoding="utf-8")
    css = (SRC / "styles.css").read_text(encoding="utf-8").rstrip()
    data = (SRC / "data.js").read_text(encoding="utf-8").rstrip()
    app = (SRC / "app.js").read_text(encoding="utf-8").rstrip()

    css_tag = '  <link rel="stylesheet" href="./styles.css" />'
    js_tags = '  <script src="./data.js"></script>\n  <script src="./app.js"></script>'

    if css_tag not in index:
        raise SystemExit(f"Missing CSS tag in {SRC / 'index.html'}")
    if js_tags not in index:
        raise SystemExit(f"Missing JS tags in {SRC / 'index.html'}")

    built = index.replace(css_tag, f"  <style>\n{css}\n  </style>")
    built = built.replace(js_tags, f"  <script>\n{data}\n\n{app}\n  </script>")

    OUT.write_text(built, encoding="utf-8")
    print(f"Built {OUT}")


if __name__ == "__main__":
    main()
