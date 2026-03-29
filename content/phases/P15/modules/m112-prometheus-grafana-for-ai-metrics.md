---
journey_id: '15.6'
module_num: 112
phase_code: P15
title: 'Prometheus & Grafana for AI Metrics'
tools: 'Prometheus, Grafana dashboards'
priority: 'OPTIONAL'
source: content/curriculum/section-6-modules.md
---

# 15.6 — Prometheus & Grafana for AI Metrics

**15.6 — Prometheus & Grafana for AI Metrics** [Optional] | Tools: `Prometheus, Grafana dashboards`
- Learn: OverviewModule 112 (P15) — Prometheus & Grafana for AI Metrics. Tools focus: Prometheus, Grafana dashboards. Optional depth — revisit when you need this specialty.Prometheus scrapes metrics; Grafana dashboards visualize SLOs. LLM-specific panels might track tokens, latency, error codes, and judge scores.
- Practice: Stand up or follow a tutorial stack with Prometheus + Grafana; import a starter dashboard; add one custom panel for LLM proxy latency p95. If you cannot run Docker locally, complete the module with a written dashboard spec and PromQL queries you would use.
- Code: `# Module 112 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 112, "topic": "Prometheus & Grafana for AI Metri`

#### P16 — Security & Governance
**Purpose:** Injection, secrets, RBAC, privacy

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 113 | Prompt Injection Detection & Protection | Core | Rebuff, custom guards, NeMo |
| 114 | API Key Management & Secret Rotation | Core | Vault, AWS Secrets Manager |
| 115 | User Authentication & RBAC | Core | Auth0, Clerk, FastAPI security |
| 116 | Output Filtering & Content Safety | Core | OpenAI moderation, custom filters |
| 117 | Red Team Testing for AI Systems | Core | PyRIT, garak, manual red-teaming |
| 118 | Data Privacy, AI Alignment & Compliance | Core | GDPR frameworks, AI Act basics |
