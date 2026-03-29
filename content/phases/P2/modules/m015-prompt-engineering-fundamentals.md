---
journey_id: '2.1'
module_num: 15
phase_code: P2
title: 'Prompt Engineering Fundamentals'
tools: 'Claude, GPT-4, PromptPerfect'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 2.1 — Prompt Engineering Fundamentals

**2.1 — Prompt Engineering Fundamentals** [Core] | Tools: `Claude, GPT-4, PromptPerfect`
- Learn: OverviewModule 15 (P2) — Prompt Engineering Fundamentals. Tools focus: Claude, GPT-4, PromptPerfect. Core path — prioritize in your sprint.Prompt engineering is the highest-ROI lever before changing models: clarity, format, examples (few-shot), and role framing steer behaviour more cheaply than fine-tunes for many tasks.Practice rewriting vague prompts into instructions with constraints, output format (JSON/Markdown), and evaluation rubrics you can automate later.
- Practice: Take one business task; write a bad prompt, then two improved iterations with explicit format.Add a negative constraint (“do not”) and verify the model respects it on five trials.Compare zero-shot vs two-shot for a structured extraction task; score with a simple checklist.Document temperature and max-tokens choices and why they fit this task.Peer-review another learner’s prompt for ambiguity; revi
- Code: `# Module 15 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 15, "topic": "Prompt Engineering Fundamentals", "`
