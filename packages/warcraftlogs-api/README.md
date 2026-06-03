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

The MCP server runs locally over stdio. Your MCP host starts this package with
Node, loads Warcraft Logs credentials from `.env.local`, and then receives the
`wcl_*` tools.

1. Create Warcraft Logs API credentials at <https://www.warcraftlogs.com/api/clients>.

2. Put credentials in the ignored local env file:

```dotenv
WARCRAFT_LOGS_CLIENT_ID=your-client-id
WARCRAFT_LOGS_CLIENT_SECRET=your-client-secret
```

3. Build the package:

```powershell
cd C:\Users\celsi\Documents\GitHub\llama-codes\wow-ai\packages\warcraftlogs-api
npm install
npm run build
```

4. Configure your MCP client to launch the stdio server with Node's `--env-file`
flag:

```json
{
  "mcpServers": {
    "warcraftlogs": {
      "command": "node",
      "args": [
        "--env-file=C:/Users/celsi/Documents/GitHub/llama-codes/wow-ai/packages/warcraftlogs-api/.env.local",
        "C:/Users/celsi/Documents/GitHub/llama-codes/wow-ai/packages/warcraftlogs-api/dist/mcp/stdio.js"
      ]
    }
  }
}
```

5. Restart the MCP host/client so it reloads tools.

6. Test the connection with the rate-limit tool first. If this works, the
credentials, local build, and stdio transport are all good:

```text
Use Warcraft Logs to check the API rate limit.
```

The MCP server exposes:

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

For stdio MCP servers, logs are written to stderr so stdout remains reserved for JSON-RPC messages.

## References

- <https://www.warcraftlogs.com/api/docs>
- <https://www.warcraftlogs.com/v2-api-docs/warcraft/>
- <https://modelcontextprotocol.io/docs/develop/build-server>
