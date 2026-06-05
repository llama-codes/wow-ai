# Crown Regidør Paladin Viserio Setup

## Setup Summary

Use this Viserio-source draft if Bobbidyboo is unavailable and Regidør replaces the Restoration Druid.

| Player | Spec | Role |
| --- | --- | --- |
| Santatumblr | Mistweaver Monk | Main healer |
| Regidør | Holy Paladin | Filler healer replacing Restoration Druid |
| Deviiarrc | Preservation Evoker | Main healer |
| Nessalove | Holy Priest | Main healer |

Source plan: `regidor-paladin-healing-plan.md`

Notes:

- This is not a generated JSON import yet.
- The first table is intentionally formatted as a `Time` / `Assignment` timeline so it can feed the local Viserio Markdown-to-import workflow later.
- Mistweaver uses `Revival` because Santatumblr's existing Vanguard export uses that button name.
- Regidør spell rows should use `Avenging Wrath` and `Aura Mastery`, which are present in the existing Vanguard export metadata.
- Spot calls and conditional non-healer raid DR are kept out of the import-source timeline so healer text-to-speech stays clean.

## Import-Source Timeline

| Time | Assignment | Purpose |
| --- | --- | --- |
| `00:05` | Regidør Avenging Wrath | Opener ramp before Echoing Darkness / Void Expulsion |
| `00:10` | Nessalove Apotheosis | Opener into Echoing Darkness / Void Expulsion |
| `00:20` | Deviiarrc Tip the Scales | Echoing Darkness + Void Expulsion setup |
| `00:29` | Santatumblr Revival | Opener reset after Echoing Darkness / Void Expulsion |
| `00:37` | Santatumblr Invoke Yu'lon, the Jade Serpent | Opener recovery into first sustain |
| `00:45` | Nessalove Divine Hymn | Opener tail / first sustain |
| `01:10` | Deviiarrc Rewind | Echoing Darkness / Grasp recovery |
| `01:31` | Deviiarrc Tip the Scales | Mid-cycle damage setup |
| `02:22` | Nessalove Apotheosis | Setup before next Simulacrum pattern |
| `03:08` | Santatumblr Invoke Yu'lon, the Jade Serpent | Simulacrum setup / rolling pressure |
| `03:25` | Regidør Avenging Wrath | Simulacrum setup / missing druid channel |
| `03:29` | Nessalove Divine Hymn | Simulacrum setup continuation |
| `03:55` | Santatumblr Revival | Fast-timer Simulacrum safety into 04:20 |
| `04:20` | Regidør Aura Mastery | Simulacrum Backlash + Void Expulsion + Voidstalker Sting |
| `04:38` | Deviiarrc Tip the Scales | Simulacrum continuation setup |
| `04:47` | Nessalove Apotheosis | Simulacrum continuation |
| `05:38` | Regidør Avenging Wrath | 05:40-06:00 transition |
| `05:50` | Santatumblr Invoke Yu'lon, the Jade Serpent + Celestial Conduit | Gravity Collapse + Cosmic Barrier transition |
| `06:04` | Deviiarrc Tip the Scales | Gravity / Cosmic continuation setup |
| `06:38` | Deviiarrc Rewind, Nessalove Divine Hymn | Gravity Collapse + Cosmic Barrier + Voidstalker Sting |
| `06:53` | Nessalove Apotheosis | 07:00 sustain bridge |
| `07:34` | Deviiarrc Tip the Scales | 07:40-08:00 buildup |
| `07:36` | Regidør Aura Mastery | Late Gravity/Cosmic overlap |
| `07:48` | Regidør Avenging Wrath | Final wall throughput |
| `07:55` | Santatumblr Revival + Celestial Conduit | Late Cosmic Barrier + Voidstalker Sting + Gravity Collapse reset |
| `08:03` | Santatumblr Invoke Yu'lon, the Jade Serpent | Long-kill final sustain |
| `08:41` | Nessalove Divine Hymn | 08:40+ finish pressure |
| `08:55` | Nessalove Apotheosis | 08:55 finish pressure |

## Actor Assignments

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

### Regidør - Holy Paladin

| Time | Assignment |
| --- | --- |
| `00:05` | Avenging Wrath |
| `03:25` | Avenging Wrath |
| `04:20` | Aura Mastery |
| `05:38` | Avenging Wrath |
| `07:36` | Aura Mastery |
| `07:48` | Avenging Wrath |

### Deviiarrc - Preservation Evoker

| Time | Assignment |
| --- | --- |
| `00:20` | Tip the Scales |
| `01:10` | Rewind |
| `01:31` | Tip the Scales |
| `04:38` | Tip the Scales |
| `06:04` | Tip the Scales |
| `06:38` | Rewind |
| `07:34` | Tip the Scales |

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

## Shareable Healer Notes

These are separated from the Viserio import-source timeline so they do not become long text-to-speech callouts.

| Time | Player | Note |
| --- | --- | --- |
| `04:30` | Santatumblr | Life Cocoon assigned Simulacrum target if needed. |
| `04:30` | Nessalove | Guardian Spirit assigned Simulacrum target if needed. |
| `04:30` | Regidør | Blessing of Sacrifice / Lay on Hands assigned Simulacrum target if needed. |
| `06:00` | Raid | Assign Rallying Cry / AMZ / Darkness equivalent before the 06:04 Pres setup. |
| `07:36` | Deviiarrc | Zephyr if no other Evoker covers the late Gravity/Cosmic overlap. |
| `07:36` | Raid | Assign AMZ/Darkness/equivalent if available. |
| `07:55` | Regidør | Blessing of Sacrifice / Lay on Hands assigned late Gravity/Cosmic target if needed. |
| `07:55` | Santatumblr | Life Cocoon assigned late Gravity/Cosmic target if needed. |
| `07:55` | Nessalove | Guardian Spirit assigned late Gravity/Cosmic target if needed. |

## Swap Rules To Preserve In Viserio Notes

| Trigger | Adjustment |
| --- | --- |
| The raid dies at `04:20-04:30`. | Keep Santatumblr `03:55` Revival and Regidør `04:20` Aura Mastery. Add Deviiarrc Rewind at `04:20` only if `06:40` has another answer. |
| The raid dies at `06:00-06:10`. | Add external raid DR at `06:00`; do not move the `06:38` Rewind unless `06:40` is already safe. |
| The raid dies at `06:40-06:50`. | Keep Nessalove `06:38` Hymn and Deviiarrc `06:38` Rewind. If still dying, move Regidør `07:36` Aura Mastery to `06:34`. |
| The raid dies at `07:30-07:50`. | Keep Regidør `07:36` Aura Mastery and add Zephyr / AMZ / Darkness there. |
| The raid dies at `08:00-08:10`. | Keep Santatumblr `07:55` Revival, Regidør `07:48` Avenging Wrath, and save spot externals for the 08:00 overlap. |
