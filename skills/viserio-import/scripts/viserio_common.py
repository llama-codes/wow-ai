#!/usr/bin/env python3
"""Shared helpers for Viserio assignment import/export scripts."""

from __future__ import annotations

import base64
import json
import re
import struct
from pathlib import Path
from typing import Any


class ViserioError(ValueError):
    """Raised when Viserio input cannot be parsed or converted."""


class MessagePackDecoder:
    """Small MessagePack decoder for the Viserio export subset."""

    def __init__(self, data: bytes) -> None:
        self.data = data
        self.offset = 0

    def unpack(self) -> Any:
        value = self._read()
        if self.offset != len(self.data):
            raise ViserioError(f"trailing bytes after MessagePack object at offset {self.offset}")
        return value

    def _read_exact(self, size: int) -> bytes:
        end = self.offset + size
        if end > len(self.data):
            raise ViserioError("unexpected end of MessagePack payload")
        chunk = self.data[self.offset:end]
        self.offset = end
        return chunk

    def _read_byte(self) -> int:
        return self._read_exact(1)[0]

    def _read_uint(self, size: int) -> int:
        return int.from_bytes(self._read_exact(size), "big", signed=False)

    def _read_int(self, size: int) -> int:
        return int.from_bytes(self._read_exact(size), "big", signed=True)

    def _read_str(self, size: int) -> str:
        return self._read_exact(size).decode("utf-8")

    def _read_array(self, size: int) -> list[Any]:
        return [self._read() for _ in range(size)]

    def _read_map(self, size: int) -> dict[Any, Any]:
        result: dict[Any, Any] = {}
        for _ in range(size):
            key = self._read()
            result[key] = self._read()
        return result

    def _read_ext(self, size: int) -> dict[str, Any]:
        ext_type = self._read_int(1)
        payload = self._read_exact(size)
        return {"__ext_type__": ext_type, "__ext_payload__": base64.b64encode(payload).decode("ascii")}

    def _read(self) -> Any:  # noqa: PLR0911, PLR0912 - direct MessagePack tag table
        tag = self._read_byte()

        if tag <= 0x7F:
            return tag
        if 0x80 <= tag <= 0x8F:
            return self._read_map(tag & 0x0F)
        if 0x90 <= tag <= 0x9F:
            return self._read_array(tag & 0x0F)
        if 0xA0 <= tag <= 0xBF:
            return self._read_str(tag & 0x1F)
        if tag >= 0xE0:
            return tag - 0x100

        if tag == 0xC0:
            return None
        if tag == 0xC2:
            return False
        if tag == 0xC3:
            return True
        if tag == 0xC4:
            return self._read_exact(self._read_uint(1))
        if tag == 0xC5:
            return self._read_exact(self._read_uint(2))
        if tag == 0xC6:
            return self._read_exact(self._read_uint(4))
        if tag == 0xC7:
            return self._read_ext(self._read_uint(1))
        if tag == 0xC8:
            return self._read_ext(self._read_uint(2))
        if tag == 0xC9:
            return self._read_ext(self._read_uint(4))
        if tag == 0xCA:
            return struct.unpack(">f", self._read_exact(4))[0]
        if tag == 0xCB:
            return struct.unpack(">d", self._read_exact(8))[0]
        if tag == 0xCC:
            return self._read_uint(1)
        if tag == 0xCD:
            return self._read_uint(2)
        if tag == 0xCE:
            return self._read_uint(4)
        if tag == 0xCF:
            return self._read_uint(8)
        if tag == 0xD0:
            return self._read_int(1)
        if tag == 0xD1:
            return self._read_int(2)
        if tag == 0xD2:
            return self._read_int(4)
        if tag == 0xD3:
            return self._read_int(8)
        if tag == 0xD4:
            return self._read_ext(1)
        if tag == 0xD5:
            return self._read_ext(2)
        if tag == 0xD6:
            return self._read_ext(4)
        if tag == 0xD7:
            return self._read_ext(8)
        if tag == 0xD8:
            return self._read_ext(16)
        if tag == 0xD9:
            return self._read_str(self._read_uint(1))
        if tag == 0xDA:
            return self._read_str(self._read_uint(2))
        if tag == 0xDB:
            return self._read_str(self._read_uint(4))
        if tag == 0xDC:
            return self._read_array(self._read_uint(2))
        if tag == 0xDD:
            return self._read_array(self._read_uint(4))
        if tag == 0xDE:
            return self._read_map(self._read_uint(2))
        if tag == 0xDF:
            return self._read_map(self._read_uint(4))

        raise ViserioError(f"unsupported MessagePack tag 0x{tag:02x} at offset {self.offset - 1}")


def load_viserio_export(path: Path) -> dict[str, Any]:
    """Load either decoded JSON or a packed Viserio MessagePack/base64 export."""

    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ViserioError(f"{path} is empty")

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        compact = "".join(text.split())
        compact += "=" * (-len(compact) % 4)
        try:
            packed = base64.b64decode(compact, validate=False)
        except Exception as exc:  # noqa: BLE001 - show the base64 failure
            raise ViserioError(f"{path} is neither JSON nor a packed Viserio export: {exc}") from exc
        data = MessagePackDecoder(packed).unpack()

    if not isinstance(data, dict):
        raise ViserioError(f"{path} did not decode to an object")
    return data


def require_array(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise ViserioError(f"{path} must be an array")
    return value


def require_object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ViserioError(f"{path} must be an object")
    return value


def normalize_key(value: str) -> str:
    cleaned = strip_inline_code(value).casefold()
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def strip_inline_code(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == "`" and value[-1] == "`":
        return value[1:-1].strip()
    return value


def parse_time(value: str) -> int | float:
    value = strip_inline_code(value).strip()
    if re.fullmatch(r"\d+(?:\.\d+)?", value):
        parsed = float(value)
        return int(parsed) if parsed.is_integer() else parsed

    parts = value.split(":")
    if len(parts) not in (2, 3):
        raise ViserioError(f"invalid time {value!r}; expected MM:SS, HH:MM:SS, or seconds")
    try:
        numbers = [float(part) for part in parts]
    except ValueError as exc:
        raise ViserioError(f"invalid time {value!r}") from exc

    if len(numbers) == 2:
        minutes, seconds = numbers
        total = minutes * 60 + seconds
    else:
        hours, minutes, seconds = numbers
        total = hours * 3600 + minutes * 60 + seconds
    return int(total) if total.is_integer() else total


def format_time(value: int | float) -> str:
    total = float(value)
    sign = "-" if total < 0 else ""
    total = abs(total)

    if total.is_integer():
        rounded = int(total)
        minutes, seconds = divmod(rounded, 60)
        return f"{sign}{minutes:02d}:{seconds:02d}"

    minutes = int(total // 60)
    seconds = total - minutes * 60
    return f"{sign}{minutes:02d}:{seconds:04.1f}"


def markdown_cell_text(value: str) -> str:
    return strip_inline_code(value.strip().replace(r"\|", "|"))


def escape_markdown_cell(value: str) -> str:
    return str(value).replace("\r", " ").replace("\n", " ").replace("|", r"\|")


def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return []
    if stripped.endswith("|"):
        stripped = stripped[1:-1]
    else:
        stripped = stripped[1:]

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in stripped:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    if escaped:
        current.append("\\")
    cells.append("".join(current).strip())
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)

