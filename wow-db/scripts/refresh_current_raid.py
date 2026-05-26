#!/usr/bin/env python3
"""Refresh the repo-local WoW current raid spec database.

The scraper intentionally uses only Python's standard library. It reads the
server-rendered Archon build pages, extracts summary metrics and talent names,
and preserves local manual notes from the existing JSON database.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import html as html_lib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


ARCHON_BASE_URL = "https://www.archon.gg"
SEED_PATH = "/wow/builds/arcane/mage/raid/overview/mythic/all-bosses"
WOWHEAD_TOOLTIPS_URL = "https://www.wowhead.com/tooltips"
DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "current-raid-mythic.json"
DEFAULT_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schema.json"
DEFAULT_DELAY_SECONDS = 1.25
DEFAULT_RAID_NAME = "The Voidspire"

CLASS_NAMES = {
    "death-knight": "Death Knight",
    "demon-hunter": "Demon Hunter",
    "druid": "Druid",
    "hunter": "Hunter",
    "monk": "Monk",
    "paladin": "Paladin",
    "rogue": "Rogue",
    "shaman": "Shaman",
    "warrior": "Warrior",
    "evoker": "Evoker",
    "mage": "Mage",
    "priest": "Priest",
    "warlock": "Warlock",
}

SPEC_NAMES = {
    "beast-mastery": "Beast Mastery",
    "deathstalker": "Deathstalker",
}

ROLE_BY_SPEC = {
    ("death-knight", "blood"): "Tank",
    ("death-knight", "frost"): "DPS",
    ("death-knight", "unholy"): "DPS",
    ("demon-hunter", "havoc"): "DPS",
    ("demon-hunter", "devourer"): "DPS",
    ("demon-hunter", "vengeance"): "Tank",
    ("druid", "balance"): "DPS",
    ("druid", "feral"): "DPS",
    ("druid", "guardian"): "Tank",
    ("druid", "restoration"): "Healer",
    ("evoker", "augmentation"): "DPS",
    ("evoker", "devastation"): "DPS",
    ("evoker", "preservation"): "Healer",
    ("hunter", "beast-mastery"): "DPS",
    ("hunter", "marksmanship"): "DPS",
    ("hunter", "survival"): "DPS",
    ("mage", "arcane"): "DPS",
    ("mage", "fire"): "DPS",
    ("mage", "frost"): "DPS",
    ("monk", "brewmaster"): "Tank",
    ("monk", "mistweaver"): "Healer",
    ("monk", "windwalker"): "DPS",
    ("paladin", "holy"): "Healer",
    ("paladin", "protection"): "Tank",
    ("paladin", "retribution"): "DPS",
    ("priest", "discipline"): "Healer",
    ("priest", "holy"): "Healer",
    ("priest", "shadow"): "DPS",
    ("rogue", "assassination"): "DPS",
    ("rogue", "outlaw"): "DPS",
    ("rogue", "subtlety"): "DPS",
    ("shaman", "elemental"): "DPS",
    ("shaman", "enhancement"): "DPS",
    ("shaman", "restoration"): "Healer",
    ("warlock", "affliction"): "DPS",
    ("warlock", "demonology"): "DPS",
    ("warlock", "destruction"): "DPS",
    ("warrior", "arms"): "DPS",
    ("warrior", "fury"): "DPS",
    ("warrior", "protection"): "Tank",
}

KNOWN_CURRENT_RAID_BOSSES = {
    "imperator": "Imperator Averzian",
    "salhadaar": "Fallen King Salhadaar",
    "vanguard": "Lightblinded Vanguard",
    "vorasius": "Vorasius",
    "beloren": "Belo'ren, Child of Al'ar",
    "chimaerus": "Chimaerus, the Undreamt God",
    "vaelgor-ezzorak": "Vaelgor & Ezzorak",
    "crown": "Crown of the Cosmos",
    "midnight-falls": "Midnight Falls",
}

HERO_TREES = {
    "Aldrachi Reaver",
    "Archon",
    "Chronowarden",
    "Colossus",
    "Conduit of the Celestials",
    "Dark Ranger",
    "Deathbringer",
    "Deathstalker",
    "Diabolist",
    "Druid of the Claw",
    "Elune's Chosen",
    "Farseer",
    "Fatebound",
    "Fel-Scarred",
    "Flameshaper",
    "Frostfire",
    "Hellcaller",
    "Herald of the Sun",
    "Keeper of the Grove",
    "Lightsmith",
    "Master of Harmony",
    "Mountain Thane",
    "Oracle",
    "Pack Leader",
    "Rider of the Apocalypse",
    "San'layn",
    "Scalecommander",
    "Sentinel",
    "Shado-Pan",
    "Slayer",
    "Soul Harvester",
    "Spellslinger",
    "Stormbringer",
    "Sunfury",
    "Templar",
    "Totemic",
    "Trickster",
    "Voidweaver",
    "Wildstalker",
}


@dataclass(frozen=True)
class SpecRef:
    class_slug: str
    spec_slug: str

    @property
    def spec_id(self) -> str:
        return f"{self.spec_slug}-{self.class_slug}"

    @property
    def class_name(self) -> str:
        return CLASS_NAMES.get(self.class_slug, title_from_slug(self.class_slug))

    @property
    def spec_name(self) -> str:
        return SPEC_NAMES.get(self.spec_slug, title_from_slug(self.spec_slug))

    @property
    def role(self) -> str:
        return ROLE_BY_SPEC.get((self.class_slug, self.spec_slug), "Unknown")

    def build_url(self, boss_slug: str = "all-bosses") -> str:
        return (
            f"{ARCHON_BASE_URL}/wow/builds/{self.spec_slug}/{self.class_slug}"
            f"/raid/overview/mythic/{boss_slug}"
        )


@dataclass(frozen=True)
class BossRef:
    slug: str
    name: str


class ScraperError(RuntimeError):
    """Raised when live data cannot be safely parsed."""


class ArchonHtmlParser(HTMLParser):
    """Small HTML collector for rendered links, image alts, and text chunks."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text_chunks: list[str] = []
        self.anchors: list[dict[str, str]] = []
        self._anchor_stack: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = {key: value or "" for key, value in attrs}
        if tag == "a":
            self._anchor_stack.append({"href": attrs_map.get("href", ""), "text": []})
        elif tag == "img":
            alt = clean_text(attrs_map.get("alt", ""))
            if alt:
                normalized_alt = normalize_image_alt(alt)
                self.text_chunks.append(normalized_alt)
                if self._anchor_stack:
                    self._anchor_stack[-1]["text"].append(normalized_alt)

    def handle_data(self, data: str) -> None:
        text = clean_text(data)
        if not text:
            return
        self.text_chunks.append(text)
        if self._anchor_stack:
            self._anchor_stack[-1]["text"].append(text)

    def handle_endtag(self, tag: str) -> None:
        if tag != "a" or not self._anchor_stack:
            return
        anchor = self._anchor_stack.pop()
        href = anchor.get("href", "")
        text = clean_text(" ".join(anchor.get("text", [])))
        self.anchors.append({"href": href, "text": text})


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def normalize_image_alt(value: str) -> str:
    value = clean_text(value)
    if value.startswith("Image: "):
        value = value[len("Image: ") :]
    return value


