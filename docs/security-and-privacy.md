# Security And Privacy

## Public-Safe Repository Policy

This repository may be pushed to a public GitHub remote after Alexander explicitly marks the current tree public-safe. Public-safe means no credentials, real patient data, authenticated-only links, browser exports, session material, or prohibited proprietary downloads are tracked.

## Do Not Commit Secrets

Never commit:

- passwords
- API keys
- tokens
- cookies
- browser profiles
- session exports
- `.env` files
- authentication config
- private keys

## Authenticated Links

Do not expose authenticated-only links in public places. If a private Google Drive, RL Studio, Slack, or Mercor link is needed locally, keep it in private project notes and never publish it.

## Patient Data

Do not include real patient data. All patients, providers, MRNs, dates, institutions, and identifiers in generated Worlds should be fictional unless the official project source explicitly authorizes a different synthetic standard.

Korvin Merrow is fictional.

## Mercor / Sanctum Source Documents

Source documents and templates are for authorized project work only. Keep them under `reference/` only when approved for repository storage. Do not add new source downloads unless Alexander has confirmed they are safe for the current remote.

## Sanitizing Exports

Before sharing or publishing any export:

1. Remove secrets and authenticated links.
2. Remove browser or session artifacts.
3. Confirm no real patient data or PHI exists.
4. Confirm reviewer comments are appropriate to share.
5. Confirm source documents are permitted for the destination.
6. Confirm the current project phase allows the artifact.

## Public Remote Gate

Before pushing to any remote, verify Alexander has approved the current tree as public-safe or private-safe. Confirm secrets and local exports are ignored, then push only the approved branch. When in doubt, pause.
