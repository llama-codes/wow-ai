# Belo'ren Lorrgs Healer Top Parses

Source: Lorrgs API.

Lorrgs does not expose an obvious public export button in the app, but the frontend uses JSON endpoints under `https://api2.lorrgs.io`.

Useful endpoint shape:

```text
GET https://api2.lorrgs.io/api/spec_ranking/{spec_slug}/beloren-child-of-alar?difficulty=mythic&metric=hps
GET https://api2.lorrgs.io/api/specs/{spec_slug}/spells
```

Boss slug:

```text
beloren-child-of-alar
```

This file focuses on the three healer specs in our setup other than Preservation Evoker:

- Holy Priest
- Holy Paladin
- Restoration Shaman

The data below is from the top 50 Mythic HPS parses per spec on Lorrgs.

## Quick Takeaways

- Holy Priest top parses strongly favor `Divine Hymn` around `00:50-00:59`, with `Apotheosis` commonly at pull, `02:00-02:09`, and late around `04:30-04:49`.
- Holy Paladin top parses use `Avenging Wrath` almost always on pull, then around `02:00-02:09`, then again in the `04:00+` range. `Aura Mastery` most often lands in `02:20-02:49`.
- Restoration Shaman top parses are extremely consistent on `Spirit Link Totem` around `02:30-02:39`. `Ascendance` is most common around `01:50-01:59`, with a second common late use near `04:50-05:09`.
- `Healing Tide Totem` did not show up in the top-50 Restoration Shaman watched casts from Lorrgs, even though it is in the Lorrgs spell dictionary. For Belo'ren planning, Lorrgs top HPS logs point more toward `Spirit Link Totem` + `Ascendance`.

## Holy Priest

Spec endpoint:

```text
https://api2.lorrgs.io/api/spec_ranking/priest-holy/beloren-child-of-alar?difficulty=mythic&metric=hps
```

Abilities to watch:

- `Divine Hymn`
- `Apotheosis`
- `Guardian Spirit`

Top-50 timing buckets:

| Ability / Window | Count |
| --- | ---: |
| `Divine Hymn 00:50-00:59` | 28 |
| `Divine Hymn 00:00-00:09` | 12 |
| `Divine Hymn 03:30-03:39` | 12 |
| `Divine Hymn 02:40-02:49` | 7 |
| `Divine Hymn 02:50-02:59` | 7 |
| `Apotheosis 02:00-02:09` | 26 |
| `Apotheosis 00:00-00:09` | 25 |
| `Apotheosis 04:30-04:39` | 13 |
| `Apotheosis 04:40-04:49` | 11 |
| `Guardian Spirit 02:40-02:49` | 3 |

Top examples:

| Rank | Report | Fight | Duration | Watched casts |
| ---: | --- | ---: | ---: | --- |
| 1 | [PTdgK9hpA7Rqzjn3](https://www.warcraftlogs.com/reports/PTdgK9hpA7Rqzjn3?fight=40) | 40 | `04:58` | `Apotheosis 00:01`; `Divine Hymn 00:53`; `Apotheosis 02:05`; `Divine Hymn 03:00`; `Apotheosis 04:35` |
| 2 | [7yWnprvKxLVMjaRh](https://www.warcraftlogs.com/reports/7yWnprvKxLVMjaRh?fight=1) | 1 | `05:00` | `Apotheosis 00:04`; `Divine Hymn 00:52`; `Guardian Spirit 01:11`; `Apotheosis 02:07`; `Divine Hymn 03:33`; `Apotheosis 04:34` |
| 3 | [2tvkL6DX8Gfaxcm3](https://www.warcraftlogs.com/reports/2tvkL6DX8Gfaxcm3?fight=28) | 28 | `05:14` | `Divine Hymn 00:52`; `Apotheosis 02:00`; `Divine Hymn 03:05`; `Apotheosis 04:36` |
| 4 | [6xdHtZhD7Pcnz4jr](https://www.warcraftlogs.com/reports/6xdHtZhD7Pcnz4jr?fight=21) | 21 | `05:17` | `Divine Hymn 00:31`; `Apotheosis 02:00`; `Divine Hymn 02:41`; `Apotheosis 04:03`; `Divine Hymn 04:43` |
| 5 | [6bBncqd7wW1arDgN](https://www.warcraftlogs.com/reports/6bBncqd7wW1arDgN?fight=21) | 21 | `04:46` | `Divine Hymn 00:53`; `Apotheosis 02:01`; `Divine Hymn 03:27`; `Apotheosis 04:20` |

Planning read:

| Time | Holy Priest plan |
| --- | --- |
| `00:50-00:55` | Very common `Divine Hymn` spot. This lines up with the first major healing ramp and the Evoker `Rewind` baseline we saw around `00:54-00:55`. |
| `02:00-02:10` | Very common `Apotheosis` spot. |
| `02:40-02:59` | Backup `Divine Hymn` option if we do not want to spend it in the first minute. |
| `04:30-04:49` | Common late `Apotheosis` timing. |

## Holy Paladin

Spec endpoint:

```text
https://api2.lorrgs.io/api/spec_ranking/paladin-holy/beloren-child-of-alar?difficulty=mythic&metric=hps
```

Abilities to watch:

- `Aura Mastery`
- `Avenging Wrath`
- `Divine Toll`
- `Blessing of Sacrifice`
- `Blessing of Protection`

Top-50 timing buckets:

| Ability / Window | Count |
| --- | ---: |
| `Avenging Wrath 00:00-00:09` | 46 |
| `Avenging Wrath 02:00-02:09` | 29 |
| `Avenging Wrath 04:00-04:09` | 17 |
| `Avenging Wrath 04:40-04:49` | 10 |
| `Aura Mastery 02:20-02:29` | 12 |
| `Aura Mastery 02:30-02:39` | 12 |
| `Aura Mastery 02:40-02:49` | 7 |
| `Blessing of Sacrifice 01:00-01:09` | 15 |
| `Blessing of Sacrifice 02:50-02:59` | 12 |
| `Divine Toll 00:00-00:09` | 49 |
| `Divine Toll 00:30-00:39` | 34 |
| `Divine Toll 01:40-01:49` | 27 |
| `Divine Toll 02:10-02:19` | 21 |

Top examples:

| Rank | Report | Fight | Duration | Watched casts |
| ---: | --- | ---: | ---: | --- |
| 1 | [QRb2trqnHpkBMJYj](https://www.warcraftlogs.com/reports/QRb2trqnHpkBMJYj?fight=54) | 54 | `05:09` | `Avenging Wrath 00:01`; `Divine Toll 00:02`; `Avenging Wrath 02:02`; `Aura Mastery 02:28`; `Blessing of Sacrifice 03:58`; `Avenging Wrath 04:03`; `Blessing of Protection 04:37` |
| 2 | [mRcBHdGy8FLqCxPa](https://www.warcraftlogs.com/reports/mRcBHdGy8FLqCxPa?fight=15) | 15 | `04:24` | `Avenging Wrath 00:01`; `Blessing of Sacrifice 00:58`; `Aura Mastery 01:54`; `Avenging Wrath 02:02`; `Blessing of Sacrifice 03:28`; `Avenging Wrath 04:02` |
| 3 | [yrWPYfBGvp6JQa2K](https://www.warcraftlogs.com/reports/yrWPYfBGvp6JQa2K?fight=89) | 89 | `05:12` | `Avenging Wrath 00:01`; `Blessing of Sacrifice 01:15`; `Avenging Wrath 02:09`; `Aura Mastery 02:32`; `Blessing of Sacrifice 03:59`; `Avenging Wrath 04:33` |
| 4 | [1CR8X7LxQYBwHJvD](https://www.warcraftlogs.com/reports/1CR8X7LxQYBwHJvD?fight=42) | 42 | `04:18` | `Avenging Wrath 00:01`; `Aura Mastery 01:04`; `Blessing of Sacrifice 01:08`; `Avenging Wrath 01:46`; `Blessing of Sacrifice 03:17`; `Avenging Wrath 03:32`; `Aura Mastery 04:07` |
| 5 | [Bza78rmjA9wgWdX1](https://www.warcraftlogs.com/reports/Bza78rmjA9wgWdX1?fight=27) | 27 | `05:08` | `Avenging Wrath 00:01`; `Blessing of Protection 01:52`; `Aura Mastery 01:57`; `Avenging Wrath 02:14`; `Avenging Wrath 04:39` |

Planning read:

| Time | Holy Paladin plan |
| --- | --- |
| `00:00-00:05` | `Avenging Wrath` + `Divine Toll` is almost universal in top parses. |
| `02:00-02:15` | Second `Avenging Wrath` window. |
| `02:20-02:49` | Best Lorrgs-backed `Aura Mastery` area. |
| `02:50-02:59` | Common `Blessing of Sacrifice` placement. |
| `04:00-04:50` | Third `Avenging Wrath`, depending on kill time and cooldown drift. |

## Restoration Shaman

Spec endpoint:

```text
https://api2.lorrgs.io/api/spec_ranking/shaman-restoration/beloren-child-of-alar?difficulty=mythic&metric=hps
```

Abilities to watch:

- `Spirit Link Totem`
- `Ascendance`
- `Healing Tide Totem`
- `Spiritwalker's Grace`
- `Windrush Totem`
- `Astral Shift`

Top-50 timing buckets:

| Ability / Window | Count |
| --- | ---: |
| `Spirit Link Totem 02:30-02:39` | 43 |
| `Spirit Link Totem 02:40-02:49` | 3 |
| `Ascendance 01:50-01:59` | 36 |
| `Ascendance 05:00-05:09` | 12 |
| `Ascendance 04:50-04:59` | 10 |
| `Ascendance 02:00-02:09` | 8 |
| `Spiritwalker's Grace 05:00-05:09` | 14 |
| `Spiritwalker's Grace 00:10-00:19` | 12 |
| `Spiritwalker's Grace 04:50-04:59` | 12 |
| `Windrush Totem 01:50-01:59` | 33 |
| `Astral Shift 04:50-04:59` | 5 |

Top examples:

| Rank | Report | Fight | Duration | Watched casts |
| ---: | --- | ---: | ---: | --- |
| 1 | [pcYLAZnCw4NJQtkV](https://www.warcraftlogs.com/reports/pcYLAZnCw4NJQtkV?fight=2) | 2 | `05:26` | `Spiritwalker's Grace 00:14`; `Windrush Totem 01:57`; `Ascendance 01:58`; `Spiritwalker's Grace 02:13`; `Spirit Link Totem 02:35`; `Astral Shift 03:00`; `Ascendance 05:01`; `Spiritwalker's Grace 05:07` |
| 2 | [6bBncqd7wW1arDgN](https://www.warcraftlogs.com/reports/6bBncqd7wW1arDgN?fight=21) | 21 | `04:46` | `Ascendance 01:57`; `Spiritwalker's Grace 01:59`; `Windrush Totem 02:11`; `Spirit Link Totem 02:23`; `Astral Shift 04:36`; `Windrush Totem 04:42` |
| 3 | [fqTNhcx6p7kmDV24](https://www.warcraftlogs.com/reports/fqTNhcx6p7kmDV24?fight=44) | 44 | `05:15` | `Windrush Totem 01:56`; `Ascendance 01:58`; `Spirit Link Totem 02:32`; `Spiritwalker's Grace 04:55` |
| 4 | [P64cwF3YZ7TvzktN](https://www.warcraftlogs.com/reports/P64cwF3YZ7TvzktN?fight=76) | 76 | `05:32` | `Windrush Totem 01:54`; `Ascendance 01:57`; `Spirit Link Totem 02:36`; `Spiritwalker's Grace 04:33`; `Ascendance 04:57` |
| 5 | [W6DvgjCdtVhfMBLR](https://www.warcraftlogs.com/reports/W6DvgjCdtVhfMBLR?fight=103) | 103 | `05:30` | `Windrush Totem 01:55`; `Ascendance 01:57`; `Spirit Link Totem 02:38`; `Ascendance 05:01` |

Planning read:

| Time | Restoration Shaman plan |
| --- | --- |
| `01:50-02:00` | Very common `Ascendance` timing. |
| `02:30-02:39` | Extremely consistent `Spirit Link Totem` timing. This is the cleanest Lorrgs-backed shaman assignment. |
| `04:50-05:09` | Common late second `Ascendance` area if fight length supports it. |
| `05:00-05:09` | Common late `Spiritwalker's Grace`, mostly useful as movement support rather than raid-CD planning. |

## Lorrgs-Backed Healer Assignment Sketch

This is the cleanest version if we use Lorrgs top HPS behavior as the main reference:

| Time | Assignment |
| --- | --- |
| `00:00-00:05` | Holy Paladin `Avenging Wrath` + `Divine Toll` |
| `00:50-00:55` | Holy Priest `Divine Hymn` and Preservation Evoker `Rewind` |
| `01:50-02:00` | Restoration Shaman `Ascendance` |
| `02:00-02:10` | Holy Priest `Apotheosis`; Holy Paladin second `Avenging Wrath` |
| `02:30-02:39` | Restoration Shaman `Spirit Link Totem`; Holy Paladin `Aura Mastery` can overlap if this is the planned hard stack |
| `04:30-04:49` | Holy Priest late `Apotheosis` |
| `04:50-05:09` | Restoration Shaman late `Ascendance`; optional late throughput/defensive stack depending on kill time |

Compared to the exact-comp logs, Lorrgs top healer parses put even more weight on Shaman `Spirit Link Totem` at `02:30-02:39` and Paladin `Aura Mastery` around `02:20-02:49`.
