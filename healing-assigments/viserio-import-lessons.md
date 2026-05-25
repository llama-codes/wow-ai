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
- For Wyldfire's Restoration Druid fallback profile, use Bobbidyboo's exported Druid metadata for `Convoke the Spirits` and `Tranquility` because the manual export still lists Wyldfire as Balance with no cooldown rows.
- `Avenging Wrath` was present in the export metadata and should be a real spell row.
- `Stasis` and `Stasis pop` should use exported Viserio metadata when available. The working export used spell ids `370537` and `370564`, `Minor Heal CD`, and Viserio GUIDs `5476581d-731e-4eda-a4ed-a402ee89167e` and `d4c22a8c-92c8-4fe0-a978-0130717bf704`.
- `Tip the Scales` and `Vaelgor's Final Stare` should use the manual current-usage export metadata when adding the full evoker Stasis package.
- `Celestial Conduit` should use the manual current-usage export metadata when adding Mistweaver assignments. The working export used spell id `443028`, GUID `46aaa4a2-831f-44c2-b369-564efa7d3bb7`, cooldown `90`, duration `4`, and `Heal CD`.
- In the current Lightblinded Vanguard plan, the full Stasis package releases on the former Celestial Conduit cadence, and Celestial Conduit has been moved back onto that same cadence so those release windows stack.
- `Rallying Cry` should use exported Warrior metadata when available. The working export used spell id `97462`, GUID `cf93a6a0-9835-419c-8db8-a367fd5338e8`, base cooldown `180`, duration `10`, `Raid DR`, and the Battlefield Commander modifier setting cooldown to `165`.
- `Mass Dispel` and `Healthstone` are safer as notes unless an export contains exact Viserio spell metadata for them.
- Manual current-usage exports can contain mechanic reminders as actor notes. The `Dispels` reminders should be copied as `Everyone` notes with the exported icon and exact timestamps.
- Add Preservation Evoker prep reminders as personal actor notes when the assignment depends on holding a normal spell for Stasis storage. Dream Breath is 30 seconds baseline, but `Spiritual Clarity` reduces it by 10 seconds, so in this plan Deviiarrc stops using it 20 seconds before each Stasis combo. Use the exported personal text reminder style with the thought-bubble icon.
- The final generated import validated as `8 actors, 70 spells, 35 notes`.

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