def title_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def normalize_url(href: str) -> str:
    if not href:
        return ""
    return urllib.parse.urljoin(ARCHON_BASE_URL, href)


def parse_number(value: str) -> int | None:
    raw = value.strip().lower().replace(",", "")
    if not raw:
        return None
    multiplier = 1
    if raw.endswith("k"):
        multiplier = 1000
        raw = raw[:-1]
    try:
        return int(float(raw) * multiplier)
    except ValueError:
        return None


def parser_from_html(html: str) -> ArchonHtmlParser:
    parser = ArchonHtmlParser()
    parser.feed(html)
    return parser


def extract_next_page(html: str) -> dict[str, Any] | None:
    marker = "__NEXT_DATA__"
    marker_index = html.find(marker)
    if marker_index == -1:
        return None
    start = html.find(">", marker_index)
    end = html.find("</script>", start)
    if start == -1 or end == -1:
        return None
    payload = html_lib.unescape(html[start + 1 : end])
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        return None
    page = data.get("props", {}).get("pageProps", {}).get("page")
    return page if isinstance(page, dict) else None


def collect_urls(value: Any) -> list[str]:
    urls: list[str] = []
    if isinstance(value, dict):
        url = value.get("url")
        if isinstance(url, str):
            urls.append(url)
        for child in value.values():
            urls.extend(collect_urls(child))
    elif isinstance(value, list):
        for child in value:
            urls.extend(collect_urls(child))
    return urls


def discover_specs(html: str) -> list[SpecRef]:
    refs: set[SpecRef] = set()
    pattern = re.compile(r"/wow/builds/([^/]+)/([^/]+)/raid/overview/mythic/all-bosses/?$")

    page = extract_next_page(html)
    urls = collect_urls(page.get("specOptions", [])) if page else []
    if not urls:
        parser = parser_from_html(html)
        urls = [anchor["href"] for anchor in parser.anchors]

    for href in urls:
        url = normalize_url(href)
        parsed = urllib.parse.urlparse(url)
        match = pattern.search(parsed.path)
        if match:
            refs.add(SpecRef(class_slug=match.group(2), spec_slug=match.group(1)))
    return sorted(refs, key=lambda item: (item.class_name, item.spec_name))


def discover_bosses(html: str) -> list[BossRef]:
    page = extract_next_page(html)
    if page:
        bosses = []
        for option in page.get("encounterOptions", []):
            slug = option.get("value")
            if not isinstance(slug, str) or slug == "all-bosses":
                continue
            label = strip_markup(str(option.get("label", "")))
            bosses.append(BossRef(slug=slug, name=KNOWN_CURRENT_RAID_BOSSES.get(slug, label or title_from_slug(slug))))
        if bosses:
            return bosses

    parser = parser_from_html(html)
    refs: dict[str, str] = {}
    pattern = re.compile(r"/wow/builds/[^/]+/[^/]+/raid/overview/mythic/([^/?#]+)/?$")
    for anchor in parser.anchors:
        url = normalize_url(anchor["href"])
        parsed = urllib.parse.urlparse(url)
        match = pattern.search(parsed.path)
        if not match:
            continue
        slug = match.group(1)
        if slug == "all-bosses":
            continue
        text = clean_text(anchor["text"])
        refs[slug] = KNOWN_CURRENT_RAID_BOSSES.get(slug, text or title_from_slug(slug))
    return [BossRef(slug=slug, name=refs[slug]) for slug in sorted(refs, key=lambda key: refs[key])]


