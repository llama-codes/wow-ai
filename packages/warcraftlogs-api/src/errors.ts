export interface WarcraftLogsErrorOptions {
  cause?: unknown;
}

export class WarcraftLogsError extends Error {
  constructor(message: string, options: WarcraftLogsErrorOptions = {}) {
    super(message, { cause: options.cause });
    this.name = new.target.name;
  }
}

export class WarcraftLogsConfigError extends WarcraftLogsError {}

export class WarcraftLogsAuthError extends WarcraftLogsError {
  readonly status?: number;
  readonly responseBody?: string;

  constructor(
    message: string,
    options: WarcraftLogsErrorOptions & { status?: number; responseBody?: string } = {},
  ) {
    super(message, options);
    this.status = options.status;
    this.responseBody = options.responseBody;
  }
}

export class WarcraftLogsHttpError extends WarcraftLogsError {
  readonly operation: "graphql" | "oauth";
  readonly status: number;
  readonly statusText: string;
  readonly responseBody: string;

  constructor(
    message: string,
    options: WarcraftLogsErrorOptions & {
      operation: "graphql" | "oauth";
      status: number;
      statusText: string;
      responseBody: string;
    },
  ) {
    super(message, options);
    this.operation = options.operation;
    this.status = options.status;
    this.statusText = options.statusText;
    this.responseBody = options.responseBody;
  }
}

export interface WarcraftLogsGraphQLErrorPayload {
  message: string;
  locations?: Array<{ line: number; column: number }>;
  path?: Array<string | number>;
  extensions?: Record<string, unknown>;
}

export class WarcraftLogsGraphQLError extends WarcraftLogsError {
  readonly errors: WarcraftLogsGraphQLErrorPayload[];

  constructor(errors: WarcraftLogsGraphQLErrorPayload[]) {
    super(`Warcraft Logs GraphQL returned ${errors.length} error(s): ${errors.map((error) => error.message).join("; ")}`);
    this.errors = errors;
  }
}
