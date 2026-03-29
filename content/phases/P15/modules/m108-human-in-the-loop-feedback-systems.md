---
journey_id: '15.2'
module_num: 108
phase_code: P15
title: 'Human-in-the-Loop Feedback Systems'
tools: 'LangSmith, Argilla'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 15.2 — Human-in-the-Loop Feedback Systems

**15.2 — Human-in-the-Loop Feedback Systems** [Core] | Tools: `LangSmith, Argilla`
- Learn: OverviewModule 108 (P15) — Human-in-the-Loop Feedback Systems. Tools focus: LangSmith, Argilla. Core path — prioritize in your sprint.Human-in-the-loop feedback (Argilla, LangSmith datasets) closes the gap between automatic scores and user satisfaction — design lightweight rubrics.
- Practice: Create 20-row eval set with binary thumbs up/down reason codes.Run blind comparison two model versions; aggregate preference.Ensure annotators see identical prompts (counter bias).Export labeled set for fine-tune or prompt iteration.Document inter-rater drift over time.
- Code: `# Module 108 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 108, "topic": "Human-in-the-Loop Feedback System`