def parse_build_page(
    html: str,
    *,
    source_url: str,
    spec: SpecRef,
    context_name: str,
    retrieved_at: str,
) -> dict[str, Any]:
    next_page = extract_next_page(html)
    if next_page:
        return parse_build_page_from_next(
            next_page,
            html=html,
            source_url=source_url,
            spec=spec,
            context_name=context_name,
            retrieved_at=retrieved_at,
        )

    parser = parser_from_html(html)
    text = clean_text(" ".join(parser.text_chunks))
    title_line = find_first(parser.text_chunks, lambda chunk: chunk.endswith("Raid Build"))
    if not title_line:
        raise ScraperError(f"Could not find raid build heading in {source_url}")

    stat_priority = extract_stat_priority(text)
    popularity = extract_popularity(text)
    parse_count = extract_parse_count(text)
    hero_tree = extract_hero_tree(parser.text_chunks)
    talents = extract_talents(parser.text_chunks, hero_tree)
    talent_edit_url = extract_talent_edit_url(parser.anchors)
    top_log_url = extract_top_log_url(parser.anchors)
    last_updated = extract_last_updated(text)
    performance_metric = extract_performance_metric(text)
    boss_name = extract_context_name(text) or context_name

    missing = []
    if parse_count is None:
        missing.append("parse count")
    if popularity is None:
        missing.append("Spec & Hero popularity")
    if not stat_priority:
        missing.append("stat priority")
    if not hero_tree:
        missing.append("hero tree")
    if not talent_edit_url:
        missing.append("Wowhead talent edit URL")
    if missing:
        raise ScraperError(f"Missing {', '.join(missing)} in {source_url}")

    entry = {
        "context": boss_name,
        "heroTree": hero_tree,
        "talentEditUrl": talent_edit_url,
        "statPriority": stat_priority,
        "popularityPercent": popularity,
        "parseCount": parse_count,
        "performanceMetric": performance_metric,
        "topLogUrl": top_log_url,
        "lastUpdated": last_updated,
        "retrievedAt": retrieved_at,
        "sourceUrl": source_url,
        "talents": talents,
    }
    entry["strongPoints"] = build_generated_strong_points(entry, spec)
    entry["weakPoints"] = build_generated_weak_points(entry)
    entry["recommendation"] = build_recommendation(entry, spec)
    return entry


def parse_build_page_from_next(
    page: dict[str, Any],
    *,
    html: str,
    source_url: str,
    spec: SpecRef,
    context_name: str,
    retrieved_at: str,
) -> dict[str, Any]:
    title = strip_markup(str(page.get("title", "")))
    if "Raid Build" not in title:
        raise ScraperError(f"Could not find raid build heading in {source_url}")

    stat_section = find_section(page, "BuildsStatPrioritySection")
    talent_section = find_section(page, "BuildsTalentTreeBuildSection")
    if not stat_section or not talent_section:
        raise ScraperError(f"Could not find stat or talent sections in {source_url}")

    stat_priority = extract_next_stat_priority(stat_section)
    recommended_set = first_talent_build_set(talent_section)
    recommended_alternative = first_recommended_alternative(recommended_set)
    metrics = metrics_from_talent_set(recommended_set)
    popularity = parse_percent(metrics.get("Spec & Hero Popularity", ""))
    performance_metric = first_performance_metric(metrics)
    parse_count = page.get("totalParses")
    if not isinstance(parse_count, int):
        parse_count = None

    talent_tree = recommended_alternative.get("talentTree", {})
    dehydrated_build = talent_tree.get("dehydratedBuild", {})
    hero_tree = hero_tree_from_next_page(page, dehydrated_build.get("heroSpecId"))
    talents = talents_from_next_page(page, dehydrated_build.get("selectedNodes", []))
    talent_export_code = talent_tree.get("exportCodeParams", {}).get("exportCode", "")

    parser = parser_from_html(html)
    talent_edit_url = extract_talent_edit_url(parser.anchors)
    if not talent_edit_url and talent_export_code:
        talent_edit_url = f"https://www.wowhead.com/talent-calc/{spec.class_slug}/{spec.spec_slug}/{talent_export_code}"

    description = strip_markup(str(page.get("description", "")))
    context = "All Bosses" if context_name == "All Bosses" else extract_context_name(description) or context_name
    top_log_url = recommended_alternative.get("reportUrl") or extract_top_log_url(parser.anchors)

    missing = []
    if parse_count is None:
        missing.append("parse count")
    if popularity is None:
        missing.append("Spec & Hero popularity")
    if not stat_priority:
        missing.append("stat priority")
    if not hero_tree:
        missing.append("hero tree")
    if not talent_edit_url:
        missing.append("Wowhead talent edit URL")
    if missing:
        raise ScraperError(f"Missing {', '.join(missing)} in {source_url}")

    entry = {
        "context": context,
        "heroTree": hero_tree,
        "talentEditUrl": talent_edit_url,
        "talentExportCode": talent_export_code,
        "statPriority": stat_priority,
        "popularityPercent": popularity,
        "parseCount": parse_count,
        "performanceMetric": performance_metric,
        "topLogUrl": top_log_url,
        "lastUpdated": str(page.get("lastUpdated", "")),
        "retrievedAt": retrieved_at,
        "sourceUrl": source_url,
        "talents": talents,
    }
    entry["strongPoints"] = build_generated_strong_points(entry, spec)
    entry["weakPoints"] = build_generated_weak_points(entry)
    entry["recommendation"] = build_recommendation(entry, spec)
    return entry


def strip_markup(value: str) -> str:
    value = html_lib.unescape(value)
    value = re.sub(r"<[^>]+>", "", value)
    return clean_text(value)


def find_section(page: dict[str, Any], component: str) -> dict[str, Any]:
    for section in page.get("sections", []):
        if section.get("component") == component:
            props = section.get("props", {})
            return props if isinstance(props, dict) else {}
    return {}


