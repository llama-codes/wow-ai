#!/usr/bin/env python3
"""Generate a Viserio assignment import JSON from a Markdown timeline table."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from viserio_common import (
    ViserioError,
    is_separator_row,
    load_viserio_export,
    markdown_cell_text,
    normalize_key,
    parse_time,
    require_array,
    require_object,
    split_markdown_row,
)


CUSTOM_ROW_KEYS = (
    "CustomCooldownSingleCast",
    "customCooldownAllCasts",
    "customDurationSingleCast",
    "customDurationAllCasts",
    "customChargesAllCasts",
)

SPELL_METADATA_KEYS = (
    "note",
    "checks",
    "cooldown",
    "duration",
    "playerSpellType",
    "guid",
    "talentModifiers",
)

SPELL_ALIASES = {
    "am": "Aura Mastery",
    "apoth": "Apotheosis",
    "cd": "Celestial Conduit",
    "celestial": "Celestial Conduit",
    "conduit": "Celestial Conduit",
    "convoke": "Convoke the Spirits",
    "dhymn": "Divine Hymn",
    "hymn": "Divine Hymn",
    "personals": "Personals",
    "personal": "Personals",
    "rally": "Rallying Cry",
    "rallying": "Rallying Cry",
    "stasis pop": "Stasis pop",
    "tip": "Tip the Scales",
    "tranq": "Tranquility",
    "tts": "Tip the Scales",
    "wings": "Avenging Wrath",
    "yulon": "Invoke Yu'lon, the Jade Serpent",
    "yu'lon": "Invoke Yu'lon, the Jade Serpent",
}


@dataclass(frozen=True)
class ParsedAssignment:
    start_time: int | float
    actor_name: str
    kind: str
    text: str


class SpellCatalog:
    def __init__(self, export_data: dict[str, Any]) -> None:
        self.actor_rows: dict[tuple[str, str], dict[str, Any]] = {}
        self.global_rows: dict[str, dict[str, Any]] = {}
        self.reference_spells = load_reference_spells()

        actors = require_array(export_data.get("actors"), "$.actors")
        for actor_index, actor_value in enumerate(actors):
            actor = require_object(actor_value, f"$.actors[{actor_index}]")
            actor_key = normalize_key(str(actor.get("name", "")))
            for spell_index, row_value in enumerate(require_array(actor.get("spells"), f"$.actors[{actor_index}].spells")):
                row = require_object(row_value, f"$.actors[{actor_index}].spells[{spell_index}]")
                spell = require_object(row.get("spell"), f"$.actors[{actor_index}].spells[{spell_index}].spell")
                spell_name = str(spell.get("spellName", "")).strip()
                if not spell_name:
                    continue
                spell_key = normalize_spell_name(spell_name)
                normalized_row = normalize_template_row(row, self.reference_spells.get(spell_key))
                self.actor_rows.setdefault((actor_key, spell_key), copy.deepcopy(normalized_row))
                self.global_rows.setdefault(spell_key, copy.deepcopy(normalized_row))

    def row_for(self, actor_name: str, spell_text: str) -> dict[str, Any]:
        spell_key = normalize_spell_name(spell_text)
        actor_key = normalize_key(actor_name)

        row = self.actor_rows.get((actor_key, spell_key))
        if row is not None:
            return copy.deepcopy(row)

        row = self.global_rows.get(spell_key)
        if row is not None:
            return copy.deepcopy(row)

        spell = self.reference_spells.get(spell_key)
        if spell is not None:
            return default_spell_row(copy.deepcopy(spell))

        raise ViserioError(f"unknown spell {spell_text!r} for actor {actor_name!r}")


def normalize_spell_name(value: str) -> str:
    key = normalize_key(value)
    canonical = SPELL_ALIASES.get(key)
    return normalize_key(canonical) if canonical else key


def default_spell_row(spell: dict[str, Any]) -> dict[str, Any]:
    spell.setdefault("note", {})
    spell.setdefault("checks", {})
    return {
        "spell": spell,
        "startTime": 0,
        "actorId": "",
        "CustomCooldownSingleCast": None,
        "customCooldownAllCasts": None,
        "customDurationSingleCast": None,
        "customDurationAllCasts": None,
        "customChargesAllCasts": None,
        "charges": None,
        "phaseNumber": 0,
        "phaseOffset": 0,
    }


def normalize_template_row(row: dict[str, Any], reference_spell: dict[str, Any] | None = None) -> dict[str, Any]:
    normalized = copy.deepcopy(row)
    spell = copy.deepcopy(require_object(normalized.get("spell"), "spell template .spell"))

    for key in SPELL_METADATA_KEYS:
        if key in normalized and key not in spell:
            spell[key] = normalized[key]
        normalized.pop(key, None)

    if reference_spell is not None:
        for key in SPELL_METADATA_KEYS:
            if key not in spell and key in reference_spell:
                spell[key] = copy.deepcopy(reference_spell[key])

    if not isinstance(spell.get("note"), dict):
        spell["note"] = {}
    if not isinstance(spell.get("checks"), dict):
        spell["checks"] = {}

    normalized["spell"] = spell
    return normalized


def load_reference_spells() -> dict[str, dict[str, Any]]:
    reference_path = Path(__file__).resolve().parents[1] / "references" / "import-format.md"
    if not reference_path.exists():
        return {}

    text = reference_path.read_text(encoding="utf-8")
    spells: dict[str, dict[str, Any]] = {}
    for match in re.finditer(r"```json\s*(.*?)\s*```", text, flags=re.DOTALL):
        try:
            value = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict) and isinstance(value.get("spellName"), str):
            spells.setdefault(normalize_spell_name(value["spellName"]), value)
    return spells


def parse_markdown_plan(path: Path, actor_names: list[str]) -> list[ParsedAssignment]:
    lines = path.read_text(encoding="utf-8").splitlines()
    table_rows: list[tuple[str, str]] = []

    for index, line in enumerate(lines):
        cells = split_markdown_row(line)
        headers = [normalize_key(cell) for cell in cells]
        if "time" not in headers or "assignment" not in headers:
            continue
        if index + 1 >= len(lines) or not is_separator_row(split_markdown_row(lines[index + 1])):
            continue

        time_index = headers.index("time")
        assignment_index = headers.index("assignment")
        for row_line in lines[index + 2 :]:
            row_cells = split_markdown_row(row_line)
            if not row_cells:
                break
            if is_separator_row(row_cells):
                continue
            if len(row_cells) <= max(time_index, assignment_index):
                continue
            table_rows.append((row_cells[time_index], row_cells[assignment_index]))
        break

    if not table_rows:
        raise ViserioError(f"no Markdown table with Time and Assignment columns found in {path}")

    parsed: list[ParsedAssignment] = []
    for time_cell, assignment_cell in table_rows:
        start_time = parse_time(markdown_cell_text(time_cell))
        assignment = markdown_cell_text(assignment_cell)
        if not assignment:
            continue
        for segment in split_assignment_cell(assignment, actor_names):
            actor_name, text = split_actor_segment(segment, actor_names)
            if text.casefold().startswith("note:"):
                note_text = text.split(":", 1)[1].strip()
                parsed.append(ParsedAssignment(start_time, actor_name, "note", note_text))
            else:
                for spell_text in re.split(r"\s+\+\s+", text):
                    spell_text = spell_text.strip()
                    if spell_text:
                        parsed.append(ParsedAssignment(start_time, actor_name, "spell", spell_text))
    return parsed


def split_assignment_cell(value: str, actor_names: list[str]) -> list[str]:
    segments: list[str] = []
    start = 0
    index = 0
    while index < len(value):
        if value[index] == ",":
            after = value[index + 1 :].lstrip()
            if actor_prefix(after, actor_names) is not None:
                segments.append(value[start:index].strip())
                start = index + 1 + (len(value[index + 1 :]) - len(after))
                index = start
                continue
        index += 1

    tail = value[start:].strip()
    if tail:
        segments.append(tail)
    return segments


def split_actor_segment(segment: str, actor_names: list[str]) -> tuple[str, str]:
    match = actor_prefix(segment, actor_names)
    if match is None:
        raise ViserioError(f"could not find an actor prefix in assignment segment {segment!r}")
    actor_name, end = match
    rest = segment[end:].strip()
    if not rest:
        raise ViserioError(f"assignment segment {segment!r} is missing a spell or note")
    return actor_name, rest


def actor_prefix(value: str, actor_names: list[str]) -> tuple[str, int] | None:
    normalized = value.casefold()
    for actor_name in sorted(actor_names, key=len, reverse=True):
        prefix = actor_name.casefold()
        if normalized == prefix:
            return actor_name, len(actor_name)
        if normalized.startswith(prefix) and value[len(actor_name)].isspace():
            return actor_name, len(actor_name)
    return None


def derive_actor_id(actor: dict[str, Any]) -> str:
    for row in actor.get("spells", []):
        if isinstance(row, dict) and isinstance(row.get("actorId"), str) and row["actorId"]:
            return row["actorId"]

    name = str(actor.get("name", "")).strip()
    realm = str(actor.get("realm", "")).strip()
    if name.casefold() == "everyone":
        return "everyone-"
    clean_realm = re.sub(r"[^a-z0-9]", "", realm.casefold())
    return f"{name.casefold()}-{clean_realm}"


def empty_actor(actor: dict[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(actor)
    result["spells"] = []
    result["notes"] = []
    return result


def prepare_spell_row(row: dict[str, Any], assignment: ParsedAssignment, actor_id: str) -> dict[str, Any]:
    prepared = copy.deepcopy(row)
    prepared["startTime"] = assignment.start_time
    prepared["actorId"] = actor_id
    for key in CUSTOM_ROW_KEYS:
        prepared[key] = None
    prepared["charges"] = None
    prepared["phaseNumber"] = 0
    prepared["phaseOffset"] = assignment.start_time
    require_object(prepared.get("spell"), "spell row .spell")
    return prepared


def prepare_note(assignment: ParsedAssignment) -> dict[str, Any]:
    return {
        "actor": assignment.actor_name,
        "startTime": assignment.start_time,
        "noteText": assignment.text,
        "icon": "",
        "phaseNumber": 0,
        "phaseOffset": assignment.start_time,
    }


def build_import(plan_path: Path, export_data: dict[str, Any]) -> dict[str, Any]:
    actors = require_array(export_data.get("actors"), "$.actors")
    actor_map: dict[str, dict[str, Any]] = {}
    actor_ids: dict[str, str] = {}
    actor_names: list[str] = []

    for actor_index, actor_value in enumerate(actors):
        actor = require_object(actor_value, f"$.actors[{actor_index}]")
        name = str(actor.get("name", "")).strip()
        if not name:
            raise ViserioError(f"$.actors[{actor_index}].name is required")
        key = normalize_key(name)
        actor_map[key] = empty_actor(actor)
        actor_ids[key] = derive_actor_id(actor)
        actor_names.append(name)

    assignments = parse_markdown_plan(plan_path, actor_names)
    catalog = SpellCatalog(export_data)

    for assignment in assignments:
        actor_key = normalize_key(assignment.actor_name)
        actor = actor_map.get(actor_key)
        if actor is None:
            raise ViserioError(f"unknown actor {assignment.actor_name!r}")

        if assignment.kind == "note":
            actor["notes"].append(prepare_note(assignment))
        else:
            template = catalog.row_for(assignment.actor_name, assignment.text)
            actor["spells"].append(prepare_spell_row(template, assignment, actor_ids[actor_key]))

    for actor in actor_map.values():
        actor["spells"].sort(key=lambda row: (row.get("startTime", 0), str(row.get("spell", {}).get("spellName", ""))))
        actor["notes"].sort(key=lambda row: (row.get("startTime", 0), str(row.get("noteText", ""))))

    return {
        "actors": [actor_map[normalize_key(str(require_object(actor, "$.actors[]").get("name", "")))] for actor in actors],
        "phases": copy.deepcopy(export_data.get("phases", [])),
        "customGridRows": copy.deepcopy(export_data.get("customGridRows", [])),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path, help="Markdown healing plan with a timeline table")
    parser.add_argument("--export", required=True, type=Path, help="Current Viserio export for roster and metadata")
    parser.add_argument("--output", required=True, type=Path, help="Viserio import JSON to write")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        export_data = load_viserio_export(args.export)
        output_data = build_import(args.plan, export_data)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(output_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except ViserioError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    spell_count = sum(len(actor.get("spells", [])) for actor in output_data["actors"])
    note_count = sum(len(actor.get("notes", [])) for actor in output_data["actors"])
    print(f"wrote {args.output} ({len(output_data['actors'])} actors, {spell_count} spells, {note_count} notes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
