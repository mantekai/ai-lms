---
journey_id: '10.1'
module_num: 75
phase_code: P10
title: 'Orchestrator Design & Patterns'
tools: 'LangGraph, custom Python'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 10.1 — Orchestrator Design & Patterns

**10.1 — Orchestrator Design & Patterns** [Core] | Tools: `LangGraph, custom Python`
- Learn: OverviewModule 75 (P10) — Orchestrator Design & Patterns. Tools focus: LangGraph, custom Python. Core path — prioritize in your sprint.Orchestrators coordinate subgraphs, retries, and human approvals. Patterns include supervisor, handoff, and parallel fan-out — each trades complexity vs observability.
- Practice: Implement supervisor routing three specialist stubs.Add pause/resume for human approval on high-risk branch.Export metrics: tasks started, succeeded, failed.Compare orchestrator code size vs prompts-only baseline.Document rollback story for partially applied side effects.
- Code: `# Module 75 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 75, "topic": "Orchestrator Design & Patterns", "s`
