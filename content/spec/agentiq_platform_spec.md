## TABLE OF CONTENTS

1. Executive Summary  
2. Problem Statement  
3. Vision & Guiding Philosophy  
4. Target Users & Personas  
5. The Living Content Model (Core Innovation)  
6. Full Curriculum Specification — 20 Phases, 133+ Modules  
7. Platform Features  
8. Gamification System — Levels, Badges, Streaks  
9. AI Agent System — 14 Agents  
10. Enterprise & Tenant Model  
11. AI Chatbot — Course Navigator  
12. AI News Feed  
13. Notification System  
14. Admin Panel  
15. Technical Architecture  
16. Content Versioning & Dynamic Completion  
17. Personalization & Adaptive Learning  
18. Certifications Catalog  
19. Capstone Projects  
20. Hackathons Catalog  
21. Open Source Contribution Targets  
22. YC-Style Startup Ideas  
23. Non-Functional Requirements  
24. Success Metrics  
25. Open Questions & Decisions  
26. Future Roadmap  

---

## 1. EXECUTIVE SUMMARY

AgentIQ is an AI-native, enterprise-grade Learning Management System purpose-built for AI education. Unlike static course platforms, AgentIQ is a **living platform** — its content grows autonomously via AI agents that research, write, and update topics daily. Students learn AI by interacting with AI. The platform runs on AI agents, is maintained by AI agents, and teaches people how to build AI agents.

**Core differentiators:**
- Content grows automatically — AI agents add new topics, sections, and modules daily
- A module marked complete today may have new sections tomorrow — progress is dynamic and honest
- AI agents handle feedback, triage improvements, respond to students, and file internal tickets
- Enterprise/tenant model — colleges, bootcamps, and companies can onboard entire cohorts
- Gamification: 10 learner levels (L1–L10), 100+ badges, streaks, leaderboards
- AI Chatbot interprets natural language queries and maps them to the right course/module
- Live AI News Feed curated by an agent monitoring X, arXiv, GitHub, and AI blogs daily
- Every AI agent interaction is transparently labeled — learners always know they are talking to an AI

---

## 2. PROBLEM STATEMENT

AI education is broken in three fundamental ways:

1. **Static content** — courses go stale within months as the AI landscape shifts weekly. A course on LangChain from 6 months ago may reference deprecated APIs.
2. **No personalization** — one-size-fits-all paths ignore where a learner actually is. A senior developer and a career switcher need different entry points.
3. **No feedback loop** — student confusion and improvement ideas disappear into a void. Nobody reads the feedback form.

AgentIQ solves all three: content is always current (agents update it), paths are adaptive (AI recommends next steps), and every piece of feedback is acted on by an AI agent within hours.

---

## 3. VISION & GUIDING PHILOSOPHY

**Vision:** The world's first AI learning platform that is itself built, maintained, and grown by AI agents — teaching people to build the same systems that run the platform.

**Guiding Philosophy (from Blueprint):**
- Hands-on first, production-oriented, portfolio-building focused
- Every module contains full explanations (not just links), exact implementation steps, ready-to-run code, and real-world use cases
- Completion of each phase provides career artifacts — LinkedIn post templates, resume bullet points, and portfolio pieces
- The shift we are teaching: Apps → Agents → Multi-Agent Systems → AI Infrastructure
- Design principle: Communication layer + Capability layer = Production AI

**Target Outcome for Learners:**
- Design, build, deploy, and sell AI systems end-to-end
- Master the full stack: LLM → Agents → Agentic AI → MCP → A2A → Production → Consulting
- Build a portfolio of capstone projects that are enterprise-grade
- Qualify for AI Consultant, AI Architect, or Agentic AI Engineer roles
- Complete 5+ globally recognised AI certifications

---

## 4. TARGET USERS & PERSONAS

### 4.1 Learner Personas

| Persona | Background | Goal | Entry Phase |
|---------|-----------|------|-------------|
| Career Switcher | Non-technical professional | AI Consultant role | P0 |
| Developer | Software engineer | Ship production AI systems | P1–P2 |
| Student | CS/Data Science undergrad | Portfolio + certifications | P0 |
| Enterprise Employee | Staff onboarded by company | Internal AI project skills | Custom path |
| AI Researcher | Advanced practitioner | Stay current, contribute | P8+ |
| Bootcamp Graduate | Recent coding bootcamp | Add AI to existing dev skills | P2 |

### 4.2 Admin Personas

| Persona | Responsibilities |
|---------|----------------|
| Platform Admin | Global content, AI agents, system health, all tenants |
| Tenant Admin | College/company cohort management, progress reports |
| Content Curator | Reviews AI agent-generated drafts before publish |
| AI Agent Supervisor | Monitors all 14 agents, task queues, errors |

---

## 5. THE LIVING CONTENT MODEL (CORE INNOVATION)

This is the most important architectural concept of AgentIQ. Content is **never frozen**.

### 5.1 Content Hierarchy
```
Platform
└── Phase (20 phases, P0–P19)
    └── Module (133+ modules, growing)
        └── Section (Learn · Practice · Code · Quiz · References)
            └── Topic (individual concept, tool, or exercise)
```

### 5.2 The Living Contract
- Any Topic, Section, or Module can receive new content at any time via AI agents or admin
- When new content is added to a module a learner has already completed:
  - Module status → **"Needs Review"** (not "Incomplete" — XP is preserved)
  - In-app notification: *"Module X has new content — review to stay current"*
  - Learner sees a **"What changed?"** diff view showing new/updated/removed topics
  - Learner re-checks new topics to restore "Complete" status
  - Quiz re-attempt is NOT required unless admin explicitly flags it
- Learners are never penalized — XP and badges are preserved, but the module badge requires re-acknowledgment of new content

### 5.3 Content Versioning
- Every Topic, Section, and Module has a `version` integer and `updated_at` timestamp
- Learner's Progress record stores `completed_at_module_version`
- On module page load: if `module.version > progress.completed_at_module_version` → show "Updated" banner
- Full version history per module: who changed what, when (human or which agent)
- Rollback to any previous version available to admins
- Scheduled publish: set future date/time for content to go live

### 5.4 Module Completion Definition
- Completion = learner has checked off all topics in Learn + Practice tabs
- Quiz passing is NOT required for completion (quiz is for self-assessment and XP bonus)
- Learner can mark individual topics complete as they go
- Module is "Complete" when all topics are checked

---

## 6. FULL CURRICULUM SPECIFICATION

Canonical **per-module** bodies live under **`content/phases/P*/modules/*.md`**.

A **single-file §6 archive** (for splitting and auditing): [`content/curriculum/section-6-modules.md`](../curriculum/section-6-modules.md). After editing it, run `python3 scripts/split_modules_one_file_each.py`.

Research and topic depth (**former §27–§73**): [`content/research/topic-and-extract-corpus.md`](../research/topic-and-extract-corpus.md). Regenerate `supplement.md` / `depth/` with `python3 scripts/build_learner_phase_corpus.py`.

---

## 7. PLATFORM FEATURES

### 7.1 Authentication & User Management

