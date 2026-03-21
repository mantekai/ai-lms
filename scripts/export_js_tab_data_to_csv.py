#!/usr/bin/env python3
# Manish.AI — One-shot export: parse platform_logic.js tab arrays → data/catalog/*.csv
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JS = (ROOT / "platform_logic.js").read_text(encoding="utf-8")
OUT = ROOT / "data" / "catalog"
OUT.mkdir(parents=True, exist_ok=True)


def sq(s: str) -> str:
    """Unescape JS single-quoted string contents."""
    if not s:
        return ""
    return s.replace("\\'", "'").replace("\\n", "\n")


def re_str(key: str, block: str) -> str:
    m = re.search(rf"{key}:\s*'((?:\\.|[^'\\])*)'", block)
    return sq(m.group(1)) if m else ""


def split_js_objects(array_body: str) -> list[str]:
    inner = array_body.strip()
    if inner.startswith("["):
        inner = inner[1:]
    if inner.rstrip().endswith("]"):
        inner = inner.rstrip()[:-1]
    parts = re.split(r"\},\s*\n\s*\{", inner)
    out = []
    for i, p in enumerate(parts):
        p = p.strip()
        if not p.startswith("{"):
            p = "{" + p
        if not p.endswith("}"):
            p = p + "}"
        out.append(p)
    return out


def extract_array(name: str) -> str:
    m = re.search(rf"const {name} = (\[[\s\S]*?\n\]);", JS)
    if not m:
        raise SystemExit(f"array {name} not found")
    return m.group(1)


def export_certs() -> None:
    body = extract_array("CERT_DEFS")
    blocks = split_js_objects(body)
    path = OUT / "certs.csv"
    fields = ["id", "provider", "name", "url", "price", "kind", "studyPhases", "note"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for b in blocks:
            w.writerow({k: re_str(k, b) for k in fields})
    print("wrote", path, "rows", len(blocks))


def export_nav_pages() -> None:
    path = OUT / "nav_pages.csv"
    rows = [
        ("dashboard", "Dashboard", "🏠", "1"),
        ("coverage", "Topic coverage", "📋", "2"),
        ("modules", "All Phases", "📚", "3"),
        ("capstone", "Capstones", "🚀", "4"),
        ("hackathons", "Hackathons", "⚡", "5"),
        ("opensource", "Open Source", "📦", "6"),
        ("yc", "YC Ideas", "💡", "7"),
        ("certs", "Cert Tracker", "🎓", "8"),
        ("career", "Career", "💼", "9"),
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["page_id", "label", "icon", "sort_order"])
        w.writeheader()
        for r in rows:
            w.writerow(dict(zip(["page_id", "label", "icon", "sort_order"], r)))
    print("wrote", path)


def export_hackathons() -> None:
    body = extract_array("HACKATHONS")
    blocks = split_js_objects(body)
    path = OUT / "hackathons.csv"
    fields = [
        "icon",
        "title",
        "org",
        "prize",
        "deadline",
        "theme",
        "prep",
        "template",
        "winners",
        "desc",
        "link",
        "meta",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for b in blocks:
            row = {k: re_str(k, b) for k in fields if k != "meta"}
            mm = re.search(r"meta:\s*\[([^\]]*)\]", b, re.S)
            meta_s = ""
            if mm:
                meta_s = re.sub(r"\s+", " ", mm.group(1)).strip()
            row["meta"] = meta_s
            w.writerow(row)
    print("wrote", path, "rows", len(blocks))


def export_opensource() -> None:
    body = extract_array("OPENSOURCE")
    blocks = split_js_objects(body)
    path = OUT / "opensource.csv"
    fields = ["icon", "title", "org", "diff", "desc", "tags", "link"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for b in blocks:
            row = {k: re_str(k, b) for k in fields if k != "tags"}
            tm = re.search(r"tags:\s*\[([^\]]*)\]", b)
            tags_s = ""
            if tm:
                tags_s = re.sub(r"['\"\s,]+", ";", tm.group(1)).strip(";")
            row["tags"] = tags_s
            w.writerow(row)
    print("wrote", path, "rows", len(blocks))


def export_yc() -> None:
    body = extract_array("YC_IDEAS")
    blocks = split_js_objects(body)
    path = OUT / "yc_ideas.csv"
    fields = ["title", "problem", "solution", "stack", "market", "mvp"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for b in blocks:
            w.writerow({k: re_str(k, b) for k in fields})
    print("wrote", path, "rows", len(blocks))


def export_capstones() -> None:
    body = extract_array("CAPSTONES")
    blocks = split_js_objects(body)
    cap_path = OUT / "capstones.csv"
    step_path = OUT / "capstone_steps.csv"
    cfields = ["id", "title", "subtitle", "difficulty", "time", "desc", "why", "github", "stack"]
    sfields = ["capstone_id", "step_n", "title", "description"]
    with cap_path.open("w", newline="", encoding="utf-8") as fc, step_path.open(
        "w", newline="", encoding="utf-8"
    ) as fs:
        cw = csv.DictWriter(fc, fieldnames=cfields)
        sw = csv.DictWriter(fs, fieldnames=sfields)
        cw.writeheader()
        sw.writeheader()
        for b in blocks:
            cid = re_str("id", b)
            row = {k: re_str(k, b) for k in cfields if k not in ("id", "stack")}
            row["id"] = cid
            sm = re.search(r"stack:\s*\[([^\]]*)\]", b)
            stack_s = ""
            if sm:
                stack_s = ";".join(re.findall(r"'([^']*)'", sm.group(1)))
            row["stack"] = stack_s
            cw.writerow(row)
            arch = re.search(r"arch:\s*\[([\s\S]*?)\]\s*,", b)
            if arch:
                inner = arch.group(1)
                steps = re.findall(
                    r"\{\s*n:\s*'([^']*)',\s*title:\s*'((?:\\.|[^'\\])*)',\s*desc:\s*'((?:\\.|[^'\\])*)'\s*\}",
                    inner,
                )
                for n, tit, des in steps:
                    sw.writerow(
                        {
                            "capstone_id": cid,
                            "step_n": sq(n),
                            "title": sq(tit),
                            "description": sq(des),
                        }
                    )
    print("wrote", cap_path, len(blocks), "and", step_path)


def main() -> None:
    export_certs()
    export_nav_pages()
    export_hackathons()
    export_opensource()
    export_yc()
    # capstones.csv + capstone_steps.csv are maintained by hand (nested arch breaks naive split)


if __name__ == "__main__":
    main()
