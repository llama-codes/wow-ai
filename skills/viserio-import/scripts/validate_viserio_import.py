#!/usr/bin/env python3
"""Validate the basic shape of a Viserio assignment import JSON file."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARNING: {message}", file=sys.stderr)


def require_object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{path} must be an object")
    return value


def require_array(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{path} must be an array")
    return value


def require_number(value: Any, path: str) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        fail(f"{path} must be a number")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_viserio_import.py <viserio-import.json>")

    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - CLI validator should show parse reason
        fail(f"could not read/parse JSON: {exc}")

    root = require_object(data, "$")
    actors = require_array(root.get("actors"), "$.actors")

    if "phases" in root:
        require_array(root["phases"], "$.phases")
    if "customGridRows" in root:
        require_array(root["customGridRows"], "$.customGridRows")

    spell_counts: Counter[str] = Counter()
    note_count = 0
    max_time = 0.0

    for actor_index, actor_value in enumerate(actors):
        actor_path = f"$.actors[{actor_index}]"
        actor = require_object(actor_value, actor_path)
        for key in ("name", "spells", "notes"):
            if key not in actor:
                fail(f"{actor_path}.{key} is required")

        spells = require_array(actor["spells"], f"{actor_path}.spells")
        notes = require_array(actor["notes"], f"{actor_path}.notes")

        for spell_index, row_value in enumerate(spells):
            row_path = f"{actor_path}.spells[{spell_index}]"
            row = require_object(row_value, row_path)
            spell = require_object(row.get("spell"), f"{row_path}.spell")
            for key in ("spellId", "spellName", "guid"):
                if key not in spell:
                    fail(f"{row_path}.spell.{key} is required")
            for key in ("startTime", "phaseNumber", "phaseOffset"):
                if key not in row:
                    fail(f"{row_path}.{key} is required")
            if "actorId" not in row:
                fail(f"{row_path}.actorId is required")
            require_number(row["startTime"], f"{row_path}.startTime")
            require_number(row["phaseOffset"], f"{row_path}.phaseOffset")
            max_time = max(max_time, float(row["startTime"]))
            spell_counts[str(spell["spellName"])] += 1

        for note_index, note_value in enumerate(notes):
            note_path = f"{actor_path}.notes[{note_index}]"
            note = require_object(note_value, note_path)
            for key in ("actor", "startTime", "noteText", "phaseNumber", "phaseOffset"):
                if key not in note:
                    fail(f"{note_path}.{key} is required")
            require_number(note["startTime"], f"{note_path}.startTime")
            require_number(note["phaseOffset"], f"{note_path}.phaseOffset")
            max_time = max(max_time, float(note["startTime"]))
            note_count += 1

    if max_time > 10000:
        warn("largest startTime is > 10000; times may be milliseconds, but Viserio assignment rows normally use seconds")

    print(f"valid Viserio import shape: {len(actors)} actors, {sum(spell_counts.values())} spells, {note_count} notes")
    for name, count in sorted(spell_counts.items()):
        print(f"{count:>3}  {name}")


if __name__ == "__main__":
    main()
