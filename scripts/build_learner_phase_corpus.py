#!/usr/bin/env python3
# Build journey-focused PRD; layout content/phases/<P*>/{index,modules,depth,supplement}. Manish.AI.
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_SRC = ROOT / "content" / "spec" / "agentiq_platform_spec.md"
RESEARCH_SRC = ROOT / "content" / "research" / "topic-and-extract-corpus.md"
PHASES_ROOT = ROOT / "content" / "phases"
CATEGORIES_DIR = ROOT / "content" / "categories"
OUT_PRD = ROOT / "docs" / "PRD_AgentIQ.md"

SECTION_HEAD = re.compile(r"^(## (\d+)\.\s)(.+)$", re.MULTILINE)
JUNK = re.compile(r"^wtmp begins", re.I)
SUB48 = re.compile(r"^### (48\.\d+)\s+(.+)$", re.MULTILINE)
DAY_LINE = re.compile(r"^\*\*Day (\d+) — .+$", re.MULTILINE)
MREF = re.compile(r"\bM(\d{1,3})\b", re.I)

TOPIC_LABELS: dict[int, str] = {
    27: "AI foundations and terminology",
    28: "Programming and scripting",
    29: "Prompt engineering depth",
    30: "LLMs and provider APIs",
    31: "AI agents",
    32: "Tool use and integration",
    33: "Agent frameworks",
    34: "RAG and knowledge systems",
    35: "Model Context Protocol",
    36: "Unified agentic systems",
    37: "Fine-tuning and optimization",
    38: "Local and edge inference",
    39: "AI-native development workflows",
    40: "Workflow automation",
    41: "Production deployment",
    42: "Monitoring and evaluation",
    43: "Security and governance",
    44: "Consulting and delivery",
    45: "Cloud platforms and credentials",
    46: "Additional tools and stacks",
    47: "Certification ROI and platform design",
    57: "Curriculum visual map — block A",
    58: "Curriculum visual map — block B",
    59: "Curriculum visual map — block C",
    60: "Curriculum visual map — block D",
    61: "Curriculum visual map — block E",
    62: "Curriculum visual map — block F",
    63: "Curriculum visual map — block G",
    64: "Curriculum visual map — block H",
}

SECTION_PHASES: dict[int, list[str]] = {
    27: ["P1"],
    28: ["P1"],
    29: ["P2"],
    30: ["P3"],
    31: ["P4"],
    32: ["P5"],
    33: ["P6"],
    34: ["P7"],
    35: ["P8"],
    36: ["P10"],
    37: ["P11"],
    38: ["P0"],
    39: ["P12"],
    40: ["P13"],
    41: ["P14"],
    42: ["P15"],
    43: ["P16"],
    44: ["P17"],
    45: ["P14", "P19"],
    46: ["P14"],
    47: ["P17", "P19"],
    57: ["P1"],
    58: ["P1"],
    59: ["P3"],
    60: ["P4"],
    61: ["P6"],
    62: ["P7"],
    63: ["P10"],
    64: ["P12"],
}

N1_DAY_PHASE: dict[int, str] = {
    1: "P1",
    2: "P11",
    3: "P14",
    4: "P14",
    5: "P14",
    6: "P1",
    7: "P1",
    8: "P2",
    9: "P7",
    10: "P15",
    11: "P16",
    12: "P14",
    13: "P4",
    14: "P6",
    15: "P6",
    16: "P5",
    17: "P6",
    18: "P15",
    19: "P10",
    20: "P17",
    21: "P18",
    22: "P18",
    23: "P18",
    24: "P18",
    25: "P18",
}

KW_PHASE: list[tuple[str, str]] = [
    ("rag", "P7"),
    ("vector", "P7"),
    ("embedding", "P7"),
    ("mcp", "P8"),
    ("a2a", "P9"),
    ("langgraph", "P6"),
    ("langchain", "P6"),
    ("crewai", "P6"),
    ("autogen", "P6"),
    ("prompt", "P2"),
    ("fine-tun", "P11"),
    ("lora", "P11"),
    ("ollama", "P0"),
    ("docker", "P14"),
    ("kubernetes", "P14"),
    ("fastapi", "P14"),
    ("streamlit", "P14"),
    ("n8n", "P13"),
    ("zapier", "P13"),
    ("governance", "P16"),
    ("injection", "P16"),
    ("rbac", "P16"),
    ("consultant", "P17"),
    ("certification", "P19"),
    ("azure", "P14"),
    ("aws", "P19"),
    ("google cloud", "P19"),
    ("observability", "P15"),
    ("langsmith", "P15"),
    ("evaluat", "P15"),
    ("agent", "P4"),
    ("tool use", "P5"),
    ("transformer", "P1"),
    ("llm", "P1"),
    ("claude code", "P12"),
    ("cursor", "P12"),
]

