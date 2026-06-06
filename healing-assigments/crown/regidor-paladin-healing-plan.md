# Crown of the Cosmos - Regidør Paladin Minimal-Change Plan

## Goal

Use this revision if Bobbidyboo is unavailable and Regidør is the fourth healer.

The learning-curve rule for this version is simple: keep Santatumblr, Deviiarrc, and Nessalove on the same timings as the druid plan. Only the outgoing Restoration Druid slot and incoming Holy Paladin slot change.

| Player | Spec | Change level |
| --- | --- | --- |
| Santatumblr | Mistweaver Monk | Unchanged in `regidor-paladin-viserio-setup.md` |
| Deviiarrc | Preservation Evoker | Unchanged in `regidor-paladin-viserio-setup.md` |
| Nessalove | Holy Priest | Unchanged in `regidor-paladin-viserio-setup.md` |
| Regidør | Holy Paladin | Replaces Bobbidyboo's Druid slot |

## Source Read

| Ref | Report | Healer comp | Why it matters |
| --- | --- | --- | --- |
| R04 | https://www.warcraftlogs.com/reports/tJC1QWjGvLfwA7mc?fight=23&type=healing | RDruid / MW / HPal / Pres | Best Holy Paladin source for Aura timing. Its Avenging Wrath casts are delayed, so this revision uses a steadier 2-minute wings cadence. |
| R06 | https://www.warcraftlogs.com/reports/cNrQwb2gMnk6zKmq?fight=42&type=healing | RDruid / Holy / Pres / MW | Exact previous comp for Santatumblr / Deviiarrc / Nessalove cadence. |

## Keep These Three Healers Unchanged

| Healer | Timings to preserve |
| --- | --- |
| Santatumblr | Revival 00:29, 03:55, 07:05. Yu'lon 00:37, 03:08, 05:50, 08:03 if long. Celestial Conduit 00:06, 01:38, 03:24, 05:46, 07:19 if talented. |
| Deviiarrc | Rewind 01:10, 06:04. Stasis setup/pop at 00:20/00:30, 01:50/02:10, 03:20/03:40, 04:50/05:10, 06:20/06:40, 07:50/08:00. Tip the Scales 00:20, 01:31, 04:38, 06:04, 07:34. |
| Nessalove | Apotheosis 00:10, 02:22, 04:47, 06:53, 08:55 if long. Divine Hymn 00:45, 03:29, 06:38, 08:41 if long. |

## Bobbidyboo To Regidør Swap

| Lost Druid job | Regidør replacement | Notes |
| --- | --- | --- |
| Opener Convoke | Avenging Wrath at 00:00 | Same pull-start call as the druid plan, shifted to exact 2-minute anchors. |
| Opener Tranquility shifted to 00:57 | Aura Mastery at 00:57 | Both fourth-healer packages cover the same early damage window. |
| 01:05 Convoke | Shared 01:10 Rewind | Druid still has Convoke here; Paladin gets the same window through Aura plus shared Rewind. |
| 02:10 Convoke | Avenging Wrath at 02:00 | Wings is active through the Convoke window. |
| 03:10 Convoke | Shared Yu'lon, Conduit, Hymn, and Stasis | This window is shared-healer driven in both versions. |
| 04:10 Convoke into 04:20 Tranquility | Avenging Wrath at 04:00 + Aura Mastery at 04:20 | Main midfight window swap. |
| 05:13 / 06:13 Convoke glue | Avenging Wrath at 06:00 plus shared Stasis/Rewind | Covers the 06:00 Gravity chain and the 06:13 Convoke slot; 05:13 is carried by shared CDs. |
| 06:40 overlap | Nessalove Hymn + Deviiarrc Stasis pop | Both versions hold the fourth-healer DR/channel for the later overlap. |
| 07:15 Convoke into 07:36 Tranquility | Aura Mastery at 07:36 + assigned raid DR | Both fourth-healer packages cover the late Gravity/Cosmic overlap. |

## Minimal-Change Assignment Timeline