- FR-AUTH-01: Email/password registration with email verification
- FR-AUTH-02: OAuth login — Google, GitHub, LinkedIn
- FR-AUTH-03: SSO/SAML for enterprise tenants (Okta, Azure AD, Google Workspace)
- FR-AUTH-04: Roles — Learner, Tenant Admin, Content Curator, Platform Admin, AI Agent Supervisor
- FR-AUTH-05: Per-tenant user provisioning — bulk CSV upload, SCIM sync
- FR-AUTH-06: Session management, JWT tokens, refresh token rotation
- FR-AUTH-07: MFA for admin roles
- FR-AUTH-08: Transparent AI labeling — every AI agent interaction clearly labeled "AI Agent" so learners always know

### 7.2 Learner Dashboard

- FR-DASH-01: Global progress bar — X of N modules complete across all phases
- FR-DASH-02: Phase cards with per-phase completion % and progress bar
- FR-DASH-03: Current level (L1-L10) with XP bar showing progress to next level
- FR-DASH-04: Active streak counter (daily, weekly)
- FR-DASH-05: Recently earned badges (last 5)
- FR-DASH-06: "Continue where you left off" — last accessed module
- FR-DASH-07: "New content added" notification panel — modules with new sections since last visit
- FR-DASH-08: AI News Feed widget — latest 5 items from News Curator Agent
- FR-DASH-09: Recommended next module — AI-powered, based on current level and completion
- FR-DASH-10: Upcoming hackathon deadlines widget
- FR-DASH-11: Certification tracker summary — In Progress / Passed counts
- FR-DASH-12: Career readiness score (0-100%) based on weighted module completion
- FR-DASH-13: Skills unlocked panel — skills earned based on completed phases

### 7.3 Course Navigation

- FR-NAV-01: Left sidebar — collapsible phase list with modules inside each phase
- FR-NAV-02: Each module shows: number, title, completion status (checkmark/dot/circle), priority tag (Core/Optional), XP value
- FR-NAV-03: Phase-level progress bar in sidebar
- FR-NAV-04: "New" badge on modules with content added in last 7 days
- FR-NAV-05: "Updated" badge on modules where learner completion was reset due to new content
- FR-NAV-06: Full-text search across all module titles and topic names
- FR-NAV-07: Filter by Phase, Priority, Status, Level
- FR-NAV-08: Mobile-responsive — sidebar collapses to hamburger below 768px
- FR-NAV-09: 5 themes — Dark, Light, Ocean, Mint, Sunset (persisted to localStorage/DB)

### 7.4 Module Page

- FR-MOD-01: Module header — phase badge, module number, title, tools list, priority tag, XP value, estimated time
- FR-MOD-02: 5 tabs — Learn · Practice · Code · Quiz · References
- FR-MOD-03: Learn tab — full concept explanation, key terms highlighted, diagrams
- FR-MOD-04: Practice tab — ordered checklist of "done when..." criteria; each item checkable
- FR-MOD-05: Code tab — runnable starter code with syntax highlighting and copy button
- FR-MOD-06: Quiz tab — 5-10 questions per module; retake allowed; score shown; XP bonus on pass
- FR-MOD-07: References tab — official docs, tutorials, links (marked free/paid)
- FR-MOD-08: "Mark Complete" button — enabled when all Practice items checked
- FR-MOD-09: Completion triggers — XP award, badge check, streak update, confetti animation
- FR-MOD-10: Section-level completion tracking — each topic/section has its own checkbox
- FR-MOD-11: "New section added" inline banner when section added after learner last visit
- FR-MOD-12: "What changed?" diff view — new topics (green), updated (yellow), removed (red strikethrough)
- FR-MOD-13: Prev/Next module navigation
- FR-MOD-14: LinkedIn post draft auto-generated on module completion (copyable)
- FR-MOD-15: Resume bullet auto-generated on phase completion
- FR-MOD-16: Feedback widget on every topic/section (see 7.5)

### 7.5 Topic-Level Feedback System

- FR-FEED-01: Every topic/section has feedback widget — thumbs up/down + optional text
- FR-FEED-02: Feedback categories — "Unclear explanation", "Outdated content", "Missing example", "Wrong code", "Great content", "Needs more depth", "Other"
- FR-FEED-03: Feedback stored with user ID, topic ID, module ID, timestamp, category, text
- FR-FEED-04: Feedback Response Agent (AGT-04) reads new feedback hourly, posts reply within 24h
- FR-FEED-05: Every agent response clearly labeled "AI Agent Response" — learner always knows
- FR-FEED-06: Content Improvement Agent (AGT-05) analyzes patterns weekly — 3+ same-category flags on same topic triggers improvement suggestion
- FR-FEED-07: Learner sees agent response inline below their feedback
- FR-FEED-08: Learner can mark agent response as "Helpful" or "Not Helpful"
- FR-FEED-09: Feedback XP — +5 XP per feedback submitted (max 3/day to prevent gaming)
- FR-FEED-10: Feedback visible only to submitter and admins (not public by default)

### 7.6 Platform Improvement Suggestions

- FR-IMPV-01: "Suggest an Improvement" section accessible from any page
- FR-IMPV-02: Form — title, description, category (New Module/Phase/Feature/Bug/Other), priority
- FR-IMPV-03: Triage Agent (AGT-06) reviews each suggestion within 48h
- FR-IMPV-04: Triage decisions:
  - ACCEPT: creates internal ticket, assigns to AGT-07, status = "Queued"
  - DEFER: status = "Deferred" with written reasoning (e.g. "Out of scope", "Duplicate of #123")
  - NEEDS CLARIFICATION: agent posts question back to submitter
- FR-IMPV-05: Submitter notified of decision with full reasoning
- FR-IMPV-06: Public suggestion board — learners can upvote others suggestions
- FR-IMPV-07: Top-voted suggestions surfaced to Platform Admin weekly
- FR-IMPV-08: Status visible to submitter — Submitted > Under Review > Accepted/Deferred > In Progress > Done

### 7.7 Progress Tracking & Analytics

- FR-PROG-01: Per-module — Not Started / In Progress / Complete / Needs Review
- FR-PROG-02: Per-phase — % complete, modules done/total, estimated time remaining
- FR-PROG-03: Global — total modules, XP, level, streak, badges earned
- FR-PROG-04: Time tracking — time spent per module, per phase, total platform time
- FR-PROG-05: Quiz history — scores, attempts, improvement over time
- FR-PROG-06: Export progress — CSV download of all module completion data
- FR-PROG-07: Shareable progress card — auto-generated image for LinkedIn/X sharing
- FR-PROG-08: Career readiness score (0-100%) based on module completion weighted by priority
- FR-PROG-09: Portfolio tracker — learner adds GitHub repo links, deployed demo URLs per capstone

### 7.8 Certification Tracker

- FR-CERT-01: Full catalog of 42+ certifications (free + paid) with provider, cost, study phases, URL
- FR-CERT-02: Per-cert status — Not Started / In Progress / Passed
- FR-CERT-03: Target exam date picker with Google Calendar link
- FR-CERT-04: AI-generated study plan mapping cert domains to platform modules
- FR-CERT-05: Filter by cost (free/paid/mixed), provider, study phase
- FR-CERT-06: Cert ROI data — salary uplift estimates, job posting frequency
- FR-CERT-07: Badge awarded on marking cert as Passed
- FR-CERT-08: Reminder notifications — 7 days and 1 day before target exam date

### 7.9 Capstone Projects