CRUFT_OPEN = re.compile(
    r"(?i)^(#{1,6}\s*)?(\d+\.\s*)?"
    r"(patch\b|final\s+gap|true\s+final|missing\s+items|"
    r"lines\s+\d+\s*[-–]\s*\d+|blueprint\s+docx|"
    r"remaining\s+coverage|final\s+items|final\s+patch|"
    r"extracted:\s*.*\(\s*lines\s+\d+)",
)


def journey_ids_from_csv(mod_phase: dict[str, dict]) -> dict[str, str]:
    """P0 → 0.1, 0.2, … ; P1 → 1.1, 1.2, … (position within phase)."""
    by_phase: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for key, row in mod_phase.items():
        by_phase[row["phase_code"]].append((int(key), key))
    for ph in by_phase:
        by_phase[ph].sort(key=lambda x: x[0])
    out: dict[str, str] = {}
    for i in range(20):
        ph = f"P{i}"
        phase_index = i
        for pos, (_num, k) in enumerate(by_phase.get(ph, []), start=1):
            out[k] = f"{phase_index}.{pos}"
    return out


def load_prd_sections() -> dict[int, str]:
    """§1–§26 (incl. §6 pointer) from spec; §27–§73 from research corpus — no duplicate curriculum body."""
    chunks: list[str] = []
    for path in (SPEC_SRC, RESEARCH_SRC):
        raw = path.read_text(encoding="utf-8")
        lines = [ln for ln in raw.splitlines() if not JUNK.search(ln)]
        chunks.append("\n".join(lines))
    text = "\n".join(chunks) + "\n"
    sections: dict[int, str] = {}
    for m in SECTION_HEAD.finditer(text):
        num = int(m.group(2))
        start = m.start()
        nxt = None
        for m2 in SECTION_HEAD.finditer(text, m.end()):
            nxt = m2.start()
            break
        end = nxt if nxt is not None else len(text)
        sections[num] = text[start:end].rstrip()
    return sections


def load_csv() -> tuple[dict[str, dict], dict[str, dict]]:
    phases: dict[str, dict] = {}
    with (ROOT / "input" / "phases.csv").open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            phases[row["phase_code"]] = row
    mod_phase: dict[str, dict] = {}
    with (ROOT / "input" / "modules.csv").open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            mod_phase[row["module_num"]] = row
    return phases, mod_phase


def strip_yaml_front(s: str) -> str:
    if s.startswith("---\n"):
        end = s.find("\n---\n", 3)
        if end != -1:
            return s[end + 5 :].lstrip()
    return s


def score_phase_for_text(text: str) -> str:
    low = text.lower()
    best_p, best_n = "P17", 0
    for kw, ph in KW_PHASE:
        c = low.count(kw)
        if c > best_n:
            best_n, best_p = c, ph
    return best_p if best_n else "P17"


def demote_merged_headings(text: str) -> str:
    out: list[str] = []
    for ln in text.splitlines():
        if re.match(r"^## \d+\.", ln):
            out.append("#### " + ln[3:])
        elif ln.startswith("## ") and not ln.startswith("###"):
            out.append("### " + ln[3:])
        else:
            out.append(ln)
    return "\n".join(out)


