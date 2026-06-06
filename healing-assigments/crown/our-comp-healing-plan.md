# Crown of the Cosmos - MW/RDruid/Pres/Holy Healing Plan

## Goal

Build a 4-healer assignment for:

| Slot | Spec | Main value |
| --- | --- | --- |
| Healer 1 | Mistweaver Monk | Restoral/Revival reset, Yu'lon ramps, Celestial Conduit if talented, Life Cocoon spot saves |
| Healer 2 | Restoration Druid | Tranquility anchors, Convoke throughput every major cycle |
| Healer 3 | Preservation Evoker | Rewind, Stasis setup/release, Tip the Scales setups, Zephyr, spot rescue |
| Healer 4 | Holy Priest | Divine Hymn anchors, Apotheosis burst healing, Guardian Spirit spot saves |

R06 is now an exact healer-comp kill, so it is the primary timing reference for healer cadence. It was also a long 08:59 kill with 11 deaths, mostly after 08:00, so we copy its proven timings while correcting the late reset plan instead of blindly copying every cast.

If Bobbidyboo is unavailable and Regidør replaces the Restoration Druid, use `regidor-paladin-healing-plan.md` instead of trying to swap Paladin buttons into this timeline one-for-one.

## Source Logs

| Ref | Report | Healer comp | Why it matters |
| --- | --- | --- | --- |
| R01 | https://www.warcraftlogs.com/reports/Q1N3nyHFLDPKvpX7?fight=17&type=healing | RSham / RDruid / Pres / Holy | Strong Holy/RDruid/Pres reference and earlier 3-Rewind example. Missing MW. |
| R02 | https://www.warcraftlogs.com/reports/MTh9DtBp6y3wPajn?fight=103&type=healing | MW / RDruid / RSham / Pres | Has MW, RDruid, Pres. Useful for long-kill late danger. Missing Holy Priest. |
| R03 | https://www.warcraftlogs.com/reports/HmaTLwKV7Aqx81CF?fight=43&type=healing | RDruid / Pres / Disc / MW | Very close to our comp, one death. Useful for final Rewind/Restoral shape. |
| R04 | https://www.warcraftlogs.com/reports/tJC1QWjGvLfwA7mc?fight=23&type=healing | RDruid / MW / HPal / Pres | Has MW, RDruid, Pres and strong external comparison. |
| R05 | https://www.warcraftlogs.com/reports/KLR8ta3myrAgvkDX?fight=55&type=healing | Pres / RDruid / Disc / MW | Very close to our comp, one death. Best non-Holy template for final 90 seconds. |
| R06 | https://www.warcraftlogs.com/reports/cNrQwb2gMnk6zKmq?fight=42&type=healing | RDruid / Holy / Pres / MW | Exact healer comp. Primary source for cadence, and proof that 06:00 and 08:00+ are real danger points. |

## Timing Rules

| Rule | Practical call |
| --- | --- |
| Exact comp wins for cadence. | Use R06 for default RDruid, Holy Priest, MW, and Pres timing unless our own pulls show a different wipe point. |
| Spend early if it still returns. | Opener CDs are good because they return before the real 03:55+ chain. |
| Default MW reset cadence is opener, early Simulacrum, 07:00. | Use Revival/Restoral around 00:29, 03:55, and 07:05. Do not leave the 07:00 section empty. |
| Default Rewind cadence is the exact-comp 2-use plan. | Use Rewind around 01:10 and 06:04. Only swap to 00:30 / 04:20 / 07:55 if Deviiarrc confirms the 3-use cadence is legal and 06:00 is covered by other raid DR. |
| 06:00 and 08:00 need external planning. | R06 used Rally/AMZ around 06:00 and stacked Darkness/AMZ/Zephyr around 07:00-07:40. If we lack those, healer CDs must move there. |
| Treat 08:00+ as a real long-kill phase. | If our kill reaches 08:00+, use the 07:19 Conduit, 07:50 Stasis setup, 08:00 Stasis pop, and late Hymn/Apotheosis plus spot saves. |

## Comparative Read

