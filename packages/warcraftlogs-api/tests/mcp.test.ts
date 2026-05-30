import { describe, expect, it, vi } from "vitest";
import { createWarcraftLogsToolHandlers, warcraftLogsToolInputSchemas } from "../src/mcp/tools.js";
import type { WarcraftLogsPublicClient } from "../src/index.js";

describe("Warcraft Logs MCP schemas", () => {
  it("validates required report inputs", () => {
    expect(warcraftLogsToolInputSchemas.wcl_report_summary.safeParse({}).success).toBe(false);
    expect(warcraftLogsToolInputSchemas.wcl_report_summary.safeParse({ code: "abc123" }).success).toBe(true);
  });

  it("requires table data type", () => {
    expect(warcraftLogsToolInputSchemas.wcl_report_table.safeParse({ code: "abc123" }).success).toBe(false);
    expect(warcraftLogsToolInputSchemas.wcl_report_table.safeParse({ code: "abc123", dataType: "DamageDone" }).success).toBe(true);
  });
});

describe("Warcraft Logs MCP handlers", () => {
  it("returns rate-limit data as JSON text", async () => {
    const client = createMockClient();
    client.getRateLimit = vi.fn(async () => ({
      limitPerHour: 3600,
      pointsSpentThisHour: 5,
      pointsResetIn: 1200,
    }));
    const handlers = createWarcraftLogsToolHandlers(client);

    const result = await handlers.wcl_rate_limit({});

    expect(client.getRateLimit).toHaveBeenCalledWith();
    expect(JSON.parse(result.content[0]?.text ?? "")).toEqual({
      limitPerHour: 3600,
      pointsSpentThisHour: 5,
      pointsResetIn: 1200,
    });
  });

  it("passes report summary inputs through to the SDK client", async () => {
    const client = createMockClient();
    client.getReportSummary = vi.fn(async () => ({
      code: "abc123",
      endTime: 200,
      exportedSegments: 1,
      revision: 2,
      segments: 1,
      startTime: 100,
      title: "Raid Night",
      visibility: "public",
    }));
    const handlers = createWarcraftLogsToolHandlers(client);

    const result = await handlers.wcl_report_summary({ code: "abc123", allowUnlisted: true });

    expect(client.getReportSummary).toHaveBeenCalledWith({ code: "abc123", allowUnlisted: true });
    expect(JSON.parse(result.content[0]?.text ?? "")).toMatchObject({ code: "abc123", title: "Raid Night" });
  });

  it("passes event filters through to the SDK client", async () => {
    const client = createMockClient();
    client.getReportEvents = vi.fn(async () => ({
      data: [{ timestamp: 1000, type: "heal" }],
      nextPageTimestamp: null,
    }));
    const handlers = createWarcraftLogsToolHandlers(client);

    const input = {
      code: "abc123",
      dataType: "Healing",
      fightIDs: [1, 2],
      sourceID: 7,
      limit: 100,
    };
    const result = await handlers.wcl_report_events(input);

    expect(client.getReportEvents).toHaveBeenCalledWith(input);
    expect(JSON.parse(result.content[0]?.text ?? "")).toEqual({
      data: [{ timestamp: 1000, type: "heal" }],
      nextPageTimestamp: null,
    });
  });
});

function createMockClient(): WarcraftLogsPublicClient {
  return {
    graphql: vi.fn(),
    getRateLimit: vi.fn(),
    getReportSummary: vi.fn(),
    getReportFights: vi.fn(),
    getReportMasterData: vi.fn(),
    getReportEvents: vi.fn(),
    getReportTable: vi.fn(),
    getReportRankings: vi.fn(),
  } as unknown as WarcraftLogsPublicClient;
}