def strip_first_numbered_heading(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return text
    if re.match(r"^#{2,6}\s*\d+\.\s", lines[0]):
        return "\n".join(lines[1:]).lstrip("\n")
    return text


def filter_cruft_paragraphs(text: str) -> str:
    out: list[str] = []
    for para in re.split(r"\n\n+", text):
        p = para.strip()
        if not p:
            continue
        first = p.split("\n", 1)[0]
        if CRUFT_OPEN.search(first):
            continue
        if re.search(r"(?i)patch\s*—\s*lines\s+\d+", first):
            continue
        out.append(p)
    return "\n\n".join(out)


def strip_trailing_horizontal_rules(text: str) -> str:
    t = text.rstrip()
    while True:
        if t.endswith("---"):
            t = t[:-3].rstrip()
            continue
        m = re.search(r"\n\n---\s*$", t)
        if m:
            t = t[: m.start()].rstrip()
            continue
        break
    return t


def clean_block(text: str) -> str:
    t = demote_merged_headings(text)
    t = strip_first_numbered_heading(t)
    t = filter_cruft_paragraphs(t).strip()
    return strip_trailing_horizontal_rules(t)


def scrub_legacy_heading_numbers(text: str) -> str:
    """Turn `### 57.2 Title` into `### Title` so depth files use journey-friendly headings."""
    out: list[str] = []
    for ln in text.splitlines():
        ln2 = re.sub(r"^(#{1,6})\s*\d+\.\d+[a-z]?\s+", r"\1 ", ln)
        ln2 = re.sub(r"^(#{1,6})\s*\d{1,2}\.\d{1,2}\s+", r"\1 ", ln2)
        out.append(ln2)
    return "\n".join(out)


def route_section_48(
    body: str,
    phase_depth: dict[str, list[str]],
    hack_chunks: list[str],
    yc_chunks: list[str],
) -> None:
    matches = list(SUB48.finditer(body))
    for i, m in enumerate(matches):
        label = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        raw = body[start:end].strip()
        chunk = scrub_legacy_heading_numbers(clean_block(raw))
        if not chunk:
            continue
        if label == "48.1":
            continue
        if label == "48.2":
            phase_depth["P1"].append("### Core concept refresher\n\n" + chunk + "\n")
        elif label == "48.3":
            phase_depth["P18"].append("### Portfolio capstone specifications\n\n" + chunk + "\n")
        elif label == "48.4":
            hack_chunks.append("### Hackathon judging patterns\n\n" + chunk + "\n")
        elif label == "48.5":
            yc_chunks.append("### Startup idea catalog\n\n" + chunk + "\n")


def route_section_66(body: str, phase_depth: dict[str, list[str]], hack_chunks: list[str]) -> None:
    if "### 66.1" in body:
        pre = body.split("### 66.2", 1)[0].strip()
        c = scrub_legacy_heading_numbers(clean_block(pre))
        if c:
            hack_chunks.append("### Multi-week sprint and hackathon format\n\n" + c + "\n")
    rest = ""
    if "### 66.3" in body:
        rest = body.split("### 66.3", 1)[1]
    for m in DAY_LINE.finditer(rest):
        day = int(m.group(1))
        start = m.start()
        nxt = DAY_LINE.search(rest, m.end())
        end = nxt.start() if nxt else len(rest)
        para = rest[start:end].strip()
        ph = N1_DAY_PHASE.get(day, score_phase_for_text(para))
        phase_depth[ph].append(f"### Syllabus theme — day {day}\n\n{para}\n")


def route_section_67(body: str, phase_depth: dict[str, list[str]]) -> None:
    if "### 67.1" in body:
        _, _, after1 = body.partition("### 67.1")
        if "### 67.2" in after1:
            b1, _, after2 = after1.partition("### 67.2")
            c1, c2 = clean_block(b1), clean_block(after2)
            c1, c2 = scrub_legacy_heading_numbers(c1), scrub_legacy_heading_numbers(c2)
            if c1:
                phase_depth["P14"].append("### Cloud and data engineering patterns\n\n" + c1 + "\n")
            if c2:
                phase_depth["P12"].append("### AI-native IDE and API mastery\n\n" + c2 + "\n")
        else:
            c = scrub_legacy_heading_numbers(clean_block(after1))
            if c:
                phase_depth["P14"].append("### Cloud and data engineering patterns\n\n" + c + "\n")
    elif "### 67.2" in body:
        _, _, after2 = body.partition("### 67.2")
        c2 = scrub_legacy_heading_numbers(clean_block(after2))
        if c2:
            phase_depth["P12"].append("### AI-native IDE and API mastery\n\n" + c2 + "\n")


def route_by_module_refs(
    text: str,
    mod_phase: dict[str, dict],
    phase_depth: dict[str, list[str]],
    module_depth: dict[int, list[str]],
) -> None:
    paras = re.split(r"\n\n+", text)
    for p in paras:
        p = p.strip()
        if len(p) < 40:
            continue
        first = p.split("\n", 1)[0]
        if CRUFT_OPEN.search(first):
            continue
        ms = [int(x) for x in MREF.findall(p)]
        body = scrub_legacy_heading_numbers(clean_block(p))
        if not body:
            continue
        if not ms:
            ph = score_phase_for_text(p)
            phase_depth[ph].append(body + "\n\n")
            continue
        for n in ms:
            if str(n) in mod_phase:
                module_depth[n].append(body + "\n\n")


def part_e_markdown() -> str:
    """Links to platform FRs, agents, and flows (core differentiator detail)."""
    return """
---

## Part E — Platform specification (flows & requirements)

Part A states **core differentiators**; this part points to where each is **specified** (functional requirements, agents, and UX).

| Topic | Document |
|-------|----------|
| Vision & learner/admin personas | [`content/platform/vision-and-personas.md`](../content/platform/vision-and-personas.md) |
| Platform features — auth (incl. AI labeling), dashboard, navigation, module page, **topic feedback**, improvement suggestions, progress, certifications UI, capstones | [`content/platform/platform-features.md`](../content/platform/platform-features.md) |
| Gamification — levels L1–L10, XP, badges, streaks, leaderboards | [`content/platform/gamification.md`](../content/platform/gamification.md) |
| **AI agent system** — registry (content, feedback, news, triage, …), transparency rules, observability | [`content/platform/ai-agents.md`](../content/platform/ai-agents.md) |
| Enterprise & **multi-tenant** model | [`content/platform/enterprise-tenant.md`](../content/platform/enterprise-tenant.md) |
| **AI chatbot** (course navigator) | [`content/platform/ai-chatbot.md`](../content/platform/ai-chatbot.md) |
| **AI news feed** | [`content/platform/ai-news-feed.md`](../content/platform/ai-news-feed.md) |
| Notification system | [`content/platform/notifications.md`](../content/platform/notifications.md) |
| Admin & tenant admin panel | [`content/platform/admin-panel.md`](../content/platform/admin-panel.md) |
| Technical architecture | [`content/platform/technical-architecture.md`](../content/platform/technical-architecture.md) |
| **Content versioning & dynamic completion** (extends Part A learning model) | [`content/platform/content-versioning.md`](../content/platform/content-versioning.md) |
| Personalization & adaptive learning | [`content/platform/personalization.md`](../content/platform/personalization.md) |
| Certifications, capstones, catalogs, NFRs, metrics, roadmap (§18–§26) | [`content/platform/catalogs-and-roadmap.md`](../content/platform/catalogs-and-roadmap.md) |

**Layered specification (no duplicate curriculum text):**
- Platform + catalogs **§1–§5, §6 (pointer), §7–§26:** [`content/spec/agentiq_platform_spec.md`](../content/spec/agentiq_platform_spec.md)
- **§6 module archive** (split source): [`content/curriculum/section-6-modules.md`](../content/curriculum/section-6-modules.md)
- **§27–§73** topic / extract corpus: [`content/research/topic-and-extract-corpus.md`](../content/research/topic-and-extract-corpus.md)

**Canonical delivery** (per-module bodies): [`content/phases/`](../content/phases/) — `P*/modules/*.md`, plus `supplement.md` / `depth/` where generated.
"""


def part_a_context(sections: dict[int, str]) -> str:
    parts: list[str] = []
    for sn, heading in ((1, "Executive summary"), (2, "Problem statement"), (5, "Learning model")):
        if sn not in sections:
            continue
        # Manish.AI: strip spec-style ### 5.1 … so Part A headings match PRD structure (not legacy § numbers).
        body = scrub_legacy_heading_numbers(clean_block(sections[sn]))
        if body:
            parts.append(f"### {heading}\n\n{body}")
    return "\n\n---\n\n".join(parts)


def module_core_path(num: int, phase_code: str) -> Path | None:
    d = PHASES_ROOT / phase_code / "modules"
    paths = sorted(d.glob(f"m{num:03d}-*.md"))
    return paths[0] if paths else None


def module_file_link(
    num: int,
    phase_code: str,
    *,
    prd_href: bool,
) -> str:
    rel_repo = f"content/phases/{phase_code}/modules/m{num:03d}-*.md"
    p = module_core_path(num, phase_code)
    if not p:
        return f"`{rel_repo}` _(run `python3 scripts/split_modules_one_file_each.py`)_"
    name = p.name
    if prd_href:
        href = f"../content/phases/{phase_code}/modules/{name}"
    else:
        href = f"modules/{name}"
    display = f"content/phases/{phase_code}/modules/{name}"
    return f"[`{display}`]({href})"


def first_module_depth_example(
    mods: list[dict], module_depth_nonempty: set[int], mod_phase: dict[str, dict]
) -> tuple[int, str] | None:
    for r in mods:
        n = int(r["module_num"])
        if n in module_depth_nonempty:
            ph = mod_phase[str(n)]["phase_code"]
            return (n, ph)
    return None


def render_phase_outline(
    pcode: str,
    prow: dict,
    mods: list[dict],
    journey: dict[str, str],
    mod_phase: dict[str, dict],
    module_depth_nonempty: set[int],
    *,
    prd_href: bool,
) -> str:
    """Slim phase document: index table + pointers to modules/ and depth/."""
    lines: list[str] = [
        f"# Phase {pcode} — {prow['name']}\n\n",
        f"**Purpose:** {prow['purpose']}\n\n",
        "## Module index\n\n",
        "Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.\n\n",
        "| Journey | Catalog # | Title | Priority | Core content |\n",
        "|---------|------------|-------|----------|----------------|\n",
    ]
    for r in mods:
        n = int(r["module_num"])
        ph = r["phase_code"]
        jid = journey.get(r["module_num"], "?")
        title = r["title"].replace("|", "\\|")
        core = module_file_link(n, ph, prd_href=prd_href)
        lines.append(f"| `{jid}` | {n} | {title} | {r['priority']} | {core} |\n")

    lines.append("\n## Extended depth\n\n")
    if prd_href:
        sup_href = f"../content/phases/{pcode}/supplement.md"
    else:
        sup_href = "supplement.md"
    lines.append(
        f"- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`]({sup_href}) "
        f"— present only when material was routed to this phase.\n"
    )
    ex = first_module_depth_example(mods, module_depth_nonempty, mod_phase)
    if ex:
        n, mph = ex
        if prd_href:
            dhref = f"../content/phases/{mph}/depth/m{n:03d}.md"
        else:
            dhref = f"depth/m{n:03d}.md" if mph == pcode else f"../{mph}/depth/m{n:03d}.md"
        lines.append(
            f"- **Per-module** addenda (when the source cites catalog ids): e.g. [`m{n:03d}.md`]({dhref}).\n"
        )
    else:
        lines.append(
            "- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).\n"
        )
    return "".join(lines)


def clear_phase_supplements() -> None:
    for i in range(20):
        pc = f"P{i}"
        sup = PHASES_ROOT / pc / "supplement.md"
        if sup.exists():
            sup.unlink()
        dd = PHASES_ROOT / pc / "depth"
        if dd.is_dir():
            for p in dd.glob("m*.md"):
                p.unlink()
    CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)
    for name in ("hackathons.md", "startup-ideas.md"):
        p = CATEGORIES_DIR / name
        if p.exists():
            p.unlink()


