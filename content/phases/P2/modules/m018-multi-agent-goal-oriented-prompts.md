---
journey_id: '2.4'
module_num: 18
phase_code: P2
title: 'Multi-Agent & Goal-Oriented Prompts'
tools: 'CrewAI, AutoGen'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 2.4 — Multi-Agent & Goal-Oriented Prompts

**2.4 — Multi-Agent & Goal-Oriented Prompts** [Core] | Tools: `CrewAI, AutoGen`
- Learn: OverviewModule 18 (P2) — Multi-Agent & Goal-Oriented Prompts. Tools focus: CrewAI, AutoGen. Core path — prioritize in your sprint.Multi-agent prompting assigns roles (researcher, critic, writer) and coordinates hand-offs. Frameworks like CrewAI or AutoGen encode patterns, but the design principles are delegation, clear interfaces, and stop conditions.Focus on avoiding infinite chatter: budgets for rounds and explicit termination.
- Practice: Design three roles for one task; specify inputs/outputs per role as JSON fields.Run a minimal two-agent exchange in code or a framework; cap at three rounds.Log each hand-off; verify no duplicate work or contradictory assumptions.Add a critic step that checks format before final user-visible output.Retrospective: when would a single-agent prompt be simpler and safer?
- Code: `# Module 18 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 18, "topic": "Multi-Agent & Goal-Oriented Prompts`
