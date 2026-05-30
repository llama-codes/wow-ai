import { z } from "zod";
import type { WarcraftLogsPublicClient } from "../types.js";

const reportLookupShape = {
  code: z.string().min(1).describe("Warcraft Logs report code."),
  allowUnlisted: z.boolean().optional().describe("Allow access to public unlisted reports when supported."),
};

const fightFilterShape = {
  difficulty: z.number().int().optional(),
  encounterID: z.number().int().optional(),
  fightIDs: z.array(z.number().int()).optional(),
  killType: z.string().optional().describe("Warcraft Logs KillType enum value."),
  translate: z.boolean().optional(),
};

const eventFilterShape = {
  abilityID: z.number().optional(),
  dataType: z.string().optional().describe("Warcraft Logs EventDataType enum value."),
  death: z.number().int().optional(),
  difficulty: z.number().int().optional(),
  encounterID: z.number().int().optional(),
  endTime: z.number().optional(),
  fightIDs: z.array(z.number().int()).optional(),
  filterExpression: z.string().optional(),
  hostilityType: z.string().optional().describe("Warcraft Logs HostilityType enum value."),
  includeResources: z.boolean().optional(),
  killType: z.string().optional().describe("Warcraft Logs KillType enum value."),
  limit: z.number().int().positive().optional(),
  sourceAurasAbsent: z.string().optional(),
  sourceAurasPresent: z.string().optional(),
  sourceClass: z.string().optional(),
  sourceID: z.number().int().optional(),
  sourceInstanceID: z.number().int().optional(),
  startTime: z.number().optional(),
  targetAurasAbsent: z.string().optional(),
  targetAurasPresent: z.string().optional(),
  targetClass: z.string().optional(),
  targetID: z.number().int().optional(),
  targetInstanceID: z.number().int().optional(),
  translate: z.boolean().optional(),
  useAbilityIDs: z.boolean().optional(),
  useActorIDs: z.boolean().optional(),
  viewOptions: z.number().int().optional(),
  wipeCutoff: z.number().int().optional(),
};

const tableFilterShape = {
  abilityID: z.number().optional(),
  dataType: z.string().min(1).describe("Warcraft Logs TableDataType enum value."),
  death: z.number().int().optional(),
  difficulty: z.number().int().optional(),
  encounterID: z.number().int().optional(),
  endTime: z.number().optional(),
  fightIDs: z.array(z.number().int()).optional(),
  filterExpression: z.string().optional(),
  hostilityType: z.string().optional().describe("Warcraft Logs HostilityType enum value."),
  killType: z.string().optional().describe("Warcraft Logs KillType enum value."),
  sourceAurasAbsent: z.string().optional(),
  sourceAurasPresent: z.string().optional(),
  sourceClass: z.string().optional(),
  sourceID: z.number().int().optional(),
  sourceInstanceID: z.number().int().optional(),
  startTime: z.number().optional(),
  targetAurasAbsent: z.string().optional(),
  targetAurasPresent: z.string().optional(),
  targetClass: z.string().optional(),
  targetID: z.number().int().optional(),
  targetInstanceID: z.number().int().optional(),
  translate: z.boolean().optional(),
  viewOptions: z.number().int().optional(),
  viewBy: z.string().optional().describe("Warcraft Logs ViewType enum value."),
  wipeCutoff: z.number().int().optional(),
};

export const warcraftLogsToolInputSchemas = {
  wcl_rate_limit: z.object({}),
  wcl_report_summary: z.object({
    ...reportLookupShape,
  }),
  wcl_report_fights: z.object({
    ...reportLookupShape,
    ...fightFilterShape,
  }),
  wcl_report_master_data: z.object({
    ...reportLookupShape,
    translate: z.boolean().optional(),
    actorType: z.string().optional().describe("Actor type filter, for example Player, NPC, or Pet."),
    actorSubType: z.string().optional().describe("Actor subtype filter, usually a class/spec/NPC subtype."),
  }),
  wcl_report_events: z.object({
    ...reportLookupShape,
    ...eventFilterShape,
  }),
  wcl_report_table: z.object({
    ...reportLookupShape,
    ...tableFilterShape,
  }),
  wcl_report_rankings: z.object({
    ...reportLookupShape,
    compare: z.string().optional().describe("Warcraft Logs RankingCompareType enum value."),
    difficulty: z.number().int().optional(),
    encounterID: z.number().int().optional(),
    fightIDs: z.array(z.number().int()).optional(),
    playerMetric: z.string().optional().describe("Warcraft Logs ReportRankingMetricType enum value."),
    timeframe: z.string().optional().describe("Warcraft Logs RankingTimeframeType enum value."),
  }),
};

export interface McpTextResult {
  [key: string]: unknown;
  content: Array<{
    type: "text";
    text: string;
  }>;
}

export function createWarcraftLogsToolHandlers(client: WarcraftLogsPublicClient) {
  return {
    wcl_rate_limit: async (_input: z.infer<typeof warcraftLogsToolInputSchemas.wcl_rate_limit>): Promise<McpTextResult> =>
      jsonContent(await client.getRateLimit()),
    wcl_report_summary: async (
      input: z.infer<typeof warcraftLogsToolInputSchemas.wcl_report_summary>,
    ): Promise<McpTextResult> => jsonContent(await client.getReportSummary(input)),
    wcl_report_fights: async (
      input: z.infer<typeof warcraftLogsToolInputSchemas.wcl_report_fights>,
    ): Promise<McpTextResult> => jsonContent(await client.getReportFights(input)),
    wcl_report_master_data: async (
      input: z.infer<typeof warcraftLogsToolInputSchemas.wcl_report_master_data>,
    ): Promise<McpTextResult> => jsonContent(await client.getReportMasterData(input)),
    wcl_report_events: async (
      input: z.infer<typeof warcraftLogsToolInputSchemas.wcl_report_events>,
    ): Promise<McpTextResult> => jsonContent(await client.getReportEvents(input)),
    wcl_report_table: async (
      input: z.infer<typeof warcraftLogsToolInputSchemas.wcl_report_table>,
    ): Promise<McpTextResult> => jsonContent(await client.getReportTable(input)),
    wcl_report_rankings: async (
      input: z.infer<typeof warcraftLogsToolInputSchemas.wcl_report_rankings>,
    ): Promise<McpTextResult> => jsonContent(await client.getReportRankings(input)),
  };
}

function jsonContent(value: unknown): McpTextResult {
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify(value, null, 2),
      },
    ],
  };
}
