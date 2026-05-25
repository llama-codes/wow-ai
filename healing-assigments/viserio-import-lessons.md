# Viserio Import Lessons

## Error We Hit

The first JSON shape failed with:

```text
Error processing data: Parsed data is not the expected object format ({ actors: [...] }).
```

That happened because the first draft used a planner-style object with `playerSpells` and `playerNotes`. Viserio's assignment import wants the exported/importable object shape instead.

## Correct Shape

Use this top-level shape:

```json
{
  "actors": [],
  "phases": [],
  "customGridRows": []
}
```

Assignments belong inside each actor:

```json
{
  "name": "Bobbidyboo",
  "realm": "Azjol-Nerub",
  "playerClass": "Druid",
  "playerSpec": "Restoration",
  "spells": [],
  "notes": []
}
```

## Rules For Future Imports

- Preserve all actors from the Viserio export unless intentionally making a minimal file.
- Add cooldown rows to `actor.spells`.
- Add mechanic calls or fallback reminders to `actor.notes`.
- Use seconds for `startTime` and `phaseOffset`, not milliseconds.
- Preserve `phases` and `customGridRows` from the export.
- Copy full spell metadata from the user's export when possible, including `guid`, `wowheadLink`, `iconLink`, `cooldown`, `duration`, and `playerSpellType`.
- If a spell is missing from the export, either ask for an export containing it or clearly mark manually supplied metadata.

## Specific Lessons From This Plan

- `Convoke the Spirits` was present in the export metadata and should be a real spell row.
- `Avenging Wrath` was present in the export metadata and should be a real spell row.
- `Dream Flight` was not present in the export metadata, but the user wanted it as a real spell row, so it was manually supplied.
- `Mass Dispel`, `Rallying Cry`, and `Healthstone` are safer as notes unless an export contains exact Viserio spell metadata for them.
- The final generated import validated as `7 actors, 36 spells, 12 notes`.

## Reusable Workflow

Use the repo-local [`viserio-import`](../skills/viserio-import/SKILL.md) skill for future conversions:

1. Start from a cooldown timeline and a Viserio export from the current roster.
2. Read [`import-format.md`](../skills/viserio-import/references/import-format.md).
3. Build `{ actors, phases, customGridRows }`.
4. Nest spell assignments and notes under the matching actors.
5. Validate the generated JSON:

```powershell
python skills\viserio-import\scripts\validate_viserio_import.py <path-to-import.json>
```

6. Report the counts, any manual metadata, and any text-only fallbacks.
