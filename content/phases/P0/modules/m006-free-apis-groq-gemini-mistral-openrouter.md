---
journey_id: '0.6'
module_num: 6
phase_code: P0
title: 'Free APIs: Groq, Gemini, Mistral, OpenRouter'
tools: 'Groq API, Gemini, OpenRouter'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 0.6 — Free APIs: Groq, Gemini, Mistral, OpenRouter

**0.6 — Free APIs: Groq, Gemini, Mistral, OpenRouter** [Core] | Tools: `Groq API, Gemini, OpenRouter`
- Learn: OverviewModule 6 (P0) — Free APIs: Groq, Gemini, Mistral, OpenRouter. Tools focus: Groq API, Gemini, OpenRouter. Core path — prioritize in your sprint.Free or low-cost hosted APIs (Groq LPU-style inference, Gemini developer tier, Mistral keys, OpenRouter aggregation) let you prototype without training models. Each has different rate limits, safety filters, and JSON/tooling support.Build a comparison matrix: latency, max context, function-calling support, and pricing unit. Never ship production t
- Practice: Create sandbox keys for at least two listed providers; store them only in env vars.Run the same three prompts through each; log latency and rough quality notes.Check each vendor's rate-limit headers or dashboard; note burst vs sustained limits.Identify which provider supports tool calling for your SDK version — try one tool call if available.Summarize in one page which provider you would default t
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

#### P1 — AI Foundations
**Purpose:** LLMs, transformers, embeddings, ML paradigms

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 7 | Top 40 AI Terms & Core Concepts | Core | Flashcards, terminology |
| 8 | How LLMs Work: Transformers & Tokenization | Core | Hugging Face, tiktoken |
| 9 | Embeddings & Vector Representations | Core | OpenAI Embeddings, SBERT |
| 10 | Inference, Context Windows & Cost Optimisation | Core | Token counters, model APIs |
| 11 | Quantization & Model Efficiency | Opt | GGUF, GPTQ, bitsandbytes |
| 12 | GPU/TPU & Compute for AI | Opt | CUDA, Colab, RunPod |
| 13 | ML Paradigms: Supervised, Unsupervised, RL | Core | scikit-learn, OpenAI Gym |
| 14 | Generative AI Pipeline (Input→Process→Output) | Core | OpenAI API, LangChain |
