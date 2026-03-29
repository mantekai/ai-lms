---
journey_id: '4.4'
module_num: 33
phase_code: P4
title: 'Decision-Making Policies for Agents'
tools: 'LangGraph, state machines'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 4.4 — Decision-Making Policies for Agents

**4.4 — Decision-Making Policies for Agents** [Core] | Tools: `LangGraph, state machines`
- Learn: OverviewModule 33 (P4) — Decision-Making Policies for Agents. Tools focus: LangGraph, state machines. Core path — prioritize in your sprint.Policies decide which tool or transition fires given state — epsilon-greedy exploration is rare in LLM agents; instead you use classifiers, routers, or scored choices. State machines keep behaviour auditable.
- Practice: Model agent state as an enum + small dict; document transitions.Implement if/match routing vs LLM-chosen tool once; compare failure rates on five cases.Add a default safe action when confidence is low.Log policy decisions with reasons (structured JSON).Describe how you would unit-test a policy without calling live models.
- Code: `# Module 33 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 33, "topic": "Decision-Making Policies for Agents`
