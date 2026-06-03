# Crown of the Cosmos - MW/RDruid/Pres/Holy Healing Plan

## Goal

Build a first-pass 4-healer assignment for:

| Slot | Spec | Main value |
| --- | --- | --- |
| Healer 1 | Mistweaver Monk | Restoral/Revival reset, Yu'lon ramps, Celestial Conduit, Life Cocoon spot saves |
| Healer 2 | Restoration Druid | Tranquility anchors, Convoke throughput every major cycle |
| Healer 3 | Preservation Evoker | Rewind, Tip the Scales setups, Zephyr, spot rescue |
| Healer 4 | Holy Priest | Divine Hymn anchors, Apotheosis burst healing, Guardian Spirit spot saves |

No sampled kill has this exact four-healer setup, so this plan compares the closest logs and maps missing healer slots into our tools. The priority for this pass is avoiding dead cooldown time: if a major CD can be used and still come back for the next lethal window, we press it.

## Source Logs

| Ref | Report | Healer comp | Why it matters |
| --- | --- | --- | --- |
| R01 | https://www.warcraftlogs.com/reports/Q1N3nyHFLDPKvpX7?fight=17&type=healing | RSham / RDruid / Pres / Holy | Only sampled log with Holy Priest, RDruid, and Pres together. Missing MW. |
| R02 | https://www.warcraftlogs.com/reports/MTh9DtBp6y3wPajn?fight=103&type=healing | MW / RDruid / RSham / Pres | Has MW, RDruid, Pres. Missing Holy Priest. |
| R03 | https://www.warcraftlogs.com/reports/HmaTLwKV7Aqx81CF?fight=43&type=healing | RDruid / Pres / Disc / MW | Very close to our comp, one death. Use for late-fight Rewind/Restoral shape. |
| R04 | https://www.warcraftlogs.com/reports/tJC1QWjGvLfwA7mc?fight=23&type=healing | RDruid / MW / HPal / Pres | Has MW, RDruid, Pres and strong external comparison. |
| R05 | https://www.warcraftlogs.com/reports/KLR8ta3myrAgvkDX?fight=55&type=healing | Pres / RDruid / Disc / MW | Very close to our comp, one death. Best template for final 90 seconds. |

## Timing Rules

| Rule | Practical call |
| --- | --- |
| Spend early if it still returns. | Opener CDs are good because they return before the real 04:20+ danger phase. |
| Do not spend a reset into 03:20 unless we are actually dying there. | The repeated lethal windows start at 04:20. Holding MW reset from 03:30 to 04:50 is better value. |
| Squeeze 3 Rewinds if our Pres build/timers allow it. | Target Rewind at 00:30, 04:20, and 07:50. If Rewind is not back by 07:50 after the 04:20 use, skip 04:20 and hold it for final. |
| Stagger channels through the 06:30-06:55 section. | RDruid Tranq first, Holy Hymn second, Zephyr during the damage overlap. |
| Treat 08:10+ as a kill-time problem. | If our kill is longer than 08:20, we need to shift one late CD later instead of spending everything by 07:50. |

## Comparative Read

| Pattern | Evidence | What we copy |
| --- | --- | --- |
| RDruid Tranquility is a fixed 3-use anchor. | Logs commonly use Tranq around 00:10-00:14, 03:18-03:36, and 06:37-06:55. | Use Tranq at 00:12, 03:30, 06:40. These are not flexible unless timers drift. |
| RDruid Convoke should almost never sit unused. | Convoke appears around 00:03-00:06, 01:04-01:13, 02:16-02:25, 03:17-03:33, 04:19-04:27, 05:17-05:31, 06:15-06:32, 07:17-07:36, and 08:20+. | Press Convoke roughly every minute, shifted a few seconds onto listed damage windows. |
| Pres Rewind can be squeezed instead of hard-held. | R01 gets Rewind at 00:31, 04:01, and 07:45. Other close logs often hold for late, but they also have Disc/HPal/RSham coverage we do not. | Try Rewind 00:30, 04:20, 07:50. If the 04:20 use blocks the 07:50 use, remove the 04:20 Rewind. |
| MW reset is best on opener, Simulacrum, final. | MW reset appears at 00:27-00:28, 03:29-04:46, and 07:01-08:05 depending comp. | Use Restoral/Revival at 00:27, 04:50, 07:50. We intentionally do not spend it at 03:29 unless 03:20 is our wipe point. |
| Holy Priest cadence follows R01 cleanly. | R01 Holy uses Apotheosis at 00:08, 02:58, 05:07, 07:08 and Divine Hymn at 01:46, 04:44, 06:45. | Copy that timing. Hymn at 01:46 is a free extra if it does not delay 04:44. |

## Boss Damage Map

