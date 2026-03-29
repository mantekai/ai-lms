---
journey_id: '3.6'
module_num: 27
phase_code: P3
title: 'Toolformer / Function Calling'
tools: 'OpenAI tools, Claude tool_use'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.6 — Toolformer / Function Calling

**3.6 — Toolformer / Function Calling** [Core] | Tools: `OpenAI tools, Claude tool_use`
- Learn: OverviewModule 27 (P3) — Toolformer / Function Calling. Tools focus: OpenAI tools, Claude tool_use. Core path — prioritize in your sprint.Tool / function calling lets models emit structured actions the runtime executes. Schemas must be tight: enums, descriptions, and required fields reduce hallucinated arguments.
- Practice: Define one JSON schema tool; register it with the provider SDK you use.Handle tool_calls in a loop until the model returns user-visible content.Test three successful calls and two invalid-args paths; verify error handling.Compare parallel vs serial tool execution for your use case.Document trust boundaries: which tools can touch production data?
- Code: `# Module 27 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 27, "topic": "Toolformer / Function Calling", "st`
