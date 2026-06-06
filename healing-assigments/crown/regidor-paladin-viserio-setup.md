# Crown Combined Healer Viserio Setup

## Setup Summary

Use this Viserio-source draft as the single import source for both fourth-healer options: Bobbidyboo on Restoration Druid and Regidør on Holy Paladin.

Santatumblr, Deviiarrc, and Nessalove keep the same timings. Bobbidyboo and Regidør are both included in the generated import so either fourth-healer package is visible from the same Viserio assignment set.

| Player | Spec | Role |
| --- | --- | --- |
| Santatumblr | Mistweaver Monk | Shared healer, unchanged timings |
| Deviiarrc | Preservation Evoker | Shared healer, unchanged timings |
| Nessalove | Holy Priest | Shared healer, unchanged timings |
| Bobbidyboo | Restoration Druid | Fourth-healer option A |
| Regidør | Holy Paladin | Fourth-healer option B |

Source plans: `our-comp-healing-plan.md`, `regidor-paladin-healing-plan.md`

Generated import:

| Import file | Fourth-healer rows included |
| --- | --- |
| `regidor-paladin-viserio-assignments.json` | Bobbidyboo, Regidør, Santatumblr, Deviiarrc, and Nessalove only |

## Bobbidyboo To Regidør Coverage Map

| Damage window | Bobbidyboo package | Regidør package | Swap read |
| --- | --- | --- | --- |
| Opener / `00:20` | `00:05` Convoke + shared opener CDs | `00:00` Avenging Wrath + shared opener CDs | Both versions spend early without committing the big DR/channel yet. |
| `01:00-01:10` | `00:57` Tranquility + `01:05` Convoke | `00:57` Aura Mastery + shared `01:10` Rewind | Both fourth-healer packages now cover the same early damage window. |
| `02:10-02:22` | `02:10` Convoke | `02:00` Avenging Wrath | Wings is active through the Convoke window. |
| `03:10-03:40` | `03:10` Convoke + shared Yu'lon, Conduit, Hymn, and Stasis | Shared Yu'lon, Conduit, Hymn, and Stasis | This window is shared-healer driven in both versions. |
| `04:20-04:30` | `04:10` Convoke + `04:20` Tranquility | `04:00` Avenging Wrath + `04:20` Aura Mastery | Both fourth-healer packages cover the 04:20 Simulacrum wall. |
| `05:10-05:20` | `05:13` Convoke | Shared `05:10` Stasis pop + Priest coverage | No direct Paladin button; unchanged Evoker/Priest coverage carries this filler window. |
| `06:00-06:15` | `06:13` Convoke | `06:00` Avenging Wrath + shared `06:04` Rewind | Wings covers the 06:00 gravity chain and the 06:13 Convoke slot. |
| `06:40-06:50` | Shared `06:38` Hymn + `06:40` Stasis pop | Shared `06:38` Hymn + `06:40` Stasis pop | Both versions hold the fourth-healer DR/channel for the later overlap. |
| `07:30-07:50` | `07:15` Convoke + `07:36` Tranquility | `07:36` Aura Mastery + assigned raid DR | Both fourth-healer packages cover the late Gravity/Cosmic overlap. |
| `08:00-08:20` | `08:16` Convoke | `08:00` Avenging Wrath + shared `08:00` Stasis pop | Wings is active through the long-kill final Convoke slot. |

Notes:

- This Markdown is the single human-edited source for the generated JSON import.
- The first table is intentionally formatted as a `Time` / `Assignment` timeline so it can feed the local Viserio Markdown-to-import workflow later.
- The `Variant` column is a label only: `Shared` rows are the three unchanged healers, `Druid` rows are Bobbidyboo, and `Paladin` rows are Regidør.
- Mistweaver uses `Revival` because Santatumblr's existing Vanguard export uses that button name.
- The generated import intentionally contains both Bobbidyboo and Regidør rows in one file, trimmed to only the five assigned players.
- Bobbidyboo rows use `Convoke the Spirits` and `Tranquility`, which are present in the existing Vanguard export metadata.
- Regidør spell rows should use `Avenging Wrath` and `Aura Mastery`, which are present in the existing Vanguard export metadata.
- Bobbidyboo's Tranquility and Regidør's Aura Mastery both sit on the same damage windows: `00:57`, `04:20`, and `07:36`.
- Spot calls and conditional non-healer raid DR are kept out of the import-source timeline so healer text-to-speech stays clean.

