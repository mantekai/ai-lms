---
journey_id: '10.3'
module_num: 77
phase_code: P10
title: 'Identity & Agent Security Layer'
tools: 'Teleport, cryptographic identity'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 10.3 — Identity & Agent Security Layer

**10.3 — Identity & Agent Security Layer** [Core] | Tools: `Teleport, cryptographic identity`
- Learn: OverviewModule 77 (P10) — Identity & Agent Security Layer. Tools focus: Teleport, cryptographic identity. Core path — prioritize in your sprint.Agent identity ties to machine IDs, SPIFFE/SPIRE concepts, or vendor features like Teleport Machine ID — goal is cryptographic proof of which workload spoke.
- Practice: Read high-level zero-trust agent identity blog/docs.List three attacks weak identity enables (spoof, replay).Sketch rotation for agent credentials (short-lived certs).Map identity to audit logs for tool calls.Tabletop: stolen agent credential response.
- Code: `# Module 77 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 77, "topic": "Identity & Agent Security Layer", "`
