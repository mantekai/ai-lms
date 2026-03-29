---
journey_id: '15.5'
module_num: 111
phase_code: P15
title: 'Auto-Evaluation Loops'
tools: 'LLM-as-judge, custom eval chains'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 15.5 — Auto-Evaluation Loops

**15.5 — Auto-Evaluation Loops** [Core] | Tools: `LLM-as-judge, custom eval chains`
- Learn: OverviewModule 111 (P15) — Auto-Evaluation Loops. Tools focus: LLM-as-judge, custom eval chains. Core path — prioritize in your sprint.Auto-evaluation loops run nightly evals, open PRs when regressions detected, or gate deploys — beware feedback loops where the judge model drifts.
- Practice: Design nightly job: sample prod queries → judge → dashboard.Choose judge model separate from production model.Add human spot-check percentage.Define rollback trigger thresholds.Document ethical limits on using user data in eval.
- Code: `# Module 111 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 111, "topic": "Auto-Evaluation Loops", "status":`