def extract_next_stat_priority(stat_section: dict[str, Any]) -> list[str]:
    stats = stat_section.get("stats", [])
    if isinstance(stats, list) and stats:
        ordered = sorted(
            [stat for stat in stats if isinstance(stat, dict) and isinstance(stat.get("order"), int)],
            key=lambda stat: stat["order"],
        )
        names = [str(stat.get("name", "")).strip() for stat in ordered]
        names = [name for name in names if name]
        if names:
            return names
    return extract_stat_priority(strip_markup(str(stat_section.get("description", ""))))


def first_talent_build_set(talent_section: dict[str, Any]) -> dict[str, Any]:
    sets = talent_section.get("talentTreeBuildSets", [])
    if not isinstance(sets, list) or not sets:
        return {}
    first = sets[0]
    return first if isinstance(first, dict) else {}


def first_recommended_alternative(talent_set: dict[str, Any]) -> dict[str, Any]:
    alternatives = talent_set.get("alternatives", [])
    if not isinstance(alternatives, list) or not alternatives:
        return {}
    for alternative in alternatives:
        if isinstance(alternative, dict) and alternative.get("isDefaultSelection"):
            return alternative
    first = alternatives[0]
    return first if isinstance(first, dict) else {}


def metrics_from_talent_set(talent_set: dict[str, Any]) -> dict[str, str]:
    metrics: dict[str, str] = {}
    for metric in talent_set.get("metricTiles", []):
        if not isinstance(metric, dict):
            continue
        label = str(metric.get("label", "")).strip()
        value = str(metric.get("value", "")).strip()
        if label:
            metrics[label] = value
    return metrics


def parse_percent(value: str) -> float | None:
    match = re.search(r"([0-9]+(?:\.[0-9]+)?)%", value)
    return float(match.group(1)) if match else None


def first_performance_metric(metrics: dict[str, str]) -> dict[str, str | None]:
    for label, value in metrics.items():
        if label != "Spec & Hero Popularity":
            return {"label": label.upper(), "value": value}
    return {"label": None, "value": None}


def first_blueprint(page: dict[str, Any]) -> dict[str, Any]:
    blueprints = page.get("talentTreeBlueprints", {})
    if isinstance(blueprints, dict) and blueprints:
        first = next(iter(blueprints.values()))
        return first if isinstance(first, dict) else {}
    return {}


def hero_tree_from_next_page(page: dict[str, Any], hero_spec_id: Any) -> str:
    blueprint = first_blueprint(page)
    for tree in blueprint.get("heroTrees", []):
        if isinstance(tree, dict) and tree.get("id") == hero_spec_id:
            return str(tree.get("name", ""))
    return ""


def talents_from_next_page(page: dict[str, Any], selected_nodes: Any) -> dict[str, list[str]]:
    blueprint = first_blueprint(page)
    ability_lookup: dict[int, tuple[str, str]] = {}
    for node in blueprint.get("changeSet", {}).get("allNodes", []):
        if not isinstance(node, dict):
            continue
        tree_type = str(node.get("treeType", ""))
        for ability in node.get("abilities", []):
            if not isinstance(ability, dict) or not isinstance(ability.get("id"), int):
                continue
            ability_lookup[ability["id"]] = (str(ability.get("name", "")), tree_type)

    talents = {"class": [], "hero": [], "spec": []}
    if not isinstance(selected_nodes, list):
        return talents

    for selected in selected_nodes:
        if not isinstance(selected, list) or not selected:
            continue
        ability_id = selected[0]
        if not isinstance(ability_id, int):
            continue
        match = ability_lookup.get(ability_id)
        if not match:
            continue
        name, tree_type = match
        bucket = tree_type if tree_type in talents else ""
        if bucket and name and name not in talents[bucket]:
            talents[bucket].append(name)
    return talents


def find_first(chunks: list[str], predicate: Any) -> str | None:
    for chunk in chunks:
        if predicate(chunk):
            return chunk
    return None


def extract_stat_priority(text: str) -> list[str]:
    match = re.search(r"stat priority for .*? looks to be (.*?)(?:\. However|\.)", text, re.IGNORECASE | re.DOTALL)
    if not match:
        return []
    raw = clean_text(match.group(1))
    return [clean_text(part) for part in raw.split(">") if clean_text(part)]


def extract_popularity(text: str) -> float | None:
    match = re.search(r"Spec\s*&\s*Hero\s+Popularity\s+([0-9]+(?:\.[0-9]+)?)%", text, re.IGNORECASE)
    if not match:
        return None
    return float(match.group(1))


def extract_parse_count(text: str) -> int | None:
    match = re.search(r"Total Parses:\s*([0-9][0-9,.]*k?)", text, re.IGNORECASE)
    if not match:
        return None
    return parse_number(match.group(1))


def extract_last_updated(text: str) -> str:
    match = re.search(r"Last updated:\s*(.*?)\s+Total Parses:", text, re.IGNORECASE)
    return clean_text(match.group(1)) if match else ""


def extract_context_name(text: str) -> str:
    match = re.search(r"Data-driven builds updated daily for (.*?) in ", text, re.IGNORECASE)
    if not match:
        return ""
    return clean_text(match.group(1))


def extract_performance_metric(text: str) -> dict[str, str | None]:
    match = re.search(
        r"Spec\s*&\s*Hero\s+Popularity\s+[0-9]+(?:\.[0-9]+)?%\s+([A-Za-z]+)\s+([0-9]+(?:\.[0-9]+)?k?)",
        text,
        re.IGNORECASE,
    )
    if not match:
        return {"label": None, "value": None}
    return {"label": match.group(1).upper(), "value": match.group(2)}


