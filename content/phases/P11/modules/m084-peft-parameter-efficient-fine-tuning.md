---
journey_id: '11.3'
module_num: 84
phase_code: P11
title: 'PEFT: Parameter Efficient Fine-Tuning'
tools: 'PEFT library, HF Transformers'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 11.3 — PEFT: Parameter Efficient Fine-Tuning

**11.3 — PEFT: Parameter Efficient Fine-Tuning** [Core] | Tools: `PEFT library, HF Transformers`
- Learn: OverviewModule 84 (P11) — PEFT: Parameter Efficient Fine-Tuning. Tools focus: PEFT library, HF Transformers. Core path — prioritize in your sprint.PEFT umbrella covers LoRA, prefix tuning, adapters. Pick method based on framework support and serving constraints (some hosts only merge LoRA).
- Practice: Tabulate three PEFT methods with memory and inference trade-offs.Implement one non-LoRA PEFt method tutorial if hardware allows.Export config YAML used for reproducibility.Version training code + data hash in experiment log.Identify failure: overfitting on tiny data — show metric.
- Code: `# Module 84 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 84, "topic": "PEFT: Parameter Efficient Fine-Tuni`
