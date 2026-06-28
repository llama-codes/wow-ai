# Belo'ren Loogs #1 Holy Paladin Notes

Source: Loogs #1 Holy Paladin cooldown usage export for NSRT.

Encounter:

- Encounter ID: `3182`
- Difficulty: Mythic
- Name: `Belo'ren, Child of Al'ar`

Spell map:

| Spell ID | Spell |
| --- | --- |
| `31884` | Avenging Wrath |
| `375576` | Divine Toll |
| `31821` | Aura Mastery |

Divine Toll cadence note: this log is consistent with the Holy Paladin taking `Quickened Invocation`, which lowers Divine Toll into a roughly 30-second rotational cooldown. The casts are therefore real repeated Divine Toll windows, not separate assigned raid cooldowns.

## Timeline

| Time | Spell |
| --- | --- |
| `00:01.0` | Avenging Wrath |
| `00:01.7` | Divine Toll |
| `00:32.9` | Divine Toll |
| `01:09.6` | Divine Toll |
| `01:40.1` | Divine Toll |
| `02:02.5` | Avenging Wrath |
| `02:16.3` | Divine Toll |
| `02:28.2` | Aura Mastery |
| `02:47.2` | Divine Toll |
| `03:19.5` | Divine Toll |
| `03:50.7` | Divine Toll |
| `04:03.1` | Avenging Wrath |
| `04:24.8` | Divine Toll |
| `04:56.1` | Divine Toll |

Planning read: this follows the common Paladin pattern from the similar-comp notes: Wings plus Divine Toll on pull, second Wings around `02:03`, Aura Mastery in the mid-fight window, then late Wings and Divine Toll repeats. Treat Divine Toll as rotational throughput context unless we intentionally want it called.

## Raw NSRT Export

```text
EncounterID:3182;Difficulty:Mythic;Name:Belo'ren, Child of Al'ar;
ph:1;time:1.0;spellid:31884;
ph:1;time:1.7;spellid:375576;
ph:1;time:32.9;spellid:375576;
ph:1;time:69.6;spellid:375576;
ph:1;time:100.1;spellid:375576;
ph:1;time:122.5;spellid:31884;
ph:1;time:136.3;spellid:375576;
ph:1;time:148.2;spellid:31821;
ph:1;time:167.2;spellid:375576;
ph:1;time:199.5;spellid:375576;
ph:1;time:230.7;spellid:375576;
ph:1;time:243.1;spellid:31884;
ph:1;time:264.8;spellid:375576;
ph:1;time:296.1;spellid:375576;
```
