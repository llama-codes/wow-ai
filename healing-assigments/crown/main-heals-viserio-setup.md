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

Regidør swap setup: `regidor-paladin-viserio-setup.md`

Notes:

- This is not a generated JSON import yet.
- The first table is intentionally formatted as a `Time` / `Assignment` timeline so it can feed the local Viserio Markdown-to-import workflow later.
- Mistweaver uses `Revival` because Santatumblr's existing Vanguard export uses that button name.
- This timeline uses the exact-comp default from R06: Deviiarrc Rewind at `01:10` and `06:04`. The optional 3-Rewind mode is preserved in the swap rules, not assigned by default.
- Spot calls and conditional non-healer raid DR are kept out of the import-source timeline so healer text-to-speech stays clean.

## Import-Source Timeline

| Time | Assignment | Purpose |
| --- | --- | --- |
| `00:05` | Bobbidyboo Convoke the Spirits | Opener ramp before Echoing Darkness / Void Expulsion |
| `00:10` | Nessalove Apotheosis | Opener into Echoing Darkness / Void Expulsion |
| `00:13` | Bobbidyboo Tranquility | Opener Echoing Darkness ramp |
| `00:20` | Deviiarrc Tip the Scales | Echoing Darkness + Void Expulsion setup |
| `00:29` | Santatumblr Revival | Opener reset after Echoing Darkness / Void Expulsion |
| `00:37` | Santatumblr Invoke Yu'lon, the Jade Serpent | Opener recovery into first sustain |
| `00:45` | Nessalove Divine Hymn | Opener tail / first sustain |
| `01:05` | Bobbidyboo Convoke the Spirits | Echoing Darkness + Void Expulsion |
| `01:10` | Deviiarrc Rewind | Echoing Darkness / Grasp recovery |
| `01:31` | Deviiarrc Tip the Scales | Mid-cycle damage setup |
| `02:10` | Bobbidyboo Convoke the Spirits | Low/mid damage setup; avoid sitting on Convoke |
| `02:22` | Nessalove Apotheosis | Setup before next Simulacrum pattern |
| `03:08` | Santatumblr Invoke Yu'lon, the Jade Serpent | Simulacrum setup / rolling pressure |
| `03:10` | Bobbidyboo Convoke the Spirits | Simulacrum setup while keeping Convoke cadence |
| `03:15` | Bobbidyboo Tranquility | Simulacrum setup / timer drift safety |
| `03:29` | Nessalove Divine Hymn | Simulacrum setup continuation |
| `03:55` | Santatumblr Revival | Fast-timer Simulacrum safety into 04:20 |
| `04:10` | Bobbidyboo Convoke the Spirits | Prep coverage for the 04:20 Simulacrum window |
| `04:38` | Deviiarrc Tip the Scales | 04:50-05:10 continuation setup |
| `04:47` | Nessalove Apotheosis | Simulacrum continuation |
| `05:13` | Bobbidyboo Convoke the Spirits | Simulacrum Backlash + Void Expulsion + Voidstalker Sting |
| `05:50` | Santatumblr Invoke Yu'lon, the Jade Serpent + Celestial Conduit | Gravity Collapse + Cosmic Barrier transition |
| `06:04` | Deviiarrc Rewind + Tip the Scales | Gravity Collapse + Cosmic Barrier reset burst |
| `06:13` | Bobbidyboo Convoke the Spirits | Gravity continuation |
| `06:38` | Nessalove Divine Hymn | Gravity Collapse + Voidstalker Sting |
| `06:40` | Bobbidyboo Tranquility | Gravity Collapse + Cosmic Barrier + Voidstalker Sting |
| `06:53` | Nessalove Apotheosis | 07:00 sustain bridge |
| `07:15` | Bobbidyboo Convoke the Spirits | Gravity / Cosmic sustain |
| `07:34` | Deviiarrc Tip the Scales | 07:40-08:00 buildup |
| `07:55` | Santatumblr Revival + Celestial Conduit | Late Cosmic Barrier + Voidstalker Sting + Gravity Collapse reset |
| `08:03` | Santatumblr Invoke Yu'lon, the Jade Serpent | Long-kill final sustain |
| `08:16` | Bobbidyboo Convoke the Spirits | Long-kill Gravity / Void pressure |
| `08:41` | Nessalove Divine Hymn | 08:40+ finish pressure |
| `08:55` | Nessalove Apotheosis | 08:55 finish pressure |