## Import-Source Timeline

| Time | Variant | Assignment | Purpose |
| --- | --- | --- | --- |
| `00:00` | Paladin | Regidør Avenging Wrath | Pull ramp before Echoing Darkness / Void Expulsion |
| `00:05` | Druid | Bobbidyboo Convoke the Spirits | Opener ramp before Echoing Darkness / Void Expulsion |
| `00:06` | Shared | Santatumblr Celestial Conduit | Early Monk throughput; mirrors the R04 Monk cadence |
| `00:10` | Shared | Nessalove Apotheosis | Opener into Echoing Darkness / Void Expulsion |
| `00:20` | Shared | Deviiarrc Stasis + Tip the Scales | Echoing Darkness + Void Expulsion setup |
| `00:29` | Shared | Santatumblr Revival | Opener reset after Echoing Darkness / Void Expulsion |
| `00:30` | Shared | Deviiarrc Stasis pop | Release opener Stasis payload |
| `00:37` | Shared | Santatumblr Invoke Yu'lon, the Jade Serpent | Opener recovery into first sustain |
| `00:45` | Shared | Nessalove Divine Hymn | Opener tail / first sustain |
| `00:57` | Druid | Bobbidyboo Tranquility | Covers the same early damage window as Regidør's Aura Mastery |
| `00:57` | Paladin | Regidør Aura Mastery | Covers the same early damage window as Bobbidyboo's `01:05` Convoke |
| `01:05` | Druid | Bobbidyboo Convoke the Spirits | Echoing Darkness + Void Expulsion |
| `01:10` | Shared | Deviiarrc Rewind | Echoing Darkness / Grasp recovery |
| `01:31` | Shared | Deviiarrc Tip the Scales | Mid-cycle damage setup |
| `01:38` | Shared | Santatumblr Celestial Conduit | Second Monk Conduit window; removes 01:40 dead space |
| `01:50` | Shared | Deviiarrc Stasis | Second Stasis setup; keeps Evoker cadence rolling |
| `02:00` | Paladin | Regidør Avenging Wrath | Extra early wings use; fills the old opener-to-midfight gap |
| `02:10` | Druid | Bobbidyboo Convoke the Spirits | Low/mid damage setup; avoid sitting on Convoke |
| `02:10` | Shared | Deviiarrc Stasis pop | Release second Stasis package |
| `02:22` | Shared | Nessalove Apotheosis | Setup before next Simulacrum pattern |
| `03:08` | Shared | Santatumblr Invoke Yu'lon, the Jade Serpent | Simulacrum setup / rolling pressure |
| `03:10` | Druid | Bobbidyboo Convoke the Spirits | Simulacrum setup while keeping Convoke cadence |
| `03:20` | Shared | Deviiarrc Stasis | Third Stasis setup for the Simulacrum chain |
| `03:24` | Shared | Santatumblr Celestial Conduit | Simulacrum Monk Conduit window |
| `03:29` | Shared | Nessalove Divine Hymn | Simulacrum setup continuation |
| `03:40` | Shared | Deviiarrc Stasis pop | Release during the Simulacrum chain |
| `03:55` | Shared | Santatumblr Revival | Fast-timer Simulacrum safety into 04:20 |
| `04:00` | Paladin | Regidør Avenging Wrath | Wings ramp into the 04:20 Simulacrum wall |
| `04:10` | Druid | Bobbidyboo Convoke the Spirits | Prep coverage for the 04:20 Simulacrum window |
| `04:20` | Druid | Bobbidyboo Tranquility | Covers the 04:20 Simulacrum damage window |
| `04:20` | Paladin | Regidør Aura Mastery | Covers the 04:20 Simulacrum damage window |
| `04:38` | Shared | Deviiarrc Tip the Scales | Simulacrum continuation setup |
| `04:47` | Shared | Nessalove Apotheosis | Simulacrum continuation |
| `04:50` | Shared | Deviiarrc Stasis | Fourth Stasis setup for the 05:10 damage window |
| `05:10` | Shared | Deviiarrc Stasis pop | Release into the 05:10 Simulacrum damage |
| `05:13` | Druid | Bobbidyboo Convoke the Spirits | Simulacrum Backlash + Void Expulsion + Voidstalker Sting |
| `05:46` | Shared | Santatumblr Celestial Conduit | Monk Conduit into the 06:00 transition |
| `05:50` | Shared | Santatumblr Invoke Yu'lon, the Jade Serpent | Gravity Collapse + Cosmic Barrier transition |
| `06:00` | Paladin | Regidør Avenging Wrath | Wings for the 06:00-06:40 gravity chain |
| `06:04` | Shared | Deviiarrc Rewind + Tip the Scales | Gravity Collapse + Cosmic Barrier reset burst |
| `06:13` | Druid | Bobbidyboo Convoke the Spirits | Gravity continuation |
| `06:20` | Shared | Deviiarrc Stasis | Fifth Stasis setup for the 06:40 overlap |
| `06:38` | Shared | Nessalove Divine Hymn | Gravity Collapse + Voidstalker Sting |
| `06:40` | Shared | Deviiarrc Stasis pop | Release into the 06:40 Gravity/Cosmic overlap |
| `06:53` | Shared | Nessalove Apotheosis | 07:00 sustain bridge |
| `07:05` | Shared | Santatumblr Revival | Late reset for the 07:00 damage chain |
| `07:15` | Druid | Bobbidyboo Convoke the Spirits | Gravity / Cosmic sustain |
| `07:19` | Shared | Santatumblr Celestial Conduit | Monk Conduit for the 07:20-07:40 ramp |
| `07:34` | Shared | Deviiarrc Tip the Scales | 07:40-08:00 buildup |
| `07:36` | Druid | Bobbidyboo Tranquility | Covers the late Gravity/Cosmic overlap |
| `07:36` | Paladin | Regidør Aura Mastery | Covers the late Gravity/Cosmic overlap |
| `07:50` | Shared | Deviiarrc Stasis | Final Stasis setup |
| `08:00` | Shared | Deviiarrc Stasis pop | Release into the 08:00 final wall |
| `08:00` | Paladin | Regidør Avenging Wrath | Long-kill final wall throughput |
| `08:03` | Shared | Santatumblr Invoke Yu'lon, the Jade Serpent | Long-kill final sustain |
| `08:16` | Druid | Bobbidyboo Convoke the Spirits | Long-kill Gravity / Void pressure |
| `08:41` | Shared | Nessalove Divine Hymn | 08:40+ finish pressure |
| `08:55` | Shared | Nessalove Apotheosis | 08:55 finish pressure |

