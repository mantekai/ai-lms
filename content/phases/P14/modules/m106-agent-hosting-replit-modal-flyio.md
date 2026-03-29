---
journey_id: '14.7'
module_num: 106
phase_code: P14
title: 'Agent Hosting: Replit, Modal, Fly.io'
tools: 'Replit, Modal, Fly.io'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 14.7 — Agent Hosting: Replit, Modal, Fly.io

**14.7 — Agent Hosting: Replit, Modal, Fly.io** [Core] | Tools: `Replit, Modal, Fly.io`
- Learn: OverviewModule 106 (P14) — Agent Hosting: Replit, Modal, Fly.io. Tools focus: Replit, Modal, Fly.io. Core path — prioritize in your sprint.Agent hosting platforms (Replit, Modal, Fly.io) differ in GPU access, sleep policies, and outbound network. Pick based on workload wake latency and compliance.
- Practice: Deploy stub agent HTTP service to one platform.Measure cold start and keep-warm trade-offs.Configure secrets and environment promotion.Test outbound allowlist if required by security.Document egress data paths for privacy review.
- Code: `# Module 106 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 106, "topic": "Agent Hosting: Replit, Modal, Fly`

#### P15 — Monitoring & Eval
**Purpose:** RAGAS, LangSmith, OpenTelemetry

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 107 | Agent Evaluation Metrics & Benchmarks | Core | RAGAS, TruLens, custom evals |
| 108 | Human-in-the-Loop Feedback Systems | Core | LangSmith, Argilla |
| 109 | LangSmith — Tracing & Debugging LLM Apps | Core | LangSmith, LangChain |
| 110 | OpenTelemetry for AI Observability | Core | OpenTelemetry, Jaeger |
| 111 | Auto-Evaluation Loops | Core | LLM-as-judge, custom eval chains |
| 112 | Prometheus & Grafana for AI Metrics | Opt | Prometheus, Grafana dashboards |
