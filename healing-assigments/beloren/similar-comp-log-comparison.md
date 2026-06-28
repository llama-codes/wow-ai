# Belo'ren Similar Comp Log Comparison

Comparison summary for exact-match Mythic Belo'ren logs using:

- Preservation Evoker
- Holy Priest
- Holy Paladin
- Restoration Shaman

Use this as the quick pattern read before building our own assignments. The raw cast evidence lives in `similar-comp-big-cooldowns.md`.

## High-Level Takeaways

- The common first `Rewind` timing is `00:54-00:55`.
- Report 01 is the main outlier: it uses `Rewind` at `00:06`, then covers the ~`00:50` window with `Divine Hymn`.
- Most Preservation Evokers are playing `Dream Flight`; report 02 is the Stasis example.
- The main mid-fight raid cooldown stack usually lands around `02:35-02:45`.
- Holy Paladin `Aura Mastery` is usually assigned near `02:11-02:55`, not on pull.
- Restoration Shaman usage varies the most: some logs prioritize `Spirit Link Totem`, others use repeated `Healing Tide Totem`, and some lean on `Ascendance`.

## Log-By-Log Comparison

| Log | Duration | Evoker style | First Rewind | Shaman pattern | Priest pattern | Paladin pattern | Main difference |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| 01 - `wj1AQF7fJBL6vyhC` | 04:59 | Dream Flight | `00:06` | `Ascendance` on pull and `03:27`; `Spirit Link Totem` at `02:36` | `Apotheosis` at `00:05`, `02:07`, `04:40`; `Divine Hymn` at `00:50`, `03:15` | `Avenging Wrath` on pull, `02:03`, `04:35`; `Aura Mastery` at `02:29` | Early Rewind outlier. Pull damage is covered aggressively by Evoker, then Priest covers ~`00:50`. |
| 02 - `6WHXm18qGFzxYwJh` | 05:10 | Stasis | `00:55` | `Ascendance` at `01:58`, `05:02`; `Spirit Link Totem` at `02:41` | `Divine Hymn` on pull and `02:37`; `Apotheosis` at `00:48`, `02:48`, `04:55` | `Aura Mastery` at `02:39`; `Avenging Wrath` on pull, `02:37`, `04:44` | Clean Stasis reference. Uses Stasis stores/releases around the big middle windows. |
| 03 - `JBxYbcnGXjdPA2Hw` | 05:17 | Dream Flight | `00:55` | `Spirit Link Totem` at `00:17`, `03:30`; `Ascendance` at `02:05`, `05:07` | `Divine Hymn` at `00:51`, `03:34`; `Apotheosis` at `02:36`, `04:44` | `Aura Mastery` at `02:19`; `Avenging Wrath` on pull, `02:04`, `04:06` | Shaman covers early with SLT instead of saving first link for ~`02:40`. |
| 04 - `GTFtCDN4Qxaf2Hvb` | 05:15 | Dream Flight | `00:55` | `Ascendance` at `01:58`, `04:58`; `Spirit Link Totem` at `02:41` | `Apotheosis` on pull, `02:12`, `04:28`; `Divine Hymn` at `00:51`, `03:31` | `Aura Mastery` at `02:11`; `Avenging Wrath` on pull, `02:01`, `04:01` | Very similar to logs 02/03, but with earlier Aura Mastery and no early SLT. |
| 05 - `yAQm3vkb4DCGqXRz` | 05:17 | Dream Flight | `00:54` | `Healing Tide Totem` at `00:04`, `02:36`, `04:49`; `Spirit Link Totem` at `02:37` | `Apotheosis` at `00:01`, `02:05`, `04:10`; `Divine Hymn` at `00:49`, `02:54`, `04:54` | `Aura Mastery` at `02:55`; repeated `Blessing of Sacrifice` | Most throughput-heavy Shaman example because it uses three Healing Tide casts plus SLT. |
| 06 - `aj1tr98L6pF3gNzJ` | 05:01 | Dream Flight | `02:01` | `Healing Tide Totem` on pull and `04:35`; `Spirit Link Totem` at `02:04` | `Divine Hymn` on pull, `02:08`, `04:38`; `Apotheosis` at `01:57`, `04:08` | `Aura Mastery` at `02:23`; `Avenging Wrath` on pull, `02:02`, `04:20` | Delays first Rewind until ~`02:00`; early windows are covered by Priest/Shaman instead. |

## Timing Patterns

### First Minute

Most logs cover the first minute with one of two patterns:

| Pattern | Logs | Shape |
| --- | --- | --- |
| Baseline Rewind | 02, 03, 04, 05 | Hold `Rewind` for `00:54-00:55`; use Priest/Paladin/Shaman buttons on pull or near `00:50`. |
| Early Rewind | 01 | Use `Rewind` at `00:06`; cover `00:50` with `Divine Hymn`. |
| No early Rewind | 06 | Hold `Rewind` until `02:01`; use pull `Divine Hymn` + `Healing Tide Totem` instead. |

For our planning, `00:55 Rewind` is the safest baseline because it appears in four of six exact-comp logs.

### Mid-Fight Stack

The most consistent major assignment cluster is around `02:35-02:45`.

Common buttons in that area:

- `Aura Mastery`
- `Spirit Link Totem`
- `Divine Hymn` or `Apotheosis`
- `Dream Flight` or `Stasis`
- Sometimes `Healing Tide Totem`

This is probably the first place to design a clean planned stack rather than copying any one log exactly.

### Late Fight

The late section usually repeats class throughput:

- Holy Paladin gets another `Avenging Wrath`.
- Holy Priest gets another `Apotheosis` and often `Divine Hymn`.
- Preservation Evoker gets either a second `Rewind` near `04:50-05:08` or a late `Dream Flight`.
- Restoration Shaman varies between `Ascendance` and `Healing Tide Totem`.

## Practical Planning Notes

- Start with log 02, 03, or 04 for a normal `00:55 Rewind` plan.
- Use log 01 only if we specifically want an early Rewind opener.
- Use log 02 if our Evoker wants to play Stasis.
- Use log 05 if we want a Shaman-heavy plan with repeated `Healing Tide Totem`.
- Use log 06 as proof that the fight can be covered without early Rewind, but it is less useful as the default because it delays Rewind to `02:01`.
