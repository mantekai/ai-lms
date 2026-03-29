---
journey_id: '3.1'
module_num: 22
phase_code: P3
title: 'OpenAI API Deep Dive (GPT-4, GPT-4o)'
tools: 'openai Python SDK'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.1 — OpenAI API Deep Dive (GPT-4, GPT-4o)

**3.1 — OpenAI API Deep Dive (GPT-4, GPT-4o)** [Core] | Tools: `openai Python SDK`
- Learn: OverviewModule 22 (P3) — OpenAI API Deep Dive (GPT-4, GPT-4o). Tools focus: openai Python SDK. Core path — prioritize in your sprint.OpenAI's API is the reference stack for chat completions, structured outputs, embeddings, and tool calls in many production systems. You learn authentication, model selection, streaming vs batch, and how errors surface (rate limits, context length, content policy).Compare latency and cost across models in the same family (e.g. mini vs full) for your own prompt shap
- Practice: Create a project API key in the OpenAI console; store it as an environment variable only.Install the official SDK for your language; run a minimal chat completion against a small model.Add structured logging: model name, latency, input/output token counts (no raw PII in logs).Call the same prompt with two model sizes; compare quality, latency, and documented pricing.Write a short openai Python SDK
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
