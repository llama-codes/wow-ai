# Belo'ren Spec Cooldown Timelines

Spec-by-spec timeline distilled from exact-match Mythic Belo'ren logs.

This is not the final assignment sheet. It is the reference for which ability names to look at and the timing windows that repeatedly show up.

## Preservation Evoker

Abilities to look at:

- `Rewind`
- `Dream Flight`
- `Stasis (Store)` / `Stasis (Release)`
- `Zephyr`
- `Time Dilation`
- `Tip the Scales`

| Window | Ability | Pattern |
| --- | --- | --- |
| `00:00-00:08` | `Dream Flight` or `Stasis (Release)` | Most Dream Flight logs cast it immediately on pull. The Stasis log releases on pull instead. |
| `00:54-00:55` | `Rewind` | Baseline first Rewind timing in logs 02, 03, 04, and 05. |
| `00:06` | `Rewind` | Early/outlier opener from log 01. Treat as alternate, not baseline. |
| `01:33-02:06` | `Tip the Scales` | Common second major Evoker throughput setup. |
| `01:46-02:50` | `Time Dilation` | Usually a targeted save, useful to track but probably not a raid-wide assignment. |
| `02:03-02:37` | `Dream Flight` or `Stasis (Store)` | Second Dream Flight window, or Stasis setup before the mid-fight stack. |
| `02:55-03:36` | `Zephyr` / `Stasis (Release)` / `Tip the Scales` | Mid-fight Evoker coverage varies by talent setup. |
| `04:38-04:58` | `Dream Flight` / `Rewind` / `Tip the Scales` | Late repeat window; most logs have either late Dream Flight or late Rewind here. |

Planning read: use `Rewind` at `00:55` unless we intentionally choose the early-Rewind opener. If our Evoker plays Stasis, use report 02 as the reference.

## Holy Priest

Abilities to look at:

- `Divine Hymn`
- `Apotheosis`

| Window | Ability | Pattern |
| --- | --- | --- |
| `00:01-00:05` | `Apotheosis` or `Divine Hymn` | Some logs use Priest immediately on pull. |
| `00:48-00:51` | `Divine Hymn` or `Apotheosis` | Common first-minute coverage, especially when Rewind is held for `00:55`. |
| `01:57-02:12` | `Apotheosis` | Common second Priest throughput setup. |
| `02:36-02:54` | `Divine Hymn` or `Apotheosis` | Main mid-fight Priest contribution. Often paired with Paladin/Shaman cooldowns. |
| `03:15-03:34` | `Divine Hymn` | Common mid-late Hymn window in Dream Flight logs. |
| `04:08-04:55` | `Apotheosis` / `Divine Hymn` | Late repeat coverage. |

Planning read: Priest is flexible. If Evoker Rewind is at `00:55`, Priest can help on pull or near `00:50`; if Evoker Rewind is early, Priest usually covers the `00:50` window.

## Holy Paladin

Abilities to look at:

- `Aura Mastery`
- `Avenging Wrath`
- `Divine Toll`
- `Blessing of Sacrifice`
- `Lay on Hands`

| Window | Ability | Pattern |
| --- | --- | --- |
| `00:00-00:04` | `Avenging Wrath` + `Divine Toll` | Very common Paladin opener. |
| `00:13-00:42` | `Blessing of Sacrifice` / `Lay on Hands` | Targeted saves or emergency usage, not default raid assignments. |
| `00:48-00:59` | `Divine Toll` | Frequent rotational support around first-minute damage. |
| `02:01-02:05` | `Avenging Wrath` | Common second Wings. |
| `02:11-02:55` | `Aura Mastery` | Main Paladin raid cooldown window. The exact timing varies between logs. |
| `02:29-02:44` | `Divine Toll` | Often sits inside the mid-fight healing stack. |
| `04:01-04:44` | `Avenging Wrath` | Late repeat Wings. |
| `04:21-04:54` | `Divine Toll` | Late repeat rotational support. |

Planning read: `Aura Mastery` is the main Paladin assignment button. `Divine Toll` and `Avenging Wrath` show up constantly, but they are better treated as throughput context unless we explicitly want them assigned.

## Restoration Shaman

Abilities to look at:

- `Spirit Link Totem`
- `Healing Tide Totem`
- `Ascendance`

| Window | Ability | Pattern |
| --- | --- | --- |
| `00:03-00:17` | `Healing Tide Totem` or `Spirit Link Totem` | Some logs use Shaman early on pull; others save Shaman for mid-fight. |
| `01:58-02:05` | `Ascendance` | Common first major Shaman throughput timing when not used on pull. |
| `02:36-02:41` | `Spirit Link Totem` / `Healing Tide Totem` | Most consistent Shaman assignment window. |
| `03:27-03:30` | `Spirit Link Totem` / `Ascendance` | Shows up in a few logs as a mid-late Shaman answer. |
| `04:35-05:07` | `Healing Tide Totem` / `Ascendance` | Late Shaman repeat window. |

Planning read: `Spirit Link Totem` around `02:36-02:41` is the most reusable Shaman assignment. `Healing Tide Totem` is strongest in the Shaman-heavy log 05 pattern, while `Ascendance` is common as a throughput repeat.

## Clean Baseline By Spec

If we want a simple first draft, this is the safest cross-log baseline:

| Time | Spec | Ability |
| --- | --- | --- |
| `00:00-00:04` | Holy Paladin | `Avenging Wrath` + `Divine Toll` |
| `00:48-00:51` | Holy Priest | `Divine Hymn` or `Apotheosis` |
| `00:54-00:55` | Preservation Evoker | `Rewind` |
| `02:04-02:05` | Holy Paladin | `Avenging Wrath` |
| `02:11-02:55` | Holy Paladin | `Aura Mastery` |
| `02:36-02:41` | Restoration Shaman | `Spirit Link Totem` |
| `02:36-02:54` | Holy Priest | `Divine Hymn` or `Apotheosis` |
| `04:35-04:58` | Preservation Evoker | `Dream Flight` or `Rewind` |
| `04:35-05:07` | Restoration Shaman | `Healing Tide Totem` or `Ascendance` |
