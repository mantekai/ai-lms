---
journey_id: '14.3'
module_num: 102
phase_code: P14
title: 'Serverless Functions for AI'
tools: 'AWS Lambda, Vercel Edge, Modal'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 14.3 — Serverless Functions for AI

**14.3 — Serverless Functions for AI** [Core] | Tools: `AWS Lambda, Vercel Edge, Modal`
- Learn: OverviewModule 102 (P14) — Serverless Functions for AI. Tools focus: AWS Lambda, Vercel Edge, Modal. Core path — prioritize in your sprint.Serverless (Lambda, Vercel, Modal) scales to zero but has cold starts and payload limits. Modal suits GPU jobs; Lambda suits thin orchestration.
- Practice: Deploy hello function to one serverless platform.Measure cold start p95 with simple load test.Set env vars + secrets via platform mechanism.Define max payload and timeout appropriate for LLM proxy.Cost estimate for 1M invocations/month at your memory setting.
- Code: `# Module 102 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 102, "topic": "Serverless Functions for AI", "st`