| Pattern | Evidence | What we copy |
| --- | --- | --- |
| RDruid Tranquility is still a 3-use anchor. | R06 uses Tranq at 00:13, 03:14, and 06:40; close logs cluster around the same spots. | Shift Tranq to 00:57, 04:20, 07:36 so the Bobbidyboo package covers the same damage windows as Regidør Aura Mastery. |
| RDruid Convoke should follow exact-comp minute cadence. | R06 uses Convoke at 00:05, 01:06, 02:09, 03:09, 04:10, 05:13, 06:13, 07:15, 08:16. | Press Convoke near those times, shifting only a few seconds for timers. |
| Holy Priest timing should move earlier. | R06 uses Hymn at 00:45, 03:29, 06:38, 08:41 and Apotheosis at 00:10, 02:22, 04:47, 06:53, 08:55. | Replace the old R01-only 01:45/04:44 Hymn plan with the R06 cadence. |
| MW reset should cover 03:55 and the 07:00 chain. | R06 uses Restoral at 00:29, 03:55, 07:05; deaths then start at 08:01. | Copy the reset cadence, then cover the 08:00 wall with Conduit, Stasis release, and external DR. |
| Pres Rewind has two realistic modes. | R06 proves 01:10 and 06:04 for exact comp. R01 proves a more aggressive 00:31, 04:01, 07:45 style with different support. | Default to 01:10/06:04. Keep the 3-Rewind mode as a confirmed-build swap, not the baseline. |
| Pres Stasis should be visible in Viserio. | Existing Viserio exports already contain Stasis and Stasis pop metadata. | Keep a steady setup/release cadence so there are no giant empty gaps. |
| Monk Conduit should be a real cadence. | R04's Monk used Celestial Conduit at 00:06, 01:38, 03:24, 05:46, 07:19. | Use that cadence when Santatumblr is playing Conduit; do not bundle only two casts onto Yu'lon/Revival. |
| Late raid DR matters as much as healer buttons. | R06 used AMZ/Rally at 05:20-06:01, then Darkness/AMZ/Zephyr/AMZ at 07:01-07:38. | Assign our real raid DR before considering the plan final. |

## Boss Damage Map

| Window | Seen in logs | Repeated boss abilities | Risk read |
| --- | --- | --- | --- |
| 00:20-00:30 | R04, R05 | Echoing Darkness, Void Expulsion | Opener burst; spend early CDs because they return. |
| 01:00-01:10 | R03, R05 | Echoing Darkness, Void Expulsion, Grasp of Emptiness | Medium-high sustain check; R06 answers this with Rewind at 01:10. |
| 04:20-04:30 | R01, R03, R04, R05, R06 | Simulacrum Backlash, Void Expulsion, Voidstalker Sting | First consistent Simulacrum danger point. Cover with Convoke plus rolling CDs unless we choose 3-Rewind mode. |
| 05:10-05:20 | R01, R02, R03, R05, R06 | Simulacrum Backlash, Voidstalker Sting, Void Expulsion, Void Barrage | Back-to-back Simulacrum pressure. Needs rolling coverage, not one stacked button. |
| 06:00-06:10 | R06 | Gravity Collapse, Cosmic Barrier, Voidstalker Sting | Exact-comp danger spike. Needs Rewind plus raid DR or equivalent. |
| 06:40-06:50 | R01, R03, R04, R05, R06 | Gravity Collapse, Cosmic Barrier, Voidstalker Sting, Void Expulsion | Major danger sequence. Use Holy Hymn, Pres Stasis pop, and raid DR here while holding the fourth-healer DR/channel for 07:36. |
| 07:00-07:20 | R01, R02, R04, R06 | Gravity Collapse, Void Expulsion, Voidstalker Sting, Cosmic Barrier | Late sustain plus movement/positioning deaths. Needs raid DR if MW reset is held. |
| 07:40-07:50 | R03, R04, R05, R06 | Gravity Collapse, Cosmic Barrier, Voidstalker Sting | Pre-final overlap. Use Tip, Zephyr/AMZ/Darkness, and prepare final reset. |
| 08:00-08:10 | R06 | Cosmic Barrier, Voidstalker Sting, Gravity Collapse, Grasp of Emptiness | R06 death wall. Use the final Conduit/Stasis/external package here on long pulls. |
| 08:40-09:00 | R06 | Voidstalker Sting, Dark Hand, boss finish pressure | Only relevant if we are still fighting after 08:40; use late Hymn/Apotheosis and spot saves. |