## Actor Assignments

### Bobbidyboo - Restoration Druid

| Time | Assignment |
| --- | --- |
| `00:05` | Convoke the Spirits |
| `00:57` | Tranquility |
| `01:05` | Convoke the Spirits |
| `02:10` | Convoke the Spirits |
| `03:10` | Convoke the Spirits |
| `04:10` | Convoke the Spirits |
| `04:20` | Tranquility |
| `05:13` | Convoke the Spirits |
| `06:13` | Convoke the Spirits |
| `07:15` | Convoke the Spirits |
| `07:36` | Tranquility |
| `08:16` | Convoke the Spirits |

### Santatumblr - Mistweaver Monk

| Time | Assignment |
| --- | --- |
| `00:06` | Celestial Conduit |
| `00:29` | Revival |
| `00:37` | Invoke Yu'lon, the Jade Serpent |
| `01:38` | Celestial Conduit |
| `03:08` | Invoke Yu'lon, the Jade Serpent |
| `03:24` | Celestial Conduit |
| `03:55` | Revival |
| `05:46` | Celestial Conduit |
| `05:50` | Invoke Yu'lon, the Jade Serpent |
| `07:05` | Revival |
| `07:19` | Celestial Conduit |
| `08:03` | Invoke Yu'lon, the Jade Serpent |

