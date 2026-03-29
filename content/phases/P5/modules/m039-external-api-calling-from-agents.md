---
journey_id: '5.3'
module_num: 39
phase_code: P5
title: 'External API Calling from Agents'
tools: 'requests, httpx, LangChain'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 5.3 — External API Calling from Agents

**5.3 — External API Calling from Agents** [Core] | Tools: `requests, httpx, LangChain`
- Learn: OverviewModule 39 (P5) — External API Calling from Agents. Tools focus: requests, httpx, LangChain. Core path — prioritize in your sprint.File tools read/write user or system files — highest risk surface. Sandboxed paths, extension allowlists, and size caps reduce exfiltration and destructive writes.
- Practice: Constrain reads to a single workspace directory in code.Reject symlinks escaping the workspace.Implement write with backup or dry-run mode.Test with oversized file and binary file edge cases.Describe how you’d add virus scanning for uploads in production.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
