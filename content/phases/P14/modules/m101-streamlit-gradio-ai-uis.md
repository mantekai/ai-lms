---
journey_id: '14.2'
module_num: 101
phase_code: P14
title: 'Streamlit & Gradio — AI UIs'
tools: 'Streamlit, Gradio'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 14.2 — Streamlit & Gradio — AI UIs

**14.2 — Streamlit & Gradio — AI UIs** [Core] | Tools: `Streamlit, Gradio`
- Learn: OverviewModule 101 (P14) — Streamlit & Gradio — AI UIs. Tools focus: Streamlit, Gradio. Core path — prioritize in your sprint.Streamlit and Gradio ship demos fast; they differ in layout models and auth story. Neither replaces hardened multi-tenant auth without extra work.
- Practice: Build Streamlit chat UI calling your FastAPI mock.Add Gradio variant with same backend.Compare session state handling.Host locally with HTTPS tunnel (e.g. cloudflared) for demo only.List production gaps: auth, rate limits, logging.
- Code: `# Module 101 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 101, "topic": "Streamlit & Gradio — AI UIs", "st`
