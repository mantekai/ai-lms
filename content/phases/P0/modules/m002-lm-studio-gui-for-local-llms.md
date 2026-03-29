---
journey_id: '0.2'
module_num: 2
phase_code: P0
title: 'LM Studio — GUI for Local LLMs'
tools: 'LM Studio, GGUF models'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 0.2 — LM Studio — GUI for Local LLMs

**0.2 — LM Studio — GUI for Local LLMs** [Core] | Tools: `LM Studio, GGUF models`
- Learn: OverviewModule 2 (P0) — LM Studio — GUI for Local LLMs. Tools focus: LM Studio, GGUF models. Core path — prioritize in your sprint.LM Studio provides a desktop UI for discovering GGUF checkpoints, loading them with configurable context and GPU layers, and exposing an OpenAI-compatible local server (often on port 1234).Learn when GUI workflows beat CLI-only runners: comparing quantizations (Q4_K_M vs Q8), toggling GPU offload, and debugging tokenizer mismatches when copying prompts from hosted AP
- Practice: Install LM Studio; download one GGUF model appropriate for your machine.Start a local server; verify `GET /v1/models` returns your loaded model.From Python or curl, send a chat completion to the local OpenAI-compatible endpoint.Experiment with GPU layer count: note speed vs quality trade-offs in a short table.Export your server settings screenshot + one sample request/response (redact any sensitiv
- Code: `# After starting LM Studio local server (default :1234):
curl http://localhost:1234/v1/models`
