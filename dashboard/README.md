# Dashboard Directory

Standalone, zero-build visualizations for this workspace. Each file is fully
self-contained (CDN dependencies only) and can be opened directly in a browser
or served as a static file.

## Contents

- `km-world-dashboard.html` — Korvin Merrow (KM01–KM06) task overview dashboard.
  Renders failure-depth as a radial node chart, run-spread dot matrices, and
  per-task detail cards. No build step, no install.

## Conventions

- Keep each dashboard as a single self-contained HTML file (Tailwind + Lucide
  via CDN). Do not introduce a build pipeline or bundled dependencies here.
- Source-of-truth data (KM01–KM06 specs, scores, run results) lives under
  `worlds/korvin-merrow/`. Dashboards embed a snapshot of that data for display;
  update the snapshot when the underlying world data changes.
- No binaries, installers, or generated caches — documentation and source files
  only.

## Viewing

Open the file directly, or serve the folder:

```bash
python3 -m http.server 8099
# then visit http://localhost:8099/dashboard/km-world-dashboard.html
```
