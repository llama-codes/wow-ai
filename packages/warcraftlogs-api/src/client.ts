import {
  WarcraftLogsAuthError,
  WarcraftLogsConfigError,
  WarcraftLogsGraphQLError,
  WarcraftLogsGraphQLErrorPayload,
  WarcraftLogsHttpError,
} from "./errors.js";
import {
  RATE_LIMIT_QUERY,
  REPORT_EVENTS_QUERY,
  REPORT_FIGHTS_QUERY,
  REPORT_MASTER_DATA_QUERY,
  REPORT_RANKINGS_QUERY,
  REPORT_SUMMARY_QUERY,
  REPORT_TABLE_QUERY,
} from "./queries.js";
import type {
  FetchLike,
  JsonValue,
  RateLimitData,
  ReportEventPaginator,
  ReportEventsParams,
  ReportFight,
  ReportFightsParams,
  ReportLookupParams,
  ReportMasterData,
  ReportMasterDataParams,
  ReportRankingsParams,
  ReportSummary,
  ReportTableParams,
  WarcraftLogsClientConfig,
  WarcraftLogsPublicClient,
} from "./types.js";

const DEFAULT_API_URL = "https://www.warcraftlogs.com/api/v2/client";
const DEFAULT_TOKEN_URL = "https://www.warcraftlogs.com/oauth/token";
const DEFAULT_TOKEN_REFRESH_BUFFER_SECONDS = 60;

interface TokenState {
  accessToken: string;
  expiresAtMs: number;
}

interface TokenResponse {
  access_token?: string;
  expires_in?: number;
  token_type?: string;
}

interface GraphQLResponse<TData> {
  data?: TData;
  errors?: WarcraftLogsGraphQLErrorPayload[];
}

export function createWarcraftLogsClient(config: WarcraftLogsClientConfig): WarcraftLogsPublicClient {
  return new DefaultWarcraftLogsClient(config);
}

export function createWarcraftLogsClientFromEnv(
  env: NodeJS.ProcessEnv = process.env,
  config: Omit<WarcraftLogsClientConfig, "clientId" | "clientSecret"> = {},
): WarcraftLogsPublicClient {
  return createWarcraftLogsClient({
    ...config,
    clientId: env.WARCRAFT_LOGS_CLIENT_ID ?? "",
    clientSecret: env.WARCRAFT_LOGS_CLIENT_SECRET ?? "",
  });
}

class DefaultWarcraftLogsClient implements WarcraftLogsPublicClient {
  private readonly clientId: string;
  private readonly clientSecret: string;
  private readonly apiUrl: string;
  private readonly tokenUrl: string;
  private readonly fetchImpl: FetchLike;
  private readonly tokenRefreshBufferMs: number;
  private tokenState?: TokenState;
  private tokenRequestInFlight?: Promise<TokenState>;

  constructor(config: WarcraftLogsClientConfig) {
    this.clientId = config.clientId?.trim();
    this.clientSecret = config.clientSecret?.trim();
    this.apiUrl = config.apiUrl ?? DEFAULT_API_URL;
    this.tokenUrl = config.tokenUrl ?? DEFAULT_TOKEN_URL;
    this.fetchImpl = config.fetch ?? globalThis.fetch?.bind(globalThis);
    this.tokenRefreshBufferMs =
      (config.tokenRefreshBufferSeconds ?? DEFAULT_TOKEN_REFRESH_BUFFER_SECONDS) * 1000;

    if (!this.clientId) {
      throw new WarcraftLogsConfigError("Missing Warcraft Logs client ID.");
    }
    if (!this.clientSecret) {
      throw new WarcraftLogsConfigError("Missing Warcraft Logs client secret.");
    }
    if (!this.fetchImpl) {
      throw new WarcraftLogsConfigError("No fetch implementation is available.");
    }
  }

  async graphql<TData, TVariables extends object = Record<string, unknown>>(
    query: string,
    variables?: TVariables,
  ): Promise<TData> {
    try {
      return await this.executeGraphQL<TData, TVariables>(query, variables, false);
    } catch (error) {
      if (error instanceof WarcraftLogsHttpError && error.status === 401) {
        this.tokenState = undefined;
        return this.executeGraphQL<TData, TVariables>(query, variables, true);
      }
      throw error;
    }
  }

  async getRateLimit(): Promise<RateLimitData> {
    const data = await this.graphql<{ rateLimitData: RateLimitData }>(RATE_LIMIT_QUERY);
    return data.rateLimitData;
  }

  async getReportSummary(params: ReportLookupParams): Promise<ReportSummary | null> {
    const data = await this.graphql<{ reportData: { report: ReportSummary | null } }>(
      REPORT_SUMMARY_QUERY,
      cleanVariables(params),
    );
    return data.reportData.report;
  }

  async getReportFights(params: ReportFightsParams): Promise<ReportFight[]> {
    const data = await this.graphql<{ reportData: { report: { fights: ReportFight[] } | null } }>(
      REPORT_FIGHTS_QUERY,
      cleanVariables(params),
    );
    return data.reportData.report?.fights ?? [];
  }

