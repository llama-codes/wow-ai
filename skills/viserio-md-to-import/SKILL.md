---
name: viserio-md-to-import
description: Generate importable Viserio Cooldowns assignment JSON from an editable Markdown healing timeline and a current Viserio export. Use when the user has a Markdown table of healing assignments and wants a Viserio import object, or when converting plain-text raid cooldown plans back into the required actors/phases/customGridRows shape.
---

# Viserio Markdown To Import

## Workflow

1. Start with a Markdown table containing `Time` and `Assignment`; `Purpose` is optional.
2. Use a current Viserio export from the target roster as metadata authority.
3. Run the shared generator:

```powershell
python skills\viserio-import\scripts\md_to_viserio_import.py --plan <plan.md> --export <export.txt-or-json> --output <assignments.json>
```

4. Validate the result:

```powershell
python skills\viserio-import\scripts\validate_viserio_import.py <assignments.json>
```

## Assignment Syntax

- Spell row: `Actor Spell`
- Same actor bundle: `Actor Spell + Spell`
- Multiple actors at one time: `Actor Spell, OtherActor Spell`
- Note row: `Actor note: text`
- Times may be `MM:SS`, `HH:MM:SS`, or seconds.

The generator supports common aliases such as `Tranq`, `Convoke`, `AM`, `Wings`, `Rally`, `Personals`, `Stasis Pop`, `Tip`, and `Yu'lon`.

## Metadata Rules

- Use exported actor and spell metadata first, including actor ids, GUIDs, spell types, cooldowns, durations, phases, and custom rows.
- Use `skills\viserio-import\references\import-format.md` only as fallback metadata.
- Fail loudly on unknown actors or unknown spells unless the row is explicitly a note.
- Treat generated JSON as an import artifact, not the human editing surface.

## Related Skills

- Use `viserio-export-to-md` to create the Markdown plan from an existing Viserio export.
- Use `viserio-validate-import` when Viserio rejects a JSON import or the validator reports shape problems.
- Use `viserio-import` to orchestrate a full round trip.
