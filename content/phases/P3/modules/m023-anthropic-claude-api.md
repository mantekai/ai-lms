---
journey_id: '3.2'
module_num: 23
phase_code: P3
title: 'Anthropic Claude API'
tools: 'anthropic Python SDK'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.2 — Anthropic Claude API

**3.2 — Anthropic Claude API** [Core] | Tools: `anthropic Python SDK`
- Learn: OverviewModule 23 (P3) — Anthropic Claude API. Tools focus: anthropic Python SDK. Core path — prioritize in your sprint.Anthropic's API is the reference stack for chat completions, structured outputs, embeddings, and tool calls in many production systems. You learn authentication, model selection, streaming vs batch, and how errors surface (rate limits, context length, content policy).Compare latency and cost across models in the same family (e.g. mini vs full) for your own prompt shapes. Log re
- Practice: Create a project API key in the Anthropic console; store it as an environment variable only.Install the official SDK for your language; run a minimal chat completion against a small model.Add structured logging: model name, latency, input/output token counts (no raw PII in logs).Call the same prompt with two model sizes; compare quality, latency, and documented pricing.Write a short anthropic Pyth
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