## Actor Assignments

### Bobbidyboo - Restoration Druid

| Time | Assignment |
| --- | --- |
| `00:05` | Convoke the Spirits |
| `00:13` | Tranquility |
| `01:05` | Convoke the Spirits |
| `02:10` | Convoke the Spirits |
| `03:10` | Convoke the Spirits |
| `03:15` | Tranquility |
| `04:10` | Convoke the Spirits |
| `05:13` | Convoke the Spirits |
| `06:13` | Convoke the Spirits |
| `06:40` | Tranquility |
| `07:15` | Convoke the Spirits |
| `08:16` | Convoke the Spirits |

### Nessalove - Holy Priest

| Time | Assignment |
| --- | --- |
| `00:10` | Apotheosis |
| `00:45` | Divine Hymn |
| `02:22` | Apotheosis |
| `03:29` | Divine Hymn |
| `04:47` | Apotheosis |
| `06:38` | Divine Hymn |
| `06:53` | Apotheosis |
| `08:41` | Divine Hymn |
| `08:55` | Apotheosis |

### Deviiarrc - Preservation Evoker

| Time | Assignment |
| --- | --- |
| `00:20` | Tip the Scales |
| `01:10` | Rewind |
| `01:31` | Tip the Scales |
| `04:38` | Tip the Scales |
| `06:04` | Rewind |
| `06:04` | Tip the Scales |
| `07:34` | Tip the Scales |

### Santatumblr - Mistweaver Monk

| Time | Assignment |
| --- | --- |
| `00:29` | Revival |
| `00:37` | Invoke Yu'lon, the Jade Serpent |
| `03:08` | Invoke Yu'lon, the Jade Serpent |
| `03:55` | Revival |
| `05:50` | Invoke Yu'lon, the Jade Serpent |
| `05:50` | Celestial Conduit |
| `07:55` | Revival |
| `07:55` | Celestial Conduit |
| `08:03` | Invoke Yu'lon, the Jade Serpent |

## Shareable Healer Notes

These are separated from the Viserio import-source timeline so they do not become long text-to-speech callouts.

| Time | Player | Note |
| --- | --- | --- |
| `04:30` | Santatumblr | Life Cocoon assigned Simulacrum target if needed. |
| `04:30` | Nessalove | Guardian Spirit assigned Simulacrum target if needed. |
| `05:20` | Raid | Assign available non-healer DR; R06 used Zephyr/AMZ around this point. |
| `06:00` | Raid | Assign Rallying Cry / AMZ / Darkness equivalent before Deviiarrc `06:04` Rewind. |
| `07:36` | Deviiarrc | Zephyr if no other Evoker covers the late Gravity/Cosmic overlap. |
| `07:36` | Raid | Assign AMZ/Darkness/equivalent if available. |
| `07:55` | Nessalove | Guardian Spirit assigned late Gravity/Cosmic target if needed. |
| `07:55` | Santatumblr | Life Cocoon assigned late Gravity/Cosmic target if needed. |

## Swap Rules To Preserve In Viserio Notes

| Trigger | Adjustment |
| --- | --- |
| Deviiarrc confirms the 3-Rewind cadence is legal and `06:00` is covered by other raid DR. | Change Rewind to `00:30`, `04:20`, `07:55`; keep `06:04` covered by Rally/AMZ/Darkness. |
| The raid dies at `04:20-04:30`. | Keep Santatumblr `03:55` Revival, then either use aggressive-mode Rewind at `04:20` or shift Nessalove `03:29` Hymn later if the 03:00 section is safe. |
| The raid dies at `06:00-06:10`. | Do not move Deviiarrc `06:04` Rewind earlier; add external raid DR at `06:00`. |
| The raid dies at `07:00-07:20`. | Move Santatumblr `07:55` Revival to `07:05`, then build a separate external package for `07:55-08:05`. |
| The raid dies at `08:00-08:10`. | Keep Santatumblr `07:55` Revival, add late raid DR around `07:36-07:50`, and save spot externals for the 08:00 overlap. |
