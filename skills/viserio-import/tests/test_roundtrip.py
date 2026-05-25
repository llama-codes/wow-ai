#!/usr/bin/env python3
"""Tests for the Viserio Markdown round-trip helpers."""

from __future__ import annotations

import base64
import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from md_to_viserio_import import build_import  # noqa: E402
from viserio_common import ViserioError, load_viserio_export  # noqa: E402
from viserio_export_to_md import build_markdown  # noqa: E402


REGIDOR = "Regid\u00f8r"


def spell_row(actor_id: str, start_time: int, spell_id: int, spell_name: str, guid: str) -> dict:
    return {
        "spell": {
            "spellId": spell_id,
            "spellName": spell_name,
            "wowheadLink": "",
            "iconLink": "",
            "note": {},
            "checks": {},
            "cooldown": 60,
            "duration": 0,
            "playerSpellType": "Heal CD",
            "guid": guid,
        },
        "startTime": start_time,
        "actorId": actor_id,
        "CustomCooldownSingleCast": None,
        "customCooldownAllCasts": None,
        "customDurationSingleCast": None,
        "customDurationAllCasts": None,
        "customChargesAllCasts": None,
        "charges": None,
        "phaseNumber": 0,
        "phaseOffset": start_time,
    }


def actor(name: str, player_class: str, spec: str, spells: list[dict] | None = None) -> dict:
    return {
        "name": name,
        "realm": "Azjol-Nerub",
        "playerClass": player_class,
        "playerSpec": spec,
        "spells": spells or [],
        "notes": [],
    }


class ViserioRoundTripTests(unittest.TestCase):
    def test_export_to_markdown_groups_spells_and_notes(self) -> None:
        data = {
            "actors": [
                actor(
                    "Bobbidyboo",
                    "Druid",
                    "Restoration",
                    [
                        spell_row("bobbidyboo-azjolnerub", 21, 391528, "Convoke the Spirits", "convoke-guid"),
                        spell_row("bobbidyboo-azjolnerub", 21, 740, "Tranquility", "tranq-guid"),
                    ],
                ),
                {
                    **actor("Everyone", "None", "All Roles"),
                    "notes": [
                        {
                            "actor": "Everyone",
                            "startTime": 21,
                            "noteText": "stabilize",
                            "icon": "",
                            "phaseNumber": 0,
                            "phaseOffset": 21,
                        }
                    ],
                },
            ],
            "phases": [{"phaseNumber": 0, "phaseTimer": 0}],
            "customGridRows": [],
        }

        markdown = build_markdown(data, "Test Plan", "fixture")

        self.assertIn("`00:21`", markdown)
        self.assertIn("Bobbidyboo Convoke the Spirits + Tranquility", markdown)
        self.assertIn("Everyone note: stabilize", markdown)

    def test_markdown_to_import_uses_aliases_reference_fallback_and_accented_names(self) -> None:
        export_data = {
            "actors": [actor(REGIDOR, "Paladin", "Holy")],
            "phases": [{"phaseNumber": 0, "phaseTimer": 0}],
            "customGridRows": [],
        }
        plan = f"""
| Time | Assignment | Purpose |
| --- | --- | --- |
| `00:05` | {REGIDOR} AM | |
| `00:06` | {REGIDOR} note: keep aura | |
"""

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "plan.md"
            path.write_text(plan, encoding="utf-8")
            result = build_import(path, export_data)

        self.assertEqual(result["phases"], export_data["phases"])
        self.assertEqual(result["customGridRows"], [])
        self.assertEqual(result["actors"][0]["spells"][0]["spell"]["spellName"], "Aura Mastery")
        self.assertEqual(result["actors"][0]["spells"][0]["spell"]["guid"], "1dc41677-01d1-4ac7-a9ca-ef005f7a96d5")
        self.assertEqual(result["actors"][0]["notes"][0]["noteText"], "keep aura")

    def test_missing_actor_and_spell_raise_clear_errors(self) -> None:
        export_data = {
            "actors": [actor("Bobbidyboo", "Druid", "Restoration")],
            "phases": [],
            "customGridRows": [],
        }

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "plan.md"
            path.write_text("| Time | Assignment |\n| --- | --- |\n| `00:01` | Unknown Tranq |\n", encoding="utf-8")
            with self.assertRaisesRegex(ViserioError, "actor prefix"):
                build_import(path, export_data)

            path.write_text("| Time | Assignment |\n| --- | --- |\n| `00:01` | Bobbidyboo Mystery CD |\n", encoding="utf-8")
            with self.assertRaisesRegex(ViserioError, "unknown spell"):
                build_import(path, export_data)

    def test_packed_export_loader(self) -> None:
        payload = base64.b64encode(b"\x81\xa6actors\x90").decode("ascii")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "export.txt"
            path.write_text(payload, encoding="utf-8")
            self.assertEqual(load_viserio_export(path), {"actors": []})

    def test_generated_import_is_json_serializable(self) -> None:
        export_data = {
            "actors": [
                actor(
                    "Bobbidyboo",
                    "Druid",
                    "Restoration",
                    [spell_row("bobbidyboo-azjolnerub", 10, 391528, "Convoke the Spirits", "convoke-guid")],
                )
            ],
            "phases": [],
            "customGridRows": [],
        }
        plan = "| Time | Assignment |\n| --- | --- |\n| `00:10` | Bobbidyboo Convoke |\n"

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "plan.md"
            path.write_text(plan, encoding="utf-8")
            result = build_import(path, export_data)

        json.dumps(result, ensure_ascii=False)
        self.assertEqual(result["actors"][0]["spells"][0]["spell"]["guid"], "convoke-guid")


if __name__ == "__main__":
    unittest.main()

