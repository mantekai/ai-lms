<!-- Extracted from content/spec/agentiq_platform_spec.md — run: python3 scripts/extract_platform_docs.py — Manish.AI -->

## 9. AI AGENT SYSTEM

### 9.1 Agent Registry

| ID | Name | Role | Trigger | Output |
|----|------|------|---------|--------|
| AGT-01 | Content Research Agent | Researches new AI topics daily | Daily cron 6am | Draft new topics/sections for curator queue |
| AGT-02 | Content Writer Agent | Writes full module content | Triggered by AGT-01 or admin | Draft Learn/Practice/Code/References content |
| AGT-03 | Quiz Generator Agent | Generates quiz questions | On new content publish | 5-10 questions per module/section |
| AGT-04 | Feedback Response Agent | Responds to topic feedback | Hourly, new feedback queue | In-app reply to learner feedback (labeled AI Agent) |
| AGT-05 | Content Improvement Agent | Analyzes feedback patterns | Weekly | Improvement suggestions, flags stale content |
| AGT-06 | Triage Agent | Triages platform improvement suggestions | On new suggestion | Accept/Defer/Clarify decision + reasoning |
| AGT-07 | Ticket Executor Agent | Executes accepted improvement tickets | On ticket assignment | Content updates, new sections (to curator queue) |
| AGT-08 | News Curator Agent | Curates AI news feed | Daily cron 7am | Summarized news items with tags and module links |
| AGT-09 | Capstone Reviewer Agent | Reviews capstone submissions | On submission | Structured feedback + pass/fail (labeled AI Agent) |
| AGT-10 | Recommendation Agent | Personalizes learning paths | On login / module complete | Next module recommendation |
| AGT-11 | Notification Agent | Sends notifications | Event-driven | Email, in-app, push notifications |
| AGT-12 | Analytics Agent | Generates insights from usage data | Weekly | Admin reports, at-risk learner alerts |
| AGT-13 | Curriculum Gap Agent | Identifies missing topics | Weekly | Gap report for admin/curator review |
| AGT-14 | Staleness Agent | Flags outdated content | Weekly | List of modules needing review |

### 9.2 Agent Transparency Rule
Every output from every agent that is visible to learners MUST be labeled:
- "AI Agent Response" on feedback replies
- "AI Agent Review" on capstone feedback
- "AI Recommended" on learning path suggestions
- "AI Curated" on news items
This is non-negotiable. Learners always know when they are interacting with an AI agent.

### 9.3 Agent Workflows

**AGT-01 + AGT-02: Content Growth Pipeline**


**AGT-04 + AGT-05: Feedback Loop**


**AGT-06 + AGT-07: Improvement Triage & Execution**


**AGT-08: News Pipeline**


**AGT-13: Curriculum Gap Detection**


**AGT-14: Staleness Detection**


### 9.4 Agent Observability Dashboard (Admin)

- FR-AGNT-01: Real-time agent status board — all 14 agents with status (Idle/Running/Error/Paused)
- FR-AGNT-02: Per-agent task queue — current task, queue depth, last completed, avg duration
- FR-AGNT-03: Agent activity log — timestamped log of every action by every agent
- FR-AGNT-04: Agent performance metrics — tasks/day, error rate, avg response time
- FR-AGNT-05: Manual override — admin can pause/resume/restart any agent
- FR-AGNT-06: Task injection — admin can manually create a task and assign to any agent
- FR-AGNT-07: Agent error alerts — Slack/email when any agent errors 3+ times in an hour
- FR-AGNT-08: Content pipeline view — all drafts in review queue with status and curator
- FR-AGNT-09: Ticket board — Kanban view (Queued > In Progress > Review > Done/Deferred)
- FR-AGNT-10: Agent cost tracking — token usage and estimated cost per agent per day
- FR-AGNT-11: Agent output quality metrics — feedback helpful rate, content acceptance rate



---