- FR-CAP-01: 4 capstone projects with full specs — architecture, deliverables, starter code
- FR-CAP-02: Submission — GitHub repo URL + deployed demo URL + 2-min video link
- FR-CAP-03: Capstone Reviewer Agent (AGT-09) evaluates against rubric — architecture, code quality, README, deployment
- FR-CAP-04: Reviewer Agent response labeled "AI Agent Review" — learner knows it is AI
- FR-CAP-05: Structured feedback within 48h
- FR-CAP-06: Capstone badge awarded on passing review
- FR-CAP-07: Public capstone gallery — approved submissions visible to all learners (opt-in)
- FR-CAP-08: Capstone leaderboard — top-rated submissions per capstone



---

## 8. GAMIFICATION SYSTEM

### 8.1 Learner Levels (L1-L10)

| Level | Title | XP Required | Unlocked By |
|-------|-------|-------------|-------------|
| L1 | AI Curious | 0 | Registration |
| L2 | Prompt Crafter | 500 | Complete P0-P1 |
| L3 | API Builder | 1,500 | Complete P2-P3 |
| L4 | Agent Apprentice | 3,500 | Complete P4-P5 |
| L5 | Framework Engineer | 7,000 | Complete P6-P7 |
| L6 | Protocol Architect | 12,000 | Complete P8-P9 |
| L7 | Systems Designer | 20,000 | Complete P10-P12 |
| L8 | Production Engineer | 32,000 | Complete P13-P15 |
| L9 | AI Security Expert | 50,000 | Complete P16-P17 |
| L10 | Agentic AI Architect | 75,000 | All phases + 2 capstones |

**XP Sources:**
- Complete a topic: +10 XP
- Complete a module: +50 XP
- Complete a phase: +200 XP
- Pass a quiz (first attempt): +100 XP
- Pass a quiz (retry): +25 XP
- Submit capstone: +500 XP
- Submit feedback: +5 XP (max 3/day)
- Daily streak bonus: +20 XP/day
- Weekly streak bonus: +100 XP/week
- Badge earned: +25-200 XP (varies by badge)

### 8.2 Streak System

- **Daily Streak** — consecutive days with at least one topic completed
- **Weekly Streak** — 5+ topics completed in a week
- **Phase Streak** — completing a phase without skipping any Core module
- **Feedback Streak** — leaving feedback on 5+ topics in a week
- **Streak Freeze** — 1 free freeze per week (miss one day without breaking streak)
- Streak milestones trigger bonus XP and badges
- Streak shown on profile with flame icon and count

### 8.3 Badge System (100+ Badges)

**Completion Badges (20+):**
- First Module Complete, First Phase Complete
- 10 Modules, 25 Modules, 50 Modules, 100 Modules, 133 Modules Complete
- "Local AI Master" (P0 complete)
- "Prompt Wizard" (P2 complete)
- "Agent Architect" (P4 complete)
- "Tool Master" (P5 complete)
- "Framework Expert" (P6 complete)
- "RAG Engineer" (P7 complete)
- "MCP Builder" (P8 complete)
- "A2A Pioneer" (P9 complete)
- "Systems Thinker" (P10 complete)
- "Fine-Tuner" (P11 complete)
- "Vibe Coder" (P12 complete)
- "Automation Architect" (P13 complete)
- "Production Ready" (P14 complete)
- "Eval Expert" (P15 complete)
- "Security Guardian" (P16 complete)
- "AI Consultant" (P17 complete)
- "Capstone Champion" (all 3 capstones)
- "Full Stack AI" (all 20 phases complete)

**Speed Badges (10+):**
- "Speed Runner" (complete a module in under 30 min)
- "Phase Sprinter" (complete a phase in 7 days)
- "Weekend Warrior" (complete 5 modules in a weekend)
- "Marathon Runner" (complete 10 modules in one day)
- "Night Owl" (complete 10 modules between 10pm-2am)
- "Early Bird" (complete 10 modules before 7am)
- "Lunch Learner" (complete 5 modules between 12pm-1pm)

**Streak Badges (8+):**
- "3-Day Streak", "7-Day Streak", "30-Day Streak", "100-Day Streak", "365-Day Streak"
- "Comeback Kid" (return after 30-day gap and complete a module)
- "Unstoppable" (maintain streak through a freeze)
- "Consistent" (complete at least 1 module every day for 14 days)

**Quality Badges (10+):**
- "Perfect Score" (100% on a quiz first try)
- "Quiz Master" (10 perfect scores)
- "Feedback Champion" (50 feedbacks submitted)
- "Helpful Reviewer" (10 feedbacks marked helpful by agent)
- "Deep Diver" (complete all Optional modules in a phase)
- "Code Shipper" (submit all 4 capstones)
- "Deployed" (capstone publicly deployed and linked)

**Community Badges (10+):**
- "Early Adopter" (joined in first 90 days)
- "Beta Tester" (participated in beta)
- "Bug Hunter" (reported a valid bug)
- "Idea Champion" (suggestion accepted and shipped)
- "Upvoter" (upvoted 20 suggestions)
- "News Junkie" (read 50 news items)
- "Hackathon Entrant" (registered for a hackathon)
- "Open Source Contributor" (logged an OSS contribution)

**Certification Badges (15+):**
- One badge per certification passed (Google, AWS, NVIDIA, Microsoft, IBM, HuggingFace, etc.)
- "Cert Collector" (5 certs passed)
- "Certified AI Professional" (3 paid credentials passed)

**Level Badges (10):** One badge per level L1-L10

**Tenant Badges (custom):**
- Tenant admins can create custom badges (e.g. "BITS Pilani AI Scholar", "Infosys AI Champion")
- Awarded manually by Tenant Admin or auto-triggered by cohort completion

**Special Badges (10+):**
- "AI Native" (completed entire curriculum using only AI-assisted tools)
- "Local First" (completed P0-P7 using only local/free APIs)
- "Polyglot" (completed code exercises in 3+ languages)
- "Researcher" (read 100 news items)
- "Mentor" (helped 5 peers via discussion threads - Phase 2 feature)

### 8.4 Leaderboards

- Global leaderboard (XP-based, weekly/all-time)
- Tenant leaderboard (within college/company)
- Phase leaderboard (who completed a phase fastest)
- Streak leaderboard (longest current streak)
- Badge leaderboard (most badges earned)
- All leaderboards configurable by Tenant Admin (show/hide to learners)



---

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

## 10. ENTERPRISE & TENANT MODEL

- FR-TENT-01: Multi-tenant architecture — each tenant has isolated data, custom branding (logo, colors), custom domain (e.g. bits.agentiq.ai)
- FR-TENT-02: Tenant Admin can invite learners (bulk CSV / email), create cohorts, assign learning paths, set deadlines, view all learner progress
- FR-TENT-03: Cohort management — group learners, assign phase range or module list, set completion deadlines
- FR-TENT-04: Tenant-level leaderboard and progress reports
- FR-TENT-05: Tenant Admin dashboard — enrollment stats, completion rates, average scores, time-on-platform, top performers, at-risk learners (no activity in 7+ days)
- FR-TENT-06: Custom learning paths — Tenant Admin creates curated path (subset of modules) for their cohort
- FR-TENT-07: Tenant-specific announcements — broadcast messages to all learners in the tenant
- FR-TENT-08: White-label option — hide AgentIQ branding for enterprise tier
- FR-TENT-09: SSO integration per tenant (Okta, Azure AD, Google Workspace)
- FR-TENT-10: Tenant billing — per-seat pricing, annual/monthly, usage reports
- FR-TENT-11: Data isolation — tenant data never mixed; GDPR-compliant data residency options; row-level security at DB level
- FR-TENT-12: Tenant-level custom badges (e.g. college-specific achievement badges)
- FR-TENT-13: Tenant-level AI News Feed customization — Tenant Admin can add custom sources relevant to their domain
- FR-TENT-14: Export — download all learner progress as CSV/PDF
- FR-TENT-15: API access — tenant LMS integration (embed AgentIQ content in existing LMS) — Phase 3 feature

