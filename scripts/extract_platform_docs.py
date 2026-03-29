#!/usr/bin/env python3
# Slice numbered sections from slim content/spec/agentiq_platform_spec.md → content/platform/*. Manish.AI.
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "content" / "spec" / "agentiq_platform_spec.md"
OUT = ROOT / "content" / "platform"

SECTION = re.compile(r"^## (\d+)\.\s", re.MULTILINE)

HEADER = (
    "<!-- Extracted from content/spec/agentiq_platform_spec.md — run: "
    "python3 scripts/extract_platform_docs.py — Manish.AI -->\n\n"
)

OUTPUT_MAP: dict[str, tuple[int, ...]] = {
    "vision-and-personas.md": (3, 4),
    "platform-features.md": (7,),
    "gamification.md": (8,),
    "ai-agents.md": (9,),
    "enterprise-tenant.md": (10,),
    "ai-chatbot.md": (11,),
    "ai-news-feed.md": (12,),
    "notifications.md": (13,),
    "admin-panel.md": (14,),
    "technical-architecture.md": (15,),
    "content-versioning.md": (16,),
    "personalization.md": (17,),
}


def split_sections(text: str) -> dict[int, str]:
    matches = list(SECTION.finditer(text))
    out: dict[int, str] = {}
    for i, m in enumerate(matches):
        num = int(m.group(1))
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[num] = text[start:end].strip()
    return out


def main() -> None:
    text = SPEC.read_text(encoding="utf-8")
    sec = split_sections(text)
    OUT.mkdir(parents=True, exist_ok=True)

    for fname, nums in OUTPUT_MAP.items():
        parts = []
        for n in nums:
            if n not in sec:
                raise SystemExit(f"Missing section ## {n}. in slim spec (needed for {fname})")
            parts.append(sec[n])
        body = "\n\n---\n\n".join(parts) + "\n"
        (OUT / fname).write_text(HEADER + body, encoding="utf-8")

    # Optional extended catalogs (§18–§26) — single file for certifications, capstones, NFRs, etc.
    extended_nums = list(range(18, 27))
    if all(n in sec for n in extended_nums):
        parts2 = [sec[n] for n in extended_nums]
        (OUT / "catalogs-and-roadmap.md").write_text(
            HEADER + "\n\n---\n\n".join(parts2) + "\n",
            encoding="utf-8",
        )

    print(f"Wrote {len(OUTPUT_MAP)} core files + optional catalogs to {OUT}")


if __name__ == "__main__":
    main()