def extract_hero_tree(chunks: list[str]) -> str:
    start = index_of(chunks, "Class Talents")
    end = index_of(chunks, "Spec Talents")
    if start == -1 or end == -1 or start >= end:
        return ""
    for chunk in chunks[start:end]:
        if chunk in HERO_TREES:
            return chunk
    return ""


def extract_talents(chunks: list[str], hero_tree: str) -> dict[str, list[str]]:
    class_start = index_of(chunks, "Class Talents")
    spec_start = index_of(chunks, "Spec Talents")
    export_start = index_of(chunks, "Export")
    hero_index = chunks.index(hero_tree) if hero_tree in chunks else -1

    class_talents = slice_talents(chunks, class_start + 1, hero_index if hero_index != -1 else spec_start)
    hero_talents = slice_talents(chunks, hero_index + 1, spec_start) if hero_index != -1 else []
    spec_talents = slice_talents(chunks, spec_start + 1, export_start if export_start != -1 else len(chunks))
    return {
        "class": class_talents,
        "hero": hero_talents,
        "spec": spec_talents,
    }


def index_of(chunks: list[str], needle: str) -> int:
    try:
        return chunks.index(needle)
    except ValueError:
        return -1


def slice_talents(chunks: list[str], start: int, end: int) -> list[str]:
    if start < 0 or end < 0 or start >= end:
        return []
    ignored = {
        "Image",
        "Class Talents",
        "Spec Talents",
        "Export",
        "Edit",
        "View Alternative Builds",
        "Currently Selected",
        "Recommended Class Tree",
    }
    talents: list[str] = []
    for chunk in chunks[start:end]:
        if chunk in ignored or chunk in HERO_TREES:
            continue
        if re.fullmatch(r"[0-9]+", chunk):
            continue
        if chunk.endswith("%") or chunk.startswith("Alternative Class Tree"):
            continue
        if chunk and chunk not in talents:
            talents.append(chunk)
    return talents


def extract_talent_edit_url(anchors: list[dict[str, str]]) -> str:
    for anchor in anchors:
        href = normalize_url(anchor["href"])
        text = anchor["text"].lower()
        if "wowhead.com" in href and ("talent" in href or text == "edit"):
            return href
    return ""


def extract_top_log_url(anchors: list[dict[str, str]]) -> str:
    for anchor in anchors:
        href = normalize_url(anchor["href"])
        if "warcraftlogs.com" in href:
            return href
    return ""


def build_generated_strong_points(entry: dict[str, Any], spec: SpecRef) -> list[dict[str, str]]:
    points: list[dict[str, str]] = []
    popularity = entry.get("popularityPercent")
    if isinstance(popularity, (int, float)) and popularity >= 60:
        points.append(
            note(
                f"High build consensus for {entry['context']} at {popularity:.1f}% Spec & Hero popularity.",
                "Spec & Hero popularity from Archon.",
                entry["sourceUrl"],
            )
        )
    if entry.get("statPriority"):
        points.append(
            note(
                f"Clear stat direction for {spec.spec_name} {spec.class_name}: {' > '.join(entry['statPriority'])}.",
                "Archon stat priority from the current two-week data window.",
                entry["sourceUrl"],
            )
        )
    return points


def build_generated_weak_points(entry: dict[str, Any]) -> list[dict[str, str]]:
    points: list[dict[str, str]] = []
    parse_count = entry.get("parseCount")
    popularity = entry.get("popularityPercent")
    if isinstance(parse_count, int) and parse_count < 50:
        points.append(
            note(
                f"Low Mythic sample size for {entry['context']} with {parse_count} parses.",
                "Archon Total Parses metric.",
                entry["sourceUrl"],
            )
        )
    if isinstance(popularity, (int, float)) and popularity < 35:
        points.append(
            note(
                f"Build consensus is split at {popularity:.1f}% Spec & Hero popularity.",
                "Spec & Hero popularity from Archon.",
                entry["sourceUrl"],
            )
        )
    return points


def build_recommendation(entry: dict[str, Any], spec: SpecRef) -> dict[str, str]:
    return {
        "text": (
            f"Use the Archon recommended {entry['heroTree']} build for "
            f"{spec.spec_name} {spec.class_name} on {entry['context']}."
        ),
        "basis": "Archon recommended talent tree, Spec & Hero popularity, and current parse sample.",
        "sourceUrl": entry["sourceUrl"],
    }


def note(text: str, basis: str, source_url: str) -> dict[str, str]:
    return {"text": text, "basis": basis, "sourceUrl": source_url}


