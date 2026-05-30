# @wow-ai/warcraftlogs

Small TypeScript SDK and local stdio MCP server for the public Warcraft Logs v2 GraphQL API.

This package uses the public client-credentials endpoint only:

- GraphQL: `https://www.warcraftlogs.com/api/v2/client`
- OAuth token: `https://www.warcraftlogs.com/oauth/token`

Private reports and user OAuth/PKCE are intentionally out of scope for v1.

## Setup

Create a Warcraft Logs API client at <https://www.warcraftlogs.com/api/clients>, then set credentials in the environment.

PowerShell:

```powershell
$env:WARCRAFT_LOGS_CLIENT_ID="your-client-id"
$env:WARCRAFT_LOGS_CLIENT_SECRET="your-client-secret"
```

Install and verify locally:

```powershell
npm install
npm run build
npm test
```

Optional live smoke check:

```powershell
npm run smoke:live
```

If credentials are missing, the live smoke script exits successfully after printing a skip message.

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

## MCP Usage

Build the package first:

```powershell
npm run build
```

Then configure an MCP client to launch the stdio server with Node:

```json
{
  "mcpServers": {
    "warcraftlogs": {
      "command": "node",
      "args": [
        "C:/Users/celsi/Documents/GitHub/llama-codes/wow-ai/packages/warcraftlogs-api/dist/mcp/stdio.js"
      ],
      "env": {
        "WARCRAFT_LOGS_CLIENT_ID": "your-client-id",
        "WARCRAFT_LOGS_CLIENT_SECRET": "your-client-secret"
      }
    }
  }
}
```

The server exposes:

- `wcl_rate_limit`
- `wcl_report_summary`
- `wcl_report_fights`
- `wcl_report_master_data`
- `wcl_report_events`
- `wcl_report_table`
- `wcl_report_rankings`

For stdio MCP servers, logs are written to stderr so stdout remains reserved for JSON-RPC messages.

## References

- <https://www.warcraftlogs.com/api/docs>
- <https://www.warcraftlogs.com/v2-api-docs/warcraft/>
- <https://modelcontextprotocol.io/docs/develop/build-server>
