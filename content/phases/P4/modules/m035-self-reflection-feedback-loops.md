---
journey_id: '4.6'
module_num: 35
phase_code: P4
title: 'Self-Reflection / Feedback Loops'
tools: 'Reflexion, LangGraph'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 4.6 — Self-Reflection / Feedback Loops

**4.6 — Self-Reflection / Feedback Loops** [Core] | Tools: `Reflexion, LangGraph`
- Learn: OverviewModule 35 (P4) — Self-Reflection / Feedback Loops. Tools focus: Reflexion, LangGraph. Core path — prioritize in your sprint.Self-reflection asks the model to critique prior outputs; multi-agent collaboration splits expertise. Combine with evaluation harnesses so reflection improves measurable scores.
- Practice: Pair generator and critic agents; cap at two critique rounds.Score outputs with a rubric before/after critique.Log whether critiques are actionable vs generic.Try a third agent as tie-breaker; note coordination overhead.Decide when human review replaces automated critique.
- Code: `# Module 35 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 35, "topic": "Self-Reflection / Feedback Loops", `
