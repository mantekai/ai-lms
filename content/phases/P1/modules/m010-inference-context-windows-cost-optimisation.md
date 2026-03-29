---
journey_id: '1.4'
module_num: 10
phase_code: P1
title: 'Inference, Context Windows & Cost Optimisation'
tools: 'Token counters, model APIs'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 1.4 — Inference, Context Windows & Cost Optimisation

**1.4 — Inference, Context Windows & Cost Optimisation** [Core] | Tools: `Token counters, model APIs`
- Learn: OverviewModule 10 (P1) — Inference, Context Windows & Cost Optimisation. Tools focus: Token counters, model APIs. Core path — prioritize in your sprint.Inference is the forward pass at serving time — distinct from training. Context windows cap how much text fits in one call; providers bill input and output tokens separately, and long prompts hit latency and cost cliffs.Practice measuring tokens before send, trimming history, summarizing threads, and choosing smaller models for easy subtasks.
- Practice: Pick a tokenizer or API metadata; measure tokens for a long thread before and after summarization.Call a chat model with the same task using a large vs small model; compare cost and latency.Implement a simple token budget guard that refuses or compresses when over a threshold.Read provider docs for max context and output limits; note what happens on overflow.Write a stakeholder-friendly paragraph 
- Code: `# Module 10 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 10, "topic": "Inference, Context Windows & Cost O`
