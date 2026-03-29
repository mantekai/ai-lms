#!/usr/bin/env python3
# Rebuild structured content from content/spec + input CSVs. Manish.AI.
"""Parse content/curriculum/section-6-modules.md and emit content/modules/*.md (domain-split, one file per phase).

Canonical learner-facing spec: run scripts/build_learner_phase_corpus.py → docs/PRD_AgentIQ.md.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input"
OUT_CONTENT = ROOT / "content"
CURRICULUM_PATH = OUT_CONTENT / "curriculum" / "section-6-modules.md"

# Phase code -> (filename stem, human domain title)
PHASE_DOMAIN: list[tuple[str, str, str]] = [
    ("P0", "local-inference-and-connectivity", "Local inference and connectivity"),
    ("P1", "ai-foundations-and-llm-mechanics", "AI foundations and LLM mechanics"),
    ("P2", "prompt-engineering", "Prompt engineering"),
    ("P3", "llm-apis-tools-and-multimodal", "LLM APIs, tools, and multimodal systems"),
    ("P4", "agents-planning-and-collaboration", "Agents, planning, and collaboration"),
    ("P5", "tool-use-memory-and-integrations", "Tool use, memory, and external integrations"),
    ("P6", "agent-frameworks-and-pipelines", "Agent frameworks and composable pipelines"),
    ("P7", "rag-and-knowledge-systems", "RAG and knowledge systems"),
    ("P8", "model-context-protocol", "Model Context Protocol (MCP)"),
    ("P9", "agent-to-agent-protocol", "Agent-to-agent protocol (A2A)"),
    ("P10", "unified-agentic-systems", "Unified agentic systems and platform architecture"),
    ("P11", "fine-tuning-and-adaptation", "Fine-tuning and domain adaptation"),
    ("P12", "ai-native-software-development", "AI-native software development"),
    ("P13", "workflow-automation", "Workflow and event-driven automation"),
    ("P14", "production-deployment", "Production deployment and hosting"),
    ("P15", "monitoring-evaluation-observability", "Monitoring, evaluation, and observability"),
    ("P16", "security-governance-and-safety", "Security, governance, and safety"),
    ("P17", "consulting-and-enterprise-delivery", "Consulting and enterprise AI delivery"),
    ("P18", "portfolio-capstones", "Portfolio capstones"),
    ("P19", "professional-certification-pathways", "Professional certification pathways"),
]


def read_curriculum() -> list[str]:
    return CURRICULUM_PATH.read_text(encoding="utf-8").splitlines(keepends=True)


def load_modules_by_phase() -> dict[str, list[dict[str, str]]]:
    by: dict[str, list[dict[str, str]]] = {p: [] for p, _, _ in PHASE_DOMAIN}
    with (INPUT / "modules.csv").open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            by.setdefault(row["phase_code"], []).append(row)
    return by


def split_curriculum_section(lines: list[str]) -> dict[str, str]:
    """Split body starting at first #### P0 through end of file (or before ## 7 if present)."""
    text = "".join(lines)
    m_start = re.search(r"^#### (P\d+) — .+$", text, re.MULTILINE)
    if not m_start:
        raise RuntimeError("Could not find start of phase blocks (#### P0)")
    start = m_start.start()
    m_end = re.search(r"\n---\n\n## 7\. PLATFORM FEATURES", text)
    end_at = m_end.start() if m_end else len(text)
    chunk = text[start:end_at]
    parts: dict[str, str] = {}
    pattern = re.compile(r"^#### (P\d+) — (.+)$", re.MULTILINE)
    matches = list(pattern.finditer(chunk))
    for i, mo in enumerate(matches):
        code = mo.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(chunk)
        body = chunk[mo.start() : end].strip()
        parts[code] = body
    return parts


def main() -> None:
    lines = read_curriculum()
    phase_bodies = split_curriculum_section(lines)
    modules_by_phase = load_modules_by_phase()

    modules_dir = OUT_CONTENT / "modules"
    modules_dir.mkdir(parents=True, exist_ok=True)

    for code, stem, title in PHASE_DOMAIN:
        body = phase_bodies.get(code, "")
        if not body:
            print(f"WARN: missing phase block {code}")
        mod_rows = modules_by_phase.get(code, [])
        lines_out = [
            "---\n",
            f"phase_code: {code}\n",
            f"domain_title: {title}\n",
            f"module_count: {len(mod_rows)}\n",
            "---\n\n",
            f"# {title}\n\n",
            f"**Phase:** `{code}`  \n",
            f"**Conceptual domain:** {title}  \n",
            "*Modules are grouped by learning domain, not by a single vendor or IDE.*\n\n",
            "## Module index (from `input/modules.csv`)\n\n",
            "| # | Title | Priority | Tools |\n",
            "|---|--------|----------|-------|\n",
        ]
        for r in mod_rows:
            t = r["title"].replace("|", "\\|")
            tools = r["tools"].replace("|", "\\|")
            lines_out.append(
                f"| {r['module_num']} | {t} | {r['priority']} | {tools} |\n"
            )
        lines_out.append("\n---\n\n## Curriculum detail (from input PRD full curriculum block)\n\n")
        lines_out.append(body)
        lines_out.append("\n")
        (modules_dir / f"{stem}.md").write_text("".join(lines_out), encoding="utf-8")

    print(f"Wrote {len(PHASE_DOMAIN)} module domain files to {modules_dir}")
    print("Canonical PRD: python3 scripts/build_learner_phase_corpus.py")


if __name__ == "__main__":
    main()
