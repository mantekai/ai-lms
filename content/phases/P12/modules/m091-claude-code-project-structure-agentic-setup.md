---
journey_id: '12.5'
module_num: 91
phase_code: P12
title: 'Claude Code: Project Structure (Agentic Setup)'
tools: 'agentic project scaffold'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 12.5 — Claude Code: Project Structure (Agentic Setup)

**12.5 — Claude Code: Project Structure (Agentic Setup)** [Core] | Tools: `agentic project scaffold`
- Learn: OverviewModule 91 (P12) — Claude Code: Project Structure (Agentic Setup). Tools focus: agentic project scaffold. Core path — prioritize in your sprint.Agentic project structure separates prompts, tools, evals, and runtime config. Scaffold early so AI assistants do not sprawl files randomly.
- Practice: Create directories: prompts/, tools/, eval/, config/.Add README explaining boundaries.Move one messy script into proper module + tests.Add pre-commit for format + lint.Have another human navigate the tree without help — time them.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
