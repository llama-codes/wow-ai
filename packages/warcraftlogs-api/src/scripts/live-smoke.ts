import { createWarcraftLogsClientFromEnv } from "../client.js";

async function main(): Promise<void> {
  if (!process.env.WARCRAFT_LOGS_CLIENT_ID || !process.env.WARCRAFT_LOGS_CLIENT_SECRET) {
    console.error("Skipping live smoke test: WARCRAFT_LOGS_CLIENT_ID and WARCRAFT_LOGS_CLIENT_SECRET are not set.");
    return;
  }

  const client = createWarcraftLogsClientFromEnv();
  const rateLimit = await client.getRateLimit();
  console.log(JSON.stringify(rateLimit, null, 2));
}

main().catch((error: unknown) => {
  console.error("Live smoke test failed:", error);
  process.exit(1);
});
