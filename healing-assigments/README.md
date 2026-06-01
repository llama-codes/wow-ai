# Healing Assignments

Repo-local notes for raid healing assignment work. This folder currently captures the Lightblinded Vanguard Mythic cooldown plan and the Viserio import lessons from chat `019e5fcf-9591-7030-8464-453bef8c7f42`.

## Documents

- [Lightblinded Vanguard Healing Plan](./lightblinded-vanguard-healing-plan.md): healing-lead timeline, key wipe gates, and assignment intent.
- [Lightblinded Vanguard Current Export](./lightblinded-vanguard-current-export.txt): latest packed Viserio export to use as the current roster/source of truth.
- [Lightblinded Vanguard Current Export Timeline](./lightblinded-vanguard-current-export.md): Markdown timeline generated from the latest packed Viserio export.
- [Lightblinded Vanguard Current Export Decoded](./lightblinded-vanguard-current-export.decoded.json): decoded view of the latest packed Viserio export for inspection.
- [Lightblinded Vanguard Viserio Assignments](./lightblinded-vanguard-viserio-assignments.md): final Viserio assignment summary by actor from the generated import.
- [Lightblinded Vanguard Viserio Import](./lightblinded-vanguard-viserio-assignments.json): importable Viserio assignment JSON generated from the final plan.
- [Viserio Import Lessons](./viserio-import-lessons.md): format rules learned from the failed import, corrected object shape, and reusable workflow.

## Related Skill

Use the repo-local [`viserio-import`](../skills/viserio-import/SKILL.md) skill when converting future raid cooldown plans into Viserio imports. The important rule is that Viserio expects top-level `{ "actors": [...], "phases": [...], "customGridRows": [...] }`, with assignments nested inside each actor.
