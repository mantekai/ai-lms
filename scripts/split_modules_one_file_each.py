#!/usr/bin/env python3
# Emit one Markdown file per curriculum module under content/phases/<P*>/modules/. Manish.AI.
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "content" / "curriculum" / "section-6-modules.md"
CSV_PATH = ROOT / "input" / "modules.csv"
PHASES_ROOT = ROOT / "content" / "phases"

MODULE_LINE = re.compile(r"^\*\*Module (\d+): (.+)$", re.MULTILINE)


def slugify(s: str, max_len: int = 50) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower())
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    return s[:max_len].rstrip("-") or "module"


def journey_ids_from_rows(rows: dict[int, dict]) -> dict[int, str]:
    by_phase: dict[str, list[int]] = defaultdict(list)
    for num, r in rows.items():
        by_phase[r["phase_code"]].append(num)
    for ph in by_phase:
        by_phase[ph].sort()
    out: dict[int, str] = {}
    for i in range(20):
        ph = f"P{i}"
        phase_index = i
        for pos, num in enumerate(by_phase.get(ph, []), start=1):
            out[num] = f"{phase_index}.{pos}"
    return out


def clear_phase_module_files() -> None:
    for i in range(20):
        d = PHASES_ROOT / f"P{i}" / "modules"
        if d.is_dir():
            for p in d.glob("m*.md"):
                p.unlink()


def main() -> None:
    chunk = CURRICULUM.read_text(encoding="utf-8")
    if "## 6." not in chunk and "**Module 1:" not in chunk:
        raise SystemExit(f"Invalid curriculum file: {CURRICULUM}")

    rows: dict[int, dict] = {}
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            rows[int(r["module_num"])] = r

    journey = journey_ids_from_rows(rows)

    matches = list(MODULE_LINE.finditer(chunk))
    if len(matches) != 133:
        raise SystemExit(f"Expected 133 module headers, found {len(matches)}")

    PHASES_ROOT.mkdir(parents=True, exist_ok=True)
    clear_phase_module_files()

    for i, m in enumerate(matches):
        num = int(m.group(1))
        title_rest = m.group(2).strip()
        title_short = title_rest.split("[")[0].split("|")[0].strip().removesuffix("**").strip()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(chunk)
        body = chunk[m.start() : end].rstrip() + "\n"
        jid = journey.get(num, "?")
        body = re.sub(
            rf"^\*\*Module {num}:\s*",
            f"**{jid} — ",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        meta = rows.get(num, {})
        phase = meta.get("phase_code", "")
        if not phase:
            raise SystemExit(f"module_num {num} missing phase_code in modules.csv")
        tools = meta.get("tools", "")
        pri = meta.get("priority", "")
        fname = f"m{num:03d}-{slugify(title_short)}.md"
        mod_dir = PHASES_ROOT / phase / "modules"
        mod_dir.mkdir(parents=True, exist_ok=True)
        header = (
            "---\n"
            f"journey_id: {jid!r}\n"
            f"module_num: {num}\n"
            f"phase_code: {phase}\n"
            f"title: {title_short!r}\n"
            f"tools: {tools!r}\n"
            f"priority: {pri!r}\n"
            "source: content/curriculum/section-6-modules.md\n"
            "---\n\n"
            f"# {jid} — {title_short}\n\n"
        )
        (mod_dir / fname).write_text(header + body, encoding="utf-8")

    print(f"Wrote 133 files under {PHASES_ROOT}/P*/modules/")


if __name__ == "__main__":
    main()
