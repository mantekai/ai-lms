---
journey_id: '2.5'
module_num: 19
phase_code: P2
title: 'Self-Critique, Retry Loops & Reflexion'
tools: 'LangGraph, custom Python'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 2.5 — Self-Critique, Retry Loops & Reflexion

**2.5 — Self-Critique, Retry Loops & Reflexion** [Core] | Tools: `LangGraph, custom Python`
- Learn: OverviewModule 19 (P2) — Self-Critique, Retry Loops & Reflexion. Tools focus: LangGraph, custom Python. Core path — prioritize in your sprint.Self-critique and reflexion patterns ask the model to evaluate its draft and revise. LangGraph and custom loops implement retries with state — production needs limits to avoid runaway spend.
- Practice: Implement generate→critique→revise for one writing task; stop after two revisions max.Compare single-pass vs two-pass quality using a rubric you define.Instrument token usage per revision; plot cost vs gain.Handle critique refusal or empty output gracefully in code.Document when reflexion is inappropriate (latency-sensitive chat).
- Code: `# Module 19 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 19, "topic": "Self-Critique, Retry Loops & Reflex`
