import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createWarcraftLogsClientFromEnv } from "../dist/index.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const packageRoot = path.resolve(__dirname, "..");
const repoRoot = path.resolve(packageRoot, "..", "..");
const outputDir = path.join(repoRoot, "healing-assigments", "crown");

const reports = [
  { index: 1, code: "Q1N3nyHFLDPKvpX7", fightID: 17 },
  { index: 2, code: "MTh9DtBp6y3wPajn", fightID: 103 },
  { index: 3, code: "HmaTLwKV7Aqx81CF", fightID: 43 },
  { index: 4, code: "tJC1QWjGvLfwA7mc", fightID: 23 },
  { index: 5, code: "KLR8ta3myrAgvkDX", fightID: 55 },
  { index: 6, code: "cNrQwb2gMnk6zKmq", fightID: 42 },
];

const onlyIndexes = parseOnlyIndexes(process.argv.slice(2));
const selectedReports = onlyIndexes
  ? reports.filter((report) => onlyIndexes.has(report.index))
  : reports;

const playerClasses = new Set([
  "DeathKnight",
  "DemonHunter",
  "Druid",
  "Evoker",
  "Hunter",
  "Mage",
  "Monk",
  "Paladin",
  "Priest",
  "Rogue",
  "Shaman",
  "Warlock",
  "Warrior",
]);

const majorCooldownNames = new Set([
  "Ancestral Guidance",
  "Anti-Magic Zone",
  "Apotheosis",
  "Ascendance",
  "Aura Mastery",
  "Avenging Wrath",
  "Blessing of Sacrifice",
  "Celestial Conduit",
  "Convoke the Spirits",
  "Darkness",
  "Divine Hymn",
  "Emerald Communion",
  "Evangelism",
  "Flourish",
  "Holy Word: Salvation",
  "Incarnation: Tree of Life",
  "Invoke Chi-Ji, the Red Crane",
  "Invoke Yu'lon, the Jade Serpent",
  "Lay on Hands",
  "Life Cocoon",
  "Nature's Vigil",
  "Pain Suppression",
  "Power Word: Barrier",
  "Rallying Cry",
  "Rapture",
  "Restoral",
  "Revival",
  "Rewind",
  "Spirit Link Totem",
  "Spiritwalker's Tidal Totem",
  "Stasis",
  "Symbol of Hope",
  "Tip the Scales",
  "Tranquility",
  "Tyr's Deliverance",
  "Vaelgor's Final Stare",
  "Vampiric Embrace",
  "Zephyr",
]);

const healerOnlyCooldownNames = new Set([
  "Ancestral Guidance",
  "Apotheosis",
  "Ascendance",
  "Aura Mastery",
  "Avenging Wrath",
  "Celestial Conduit",
  "Convoke the Spirits",
  "Divine Hymn",
  "Emerald Communion",
  "Evangelism",
  "Flourish",
  "Holy Word: Salvation",
  "Incarnation: Tree of Life",
  "Invoke Chi-Ji, the Red Crane",
  "Invoke Yu'lon, the Jade Serpent",
  "Nature's Vigil",
  "Power Word: Barrier",
  "Rapture",
  "Restoral",
  "Revival",
  "Rewind",
  "Spirit Link Totem",
  "Spiritwalker's Tidal Totem",
  "Stasis",
  "Symbol of Hope",
  "Tip the Scales",
  "Tranquility",
  "Tyr's Deliverance",
  "Vaelgor's Final Stare",
]);

const healerSpecs = new Set(["Restoration", "Preservation", "Holy", "Discipline", "Mistweaver"]);

await loadEnvLocal(path.join(packageRoot, ".env.local"));

const client = createWarcraftLogsClientFromEnv();

for (const report of selectedReports) {
  console.error(`Extracting ${report.code} fight ${report.fightID}...`);
  const analysis = await extractReport(report);
  const markdown = renderMarkdown(analysis);
  const outPath = path.join(outputDir, `similar-comp-${String(report.index).padStart(2, "0")}-${report.code}-fight-${report.fightID}.md`);
  await fs.writeFile(outPath, markdown, "utf8");
  console.error(`Wrote ${path.relative(repoRoot, outPath)}`);
}

