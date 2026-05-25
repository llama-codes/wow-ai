---
name: viserio-import
description: Orchestrate Viserio Cooldowns healing assignment workflows across export-to-Markdown, Markdown-to-import generation, and import validation. Use when converting raid cooldown plans, healing assignment timelines, Warcraft Logs/Wipefest notes, or Viserio exports end-to-end, or when deciding which focused Viserio skill should handle a task.
---

# Viserio Assignment Workflow

## Choose The Focused Skill

- Existing Viserio export -> editable Markdown timeline: use `viserio-export-to-md`.
- Edited Markdown timeline -> importable Viserio JSON: use `viserio-md-to-import`.
- Validate, diagnose, or repair rejected Viserio JSON: use `viserio-validate-import`.
- Full workflow: run the focused skills in this order: export to Markdown, edit/review Markdown, generate JSON, validate JSON.

## Orchestration Rules

- Treat Markdown timelines as the human-edited source of truth.
- Treat generated JSON as an import artifact.
- Treat the current Viserio export as the authority for roster, actor ids, spell metadata, GUIDs, phases, and custom grid rows.
- Do not edit packed Viserio export strings directly.
- Preserve all actors from the export unless the user asks for a minimal import.
- Use notes for mechanics, callouts, or unavailable spell metadata.

## Shared Resources

The focused skills share these implementation files:

- `scripts/viserio_export_to_md.py`: Viserio export to Markdown timeline.
- `scripts/md_to_viserio_import.py`: Markdown timeline to importable JSON.
- `scripts/validate_viserio_import.py`: import JSON validator.
- `references/import-format.md`: Viserio shape rules and fallback spell metadata.

## Reporting

After generating or validating an import, report:

- The output file path.
- Actor, spell, note, phase, and custom row counts.
- Any manually supplied metadata or note-only fallbacks.
- Any validation warnings that may matter for Viserio import.
