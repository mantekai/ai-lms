---
journey_id: '10.5'
module_num: 79
phase_code: P10
title: 'Guardrails & Output Safety Systems'
tools: 'NeMo Guardrails, custom filters'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 10.5 — Guardrails & Output Safety Systems

**10.5 — Guardrails & Output Safety Systems** [Core] | Tools: `NeMo Guardrails, custom filters`
- Learn: OverviewModule 79 (P10) — Guardrails & Output Safety Systems. Tools focus: NeMo Guardrails, custom filters. Core path — prioritize in your sprint.Guardrails span input classifiers, output validators, topic allowlists, and NeMo-style policy YAML. Combine deterministic checks with model-based judges sparingly (cost).
- Practice: Implement regex + length guard on user input.Add LLM moderation or policy call on flagged subset only.Unit-test guard with adversarial prompts (synthetic).Measure latency impact of each layer.Define escalation path when guards disagree.
- Code: `# Module 79 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 79, "topic": "Guardrails & Output Safety Systems"`
