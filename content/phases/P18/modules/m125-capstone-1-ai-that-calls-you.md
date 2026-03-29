---
journey_id: '18.1'
module_num: 125
phase_code: P18
title: 'CAPSTONE 1: AI That Calls You'
tools: 'LangGraph, Twilio, FastAPI'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 18.1 — CAPSTONE 1: AI That Calls You

**18.1 — CAPSTONE 1: AI That Calls You** [Core] | Tools: `LangGraph, Twilio, FastAPI`
- Learn: OverviewModule 125 (P18) — CAPSTONE 1: AI That Calls You. Tools focus: LangGraph, Twilio, FastAPI. Core path — prioritize in your sprint.Capstone 1: outbound voice or call experience using LangGraph orchestration, Twilio (or similar) telephony, and FastAPI webhooks — focus on state machine for call flows and PCI-adjacent caution.
- Practice: Define user story: who is called, when, and with what consent.Sketch call state machine (ringing, in-progress, escalate).Prototype webhook → LLM → TwiML response in dev environment.Add logging without recording sensitive audio in clear text.Document compliance checklist (consent, opt-out, retention).
- Code: `# Module 125 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 125, "topic": "CAPSTONE 1: AI That Calls You", "`
