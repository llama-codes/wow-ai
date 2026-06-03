# @wow-ai/warcraftlogs

Small TypeScript SDK and local stdio MCP server for the public Warcraft Logs v2 GraphQL API.

This package uses the public client-credentials endpoint only:

- GraphQL: `https://www.warcraftlogs.com/api/v2/client`
- OAuth token: `https://www.warcraftlogs.com/oauth/token`

Private reports and user OAuth/PKCE are intentionally out of scope for v1.

## Setup

Create a Warcraft Logs API client at <https://www.warcraftlogs.com/api/clients>.

For this local MCP setup, use a repo-local env file instead of typing secrets
into the CLI. Create `packages/warcraftlogs-api/.env.local` with your
credentials:

```dotenv
WARCRAFT_LOGS_CLIENT_ID=your-client-id
WARCRAFT_LOGS_CLIENT_SECRET=your-client-secret
```

`.env.local` is ignored by Git. The tracked `.env.local.example` file shows the
expected keys.

Install and verify locally:

```powershell
npm install
npm run build
npm test
```

Optional live smoke check:

```powershell
npm run smoke:live:local
```

If `.env.local` is missing, Node exits before the smoke script runs. If the file
exists but credentials are blank, the live smoke script exits successfully after
printing a skip message.

## SDK Usage

```ts
import { createWarcraftLogsClientFromEnv } from "@wow-ai/warcraftlogs";

const client = createWarcraftLogsClientFromEnv();

const rateLimit = await client.getRateLimit();
const summary = await client.getReportSummary({ code: "REPORT_CODE" });
const fights = await client.getReportFights({ code: "REPORT_CODE", killType: "Kills" });
const events = await client.getReportEvents({
  code: "REPORT_CODE",
  dataType: "Healing",
  fightIDs: [1],
  limit: 1000,
});
```

You can also inject credentials and `fetch` directly:

```ts
import { createWarcraftLogsClient } from "@wow-ai/warcraftlogs";

const client = createWarcraftLogsClient({
  clientId: "client-id",
  clientSecret: "client-secret",
});
```

## MCP Quick Start

The MCP server runs locally over stdio. The MCP host starts the local Node
server, the server reads Warcraft Logs credentials, and then the host receives
the `wcl_*` tools.

For this repo, prefer the tracked PowerShell launcher
`scripts/start-mcp.ps1`. It loads `packages/warcraftlogs-api/.env.local` into
the MCP process without putting secrets in `%USERPROFILE%\.codex\config.toml`.

1. Create Warcraft Logs API credentials at <https://www.warcraftlogs.com/api/clients>.

2. Put credentials in the ignored local env file:

```dotenv
WARCRAFT_LOGS_CLIENT_ID=your-client-id
WARCRAFT_LOGS_CLIENT_SECRET=your-client-secret
```

The file should live here:

```text
<repo-root>\packages\warcraftlogs-api\.env.local
```

3. Build and verify the package:

```powershell
cd <repo-root>\packages\warcraftlogs-api
npm install
npm run build
npm test
npm run smoke:live:local
```

4. Check that the MCP launcher sees the local env file without printing secret
values:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\start-mcp.ps1 -Check
```

Expected output:

```text
WARCRAFT_LOGS_CLIENT_ID=set
WARCRAFT_LOGS_CLIENT_SECRET=set
```

5. Add the MCP server to Codex Desktop config:

```text
%USERPROFILE%\.codex\config.toml
```

Use TOML, not JSON:

```toml
[mcp_servers.warcraftlogs]
command = "powershell.exe"
args = ["-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "<repo-root>/packages/warcraftlogs-api/scripts/start-mcp.ps1"]
startup_timeout_sec = 120
```

Do not add a `[mcp_servers.warcraftlogs.env]` block for these secrets. The
launcher reads `.env.local` and forwards those values only to the MCP child
process.

6. Fully restart Codex Desktop. A normal thread reload may not be enough because
MCP servers are discovered when Codex starts.

7. Verify inside Codex by asking:

```text
Use Warcraft Logs to check the API rate limit.
```

If the server is loaded, Codex should expose these tools:

- `wcl_rate_limit`
- `wcl_report_summary`
- `wcl_report_fights`
- `wcl_report_master_data`
- `wcl_report_events`
- `wcl_report_table`
- `wcl_report_rankings`

Example prompts once connected:

```text
Use Warcraft Logs to get the fights for report REPORT_CODE.
```

```text
Use Warcraft Logs to get healing events for fight 1 in report REPORT_CODE.
```

Under the hood, the MCP calls the local SDK package, which handles OAuth,
token caching, GraphQL requests, and JSON response formatting.

For stdio MCP servers, logs are written to stderr so stdout remains reserved for
JSON-RPC messages.

### Generic MCP Client Config

For MCP clients that use JSON config and do not need the PowerShell launcher,
you can launch Node directly with `--env-file`:

```json
{
  "mcpServers": {
    "warcraftlogs": {
      "command": "node",
      "args": [
        "--env-file=<repo-root>/packages/warcraftlogs-api/.env.local",
        "<repo-root>/packages/warcraftlogs-api/dist/mcp/stdio.js"
      ]
    }
  }
}
```

### Troubleshooting

- `wcl_*` tools do not appear: restart Codex Desktop after editing
  `config.toml`.
- `Missing env file`: create `.env.local` in `packages/warcraftlogs-api`, not
  the repo root.
- `WARCRAFT_LOGS_CLIENT_ID=missing`: check the variable name in `.env.local`.
- `Missing built MCP server`: run `npm run build`.
- OAuth or GraphQL auth failures: run `npm run smoke:live:local` from
  `packages/warcraftlogs-api` to validate the credentials outside MCP.
- Never commit `.env.local`; it is intentionally ignored by `.gitignore`.

## References

- <https://www.warcraftlogs.com/api/docs>
- <https://www.warcraftlogs.com/v2-api-docs/warcraft/>
- <https://modelcontextprotocol.io/docs/develop/build-server>
