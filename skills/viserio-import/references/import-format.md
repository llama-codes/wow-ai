# Viserio Assignment Import Format

## Required Shape

Viserio assignment import expects a top-level object:

```json
{
  "actors": [],
  "phases": [],
  "customGridRows": []
}
```

`actors` is required and must be an array. `phases` and `customGridRows` should be preserved from an export when available.

Do not provide only `playerSpells` or `playerNotes`; that is an internal/planner shape and can produce: `Parsed data is not the expected object format ({ actors: [...] })`.

## Actor Shape

```json
{
  "name": "Bobbidyboo",
  "realm": "Azjol-Nerub",
  "playerClass": "Druid",
  "playerSpec": "Restoration",
  "spells": [],
  "notes": []
}
```

Keep all roster actors from an export unless the user asks for a minimal import.

## Spell Assignment Shape

```json
{
  "spell": {
    "spellId": 740,
    "spellName": "Tranquility",
    "wowheadLink": "https://www.wowhead.com/spell=740/tranquility",
    "iconLink": "/viserio-cooldowns/images/druid/740.jpg",
    "note": {},
    "checks": {},
    "cooldown": 180,
    "duration": 6,
    "playerSpellType": "Heal CD",
    "guid": "7ea56e43-5557-4785-9ce5-c5b2d6dfd0b8"
  },
  "startTime": 21,
  "actorId": "bobbidyboo-azjolnerub",
  "CustomCooldownSingleCast": null,
  "customCooldownAllCasts": null,
  "customDurationSingleCast": null,
  "customDurationAllCasts": null,
  "customChargesAllCasts": null,
  "charges": null,
  "phaseNumber": 0,
  "phaseOffset": 21
}
```

`startTime` and `phaseOffset` are seconds from pull or phase start. Do not use milliseconds.

## Note Shape

```json
{
  "actor": "Everyone",
  "startTime": 147,
  "noteText": "Hard focus Tyr's Wrath absorbs; clear before 2:45",
  "icon": "",
  "phaseNumber": 0,
  "phaseOffset": 147
}
```

Use notes for callouts, mechanics, or spells whose metadata is not available and the user accepts a text reminder.

## Common Spell Metadata

Prefer copying spell metadata from the user's export. Use these only when the export lacks the spell and the user wants a real spell row.

### Druid

```json
{
  "spellId": 740,
  "spellName": "Tranquility",
  "wowheadLink": "https://www.wowhead.com/spell=740/tranquility",
  "iconLink": "/viserio-cooldowns/images/druid/740.jpg",
  "note": {},
  "checks": {},
  "cooldown": 180,
  "duration": 6,
  "playerSpellType": "Heal CD",
  "guid": "7ea56e43-5557-4785-9ce5-c5b2d6dfd0b8"
}
```

```json
{
  "spellId": 391528,
  "spellName": "Convoke the Spirits",
  "wowheadLink": "https://www.wowhead.com/spell=391528",
  "iconLink": "/viserio-cooldowns/images/druid/391528.jpg",
  "note": {},
  "checks": {},
  "cooldown": 60,
  "duration": 10,
  "playerSpellType": "Heal CD",
  "guid": "06d3eec0-0414-49d0-b774-39b5329a850e"
}
```

### Priest

```json
{
  "spellId": 64843,
  "spellName": "Divine Hymn",
  "wowheadLink": "https://www.wowhead.com/beta/spell=64843/divine-hymn",
  "iconLink": "/viserio-cooldowns/images/priest/64843.jpg",
  "note": {},
  "checks": {},
  "cooldown": 120,
  "duration": 19,
  "playerSpellType": "Heal CD",
  "guid": "bdb96a7c-1e41-4049-a260-c03cb9fa1a96"
}
```

```json
{
  "spellId": 200183,
  "spellName": "Apotheosis",
  "wowheadLink": "https://www.wowhead.com/beta/spell=200183/apotheosis",
  "iconLink": "/viserio-cooldowns/images/priest/200183.jpg",
  "note": {},
  "checks": {},
  "cooldown": 120,
  "duration": 30,
  "playerSpellType": "Heal CD",
  "guid": "ed87014e-e052-4c3d-b4d5-cffd3f850b07"
}
```

Mass Dispel can be represented as a note unless the export contains a Viserio spell row for it.

### Evoker

```json
{
  "spellId": 363534,
  "spellName": "Rewind",
  "wowheadLink": "https://www.wowhead.com/beta/spell=363534/rewind",
  "iconLink": "/viserio-cooldowns/images/evoker/363534.jpg",
  "note": {},
  "checks": {},
  "cooldown": 180,
  "duration": 5,
  "playerSpellType": "Heal CD",
  "guid": "3757fabb-b87d-47c8-bd65-f32bf8d256c7"
}
```

```json
{
  "spellId": 370537,
  "spellName": "Stasis",
  "wowheadLink": "https://www.wowhead.com/beta/spell=370537/stasis",
  "iconLink": "/viserio-cooldowns/images/evoker/370537.jpg",
  "note": {},
  "checks": {},
  "cooldown": 90,
  "duration": 30,
  "playerSpellType": "Minor Heal CD",
  "guid": "5476581d-731e-4eda-a4ed-a402ee89167e"
}
```

```json
{
  "spellId": 370564,
  "spellName": "Stasis pop",
  "wowheadLink": "https://www.wowhead.com/beta/spell=370564/stasis",
  "iconLink": "/viserio-cooldowns/images/evoker/370537.jpg",
  "note": {},
  "checks": {},
  "cooldown": 0,
  "duration": 0,
  "playerSpellType": "Minor Heal CD",
  "guid": "d4c22a8c-92c8-4fe0-a978-0130717bf704"
}
```

