---
journey_id: '16.5'
module_num: 117
phase_code: P16
title: 'Red Team Testing for AI Systems'
tools: 'PyRIT, garak, manual red-teaming'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 16.5 — Red Team Testing for AI Systems

**16.5 — Red Team Testing for AI Systems** [Core] | Tools: `PyRIT, garak, manual red-teaming`
- Learn: OverviewModule 117 (P16) — Red Team Testing for AI Systems. Tools focus: PyRIT, garak, manual red-teaming. Core path — prioritize in your sprint.Red teaming uses tools like PyRIT/garak plus manual creativity to find jailbreaks and data exfil paths — schedule before major launches.
- Practice: Run garak or PyRIT quick scan on a test model endpoint.Document five findings with severity and repro steps.Track fixes in issue tracker with retest dates.Invite non-author to attempt jailbreak (fresh eyes).Define sign-off criteria for GA.
- Code: `# Module 117 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 117, "topic": "Red Team Testing for AI Systems",`
