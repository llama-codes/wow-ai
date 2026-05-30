import { describe, expect, it, vi } from "vitest";
import {
  createWarcraftLogsClient,
  createWarcraftLogsClientFromEnv,
  WarcraftLogsAuthError,
  WarcraftLogsConfigError,
  WarcraftLogsGraphQLError,
  WarcraftLogsHttpError,
} from "../src/index.js";
import type { FetchLike } from "../src/index.js";

describe("Warcraft Logs client auth", () => {
  it("reads credentials from env and rejects missing values", () => {
    expect(() => createWarcraftLogsClientFromEnv({})).toThrow(WarcraftLogsConfigError);
    expect(() =>
      createWarcraftLogsClientFromEnv({
        WARCRAFT_LOGS_CLIENT_ID: "client-id",
        WARCRAFT_LOGS_CLIENT_SECRET: "client-secret",
      }),
    ).not.toThrow();
  });

  it("caches access tokens across requests", async () => {
    const fetchMock = vi.fn(async (input: RequestInfo | URL) => {
      if (String(input).includes("/oauth/token")) {
        return jsonResponse({ access_token: "token-1", expires_in: 3600 });
      }
      return jsonResponse({ data: { rateLimitData: rateLimitFixture } });
    }) as unknown as FetchLike;
    const client = createWarcraftLogsClient({
      clientId: "client-id",
      clientSecret: "client-secret",
      fetch: fetchMock,
    });

    await client.getRateLimit();
    await client.getRateLimit();

    const tokenCalls = fetchMockMockCalls(fetchMock).filter(([input]) => String(input).includes("/oauth/token"));
    expect(tokenCalls).toHaveLength(1);
    expect(tokenCalls[0]?.[1]?.headers).toMatchObject({
      authorization: `Basic ${Buffer.from("client-id:client-secret").toString("base64")}`,
      "content-type": "application/x-www-form-urlencoded",
    });
    expect(tokenCalls[0]?.[1]?.body).toBeInstanceOf(URLSearchParams);
  });

  it("dedupes concurrent token requests", async () => {
    let resolveToken!: (response: Response) => void;
    const tokenResponse = new Promise<Response>((resolve) => {
      resolveToken = resolve;
    });
    const fetchMock = vi.fn(async (input: RequestInfo | URL) => {
      if (String(input).includes("/oauth/token")) {
        return tokenResponse;
      }
      return jsonResponse({ data: { rateLimitData: rateLimitFixture } });
    }) as unknown as FetchLike;
    const client = createWarcraftLogsClient({
      clientId: "client-id",
      clientSecret: "client-secret",
      fetch: fetchMock,
    });

    const first = client.getRateLimit();
    const second = client.getRateLimit();
    await Promise.resolve();

    expect(fetchMock).toHaveBeenCalledTimes(1);
    resolveToken(jsonResponse({ access_token: "token-1", expires_in: 3600 }));

    await expect(Promise.all([first, second])).resolves.toEqual([rateLimitFixture, rateLimitFixture]);
    const tokenCalls = fetchMockMockCalls(fetchMock).filter(([input]) => String(input).includes("/oauth/token"));
    expect(tokenCalls).toHaveLength(1);
  });

  it("refreshes the token once after a GraphQL 401", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(jsonResponse({ access_token: "expired-token", expires_in: 3600 }))
      .mockResolvedValueOnce(textResponse("expired", { status: 401, statusText: "Unauthorized" }))
      .mockResolvedValueOnce(jsonResponse({ access_token: "fresh-token", expires_in: 3600 }))
      .mockResolvedValueOnce(jsonResponse({ data: { rateLimitData: rateLimitFixture } })) as unknown as FetchLike;
    const client = createWarcraftLogsClient({
      clientId: "client-id",
      clientSecret: "client-secret",
      fetch: fetchMock,
    });

    await expect(client.getRateLimit()).resolves.toEqual(rateLimitFixture);

    const graphQLCalls = fetchMockMockCalls(fetchMock).filter(([input]) => !String(input).includes("/oauth/token"));
    expect(graphQLCalls).toHaveLength(2);
    expect(graphQLCalls[0]?.[1]?.headers).toMatchObject({ authorization: "Bearer expired-token" });
    expect(graphQLCalls[1]?.[1]?.headers).toMatchObject({ authorization: "Bearer fresh-token" });
  });
});

