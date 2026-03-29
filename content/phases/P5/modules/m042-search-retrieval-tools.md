---
journey_id: '5.6'
module_num: 42
phase_code: P5
title: 'Search & Retrieval Tools'
tools: 'Tavily, SerpAPI, DuckDuckGo'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 5.6 — Search & Retrieval Tools

**5.6 — Search & Retrieval Tools** [Core] | Tools: `Tavily, SerpAPI, DuckDuckGo`
- Learn: OverviewModule 42 (P5) — Search & Retrieval Tools. Tools focus: Tavily, SerpAPI, DuckDuckGo. Core path — prioritize in your sprint.Browsing tools (Playwright, Firecrawl) render pages and extract content — fragile vs layout changes and heavy on resources. Prefer structured APIs when available.
- Practice: Fetch one static page and one SPA; note differences in extraction quality.Set navigation timeouts and user-agent responsibly.Strip scripts and ads before sending text to the model.Respect robots.txt for public projects; note legal nuance.Fallback path when page load fails mid-task.
- Code: `# Module 42 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 42, "topic": "Search & Retrieval Tools", "status"`
