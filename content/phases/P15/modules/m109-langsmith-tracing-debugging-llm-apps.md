---
journey_id: '15.3'
module_num: 109
phase_code: P15
title: 'LangSmith — Tracing & Debugging LLM Apps'
tools: 'LangSmith, LangChain'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 15.3 — LangSmith — Tracing & Debugging LLM Apps

**15.3 — LangSmith — Tracing & Debugging LLM Apps** [Core] | Tools: `LangSmith, LangChain`
- Learn: OverviewModule 109 (P15) — LangSmith — Tracing & Debugging LLM Apps. Tools focus: LangSmith, LangChain. Core path — prioritize in your sprint.LangSmith traces show LLM spans, tool calls, and retries — essential for debugging non-deterministic failures in staging.
- Practice: Enable tracing on one chain; reproduce a bug twice.Filter traces by tags and latency.Share trace link internally with redaction checklist.Add evaluators on a dataset run.Set retention and access controls per environment.
- Code: `# Module 109 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 109, "topic": "LangSmith — Tracing & Debugging L`
