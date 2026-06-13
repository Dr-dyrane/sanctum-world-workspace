# Dashboard Directory

Standalone, zero-build visualizations for this workspace. Each file is fully
self-contained (CDN dependencies only) and can be opened directly in a browser
or served as a static file.

## Contents

- `km-world-dashboard.html` — Korvin Merrow (KM01–KM10) task suite dashboard.
  Renders failure-depth as a radial node chart, run-spread dot matrices, and
  per-task detail cards. Built to be readable by someone outside AI training:
  a "How to read this" explainer, plain-English "Tests:" line and verdict per
  task, tap-for-definition glossary terms, a pipeline stage stepper, data-quality
  badges (EXACT / APPROXIMATE / PARTIAL), and a reachability indicator. Includes
  status filtering, sorting, and shareable deep links via the URL hash.
  Data synced 2026-06-13 from `task-setup/KM-WORLD-PERFORMANCE-REPORT.md`.

## Deep links

The hash drives view state, so any filtered/sorted view is shareable:

- `#KM03` … `#KM10` — scroll directly to a specific task card.
- `#filter=delivered` / `#filter=review` — show only tasks in that status.
  (Legacy `complete`/`pending` links still resolve.)
- `#sort=low` — order cards by mean (`position`, `high`, `low`).
- Combine with `&`, e.g. `#filter=review&sort=low`.

## Internal structure (single file, modular)

The inline script is organized as banner-commented modules so each concern has
one home: CONFIG (score bands, stages, labels — every threshold lives here),
GLOSSARY (plain-English definitions), DATA (the WORLDS registry), UTILS, STATE
(versioned localStorage), WORLD CONTROL, COMPONENTS (pure render functions),
VIEWS (all re-renderable), CONTROLLER (filter/sort/hash), SOUND (opt-in, muted
by default), WORLD SWITCHER + BOOT. Change a score threshold once in CONFIG and
every visual follows.

## Adding a world

The dashboard is multi-world. All data lives in the `WORLDS` registry in the
DATA module; the header title is a dropdown listing every registered world.
To plug in a new world, add one block:

```js
WORLDS['my-world'] = {
  title: '...', kicker: '...', blurb: '...', driveUrl: '...' /* or null */,
  meta: { world, patient, chart, writer, source, dataSyncedOn, provenance },
  tasks: [ { id, position, stage, name, plain, mechanism, verdict, workflow,
             reviewer, platformId, taigaJob, mean, spread, runsTotal,
             quality, reach, provNote? }, ... ],
};
```

Everything else (hero, radial, cards, filters, summary, FAB, deep links,
screen-reader table) renders from the registry. The selected world persists
across reloads and is shareable via `#world=<id>`. Task deep links work for
any world's ids (e.g. `#QX03`).

## Conventions

- Keep each dashboard as a single self-contained HTML file (Tailwind + Lucide
  via CDN). Do not introduce a build pipeline or bundled dependencies here.
- Source-of-truth data lives in `task-setup/KM-WORLD-PERFORMANCE-REPORT.md`
  (canonical) and each `taskN/TASKN-STATE.md`. Dashboards embed a snapshot for
  display; update the snapshot when the underlying data changes (hygiene rule:
  on every pilot gate clear or status change).
- Color doctrine: monochrome purple field with semantic accents on small status
  elements only (never large surfaces or charts). Purple = performance, brand,
  in-motion pipeline states; green = completion/verified (delivered, reachability
  proven, exact vectors); amber = caution (floors, provisional data); rose token
  is defined but reserved for future sent-back/blocked states.
- Honesty rule: approximate or partial vectors are always badged as such and
  never displayed as exact (see DATA-SOURCE INTEGRITY note in the report).
- No binaries, installers, or generated caches — documentation and source files
  only.

## Viewing

Open the file directly, or serve the folder:

```bash
python3 -m http.server 8099
# then visit http://localhost:8099/dashboard/km-world-dashboard.html
```