function parseOnlyIndexes(args) {
  const raw = args.find((arg) => arg.startsWith("--only="))?.slice("--only=".length);
  if (!raw) {
    return null;
  }
  return new Set(
    raw
      .split(",")
      .map((value) => Number.parseInt(value.trim(), 10))
      .filter(Number.isInteger),
  );
}

async function extractReport(reportRef) {
  const [summary, fights, masterData, healingTable, damageDoneTable] = await Promise.all([
    client.getReportSummary({ code: reportRef.code, allowUnlisted: true }),
    client.getReportFights({ code: reportRef.code, fightIDs: [reportRef.fightID], allowUnlisted: true }),
    client.getReportMasterData({ code: reportRef.code, allowUnlisted: true, translate: true }),
    client.getReportTable({ code: reportRef.code, fightIDs: [reportRef.fightID], dataType: "Healing", allowUnlisted: true }),
    client.getReportTable({ code: reportRef.code, fightIDs: [reportRef.fightID], dataType: "DamageDone", allowUnlisted: true }),
  ]);

  const fight = fights[0];
  if (!summary) {
    throw new Error(`Report ${reportRef.code} was not returned by Warcraft Logs.`);
  }
  if (!fight) {
    throw new Error(`Fight ${reportRef.fightID} was not found in report ${reportRef.code}.`);
  }
  if (!masterData) {
    throw new Error(`Master data missing for report ${reportRef.code}.`);
  }

  const actors = new Map((masterData.actors ?? []).map((actor) => [actor.id, actor]));
  const abilities = new Map((masterData.abilities ?? []).map((ability) => [ability.gameID, ability]));
  const playerIDs = new Set(
    (masterData.actors ?? [])
      .filter((actor) => actor.type === "Player" || playerClasses.has(actor.subType ?? ""))
      .map((actor) => actor.id)
      .filter((id) => id != null),
  );

  const [castEvents, damageEvents, deathEvents] = await Promise.all([
    getAllEvents({ code: reportRef.code, fightIDs: [reportRef.fightID], dataType: "Casts", allowUnlisted: true }, fight),
    getAllEvents({ code: reportRef.code, fightIDs: [reportRef.fightID], dataType: "DamageTaken", allowUnlisted: true }, fight),
    getAllEvents({ code: reportRef.code, fightIDs: [reportRef.fightID], dataType: "Deaths", allowUnlisted: true }, fight),
  ]);

  const healingEntries = tableEntries(healingTable);
  const damageDoneEntries = tableEntries(damageDoneTable);
  const healers = detectHealers(healingEntries);
  const healerNames = new Set(healers.map((healer) => healer.name));
  const roster = detectRoster(damageDoneEntries, healingEntries);
  const deaths = summarizeDeaths(deathEvents, fight, actors, abilities);
  const cooldowns = summarizeCooldownCasts(castEvents, fight, actors, abilities, playerIDs, healerNames);
  const damage = summarizeDamage(damageEvents, fight, actors, abilities, playerIDs, deaths);

  return {
    reportRef,
    sourceUrl: `https://www.warcraftlogs.com/reports/${reportRef.code}?fight=${reportRef.fightID}&type=healing`,
    summary,
    fight,
    healers,
    roster,
    deaths,
    cooldowns,
    damage,
  };
}

async function getAllEvents(params, fight) {
  const events = [];
  let startTime = fight.startTime;
  const endTime = fight.endTime;
  const seenPages = new Set();

  for (let page = 0; page < 50; page += 1) {
    const pageKey = `${params.dataType}:${startTime}`;
    if (seenPages.has(pageKey)) {
      break;
    }
    seenPages.add(pageKey);

    const result = await client.getReportEvents({
      ...params,
      startTime,
      endTime,
      limit: 10000,
      translate: true,
      useActorIDs: true,
      useAbilityIDs: true,
    });
    const data = Array.isArray(result?.data) ? result.data : [];
    events.push(...data);

    if (!result?.nextPageTimestamp || result.nextPageTimestamp >= endTime) {
      break;
    }
    startTime = result.nextPageTimestamp;
  }

  return events;
}

