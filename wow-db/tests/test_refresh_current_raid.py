#!/usr/bin/env python3
"""Tests for the WoW current raid database refresher."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from refresh_current_raid import (  # noqa: E402
    BossRef,
    ScraperError,
    SpecRef,
    build_database,
    discover_bosses,
    discover_specs,
    parse_build_page,
    validate_database,
    write_split_database,
)


def build_html(context: str = "All Bosses", parses: str = "2,348", popularity: str = "63.2") -> str:
    return f"""
<html>
  <body>
    <nav>
      <a href="/wow/builds/arcane/mage/raid/overview/mythic/all-bosses">Arcane</a>
      <a href="/wow/builds/fire/mage/raid/overview/mythic/all-bosses">Fire</a>
      <a href="/wow/builds/restoration/druid/raid/overview/mythic/all-bosses">Restoration</a>
      <a href="/wow/builds/arcane/mage/raid/overview/mythic/vanguard">Lightblinded Vanguard</a>
      <a href="/wow/builds/arcane/mage/raid/overview/mythic/crown">Crown of the Cosmos</a>
    </nav>
    <h1>Arcane Mage Raid Build</h1>
    <p>The most popular Arcane Mage Build in WoW - Midnight.</p>
    <p>Data-driven builds updated daily for {context} in Midnight 12.0.5.</p>
    <p>Last updated: 14 hours ago Total Parses: {parses} Based on the top 50% of data in the last 14 days.</p>
    <h2>Arcane Mage Stats</h2>
    <p>Based on data in the last 2 weeks, the stat priority for Arcane Mage looks to be Intellect > Mastery > Crit > Haste > Vers. However, there may be bias based on what gear is available to players.</p>
    <h2>Recommended Arcane Mage Talent Tree Build</h2>
    <p>Spec &amp; Hero Popularity</p>
    <p>{popularity}%</p>
    <p>DPS</p>
    <p>163.1k</p>
    <a href="https://www.warcraftlogs.com/reports/example">Top Log Open Report</a>
    <h3>Class Talents</h3>
    <img alt="Image: Prismatic Barrier">
    <img alt="Image: Alter Time">
    <span>2</span>
    <p>Spellslinger</p>
    <img alt="Image: Attuned Familiar">
    <img alt="Image: Slippery Slinging">
    <h3>Spec Talents</h3>
    <img alt="Image: Arcane Missiles">
    <img alt="Image: Arcane Surge">
    <span>4</span>
    <a href="/export">Export</a>
    <a href="https://www.wowhead.com/talent-calc/mage/arcane/example">Edit</a>
  </body>