---

## 11. AI CHATBOT — COURSE NAVIGATOR

- FR-BOT-01: Persistent chat widget available on all pages (bottom-right)
- FR-BOT-02: Natural language query to course/module recommendation
  - Example: "I want to learn how to build an agent that can browse the web" -> recommends M43 (Web Browsing Tools), M34 (Action Planning Loops), M46 (LangGraph)
- FR-BOT-03: Diagnostic quiz mode — chatbot asks 3-5 questions to assess current level, then recommends a learning path
- FR-BOT-04: Topic search — "What is RAG?" returns definition + links to relevant modules
- FR-BOT-05: "What should I learn next?" — personalized recommendation based on completed modules and level
- FR-BOT-06: Certification guidance — "I want to get AWS AI Practitioner certified" returns study plan mapped to platform modules
- FR-BOT-07: Hackathon prep — "I want to enter the LangGraph hackathon" returns prep path and quick-start template
- FR-BOT-08: Full context of learner's progress, level, and completed modules
- FR-BOT-09: Can answer questions about module content (RAG over all module content)
- FR-BOT-10: Conversation history persisted per user
- FR-BOT-11: Escalation — if chatbot cannot answer, creates a feedback ticket for agent review
- FR-BOT-12: Always labeled "AI Chatbot" — learner always knows they are talking to an AI
- FR-BOT-13: Chatbot can explain the difference between any two topics (e.g. "What is the difference between MCP and A2A?")
- FR-BOT-14: Chatbot can generate a custom study plan for a stated goal and timeline

---

## 12. AI NEWS FEED

- FR-NEWS-01: Dedicated News Feed page accessible from sidebar
- FR-NEWS-02: News Curator Agent (AGT-08) runs daily — scrapes arXiv, X/Twitter (AI accounts), GitHub trending, HuggingFace blog, Anthropic/OpenAI/Google/LangChain blogs, The Batch, Import AI
- FR-NEWS-03: Each item: title, 2-sentence summary, source, date, relevance tags (which platform phases/modules it relates to)
- FR-NEWS-04: News items tagged by topic — #MCP, #Agents, #RAG, #FineTuning, #Security, #Tools, #Research, #Industry, #Protocols, #VibeCoding
- FR-NEWS-05: Learner can filter news by tag or search
- FR-NEWS-06: "Related modules" shown alongside each news item
- FR-NEWS-07: Learner can bookmark news items
- FR-NEWS-08: News widget on dashboard shows latest 5 items
- FR-NEWS-09: Weekly digest email — top 10 AI news items of the week, personalized by learner's current phase
- FR-NEWS-10: When a news item is highly relevant to a module, a "New Development" banner appears on that module page
- FR-NEWS-11: News items can trigger content update suggestions — if a tool is deprecated or new version released, agent flags the relevant module for review
- FR-NEWS-12: All news items labeled "AI Curated" — learners know the curation is AI-driven

---

## 13. NOTIFICATION SYSTEM

| Event | Channel | Timing |
|-------|---------|--------|
| New content added to completed module | In-app + Email | Immediate |
| Feedback response from AI agent | In-app | Within 24h |
| Improvement suggestion decision (Accept/Defer) | In-app + Email | Within 48h |
| Badge earned | In-app | Immediate |
| Level up | In-app + Email | Immediate |
| Streak at risk (no activity today) | Push + In-app | 8pm local time |
| Streak broken | In-app | Next login |
| Cert exam date reminder | Email | 7 days + 1 day before |
| Hackathon deadline reminder | In-app + Email | 7 days + 1 day before |
| Weekly AI news digest | Email | Every Monday 8am |
| Capstone review complete | In-app + Email | Within 48h |
| New module published in current phase | In-app | Immediate |
| Tenant announcement | In-app + Email | Immediate |
| At-risk alert (Tenant Admin) | Email | After 7 days inactivity |
| New suggestion upvoted (submitter) | In-app | When upvote count hits 5/10/25 |
| Suggestion ticket completed | In-app + Email | On completion |

---

## 14. ADMIN PANEL

### 14.1 Platform Admin
- FR-ADMIN-01: Content management — create/edit/delete phases, modules, sections, topics
- FR-ADMIN-02: Module versioning — every content change creates a version; rollback available
- FR-ADMIN-03: Publish workflow — Draft > Curator Review > Published
- FR-ADMIN-04: Bulk operations — reorder modules, move modules between phases, bulk publish
- FR-ADMIN-05: User management — view all users, roles, activity, ban/suspend
- FR-ADMIN-06: Tenant management — create/edit/suspend tenants, view per-tenant stats
- FR-ADMIN-07: Badge management — create custom badges, assign criteria, award manually
- FR-ADMIN-08: Analytics dashboard — DAU/MAU, completion rates, popular modules, drop-off points
- FR-ADMIN-09: AI Agent dashboard (see Section 9.4)
- FR-ADMIN-10: System health — API latency, DB performance, error rates, uptime
- FR-ADMIN-11: Feature flags — enable/disable features per tenant or globally
- FR-ADMIN-12: Announcement system — broadcast to all users or specific tenants
- FR-ADMIN-13: Content diff viewer — see exactly what changed between any two versions of a module
- FR-ADMIN-14: Scheduled publish — set future date/time for content to go live

### 14.2 Tenant Admin
- FR-TADMIN-01: Cohort management — create cohorts, add/remove learners
- FR-TADMIN-02: Custom learning path — select subset of modules, set order, set deadlines
- FR-TADMIN-03: Progress reports — per-learner and cohort-level completion, scores, time
- FR-TADMIN-04: At-risk alerts — learners with no activity in 7+ days
- FR-TADMIN-05: Leaderboard — tenant-scoped, configurable (show/hide to learners)
- FR-TADMIN-06: Announcements — broadcast to tenant learners
- FR-TADMIN-07: Custom badges — create tenant-specific badges
- FR-TADMIN-08: Export — download all learner progress as CSV/PDF
- FR-TADMIN-09: Billing — view seat usage, invoices, upgrade/downgrade plan



---

## 15. TECHNICAL ARCHITECTURE

### 15.1 System Overview

```
CLIENT LAYER
  Next.js 14 (App Router) | TypeScript | Tailwind CSS
  PWA-enabled | Web Push | Responsive (mobile-first)
  5 themes: Dark, Light, Ocean, Mint, Sunset

API LAYER
  FastAPI (Python) | REST + WebSocket | JWT Auth
  Rate limiting | Request validation (Pydantic)
  OpenAPI auto-docs

DATA LAYER
  PostgreSQL (primary data, row-level security for multi-tenancy)
  Redis (cache, sessions, task queues, pub/sub real-time)
  Vector DB: Chroma (dev) / Weaviate (prod) — RAG for chatbot
  Object Store: S3-compatible (MinIO self-host / AWS S3) — media, code files, exports

AI AGENT LAYER
  14 agents | LangGraph orchestration | Task queue (Redis)
  LLM: Claude API (primary) + Ollama (local fallback)
  Each agent: isolated context, tool access, full audit log
  All agent outputs to learners: labeled as AI-generated
```