def write_supplement_files(
    phase_depth: dict[str, list[str]],
    module_depth: dict[int, list[str]],
    hack_chunks: list[str],
    yc_chunks: list[str],
    mod_phase: dict[str, dict],
) -> None:
    clear_phase_supplements()
    for pcode, chunks in phase_depth.items():
        if not chunks:
            continue
        base = PHASES_ROOT / pcode
        base.mkdir(parents=True, exist_ok=True)
        (base / "modules").mkdir(exist_ok=True)
        (base / "depth").mkdir(exist_ok=True)
        body = "\n".join(chunks)
        text = (
            "---\n"
            f"kind: phase_supplement\n"
            f"phase_code: {pcode}\n"
            "---\n\n"
            f"# Phase {pcode} — supplemental depth\n\n" + body
        )
        (base / "supplement.md").write_text(text, encoding="utf-8")

    for n, chunks in sorted(module_depth.items()):
        if not chunks:
            continue
        pcode = mod_phase[str(n)]["phase_code"]
        base = PHASES_ROOT / pcode
        (base / "depth").mkdir(parents=True, exist_ok=True)
        body = "\n".join(chunks)
        text = (
            "---\n"
            f"kind: module_supplement\n"
            f"module_num: {n}\n"
            "---\n\n"
            f"# Catalog module {n} — supplemental depth\n\n" + body
        )
        (base / "depth" / f"m{n:03d}.md").write_text(text, encoding="utf-8")

    if hack_chunks:
        h = (
            "---\nkind: category_supplement\ntitle: Hackathons\n---\n\n"
            "# Hackathons — supplemental depth\n\n" + "\n".join(hack_chunks)
        )
        (CATEGORIES_DIR / "hackathons.md").write_text(h, encoding="utf-8")

    if yc_chunks:
        y = (
            "---\nkind: category_supplement\ntitle: Startup ideas\n---\n\n"
            "# Startup ideas — supplemental depth\n\n" + "\n".join(yc_chunks)
        )
        (CATEGORIES_DIR / "startup-ideas.md").write_text(y, encoding="utf-8")


