# MCP And Integration Audit

Audit date: 2026-05-29

No MCPs or plugins were installed during this audit.

Addendum: 2026-06-11. Installed and enabled `omni-analytics@openai-curated` from the Codex marketplace as the available Data and Analytics connector. This is an app connector, not a standalone external MCP server, so `codex mcp list` still only shows external MCP servers such as `node_repl`. The current session did not hot-load Omni tools after install; expect a new Codex session or app reload, and connector authentication if prompted.

## Configured MCP Servers

| MCP | Purpose | Usefulness To Sanctum Workflow | Installation Method | Recommendation |
| --- | --- | --- | --- | --- |
| `playwright` | Browser automation through Playwright MCP. | Useful for controlled browser verification and future RL Studio navigation only when authorized. | Configured in `C:\Users\Dyrane\.codex\config.toml` with `npx @playwright/mcp@latest`. | Keep. Use only with explicit browser/RL Studio authorization. |
| `node_repl` | Persistent Node-backed execution kernel. | Useful for lightweight local scripting, structured extraction, and quick checks. Less central than Python for DOCX/PDF work. | Configured in Codex config with local `node_repl.exe`. | Keep. No changes needed. |

## Installed Codex Plugins / Integrations

| Integration | Purpose | Usefulness To Sanctum Workflow | Installation Method | Recommendation |
| --- | --- | --- | --- | --- |
| Browser | In-app browser automation for local pages and non-authenticated browser checks. | Useful for local previews and simple web checks; not enough for authenticated RL Studio if Chrome session is required. | Installed plugin cache: `openai-bundled/browser`. | Keep. Use only when needed. |
| Chrome | Authenticated Chrome automation and Codex Chrome extension workflow. | Potentially useful for RL Studio operations requiring Alexander's logged-in profile. Previously had bridge/trust issues, so verify before relying on it. | Installed plugin cache: `openai-bundled/chrome`. | Keep. Repair/reconnect only with explicit authorization. |
| Documents | DOCX creation/editing/rendering workflow. | Highly useful for Brainstorm and World Spec artifacts. | Installed plugin cache: `openai-primary-runtime/documents`. | Keep. Now strengthened by LibreOffice and Python packages. |
| Spreadsheets | XLSX/CSV handling. | Useful for the Task Selection tracker and future workflow mapping. | Installed plugin cache: `openai-primary-runtime/spreadsheets`. | Keep. |
| Presentations | PPTX/slide workflow. | Low usefulness for current Sanctum onboarding. | Installed plugin cache: `openai-primary-runtime/presentations`. | Keep, not needed now. |
| GitHub | Repository/PR/issue workflows. | Useful when Alexander decides to use an approved GitHub remote. Do not publish without approval. | Installed plugin cache: `openai-curated/github`. | Keep. Confirm public-safe or private-safe status before use. |
| Omni Analytics | Data and analytics connector for querying Omni through the team's semantic model and permissions. | Useful if Alexander connects an Omni workspace for structured performance or operational analytics. Not a replacement for local chart-byte verification. | Installed 2026-06-11 with `codex plugin add omni-analytics@openai-curated`; enabled in `/Users/dyrane/.codex/config.toml`. | Keep if authenticated and useful; otherwise remove. |
| Build Web Apps | Frontend app tooling. | Not needed for current Sanctum document workflow. | Installed plugin cache: `openai-curated/build-web-apps`. | Keep, no action. |
| Vercel | Deployment and web app tooling. | Not needed for Sanctum onboarding. | Installed plugin cache: `openai-curated/vercel`. | Keep, no action. |
| Stripe | Payments/business tooling. | Not needed for Sanctum onboarding. | Installed plugin cache: `openai-curated/stripe`. | Keep, no action. |

## Local Config Presence

- Codex config exists at `C:\Users\Dyrane\.codex\config.toml`.
- MCP config was audited by server/plugin names only. Secrets or token values were not copied into this repository.

## Recommendations

- Do not install additional MCPs now.
- Use Python plus Documents/Spreadsheets plugins for Sanctum artifacts.
- Use Chrome automation only after explicit authorization and bridge verification.
- Keep GitHub usage approval-gated and confirm the current tree is public-safe or private-safe before pushing.
- Re-audit MCPs if new connectors are added or if RL Studio browser operation becomes active again.