function tableEntries(table) {
  return table?.data?.entries && Array.isArray(table.data.entries) ? table.data.entries : [];
}

function detectHealers(entries) {
  return entries
    .filter((entry) => healerSpecs.has(specFromIcon(entry.icon)))
    .sort((a, b) => (b.total ?? 0) - (a.total ?? 0))
    .map((entry) => ({
      name: entry.name,
      className: entry.type,
      spec: specFromIcon(entry.icon),
      total: entry.total ?? 0,
      overheal: entry.overheal ?? 0,
      activeTime: entry.activeTime ?? 0,
    }));
}

function detectRoster(damageEntries, healingEntries) {
  const byName = new Map();
  for (const entry of [...damageEntries, ...healingEntries]) {
    if (!entry?.name || !playerClasses.has(entry.type)) {
      continue;
    }
    const current = byName.get(entry.name);
    if (!current || (!current.icon && entry.icon)) {
      byName.set(entry.name, {
        name: entry.name,
        className: entry.type,
        spec: specFromIcon(entry.icon),
      });
    }
  }

  return [...byName.values()].sort((a, b) => {
    const left = `${a.className}-${a.spec}-${a.name}`;
    const right = `${b.className}-${b.spec}-${b.name}`;
    return left.localeCompare(right);
  });
}

function summarizeCooldownCasts(events, fight, actors, abilities, playerIDs, healerNames) {
  const raw = events
    .filter((event) => event.type === "cast" || event.type === "begincast")
    .filter((event) => playerIDs.has(event.sourceID))
    .map((event) => {
      const abilityName = abilityNameFor(event.abilityGameID, abilities);
      const actor = actors.get(event.sourceID);
      return {
        timestamp: event.timestamp,
        seconds: Math.max(0, (event.timestamp - fight.startTime) / 1000),
        player: actor?.name ?? `actor ${event.sourceID}`,
        className: actor?.subType ?? actor?.type ?? "",
        ability: abilityName,
      };
    })
    .filter((event) => majorCooldownNames.has(event.ability))
    .filter((event) => !healerOnlyCooldownNames.has(event.ability) || healerNames.has(event.player))
    .sort((a, b) => a.timestamp - b.timestamp || a.player.localeCompare(b.player) || a.ability.localeCompare(b.ability));

  const collapsed = [];
  const lastByPlayerAbility = new Map();
  for (const event of raw) {
    const key = `${event.player}:${event.ability}`;
    const previousSecond = lastByPlayerAbility.get(key);
    if (previousSecond != null && Math.abs(previousSecond - event.seconds) <= 10) {
      continue;
    }
    collapsed.push(event);
    lastByPlayerAbility.set(key, event.seconds);
  }
  return collapsed;
}