  async getReportMasterData(params: ReportMasterDataParams): Promise<ReportMasterData | null> {
    const data = await this.graphql<{ reportData: { report: { masterData: ReportMasterData | null } | null } }>(
      REPORT_MASTER_DATA_QUERY,
      cleanVariables(params),
    );
    return data.reportData.report?.masterData ?? null;
  }

  async getReportEvents(params: ReportEventsParams): Promise<ReportEventPaginator | null> {
    const data = await this.graphql<{ reportData: { report: { events: ReportEventPaginator | null } | null } }>(
      REPORT_EVENTS_QUERY,
      cleanVariables(params),
    );
    return data.reportData.report?.events ?? null;
  }

  async getReportTable(params: ReportTableParams): Promise<JsonValue | null> {
    const data = await this.graphql<{ reportData: { report: { table: JsonValue | null } | null } }>(
      REPORT_TABLE_QUERY,
      cleanVariables(params),
    );
    return data.reportData.report?.table ?? null;
  }

  async getReportRankings(params: ReportRankingsParams): Promise<JsonValue | null> {
    const data = await this.graphql<{ reportData: { report: { rankings: JsonValue | null } | null } }>(
      REPORT_RANKINGS_QUERY,
      cleanVariables(params),
    );
    return data.reportData.report?.rankings ?? null;
  }

  private async executeGraphQL<TData, TVariables extends object>(
    query: string,
    variables: TVariables | undefined,
    forceTokenRefresh: boolean,
  ): Promise<TData> {
    const accessToken = await this.getAccessToken(forceTokenRefresh);
    const response = await this.fetchImpl(this.apiUrl, {
      method: "POST",
      headers: {
        accept: "application/json",
        authorization: `Bearer ${accessToken}`,
        "content-type": "application/json",
      },
      body: JSON.stringify({ query, variables: cleanVariables(variables) }),
    });

    if (!response.ok) {
      const responseBody = await readResponseBody(response);
      throw new WarcraftLogsHttpError(`Warcraft Logs GraphQL request failed with HTTP ${response.status}.`, {
        operation: "graphql",
        status: response.status,
        statusText: response.statusText,
        responseBody,
      });
    }

    let payload: GraphQLResponse<TData>;
    try {
      payload = (await response.json()) as GraphQLResponse<TData>;
    } catch (error) {
      throw new WarcraftLogsHttpError("Warcraft Logs GraphQL response was not valid JSON.", {
        operation: "graphql",
        status: response.status,
        statusText: response.statusText,
        responseBody: "Invalid JSON response",
        cause: error,
      });
    }

    if (payload.errors?.length) {
      throw new WarcraftLogsGraphQLError(payload.errors);
    }
    return payload.data as TData;
  }

  private async getAccessToken(forceRefresh: boolean): Promise<string> {
    if (!forceRefresh && this.tokenState && !this.isTokenExpiring(this.tokenState)) {
      return this.tokenState.accessToken;
    }
    if (!forceRefresh && this.tokenRequestInFlight) {
      return (await this.tokenRequestInFlight).accessToken;
    }

    const tokenRequest = this.requestAccessToken();
    this.tokenRequestInFlight = tokenRequest;
    try {
      const tokenState = await tokenRequest;
      this.tokenState = tokenState;
      return tokenState.accessToken;
    } finally {
      if (this.tokenRequestInFlight === tokenRequest) {
        this.tokenRequestInFlight = undefined;
      }
    }
  }

  private isTokenExpiring(token: TokenState): boolean {
    return Date.now() + this.tokenRefreshBufferMs >= token.expiresAtMs;
  }

  private async requestAccessToken(): Promise<TokenState> {
    const response = await this.fetchImpl(this.tokenUrl, {
      method: "POST",
      headers: {
        accept: "application/json",
        authorization: `Basic ${Buffer.from(`${this.clientId}:${this.clientSecret}`).toString("base64")}`,
        "content-type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({ grant_type: "client_credentials" }),
    });

    if (!response.ok) {
      const responseBody = await readResponseBody(response);
      throw new WarcraftLogsAuthError(`Warcraft Logs OAuth request failed with HTTP ${response.status}.`, {
        status: response.status,
        responseBody,
      });
    }

    let payload: TokenResponse;
    try {
      payload = (await response.json()) as TokenResponse;
    } catch (error) {
      throw new WarcraftLogsAuthError("Warcraft Logs OAuth response was not valid JSON.", { cause: error });
    }

    if (!payload.access_token) {
      throw new WarcraftLogsAuthError("Warcraft Logs OAuth response did not include an access token.");
    }

    const expiresInSeconds = payload.expires_in ?? 3600;
    return {
      accessToken: payload.access_token,
      expiresAtMs: Date.now() + expiresInSeconds * 1000,
    };
  }
}

function cleanVariables(variables?: object): Record<string, unknown> {
  return Object.fromEntries(
    Object.entries(variables ?? {}).filter(([, value]) => value !== undefined),
  );
}

async function readResponseBody(response: Response): Promise<string> {
  try {
    return await response.text();
  } catch {
    return "";
  }
}
