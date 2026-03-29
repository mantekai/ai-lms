---
journey_id: '0.4'
module_num: 4
phase_code: P0
title: 'vLLM — High-Performance Inference'
tools: 'vLLM, CUDA, Python'
priority: 'OPTIONAL'
source: content/curriculum/section-6-modules.md
---

# 0.4 — vLLM — High-Performance Inference

**0.4 — vLLM — High-Performance Inference** [Optional] | Tools: `vLLM, CUDA, Python`
- Learn: OverviewModule 4 (P0) — vLLM — High-Performance Inference. Tools focus: vLLM, CUDA, Python. Optional depth — revisit when you need this specialty.vLLM targets high-throughput GPU serving with PagedAttention and continuous batching. It is the layer beneath many internal model-serving stacks when latency under load matters more than a desktop GUI.Understand CUDA/driver expectations, batching knobs, and when vLLM is overkill vs Ollama for solo development.
- Practice: Read the official installation prerequisites (CUDA version, GPU memory).Launch a minimal OpenAI-compatible server with a documented quickstart model.Send concurrent requests (simple script) and observe throughput vs single-threaded local runners.Capture one error from misconfigured CUDA or OOM and document the fix path.Write two sentences: when you would choose vLLM vs a simpler local runner for a
- Code: `# Module 4 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 4, "topic": "vLLM — High-Performance Inference", "`
