---
journey_id: '10.4'
module_num: 78
phase_code: P10
title: 'Observability: Logs, Traces, Metrics'
tools: 'LangSmith, OpenTelemetry'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 10.4 — Observability: Logs, Traces, Metrics

**10.4 — Observability: Logs, Traces, Metrics** [Core] | Tools: `LangSmith, OpenTelemetry`
- Learn: OverviewModule 78 (P10) — Observability: Logs, Traces, Metrics. Tools focus: LangSmith, OpenTelemetry. Core path — prioritize in your sprint.Observability triad: structured logs, traces, metrics. LLM apps add prompt/response spans, token counters, and evaluator scores — scrub PII before export.
- Practice: Emit JSON logs with trace_id on one multi-step run.View trace in LangSmith or Jaeger tutorial.Add three RED metrics definitions for your API.Test log sampling under load.Document retention aligned to compliance policy.
- Code: `# Module 78 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 78, "topic": "Observability: Logs, Traces, Metric`
