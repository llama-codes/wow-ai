# Belo'ren Lorrgs Non-Healer Top Parses

Source: Lorrgs API.

Lorrgs does not expose an obvious public export button in the app, but the frontend uses JSON endpoints under `https://api2.lorrgs.io`.

Useful endpoint shape:

```text
GET https://api2.lorrgs.io/api/spec_ranking/{spec_slug}/{boss_slug}?difficulty=mythic&metric=dps
GET https://api2.lorrgs.io/api/specs/{spec_slug}/spells
GET https://api2.lorrgs.io/api/zones
```

Belo'ren boss slug:

```text
beloren-child-of-alar
```

This file focuses on the three non-healer classes we have for raid defensive planning:

- Warrior tank
- Demon Hunter DPS
- Death Knight DPS

## Quick Takeaways

- Protection Warrior top parses most often use `Rallying Cry` in the `02:30-02:50` range.
- Havoc Demon Hunter top parses commonly use `Darkness` around `02:40-02:50`; some use it at `00:50`, `03:49`, or `05:02`.
- Devourer Demon Hunter top parses mostly show `Blur` and rarely show `Darkness`, so Havoc logs are the better Lorrgs reference for Darkness placement.
- Unholy Death Knight top parses often place `Anti-Magic Zone` around `02:35-02:43`; some use it earlier at `02:08` or later near `02:55`.
- These Lorrgs top-parse timings support the same mid-fight external stack we saw in Warcraft Logs: `02:35-02:50` is the most repeated defensive zone.

## Protection Warrior

Spec endpoint:

```text
https://api2.lorrgs.io/api/spec_ranking/warrior-protection/beloren-child-of-alar?difficulty=mythic&metric=dps
```

Ability to watch:

- `Rallying Cry`

Top-50 timing buckets for `Rallying Cry`:

| Window | Count |
| --- | ---: |
| `02:30-02:40` | 9 |
| `02:40-02:50` | 5 |
| `03:50-04:00` | 4 |
| `04:10-04:20` | 3 |
| `04:20-04:30` | 3 |
| `04:30-04:40` | 3 |
| `00:50-01:00` | 2 |
| `01:50-02:00` | 2 |
| `05:10-05:20` | 2 |

Top parse examples:

| Rank | Report | Fight | Duration | `Rallying Cry` |
| ---: | --- | ---: | ---: | --- |
| 1 | [aVQbrt6CNzPgKRHJ](https://www.warcraftlogs.com/reports/aVQbrt6CNzPgKRHJ?fight=21) | 21 | 05:58 | `05:13` |
| 2 | [jAaWBcMmbtLKd2X7](https://www.warcraftlogs.com/reports/jAaWBcMmbtLKd2X7?fight=33) | 33 | 04:57 | `02:30` |
| 3 | [47jarVtFKYLgZpcf](https://www.warcraftlogs.com/reports/47jarVtFKYLgZpcf?fight=5) | 5 | 05:06 | `02:02` |
| 4 | [YhPLcJ4mdGyKzFWf](https://www.warcraftlogs.com/reports/YhPLcJ4mdGyKzFWf?fight=5) | 5 | 04:55 | `00:52` |
| 5 | [NGXQpDynTvbLa9Fc](https://www.warcraftlogs.com/reports/NGXQpDynTvbLa9Fc?fight=24) | 24 | 05:22 | `02:36` |

Planning read: if we want the Warrior tank defensive to match top-parse behavior, use `Rallying Cry` around `02:30-02:40`. If we want it to smooth the start of the danger ramp instead, `02:10-02:15` is still defensible from our damage-window review, but Lorrgs top parses lean later.

## Demon Hunter DPS

Spec endpoints:

```text
https://api2.lorrgs.io/api/spec_ranking/demonhunter-devourer/beloren-child-of-alar?difficulty=mythic&metric=dps
https://api2.lorrgs.io/api/spec_ranking/demonhunter-havoc/beloren-child-of-alar?difficulty=mythic&metric=dps
```

Abilities to watch:

- `Darkness`
- `Blur`

### Devourer Demon Hunter

Top Devourer parses mostly do not show `Darkness`. They mainly show personal `Blur`.

Top-50 timing buckets for Devourer `Blur`:

| Window | Count |
| --- | ---: |
| `02:10-02:20` | 7 |
| `02:20-02:30` | 7 |
| `02:50-03:00` | 7 |
| `03:50-04:00` | 7 |
| `04:00-04:10` | 6 |
| `03:20-03:30` | 6 |

Top Devourer examples:

| Rank | Report | Fight | Duration | Defensive casts |
| ---: | --- | ---: | ---: | --- |
| 1 | [r4jxLbndD2pVNgAk](https://www.warcraftlogs.com/reports/r4jxLbndD2pVNgAk?fight=12) | 12 | 04:29 | `Blur 03:50` |
| 2 | [6y4kp8VYXJAtWxRb](https://www.warcraftlogs.com/reports/6y4kp8VYXJAtWxRb?fight=1) | 1 | 05:20 | `Blur 01:15`, `02:56`, `04:03` |
| 5 | [mvLahBKjDMbZXA6W](https://www.warcraftlogs.com/reports/mvLahBKjDMbZXA6W?fight=44) | 44 | 04:26 | `Blur 02:24`, `02:45`, `04:12` |

Planning read: Devourer parses are not good evidence for `Darkness`; they are useful for personal survival timing only.

### Havoc Demon Hunter

Top-50 timing buckets:

| Ability / Window | Count |
| --- | ---: |
| `Darkness 02:40-02:50` | 9 |
| `Blur 02:40-02:50` | 16 |
| `Blur 02:30-02:40` | 8 |
| `Blur 04:40-04:50` | 8 |
| `Blur 04:30-04:40` | 7 |
| `Blur 00:10-00:20` | 7 |

Top Havoc examples:

| Rank | Report | Fight | Duration | Defensive casts |
| ---: | --- | ---: | ---: | --- |
| 1 | [h8Mn7NdkRT9KYx6A](https://www.warcraftlogs.com/reports/h8Mn7NdkRT9KYx6A?fight=11) | 11 | 05:22 | `Darkness 00:50`, `Darkness 05:02`; `Blur 01:59`, `02:38`, `03:05`, `04:40` |
| 3 | [vmtyM2WwAdZf3cqJ](https://www.warcraftlogs.com/reports/vmtyM2WwAdZf3cqJ?fight=30) | 30 | 05:04 | `Darkness 02:41`; `Blur 00:26`, `02:40`, `03:13`, `04:48` |
| 4 | [2BCKZ7jy3cX6rhJT](https://www.warcraftlogs.com/reports/2BCKZ7jy3cX6rhJT?fight=6) | 6 | 05:28 | `Darkness 02:43`; `Blur 02:43` |
| 9 | [yPdvLhV7fgDFC4wM](https://www.warcraftlogs.com/reports/yPdvLhV7fgDFC4wM?fight=24) | 24 | 05:09 | `Darkness 03:49`; `Blur 00:18`, `01:07`, `02:26`, `02:46`, `03:49` |

Planning read: if our DHs can use `Darkness`, the strongest top-parse-backed default is `02:41-02:43`. A second Darkness can be held for `04:50-05:05` if the fight lasts long enough and positioning allows it.

## Unholy Death Knight

Spec endpoint:

```text
https://api2.lorrgs.io/api/spec_ranking/deathknight-unholy/beloren-child-of-alar?difficulty=mythic&metric=dps
```

Abilities to watch:

- `Anti-Magic Zone`
- `Anti-Magic Shell`
- `Icebound Fortitude`

Top-50 timing buckets:

| Ability / Window | Count |
| --- | ---: |
| `Anti-Magic Zone 02:35-02:43` | common in examples |
| `Anti-Magic Shell 00:00-00:10` | 15 |
| `Anti-Magic Shell 02:10-02:20` | 15 |
| `Anti-Magic Shell 03:20-03:30` | 12 |
| `Anti-Magic Shell 04:00-04:10` | 10 |
| `Anti-Magic Shell 05:00-05:10` | 10 |
| `Icebound Fortitude 02:40-02:50` | 7 |

Top Unholy examples:

| Rank | Report | Fight | Duration | Defensive casts |
| ---: | --- | ---: | ---: | --- |
| 2 | [wgkLNhbmnY723yQr](https://www.warcraftlogs.com/reports/wgkLNhbmnY723yQr?fight=13) | 13 | 05:10 | `Anti-Magic Zone 02:36`; `Icebound Fortitude 02:39`, `04:44`; `Anti-Magic Shell 01:15`, `02:02`, `03:22`, `04:04`, `04:56` |
| 4 | [cLNHJ7GWRbfTvhwY](https://www.warcraftlogs.com/reports/cLNHJ7GWRbfTvhwY?fight=27) | 27 | 05:35 | `Anti-Magic Zone 02:43`; `Icebound Fortitude 04:09`; `Anti-Magic Shell 00:01`, `00:50`, `02:09`, `02:50`, `03:35`, `04:29`, `05:11` |
| 7 | [t3MYzp2WyBQ7fDXm](https://www.warcraftlogs.com/reports/t3MYzp2WyBQ7fDXm?fight=35) | 35 | 05:04 | `Anti-Magic Zone 02:35`; `Anti-Magic Shell 03:12`, `04:51` |
| 9 | [ZJTqCQatbXkL64PH](https://www.warcraftlogs.com/reports/ZJTqCQatbXkL64PH?fight=49) | 49 | 04:16 | `Anti-Magic Zone 02:08`; `Icebound Fortitude 02:42`; `Anti-Magic Shell 00:33`, `01:53`, `02:39`, `03:21`, `04:02` |
| 10 | [xbqwjCWdtPhfnaz6](https://www.warcraftlogs.com/reports/xbqwjCWdtPhfnaz6?fight=30) | 30 | 05:31 | `Anti-Magic Zone 02:40`; `Icebound Fortitude 04:51`; `Anti-Magic Shell 02:18`, `03:20`, `04:56` |

Planning read: top Unholy parses strongly support `Anti-Magic Zone` in the mid-fight stack, especially `02:35-02:43`. If we already have too much at that point, the alternative is to keep AMZ for the late `04:50-05:00` push, but that is less represented in the Lorrgs top examples.

## Updated Defensive Planning Implication

Compared with the previous defensive-window draft, Lorrgs top parses push the tank/DPS externals slightly more toward the middle:

| Time | Assignment | Lorrgs support |
| --- | --- | --- |
| `00:50` | Optional `Darkness` or `Anti-Magic Zone` | Seen in some top examples, but not the strongest aggregate point. |
| `02:35-02:43` | `Rallying Cry`, `Anti-Magic Zone`, and/or `Darkness` | Strongest repeated top-parse defensive cluster. |
| `04:45-05:05` | Late `Darkness` or saved `Anti-Magic Zone` | Useful for kill lengths around 5 minutes, but less consistent than the mid-fight stack. |

If we want a Lorrgs-backed first pass:

| Time | Defensive |
| --- | --- |
| `02:35` | Death Knight `Anti-Magic Zone` |
| `02:38` | Warrior tank `Rallying Cry` |
| `02:42` | Demon Hunter `Darkness` |
| `04:50-05:05` | Second Demon Hunter `Darkness` if available and useful |

This is heavier at `02:35-02:43` than the earlier spread plan, but it matches top-parse behavior better.
