---
journey_id: '11.2'
module_num: 83
phase_code: P11
title: 'LoRA & QLoRA (Efficient Fine-Tuning)'
tools: 'PEFT, bitsandbytes, LoRA'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 11.2 — LoRA & QLoRA (Efficient Fine-Tuning)

**11.2 — LoRA & QLoRA (Efficient Fine-Tuning)** [Core] | Tools: `PEFT, bitsandbytes, LoRA`
- Learn: OverviewModule 83 (P11) — LoRA & QLoRA (Efficient Fine-Tuning). Tools focus: PEFT, bitsandbytes, LoRA. Core path — prioritize in your sprint.LoRA/QLoRA train low-rank adapters while freezing most weights — feasible on consumer GPUs with bitsandbytes quant. Watch for catastrophic forgetting on edge tasks.
- Practice: Read PEFT LoRA guide; note rank and alpha defaults.Configure one QLoRA training job on a tiny dataset.Compare adapter-only checkpoint size vs full weights.Merge adapters vs load at runtime — decide for deployment.Run qualitative eval on domain jargon the base model mishandled.
- Code: `# Module 83 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 83, "topic": "LoRA & QLoRA (Efficient Fine-Tuning`
