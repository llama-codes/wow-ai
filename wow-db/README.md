# WoW Current Raid Spec Database

This folder holds a small repo-local database for current Mythic raid build planning.
It is designed for healing assignment and raid-prep work where we need quick class,
spec, and boss-specific recommendations without copying full guide pages.

## Files

- `current-raid-mythic.json`: canonical local database snapshot.
- `specs/<class>/<spec>.json`: per-spec boss recommendations and talent data.
- `schema.json`: reviewable JSON Schema for the database shape.
- `scripts/refresh_current_raid.py`: stdlib-only manual refresh and validator.
- `tests/test_refresh_current_raid.py`: parser and preservation tests using small fixtures.

## Source Policy

- Archon is used for data-driven build metrics, stat priority, talent popularity,
  parse counts, top-log links, and boss-specific recommendation pages.
- Wowhead is used for canonical tooltip-friendly talent, spell, and item links.
- Do not copy guide prose into this database. Local strong/weak points should be
  short notes with a measurable basis and a source URL.

## Refresh

Preview a one-spec, one-boss live smoke check:

```powershell
python wow-db\scripts\refresh_current_raid.py --live-smoke
```

Refresh and write the full database:

```powershell
python wow-db\scripts\refresh_current_raid.py --write
```

Split an existing monolithic snapshot without fetching:

```powershell
python wow-db\scripts\refresh_current_raid.py --split-existing
```

Validate the current local snapshot:

```powershell
python wow-db\scripts\refresh_current_raid.py --validate
```

The script rate-limits live requests by default. Use `--delay` only when you have
a reason to change the default.

## Manual Notes

Generated strong/weak points are replaced on refresh. Put local raid-lead judgment
in a spec file's `manualNotes` object instead, for example
`specs/druid/restoration.json`:

```json
{
  "strongPoints": [
    {
      "text": "Excellent external coverage for predictable raid bursts.",
      "basis": "Local roster planning note.",
      "sourceUrl": ""
    }
  ],
  "weakPoints": [],
  "recommendationBuilds": []
}
```

`manualNotes` are preserved by `refresh_current_raid.py --write`.
