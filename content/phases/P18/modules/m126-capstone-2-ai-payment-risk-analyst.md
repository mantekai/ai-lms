---
journey_id: '18.2'
module_num: 126
phase_code: P18
title: 'CAPSTONE 2: AI Payment Risk Analyst'
tools: 'RAG, compliance logic, FastAPI'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 18.2 — CAPSTONE 2: AI Payment Risk Analyst

**18.2 — CAPSTONE 2: AI Payment Risk Analyst** [Core] | Tools: `RAG, compliance logic, FastAPI`
- Learn: OverviewModule 126 (P18) — CAPSTONE 2: AI Payment Risk Analyst. Tools focus: RAG, compliance logic, FastAPI. Core path — prioritize in your sprint.Capstone 2: payment risk analyst blends RAG over policy docs, structured rules, and human escalation — emphasise audit trails and non-hallucinated citations.
- Practice: Ingest policy corpuses with metadata (version, jurisdiction).Force citation snippets in model answers; validate existence.Implement risk score + threshold routing to human review.Add eval set of historical cases (synthetic if needed).Threat-model data leakage between tenants.
- Code: `# Module 126 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 126, "topic": "CAPSTONE 2: AI Payment Risk Analy`
