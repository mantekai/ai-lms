---
journey_id: '6.4'
module_num: 48
phase_code: P6
title: 'AutoGen — Conversational Multi-Agent'
tools: 'AutoGen, ConversableAgent'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 6.4 — AutoGen — Conversational Multi-Agent

**6.4 — AutoGen — Conversational Multi-Agent** [Core] | Tools: `AutoGen, ConversableAgent`
- Learn: OverviewModule 48 (P6) — AutoGen — Conversational Multi-Agent. Tools focus: AutoGen, ConversableAgent. Core path — prioritize in your sprint.AutoGen uses conversable agents with code execution hooks. Learn group chat patterns and safety around code_runner.
- Practice: Spin up two-agent chat solving a coding puzzle.Constrain code execution to a sandbox if available.Stop the chat after N messages programmatically.Capture one failure where agents talk past each other; fix prompts.Summarize when AutoGen beats simpler orchestration.
- Code: `# Module 48 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 48, "topic": "AutoGen — Conversational Multi-Agen`
