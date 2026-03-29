---
journey_id: '0.5'
module_num: 5
phase_code: P0
title: 'LiteLLM Routing & Load Balancing'
tools: 'LiteLLM, proxy server'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 0.5 — LiteLLM Routing & Load Balancing

**0.5 — LiteLLM Routing & Load Balancing** [Core] | Tools: `LiteLLM, proxy server`
- Learn: OverviewModule 5 (P0) — LiteLLM Routing & Load Balancing. Tools focus: LiteLLM, proxy server. Core path — prioritize in your sprint.LiteLLM is a unified router: one interface to many providers and local endpoints, with optional proxy features for budgets, fallbacks, and load balancing. It fits teams that standardize on OpenAI-style request bodies.Practice routing the same prompt to a local model and a hosted model; compare responses and failure modes when a backend is down.
- Practice: Install LiteLLM; configure at least two backends (e.g. Ollama + one hosted key).Send a completion through LiteLLM using the unified model string format.Simulate a failing backend; configure a fallback model and verify the request succeeds.Enable or inspect spend logging (if using proxy mode) with synthetic requests only.Document your routing table and when each backend is chosen.
- Code: `pip install litellm
python -c "import litellm; print(litellm.completion(model='ollama/llama3.2', messages=[{'role':'user','content':'ping'}]))"`