def main() -> None:
    sections = load_prd_sections()
    phases, mod_phase = load_csv()
    journey = journey_ids_from_csv(mod_phase)

    phase_depth: dict[str, list[str]] = defaultdict(list)
    module_depth: dict[int, list[str]] = defaultdict(list)
    hack_chunks: list[str] = []
    yc_chunks: list[str] = []

    for sn, ph_list in SECTION_PHASES.items():
        if sn not in sections:
            continue
        label = TOPIC_LABELS.get(sn, "Extended topics")
        body = scrub_legacy_heading_numbers(clean_block(sections[sn]))
        if not body:
            continue
        for ph in ph_list:
            phase_depth[ph].append(f"### {label}\n\n{body}\n")

    if 48 in sections:
        route_section_48(sections[48], phase_depth, hack_chunks, yc_chunks)

    for sn in (65, 66, 67, 68):
        if sn not in sections:
            continue
        body = sections[sn]
        if sn == 66:
            route_section_66(body, phase_depth, hack_chunks)
        elif sn == 67:
            route_section_67(body, phase_depth)
        else:
            route_by_module_refs(body, mod_phase, phase_depth, module_depth)

    if 69 in sections:
        c = scrub_legacy_heading_numbers(clean_block(sections[69]))
        if c:
            hack_chunks.append("### Competition and hackathon notes\n\n" + c + "\n")

    if 70 in sections:
        route_by_module_refs(sections[70], mod_phase, phase_depth, module_depth)

    write_supplement_files(phase_depth, module_depth, hack_chunks, yc_chunks, mod_phase)

    module_depth_nonempty = {k for k, v in module_depth.items() if v}
    phase_order = [f"P{i}" for i in range(20)]
    for pcode in phase_order:
        prow = phases[pcode]
        mods = [row for _, row in sorted(mod_phase.items(), key=lambda x: int(x[0])) if row["phase_code"] == pcode]
        body = render_phase_outline(
            pcode,
            prow,
            mods,
            journey,
            mod_phase,
            module_depth_nonempty,
            prd_href=False,
        )
        base = PHASES_ROOT / pcode
        base.mkdir(parents=True, exist_ok=True)
        (base / "modules").mkdir(exist_ok=True)
        (base / "depth").mkdir(exist_ok=True)
        idx = (
            "---\n"
            f"phase_code: {pcode}\n"
            f"title: {prow['name']}\n"
            "---\n\n" + body
        )
        (base / "index.md").write_text(idx, encoding="utf-8")

    intro = (
        "# AgentIQ — Product and learning specification\n\n"
        "AgentIQ is an AI-native learning platform with a **living curriculum**. Learners move through **phases P0–P19** using **journey module ids** "
        "(`0.1`, `1.2`, … = phase index · order within phase). **What to study and in what order** is below. **Full module bodies** live under "
        "[`content/phases/<P*>/modules/`](../content/phases/P0/modules/) (see each phase’s **index** and **Extended depth** links).\n\n"
        "---\n\n"
        "## Part A — Context\n\n"
        + part_a_context(sections)
        + "\n\n---\n\n## Part B — Curriculum by phase\n\n"
    )

    prd_body: list[str] = [intro]
    for pcode in phase_order:
        prow = phases[pcode]
        mods = [row for _, row in sorted(mod_phase.items(), key=lambda x: int(x[0])) if row["phase_code"] == pcode]
        prd_body.append(
            render_phase_outline(
                pcode,
                prow,
                mods,
                journey,
                mod_phase,
                module_depth_nonempty,
                prd_href=True,
            )
            + "\n\n---\n\n"
        )

    prd_body.append(
        "## Part C — Hackathons\n\n"
        "Narratives, judging patterns, and competition notes: "
        "[`content/categories/hackathons.md`](../content/categories/hackathons.md).\n\n"
        "---\n\n"
        "## Part D — Startup ideas\n\n"
        "Extended idea specs: [`content/categories/startup-ideas.md`](../content/categories/startup-ideas.md).\n"
    )

    prd_body.append(part_e_markdown())

    OUT_PRD.parent.mkdir(parents=True, exist_ok=True)
    OUT_PRD.write_text("".join(prd_body), encoding="utf-8")
    print(f"Wrote {OUT_PRD}, {PHASES_ROOT}/P*/index.md, supplements, {CATEGORIES_DIR}/")


if __name__ == "__main__":
    main()
