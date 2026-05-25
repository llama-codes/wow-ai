---
name: viserio-validate-import
description: Validate, diagnose, and repair Viserio Cooldowns assignment import JSON. Use when Viserio reports expected object format errors, actors/playerSpells shape errors, missing spell metadata, milliseconds-vs-seconds timing issues, or when checking a generated assignments JSON before import.
---

# Viserio Validate Import

## Workflow

1. Validate the JSON:

```powershell
python skills\viserio-import\scripts\validate_viserio_import.py <assignments.json>
```

2. If validation fails, inspect the decoded JSON object, not any packed export string.
3. Read `skills\viserio-import\references\import-format.md` when repairing structure or spell metadata.
4. Re-run validation after every repair.

## Required Shape

Viserio assignment imports must be a top-level object with:

```json
{
  "actors": [],
  "phases": [],
  "customGridRows": []
}
```

Assignments must be nested inside each actor's `spells` array. Notes must be nested inside each actor's `notes` array. Do not use standalone `playerSpells` or `playerNotes`.

## Repair Rules

- Preserve all roster actors, phases, and custom grid rows from a current Viserio export unless the user asks for a minimal file.
- Spell rows need nested `spell` metadata with `spellId`, `spellName`, and `guid`, plus row-level `startTime`, `actorId`, `phaseNumber`, and `phaseOffset`.
- Use seconds for `startTime` and `phaseOffset`, not milliseconds.
- Prefer regenerated JSON from `viserio-md-to-import` over manual edits when a Markdown plan and export are available.
- If exact spell metadata is unavailable, represent the item as a note or clearly report the fallback.

## Related Skills

- Use `viserio-md-to-import` to regenerate a clean import from Markdown and export metadata.
- Use `viserio-export-to-md` to recover an editable timeline from an existing export.
- Use `viserio-import` to choose and sequence the full workflow.
