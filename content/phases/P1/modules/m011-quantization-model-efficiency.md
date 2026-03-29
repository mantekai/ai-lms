---
journey_id: '1.5'
module_num: 11
phase_code: P1
title: 'Quantization & Model Efficiency'
tools: 'GGUF, GPTQ, bitsandbytes'
priority: 'OPTIONAL'
source: content/curriculum/section-6-modules.md
---

# 1.5 — Quantization & Model Efficiency

**1.5 — Quantization & Model Efficiency** [Optional] | Tools: `GGUF, GPTQ, bitsandbytes`
- Learn: OverviewModule 11 (P1) — Quantization & Model Efficiency. Tools focus: GGUF, GPTQ, bitsandbytes. Optional depth — revisit when you need this specialty.Quantization reduces weight precision (e.g. FP16 → INT8 → 4-bit) to shrink memory and speed inference. GGUF bundles for llama.cpp, GPTQ, and bitsandbytes QLoRA during training are common touchpoints.Understand accuracy vs size trade-offs and why quantized models behave slightly differently on code or math.
- Practice: Read one official guide each for GGUF inference vs training-time quantization (QLoRA).Run one pre-quantized model locally; note RAM/VRAM vs full precision expectations.List three metrics you would monitor if you switched quantization in production (latency, perplexity, task evals).Identify a task where low-bit quantization might fail (e.g. long arithmetic) and test informally.Summarize when you wo
- Code: `# Module 11 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 11, "topic": "Quantization & Model Efficiency", "`
