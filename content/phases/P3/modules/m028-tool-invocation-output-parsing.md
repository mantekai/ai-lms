---
journey_id: '3.7'
module_num: 28
phase_code: P3
title: 'Tool Invocation & Output Parsing'
tools: 'Pydantic, json_schema, LangChain'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.7 — Tool Invocation & Output Parsing

**3.7 — Tool Invocation & Output Parsing** [Core] | Tools: `Pydantic, json_schema, LangChain`
- Learn: OverviewModule 28 (P3) — Tool Invocation & Output Parsing. Tools focus: Pydantic, json_schema, LangChain. Core path — prioritize in your sprint.Parsing tool outputs into Pydantic models (or equivalent) enforces types before side effects. LangChain structured output helpers wrap similar ideas with retries.
- Practice: Return tool output as JSON; validate with Pydantic v2 models.Add a repair pass: on ValidationError, ask the model to fix shape.Unit-test parsers with golden files (no live API).Measure how often repair passes trigger in a 50-call sample.List schemas you would never auto-parse without human review.
- Code: `# Module 28 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 28, "topic": "Tool Invocation & Output Parsing", `
