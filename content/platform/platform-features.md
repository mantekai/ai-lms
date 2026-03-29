<!-- Extracted from content/spec/agentiq_platform_spec.md — run: python3 scripts/extract_platform_docs.py — Manish.AI -->

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
