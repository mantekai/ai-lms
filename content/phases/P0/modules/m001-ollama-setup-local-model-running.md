---
journey_id: '0.1'
module_num: 1
phase_code: P0
title: 'Ollama Setup & Local Model Running'
tools: 'Ollama, llama3, mistral'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 0.1 — Ollama Setup & Local Model Running

**0.1 — Ollama Setup & Local Model Running** [Core] | Tools: `Ollama, llama3, mistral`
- Learn: OverviewModule 1 (P0) — Ollama Setup & Local Model Running. Tools focus: Ollama, llama3, mistral. Core path — prioritize in your sprint.Ollama runs open-weight models locally with a simple CLI and HTTP API. Models ship as downloadable blobs; you pull once and run offline-capable inference on CPU or GPU depending on size.Practice the full loop: install, pull a 7–8B-class model, run interactive chat, then call the HTTP API from a script. Note RAM/VRAM limits — if generation is slow, that is expect
- Practice: Install Ollama from the official site for your OS; confirm `ollama --version`.Run `ollama pull` for a small chat model (e.g. llama3.2 or mistral) and wait for completion.Use `ollama run <model>` with three prompts: factual, reasoning, and code generation.From another terminal, hit the local HTTP API with curl or httpx using the same model.Document hardware (RAM/GPU), model size, and tokens/sec in 
- Code: `curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
ollama run llama3.2 "Summarize MCP in 3 bullets"`
