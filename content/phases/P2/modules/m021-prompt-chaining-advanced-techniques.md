---
journey_id: '2.7'
module_num: 21
phase_code: P2
title: 'Prompt Chaining & Advanced Techniques'
tools: 'LangChain, LangGraph, LCEL'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 2.7 — Prompt Chaining & Advanced Techniques

**2.7 — Prompt Chaining & Advanced Techniques** [Core] | Tools: `LangChain, LangGraph, LCEL`
- Learn: OverviewModule 21 (P2) — Prompt Chaining & Advanced Techniques. Tools focus: LangChain, LangGraph, LCEL. Core path — prioritize in your sprint.Prompt chaining composes LCEL or LangGraph nodes so each stage has a contract. Advanced techniques include routing, parallel branches, and structured outputs between hops.
- Practice: Build a three-node chain: extract → transform → generate; validate JSON between nodes.Add a conditional branch on extracted intent; test two paths.Measure end-to-end latency vs monolithic prompt.Version prompts separately per node; document compatibility.List failure modes per hop and corresponding fallbacks.
- Code: `# Module 21 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 21, "topic": "Prompt Chaining & Advanced Techniqu`

#### P3 — LLMs & APIs
**Purpose:** Providers, auth, tools, multimodal

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 22 | OpenAI API Deep Dive (GPT-4, GPT-4o) | Core | openai Python SDK |
| 23 | Anthropic Claude API | Core | anthropic Python SDK |
| 24 | Google Gemini API | Core | google-generativeai |
| 25 | Mistral & Open Source LLMs (LLaMA, DeepSeek) | Core | Hugging Face, mistralai SDK |
| 26 | API Authentication & Rate Limiting | Core | API keys, backoff, tenacity |
| 27 | Toolformer / Function Calling | Core | OpenAI tools, Claude tool_use |
| 28 | Tool Invocation & Output Parsing | Core | Pydantic, json_schema, LangChain |
| 29 | Multimodal AI (Text + Image + Audio + Video) | Core | GPT-4V, Gemini, Pika, ElevenLabs |
