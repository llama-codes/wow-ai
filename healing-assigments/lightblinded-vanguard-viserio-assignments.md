# Lightblinded Vanguard Viserio Assignments

## Import Summary

The final generated Viserio import from the chat validated with:

- `7` actors
- `36` spell assignments
- `12` notes
- `2` phases
- `0` custom grid rows

The import used the correct Viserio assignment shape: top-level `actors`, `phases`, and `customGridRows`, with each player's casts nested under that actor's `spells` array.

## Actor Assignments

### Bobbidyboo - Restoration Druid

| Time | Assignment |
| --- | --- |
| `00:10` | Convoke the Spirits |
| `00:21` | Tranquility |
| `01:14` | Convoke the Spirits |
| `02:17` | Convoke the Spirits |
| `03:22` | Tranquility |
| `04:24` | Convoke the Spirits |
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
| `00:10` | Dream Flight |
| `00:22` | Rewind |
| `02:09` | Dream Flight |
| `03:18` | Rewind |
| `04:24` | Dream Flight |

### Regidør - Holy Paladin

| Time | Assignment |
| --- | --- |
| `00:20` | Avenging Wrath |
| `02:24` | Avenging Wrath |
| `02:24` | Aura Mastery |
| `04:24` | Avenging Wrath |
| `05:50` | Aura Mastery |
| `06:24` | Avenging Wrath |

### Santatumblr - Mistweaver Monk

| Time | Assignment |
| --- | --- |
| `01:12` | Revival |
| `01:28` | Invoke Yu'lon, the Jade Serpent |
| `03:33` | Invoke Yu'lon, the Jade Serpent |
| `03:54` | Revival |
| `05:39` | Invoke Yu'lon, the Jade Serpent |
| `06:36` | Revival |

### Flakiron - Protection Warrior

| Time | Assignment |
| --- | --- |
| `02:24` | Note: Rallying Cry - main wipe gate |

### Everyone

| Time | Assignment |
| --- | --- |
| `01:21` | Note: Venel / Execution Sentence incoming |
| `01:25` | Personals |
| `02:17` | Note: Senn / Aura of Peace / Execution Sentence incoming |
| `02:25` | Note: Healthstones for Execution Sentence hit |
| `02:27` | Note: Hard focus Tyr's Wrath absorbs; clear before `02:45` |
| `02:45` | Personals |
| `03:07` | Note: Bellamy 2 |
| `04:00` | Note: Venel 2 |
| `04:05` | Personals |
| `04:33` | Note: Sacred Toll - stabilize |
| `04:56` | Note: Senn 2 |
| `05:05` | Personals |
| `05:27` | Personals |
| `05:46` | Note: Bellamy 3 |
| `06:03` | Note: Sacred Toll |

## Patch Notes From The Chat

- The first Viserio attempt used a legacy `playerSpells` / `playerNotes` structure and failed import validation.
- The corrected import nested assignments under each actor.
- The final patch added real spell rows for `Convoke the Spirits`, `Avenging Wrath`, and `Dream Flight`.
- Dream Flight was not present in the provided Viserio export, so its spell metadata was manually supplied.
- Mass Dispel, Rallying Cry, and Healthstone were represented as notes where exact exported spell metadata was not available.