## Optimized Assignment Timeline

| Time | Active coverage | Boss ability covered | Assignment | Why this timing |
| --- | --- | --- | --- | --- |
| 00:05 | 00:05-00:15 | Opener ramp | RDruid Convoke. | Exact-comp opener cadence. |
| 00:06 | 00:06-00:10 | Opener ramp | MW Celestial Conduit. | R04 Monk cadence; adds an early Conduit instead of leaving it unused. |
| 00:10 | 00:10-00:25 | Opener into Echoing Darkness / Void Expulsion | Holy Priest Apotheosis. | R06 uses 00:10 and it returns for 02:22/04:47. |
| 00:20 | 00:20-00:30 | Echoing Darkness + Void Expulsion | Pres Stasis + Tip the Scales setup into empowered healing. | Keeps opener stable without committing Rewind too early. |
| 00:29 | 00:29 instant reset | Echoing Darkness + Void Expulsion recovery | MW Restoral/Revival. | Exact-comp first reset. |
| 00:30 | 00:30 release | Echoing Darkness + Void Expulsion recovery | Pres Stasis pop. | Makes the opener Stasis release visible. |
| 00:37 | 00:37-01:00 | Opener recovery into sustain | MW Yu'lon. | Exact-comp first Yu'lon. |
| 00:45 | 00:45-00:55 | Opener tail / first sustain | Holy Priest Divine Hymn. | R06 uses early Hymn and gets it back for 03:29. |
| 00:57 | 00:57-01:05 | Echoing Darkness + Void Expulsion follow-up | RDruid Tranquility. | Shifted to match the Regidør Aura damage-window swap. |
| 01:05 | 01:05-01:15 | Echoing Darkness + Void Expulsion | RDruid Convoke. | Matches R06 01:06. |
| 01:10 | 01:10 recovery | Echoing Darkness / Grasp recovery | Pres Rewind. | Default exact-comp first Rewind. |
| 01:31 | 01:31 setup | Mid-cycle damage | Pres Tip the Scales. | Matches R06 Tip cadence. |
| 01:38 | 01:38-01:42 | Mid-cycle sustain | MW Celestial Conduit. | R04 Monk Conduit cadence. |
| 01:50 | 01:50 setup | Rolling cadence | Pres Stasis. | Keeps Stasis rolling after opener instead of waiting until 04:00. |
| 02:10 | 02:10-02:20 | Low/mid damage setup | RDruid Convoke. | Avoids sitting on Convoke. |
| 02:10 | 02:10 release | Rolling cadence | Pres Stasis pop. | Releases the second Stasis package. |
| 02:22 | 02:22-02:40 | Setup before Simulacrum pattern | Holy Priest Apotheosis. | Exact-comp second Apotheosis. |
| 03:08 | 03:08-03:25 | Simulacrum setup / rolling pressure | MW Yu'lon. | Exact-comp Yu'lon; keep Stasis for the actual 04:20 wall. |
| 03:10 | 03:10-03:20 | Simulacrum setup | RDruid Convoke. | Matches R06 03:09. |
| 03:20 | 03:20 setup | Simulacrum chain | Pres Stasis. | Third setup keeps Evoker active before the 04:00+ sequence. |
| 03:24 | 03:24-03:28 | Simulacrum setup | MW Celestial Conduit. | R04 Monk Conduit cadence. |
| 03:29 | 03:29-03:40 | Simulacrum setup continuation | Holy Priest Divine Hymn. | Exact-comp second Hymn. |
| 03:40 | 03:40 release | Simulacrum chain | Pres Stasis pop. | Releases during the Simulacrum ramp. |
| 03:55 | 03:55 instant reset | Fast-timer Simulacrum safety into 04:20 | MW Restoral/Revival. | R06 proves this stabilizes the 04:20 section without Rewind. |
| 04:10 | 04:10-04:25 | 04:20 Simulacrum window | RDruid Convoke. | Exact-comp Convoke before the first lethal Simulacrum window. |
| 04:20 | 04:20-04:32 | 04:20 Simulacrum window | RDruid Tranquility. | Shifted to match the Regidør Aura damage-window swap. |
| 04:30 | 04:30 spot save | Simulacrum target danger | MW Life Cocoon as assigned. | R06 uses Cocoon here; assign if a marked target is low. |
| 04:38 | 04:38 setup | 04:50-05:10 continuation | Pres Tip the Scales. | Exact-comp Tip timing. |
| 04:47 | 04:47-05:05 | Simulacrum continuation | Holy Priest Apotheosis. | R06 uses Apotheosis here instead of a 04:44 Hymn. |
| 04:50 | 04:50 setup | 05:10 damage window | Pres Stasis. | Sets up the 05:10 Simulacrum damage. |
| 05:10 | 05:10 release | 05:10 damage window | Pres Stasis pop. | Releases into the 05:10 damage window. |
| 05:13 | 05:13-05:25 | Simulacrum Backlash + Void Expulsion + Voidstalker Sting | RDruid Convoke. | Exact-comp coverage for the 05:10 damage window. |
| 05:20 | 05:20-05:30 | Simulacrum tail | Assign available raid DR. | R06 used Zephyr/AMZ around this point. |
| 05:46 | 05:46-05:50 | Gravity Collapse + Cosmic Barrier transition | MW Celestial Conduit. | R04 Monk Conduit cadence into the 06:00 danger spike. |
| 05:50 | 05:50-06:10 | Gravity Collapse + Cosmic Barrier transition | MW Yu'lon. | R06 moves Yu'lon here for the 06:00 danger spike. |
| 06:01 | 06:01-06:10 | Gravity Collapse + Cosmic Barrier | Rallying Cry / AMZ / equivalent raid DR. | R06 used Rally at 06:01. |
| 06:04 | 06:04 reset burst | Gravity Collapse + Cosmic Barrier | Pres Rewind + Tip the Scales. | Exact-comp second Rewind; this is the main reason not to baseline Rewind at 04:20. |
| 06:13 | 06:13-06:25 | Gravity continuation | RDruid Convoke. | Exact-comp Convoke cadence. |
| 06:20 | 06:20 setup | 06:40 overlap | Pres Stasis. | Sets up the 06:40 Gravity/Cosmic overlap. |
| 06:38 | 06:38-06:50 | Gravity Collapse + Voidstalker Sting | Holy Priest Divine Hymn. | Exact-comp third Hymn. |
| 06:40 | 06:40 release | 06:40 overlap | Pres Stasis pop. | Releases into the 06:40 overlap. |
| 06:53 | 06:53-07:10 | 07:00 sustain bridge | Holy Priest Apotheosis. | R06 uses Apotheosis immediately after the channel stack. |
| 07:05 | 07:05 instant reset | 07:00 damage chain | MW Restoral/Revival. | Removes the dead 07:00 window. |
| 07:15 | 07:15-07:25 | Gravity / Cosmic sustain | RDruid Convoke. | Exact-comp late Convoke. |
| 07:19 | 07:19-07:23 | 07:20-07:40 ramp | MW Celestial Conduit. | R04 Monk Conduit cadence. |
| 07:34 | 07:34 setup | 07:40-08:00 buildup | Pres Tip the Scales. | Keeps Tip on cadence before the final wall. |
| 07:36 | 07:36-07:48 | Late Gravity/Cosmic overlap | RDruid Tranquility. | Shifted to match the Regidør Aura late-overlap swap. |
| 07:36 | 07:36-07:50 | Late Gravity/Cosmic overlap | Zephyr / AMZ / Darkness from available raid CDs. | R06 stacked non-healer DR here. |
| 07:50 | 07:50 setup | Final wall | Pres Stasis. | Final Stasis setup. |
| 08:00 | 08:00 release | 08:00+ final wall | Pres Stasis pop. | Releases into the final wall instead of after it. |
| 08:03 | 08:03-08:20 contingency | Long-kill final sustain | MW Yu'lon if the pull is still going. | R06 used Yu'lon at 08:03 while deaths were happening. |
| 08:16 | 08:16-08:26 contingency | Long-kill Gravity / Void pressure | RDruid Convoke. | Exact-comp long-kill Convoke. |
| 08:41 | 08:41-08:53 contingency | 08:40+ finish pressure | Holy Priest Divine Hymn. | R06 used a fourth Hymn here. |
| 08:55 | 08:55-finish contingency | 08:55 finish pressure | Holy Priest Apotheosis and spot externals. | R06 used late Apotheosis; only matters on very long kills. |

