---
journey_id: '15.1'
module_num: 107
phase_code: P15
title: 'Agent Evaluation Metrics & Benchmarks'
tools: 'RAGAS, TruLens, custom evals'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 15.1 — Agent Evaluation Metrics & Benchmarks

**15.1 — Agent Evaluation Metrics & Benchmarks** [Core] | Tools: `RAGAS, TruLens, custom evals`
- Learn: OverviewModule 107 (P15) — Agent Evaluation Metrics & Benchmarks. Tools focus: RAGAS, TruLens, custom evals. Core path — prioritize in your sprint.RAGAS and similar frameworks score faithfulness, answer relevance, and context precision — useful for regression suites, not perfect truth.
- Practice: Install RAGAS; run quickstart on synthetic QA pairs.Log metric distributions across five prompts.Identify one metric that misfires; explain why.Wire metrics export to CSV or W&B.Define pass threshold for CI gating.
- Code: `# Module 107 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 107, "topic": "Agent Evaluation Metrics & Benchm`