</html>
"""


def build_next_html() -> str:
    payload = {
        "props": {
            "pageProps": {
                "page": {
                    "title": "<Styled type='Mage'>Arcane Mage</Styled> Raid Build",
                    "description": "Data-driven builds updated daily for Lightblinded Vanguard in Midnight 12.0.5.",
                    "lastUpdated": "2026-05-25T12:00:00Z",
                    "totalParses": 2378,
                    "metadataSummaryDescription": "Based on the top 50% of data in the last 14 days.",
                    "specOptions": [
                        {
                            "options": [
                                {
                                    "url": "/wow/builds/arcane/mage/raid/overview/mythic/all-bosses",
                                }
                            ]
                        }
                    ],
                    "encounterOptions": [
                        {"value": "all-bosses", "label": "All Bosses"},
                        {
                            "value": "vanguard",
                            "label": "<EncounterIcon id='3180'>Vanguard</EncounterIcon>",
                        },
                    ],
                    "sections": [
                        {
                            "component": "BuildsStatPrioritySection",
                            "props": {
                                "description": "The stat priority looks to be Intellect > Mastery > Crit.",
                                "stats": [
                                    {"name": "Intellect", "order": 1},
                                    {"name": "Mastery", "order": 2},
                                    {"name": "Crit", "order": 3},
                                ],
                            },
                        },
                        {
                            "component": "BuildsTalentTreeBuildSection",
                            "props": {
                                "talentTreeBuildSets": [
                                    {
                                        "metricTiles": [
                                            {"label": "Spec & Hero Popularity", "value": "62.4%"},
                                            {"label": "DPS", "value": "163.1k"},
                                        ],
                                        "alternatives": [
                                            {
                                                "isDefaultSelection": True,
                                                "reportUrl": "https://www.warcraftlogs.com/reports/example",
                                                "talentTree": {
                                                    "dehydratedBuild": {
                                                        "selectedNodes": [[1], [2], [3]],
                                                        "heroSpecId": 40,
                                                    },
                                                    "exportCodeParams": {
                                                        "exportCode": "C4DAAAAAAAAA",
                                                    },
                                                },
                                            }
                                        ],
                                    }
                                ]
                            },
                        },
                    ],
                    "talentTreeBlueprints": {
                        "Mage_Arcane_14": {
                            "heroTrees": [{"name": "Spellslinger", "id": 40}],
                            "changeSet": {
                                "allNodes": [
                                    {
                                        "treeType": "class",
                                        "abilities": [{"id": 1, "name": "Prismatic Barrier"}],
                                    },
                                    {
                                        "treeType": "hero",
                                        "abilities": [{"id": 2, "name": "Attuned Familiar"}],
                                    },
                                    {
                                        "treeType": "spec",
                                        "abilities": [{"id": 3, "name": "Arcane Surge"}],
                                    },
                                ]
                            },
                        }
                    },
                }
            }
        }
    }
    return f'<script id="__NEXT_DATA__" type="application/json">{json.dumps(payload)}</script>'


class RefreshCurrentRaidTests(unittest.TestCase):
    def test_discovers_specs_and_bosses_from_archon_links(self) -> None:
        html = build_html()

        specs = discover_specs(html)
        bosses = discover_bosses(html)

        self.assertEqual([spec.spec_id for spec in specs], ["restoration-druid", "arcane-mage", "fire-mage"])
        self.assertEqual([boss.slug for boss in bosses], ["crown", "vanguard"])
        self.assertEqual(bosses[1].name, "Lightblinded Vanguard")

    def test_parse_build_page_extracts_summary_metrics_and_talents(self) -> None:
        spec = SpecRef(class_slug="mage", spec_slug="arcane")
        entry = parse_build_page(
            build_html(),
            source_url=spec.build_url(),
            spec=spec,
            context_name="All Bosses",
            retrieved_at="2026-05-26T00:00:00Z",
        )

        self.assertEqual(entry["context"], "All Bosses")
        self.assertEqual(entry["heroTree"], "Spellslinger")
        self.assertEqual(entry["statPriority"], ["Intellect", "Mastery", "Crit", "Haste", "Vers"])
        self.assertEqual(entry["popularityPercent"], 63.2)
        self.assertEqual(entry["parseCount"], 2348)
        self.assertEqual(entry["performanceMetric"], {"label": "DPS", "value": "163.1k"})
        self.assertEqual(entry["talents"]["class"], ["Prismatic Barrier", "Alter Time"])
        self.assertEqual(entry["talents"]["hero"], ["Attuned Familiar", "Slippery Slinging"])
        self.assertEqual(entry["talents"]["spec"], ["Arcane Missiles", "Arcane Surge"])
        self.assertTrue(entry["strongPoints"])
        self.assertEqual(entry["weakPoints"], [])
        self.assertIn("wowhead.com/talent-calc", entry["talentEditUrl"])

    def test_parse_build_page_prefers_structured_next_data(self) -> None:
        spec = SpecRef(class_slug="mage", spec_slug="arcane")
        entry = parse_build_page(
            build_next_html(),
            source_url=spec.build_url("vanguard"),
            spec=spec,
            context_name="Lightblinded Vanguard",
            retrieved_at="2026-05-26T00:00:00Z",
        )

        self.assertEqual(entry["context"], "Lightblinded Vanguard")
        self.assertEqual(entry["heroTree"], "Spellslinger")
        self.assertEqual(entry["talentExportCode"], "C4DAAAAAAAAA")
        self.assertEqual(entry["talentEditUrl"], "https://www.wowhead.com/talent-calc/mage/arcane/C4DAAAAAAAAA")
        self.assertEqual(entry["talents"]["class"], ["Prismatic Barrier"])
        self.assertEqual(entry["talents"]["hero"], ["Attuned Familiar"])
        self.assertEqual(entry["talents"]["spec"], ["Arcane Surge"])
        self.assertEqual(discover_bosses(build_next_html())[0].slug, "vanguard")

    def test_generated_weak_point_flags_low_sample_size(self) -> None:
        spec = SpecRef(class_slug="mage", spec_slug="arcane")
        entry = parse_build_page(
            build_html(context="Lightblinded Vanguard", parses="25", popularity="88.0"),
            source_url=spec.build_url("vanguard"),
            spec=spec,
            context_name="Lightblinded Vanguard",
            retrieved_at="2026-05-26T00:00:00Z",
        )

        self.assertEqual(entry["parseCount"], 25)
        self.assertIn("Low Mythic sample size", entry["weakPoints"][0]["text"])

    def test_build_database_preserves_manual_notes(self) -> None:
        spec = SpecRef(class_slug="mage", spec_slug="arcane")
        boss = BossRef(slug="vanguard", name="Lightblinded Vanguard")
        manual_note = {
            "text": "Local roster prefers extra immunity coverage.",
            "basis": "Raid-lead note.",
            "sourceUrl": "",
        }
        existing = {
            "raidName": "Manaforge Omega",
            "warnings": [],
            "specs": [
                {
                    "id": "arcane-mage",
                    "manualNotes": {
                        "strongPoints": [manual_note],
                        "weakPoints": [],
                        "recommendationBuilds": [],
                    },
                }
            ],
        }

        def fetcher(url: str) -> str:
            if url.endswith("/vanguard"):
                return build_html(context="Lightblinded Vanguard", parses="25", popularity="88.0")
            return build_html()

        database = build_database(specs=[spec], bosses=[boss], fetcher=fetcher, delay_seconds=0, existing=existing)

        self.assertEqual(database["raidName"], "Manaforge Omega")
        self.assertEqual(database["specs"][0]["manualNotes"]["strongPoints"], [manual_note])
        self.assertIn("vanguard", database["specs"][0]["bosses"])
        self.assertEqual(database["specs"][0]["bosses"]["vanguard"]["sourceUrl"], spec.build_url("vanguard"))
        validate_database(database)

    def test_write_split_database_creates_manifest_and_spec_file(self) -> None:
        spec = SpecRef(class_slug="mage", spec_slug="arcane")
        database = build_database(
            specs=[spec],
            bosses=[],
            fetcher=lambda _url: build_html(),
            delay_seconds=0,
            existing={},
        )

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "current-raid-mythic.json"
            write_split_database(database, output)
            manifest = json.loads(output.read_text(encoding="utf-8"))
            spec_path = Path(tmp) / manifest["specFiles"][0]["path"]
            spec_data = json.loads(spec_path.read_text(encoding="utf-8"))

        self.assertNotIn("specs", manifest)
        self.assertEqual(manifest["specFiles"][0]["path"], "specs/mage/arcane.json")
        self.assertEqual(spec_data["id"], "arcane-mage")

    def test_validate_database_rejects_missing_source_url(self) -> None:
        spec = SpecRef(class_slug="mage", spec_slug="arcane")
        entry = parse_build_page(
            build_html(),
            source_url=spec.build_url(),
            spec=spec,
            context_name="All Bosses",
            retrieved_at="2026-05-26T00:00:00Z",
        )
        database = {
            "expansion": "Midnight",
            "patch": "12.0.5",
            "raidName": "Current Raid",
            "difficulty": "Mythic",
            "generatedAt": "2026-05-26T00:00:00Z",
            "sourceWindow": "last 14 days",
            "sources": [{"name": "Archon", "url": "https://www.archon.gg", "usage": "test"}],
            "warnings": [],
            "specs": [
                {
                    "id": "arcane-mage",
                    "className": "Mage",
                    "classSlug": "mage",
                    "specName": "Arcane",
                    "specSlug": "arcane",
                    "role": "DPS",
                    "baseline": entry,
                    "bosses": {},
                    "manualNotes": {"strongPoints": [], "weakPoints": [], "recommendationBuilds": []},
                }
            ],
        }
        broken = copy.deepcopy(database)
        broken["specs"][0]["baseline"]["sourceUrl"] = ""

        with self.assertRaisesRegex(ScraperError, "sourceUrl"):
            validate_database(broken)


if __name__ == "__main__":
    unittest.main()