### 15.2 Key Data Models

**Tenant** — id, name, slug, domain, branding_json, plan, settings_json, created_at
**User** — id, tenant_id, email, role, level, xp, streak_current, streak_longest, theme, created_at
**Phase** — id, code, name, purpose, icon, color, order, version, created_at
**Module** — id, phase_id, number, title, tools, priority, xp_value, version, published_at, updated_at
**Section** — id, module_id, type (learn/practice/code/quiz/references), content, version, created_at
**Topic** — id, section_id, title, content, order, version, created_at, updated_at
**Progress** — id, user_id, module_id, status, completed_at, completed_at_module_version, quiz_score, time_spent_seconds
**TopicProgress** — id, user_id, topic_id, completed, completed_at
**Badge** — id, name, description, icon, criteria_type, criteria_value, xp_bonus, tenant_id (null = global)
**UserBadge** — id, user_id, badge_id, earned_at
**Streak** — id, user_id, type, current_count, longest_count, last_activity_date, freeze_used_this_week
**Feedback** — id, user_id, topic_id, module_id, category, text, agent_response, agent_response_at, helpful, created_at
**Suggestion** — id, user_id, title, description, category, priority, status, agent_decision, reasoning, ticket_id, upvotes, created_at
**Ticket** — id, suggestion_id, assigned_agent_id, status, created_at, resolved_at, resolution_notes
**NewsItem** — id, title, summary, source_url, source_name, tags_json, related_module_ids_json, published_at, bookmarked_by_json
**AgentTask** — id, agent_id, type, payload_json, status, started_at, completed_at, error, token_cost
**AgentLog** — id, agent_id, task_id, action, details_json, timestamp
**Notification** — id, user_id, type, title, body, read, created_at
**Cohort** — id, tenant_id, name, learning_path_json, deadline, created_at
**CohortMember** — id, cohort_id, user_id, joined_at
**ContentVersion** — id, entity_type, entity_id, version, content_snapshot_json, changed_by, changed_by_type (human/agent), created_at
**CertTracker** — id, user_id, cert_id, status, target_exam_date, passed_at
**CapstoneSubmission** — id, user_id, capstone_id, github_url, demo_url, video_url, agent_review, score, status, submitted_at

### 15.3 Technology Decisions

| Component | Choice | Reason |
|-----------|--------|--------|
| Frontend | Next.js 14 (App Router) | SSR for SEO, RSC for performance, PWA support |
| Backend API | FastAPI (Python) | Native AI/ML ecosystem, async, Pydantic validation |
| Primary DB | PostgreSQL | Relational integrity, JSONB for flexible content, row-level security |
| Cache/Queue | Redis | Session cache, task queues for agents, pub/sub for real-time |
| Vector DB | Chroma (dev) / Weaviate (prod) | RAG for chatbot over module content |
| LLM (agents) | Claude API (primary) + Ollama (fallback) | Quality + cost control |
| Agent orchestration | LangGraph | Stateful agent workflows, checkpointing, HITL |
| Auth | NextAuth.js + JWT | OAuth, SSO/SAML, session management |
| File storage | S3-compatible | Media, code files, exports |
| Email | Resend / SendGrid | Transactional + digest emails |
| Push notifications | Web Push API | Browser push, no native app needed initially |
| Deployment | Docker Compose (dev) / Kubernetes (prod) | Scalable, reproducible |
| Monitoring | OpenTelemetry + Grafana + Prometheus | Full observability stack |
| CI/CD | GitHub Actions | Automated testing, containerization, deployment |

### 15.4 Security Architecture
- All API endpoints require JWT authentication
- Row-level security in PostgreSQL for tenant data isolation
- Agent outputs never bypass curator review before publish
- Agents cannot delete content — only create/update drafts
- Agent LLM costs capped per day; fallback to smaller models if budget exceeded
- No PII in agent logs
- All secrets in vault (HashiCorp Vault or cloud secret manager)
- OWASP Top 10 compliance
- GDPR: right to erasure, data export, consent management

---

## 16. CONTENT VERSIONING & DYNAMIC COMPLETION

### 16.1 Version Rules
- Every Topic, Section, Module has version integer and updated_at timestamp
- When Topic updated: topic.version++, section.version++, module.version++
- When new Topic added to Section: same cascade
- Learner Progress stores completed_at_module_version
- On module page load: if module.version > progress.completed_at_module_version -> show Updated banner
- If learner had status Complete and module version changed: status -> Needs Review
- Learner must re-visit and re-check new topics to restore Complete status
- Quiz NOT re-required unless admin explicitly marks quiz-required-on-update

### 16.2 Content Diff View
- Learner clicks "What changed?" to see diff since their last completion
- New topics: green highlight
- Updated topics: yellow highlight
- Removed topics: red strikethrough
- Diff shows date of change and whether change was by human or AI agent

### 16.3 Admin Version Control
- Full version history per module: who changed what, when (human or which agent)
- Rollback to any previous version
- Preview before publish
- Scheduled publish: set future date/time for content to go live
- Bulk version bump: admin can force all learners to re-review a module

---

## 17. PERSONALIZATION & ADAPTIVE LEARNING

- FR-PERS-01: On first login — 5-question diagnostic quiz to assess current level -> auto-sets starting phase
- FR-PERS-02: Learning path recommendation based on level, completed modules, and stated goal (job role)
- FR-PERS-03: "Skip ahead" option — learner takes competency quiz to skip a module they already know
- FR-PERS-04: Adaptive quiz difficulty — questions get harder as learner improves
- FR-PERS-05: Spaced repetition reminders — modules completed 30+ days ago with no revisit get "Review?" nudge
- FR-PERS-06: Goal setting — learner sets goal (e.g. "Get AWS AI Practitioner cert by June") -> platform generates daily study plan
- FR-PERS-07: Time preference — learner sets available hours/week -> platform estimates completion date
- FR-PERS-08: Recommendation Agent (AGT-10) updates recommendations after every module completion
- FR-PERS-09: "Learners like you also completed..." — collaborative filtering recommendations

---

## 18. CERTIFICATIONS CATALOG

> 42+ certifications and learning paths mapped to platform phases.

- **Google Cloud** — Generative AI Leader (+ PMLE depth) | Exam/Credential | Paid
  - Study phases: P2, P3, P6, P7, P14
  - Note: Separate exams; PMLE → cloud.google.com/learn/certification/machine-learning-engineer
  - URL: https://cloud.google.com/learn/certification/generative-ai-leader
- **Google Cloud** — Introduction to Generative AI (Skills Boost) | Learning Path | Free
  - Study phases: P1, P2
  - Note: Micro-course + optional skill badge
  - URL: https://www.cloudskillsboost.google/course_templates/536
- **Google Cloud** — Generative AI Leader — prep path (Skills Boost) | Learning Path | Free
  - Study phases: P2, P3, P14
  - Note: Aligns with GAL exam domains
  - URL: https://www.cloudskillsboost.google/paths/1951
- **Google Cloud** — Advanced: Generative AI for Developers (Skills Boost) | Learning Path | Free
  - Study phases: P3, P6, P7
  - Note: Technical path; labs may need GCP credits
  - URL: https://www.cloudskillsboost.google/paths/183
