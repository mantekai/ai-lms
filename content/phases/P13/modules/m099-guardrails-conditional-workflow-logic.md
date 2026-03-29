---
journey_id: '13.5'
module_num: 99
phase_code: P13
title: 'Guardrails & Conditional Workflow Logic'
tools: 'LangGraph conditionals, n8n'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 13.5 — Guardrails & Conditional Workflow Logic

**13.5 — Guardrails & Conditional Workflow Logic** [Core] | Tools: `LangGraph conditionals, n8n`
- Learn: OverviewModule 99 (P13) — Guardrails & Conditional Workflow Logic. Tools focus: LangGraph conditionals, n8n. Core path — prioritize in your sprint.Conditional logic and guardrails in automation prevent runaway AI calls — caps on tokens, approvals on writes, and circuit breakers on error rates.
- Practice: Add branch on HTTP status in a flow.Cap OpenAI node max tokens and concurrency.Insert human approval email/Slack before payment action (mock).Simulate 5xx storm; verify breaker stops spam.Document rollback for partially executed scenario.
- Code: `# Module 99 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 99, "topic": "Guardrails & Conditional Workflow L`

#### P14 — Production AI
**Purpose:** APIs, Docker, hosting, serverless

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 100 | FastAPI — Production API for AI Systems | Core | FastAPI, Pydantic, uvicorn |
| 101 | Streamlit & Gradio — AI UIs | Core | Streamlit, Gradio |
| 102 | Serverless Functions for AI | Core | AWS Lambda, Vercel Edge, Modal |
| 103 | Docker for AI Systems | Core | Docker, docker-compose |
| 104 | Kubernetes for AI Scale | Opt | Kubernetes, Helm, k8s |
| 105 | Vector DB Hosting & Management | Core | Pinecone cloud, Weaviate cloud |
| 106 | Agent Hosting: Replit, Modal, Fly.io | Core | Replit, Modal, Fly.io |
