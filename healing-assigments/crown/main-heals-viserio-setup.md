# Crown Main Heals Viserio Setup

## Setup Summary

This is the human-edited Viserio setup draft for Crown of the Cosmos using only the main healers from `../raid-comp.md`.

| Player | Spec | Role |
| --- | --- | --- |
| Bobbidyboo | Restoration Druid | Main healer |
| Nessalove | Holy Priest | Main healer |
| Deviiarrc | Preservation Evoker | Main healer |
| Santatumblr | Mistweaver Monk | Main healer |

Source plan: `our-comp-healing-plan.md`

Notes:

- This is not a generated JSON import yet.
- The first table is intentionally formatted as a `Time` / `Assignment` timeline so it can feed the local Viserio Markdown-to-import workflow later.
- Mistweaver uses `Revival` because Santatumblr's existing Vanguard export uses that button name.
- Bobbidyboo's Convoke timings are shifted a few seconds earlier where needed to preserve a legal 60-second cadence while still covering the planned windows.
- Spot calls and conditional notes are kept out of the import-source timeline so healer text-to-speech stays clean.

## Import-Source Timeline

| Time | Assignment | Purpose |
| --- | --- | --- |
| `00:05` | Bobbidyboo Convoke the Spirits | Opener ramp before Echoing Darkness / Void Expulsion |
| `00:08` | Nessalove Apotheosis | Opener into Echoing Darkness / Void Expulsion |
| `00:12` | Bobbidyboo Tranquility | Opener Echoing Darkness ramp |
| `00:20` | Deviiarrc Tip the Scales | Echoing Darkness + Void Expulsion setup |
| `00:27` | Santatumblr Revival | Opener reset after Echoing Darkness / Void Expulsion |
| `00:30` | Deviiarrc Rewind | Opener recovery |
| `00:40` | Santatumblr Invoke Yu'lon, the Jade Serpent | Opener recovery into first sustain |
| `01:05` | Bobbidyboo Convoke the Spirits | Echoing Darkness + Void Expulsion |
| `01:45` | Nessalove Divine Hymn, Santatumblr Celestial Conduit | Free stabilizer before both return for later windows |
| `02:15` | Bobbidyboo Convoke the Spirits | Low/mid damage setup; avoid sitting on Convoke |
| `02:58` | Nessalove Apotheosis | Setup before next Simulacrum pattern |
| `03:05` | Santatumblr Invoke Yu'lon, the Jade Serpent | Simulacrum setup / rolling pressure |
| `03:17` | Bobbidyboo Convoke the Spirits | Simulacrum setup while keeping Convoke cadence |
| `03:30` | Bobbidyboo Tranquility | Simulacrum setup / timer drift safety |
| `03:55` | Santatumblr Celestial Conduit | Fast-timer Simulacrum Backlash safety |
| `04:17` | Bobbidyboo Convoke the Spirits | Prep coverage for the 04:20 Simulacrum window |
| `04:20` | Deviiarrc Rewind + Tip the Scales | Simulacrum Backlash + Void Expulsion + Voidstalker Sting |
| `04:44` | Nessalove Divine Hymn | Simulacrum Backlash / Voidstalker Sting continuation |
| `04:50` | Santatumblr Revival | Simulacrum Backlash + Voidstalker Sting + Void Barrage reset |
| `05:07` | Nessalove Apotheosis | Simulacrum Backlash + Void Expulsion + Voidstalker Sting |
| `05:10` | Santatumblr Invoke Yu'lon, the Jade Serpent | Rolling healing through the 05:10 Simulacrum window |
| `05:17` | Bobbidyboo Convoke the Spirits | Simulacrum continuation |
| `05:50` | Santatumblr Celestial Conduit, Deviiarrc Tip the Scales | Gravity Collapse + Cosmic Barrier transition |
| `06:20` | Bobbidyboo Convoke the Spirits | Gravity Collapse + Void Expulsion |
| `06:40` | Bobbidyboo Tranquility | Gravity Collapse + Cosmic Barrier + Voidstalker Sting |
| `06:48` | Nessalove Divine Hymn | Staggered coverage after Tranq |
| `07:08` | Nessalove Apotheosis | Gravity Collapse + Void Expulsion + Voidstalker Sting |
| `07:10` | Santatumblr Invoke Yu'lon, the Jade Serpent | Late Gravity rolling pressure |
| `07:20` | Bobbidyboo Convoke the Spirits, Santatumblr Celestial Conduit | Gravity Collapse / Cosmic Barrier buildup |
| `07:24` | Deviiarrc Tip the Scales | Prep for final Gravity/Cosmic overlap |
| `07:50` | Deviiarrc Rewind, Santatumblr Revival | Final Gravity Collapse + Cosmic Barrier + Voidstalker Sting reset burst |
| `08:20` | Bobbidyboo Convoke the Spirits | Long-kill Gravity Collapse / Void Expulsion contingency |