- **AWS** — Certified AI Practitioner (AIF-C01) | Exam/Credential | Paid
  - Study phases: P3, P4, P7, P14, P16
  - Note: Official proctored exam
  - URL: https://aws.amazon.com/certification/certified-ai-practitioner/
- **AWS** — Learn About Generative AI (training hub) | Learning Path | Free
  - Study phases: P1, P3, P4
  - Note: Curated digital courses & learning plans
  - URL: https://aws.amazon.com/training/learn-about/generative-ai/
- **AWS** — Generative AI Learning Plan for Developers (Skill Builder) | Learning Path | Free
  - Study phases: P3, P6, P7
  - Note: Includes labs; free digital training
  - URL: https://skillbuilder.aws/learning-plan/5C9XQBTXBB/generative-ai-learning-plan-for-developers-includes-labs/EGATKJP13J
- **AWS** — AWS AI Practitioner Learning Plan (Skill Builder) | Learning Path | Free
  - Study phases: P3, P4, P16
  - Note: Prepares concepts used on AIF-C01
  - URL: https://skillbuilder.aws/learning-plan/G8ENMJ5QBE/aws-artificial-intelligence-practitioner-learning-plan/SU2A1EJM1A
- **AWS** — Building Gen AI Apps with Amazon Bedrock (course) | Learning Path | Free
  - Study phases: P3, P6, P7
  - Note: Bedrock APIs & patterns
  - URL: https://skillbuilder.aws/learn/TM4ZAXTGEZ/building-generative-ai-applications-using-amazon-bedrock/WM6Z6ZHU7K
- **Microsoft** — Azure AI Engineer (AI-102) | Exam/Credential | Paid
  - Study phases: P3, P4, P6, P7, P14
  - Note: Proctored certification exam
  - URL: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/
- **Microsoft** — Azure AI Fundamentals (AI-900) | Exam/Credential | Mixed
  - Study phases: P1, P3
  - Note: Free Microsoft Learn prep; exam fee paid
  - URL: https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/
- **Microsoft** — Get started with Azure AI Fundamentals (Learn path) | Learning Path | Free
  - Study phases: P1, P3
  - Note: Maps to AI-900 topics
  - URL: https://learn.microsoft.com/en-us/training/paths/get-started-azure-ai-fundamentals/
- **Microsoft** — Browse AI & ML learning paths (Microsoft Learn) | Learning Path | Free
  - Study phases: P1–P16
  - Note: Filter Azure + AI paths
  - URL: https://learn.microsoft.com/en-us/training/browse/?resource_type=learning%20path&products=azure&subjects=artificial-intelligence
- **NVIDIA** — Generative AI LLM (NCA-GENL / NCP-GENL) | Exam/Credential | Paid
  - Study phases: P0, P1, P4, P6, P7
  - Note: Professional track → nvidia.com/.../generative-ai-llm-professional/
  - URL: https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/
- **NVIDIA** — NVIDIA Training & DLI course catalog | Learning Path | Free
  - Study phases: P0, P1, P11
  - Note: Mix of free & paid workshops
  - URL: https://www.nvidia.com/en-us/training/
- **IBM** — Generative AI Engineering (Coursera Professional Certificate) | Exam/Credential | Paid
  - Study phases: P2, P4, P6, P16
  - Note: Subscription / Coursera fee
  - URL: https://www.coursera.org/professional-certificates/ibm-generative-ai-engineering
- **IBM** — SkillsBuild — free learning (search AI courses) | Learning Path | Free
  - Study phases: P1, P2
  - Note: Use catalog search for artificial intelligence topics
  - URL: https://skillsbuild.org/learners
- **Hugging Face** — Learn hub — LLM, Agents, audio, CV | Learning Path | Free
  - Study phases: P1, P4, P6, P7, P11
  - Note: Courses & certificates of completion
  - URL: https://huggingface.co/learn
- **Hugging Face** — LLM Course (chapter 1) | Learning Path | Free
  - Study phases: P1, P4, P7
  - Note: Open models & transformers
  - URL: https://huggingface.co/learn/llm-course/chapter1/1
- **Hugging Face** — Agents Course (introduction) | Learning Path | Free
  - Study phases: P4, P6
  - Note: Tool use & agent loops
  - URL: https://huggingface.co/learn/agents-course/unit0/introduction
- **Databricks** — Generative AI Fundamentals (accreditation) | Learning Path | Free
  - Study phases: P1, P7
  - Note: Short videos + knowledge test + digital badge
  - URL: https://www.databricks.com/resources/learn/training/generative-ai-fundamentals
- **Kaggle** — 5-Day Intensive Generative AI (guide) | Learning Path | Free
  - Study phases: P1, P2, P7
  - Note: Partner content; self-paced
  - URL: https://www.kaggle.com/learn-guide/5-day-genai
- **Kaggle** — 5-Day AI Agents Intensive (guide) | Learning Path | Free
  - Study phases: P4, P6
  - Note: Agent patterns & deployment topics
  - URL: https://www.kaggle.com/learn-guide/5-day-agents
- **Kaggle** — Intro to AI Ethics (course) | Learning Path | Free
  - Study phases: P2, P16
  - Note: Responsible-AI foundations
  - URL: https://www.kaggle.com/learn/intro-to-ai-ethics
- **DeepLearning.AI** — Short courses (LLM apps, agents, RAG, etc.) | Learning Path | Mixed
  - Study phases: P2, P4, P6, P7
  - Note: Often free to audit; certificate paid
  - URL: https://www.deeplearning.ai/courses/
- **Anthropic** — Educational course materials (GitHub) | Learning Path | Free
  - Study phases: P2, P3, P4
  - Note: Prompting & Claude-related exercises; no vendor exam
  - URL: https://github.com/anthropics/courses
- **Anthropic** — Claude API — documentation | Learning Path | Free
  - Study phases: P3, P4, P16
  - Note: Official API & safety docs
  - URL: https://docs.anthropic.com/
- **OpenAI** — OpenAI Cookbook (patterns & examples) | Learning Path | Free
  - Study phases: P3, P6, P7
  - Note: No OpenAI exam; dev-focused
  - URL: https://cookbook.openai.com/
- **OpenAI** — OpenAI Platform documentation | Learning Path | Free
  - Study phases: P3, P4
  - Note: API reference & guides
  - URL: https://platform.openai.com/docs
- **Meta** — Blueprint — training catalog | Learning Path | Free
  - Study phases: P14
  - Note: Ads & marketing AI topics; not an LLM-dev cert
  - URL: https://www.facebookblueprint.com/student/catalog
- **Oracle** — Oracle certification program (AI & data exams) | Exam/Credential | Paid
  - Study phases: P7, P14
  - Note: Check catalog for current AI / OCI exams
  - URL: https://education.oracle.com/oracle-certification-program
- **SAP** — SAP Learning Hub — search AI topics | Learning Path | Mixed
  - Study phases: P14, P17
  - Note: Enterprise AI courses; subscription varies
  - URL: https://learning.sap.com/
- **Snowflake** — Snowflake Learning — AI & ML catalog | Learning Path | Mixed
  - Study phases: P7, P14
  - Note: Free & paid modules; filter for AI/ML
  - URL: https://learn.snowflake.com/
- **MongoDB** — MongoDB University — AI & vector search topics | Learning Path | Free
  - Study phases: P7
  - Note: RAG-friendly data patterns
  - URL: https://learn.mongodb.com/catalog