describe("Warcraft Logs client errors", () => {
  it("maps OAuth failures to auth errors", async () => {
    const fetchMock = vi.fn(async () => textResponse("bad credentials", { status: 401, statusText: "Unauthorized" })) as unknown as FetchLike;
    const client = createWarcraftLogsClient({
      clientId: "client-id",
      clientSecret: "client-secret",
      fetch: fetchMock,
    });

    await expect(client.getRateLimit()).rejects.toBeInstanceOf(WarcraftLogsAuthError);
  });

  it("maps GraphQL HTTP failures to HTTP errors", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(jsonResponse({ access_token: "token-1", expires_in: 3600 }))
      .mockResolvedValueOnce(textResponse("server error", { status: 500, statusText: "Internal Server Error" })) as unknown as FetchLike;
    const client = createWarcraftLogsClient({
      clientId: "client-id",
      clientSecret: "client-secret",
      fetch: fetchMock,
    });

    await expect(client.getRateLimit()).rejects.toBeInstanceOf(WarcraftLogsHttpError);
  });

  it("maps GraphQL response errors to GraphQL errors", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce(jsonResponse({ access_token: "token-1", expires_in: 3600 }))
      .mockResolvedValueOnce(jsonResponse({ errors: [{ message: "Unknown field" }] })) as unknown as FetchLike;
    const client = createWarcraftLogsClient({
      clientId: "client-id",
      clientSecret: "client-secret",
      fetch: fetchMock,
    });

    await expect(client.getRateLimit()).rejects.toBeInstanceOf(WarcraftLogsGraphQLError);
  });
});

describe("Warcraft Logs wrapper methods", () => {
  it("gets rate-limit data", async () => {
    const { client, graphqlBodies } = createMockedClient({ rateLimitData: rateLimitFixture });

    await expect(client.getRateLimit()).resolves.toEqual(rateLimitFixture);

    expect(graphqlBodies[0]?.query).toContain("WarcraftLogsRateLimit");
  });

  it("gets report summaries", async () => {
    const report = {
      code: "abc123",
      endTime: 200,
      exportedSegments: 1,
      revision: 3,
      segments: 1,
      startTime: 100,
      title: "Raid Night",
      visibility: "public",
    };
    const { client, graphqlBodies } = createMockedClient({ reportData: { report } });

    await expect(client.getReportSummary({ code: "abc123", allowUnlisted: true })).resolves.toEqual(report);

    expect(graphqlBodies[0]?.query).toContain("WarcraftLogsReportSummary");
    expect(graphqlBodies[0]?.variables).toEqual({ code: "abc123", allowUnlisted: true });
  });

  it("gets report fights", async () => {
    const fights = [{ id: 1, name: "Boss", startTime: 10, endTime: 20, encounterID: 99, kill: true, difficulty: 5 }];
    const { client, graphqlBodies } = createMockedClient({ reportData: { report: { fights } } });

    await expect(client.getReportFights({ code: "abc123", fightIDs: [1], killType: "Kills" })).resolves.toEqual(fights);

    expect(graphqlBodies[0]?.query).toContain("WarcraftLogsReportFights");
    expect(graphqlBodies[0]?.variables).toEqual({ code: "abc123", fightIDs: [1], killType: "Kills" });
  });

  it("gets report master data", async () => {
    const masterData = {
      logVersion: 1,
      gameVersion: 120000,
      lang: "en",
      abilities: [{ gameID: 1, icon: "spell.jpg", name: "Spell", type: "Ability" }],
      actors: [{ gameID: 2, icon: "mage.jpg", id: 3, name: "Mage", petOwner: null, server: "realm", subType: "Mage", type: "Player" }],
    };
    const { client, graphqlBodies } = createMockedClient({ reportData: { report: { masterData } } });

    await expect(client.getReportMasterData({ code: "abc123", actorType: "Player", translate: true })).resolves.toEqual(masterData);

    expect(graphqlBodies[0]?.query).toContain("WarcraftLogsReportMasterData");
    expect(graphqlBodies[0]?.variables).toEqual({ code: "abc123", actorType: "Player", translate: true });
  });

  it("gets report events", async () => {
    const events = { data: [{ timestamp: 10, type: "cast" }], nextPageTimestamp: 12345 };
    const { client, graphqlBodies } = createMockedClient({ reportData: { report: { events } } });

    await expect(
      client.getReportEvents({
        code: "abc123",
        dataType: "Casts",
        fightIDs: [4],
        startTime: 100,
        endTime: 200,
        limit: 100,
        translate: undefined,
      }),
    ).resolves.toEqual(events);

    expect(graphqlBodies[0]?.query).toContain("WarcraftLogsReportEvents");
    expect(graphqlBodies[0]?.variables).toEqual({
      code: "abc123",
      dataType: "Casts",
      fightIDs: [4],
      startTime: 100,
      endTime: 200,
      limit: 100,
    });
  });

  it("gets report tables", async () => {
    const table = { entries: [{ name: "Player", total: 5000 }] };
    const { client, graphqlBodies } = createMockedClient({ reportData: { report: { table } } });

    await expect(client.getReportTable({ code: "abc123", dataType: "DamageDone", encounterID: 99 })).resolves.toEqual(table);

    expect(graphqlBodies[0]?.query).toContain("WarcraftLogsReportTable");
    expect(graphqlBodies[0]?.variables).toEqual({ code: "abc123", dataType: "DamageDone", encounterID: 99 });
  });

  it("gets report rankings", async () => {
    const rankings = { data: [{ name: "Player", rankPercent: 95 }] };
    const { client, graphqlBodies } = createMockedClient({ reportData: { report: { rankings } } });

    await expect(client.getReportRankings({ code: "abc123", playerMetric: "hps", timeframe: "Historical" })).resolves.toEqual(rankings);

    expect(graphqlBodies[0]?.query).toContain("WarcraftLogsReportRankings");
    expect(graphqlBodies[0]?.variables).toEqual({ code: "abc123", playerMetric: "hps", timeframe: "Historical" });
  });
});

