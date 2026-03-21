# Manish.AI — CSV catalog I/O for phases + modules (human-editable source of truth).
"""Load phase and module rows from data/catalog/*.csv; bootstrap files from legacy tuples if missing."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATALOG_DIR = ROOT / "data" / "catalog"
PHASES_CSV = CATALOG_DIR / "phases.csv"
MODULES_CSV = CATALOG_DIR / "modules.csv"


def _bootstrap_catalog_from_legacy(
    phase_meta: list[tuple], rows: list[tuple[str, str, str]]
) -> None:
    """Write phases.csv + modules.csv from in-memory PHASE_META + ROWS (module order 1..133)."""
    CATALOG_DIR.mkdir(parents=True, exist_ok=True)
    with PHASES_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["phase_code", "name", "purpose", "icon", "color", "module_count"],
        )
        w.writeheader()
        for code, name, purpose, icon, color, count in phase_meta:
            w.writerow(
                {
                    "phase_code": code,
                    "name": name,
                    "purpose": purpose,
                    "icon": icon,
                    "color": color,
                    "module_count": count,
                }
            )
    flat: list[tuple[str, str, str, str, str]] = []
    idx = 0
    for code, _, _, _, _, count in phase_meta:
        for _ in range(count):
            title, tools, pri = rows[idx]
            flat.append((str(idx + 1), code, title, tools, pri))
            idx += 1
    assert idx == len(rows) == 133
    with MODULES_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["module_num", "phase_code", "title", "tools", "priority"],
        )
        w.writeheader()
        for num, code, title, tools, pri in flat:
            w.writerow(
                {
                    "module_num": num,
                    "phase_code": code,
                    "title": title,
                    "tools": tools,
                    "priority": pri,
                }
            )


def load_phase_meta_from_csv() -> list[tuple[str, str, str, str, str, int]]:
    """Return PHASE_META-shaped tuples from phases.csv (includes module_count)."""
    with PHASES_CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out: list[tuple[str, str, str, str, str, int]] = []
    for r in rows:
        out.append(
            (
                r["phase_code"].strip(),
                r["name"].strip(),
                r["purpose"].strip(),
                r["icon"].strip(),
                r["color"].strip(),
                int(r["module_count"].strip()),
            )
        )
    return out


def load_rows_from_csv() -> list[tuple[str, str, str]]:
    """Return (title, tools, priority) in module_num order."""
    with MODULES_CSV.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    rows.sort(key=lambda r: int(r["module_num"].strip()))
    return [(r["title"].strip(), r["tools"].strip(), r["priority"].strip()) for r in rows]


def validate_catalog(
    phase_meta: list[tuple[str, str, str, str, str, int]],
    rows: list[tuple[str, str, str]],
) -> None:
    if sum(p[5] for p in phase_meta) != len(rows):
        raise ValueError("phase module_count sum must equal number of module rows")
    if len(rows) != 133:
        raise ValueError(f"expected 133 modules, got {len(rows)}")
    with MODULES_CSV.open(encoding="utf-8") as f:
        mod_rows = list(csv.DictReader(f))
    counts = Counter(r["phase_code"].strip() for r in mod_rows)
    for code, _, _, _, _, expected in phase_meta:
        if counts.get(code, 0) != expected:
            raise ValueError(f"phase {code}: csv has {counts.get(code,0)} modules, expected {expected}")


def ensure_catalog_or_bootstrap(
    legacy_phase_meta: list[tuple],
    legacy_rows: list[tuple[str, str, str]],
) -> tuple[list[tuple[str, str, str, str, str, int]], list[tuple[str, str, str]]]:
    """If CSV catalog missing, create it from legacy tuples; then load and validate."""
    if not PHASES_CSV.exists() or not MODULES_CSV.exists():
        _bootstrap_catalog_from_legacy(legacy_phase_meta, legacy_rows)
    phase_meta = load_phase_meta_from_csv()
    rows = load_rows_from_csv()
    validate_catalog(phase_meta, rows)
    return phase_meta, rows