- **fast.ai** — Practical Deep Learning for Coders | Learning Path | Free
  - Study phases: P1, P11
  - Note: Practical ML; complements LLM modules
  - URL: https://course.fast.ai/

---

## 19. CAPSTONE PROJECTS (Full Specifications)

### Capstone 1 — AI That Calls You
**Difficulty:** Advanced | **Time:** 1-2 weeks
**Stack:** LangGraph + Twilio Voice + FastAPI + Ollama + Redis + WebSocket + Ngrok

**What it demonstrates:**
- LangGraph StateGraph with human-in-the-loop node
- Twilio Voice API for outbound calls with TTS
- Redis checkpointer for state persistence across async resumption
- FastAPI webhook endpoints for Twilio callbacks
- Keypad response capture (1=approve, 2=reject)
- Full audit trail logging for compliance

**Architecture:**
1. Task Trigger — API or webhook event starts agent
2. Autonomous Execution — tools + memory, confidence scored each step
3. Decision Gate — below-threshold confidence opens voice flow
4. Phone Call — Twilio TTS reads situation, waits for keypad input
5. Resume — agent continues based on human decision
6. Audit — structured logs for compliance-style reviews

**Deliverables:**
- GitHub repo with README and architecture diagram
- Deployed FastAPI backend (Railway or Fly.io)
- 2-minute demo recording
- LinkedIn post template

**Modules required:** M125, M46, M100, M76, M77, M81

---

### Capstone 2 — AI Payment Risk Analyst
**Difficulty:** Advanced | **Time:** 2-3 weeks
**Stack:** FastAPI + Vector DB + RAG + Streamlit + Claude or GPT-4

**What it demonstrates:**
- RAG pipeline over compliance documents (RBI, PCI-DSS, internal rules)
- Structured risk scoring (0-100) with explainable citations
- Dual-layer fraud detection: rule-based + LLM-based
- Streamlit dashboard for risk officers
- Batch processing of historical transactions

**Architecture:**
1. Ingest — chunk and embed policy docs (synthetic data only)
2. Retrieve — hybrid search for rules relevant to each transaction
3. Reason — LLM outputs risk score, summary, cited rule IDs
4. Review UI — Streamlit dashboard for officers to browse flagged items

**Deliverables:**
- GitHub repo with full code
- Sample synthetic dataset + populated vector DB
- Streamlit demo deployed publicly
- Architecture document (1-pager)

**Modules required:** M126, M55, M59, M60, M100, M101

---

### Capstone 3 — Local Perplexity Clone
**Difficulty:** Intermediate | **Time:** 3-7 days
**Stack:** Ollama + SearXNG + Docker + Streamlit + LangChain

**What it demonstrates:**
- Self-hosted meta-search (SearXNG via Docker)
- Local LLM answer synthesis with source citations
- Zero external API cost — fully local stack
- Privacy-preserving research tooling

**Architecture:**
1. Search — SearXNG returns ranked URLs and snippets
2. Fetch — optional light fetch for top hits (respect robots.txt)
3. Synthesize — local model cites sources in response
4. Chat UI — Streamlit with history and model picker

**Deliverables:**
- Docker Compose file (one command to run everything)
- GitHub repo with full code and setup guide
- 5-minute demo video

**Modules required:** M127, M1, M3, M95, M101, M103

---

### Capstone 4 — AI Financial Risk Monitor
**Difficulty:** Advanced | **Time:** 2-3 weeks
**Stack:** LangGraph + n8n + Claude API + Pinecone + FastAPI + Twilio SMS + Redis Streams

**What it demonstrates:**
- Real-time transaction monitoring via Redis Streams
- Pinecone similarity search against known fraud patterns
- LLM-based explainable risk reasoning
- Multi-channel escalation (SMS/Slack/log)
- AML/fraud detection for fintech consulting

**Architecture:**
1. Data Ingestion — Redis Streams for real-time transaction feed
2. Risk Scoring — Pinecone similarity search against fraud patterns
3. LLM Analysis — Claude/GPT-4 for explainable risk reasoning
4. Escalation — SMS/Slack/log based on risk threshold

**Modules required:** M46, M59, M95, M100, M76

---

## 20. HACKATHONS CATALOG

> 7 hackathons with prep paths, templates, and winner patterns.


**Anthropic AI Safety Hackathon** | Org: Anthropic | Prize: ~$50K (varies by event)
- Theme: Safety, interpretability, alignment
- Description: Build systems with safety or interpretability focus; mentor access from lab engineers.
- Deadline: Check official site for next dates
- Prep: Complete P2 Prompting + P16 Security modules first
- Quick-start: Guardrailed agent + eval harness + short policy doc
- Winners: Winning teams often combine strong eval metrics with crisp demos (Streamlit/FastAPI).

**Hugging Face Open-Source Sprint** | Org: HuggingFace | Prize: Hub credits + visibility
- Theme: Models, datasets, Spaces
- Description: 48-hour style sprints for Hub-ready artifacts.
- Deadline: Quarterly sprints
- Prep: P1 foundations + P6 frameworks + P7 RAG
- Quick-start: Gradio Space + dataset card + small model or adapter
- Winners: Top entries ship clean cards, reproducible training, and eval tables.

**Devpost AI Hackathons** | Org: Devpost | Prize: $10K–$100K depending on sponsor
- Theme: Sponsor-specific (Gemini, AWS, Azure, …)
- Description: Filter by AI; many enterprise-sponsored challenges.
- Deadline: Rolling calendar
- Prep: P3 LLM APIs + P14 deployment
- Quick-start: MVP API + minimal UI + 90-second demo video
- Winners: Clear problem statement + live demo + public repo fork win most tracks.

**LangGraph Build Challenge** | Org: LangChain | Prize: Credits + ecosystem visibility
- Theme: Production agents
- Description: Focus on durable, deployable LangGraph apps.
- Deadline: Periodic announcements
- Prep: P4 Agents + P6 LangGraph depth
- Quick-start: StateGraph + tool routing + LangSmith traces
- Winners: Projects with traces, tests, and Dockerfile score highest.

**Google AI Hackathon (Gemini)** | Org: Google | Prize: Large pooled prizes (see site)
- Theme: Gemini API apps
- Description: Build on Gemini with mentor office hours.
- Deadline: Annual / regional
- Prep: P3 multimodal + P14 FastAPI/Streamlit
- Quick-start: Gemini tool use + OAuth + hosted demo
- Winners: Creative multimodal UX with latency under control.

**CrewAI Multi-Agent Challenge** | Org: CrewAI | Prize: Cash + enterprise intros
- Theme: Multi-agent crews
- Description: Enterprise-flavored multi-agent builds.
- Deadline: Periodic
- Prep: P4 collaboration + P6 CrewAI module
- Quick-start: Defined roles + sequential process + task outputs
- Winners: Clear agent boundaries and measurable task success.

**n8n Automation Hackathon** | Org: n8n | Prize: ~$5K (see rules)
- Theme: Workflow + AI nodes
- Description: AI-powered automations in n8n.
- Deadline: Quarterly
- Prep: P13 automation modules
- Quick-start: Webhook → LLM → CRM/Slack with error branch
- Winners: Reusable templates published to marketplace trend well.

---

## 21. OPEN SOURCE CONTRIBUTION TARGETS