| Window | Seen in logs | Repeated boss abilities | Risk read |
| --- | --- | --- | --- |
| 00:20-00:30 | R04, R05 | Echoing Darkness, Void Expulsion | Opener burst; spend early CDs because they return. |
| 01:00-01:10 | R03, R05 | Echoing Darkness, Void Expulsion, Grasp of Emptiness | Medium-high sustain check; cover with Convoke and rolling throughput. |
| 04:00-04:10 | R01 | Simulacrum Backlash, Voidstalker Sting, Bursting Emptiness | Fast-timer warning. If our timers match R01, start the 04:20 package earlier. |
| 04:20-04:30 | R01, R03, R04, R05 | Simulacrum Backlash, Void Expulsion, Voidstalker Sting | First consistent lethal Simulacrum window. |
| 04:50-05:20 | R01, R02, R03, R05 | Simulacrum Backlash, Voidstalker Sting, Void Expulsion, Void Barrage | Back-to-back Simulacrum pressure. Needs rolling coverage, not one stacked button. |
| 05:40-06:00 | R02, R03 | Simulacrum Backlash, Gravity Collapse, Cosmic Barrier, Voidstalker Sting | Transition into late Gravity/Cosmic pattern. |
| 06:20-06:55 | R01, R03, R04, R05 | Gravity Collapse, Cosmic Barrier, Voidstalker Sting, Void Expulsion | Major danger sequence. Several logs chain multiple raid CDs here. |
| 07:10-07:30 | R01, R02, R04 | Gravity Collapse, Void Expulsion, Voidstalker Sting, Cosmic Barrier | Late sustain plus movement/positioning deaths. |
| 07:30-08:00 | R01, R03, R04, R05 | Gravity Collapse, Cosmic Barrier, Voidstalker Sting | Final lethal overlap in the closest one-death logs. |
| 08:10-08:20 | R02, R04 | Gravity Collapse, Void Expulsion, Voidstalker Sting | Long-kill danger. Needs a plan only if our kill timer reaches it. |

## Optimized Assignment Timeline

| Time | Active coverage | Boss ability covered | Assignment | Why this timing |
| --- | --- | --- | --- | --- |
| 00:08 | 00:08-00:25 | Opener into Echoing Darkness / Void Expulsion | Holy Priest Apotheosis. RDruid starts opener ramp. | R01 uses Apotheosis 00:08; this comes back for 02:58/05:07/07:08. |
| 00:12 | 00:12-00:24 | Opener Echoing Darkness ramp | RDruid Tranquility. | Close logs use Tranq 00:10-00:14; using it here still gives 03:30 and 06:40. |
| 00:20 | 00:20-00:30 | Echoing Darkness + Void Expulsion | Pres Tip the Scales setup into empowered healing. | Aligns with the first proven 00:20-00:30 spike. |
| 00:27 | 00:27 instant reset | Echoing Darkness + Void Expulsion | MW Restoral/Revival. | This is a free early use if we save the next for 04:50. |
| 00:30 | 00:30 recovery | Opener recovery | Pres Rewind. | Logs consistently use early Rewind around 00:30; try to make this use 1 of 3. |
| 00:40 | 00:40-01:00 | Opener recovery into first sustain | MW Yu'lon. | Close MW logs start Yu'lon around 00:37-00:41. |
| 01:05 | 01:05-01:15 | Echoing Darkness + Void Expulsion | RDruid Convoke. | Covers the 01:00-01:10 window without spending a longer CD. |
| 01:45 | 01:45-01:55 | Residual Echoing Darkness / Grasp of Emptiness | Holy Priest Divine Hymn if raid is taking damage; MW Celestial Conduit if Hymn is held. | This is a free Hymn use if it does not delay 04:44. |
| 02:15 | 02:15-02:25 | Low/mid damage setup | RDruid Convoke. | Press to avoid sitting on Convoke; it returns for 03:20/04:20. |
| 02:58 | 02:58-03:15 | Setup before Simulacrum pattern | Holy Priest Apotheosis. | Matches R01 and comes back for 05:07. |
| 03:05 | 03:05-03:25 | Simulacrum setup / rolling pressure | MW Yu'lon. | Matches R03/R05. This is enough unless 03:20 is specifically killing us. |
| 03:30 | 03:30-03:42 | Simulacrum setup / timer drift safety | RDruid Tranquility + Convoke around 03:20-03:30. | Copies close logs. Do not add MW reset here by default. |
| 03:55 | 03:55-04:10 | Fast-timer Simulacrum Backlash safety | MW Celestial Conduit. | R01 has a 04:00 spike; this covers fast timers without blocking 05:50. |
| 04:20 | 04:20-04:30 | Simulacrum Backlash + Void Expulsion + Voidstalker Sting | Pres Rewind + RDruid Convoke + Pres Tip the Scales. | First consistent lethal window. This is where we squeeze the middle Rewind if it still returns for 07:50. |
| 04:44 | 04:44-04:55 | Simulacrum Backlash / Voidstalker Sting continuation | Holy Priest Divine Hymn. | Direct copy from R01; catches the 04:50 spike start. |
| 04:50 | 04:50 instant reset | Simulacrum Backlash + Voidstalker Sting + Void Barrage | MW Restoral/Revival. | Better than spending MW reset at 03:29 because 04:50 is repeated in four logs. |
| 05:07 | 05:07-05:25 | Simulacrum Backlash + Void Expulsion + Voidstalker Sting | Holy Priest Apotheosis + MW Yu'lon + RDruid Convoke around 05:17. | R01 uses Apotheosis 05:07; MW logs use Yu'lon 05:09-05:22. |
| 05:50 | 05:50-06:00 | Gravity Collapse + Cosmic Barrier transition | MW Celestial Conduit + Pres Tip the Scales. | R02/R03 show 05:40-06:00 danger; Conduit logs land around 05:46-05:49. |
| 06:20 | 06:20-06:35 | Gravity Collapse + Void Expulsion | RDruid Convoke. | Catches R01 06:20-06:30 and rolls into the larger 06:30+ section. |
| 06:40 | 06:40-06:48 | Gravity Collapse + Cosmic Barrier + Voidstalker Sting | RDruid Tranquility. | Main healer channel for the 06:40 damage overlap. |
| 06:48 | 06:48-06:56 | Cosmic Barrier / Gravity continuation | Pres Zephyr + Holy Priest Divine Hymn. | Staggers after Tranq instead of stacking everything on the first tick. |
| 07:08 | 07:08-07:25 | Gravity Collapse + Void Expulsion + Voidstalker Sting | Holy Priest Apotheosis + MW Yu'lon. | R01 Holy timing plus close MW late Yu'lon timing. |
| 07:24 | 07:24-07:35 | Gravity Collapse / Cosmic Barrier buildup | RDruid Convoke + Pres Tip the Scales. | Covers R01/R02/R04 07:10-07:30 windows and prepares for final. |
| 07:50 | 07:50 reset burst | Gravity Collapse + Cosmic Barrier + Voidstalker Sting | Pres Rewind + MW Restoral/Revival. Add any remaining DPS raid DR here. | R03/R05 hold Rewind to 07:50 and R04/R05 spend MW reset late. This is the final lethal overlap. |
| 08:10 | 08:10-08:20 contingency | Long-kill Gravity Collapse / Void Expulsion | If we reach this, use remaining DPS raid DR and spot externals. Shift either MW reset or Pres Rewind later on future pulls if this becomes the wipe point. | R02/R04 show this as dangerous, but the 07:50 window is too lethal to ignore blindly. |

