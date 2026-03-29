---
journey_id: '3.4'
module_num: 25
phase_code: P3
title: 'Mistral & Open Source LLMs (LLaMA, DeepSeek)'
tools: 'Hugging Face, mistralai SDK'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.4 — Mistral & Open Source LLMs (LLaMA, DeepSeek)

**3.4 — Mistral & Open Source LLMs (LLaMA, DeepSeek)** [Core] | Tools: `Hugging Face, mistralai SDK`
- Learn: OverviewModule 25 (P3) — Mistral & Open Source LLMs (LLaMA, DeepSeek). Tools focus: Hugging Face, mistralai SDK. Core path — prioritize in your sprint.Mistral’s hosted API and open-weights families (e.g. LLaMA-class, DeepSeek-class on Hugging Face) span commercial keys and self-hosted inference. Understand license tags, gated models, and HF tokens for downloads.Practice one hosted completion and one local or HF inference path so you can advise clients on lock-in vs control.
- Practice: Create a Mistral API key or HF token; never commit either.Call a Mistral chat model via official SDK or HTTP.Pull a small open model card on Hugging Face; read license and use restrictions.Run a minimal generate call locally or via inference endpoint if feasible.Summarize when you would recommend API vs self-host for a regulated client.
- Code: `# Module 25 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 25, "topic": "Mistral & Open Source LLMs (LLaMA, `