function summarizeDamage(events, fight, actors, abilities, playerIDs, deaths) {
  const bucketSize = 10;
  const buckets = new Map();
  const abilityTotals = new Map();

  for (const event of events) {
    if (event.type !== "damage" || !playerIDs.has(event.targetID) || event.abilityGameID === 1) {
      continue;
    }

    const amount = Number(event.amount ?? 0);
    const absorbed = Number(event.absorbed ?? 0);
    const totalPressure = amount + absorbed;
    if (totalPressure <= 0) {
      continue;
    }

    const seconds = Math.max(0, (event.timestamp - fight.startTime) / 1000);
    const bucketStart = Math.floor(seconds / bucketSize) * bucketSize;
    const ability = abilityNameFor(event.abilityGameID, abilities);

    const bucket = buckets.get(bucketStart) ?? {
      start: bucketStart,
      end: bucketStart + bucketSize,
      amount: 0,
      absorbed: 0,
      abilities: new Map(),
    };
    bucket.amount += amount;
    bucket.absorbed += absorbed;
    bucket.abilities.set(ability, (bucket.abilities.get(ability) ?? 0) + totalPressure);
    buckets.set(bucketStart, bucket);

    const total = abilityTotals.get(ability) ?? { ability, amount: 0, absorbed: 0, count: 0 };
    total.amount += amount;
    total.absorbed += absorbed;
    total.count += 1;
    abilityTotals.set(ability, total);
  }

  const deathByBucket = new Map();
  for (const death of deaths) {
    const bucketStart = Math.floor(death.seconds / bucketSize) * bucketSize;
    const list = deathByBucket.get(bucketStart) ?? [];
    list.push(death.player);
    deathByBucket.set(bucketStart, list);
  }

  const spikeWindows = [...buckets.values()]
    .map((bucket) => ({
      ...bucket,
      pressure: bucket.amount + bucket.absorbed,
      topAbilities: [...bucket.abilities.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 3)
        .map(([ability, total]) => ({ ability, total })),
      deaths: deathByBucket.get(bucket.start) ?? [],
    }))
    .sort((a, b) => b.pressure - a.pressure)
    .slice(0, 8)
    .sort((a, b) => a.start - b.start);

  const topAbilities = [...abilityTotals.values()]
    .map((entry) => ({ ...entry, pressure: entry.amount + entry.absorbed }))
    .sort((a, b) => b.pressure - a.pressure)
    .slice(0, 10);

  return { spikeWindows, topAbilities };
}

function summarizeDeaths(events, fight, actors, abilities) {
  return events
    .filter((event) => event.type === "death")
    .map((event) => ({
      seconds: Math.max(0, (event.timestamp - fight.startTime) / 1000),
      player: actors.get(event.targetID)?.name ?? `actor ${event.targetID}`,
      killingAbility: abilityNameFor(event.killingAbilityGameID ?? event.abilityGameID, abilities),
      killer: actors.get(event.killerID)?.name ?? "",
    }))
    .sort((a, b) => a.seconds - b.seconds);
}

