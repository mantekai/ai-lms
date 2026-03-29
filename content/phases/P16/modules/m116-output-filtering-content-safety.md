---
journey_id: '16.4'
module_num: 116
phase_code: P16
title: 'Output Filtering & Content Safety'
tools: 'OpenAI moderation, custom filters'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 16.4 — Output Filtering & Content Safety

**16.4 — Output Filtering & Content Safety** [Core] | Tools: `OpenAI moderation, custom filters`
- Learn: OverviewModule 116 (P16) — Output Filtering & Content Safety. Tools focus: OpenAI moderation, custom filters. Core path — prioritize in your sprint.Output filtering blocks PII leaks, toxic content, or policy violations — combine provider moderation APIs with local regex for formats.
- Practice: Call moderation API on five synthetic outputs.Add local redact for credit-card-like patterns.Define fallback message when content blocked.Measure added latency.Human review queue for borderline cases.
- Code: `# Module 116 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 116, "topic": "Output Filtering & Content Safety`