## Per-Healer CD Cadence

| Healer | Optimized cadence | Notes |
| --- | --- | --- |
| Mistweaver Monk | Restoral/Revival 00:29, 03:55, 07:05. Yu'lon 00:37, 03:08, 05:50, 08:03 if long. Celestial Conduit 00:06, 01:38, 03:24, 05:46, 07:19 if talented. | This removes the two-Conduit problem and the empty 07:00 window. Use Life Cocoon on 04:30 and late Gravity targets. |
| Restoration Druid | Tranquility 00:57, 04:20, 07:36. Convoke 00:05, 01:05, 02:10, 03:10, 04:10, 05:13, 06:13, 07:15, 08:16 if long. | Tranq is shifted from the copied R06 anchors to match the Regidør damage-window swap. Convoke remains the anti-dead-time button. |
| Preservation Evoker | Default Rewind 01:10, 06:04. Stasis setup/pop at 00:20/00:30, 01:50/02:10, 03:20/03:40, 04:50/05:10, 06:20/06:40, 07:50/08:00. Tip the Scales 00:20, 01:31, 04:38, 06:04, 07:34. | This keeps Stasis rolling across the whole fight instead of creating a dead 00:30-04:00 gap. |
| Holy Priest | Apotheosis 00:10, 02:22, 04:47, 06:53, 08:55 if long. Divine Hymn 00:45, 03:29, 06:38, 08:41 if long. Guardian Spirit as assigned spot save. | This is the biggest change from the previous plan: R06 supports earlier Hymns and Apotheosis at 04:47 instead of spending Hymn at 04:44. |