function renderMarkdown(analysis) {
  const duration = (analysis.fight.endTime - analysis.fight.startTime) / 1000;
  const rosterBySpec = countBy(analysis.roster.map((player) => `${player.spec || "Unknown"} ${spacedClass(player.className)}`.trim()));

  return [
    `# Crown Similar Comp Report ${String(analysis.reportRef.index).padStart(2, "0")}`,
    "",
    "## Source",
    "",
    `- Report: ${analysis.sourceUrl}`,
    `- Title: ${analysis.summary.title}`,
    `- Fight: ${analysis.fight.name} (${analysis.fight.kill ? "kill" : "wipe"}, Mythic/difficulty ${analysis.fight.difficulty})`,
    `- Duration: ${formatTime(duration)}`,
    "",
    "## Assignment Snapshot",
    "",
    `- Healers detected: ${analysis.healers.length ? analysis.healers.map((healer) => `${healer.name} (${healer.spec} ${spacedClass(healer.className)})`).join(", ") : "none detected from healing table"}`,
    `- Raid size detected: ${analysis.roster.length}`,
    `- Deaths: ${analysis.deaths.length}`,
    `- Major cooldown casts found: ${analysis.cooldowns.length}`,
    "",
    "## Healer Throughput",
    "",
    table(
      ["Healer", "Spec", "Healing", "Overheal"],
      analysis.healers.map((healer) => [
        healer.name,
        `${healer.spec} ${spacedClass(healer.className)}`,
        formatNumber(healer.total),
        formatPercent(healer.overheal / Math.max(1, healer.total + healer.overheal)),
      ]),
      "No healer entries detected.",
    ),
    "",
    "## Major Cooldown Timeline",
    "",
    table(
      ["Time", "Player", "Cooldown"],
      analysis.cooldowns.map((cooldown) => [formatTime(cooldown.seconds), cooldown.player, cooldown.ability]),
      "No major cooldown casts matched the tracked list.",
    ),
    "",
    "## Highest Raid-Damage Windows",
    "",
    table(
      ["Window", "Pressure", "Top sources", "Deaths"],
      analysis.damage.spikeWindows.map((window) => [
        `${formatTime(window.start)}-${formatTime(window.end)}`,
        formatNumber(window.pressure),
        window.topAbilities.map((entry) => `${entry.ability} (${formatNumber(entry.total)})`).join("; "),
        window.deaths.join(", ") || "-",
      ]),
      "No damage events returned.",
    ),
    "",
    "## Top Damage Sources",
    "",
    table(
      ["Ability", "Pressure", "Hits"],
      analysis.damage.topAbilities.map((entry) => [entry.ability, formatNumber(entry.pressure), formatNumber(entry.count)]),
      "No damage source data returned.",
    ),
    "",
    "## Deaths",
    "",
    table(
      ["Time", "Player", "Killing ability", "Killer"],
      analysis.deaths.map((death) => [formatTime(death.seconds), death.player, death.killingAbility, death.killer || "-"]),
      "No deaths recorded.",
    ),
    "",
    "## Roster Snapshot",
    "",
    table(
      ["Spec/Class", "Count"],
      [...rosterBySpec.entries()].sort((a, b) => a[0].localeCompare(b[0])).map(([spec, count]) => [spec, String(count)]),
      "No roster entries detected.",
    ),
    "",
    "## Notes For Assignment Work",
    "",
    "- Use the cooldown timeline as evidence for realistic similar-comp assignments, not as a final plan.",
    "- Damage windows are 10-second buckets using actual damage plus absorbs, with melee excluded so boss/mechanic pressure is easier to see.",
    "- Some externals or personals may be absent if Warcraft Logs records them as buffs rather than casts.",
    "",
  ].join("\n");
}

async function loadEnvLocal(envPath) {
  let contents;
  try {
    contents = await fs.readFile(envPath, "utf8");
  } catch {
    return;
  }

  for (const rawLine of contents.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) {
      continue;
    }

    const normalized = line.replace(/^export\s+/, "");
    const separator = normalized.indexOf("=");
    if (separator < 1) {
      continue;
    }

    const name = normalized.slice(0, separator).trim();
    let value = normalized.slice(separator + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    process.env[name] = process.env[name] ?? value;
  }
}

function abilityNameFor(id, abilities) {
  if (id == null || id === 0) {
    return "Unknown";
  }
  return abilities.get(id)?.name ?? `ability ${id}`;
}

function specFromIcon(icon) {
  if (!icon || !icon.includes("-")) {
    return "";
  }
  return icon.split("-").slice(1).join(" ");
}

function spacedClass(className) {
  return String(className ?? "").replace(/([a-z])([A-Z])/g, "$1 $2");
}

function formatTime(totalSeconds) {
  const seconds = Math.max(0, Math.round(totalSeconds));
  const minutes = Math.floor(seconds / 60);
  const remainder = seconds % 60;
  return `${String(minutes).padStart(2, "0")}:${String(remainder).padStart(2, "0")}`;
}

function formatNumber(value) {
  return Math.round(Number(value ?? 0)).toLocaleString("en-US");
}

function formatPercent(value) {
  return `${Math.round(value * 100)}%`;
}

function table(headers, rows, emptyText) {
  if (!rows.length) {
    return emptyText;
  }
  const header = `| ${headers.join(" | ")} |`;
  const separator = `| ${headers.map(() => "---").join(" | ")} |`;
  const body = rows.map((row) => `| ${row.map(escapeCell).join(" | ")} |`);
  return [header, separator, ...body].join("\n");
}

function escapeCell(value) {
  return String(value ?? "").replace(/\|/g, "\\|");
}

function countBy(values) {
  const counts = new Map();
  for (const value of values) {
    counts.set(value, (counts.get(value) ?? 0) + 1);
  }
  return counts;
}