| Time | Active coverage | Boss ability covered | Assignment | Why this timing |
| --- | --- | --- | --- | --- |
| 00:00 | 00:00-00:30 | Pull ramp | Regidør Avenging Wrath. | Replaces Bobbidyboo opener Convoke while keeping later wings on exact 2-minute anchors. |
| 00:06 | 00:06-00:10 | Opener ramp | Santatumblr Celestial Conduit. | Adds early Monk value instead of waiting until late. |
| 00:10 | 00:10-00:25 | Opener into Echoing Darkness / Void Expulsion | Nessalove Apotheosis. | Unchanged. |
| 00:20 | 00:20-00:30 | Echoing Darkness + Void Expulsion | Deviiarrc Stasis + Tip the Scales. | Unchanged cadence, now with visible Stasis setup. |
| 00:29 | 00:29 instant reset | Opener recovery | Santatumblr Revival. | Unchanged. |
| 00:30 | 00:30 release | Opener recovery | Deviiarrc Stasis pop. | Shows the first Stasis release in Viserio. |
| 00:37 | 00:37-01:00 | Opener recovery into sustain | Santatumblr Yu'lon. | Unchanged. |
| 00:45 | 00:45-00:55 | Opener tail | Nessalove Divine Hymn. | Unchanged. |
| 00:57 | 00:57-01:05 | Early sustain | Regidør Aura Mastery. | Mirrors Bobbidyboo's shifted 00:57 Tranquility window. |
| 01:10 | 01:10 recovery | Echoing Darkness / Grasp recovery | Deviiarrc Rewind. | Unchanged. |
| 01:31 | 01:31 setup | Mid-cycle damage | Deviiarrc Tip the Scales. | Unchanged. |
| 01:38 | 01:38-01:42 | Mid-cycle sustain | Santatumblr Celestial Conduit. | Second Conduit on cadence. |
| 01:50 | 01:50 setup | Rolling cadence | Deviiarrc Stasis. | Keeps Stasis rolling after opener instead of waiting until 04:00. |
| 02:00 | 02:00-02:30 | Rolling Paladin throughput | Regidør Avenging Wrath. | Extra wings cast between the first and old delayed midfight wings. |
| 02:10 | 02:10 release | Rolling cadence | Deviiarrc Stasis pop. | Releases the second Stasis package. |
| 02:22 | 02:22-02:40 | Setup before Simulacrum pattern | Nessalove Apotheosis. | Unchanged. |
| 03:08 | 03:08-03:25 | Simulacrum setup | Santatumblr Yu'lon. | Unchanged Yu'lon; keep Stasis for the actual 04:20 wall. |
| 03:20 | 03:20 setup | Simulacrum chain | Deviiarrc Stasis. | Third setup keeps Evoker active before the 04:00+ sequence. |
| 03:24 | 03:24-03:28 | Simulacrum setup | Santatumblr Celestial Conduit. | Third Conduit on cadence. |
| 03:29 | 03:29-03:40 | Simulacrum setup continuation | Nessalove Divine Hymn. | Unchanged. |
| 03:40 | 03:40 release | Simulacrum chain | Deviiarrc Stasis pop. | Releases during the Simulacrum ramp. |
| 03:55 | 03:55 instant reset | Fast-timer Simulacrum safety into 04:20 | Santatumblr Revival. | Unchanged and now more important without Convoke. |
| 04:00 | 04:00-04:30 | Simulacrum setup / missing druid channel | Regidør Avenging Wrath. | Covers the full 04:20 Simulacrum wall with the Viserio 30s duration. |
| 04:20 | 04:20-04:28 | Simulacrum Backlash + Void Expulsion + Sting | Regidør Aura Mastery. | Mirrors Bobbidyboo's shifted 04:20 Tranquility window. |
| 04:38 | 04:38 setup | Simulacrum continuation | Deviiarrc Tip the Scales. | Unchanged Tip cadence. |
| 04:47 | 04:47-05:05 | Simulacrum continuation | Nessalove Apotheosis. | Unchanged. |
| 04:50 | 04:50 setup | 05:10 damage window | Deviiarrc Stasis. | Sets up the 05:10 Simulacrum damage. |
| 05:10 | 05:10 release | 05:10 damage window | Deviiarrc Stasis pop. | Releases into the 05:10 damage window. |
| 05:46 | 05:46-05:50 | Gravity Collapse + Cosmic Barrier transition | Santatumblr Celestial Conduit. | Fourth Conduit on cadence. |
| 05:50 | 05:50-06:10 | Gravity Collapse + Cosmic Barrier transition | Santatumblr Yu'lon. | Unchanged. |
| 06:04 | 06:04 reset burst | Gravity Collapse + Cosmic Barrier | Deviiarrc Rewind + Tip the Scales. | Unchanged. |
| 06:00 | 06:00-06:30 | Gravity chain throughput | Regidør Avenging Wrath. | Starts directly on the 06:00 Gravity/Cosmic spike. |
| 06:20 | 06:20 setup | 06:40 overlap | Deviiarrc Stasis. | Sets up the 06:40 Gravity/Cosmic overlap. |
| 06:38 | 06:38-06:50 | Gravity Collapse + Voidstalker Sting | Nessalove Divine Hymn. | Unchanged; this is the weak point if no raid DR is available. |
| 06:40 | 06:40 release | 06:40 overlap | Deviiarrc Stasis pop. | Releases into the 06:40 overlap. |
| 06:53 | 06:53-07:10 | 07:00 sustain bridge | Nessalove Apotheosis. | Unchanged. |
| 07:05 | 07:05 instant reset | 07:00 damage chain | Santatumblr Revival. | Removes the empty 07:00 window. |
| 07:19 | 07:19-07:23 | 07:20-07:40 ramp | Santatumblr Celestial Conduit. | Fifth Conduit on cadence. |
| 07:34 | 07:34 setup | 07:40-08:00 buildup | Deviiarrc Tip the Scales. | Keeps Tip on cadence before the final wall. |
| 07:36 | 07:36-07:50 | Late Gravity/Cosmic overlap | Regidør Aura Mastery + assigned raid DR. | Mirrors Bobbidyboo's shifted 07:36 Tranquility window. |
| 07:50 | 07:50 setup | Final wall | Deviiarrc Stasis. | Final Stasis setup. |
| 08:00 | 08:00 release | 08:00+ final wall | Deviiarrc Stasis pop. | Releases into the final wall instead of after it. |
| 08:03 | 08:03-08:20 contingency | Long-kill sustain | Santatumblr Yu'lon if still fighting. | Unchanged. |
| 08:00 | 08:00-08:30 contingency | Long-kill final throughput | Regidør Avenging Wrath. | Starts directly on the 08:00 wall. |
| 08:41 | 08:41-08:53 contingency | 08:40+ finish pressure | Nessalove Divine Hymn. | Unchanged. |
| 08:55 | 08:55-finish contingency | 08:55 finish pressure | Nessalove Apotheosis and spot externals. | Unchanged. |