const rateLimitFixture = {
  limitPerHour: 3600,
  pointsSpentThisHour: 12.5,
  pointsResetIn: 1800,
};

interface GraphQLBody {
  query: string;
  variables?: Record<string, unknown>;
}

function createMockedClient(graphqlData: unknown): {
  client: ReturnType<typeof createWarcraftLogsClient>;
  graphqlBodies: GraphQLBody[];
} {
  const graphqlBodies: GraphQLBody[] = [];
  const fetchMock = vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
    if (String(input).includes("/oauth/token")) {
      return jsonResponse({ access_token: "token-1", expires_in: 3600 });
    }
    graphqlBodies.push(JSON.parse(String(init?.body)) as GraphQLBody);
    return jsonResponse({ data: graphqlData });
  }) as unknown as FetchLike;

  return {
    client: createWarcraftLogsClient({
      clientId: "client-id",
      clientSecret: "client-secret",
      fetch: fetchMock,
    }),
    graphqlBodies,
  };
}

function jsonResponse(body: unknown, init: { status?: number; statusText?: string } = {}): Response {
  const status = init.status ?? 200;
  return {
    ok: status >= 200 && status < 300,
    status,
    statusText: init.statusText ?? "OK",
    json: vi.fn(async () => body),
    text: vi.fn(async () => JSON.stringify(body)),
  } as unknown as Response;
}

function textResponse(text: string, init: { status?: number; statusText?: string } = {}): Response {
  const status = init.status ?? 200;
  return {
    ok: status >= 200 && status < 300,
    status,
    statusText: init.statusText ?? "OK",
    json: vi.fn(async () => {
      throw new Error("Not JSON");
    }),
    text: vi.fn(async () => text),
  } as unknown as Response;
}

function fetchMockMockCalls(fetchMock: FetchLike): Array<[RequestInfo | URL, RequestInit | undefined]> {
  return (fetchMock as unknown as ReturnType<typeof vi.fn>).mock.calls as Array<[RequestInfo | URL, RequestInit | undefined]>;
}
