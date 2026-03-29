---
journey_id: '12.2'
module_num: 88
phase_code: P12
title: 'Claude Code: Setup, CLAUDE.md & Workflow'
tools: 'Claude Code CLI, CLAUDE.md'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 12.2 — Claude Code: Setup, CLAUDE.md & Workflow

**12.2 — Claude Code: Setup, CLAUDE.md & Workflow** [Core] | Tools: `Claude Code CLI, CLAUDE.md`
- Learn: OverviewModule 88 (P12) — Claude Code: Setup, CLAUDE.md & Workflow. Tools focus: Claude Code CLI, CLAUDE.md. Core path — prioritize in your sprint.Claude Code CLI uses project context files (CLAUDE.md), skills, and hooks to standardise behaviour across sessions — treat it like onboarding docs for a junior dev.
- Practice: Install Claude Code per vendor docs; create CLAUDE.md with stack + commands.Add repo map: directories, owners, test entrypoints.Run one guided task: fix lint + add test using the tool.Document which files the tool may edit vs forbid.Snapshot lessons learned in team wiki (redacted).
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