## Actor Assignments

### Bobbidyboo - Restoration Druid

| Time | Assignment |
| --- | --- |
| `00:05` | Convoke the Spirits |
| `00:12` | Tranquility |
| `01:05` | Convoke the Spirits |
| `02:15` | Convoke the Spirits |
| `03:17` | Convoke the Spirits |
| `03:30` | Tranquility |
| `04:17` | Convoke the Spirits |
| `05:17` | Convoke the Spirits |
| `06:20` | Convoke the Spirits |
| `06:40` | Tranquility |
| `07:20` | Convoke the Spirits |
| `08:20` | Convoke the Spirits |

### Nessalove - Holy Priest

| Time | Assignment |
| --- | --- |
| `00:08` | Apotheosis |
| `01:45` | Divine Hymn |
| `02:58` | Apotheosis |
| `04:44` | Divine Hymn |
| `05:07` | Apotheosis |
| `06:48` | Divine Hymn |
| `07:08` | Apotheosis |

### Deviiarrc - Preservation Evoker

| Time | Assignment |
| --- | --- |
| `00:20` | Tip the Scales |
| `00:30` | Rewind |
| `04:20` | Rewind |
| `04:20` | Tip the Scales |
| `05:50` | Tip the Scales |
| `07:24` | Tip the Scales |
| `07:50` | Rewind |

### Santatumblr - Mistweaver Monk

| Time | Assignment |
| --- | --- |
| `00:27` | Revival |
| `00:40` | Invoke Yu'lon, the Jade Serpent |
| `01:45` | Celestial Conduit |
| `03:05` | Invoke Yu'lon, the Jade Serpent |
| `03:55` | Celestial Conduit |
| `04:50` | Revival |
| `05:10` | Invoke Yu'lon, the Jade Serpent |
| `05:50` | Celestial Conduit |
| `07:10` | Invoke Yu'lon, the Jade Serpent |
| `07:20` | Celestial Conduit |
| `07:50` | Revival |

## Shareable Healer Notes

These are separated from the Viserio import-source timeline so they do not become long text-to-speech callouts.

| Time | Player | Note |
| --- | --- | --- |
| `04:20` | Nessalove | Guardian Spirit assigned Simulacrum target if needed. |
| `04:20` | Santatumblr | Life Cocoon assigned Simulacrum target if needed. |
| `06:48` | Deviiarrc | Zephyr during Cosmic Barrier / Gravity continuation. |
| `07:50` | Nessalove | Guardian Spirit assigned late Gravity target if needed. |
| `07:50` | Santatumblr | Life Cocoon assigned late Gravity target if needed. |

## Swap Rules To Preserve In Viserio Notes

| Trigger | Adjustment |
| --- | --- |
| Rewind is not back for `07:50` after the `04:20` use. | Delete Deviiarrc `04:20` Rewind and keep the `07:50` Rewind. |
| The raid dies at `03:20-03:35`. | Move Santatumblr `04:50` Revival to `03:29`, then decide whether the next Revival lands at `07:25` or `07:50`. |
| The raid dies before `06:48` Hymn lands. | Move Nessalove Hymn to `06:40` and move Deviiarrc Zephyr note to `06:38`. |
| The raid consistently reaches `08:10+`. | Delay one final reset toward `08:05-08:10` only after confirming `07:50` survives without it. |
