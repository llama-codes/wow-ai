---
name: lorrgs-log-analysis
description: Use when Codex needs to analyze Lorrgs.io World of Warcraft log rankings, discover Lorrgs API endpoints, pull top parses for a boss/spec, map spell IDs, or extract cooldown timing buckets for raid planning. Especially useful for Warcraft Logs/Lorrgs fight prep, Mythic boss healing or defensive timelines, and comparing top-parse cooldown usage without rediscovering the Lorrgs frontend API.
---

# Lorrgs Log Analysis

## Overview

Use this skill to query Lorrgs top-parse data directly from the JSON API used by the site, map spell IDs to names, and summarize cooldown timing patterns for raid planning.

Lorrgs data is current/live. If network access is restricted, request network escalation before calling the API.

## Core API

Base URL:

```text
https://api2.lorrgs.io
```

Useful endpoints:

```text
GET /api/seasons/current
GET /api/zones
GET /api/spec_ranking/{spec_slug}/{boss_slug}?difficulty=mythic&metric=hps
GET /api/spec_ranking/{spec_slug}/{boss_slug}?difficulty=mythic&metric=dps
GET /api/specs/{spec_slug}/spells
```

Typical workflow:

1. Call `/api/seasons/current` and `/api/zones` if the boss slug or current season is unknown.
2. Use `/api/spec_ranking/...` to get top parses for the requested boss/spec.
3. Use `/api/specs/{spec_slug}/spells` to map spell IDs to names and identify watched abilities.
4. Extract `reports[].fights[].players[].casts[]`, filter to the watched spell IDs, and bucket `ts` timestamps relative to pull.
5. Save results as repo-local markdown when the user asks for an artifact.

## Known Belo'ren Data

For Mythic Belo'ren planning, the boss slug discovered from Lorrgs is:

```text
beloren-child-of-alar
```

Useful healer spec slugs:

```text
evoker-preservation
priest-holy
paladin-holy
shaman-restoration
```

Useful non-healer spec slugs from the same exploration:

```text
warrior-protection
demonhunter-havoc
demonhunter-devourer
deathknight-unholy
evoker-augmentation
evoker-devastation
```

Belo'ren healer cooldown IDs that were useful in planning:

```text
priest-holy:64843=Divine Hymn,200183=Apotheosis,47788=Guardian Spirit
paladin-holy:31821=Aura Mastery,31884=Avenging Wrath,216331=Avenging Crusader,375576=Divine Toll,6940=Blessing of Sacrifice,1022=Blessing of Protection
shaman-restoration:98008=Spirit Link Totem,108280=Healing Tide Totem,114052=Ascendance,108271=Astral Shift,79206=Spiritwalker's Grace,192077=Windrush Totem
evoker-preservation:363534=Rewind,355936=Dream Flight,370537=Stasis,370562=Stasis,374227=Zephyr,357170=Time Dilation
```

Belo'ren non-healer defensive IDs from the same exploration:

```text
warrior-protection:97462=Rallying Cry,23920=Spell Reflection,871=Shield Wall,1160=Demoralizing Shout
demonhunter-havoc:196718=Darkness,198589=Blur,200166=Metamorphosis
demonhunter-devourer:196718=Darkness,198589=Blur,200166=Metamorphosis
deathknight-unholy:51052=Anti-Magic Zone,48707=Anti-Magic Shell,48792=Icebound Fortitude,49039=Lichborne
```

Treat these IDs as cached starting points. Verify with `/api/specs/{spec_slug}/spells` when working on a new patch, season, or boss.

## Extractor Script

Use `scripts/lorrgs-cooldowns.mjs` for repeatable extraction.

Example for the Belo'ren healer setup:

```bash
node skills/lorrgs-log-analysis/scripts/lorrgs-cooldowns.mjs \
  --boss beloren-child-of-alar \
  --difficulty mythic \
  --metric hps \
  --top 50 \
  --spec "priest-holy:64843=Divine Hymn,200183=Apotheosis,47788=Guardian Spirit" \
  --spec "paladin-holy:31821=Aura Mastery,31884=Avenging Wrath,375576=Divine Toll,6940=Blessing of Sacrifice,1022=Blessing of Protection" \
  --spec "shaman-restoration:98008=Spirit Link Totem,108280=Healing Tide Totem,114052=Ascendance,108271=Astral Shift,79206=Spiritwalker's Grace,192077=Windrush Totem"
```

PowerShell works best with one line or backticks instead of bash continuations.

## Interpretation Notes

- Lorrgs ranking responses include report IDs, fights, players, and per-player cast arrays.
- `ts` is milliseconds from pull; convert to `MM:SS` for planner timelines.
- Some buff events, especially external buffs like `Blessing of Sacrifice`, can appear duplicated. Use those as placement signals rather than exact cast counts.
- Cast-based raid cooldowns such as `Divine Hymn`, `Aura Mastery`, `Spirit Link Totem`, `Rewind`, `Darkness`, and `Rallying Cry` are cleaner anchors.
- Lorrgs top parses are not the same as exact-comp Warcraft Logs searches. Use Lorrgs to learn strong timing patterns, then compare against exact-comp logs when composition matching matters.
- Prefer writing compact markdown summaries with top timing buckets, 3-5 example reports, and a short planning read.
