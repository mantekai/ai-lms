---
kind: phase_supplement
phase_code: P0
---

# Phase P0 — supplemental depth

### Local and edge inference

**GGUF Format:** A binary file format for storing quantized LLM weights, designed for llama.cpp inference. GGUF files bundle the model weights, tokenizer, and metadata in a single file. Quantization levels: Q4_K_M (4-bit, good quality/size balance), Q8_0 (8-bit, near full quality), Q2_K (2-bit, smallest but lower quality). LM Studio and Ollama both use GGUF models. Understanding quantization levels helps learners choose the right model for their hardware.

**Hardware Considerations:** RAM/VRAM requirements for local model inference. Rule of thumb: model size in GB ≈ parameters × bytes per weight. A 7B model at Q4 ≈ 4GB RAM. A 13B model at Q4 ≈ 8GB RAM. A 70B model at Q4 ≈ 40GB RAM. CPU-only inference is 5-10x slower than GPU inference. Learners must document their hardware specs and measure tokens-per-second to understand their local inference capabilities.

- Ollama runs open-weight models locally with CLI and HTTP API
- Models ship as downloadable blobs; pull once, run offline-capable inference on C
- Steps: Install Ollama → pull llama3.2/mistral → run interactive chat → call HTTP
- Key commands: `ollama pull`, `ollama run`, `ollama list`
- Distinguish pull vs run vs serving multiple models
- Know RAM/VRAM limits; CPU-only machines will be slower
- Desktop UI for discovering GGUF checkpoints with configurable context and GPU la
- Exposes OpenAI-compatible local server (default port 1234)
- Compare quantizations: Q4_K_M vs Q8, toggle GPU offload
- Steps: Install → download GGUF model → start local server → verify `/v1/models`
- Browser front-end for Ollama, OpenAI-compatible proxies via Docker
- Multi-user patterns, model switching, optional RAG plugins
- Steps: Docker run → connect to Ollama/LM Studio backend → create model presets →
- Steps: Check CUDA prerequisites → launch OpenAI-compatible server → send concurr
- Steps: Install → configure 2+ backends → send completion via unified model strin
- Free/low-cost hosted APIs for prototyping without training models
- Build comparison matrix: latency, max context, function-calling support, pricing
- Never ship production traffic on keys committed to git
- Steps: Create sandbox keys (env vars only) → run same prompts through each → che


- Module 1: Ollama Setup & Local Model Running [Core] | Tools: Ollama, llama3, mis
- Module 5: LiteLLM Routing & Load Balancing [Core] | Tools: LiteLLM, proxy server


- Ollama as OpenAI-compatible API (`http://localhost:11434/v1`)
- Groq: 14,400 req/day, 300+ tok/sec
- Google AI Studio: 1M tokens/min, Gemini 2.5 Flash
- Mistral: 1B tokens/month free