## Swap Rules

| Problem on pull | Change |
| --- | --- |
| We die at 04:20-04:30. | Keep MW reset at 03:55, then add either Pres aggressive-mode Rewind at 04:20 or shift Holy Hymn later from 03:29 only if 03:10-03:40 is safe. |
| We die at 06:00-06:10. | Do not use Rewind at 04:20. Keep Rewind for 06:04 and add Rally/AMZ/Darkness or equivalent raid DR at 06:00. |
| We die at 06:40 before Hymn/Stasis land. | Move Holy Hymn to 06:35 and start Pres/Raid DR earlier; do not move the 07:36 fourth-healer button unless the 06:40 wall is the consistent wipe point. |
| We die at 07:00-07:20. | Keep MW third reset at 07:05 and add a separate external package around 07:36-07:50. |
| We die at 08:00-08:10. | Keep 07:19 Conduit and 08:00 Stasis pop, add Zephyr/AMZ/Darkness around 07:36-07:50, and save spot externals for players targeted during the 08:00 overlap. |

## Open Questions For Next Pass

| Question | Why it matters |
| --- | --- |
| Do we have Darkness, AMZ, Rallying Cry, Aug Zephyr, or Vampiric Embrace? | R06 relied heavily on non-healer DR from 05:20 onward. |
| Is Santatumblr using Revival or Restoral, and are they playing Celestial Conduit? | The import/setup should use the exact button names and only assign Conduit if it exists. |
| Can Deviiarrc truly do the 3-Rewind cadence? | If yes, use the aggressive 00:30/04:20/07:55 mode; if not, use the exact-comp 01:10/06:04 mode. |
| What is our expected kill time? | If we kill before 08:00, the third MW reset can go at 07:05. If we reach 08:40+, we need the full long-kill contingency. |
