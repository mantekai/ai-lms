---
journey_id: '14.5'
module_num: 104
phase_code: P14
title: 'Kubernetes for AI Scale'
tools: 'Kubernetes, Helm, k8s'
priority: 'OPTIONAL'
source: content/curriculum/section-6-modules.md
---

# 14.5 — Kubernetes for AI Scale

**14.5 — Kubernetes for AI Scale** [Optional] | Tools: `Kubernetes, Helm, k8s`
- Learn: OverviewModule 104 (P14) — Kubernetes for AI Scale. Tools focus: Kubernetes, Helm, k8s. Optional depth — revisit when you need this specialty.Kubernetes schedules GPU workloads, autoscaling, and config maps — operational overhead is real. Helm charts help but require cluster expertise.
- Practice: Read pod/resource requests vs limits for GPU pods.Sketch Deployment + Service + Ingress for your API.Plan config via ConfigMap vs Secret for keys.Understand HPA signals beyond CPU (custom metrics).Write when you would stay on VMs vs k8s for a client MVP.
- Code: `# Module 104 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 104, "topic": "Kubernetes for AI Scale", "status`
