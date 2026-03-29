---
journey_id: '9.3'
module_num: 72
phase_code: P9
title: 'Task Delegation & Result Artifacts'
tools: 'A2A tasks, Python SDK'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 9.3 — Task Delegation & Result Artifacts

**9.3 — Task Delegation & Result Artifacts** [Core] | Tools: `A2A tasks, Python SDK`
- Learn: OverviewModule 72 (P9) — Task Delegation & Result Artifacts. Tools focus: A2A tasks, Python SDK. Core path — prioritize in your sprint.Task delegation passes structured work items between agents; artifacts carry results (files, JSON, structured reports). Idempotency and correlation IDs matter across hops.
- Practice: Define task schema fields you would require (id, deadline, inputs).Simulate two-agent handoff with mocked HTTP; log correlation IDs.Handle partial failure: who retries, who compensates?Store artifacts in object storage vs inline JSON — decide per size.Write SLO for end-to-end task latency.
- Code: `# Module 72 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 72, "topic": "Task Delegation & Result Artifacts"`
