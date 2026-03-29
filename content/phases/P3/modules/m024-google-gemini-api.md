---
journey_id: '3.3'
module_num: 24
phase_code: P3
title: 'Google Gemini API'
tools: 'google-generativeai'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.3 — Google Gemini API

**3.3 — Google Gemini API** [Core] | Tools: `google-generativeai`
- Learn: OverviewModule 24 (P3) — Google Gemini API. Tools focus: google-generativeai. Core path — prioritize in your sprint.Google’s Gemini API exposes multimodal and long-context models with a distinct SDK surface from OpenAI. You learn API keys via AI Studio, model IDs, safety settings, and quota dashboards.Compare request/response shapes to OpenAI for the same task; note tool and JSON schema support per model generation.Store keys in GOOGLE_API_KEY or the env var your SDK expects.Log model id + laten
- Practice: Create a key in Google AI Studio; export it to your shell environment only.Install google-genai or google-generativeai per current docs; list models available to your project.Run text and (if available) one image+text call; capture latency.Try structured output or function calling if supported on your chosen model.Write integration notes: differences vs OpenAI that would affect a shared abstractio
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
