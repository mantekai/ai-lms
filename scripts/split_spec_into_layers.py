#!/usr/bin/env python3
# One-time / maintenance: split a MONOLITHIC agentiq_platform_spec (with ## 6 … ## 7 … ## 27) into layers.
# Do not run on an already-slim spec (missing ## 27). Manish.AI.
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "content" / "spec" / "agentiq_platform_spec.md"
CUR = ROOT / "content" / "curriculum" / "section-6-modules.md"
RES = ROOT / "content" / "research" / "topic-and-extract-corpus.md"

SECTION = re.compile(r"^## (\d+)\.\s", re.MULTILINE)


def find_start(text: str, n: int) -> int | None:
    for m in SECTION.finditer(text):
        if int(m.group(1)) == n:
            return m.start()
    return None


def main() -> None:
    text = MONO.read_text(encoding="utf-8")
    p6, p7, p27 = find_start(text, 6), find_start(text, 7), find_start(text, 27)
    if p6 is None or p7 is None or p27 is None:
        raise SystemExit("Expected ## 6., ## 7., and ## 27. in agentiq_platform_spec.md")

    head = text[:p6].rstrip() + "\n\n"
    curriculum = text[p6:p7].rstrip() + "\n"
    platform = text[p7:p27].rstrip() + "\n"
    research = text[p27:].lstrip()

    stub = (
        "## 6. FULL CURRICULUM SPECIFICATION\n\n"
        "Canonical **per-module** bodies live under **`content/phases/P*/modules/*.md`**.\n\n"
        "A **single-file §6 archive** (for splitting and auditing): [`content/curriculum/section-6-modules.md`](../curriculum/section-6-modules.md). "
        "After editing it, run `python3 scripts/split_modules_one_file_each.py`.\n\n"
        "Research and topic depth (**former §27–§73**): [`content/research/topic-and-extract-corpus.md`](../research/topic-and-extract-corpus.md). "
        "Regenerate `supplement.md` / `depth/` with `python3 scripts/build_learner_phase_corpus.py`.\n\n"
        "---\n\n"
    )

    new_spec = head + stub + platform

    CUR.parent.mkdir(parents=True, exist_ok=True)
    RES.parent.mkdir(parents=True, exist_ok=True)
    CUR.write_text(curriculum, encoding="utf-8")
    RES.write_text(research, encoding="utf-8")
    MONO.write_text(new_spec, encoding="utf-8")
    print(f"Wrote {CUR.name} ({len(curriculum):,} chars)")
    print(f"Wrote {RES.name} ({len(research):,} chars)")
    print(f"Slim {MONO.name} ({len(new_spec):,} chars)")


if __name__ == "__main__":
    main()