def load_existing_database(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if "specFiles" in data and "specs" not in data:
        data["specs"] = load_split_specs(data, path.parent)
    return data


def load_split_specs(manifest: dict[str, Any], base_dir: Path) -> list[dict[str, Any]]:
    specs = []
    for spec_file in manifest.get("specFiles", []):
        relative_path = spec_file.get("path")
        if not relative_path:
            continue
        path = base_dir / relative_path
        with path.open("r", encoding="utf-8") as handle:
            specs.append(json.load(handle))
    return specs


def manual_notes_by_spec(existing: dict[str, Any]) -> dict[str, Any]:
    notes: dict[str, Any] = {}
    for spec in existing.get("specs", []):
        spec_id = spec.get("id")
        if spec_id:
            notes[spec_id] = copy.deepcopy(spec.get("manualNotes", default_manual_notes()))
    return notes


def default_manual_notes() -> dict[str, list[Any]]:
    return {
        "strongPoints": [],
        "weakPoints": [],
        "recommendationBuilds": [],
    }


def build_database(
    *,
    specs: list[SpecRef],
    bosses: list[BossRef],
    fetcher: Any,
    delay_seconds: float,
    existing: dict[str, Any],
) -> dict[str, Any]:
    retrieved_at = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    warnings: list[str] = []
    existing_manual_notes = manual_notes_by_spec(existing)
    output_specs: list[dict[str, Any]] = []
    expansion = ""
    patch = ""
    source_window = "last 14 days"
    existing_raid_name = existing.get("raidName")
    raid_name = existing_raid_name if existing_raid_name and existing_raid_name != "Current Raid" else DEFAULT_RAID_NAME

    for index, spec in enumerate(specs):
        baseline_url = spec.build_url("all-bosses")
        baseline_html = fetcher(baseline_url)
        baseline = parse_build_page(
            baseline_html,
            source_url=baseline_url,
            spec=spec,
            context_name="All Bosses",
            retrieved_at=retrieved_at,
        )
        next_page = extract_next_page(baseline_html)
        if next_page:
            page_text = " ".join(
                [
                    strip_markup(str(next_page.get("description", ""))),
                    strip_markup(str(next_page.get("metadataSummaryDescription", ""))),
                ]
            )
        else:
            page_text = clean_text(" ".join(parser_from_html(baseline_html).text_chunks))
        expansion = expansion or extract_expansion(page_text)
        patch = patch or extract_patch(page_text)
        source_window = extract_source_window(page_text) or source_window

        boss_entries: dict[str, Any] = {}
        for boss in bosses:
            if delay_seconds:
                time.sleep(delay_seconds)
            boss_url = spec.build_url(boss.slug)
            boss_html = fetcher(boss_url)
            boss_entry = parse_build_page(
                boss_html,
                source_url=boss_url,
                spec=spec,
                context_name=boss.name,
                retrieved_at=retrieved_at,
            )
            boss_entry["bossSlug"] = boss.slug
            boss_entry["bossName"] = boss_entry["context"]
            boss_entries[boss.slug] = boss_entry

        output_specs.append(
            {
                "id": spec.spec_id,
                "className": spec.class_name,
                "classSlug": spec.class_slug,
                "specName": spec.spec_name,
                "specSlug": spec.spec_slug,
                "role": spec.role,
                "baseline": baseline,
                "bosses": boss_entries,
                "manualNotes": existing_manual_notes.get(spec.spec_id, default_manual_notes()),
            }
        )
        if delay_seconds and index != len(specs) - 1:
            time.sleep(delay_seconds)

    if not expansion:
        warnings.append("Could not extract expansion name from Archon pages.")
    if not patch:
        warnings.append("Could not extract patch version from Archon pages.")
    if not bosses:
        warnings.append("No boss-specific pages were discovered; database only has all-bosses baselines.")

    database = {
        "$schema": "./schema.json",
        "expansion": expansion or existing.get("expansion", ""),
        "patch": patch or existing.get("patch", ""),
        "raidName": raid_name,
        "difficulty": "Mythic",
        "generatedAt": retrieved_at,
        "sourceWindow": source_window,
        "sources": [
            {
                "name": "Archon",
                "url": f"{ARCHON_BASE_URL}{SEED_PATH}",
                "usage": "Data-driven build metrics, stat priorities, talent recommendations, parse counts, and source links.",
            },
            {
                "name": "Wowhead Tooltips",
                "url": WOWHEAD_TOOLTIPS_URL,
                "usage": "Canonical tooltip-friendly talent, spell, and item links.",
            },
        ],
        "warnings": [*preserved_warnings(existing), *warnings],
        "specs": output_specs,
    }
    validate_database(database)
    return database


def preserved_warnings(existing: dict[str, Any]) -> list[str]:
    stale_prefixes = (
        "Initial empty snapshot.",
        "No boss-specific pages were discovered;",
    )
    return [
        warning
        for warning in existing.get("warnings", [])
        if not any(str(warning).startswith(prefix) for prefix in stale_prefixes)
    ]


def extract_expansion(text: str) -> str:
    match = re.search(r"in (Midnight|The War Within|Dragonflight)(?:\s+[0-9]|\s+Pre-Patch)", text)
    return match.group(1) if match else ""


def extract_patch(text: str) -> str:
    match = re.search(r"\b([0-9]+\.[0-9]+(?:\.[0-9]+)?)\b", text)
    return match.group(1) if match else ""


def extract_source_window(text: str) -> str:
    match = re.search(r"Based on .*? in the (last [0-9]+ days)", text, re.IGNORECASE)
    return match.group(1) if match else ""


def validate_database(data: dict[str, Any]) -> None:
    if "specFiles" in data:
        validate_split_database(data, DEFAULT_DB_PATH.parent)
        return

    if DEFAULT_SCHEMA_PATH.exists():
        # Generated in-memory databases use the old monolithic shape. The
        # committed snapshot is split before it is written and then validated
        # against schema.json.
        pass

    validate_monolith_database(data)


def validate_monolith_database(data: dict[str, Any]) -> None:
    required = ["expansion", "patch", "raidName", "difficulty", "generatedAt", "sourceWindow", "sources", "warnings", "specs"]
    for key in required:
        if key not in data:
            raise ScraperError(f"Database is missing top-level key: {key}")
    if data["difficulty"] != "Mythic":
        raise ScraperError("Database difficulty must be Mythic")
    if not isinstance(data["sources"], list) or not data["sources"]:
        raise ScraperError("Database must include at least one source")
    if not isinstance(data["specs"], list):
        raise ScraperError("Database specs must be a list")
    for spec in data["specs"]:
        validate_spec(spec)


def validate_split_database(data: dict[str, Any], base_dir: Path) -> None:
    if DEFAULT_SCHEMA_PATH.exists():
        manifest_for_schema = copy.deepcopy(data)
        manifest_for_schema.pop("specs", None)
        with DEFAULT_SCHEMA_PATH.open("r", encoding="utf-8") as handle:
            validate_json_schema(manifest_for_schema, json.load(handle))

    required = ["expansion", "patch", "raidName", "difficulty", "generatedAt", "sourceWindow", "sources", "warnings", "specFiles"]
    for key in required:
        if key not in data:
            raise ScraperError(f"Database is missing top-level key: {key}")
    if data["difficulty"] != "Mythic":
        raise ScraperError("Database difficulty must be Mythic")
    if not isinstance(data["sources"], list) or not data["sources"]:
        raise ScraperError("Database must include at least one source")
    if not isinstance(data["specFiles"], list):
        raise ScraperError("Database specFiles must be a list")

    for spec_file in data["specFiles"]:
        relative_path = spec_file.get("path")
        if not isinstance(relative_path, str) or not relative_path:
            raise ScraperError("Each specFiles entry must include a path")
        path = base_dir / relative_path
        if not path.exists():
            raise ScraperError(f"Spec file does not exist: {path}")
        with path.open("r", encoding="utf-8") as handle:
            spec = json.load(handle)
        if DEFAULT_SCHEMA_PATH.exists():
            with DEFAULT_SCHEMA_PATH.open("r", encoding="utf-8") as handle:
                root_schema = json.load(handle)
            validate_json_schema(spec, {"$ref": "#/$defs/spec"}, root_schema)
        validate_spec(spec)


def validate_spec(spec: dict[str, Any]) -> None:
    for key in ["id", "className", "classSlug", "specName", "specSlug", "role", "baseline", "bosses", "manualNotes"]:
        if key not in spec:
            raise ScraperError(f"Spec entry is missing key: {key}")
    validate_build_entry(spec["baseline"], f"{spec['id']} baseline")
    if not isinstance(spec["bosses"], dict):
        raise ScraperError(f"{spec['id']} bosses must be an object keyed by boss slug")
    for boss_slug, boss_entry in spec["bosses"].items():
        if not isinstance(boss_entry, dict):
            raise ScraperError(f"{spec['id']} boss {boss_slug} must be an object")
        validate_build_entry(boss_entry, f"{spec['id']} boss {boss_slug}")


def validate_build_entry(entry: dict[str, Any], label: str) -> None:
    required = [
        "context",
        "heroTree",
        "talentEditUrl",
        "statPriority",
        "popularityPercent",
        "parseCount",
        "topLogUrl",
        "sourceUrl",
        "strongPoints",
        "weakPoints",
        "recommendation",
    ]
    for key in required:
        if key not in entry:
            raise ScraperError(f"{label} is missing key: {key}")
    if not entry["sourceUrl"]:
        raise ScraperError(f"{label} is missing sourceUrl")
    for collection in ["strongPoints", "weakPoints"]:
        if not isinstance(entry[collection], list):
            raise ScraperError(f"{label} {collection} must be a list")
        for note_entry in entry[collection]:
            validate_note(note_entry, f"{label} {collection}")
    validate_note(entry["recommendation"], f"{label} recommendation")


def validate_note(note_entry: dict[str, Any], label: str) -> None:
    for key in ["text", "basis", "sourceUrl"]:
        if key not in note_entry:
            raise ScraperError(f"{label} note is missing key: {key}")


def validate_json_schema(instance: Any, schema: dict[str, Any], root_schema: dict[str, Any] | None = None, path: str = "$") -> None:
    root_schema = root_schema or schema
    if "$ref" in schema:
        schema = resolve_schema_ref(root_schema, schema["$ref"])

    if "const" in schema and instance != schema["const"]:
        raise ScraperError(f"{path} must equal {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        raise ScraperError(f"{path} must be one of {schema['enum']!r}")
    if "type" in schema:
        expected = schema["type"]
        expected_types = expected if isinstance(expected, list) else [expected]
        if not any(matches_json_type(instance, expected_type) for expected_type in expected_types):
            raise ScraperError(f"{path} must be {expected!r}")

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                raise ScraperError(f"{path} is missing required key {key!r}")

        properties = schema.get("properties", {})
        additional = schema.get("additionalProperties", True)
        for key, value in instance.items():
            child_path = f"{path}.{key}"
            if key in properties:
                validate_json_schema(value, properties[key], root_schema, child_path)
            elif additional is False:
                raise ScraperError(f"{child_path} is not allowed by schema")
            elif isinstance(additional, dict):
                validate_json_schema(value, additional, root_schema, child_path)

    if isinstance(instance, list) and isinstance(schema.get("items"), dict):
        for index, value in enumerate(instance):
            validate_json_schema(value, schema["items"], root_schema, f"{path}[{index}]")


def resolve_schema_ref(root_schema: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ScraperError(f"Unsupported schema ref: {ref}")
    current: Any = root_schema
    for part in ref[2:].split("/"):
        if not isinstance(current, dict) or part not in current:
            raise ScraperError(f"Could not resolve schema ref: {ref}")
        current = current[part]
    if not isinstance(current, dict):
        raise ScraperError(f"Schema ref does not resolve to an object: {ref}")
    return current


def matches_json_type(value: Any, expected_type: str) -> bool:
    if expected_type == "object":
        return isinstance(value, dict)
    if expected_type == "array":
        return isinstance(value, list)
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected_type == "null":
        return value is None
    if expected_type == "boolean":
        return isinstance(value, bool)
    raise ScraperError(f"Unsupported JSON Schema type: {expected_type}")


def fetch_url(url: str, timeout_seconds: float) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "wow-ai-local-db/1.0 (+https://www.archon.gg/wow)",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")
    except urllib.error.URLError as exc:
        raise ScraperError(f"Failed to fetch {url}: {exc}") from exc


def static_bosses() -> list[BossRef]:
    return [BossRef(slug=slug, name=name) for slug, name in KNOWN_CURRENT_RAID_BOSSES.items()]


def spec_relative_path(spec: dict[str, Any]) -> Path:
    return Path("specs") / str(spec["classSlug"]) / f"{spec['specSlug']}.json"


def manifest_from_database(database: dict[str, Any]) -> dict[str, Any]:
    manifest = {key: copy.deepcopy(value) for key, value in database.items() if key != "specs"}
    manifest["specFiles"] = [
        {
            "id": spec["id"],
            "className": spec["className"],
            "specName": spec["specName"],
            "role": spec["role"],
            "path": spec_relative_path(spec).as_posix(),
        }
        for spec in database.get("specs", [])
    ]
    return manifest


def write_split_database(database: dict[str, Any], output_path: Path) -> None:
    validate_monolith_database(database)
    base_dir = output_path.parent
    for spec in database.get("specs", []):
        path = base_dir / spec_relative_path(spec)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(spec, handle, ensure_ascii=False, indent=2)
            handle.write("\n")

    manifest = manifest_from_database(database)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    validate_split_database(manifest, base_dir)


def split_existing_database(output_path: Path) -> dict[str, Any]:
    data = load_existing_database(output_path)
    if "specs" not in data:
        raise ScraperError(f"{output_path} does not contain monolithic specs to split")
    write_split_database(data, output_path)
    manifest = load_existing_database(output_path)
    validate_split_database(manifest, output_path.parent)
    return manifest


def parse_spec_filter(value: str) -> SpecRef:
    parts = value.split("/")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("spec filters must use spec-slug/class-slug, e.g. arcane/mage")
    return SpecRef(spec_slug=parts[0], class_slug=parts[1])


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh the local WoW current raid spec database.")
    parser.add_argument("--output", type=Path, default=DEFAULT_DB_PATH, help="Database JSON path to write or validate.")
    parser.add_argument("--write", action="store_true", help="Write the refreshed database to --output.")
    parser.add_argument("--monolith", action="store_true", help="Write a single large JSON file instead of split spec files.")
    parser.add_argument("--split-existing", action="store_true", help="Split an existing monolithic --output file into per-spec files.")
    parser.add_argument("--validate", action="store_true", help="Validate --output and exit without fetching.")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS, help="Delay between live requests in seconds.")
    parser.add_argument("--timeout", type=float, default=30.0, help="Network timeout per request in seconds.")
    parser.add_argument("--live-smoke", action="store_true", help="Fetch one spec and one boss without writing unless --write is set.")
    parser.add_argument("--max-specs", type=int, default=0, help="Limit number of specs fetched. Mostly for smoke checks.")
    parser.add_argument("--max-bosses", type=int, default=0, help="Limit number of boss pages fetched per spec. Mostly for smoke checks.")
    parser.add_argument("--spec", type=parse_spec_filter, default=None, help="Fetch only one spec as spec-slug/class-slug.")
    parser.add_argument("--boss", default="", help="Fetch only one boss slug, or all-bosses for baseline only.")
    parser.add_argument(
        "--strict-discovery",
        action="store_true",
        help="Fail if boss links are not discoverable from Archon instead of using local current-raid seeds.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.split_existing:
        manifest = split_existing_database(args.output)
        print(f"Split {args.output} into {len(manifest['specFiles'])} spec files")
        return 0

    if args.validate:
        data = load_existing_database(args.output)
        if "specFiles" in data:
            validate_split_database(data, args.output.parent)
        else:
            validate_database(data)
        print(f"Validated {args.output}")
        return 0

    fetcher = lambda url: fetch_url(url, args.timeout)
    existing = load_existing_database(args.output)
    seed_url = f"{ARCHON_BASE_URL}{SEED_PATH}"
    seed_html = fetcher(seed_url)

    specs = [args.spec] if args.spec else discover_specs(seed_html)
    if not specs:
        raise ScraperError(f"No class/spec build links discovered from {seed_url}")

    if args.boss == "all-bosses":
        bosses: list[BossRef] = []
    elif args.boss:
        bosses = [BossRef(slug=args.boss, name=KNOWN_CURRENT_RAID_BOSSES.get(args.boss, title_from_slug(args.boss)))]
    else:
        bosses = discover_bosses(seed_html)
        if not bosses:
            if args.strict_discovery:
                raise ScraperError(f"No boss-specific build links discovered from {seed_url}")
            bosses = static_bosses()
            existing.setdefault("warnings", []).append(
                "Boss links were not discoverable from the seed page; used local current-raid boss seeds."
            )

    if args.live_smoke:
        specs = specs[:1]
        bosses = bosses[:1]
    if args.max_specs:
        specs = specs[: args.max_specs]
    if args.max_bosses:
        bosses = bosses[: args.max_bosses]

    database = build_database(
        specs=specs,
        bosses=bosses,
        fetcher=fetcher,
        delay_seconds=args.delay,
        existing=existing,
    )

    if args.write:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        if args.monolith:
            with args.output.open("w", encoding="utf-8") as handle:
                json.dump(database, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            print(f"Wrote monolithic {args.output} with {len(database['specs'])} specs")
        else:
            write_split_database(database, args.output)
            print(f"Wrote split {args.output} with {len(database['specs'])} specs")
    else:
        print(json.dumps(database, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except ScraperError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