- **Hugging Face smol-course** (HuggingFace) — Beginner → Intermediate
  - Small-model training curriculum; contribute notebooks and examples.
  - https://github.com/huggingface/smol-course
- **LangGraph** (LangChain) — Intermediate
  - Stateful agents; fix docs, add tools, improve examples.
  - https://github.com/langchain-ai/langgraph
- **Ollama** (Ollama) — Beginner-friendly
  - Local model runner; Modelfiles and docs welcome.
  - https://github.com/ollama/ollama
- **MCP Servers** (Model Context Protocol) — Intermediate → Advanced
  - Reference servers and patterns for tool exposure.
  - https://github.com/modelcontextprotocol/servers
- **Dify** (Community) — Intermediate
  - Open LLMOps UI; plugins and integrations.
  - https://github.com/langgenius/dify

---

## 22. YC-STYLE STARTUP IDEAS

> 9 startup-grade AI project ideas with problem, solution, stack, market, and 2-week MVP scope.


**AI policy copilot for regulated orgs**
- Problem: Teams drown in internal policy updates.
- Solution: RAG over policy corpuses with citation-only answers.
- Stack: P7 RAG, P8 MCP, P14 FastAPI
- Market: Large governance / compliance software TAM (indicative billions class).
- 2-week MVP: Upload PDFs → query API → Slack bot in 2 weeks.

**Meeting → action-item router**
- Problem: Action items die in notes after calls.
- Solution: Transcript → structured tasks → Jira/Asana via agents.
- Stack: P4 Agents, P5 tools, P13 n8n
- Market: Productivity / collaboration segment.
- 2-week MVP: Webhook + single integration + reviewer UI.

**Sales email personalizer (bounded)**
- Problem: Generic outreach converts poorly.
- Solution: Template-safe LLM that only fills approved slots from CRM fields.
- Stack: P2 prompting, P16 safety, P3 APIs
- Market: GTM tooling; crowded but always in demand.
- 2-week MVP: CSV in → CSV out with moderation filter.

**Onboarding assistant for internal wikis**
- Problem: New hires cannot find canonical docs.
- Solution: Agent answers from verified sources with links.
- Stack: P7 RAG, P10 unified stack, P14 hosting
- Market: Enterprise internal tools.
- 2-week MVP: Single Confluence space + chat UI.

**Agent observability starter pack**
- Problem: No tracing for ad-hoc LLM scripts.
- Solution: Drop-in OpenTelemetry + LangSmith-style dashboard template.
- Stack: P15 monitoring, P10 observability layer
- Market: Developer tooling for AI teams.
- 2-week MVP: One FastAPI service with exemplar traces.

---

## 23. NON-FUNCTIONAL REQUIREMENTS

| Requirement | Target |
|-------------|--------|
| Module page load | < 2 seconds |
| Chatbot first response | < 3 seconds |
| Agent feedback response | < 24 hours |
| Capstone review | < 48 hours |
| Availability | 99.9% uptime SLA |
| Concurrent users | 10,000 without degradation |
| Security | OWASP Top 10 compliance |
| Data privacy | GDPR compliant, right to erasure, data export |
| Multi-tenancy | Complete data isolation at DB level (row-level security) |
| Agent safety | All agent content through curator review before publish |
| Agent cost | Daily token budget cap per agent; fallback to smaller models |
| Accessibility | WCAG 2.1 AA target (manual testing required) |
| Mobile | Fully responsive, PWA-enabled |
| Offline | Module content cached for offline reading (PWA) |

---

## 24. SUCCESS METRICS

| Metric | 6-month Target | 12-month Target |
|--------|---------------|----------------|
| Registered users | 5,000 | 25,000 |
| Active learners (MAU) | 2,000 | 10,000 |
| Modules completed/day | 500 | 3,000 |
| Average session duration | 25 min | 30 min |
| 7-day retention | 40% | 55% |
| 30-day retention | 25% | 40% |
| Tenant accounts | 10 | 50 |
| Learners in enterprise tenants | 500 | 5,000 |
| Content items added by agents/week | 20 | 50 |
| Feedback response rate (agent, within 24h) | 90% | 95% |
| Content acceptance rate (curator approves agent draft) | 70% | 80% |
| NPS score | 45 | 60 |

---

## 25. OPEN QUESTIONS & DECISIONS

| # | Question | Decision |
|---|----------|---------|
| Q1 | Module completion definition | Checking all topics in Learn + Practice tabs. Quiz NOT required. |
| Q2 | Agent content publishing | All agent-written content goes through human curator before publish. Agents cannot publish directly. |
| Q3 | Pricing model | TBD — not yet decided. Options: freemium, subscription, per-seat enterprise. |
| Q4 | AI transparency | YES — every AI agent interaction clearly labeled. Learners always know they are talking to an AI. |
| Q5 | Feedback visibility | Private to submitter and admins by default. Option to make public per feedback item. |
| Q6 | Suggestion board | Public with submitter names shown (can be anonymous if user opts in). |
| Q7 | Quiz retake policy | Unlimited retakes. No cooldown. Quiz is for learning, not gatekeeping. |
| Q8 | Capstone review | AI-only review (AGT-09) for standard tier. Human review option for enterprise tenants. |
| Q9 | Offline access | Module content cached via PWA for offline reading. Progress sync on reconnect. |
| Q10 | News feed submissions | Agent-curated only. Learners can suggest sources via Improvement Suggestion system. |
| Q11 | Tenant data export | Yes — GDPR portability. CSV and JSON formats. |
| Q12 | Content moderation | Agent draft -> Curator review -> Publish. No direct agent publish. |

---

## 26. FUTURE ROADMAP

### Phase 2 (3-6 months post-launch)
- Live cohort sessions — scheduled live sessions for tenant cohorts (Zoom/Meet integration)
- Peer learning — discussion threads per module, peer Q&A
- Code playground — in-browser code execution (E2B sandbox) for Code tab
- AI pair programmer — Claude Code integration in the Code tab for guided coding
- Mobile app — React Native app for iOS/Android

### Phase 3 (6-12 months)
- Mentor marketplace — connect learners with AI practitioners for 1:1 sessions
- Job board — AI job listings matched to learner's level and completed modules
- Company hiring — companies post roles, filter candidates by AgentIQ level + badges
- Cohort projects — multi-learner collaborative capstone projects
- Tenant API — embed AgentIQ content in existing LMS

### Phase 4 (12+ months)
- AgentIQ Certified — industry-recognized certification issued by AgentIQ itself
- Content marketplace — external experts submit modules; revenue share model
- Agent builder sandbox — in-platform environment to build and test AI agents
- Research track — advanced track for practitioners contributing to AI research
- Multilingual — AI-translated content in 10+ languages (AGT-15: Translation Agent)

---

*End of PRD v2.0*
*Sources: AI Master Tracker Blueprint (docx) | extracted_image_topics.md | master_topic_list.md | ai-consultant-roadmap.html*
*Total curriculum: 20 phases, 133+ modules, 42+ certifications, 4 capstones, 7 hackathons, 9 YC ideas, 8 OSS targets*

# Product Requirements Document
# AgentIQ — The Living AI Learning Platform

**Version:** 2.0 — Complete  
**Date:** March 2026  
**Author:** Manish Taneja  
**Status:** Final Draft  
**Sources:** AI Master Tracker Blueprint (docx) · extracted_image_topics.md · master_topic_list.md · ai-consultant-roadmap.html  

---

---

---
