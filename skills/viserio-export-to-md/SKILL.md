---
name: viserio-export-to-md
description: Convert Viserio Cooldowns assignment exports into editable Markdown timeline tables. Use when the user provides a packed Viserio export string or decoded Viserio JSON and wants a plain-text/Markdown healing assignment plan, a reverse-generated timeline, or a starting point for round-tripping assignments.
---

# Viserio Export To Markdown

## Workflow

1. Use the shared reverse generator from the `viserio-import` skill:

```powershell
python skills\viserio-import\scripts\viserio_export_to_md.py --input <export.txt-or-json> --output <plan.md>
```

2. The input may be a decoded Viserio JSON object or a packed Viserio export string.
3. The output is an editable Markdown table with `Time`, `Assignment`, and blank `Purpose`.
4. Same-time casts are grouped into compact assignment cells. Same actor spells use `+`; different actors use commas. Notes are emitted as `Actor note: text`.

## Rules

- Do not edit packed Viserio export strings directly.
- Treat the generated Markdown as the human-editable source for future changes.
- Leave `Purpose` blank when generating from Viserio; Viserio exports do not contain that context.
- If the user asks for actor-by-actor review, generate the timeline first and then summarize from it instead of changing the source format.

## Related Skills

- Use `viserio-md-to-import` to turn the edited Markdown timeline back into importable JSON.
- Use `viserio-validate-import` to validate the generated JSON.
- Use `viserio-import` when orchestrating the whole export -> Markdown -> JSON workflow.
