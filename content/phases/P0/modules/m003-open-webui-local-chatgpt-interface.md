---
journey_id: '0.3'
module_num: 3
phase_code: P0
title: 'Open WebUI — Local ChatGPT Interface'
tools: 'Open WebUI, Docker'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 0.3 — Open WebUI — Local ChatGPT Interface

**0.3 — Open WebUI — Local ChatGPT Interface** [Core] | Tools: `Open WebUI, Docker`
- Learn: OverviewModule 3 (P0) — Open WebUI — Local ChatGPT Interface. Tools focus: Open WebUI, Docker. Core path — prioritize in your sprint.Open WebUI is a browser front-end for many backends (Ollama, OpenAI-compatible proxies). Docker is the common install path; you get multi-user patterns, model switching, and optional RAG plugins depending on build.Focus on operational concerns: volume mounts for persistence, upgrading images, and separating internal vs external network exposure if you demo on a lap
- Practice: Run Open WebUI via the documented Docker command; confirm the UI loads on localhost.Connect the UI to your local Ollama or LM Studio backend; send test chats through both.Create two model presets (e.g. fast vs quality) and document when you would use each.Back up or note the Docker volume path so you can recreate the environment.List one limitation you hit (auth, plugins, model list) and how you w
- Code: `# Module 3 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 3, "topic": "Open WebUI — Local ChatGPT Interface"`
