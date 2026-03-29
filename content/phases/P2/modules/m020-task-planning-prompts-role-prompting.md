---
journey_id: '2.6'
module_num: 20
phase_code: P2
title: 'Task Planning Prompts & Role Prompting'
tools: 'Claude, GPT-4, Perplexity'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 2.6 — Task Planning Prompts & Role Prompting

**2.6 — Task Planning Prompts & Role Prompting** [Core] | Tools: `Claude, GPT-4, Perplexity`
- Learn: OverviewModule 20 (P2) — Task Planning Prompts & Role Prompting. Tools focus: Claude, GPT-4, Perplexity. Core path — prioritize in your sprint.Task planning prompts decompose goals into ordered steps; role prompting sets expertise and tone. Combine with explicit tool lists when the model should choose actions.
- Practice: Write a planner prompt that outputs a numbered plan only (no execution).Feed the plan to an executor prompt; check step adherence on a simple project.Swap roles (junior vs principal) and note behaviour changes.Add a checklist the model must tick before claiming completion.Capture one derailment (skipped step) and tighten the prompt.
- Code: `# Module 20 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 20, "topic": "Task Planning Prompts & Role Prompt`
