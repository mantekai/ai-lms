---
journey_id: '3.8'
module_num: 29
phase_code: P3
title: 'Multimodal AI (Text + Image + Audio + Video)'
tools: 'GPT-4V, Gemini, Pika, ElevenLabs'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.8 — Multimodal AI (Text + Image + Audio + Video)

**3.8 — Multimodal AI (Text + Image + Audio + Video)** [Core] | Tools: `GPT-4V, Gemini, Pika, ElevenLabs`
- Learn: OverviewModule 29 (P3) — Multimodal AI (Text + Image + Audio + Video). Tools focus: GPT-4V, Gemini, Pika, ElevenLabs. Core path — prioritize in your sprint.Multimodal models accept images, audio, or video alongside text. Constraints include resolution limits, MIME handling, latency of uploads, and safety filters on media.
- Practice: Call a vision-capable model with three image types: chart, screenshot, photo.Compare text-only vs image+text answers on a diagram question.Handle oversized images: resize/compress pipeline with tests.Read provider limits on frames or duration for video inputs.Write privacy rules for user-uploaded media in logs and retention.
- Code: `# Module 29 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 29, "topic": "Multimodal AI (Text + Image + Audio`

#### P4 — Agent Fundamentals
**Purpose:** Architectures, planning, collaboration

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 30 | What Are AI Agents? Autonomous vs Semi-Auto | Core | LangChain, custom Python |
| 31 | Agent Architectures: ReAct, CAMEL, AutoGPT | Core | LangChain ReAct, AutoGPT |
| 32 | Goal Decomposition & Task Planning Algorithms | Core | LangGraph, custom planners |
| 33 | Decision-Making Policies for Agents | Core | LangGraph, state machines |
| 34 | Action Planning Loops & Execution | Core | LangGraph, ReAct pattern |
| 35 | Self-Reflection / Feedback Loops | Core | Reflexion, LangGraph |
| 36 | Multi-Agent Collaboration Patterns | Core | CrewAI, AutoGen, LangGraph |
