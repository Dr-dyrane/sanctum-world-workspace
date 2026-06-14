# Sanctum Dashboard

Next.js cockpit for Project Sanctum world and task presentation.

## Local Run

```bash
npm install
npm run seed:docs
npm run dev
```

The app reads local database settings from `.env.local`. That file is ignored by git. Keep real credentials in Vercel environment variables for deployment.

## Current Shape

- Static world and task data lives in `src/lib/sanctum-data.ts`.
- Neon is wired as a server-only readiness layer in `src/lib/database.ts`.
- Packet documents are seeded to Neon with `npm run seed:docs`.
- Public downloads are intentionally not promoted yet. Add only sanitized artifacts to `public/downloads/`.
- The existing single-file dashboard remains in `dashboard/` until this app fully replaces it.
