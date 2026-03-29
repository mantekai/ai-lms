---
journey_id: '10.7'
module_num: 81
phase_code: P10
title: 'RBAC & Securing AI Agents (Cryptographic ID)'
tools: 'RBAC, Teleport, policy engines'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 10.7 — RBAC & Securing AI Agents (Cryptographic ID)

**10.7 — RBAC & Securing AI Agents (Cryptographic ID)** [Core] | Tools: `RBAC, Teleport, policy engines`
- Learn: OverviewModule 81 (P10) — RBAC & Securing AI Agents (Cryptographic ID). Tools focus: RBAC, Teleport, policy engines. Core path — prioritize in your sprint.RBAC for agents binds roles to tool permissions and data scopes. Cryptographic identity ties policy enforcement to workloads, not just API keys in env vars.
- Practice: Write RBAC matrix: roles × tools × data classes.Map Auth0/Clerk-style JWT claims to agent permissions.Test deny path when role lacks a tool.Integrate short-lived identity document for agent pod.Review OWASP authorization cheat sheet; note two gaps you will close.
- Code: `# Module 81 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 81, "topic": "RBAC & Securing AI Agents (Cryptogr`

#### P11 — Fine-Tuning
**Purpose:** LoRA, PEFT, data prep, evaluation

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 82 | Fine-Tuning Fundamentals & When to Use It | Core | Hugging Face, OpenAI fine-tune |
| 83 | LoRA & QLoRA (Efficient Fine-Tuning) | Core | PEFT, bitsandbytes, LoRA |
| 84 | PEFT: Parameter Efficient Fine-Tuning | Core | PEFT library, HF Transformers |
| 85 | Training Data Preparation & Curation | Core | datasets, Argilla, Label Studio |
| 86 | Domain Adaptation & Model Evaluation | Opt | ROUGE, BERTScore, Eleuther LM Eval |
