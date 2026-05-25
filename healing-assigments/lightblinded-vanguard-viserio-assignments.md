# Lightblinded Vanguard Viserio Assignments

## Import Summary

The final generated Viserio import from the chat validated with:

- `8` actors
- `70` spell assignments
- `35` notes
- `2` phases
- `0` custom grid rows

The import used the correct Viserio assignment shape: top-level `actors`, `phases`, and `customGridRows`, with each player's casts nested under that actor's `spells` array.

Import file: [lightblinded-vanguard-viserio-assignments.json](./lightblinded-vanguard-viserio-assignments.json)

## Actor Assignments

### Bobbidyboo - Restoration Druid

| Time | Assignment |
| --- | --- |
| `00:10` | Convoke the Spirits |
| `00:21` | Tranquility |
| `01:14` | Convoke the Spirits |
| `02:17` | Convoke the Spirits |
| `03:22` | Tranquility |
| `03:29` | Convoke the Spirits |
| `04:35` | Convoke the Spirits |
| `05:39` | Convoke the Spirits |
| `06:33` | Tranquility |

### Nessalove - Holy Priest

| Time | Assignment |
| --- | --- |
| `00:00` | Note: Mass Dispel boss bubbles |
| `00:12` | Divine Hymn |
| `00:23` | Apotheosis |
| `02:19` | Divine Hymn |
| `02:25` | Apotheosis |
| `04:35` | Apotheosis |
| `05:18` | Divine Hymn |

### Deviiarrc - Preservation Evoker

| Time | Assignment |
| --- | --- |
| `00:18` | Note: Do not cast Dream Breath; save for Stasis combo |
| `00:22` | Rewind |
| `00:38` | Stasis |
| `00:38` | Tip the Scales |
| `00:52` | Vaelgor's Final Stare |
| `00:58` | Stasis pop |
| `01:48` | Note: Do not cast Dream Breath; save for Stasis combo |
| `02:08` | Stasis |
| `02:08` | Tip the Scales |
| `02:22` | Vaelgor's Final Stare |
| `02:28` | Stasis pop |
| `03:17` | Rewind |
| `03:18` | Note: Do not cast Dream Breath; save for Stasis combo |
| `03:38` | Stasis |
| `03:38` | Tip the Scales |
| `03:52` | Vaelgor's Final Stare |
| `03:58` | Stasis pop |
| `04:48` | Note: Do not cast Dream Breath; save for Stasis combo |
| `05:08` | Stasis |
| `05:08` | Tip the Scales |
| `05:22` | Vaelgor's Final Stare |
| `05:28` | Stasis pop |
| `06:18` | Note: Do not cast Dream Breath; save for Stasis combo |
| `06:38` | Stasis |
| `06:38` | Tip the Scales |
| `06:52` | Vaelgor's Final Stare |
| `06:58` | Stasis pop |
| `06:59` | Rewind |

### Regidør - Holy Paladin

| Time | Assignment |
| --- | --- |
| `00:20` | Avenging Wrath |
| `02:24` | Avenging Wrath |
| `02:24` | Aura Mastery |
| `04:24` | Avenging Wrath |
| `05:50` | Aura Mastery |
| `06:24` | Avenging Wrath |

### Wyldfire - Restoration Druid

| Time | Assignment |
| --- | --- |
| `00:20` | Convoke the Spirits |
| `01:20` | Convoke the Spirits |
| `02:24` | Tranquility |
| `03:24` | Convoke the Spirits |
| `04:24` | Convoke the Spirits |
| `05:24` | Convoke the Spirits |
| `05:50` | Tranquility |
| `06:24` | Convoke the Spirits |

### Santatumblr - Mistweaver Monk

| Time | Assignment |
| --- | --- |
| `00:58` | Celestial Conduit |
| `01:12` | Revival |
| `01:28` | Invoke Yu'lon, the Jade Serpent |
| `02:28` | Celestial Conduit |
| `03:33` | Invoke Yu'lon, the Jade Serpent |
| `03:54` | Revival |
| `03:58` | Celestial Conduit |
| `05:28` | Celestial Conduit |
| `05:39` | Invoke Yu'lon, the Jade Serpent |
| `06:36` | Revival |
| `06:58` | Celestial Conduit |

### Flakiron - Protection Warrior

| Time | Assignment |
| --- | --- |
| `02:24` | Rallying Cry |
| `05:27` | Rallying Cry |

### Everyone

| Time | Assignment |
| --- | --- |
| `00:18` | Note: Dispels |
| `01:12` | Note: Dispels |
| `01:21` | Note: Venel / Execution Sentence incoming |
| `01:25` | Personals |
| `01:36` | Note: Dispels |
| `01:48` | Note: Dispels |
| `02:06` | Note: Dispels |
| `02:17` | Note: Senn / Aura of Peace / Execution Sentence incoming |
| `02:20` | Note: Dispels |
| `02:25` | Note: Healthstones for Execution Sentence hit |
| `02:26` | Note: Dispels |
| `02:27` | Note: Hard focus Tyr's Wrath absorbs; clear before `02:45` |
| `02:42` | Note: Dispels |
| `02:45` | Personals |
| `03:00` | Note: Dispels |
| `03:07` | Note: Bellamy 2 |
| `03:54` | Note: Dispels |
| `04:00` | Note: Venel 2 |
| `04:05` | Personals |
| `04:15` | Note: Dispels |
| `04:30` | Note: Dispels |
| `04:33` | Note: Sacred Toll - stabilize |
| `04:48` | Note: Dispels |
| `04:56` | Note: Senn 2 |
| `04:59` | Note: Dispels |
| `05:05` | Personals |
| `05:06` | Note: Dispels |
| `05:26` | Note: Dispels |
| `05:27` | Personals |
| `05:42` | Note: Dispels |
| `05:46` | Note: Bellamy 3 |
| `06:03` | Note: Sacred Toll |
| `06:36` | Note: Dispels |
| `06:54` | Note: Dispels |

## Patch Notes From The Chat

- The first Viserio attempt used a legacy `playerSpells` / `playerNotes` structure and failed import validation.
- The corrected import nested assignments under each actor.
- The final patch added real spell rows for `Convoke the Spirits`, `Tranquility`, `Avenging Wrath`, `Stasis`, `Stasis pop`, `Tip the Scales`, `Vaelgor's Final Stare`, `Rallying Cry`, and `Celestial Conduit`.
- Wyldfire was added as a Restoration Druid fallback actor with optimized Convoke timings around the Regidør absence swap.
- Stasis, Stasis pop, Tip the Scales, and Vaelgor's Final Stare use exported Viserio metadata from the manual current-usage export.
- Celestial Conduit uses exported Viserio metadata from the manual current-usage export and is back on its previous cadence.
- The current plan stacks Celestial Conduit with the full Stasis package on the previous Celestial Conduit windows.
- Everyone dispel text reminders were copied from the manual current-usage export as Viserio notes.
- Deviiarrc has Stasis prep reminders 20 seconds before each combo to keep talented Dream Breath available.
- Rallying Cry uses exact exported Viserio metadata from the assignment export, including GUID `cf93a6a0-9835-419c-8db8-a367fd5338e8` and the Battlefield Commander cooldown modifier.
- Mass Dispel and Healthstone were represented as notes where exact exported spell metadata was not available.
