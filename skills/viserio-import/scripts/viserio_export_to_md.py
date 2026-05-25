#!/usr/bin/env python3
"""Convert a Viserio assignment export into an editable Markdown timeline."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from viserio_common import (
    ViserioError,
    escape_markdown_cell,
    format_time,
    load_viserio_export,
    require_array,
    require_object,
)


def numeric_time(row: dict[str, Any]) -> int | float:
    value = row.get("startTime", row.get("phaseOffset"))
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ViserioError("assignment row is missing numeric startTime")
    return int(value) if float(value).is_integer() else float(value)


def render_segments(events: list[dict[str, Any]]) -> str:
    buckets: list[dict[str, Any]] = []
    for event in events:
        if event["kind"] == "spell":
            for bucket in buckets:
                if bucket["kind"] == "spell" and bucket["actor"] == event["actor"]:
                    bucket["texts"].append(event["text"])
                    break
            else:
                buckets.append({"kind": "spell", "actor": event["actor"], "texts": [event["text"]]})
        else:
            buckets.append(event)

    segments: list[str] = []
    for bucket in buckets:
        if bucket["kind"] == "spell":
            segments.append(f"{bucket['actor']} {' + '.join(bucket['texts'])}")
        else:
            segments.append(f"{bucket['actor']} note: {bucket['text']}")
    return ", ".join(segments)


def build_markdown(data: dict[str, Any], title: str, source_label: str) -> str:
    actors = require_array(data.get("actors"), "$.actors")
    events_by_time: dict[int | float, list[dict[str, Any]]] = defaultdict(list)

    for actor_index, actor_value in enumerate(actors):
        actor = require_object(actor_value, f"$.actors[{actor_index}]")
        actor_name = str(actor.get("name", "")).strip()
        if not actor_name:
            raise ViserioError(f"$.actors[{actor_index}].name is required")

        for spell_index, spell_value in enumerate(require_array(actor.get("spells"), f"$.actors[{actor_index}].spells")):
            row = require_object(spell_value, f"$.actors[{actor_index}].spells[{spell_index}]")
            spell = require_object(row.get("spell"), f"$.actors[{actor_index}].spells[{spell_index}].spell")
            spell_name = str(spell.get("spellName", "")).strip()
            if not spell_name:
                raise ViserioError(f"$.actors[{actor_index}].spells[{spell_index}].spell.spellName is required")
            events_by_time[numeric_time(row)].append(
                {"kind": "spell", "actor": actor_name, "text": spell_name}
            )

        for note_index, note_value in enumerate(require_array(actor.get("notes"), f"$.actors[{actor_index}].notes")):
            note = require_object(note_value, f"$.actors[{actor_index}].notes[{note_index}]")
            note_actor = str(note.get("actor") or actor_name).strip()
            note_text = str(note.get("noteText", "")).strip()
            events_by_time[numeric_time(note)].append(
                {"kind": "note", "actor": note_actor, "text": note_text}
            )

    lines = [
        f"# {title}",
        "",
        f"Generated from `{escape_markdown_cell(source_label)}`.",
        "",
        "| Time | Assignment | Purpose |",
        "| --- | --- | --- |",
    ]

    for start_time in sorted(events_by_time):
        assignment = render_segments(events_by_time[start_time])
        lines.append(f"| `{format_time(start_time)}` | {escape_markdown_cell(assignment)} | |")

    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Viserio export as decoded JSON or packed text")
    parser.add_argument("--output", required=True, type=Path, help="Markdown timeline to write")
    parser.add_argument("--title", default="Viserio Healing Plan", help="Markdown H1 title")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = load_viserio_export(args.input)
        markdown = build_markdown(data, args.title, str(args.input))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
    except ViserioError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

