---
journey_id: '2.2'
module_num: 16
phase_code: P2
title: 'Chain-of-Thought (CoT) Prompting'
tools: 'GPT-4o, Claude, Gemini'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 2.2 — Chain-of-Thought (CoT) Prompting

**2.2 — Chain-of-Thought (CoT) Prompting** [Core] | Tools: `GPT-4o, Claude, Gemini`
- Learn: OverviewModule 16 (P2) — Chain-of-Thought (CoT) Prompting. Tools focus: GPT-4o, Claude, Gemini. Core path — prioritize in your sprint.Chain-of-thought elicits intermediate reasoning before answers, improving multi-step math and logic when the model is instructed to show steps — but increases tokens and can leak verbose internals.Learn when to keep reasoning hidden from end users vs when to display it for auditability.
- Practice: Solve five numeric word problems with and without CoT; compare accuracy.Ask for explicit “final answer in a box” after reasoning to separate UI from chain.Measure token increase from CoT; decide if cost is justified per task.Try a self-consistency variant (multiple chains, vote) on one hard puzzle.Note one failure mode (overconfident wrong chain) and a guardrail.
- Code: `# Module 16 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 16, "topic": "Chain-of-Thought (CoT) Prompting", `
