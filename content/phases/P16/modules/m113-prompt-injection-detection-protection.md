---
journey_id: '16.1'
module_num: 113
phase_code: P16
title: 'Prompt Injection Detection & Protection'
tools: 'Rebuff, custom guards, NeMo'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 16.1 — Prompt Injection Detection & Protection

**16.1 — Prompt Injection Detection & Protection** [Core] | Tools: `Rebuff, custom guards, NeMo`
- Learn: OverviewModule 113 (P16) — Prompt Injection Detection & Protection. Tools focus: Rebuff, custom guards, NeMo. Core path — prioritize in your sprint.Prompt injection attempts to override system instructions via untrusted content — defenses include privilege separation, tool allowlists, and output policies.
- Practice: Reproduce a benign injection in a sandbox prompt.Move secrets and policies to system messages the user cannot edit.Add delimiter markers for untrusted document sections.Test Rebuff/regex guard if applicable.Write incident runbook if injection leads to data leak.
- Code: `# Module 113 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 113, "topic": "Prompt Injection Detection & Prot`
