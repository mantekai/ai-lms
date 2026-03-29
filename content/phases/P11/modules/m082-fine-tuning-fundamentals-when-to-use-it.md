---
journey_id: '11.1'
module_num: 82
phase_code: P11
title: 'Fine-Tuning Fundamentals & When to Use It'
tools: 'Hugging Face, OpenAI fine-tune'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 11.1 — Fine-Tuning Fundamentals & When to Use It

**11.1 — Fine-Tuning Fundamentals & When to Use It** [Core] | Tools: `Hugging Face, OpenAI fine-tune`
- Learn: OverviewModule 82 (P11) — Fine-Tuning Fundamentals & When to Use It. Tools focus: Hugging Face, OpenAI fine-tune. Core path — prioritize in your sprint.Fine-tuning adapts a pretrained model to style, format, or domain with smaller curated datasets. Prefer prompting + RAG first; tune when you need consistent behaviour cheaper at inference than giant prompts.
- Practice: List go/no-go criteria: when tuning beats prompt/RAG for your use case.Sketch data card: source, license, PII scrubbing method.Run a toy HF Trainer or API fine-tune on public data only.Evaluate before/after on ten held-out prompts with a rubric.Document rollback: how to revert to base model serving.
- Code: `# Module 82 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 82, "topic": "Fine-Tuning Fundamentals & When to `
