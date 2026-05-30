export type JsonValue =
  | string
  | number
  | boolean
  | null
  | JsonValue[]
  | { [key: string]: JsonValue };

export type FetchLike = (input: RequestInfo | URL, init?: RequestInit) => Promise<Response>;

export interface WarcraftLogsClientConfig {
  clientId: string;
  clientSecret: string;
  apiUrl?: string;
  tokenUrl?: string;
  fetch?: FetchLike;
  tokenRefreshBufferSeconds?: number;
}

export interface RateLimitData {
  limitPerHour: number;
  pointsSpentThisHour: number;
  pointsResetIn: number;
}

export interface ReportSummary {
  code: string;
  endTime: number;
  exportedSegments: number;
  revision: number;
  segments: number;
  startTime: number;
  title: string;
  visibility: string;
}

export interface ReportFight {
  id: number;
  name: string;
  startTime: number;
  endTime: number;
  encounterID: number;
  kill: boolean | null;
  difficulty: number | null;
}

export interface ReportAbility {
  gameID: number | null;
  icon: string | null;
  name: string | null;
  type: string | null;
}

export interface ReportActor {
  gameID: number | null;
  icon: string | null;
  id: number | null;
  name: string | null;
  petOwner: number | null;
  server: string | null;
  subType: string | null;
  type: string | null;
}

export interface ReportMasterData {
  logVersion: number;
  gameVersion: number | null;
  lang: string | null;
  abilities: ReportAbility[] | null;
  actors: ReportActor[] | null;
}

export interface ReportEventPaginator {
  data: JsonValue;
  nextPageTimestamp: number | null;
}

export type EventDataType = string;
export type HostilityType = string;
export type KillType = string;
export type TableDataType = string;
export type ViewType = string;
export type ReportRankingMetricType = string;
export type RankingTimeframeType = string;
export type RankingCompareType = string;

export interface ReportLookupParams {
  code: string;
  allowUnlisted?: boolean;
}

export interface ReportFightsParams extends ReportLookupParams {
  difficulty?: number;
  encounterID?: number;
  fightIDs?: number[];
  killType?: KillType;
  translate?: boolean;
}

export interface ReportMasterDataParams extends ReportLookupParams {
  translate?: boolean;
  actorType?: string;
  actorSubType?: string;
}

export interface ReportEventsParams extends ReportLookupParams {
  abilityID?: number;
  dataType?: EventDataType;
  death?: number;
  difficulty?: number;
  encounterID?: number;
  endTime?: number;
  fightIDs?: number[];
  filterExpression?: string;
  hostilityType?: HostilityType;
  includeResources?: boolean;
  killType?: KillType;
  limit?: number;
  sourceAurasAbsent?: string;
  sourceAurasPresent?: string;
  sourceClass?: string;
  sourceID?: number;
  sourceInstanceID?: number;
  startTime?: number;
  targetAurasAbsent?: string;
  targetAurasPresent?: string;
  targetClass?: string;
  targetID?: number;
  targetInstanceID?: number;
  translate?: boolean;
  useAbilityIDs?: boolean;
  useActorIDs?: boolean;
  viewOptions?: number;
  wipeCutoff?: number;
}

export interface ReportTableParams extends ReportLookupParams {
  abilityID?: number;
  dataType: TableDataType;
  death?: number;
  difficulty?: number;
  encounterID?: number;
  endTime?: number;
  fightIDs?: number[];
  filterExpression?: string;
  hostilityType?: HostilityType;
  killType?: KillType;
  sourceAurasAbsent?: string;
  sourceAurasPresent?: string;
  sourceClass?: string;
  sourceID?: number;
  sourceInstanceID?: number;
  startTime?: number;
  targetAurasAbsent?: string;
  targetAurasPresent?: string;
  targetClass?: string;
  targetID?: number;
  targetInstanceID?: number;
  translate?: boolean;
  viewOptions?: number;
  viewBy?: ViewType;
  wipeCutoff?: number;
}

export interface ReportRankingsParams extends ReportLookupParams {
  compare?: RankingCompareType;
  difficulty?: number;
  encounterID?: number;
  fightIDs?: number[];
  playerMetric?: ReportRankingMetricType;
  timeframe?: RankingTimeframeType;
}

export interface WarcraftLogsPublicClient {
  graphql<TData, TVariables extends object = Record<string, unknown>>(
    query: string,
    variables?: TVariables,
  ): Promise<TData>;
  getRateLimit(): Promise<RateLimitData>;
  getReportSummary(params: ReportLookupParams): Promise<ReportSummary | null>;
  getReportFights(params: ReportFightsParams): Promise<ReportFight[]>;
  getReportMasterData(params: ReportMasterDataParams): Promise<ReportMasterData | null>;
  getReportEvents(params: ReportEventsParams): Promise<ReportEventPaginator | null>;
  getReportTable(params: ReportTableParams): Promise<JsonValue | null>;
  getReportRankings(params: ReportRankingsParams): Promise<JsonValue | null>;
}
