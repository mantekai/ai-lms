---
journey_id: '12.4'
module_num: 90
phase_code: P12
title: 'Claude Code: 4-Layer Architecture'
tools: 'CLAUDE.md, Skills, Hooks, Agents'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 12.4 — Claude Code: 4-Layer Architecture

**12.4 — Claude Code: 4-Layer Architecture** [Core] | Tools: `CLAUDE.md, Skills, Hooks, Agents`
- Learn: OverviewModule 90 (P12) — Claude Code: 4-Layer Architecture. Tools focus: CLAUDE.md, Skills, Hooks, Agents. Core path — prioritize in your sprint.Four-layer mental model: project memory (CLAUDE.md), skills, hooks, subagents/specialists. Align layers so instructions do not contradict.
- Practice: Produce a single-page diagram of the four layers for your main repo. Highlight one contradiction you resolved between CLAUDE.md and a skill, and how you fixed it. Completion = diagram + short write-up; no extra install beyond your existing Claude Code setup.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
