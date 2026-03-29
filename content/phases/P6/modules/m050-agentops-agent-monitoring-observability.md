---
journey_id: '6.6'
module_num: 50
phase_code: P6
title: 'AgentOps — Agent Monitoring & Observability'
tools: 'AgentOps, LangSmith'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 6.6 — AgentOps — Agent Monitoring & Observability

**6.6 — AgentOps — Agent Monitoring & Observability** [Core] | Tools: `AgentOps, LangSmith`
- Learn: OverviewModule 50 (P6) — AgentOps — Agent Monitoring & Observability. Tools focus: AgentOps, LangSmith. Core path — prioritize in your sprint.AgentOps and LangSmith-class tools trace spans per model/tool call. You need consistent run IDs, cost attribution, and PII scrubbing.
- Practice: Instrument one agent with tracing SDK; view a waterfall.Tag traces with user_session anonymized.Add eval scores to a traced run manually.Configure retention policy appropriate for test data.Document who can access traces in your team RBAC model.
- Code: `# Module 50 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 50, "topic": "AgentOps — Agent Monitoring & Obser`
