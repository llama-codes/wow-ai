import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { createWarcraftLogsClientFromEnv } from "../client.js";
import type { WarcraftLogsPublicClient } from "../types.js";
import { createWarcraftLogsToolHandlers, warcraftLogsToolInputSchemas } from "./tools.js";

export interface WarcraftLogsMcpServerOptions {
  client?: WarcraftLogsPublicClient;
}

export function createWarcraftLogsMcpServer(options: WarcraftLogsMcpServerOptions = {}): McpServer {
  const client = options.client ?? createWarcraftLogsClientFromEnv();
  const handlers = createWarcraftLogsToolHandlers(client);
  const server = new McpServer({
    name: "warcraftlogs",
    version: "0.1.0",
  });

  server.registerTool(
    "wcl_rate_limit",
    {
      description: "Get current Warcraft Logs API rate-limit usage for these credentials.",
      inputSchema: warcraftLogsToolInputSchemas.wcl_rate_limit.shape,
    },
    (input) => handlers.wcl_rate_limit(input),
  );

  server.registerTool(
    "wcl_report_summary",
    {
      description: "Get public summary metadata for a Warcraft Logs report.",
      inputSchema: warcraftLogsToolInputSchemas.wcl_report_summary.shape,
    },
    (input) => handlers.wcl_report_summary(input),
  );

  server.registerTool(
    "wcl_report_fights",
    {
      description: "Get fights from a Warcraft Logs report, optionally filtered by encounter, difficulty, fight IDs, or kill type.",
      inputSchema: warcraftLogsToolInputSchemas.wcl_report_fights.shape,
    },
    (input) => handlers.wcl_report_fights(input),
  );

  server.registerTool(
    "wcl_report_master_data",
    {
      description: "Get report master data, including actors and abilities, from a Warcraft Logs report.",
      inputSchema: warcraftLogsToolInputSchemas.wcl_report_master_data.shape,
    },
    (input) => handlers.wcl_report_master_data(input),
  );

  server.registerTool(
    "wcl_report_events",
    {
      description: "Get paginated event data from a Warcraft Logs report.",
      inputSchema: warcraftLogsToolInputSchemas.wcl_report_events.shape,
    },
    (input) => handlers.wcl_report_events(input),
  );

  server.registerTool(
    "wcl_report_table",
    {
      description: "Get a Warcraft Logs report table, such as damage, healing, casts, buffs, or deaths.",
      inputSchema: warcraftLogsToolInputSchemas.wcl_report_table.shape,
    },
    (input) => handlers.wcl_report_table(input),
  );

  server.registerTool(
    "wcl_report_rankings",
    {
      description: "Get rankings data from a Warcraft Logs report.",
      inputSchema: warcraftLogsToolInputSchemas.wcl_report_rankings.shape,
    },
    (input) => handlers.wcl_report_rankings(input),
  );

  return server;
}

export { createWarcraftLogsToolHandlers, warcraftLogsToolInputSchemas } from "./tools.js";
