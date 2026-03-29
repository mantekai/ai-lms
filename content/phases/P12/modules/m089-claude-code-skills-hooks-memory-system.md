---
journey_id: '12.3'
module_num: 89
phase_code: P12
title: 'Claude Code: Skills, Hooks & Memory System'
tools: 'Claude Code skills, hooks'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 12.3 — Claude Code: Skills, Hooks & Memory System

**12.3 — Claude Code: Skills, Hooks & Memory System** [Core] | Tools: `Claude Code skills, hooks`
- Learn: OverviewModule 89 (P12) — Claude Code: Skills, Hooks & Memory System. Tools focus: Claude Code skills, hooks. Core path — prioritize in your sprint.Hooks intercept tool lifecycle events; skills package repeatable workflows. Together they reduce drift between developers using the same repo.
- Practice: Configure one hook (pre-tool or post-edit) with safe logging only.Author one skill file for a repetitive task (e.g. migration checklist).Share skill with peer; gather usability feedback.Version skills in git; review changes via PR.List hook failure modes and fallbacks if hook crashes.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
