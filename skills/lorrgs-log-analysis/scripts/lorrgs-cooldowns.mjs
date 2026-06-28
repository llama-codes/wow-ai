#!/usr/bin/env node

const args = process.argv.slice(2);

function take(flag, fallback = undefined) {
  const index = args.indexOf(flag);
  if (index === -1) return fallback;
  return args[index + 1];
}

function takeAll(flag) {
  const values = [];
  for (let i = 0; i < args.length; i++) {
    if (args[i] === flag && args[i + 1]) values.push(args[i + 1]);
  }
  return values;
}

function parseSpec(value) {
  const [slug, rawAbilities = ""] = value.split(":");
  if (!slug) throw new Error(`Invalid --spec value: ${value}`);
  const abilities = new Map();
  for (const entry of rawAbilities.split(",").filter(Boolean)) {
    const [id, name] = entry.split("=");
    if (!id || !name) throw new Error(`Invalid ability mapping in --spec ${slug}: ${entry}`);
    abilities.set(Number(id), name);
  }
  return { slug, abilities };
}

function fmt(ms) {
  const seconds = Math.round(ms / 1000);
  const minutes = Math.floor(seconds / 60);
  return `${String(minutes).padStart(2, "0")}:${String(seconds % 60).padStart(2, "0")}`;
}

function bucket(ms, bucketSeconds) {
  const start = Math.floor(ms / 1000 / bucketSeconds) * bucketSeconds;
  const end = start + bucketSeconds - 1;
  return `${String(Math.floor(start / 60)).padStart(2, "0")}:${String(start % 60).padStart(2, "0")}-${String(Math.floor(end / 60)).padStart(2, "0")}:${String(end % 60).padStart(2, "0")}`;
}

async function getJson(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error(`${response.status} ${response.statusText}: ${url}`);
  return response.json();
}

const boss = take("--boss");
const difficulty = take("--difficulty", "mythic");
const metric = take("--metric", "hps");
const top = Number(take("--top", "50"));
const bucketSeconds = Number(take("--bucket-seconds", "10"));
const exampleCount = Number(take("--examples", "5"));
const specValues = takeAll("--spec");

if (!boss || specValues.length === 0) {
  console.error(`Usage:
node lorrgs-cooldowns.mjs --boss beloren-child-of-alar --difficulty mythic --metric hps --top 50 \\
  --spec "priest-holy:64843=Divine Hymn,200183=Apotheosis"`);
  process.exit(1);
}

const specs = specValues.map(parseSpec);
const base = "https://api2.lorrgs.io";

console.log("# Lorrgs Cooldown Summary");
console.log();
console.log(`Boss: \`${boss}\``);
console.log(`Difficulty: \`${difficulty}\``);
console.log(`Metric: \`${metric}\``);
console.log(`Top parses per spec: \`${top}\``);
console.log(`Bucket size: \`${bucketSeconds}s\``);

for (const spec of specs) {
  const url = `${base}/api/spec_ranking/${spec.slug}/${boss}?difficulty=${encodeURIComponent(difficulty)}&metric=${encodeURIComponent(metric)}`;
  const data = await getJson(url);
  const reports = (data.reports || []).slice(0, top);
  const events = [];
  const examples = [];

  for (let rankIndex = 0; rankIndex < reports.length; rankIndex++) {
    const report = reports[rankIndex];
    for (const fight of report.fights || []) {
      const player = (fight.players || []).find((candidate) => candidate.spec_slug === spec.slug) || (fight.players || [])[0];
      if (!player) continue;

      const watched = (player.casts || [])
        .filter((cast) => spec.abilities.has(Number(cast.id)))
        .map((cast) => ({
          id: Number(cast.id),
          name: spec.abilities.get(Number(cast.id)),
          ms: cast.ts,
          time: fmt(cast.ts),
          rank: rankIndex + 1,
          report: report.report_id,
          fight: fight.fight_id,
          duration: fmt(fight.duration),
        }));

      watched.forEach((event) => events.push(event));
      if (examples.length < exampleCount) {
        examples.push({
          rank: rankIndex + 1,
          report: report.report_id,
          fight: fight.fight_id,
          duration: fmt(fight.duration),
          watched,
        });
      }
    }
  }

  console.log();
  console.log(`## ${spec.slug}`);
  if (data.updated) console.log(`Updated: \`${data.updated}\``);

  for (const [id, name] of spec.abilities.entries()) {
    const abilityEvents = events.filter((event) => event.id === id);
    if (abilityEvents.length === 0) continue;

    const counts = new Map();
    for (const event of abilityEvents) {
      const key = bucket(event.ms, bucketSeconds);
      counts.set(key, (counts.get(key) || 0) + 1);
    }

    console.log();
    console.log(`### ${name}`);
    console.log();
    console.log(`Total watched events: \`${abilityEvents.length}\``);
    console.log();
    console.log("| Window | Count |");
    console.log("| --- | ---: |");
    [...counts.entries()]
      .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
      .slice(0, 10)
      .forEach(([window, count]) => console.log(`| \`${window}\` | ${count} |`));
  }

  console.log();
  console.log("### Examples");
  console.log();
  console.log("| Rank | Report | Fight | Duration | Watched casts |");
  console.log("| ---: | --- | ---: | ---: | --- |");
  for (const example of examples) {
    const casts = example.watched.map((event) => `\`${event.name} ${event.time}\``).join("; ") || "none";
    const link = `[${example.report}](https://www.warcraftlogs.com/reports/${example.report}?fight=${example.fight})`;
    console.log(`| ${example.rank} | ${link} | ${example.fight} | \`${example.duration}\` | ${casts} |`);
  }
}
