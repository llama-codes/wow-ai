#!/usr/bin/env node
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { createWarcraftLogsMcpServer } from "./server.js";

async function main(): Promise<void> {
  const server = createWarcraftLogsMcpServer();
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Warcraft Logs MCP Server running on stdio");
}

main().catch((error: unknown) => {
  console.error("Fatal error in Warcraft Logs MCP server:", error);
  process.exit(1);
});