### Regidør - Holy Paladin

| Time | Assignment |
| --- | --- |
| `00:00` | Avenging Wrath |
| `00:57` | Aura Mastery |
| `02:00` | Avenging Wrath |
| `04:00` | Avenging Wrath |
| `04:20` | Aura Mastery |
| `06:00` | Avenging Wrath |
| `07:36` | Aura Mastery |
| `08:00` | Avenging Wrath |

### Deviiarrc - Preservation Evoker

| Time | Assignment |
| --- | --- |
| `00:20` | Stasis |
| `00:20` | Tip the Scales |
| `00:30` | Stasis pop |
| `01:10` | Rewind |
| `01:31` | Tip the Scales |
| `01:50` | Stasis |
| `02:10` | Stasis pop |
| `03:20` | Stasis |
| `03:40` | Stasis pop |
| `04:38` | Tip the Scales |
| `04:50` | Stasis |
| `05:10` | Stasis pop |
| `06:04` | Rewind |
| `06:04` | Tip the Scales |
| `06:20` | Stasis |
| `06:40` | Stasis pop |
| `07:34` | Tip the Scales |
| `07:50` | Stasis |
| `08:00` | Stasis pop |

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
| `04:30` | Bobbidyboo | Druid option: Ironbark assigned Simulacrum target if needed. |
| `04:30` | Regidør | Paladin option: Blessing of Sacrifice / Lay on Hands assigned Simulacrum target if needed. |
| `06:00` | Raid | Assign Rallying Cry / AMZ / Darkness equivalent before Deviiarrc `06:04` Rewind. |
| `06:40` | Raid | Both options use shared Hymn and Stasis here; add external DR if this still feels weak. |
| `07:36` | Bobbidyboo | Druid option: Tranquility covers the late Gravity/Cosmic overlap. |
| `07:36` | Regidør | Paladin option: Aura Mastery covers the late Gravity/Cosmic overlap. |
| `07:36` | Deviiarrc | Zephyr if no other Evoker covers the late Gravity/Cosmic overlap. |
| `07:36` | Raid | Assign AMZ/Darkness/equivalent if available. |
| `07:05` | Santatumblr | Life Cocoon assigned late Gravity/Cosmic target if needed. |
| `08:00` | Regidør | Paladin option: Blessing of Sacrifice / Lay on Hands assigned late Gravity/Cosmic target if needed. |
| `08:00` | Nessalove | Guardian Spirit assigned late Gravity/Cosmic target if needed. |

## Swap Rules To Preserve In Viserio Notes

| Trigger | Adjustment |
| --- | --- |
| The raid dies at `04:20-04:30`. | Keep Santatumblr `03:55` Revival. Druid option keeps Bobbidyboo `04:10` Convoke + `04:20` Tranquility; Paladin option keeps Regidør `04:00` Wings + `04:20` Aura. Add spot saves at `04:30` before changing shared healers. |
| The raid dies at `06:00-06:10`. | Keep Deviiarrc `06:04` Rewind and add external raid DR at `06:00`. |
| The raid dies at `06:40-06:50`. | Both options use Nessalove `06:38` Hymn and Deviiarrc `06:40` Stasis pop. If still dying, add raid DR here before moving the `07:36` fourth-healer button. |
| The raid dies at `07:30-07:50`. | Keep Santatumblr `07:05` Revival and `07:19` Conduit. Druid option keeps Bobbidyboo `07:15` Convoke + `07:36` Tranquility; Paladin option keeps Regidør `07:36` Aura Mastery plus Zephyr / AMZ / Darkness there. |
| The raid dies at `08:00-08:10`. | Keep the `07:19` Conduit and `08:00` Stasis pop. Druid option uses Bobbidyboo `08:16` Convoke if the pull continues; Paladin option uses Regidør `08:00` Avenging Wrath. Save spot externals for the 08:00 overlap. |
