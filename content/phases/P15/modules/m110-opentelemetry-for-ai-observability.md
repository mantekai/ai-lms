---
journey_id: '15.4'
module_num: 110
phase_code: P15
title: 'OpenTelemetry for AI Observability'
tools: 'OpenTelemetry, Jaeger'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 15.4 — OpenTelemetry for AI Observability

**15.4 — OpenTelemetry for AI Observability** [Core] | Tools: `OpenTelemetry, Jaeger`
- Learn: OverviewModule 110 (P15) — OpenTelemetry for AI Observability. Tools focus: OpenTelemetry, Jaeger. Core path — prioritize in your sprint.OpenTelemetry standardises traces/metrics/logs export to Jaeger, Grafana, etc. Auto-instrument HTTP clients/servers first.
- Practice: Add OTel SDK to FastAPI service.Export traces to local Jaeger or Grafana stack.Create span around LLM HTTP call with attributes (model, not content).Add metric counter for tool errors.Verify sampling rate under load test.
- Code: `# Module 110 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 110, "topic": "OpenTelemetry for AI Observabilit`