## Per-Healer CD Cadence

| Healer | Optimized cadence | Notes |
| --- | --- | --- |
| Mistweaver Monk | Restoral/Revival 00:27, 04:50, 07:50. Yu'lon 00:40, 03:05, 05:10, 07:10. Celestial Conduit 01:45, 03:55, 05:50, 07:20 if available. | Do not burn reset at 03:29 unless 03:20 is our actual wipe point. Use Life Cocoon on Simulacrum Backlash targets or late Gravity Collapse targets. |
| Restoration Druid | Tranquility 00:12, 03:30, 06:40. Convoke 00:05, 01:05, 02:15, 03:20, 04:20, 05:17, 06:20, 07:24, 08:20 if long. | Convoke is the anti-dead-time button. Shift it a few seconds to land inside damage windows, but do not sit on it for long. |
| Preservation Evoker | Rewind 00:30, 04:20, 07:50 if possible. Tip the Scales 00:20, 04:20, 05:50, 07:24. Zephyr 06:48. | If Rewind cannot return by 07:50 after the 04:20 use, remove the 04:20 Rewind and use extra healer throughput there instead. |
| Holy Priest | Apotheosis 00:08, 02:58, 05:07, 07:08. Divine Hymn 01:45 if useful, 04:44, 06:48. Guardian Spirit as assigned spot save. | The 01:45 Hymn should be used only if it does not delay the 04:44 Hymn. Guardian Spirit should go on marked players during Simulacrum Backlash or late Gravity Collapse. |

## Swap Rules

| Problem on pull | Change |
| --- | --- |
| We die at 03:20-03:35. | Move MW Restoral/Revival from 04:50 to 03:29, then use the next reset at 07:25-07:50 depending deaths. |
| Rewind is not ready for 07:50 after using it at 04:20. | Stop using Rewind at 04:20. Cover 04:20 with RDruid Convoke + Pres Tip + Holy spot throughput, then keep Rewind for 07:50. |
| We die at 06:40 before Hymn lands. | Move Holy Hymn to 06:40 and Pres Zephyr to 06:38, then let RDruid Tranq carry the back half. |
| We consistently reach 08:10+. | Delay one of the 07:50 resets to 08:05-08:10 on future pulls, but only after confirming 07:50 is survivable without it. |

## Open Questions For Next Pass

| Question | Why it matters |
| --- | --- |
| Do we have Darkness, AMZ, Rallying Cry, non-healer Zephyr, or Vampiric Embrace? | Several source kills rely on DPS/raid DR during 05:47-06:50 and 07:45-08:00. |
| Is our Mistweaver using Restoral or Revival? | The assignment should use the exact in-game button. |
| Is Pres Rewind available at 07:50 after a 04:20 use in our build? | This decides whether the optimized 3-Rewind plan is real or whether 04:20 needs a different CD. |
| What is our expected kill time? | If we are closer to 08:50, 08:10 becomes a real coverage point instead of contingency. |