## Regidør Cadence

| Spell | Timings | Notes |
| --- | --- | --- |
| Avenging Wrath | 00:00, 02:00, 04:00, 06:00, 08:00 | Adds the missing early cast and keeps wings active on the target windows. |
| Aura Mastery | 00:57, 04:20, 07:36 | Mirrors Bobbidyboo's shifted Tranquility damage-window timings. |
| Blessing of Sacrifice / Lay on Hands | 04:30, 08:00+ as assigned | Keep as spot saves unless we build a full import with exact target notes. |

## Swap Rules

| Problem on pull | Change |
| --- | --- |
| We die at 04:20-04:30. | Keep Santatumblr 03:55 Revival and Regidør 04:00 Wings + 04:20 Aura. Add spot saves at 04:30 before changing the unchanged healer timings. |
| We die at 06:00-06:10. | Keep Deviiarrc 06:04 Rewind. Add Rallying Cry / AMZ / Darkness at 06:00. |
| We die at 06:40-06:50. | Keep Nessalove 06:38 Hymn and Deviiarrc 06:40 Stasis pop. Add raid DR here before moving the 07:36 fourth-healer button. |
| We die at 07:30-07:50. | Keep Santatumblr 07:05 Revival, Regidør 07:36 Aura, and add Zephyr / AMZ / Darkness there. The Druid version uses Bobbidyboo 07:36 Tranquility in the same slot. |
| We die at 08:00-08:10. | Keep 07:19 Conduit, 08:00 Stasis pop, and Regidør 08:00 wings. Save Sac / Lay on Hands / Guardian Spirit / Cocoon for marked players in the overlap. |

## Open Questions

| Question | Why it matters |
| --- | --- |
| Does Regidør's build support the R04-style wings cadence? | If not, keep the two Aura timings and let Regidør follow their actual wings cooldown. |
| Does Santatumblr have Celestial Conduit? | If no, add external DR at 05:46 and 07:19. |
| Which non-healer DRs are available? | The minimal-change plan most needs help at 06:40 and 07:36. |