The Stasis and Stasis pop GUIDs above came from a working Viserio export. Preserve them when making real spell rows.

```json
{
  "spellId": 370553,
  "spellName": "Tip the Scales",
  "wowheadLink": "https://www.wowhead.com/spell=370553/tip-the-scales",
  "iconLink": "/viserio-cooldowns/images/evoker/370553.jpg",
  "note": {},
  "checks": {},
  "cooldown": 120,
  "duration": 0,
  "playerSpellType": "DPS CD",
  "guid": "43f50e94-d34b-4e60-8907-9398eca92a13"
}
```

When adding Tip the Scales from the manual current-usage export, preserve the row-level `talentModifiers` for `Chronoboon` if present.

```json
{
  "spellId": 1260459,
  "spellName": "Vaelgor's Final Stare",
  "wowheadLink": "https://www.wowhead.com/spell=1260459/vaelgors-final-stare",
  "iconLink": "/viserio-cooldowns/images/trinkets/1260459.jpg",
  "note": {},
  "checks": {},
  "cooldown": 90,
  "duration": 15,
  "playerSpellType": "Trinkets",
  "guid": "vaelgors-final-stare-healer"
}
```

```json
{
  "spellId": 359816,
  "spellName": "Dream Flight",
  "wowheadLink": "https://www.wowhead.com/spell=359816/dream-flight",
  "iconLink": "/viserio-cooldowns/images/evoker/359816.jpg",
  "note": {},
  "checks": {},
  "cooldown": 120,
  "duration": 10,
  "playerSpellType": "Heal CD",
  "guid": "dream-flight-healer"
}
```

The Dream Flight GUID above is a manual placeholder from local usage; replace it with an exported Viserio GUID if one is available.

### Paladin

```json
{
  "spellId": 31821,
  "spellName": "Aura Mastery",
  "wowheadLink": "https://www.wowhead.com/spell=31821/aura-mastery",
  "iconLink": "/viserio-cooldowns/images/paladin/31821.jpg",
  "note": {},
  "checks": {},
  "cooldown": 180,
  "duration": 8,
  "playerSpellType": "Raid DR",
  "guid": "1dc41677-01d1-4ac7-a9ca-ef005f7a96d5"
}
```

```json
{
  "spellId": 31884,
  "spellName": "Avenging Wrath",
  "wowheadLink": "https://www.wowhead.com/spell=31884/avenging-wrath",
  "iconLink": "/viserio-cooldowns/images/paladin/31884.jpg",
  "note": {},
  "checks": {},
  "cooldown": 120,
  "duration": 30,
  "playerSpellType": "Heal CD",
  "guid": "fc0d6ab6-fba4-4f3c-add2-f4f37fb4dd6b"
}
```

### Monk

```json
{
  "spellId": 115310,
  "spellName": "Revival",
  "wowheadLink": "https://www.wowhead.com/spell=115310/revival",
  "iconLink": "/viserio-cooldowns/images/monk/115310.jpg",
  "note": {},
  "checks": {},
  "cooldown": 180,
  "duration": 0,
  "playerSpellType": "Heal CD",
  "guid": "8afbc98e-8857-4d23-9f27-1afc68fad84d"
}
```

```json
{
  "spellId": 322118,
  "spellName": "Invoke Yu'lon, the Jade Serpent",
  "wowheadLink": "https://www.wowhead.com/spell=322118/invoke-yulon-the-jade-serpent",
  "iconLink": "/viserio-cooldowns/images/monk/322118.jpg",
  "note": {},
  "checks": {},
  "cooldown": 120,
  "duration": 12,
  "playerSpellType": "Heal CD",
  "guid": "20639b47-c5da-492c-aed6-a4cfbe761f11"
}
```

```json
{
  "spellId": 443028,
  "spellName": "Celestial Conduit",
  "wowheadLink": "https://www.wowhead.com/beta/spell=443028/celestial-conduit?spellModifier=137024",
  "iconLink": "/viserio-cooldowns/images/monk/443028.jpg",
  "note": {},
  "checks": {},
  "cooldown": 90,
  "duration": 4,
  "playerSpellType": "Heal CD",
  "guid": "46aaa4a2-831f-44c2-b369-564efa7d3bb7"
}
```

The Celestial Conduit GUID above came from the manual current-usage export. Preserve it when making real spell rows.

### Warrior

```json
{
  "spellId": 97462,
  "spellName": "Rallying Cry",
  "wowheadLink": "https://www.wowhead.com/spell=97462/rallying-cry",
  "iconLink": "/viserio-cooldowns/images/warrior/97462.jpg",
  "note": {},
  "checks": {},
  "cooldown": 180,
  "duration": 10,
  "playerSpellType": "Raid DR",
  "guid": "cf93a6a0-9835-419c-8db8-a367fd5338e8",
  "talentModifiers": [
    {
      "spell": {
        "spellId": 424742,
        "spellName": "Battlefield Commander",
        "wowheadLink": "https://www.wowhead.com/spell=424742",
        "iconLink": ""
      },
      "modifiedValues": {
        "cooldown": 165
      }
    }
  ]
}
```

The Rallying Cry GUID and Battlefield Commander modifier above came from a working Viserio assignment export. Preserve them when making real spell rows.

### Everyone

```json
{
  "spellId": 431416,
  "spellName": "Personals",
  "wowheadLink": "",
  "iconLink": "/viserio-cooldowns/images/everyone/134952.jpg",
  "note": {},
  "checks": {},
  "cooldown": 60,
  "duration": 0,
  "playerSpellType": "Defensives",
  "guid": "667be180-5263-42e7-b8ab-84a95996b3ff"
}
```

Healthstone should use exported spell metadata when available; otherwise use notes or ask for a Viserio export containing it.
