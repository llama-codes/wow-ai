---
name: viserio-import
description: Build and repair Viserio Cooldowns assignment imports for WoW raid cooldown plans. Use when converting healer or raid cooldown plans, Warcraft Logs/Wipefest timing notes, or Viserio export data into an importable Viserio assignments object, especially when Viserio reports expected object format errors like { actors: [...] }.
---

# Viserio Import

## Workflow

1. Collect the cooldown plan and, when available, a Viserio export from the target raid group. Prefer an existing export because it contains the roster, actor ids, spell metadata, GUIDs, phases, and any custom rows Viserio expects.
2. Read `references/import-format.md` before creating or repairing an import object.
3. Build a top-level object shaped as `{ "actors": [...], "phases": [...], "customGridRows": [...] }`. Do not use standalone `playerSpells` or `playerNotes`; Viserio assignment import rejects that shape.
4. Preserve all actors from the export unless the user asks for a smaller file. Add assignments inside the matching actor's `spells` array and callouts inside that actor's `notes` array.
5. Use seconds for `startTime` and `phaseOffset`, not milliseconds. Use `phaseNumber: 0` unless the export has real multi-phase timing that should be preserved.
6. Prefer copying complete `spell` metadata from the user's Viserio export for the same spell. If a spell is missing from the export, use known metadata from the reference file or add it as a note and clearly tell the user what was not a real spell row.
7. Validate the finished JSON with `scripts/validate_viserio_import.py <json-file>`.
8. Return the file path, the import shape, and a short count of important assigned spells. Mention any manually supplied spell metadata or text-only fallbacks.

## Practical Rules

- Keep the actor object fields from the export: `name`, `realm`, `playerClass`, `playerSpec`, `spells`, and `notes`.
- Copy `actorId` from existing spell rows for that actor when possible. If deriving it, use lower-case `name-realm`, remove punctuation from the realm, and treat `Everyone` as `everyone-`.
- Spell assignment rows need the nested `spell` object, `startTime`, `actorId`, custom cooldown/duration fields set to `null`, `charges: null`, `phaseNumber`, and `phaseOffset`.
- Notes use `actor`, `startTime`, `noteText`, `icon`, `phaseNumber`, and `phaseOffset`.
- Packed Viserio export strings are not plain JSON. Do not edit the packed string directly; construct or repair the decoded JSON object shape instead.
- For fragile imports, keep spell metadata exactly as exported, including `guid`, `wowheadLink`, `iconLink`, `cooldown`, `duration`, and `playerSpellType`.

## Resources

- `references/import-format.md`: schema, field rules, and common spell metadata used in Viserio assignments.
- `scripts/validate_viserio_import.py`: JSON validator for the expected Viserio assignment object shape.
