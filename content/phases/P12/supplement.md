---
kind: phase_supplement
phase_code: P12
---

# Phase P12 — supplemental depth

### AI-native development workflows

### Philosophy & Spectrum

**Traditional Coding vs Vibe Coding vs No-Code Spectrum:**
- Traditional Coding: Full manual control, custom architectures, deep technical skill required, unlimited flexibility. Languages: Python, JavaScript, TypeScript, Java, Go, C#. Frameworks: React, Next.js, FastAPI, Flask. Best for: custom AI agents, backend services, complex integrations, high-performance systems.
- Vibe Coding (AI-Assisted): AI writes most of the code, human reviews and edits, very fast prototyping, blends coding and prompting. Tools: Claude Code, Cursor AI, GitHub Copilot, Replit AI, Tabnine, Codeium. Best for: AI agent development, API automation, MVPs, data pipelines, integration scripts.
- No-Code: Zero coding required, drag-and-drop building, AI handles logic, fastest development speed. Tools: Zapier, Make.com, n8n, Power Automate, ServiceNow Flow Designer, Webflow, Bubble. Best for: business automation, AI workflows, CRM/ERP integrations, internal tools.

**AI-Assisted Development:** The practice of using AI tools to accelerate software development. The developer provides high-level intent and reviews AI-generated code rather than writing every line manually. Key skills: writing clear intent descriptions, reviewing diffs critically, catching security issues in generated code, writing tests for AI-generated functions. The developer remains responsible for correctness, security, and maintainability.

### Claude Code

**Memory File Hierarchy:** Four levels of CLAUDE.md files with increasing scope:
1. `~/.claude/CLAUDE.md` — Global: applies to all projects on this machine. Personal preferences, global tools, coding standards.
2. `~/CLAUDE.md` — Parent: applies to all projects in the home directory. Monorepo-level context.
3. `./CLAUDE.md` — Project: shared via git, applies to all team members. Tech stack, architecture, build commands, gotchas.
4. `./subfolder/CLAUDE.md` — Scoped: applies only within that subdirectory. Component-specific context.
Rules: keep each file under 200 lines, subfolder files append (not override) parent context, commit project-level files to git for team sharing.

**Claude Code Project Structure:** Recommended directory layout for agentic projects:
```
project/
├── CLAUDE.md                    # Project memory
├── .claude/
│   ├── settings.json            # CLI & model preferences
│   ├── hooks/                   # Automation guardrails (PreToolUse, PostToolUse)
│   ├── skills/                  # Reusable AI workflows (code-review, testing)
│   ├── commands/                # Reusable prompt templates
│   └── agents/                  # Specialized sub-agent definitions
├── config/
│   ├── agent_config.yaml        # LLM parameters (temperature, model, max_tokens)
│   └── env_config.yaml          # API keys and environment variables
├── src/
│   ├── agents/                  # Claude-powered agent implementations
│   ├── core/                    # memory.py, reasoning.py, planner.py
│   └── utils/prompts/           # Externalized prompt templates
├── tests/                       # Evaluation and unit tests
└── requirements.txt
```

**Context Engineering:** The practice of designing what goes into the model's context window to maximize accuracy and minimize cost. Key principle: smaller, more focused context = higher accuracy. Techniques: load only relevant skills (not all skills), use subagents with isolated context for independent subtasks, compress conversation history with /compact, reference files with @filename instead of pasting content.

**Reusability Engine:** The progression from one-off prompts to reusable systems: Prompt (one-time instruction) → Command (saved reusable prompt in .claude/commands/) → Skill (markdown guide with metadata that auto-activates) → Workflow (orchestrated sequence of commands and skills). Stop rewriting the same prompts — build once, reuse everywhere.

**MCP Integration in Claude Code:** Claude Code connects to MCP servers via `.claude/settings.json`. The integration allows Claude to call external tools (databases, APIs, file systems) directly during coding sessions. Example: Claude queries a PostgreSQL database to understand the schema before writing a migration, or reads from S3 to understand the data format before writing a parser.

**Iteration System:** Claude Code's development cycle: Build (implement feature) → Review (Claude reviews its own output) → Checkpoint (save state with git commit) → Rewind (Esc Esc to undo if needed) → Build again. The checkpoint/rewind system enables safe experimentation — try an approach, evaluate, rewind if it doesn't work, try another approach.

**Skill Auto-Activation Patterns:** Claude Code skills auto-activate when the user's natural language request matches the skill's description field. The description field is the most critical part of a skill file — it must precisely describe when the skill should be used. Example: description "Use when reviewing Python code for security vulnerabilities" will activate when the user says "check this code for security issues."

**Context Injection Techniques:** Methods for injecting context into Claude Code sessions: Template variables (fill placeholders in command files at runtime), Hook-based injection (PreToolUse hooks add context before tool calls), Skill-level loading (skills inject their own context when activated), Command references (@filename to include file content). Each technique has different performance and maintainability trade-offs.

**Permissions & Safety:** Claude Code's permission system in settings.json controls what the agent can and cannot do. Allow list: `"Read:*"` (read any file), `"Bash:git:*"` (run any git command), `"Write:*:*.md"` (write only markdown files). Deny list: `"Read:env:*"` (never read .env files), `"Bash:sudo:*"` (never run sudo commands). Exit codes: 0 = allow the tool call, 2 = block the tool call (used in PreToolUse hooks).

### Other AI Dev Tools

**Cowork Mode & Desktop Plugins:** Claude's desktop application feature that provides a Linux VM environment with file access and pre-loaded skills. Document Skills: create Word documents, PowerPoint presentations, Excel spreadsheets, and PDFs via natural language. Plugin Ecosystem: bundles of MCPs + skills + commands packaged as installable plugins. Email Copilot Plugin: Gmail + Google Calendar integration for email triage, drafting, and scheduling.

**Claude.ai Projects:** A persistent memory and shared context feature in Claude.ai (Pro/Team/Enterprise plans). Projects store: role and persona, user preferences, domain knowledge, output format preferences, example outputs. Context persists across all conversations within the project. Useful for ongoing work where you want Claude to remember your preferences and project context without re-explaining every session.

**Chrome Automation:** Claude's Chrome extension enables browser automation directly from the Claude interface. Capabilities: navigate to URLs, read page content, fill form fields, click elements, extract structured data, take screenshots. Use cases: web research, form automation, data extraction, multi-step web workflows. Respects robots.txt and requires explicit user permission for sensitive actions.

**Scheduled Tasks:** Cron-based AI workflows that run automatically on a schedule. Configuration: natural language schedule ("every weekday at 8am") or cron syntax. The scheduled task runs with full MCP access — it can read emails, check calendars, query databases, and send notifications. Use cases: daily standup generation, weekly digest emails, automated monitoring and alerting.

**Plugin Development:** Building custom Claude plugins by packaging MCPs + skills + commands into a distributable bundle. Plugin structure: `plugin.json` manifest (name, version, description, permissions), `skills/` directory (SKILL.md files), `commands/` directory (command markdown files), MCP server configuration. Published plugins can be shared with teams or the broader community.

### Curriculum visual map — block H

### Image 13: Claude Code Cheatsheet — Rules, Best Practices, Skills, Hooks

**Memory File Rules:** Keep each CLAUDE.md file under 200 lines. Subfolder files append context (never override parent). Never overwrite parent context.

**CLAUDE.md Best Practices:**
1. Run `/init` first then refine output
2. Be specific in instructions
3. Add gotchas Claude cannot infer
4. Reference docs with @filename
5. Add workflow rules
6. Keep memory concise
7. Commit to Git for team sharing

**Project File Structure:**
```
your_project/
├── CLAUDE.md
├── .claude/
│   ├── settings.json
│   ├── settings.local.json
│   ├── skills/code-review/SKILL.md
│   ├── skills/testing/SKILL.md
│   ├── helpers.py
│   ├── commands/deploy.md
│   └── agents/security-reviewer.md
```

**Adding Skills:** Skills = markdown guides Claude auto-invokes via natural language. Project skill: `.claude/skills/<name>/SKILL.md`. Personal skill: `~/.claude/skills/<name>/SKILL.md`. Skill file format: YAML frontmatter with name, description, allowed tools. Description field is critical for auto-activation. Example: `description: Jest testing patterns` triggers when user asks about testing.

**4-Layer Architecture:**
- L1 — CLAUDE.md: Persistent context and rules
- L2 — Skills: Auto-invoked knowledge packs
- L3 — Hooks: Safety gates and automation
- L4 — Agents: Subagents with their own context

**Daily Workflow Pattern:** `cd project && claude` → Shift + Tab + Tab → Plan Mode → Describe feature intent → Shift + Tab → Auto Accept → `/compact` → Esc Esc → rewind → Commit frequently → Start new session per feature.

**Quick Reference:**
- `/init` — Generate CLAUDE.md
- `/doccat` — Check installation
- `/compact` — Compress context
- `Shift + Tab` — Change modes
- `Tab` — Toggle extended thinking
- `Esc Esc` — Rewind menu

### Image 14: Claude Code Project Structure

**Full Directory Layout:**
```
claude_agentic_project/
├── CLAUDE.md                    # Global project memory & CLI instructions
├── README.md
├── .claude/settings.json        # CLI & Model preferences
├── .claude/hooks/               # Automation guardrails
├── .claude/skills/              # Reusable AI workflows
├── config/agent_config.yaml     # LLM parameters (temperature, model)
├── config/env_config.yaml       # API keys and environment variables
├── src/agents/base_agent.py
├── src/agents/skill_agent.py    # Bridges .claude/skills to Python
├── src/core/memory.py           # State management
├── src/core/reasoning.py        # Prompt chain logic
├── src/core/planner.py          # Task decomposition
├── src/utils/prompts/           # Externalized prompt templates
├── docs/architecture.md
├── docs/decisions/              # ADRs (Architecture Decision Records)
├── tests/
└── requirements.txt
```

**Key Architectural Concepts:** CLAUDE.md at root = global project memory & CLI instructions. .claude/ directory = Claude-specific automation (settings, hooks, skills). config/ = separated LLM parameters and environment variables. src/agents/ = Claude-powered agent implementations with skill bridging. src/core/ = the "brain" — memory (state), reasoning (prompt chains), planner (task decomposition). src/utils/prompts/ = externalized prompt templates (not hardcoded). docs/decisions/ = Architecture Decision Records (ADRs) for traceability.

### Image 15: 15 Free Courses to Master Claude, MCP, and AI Agents

**Free Anthropic Learning Roadmap:**

Section 1 — Foundation:
1. Claude 101 — anthropic.skilljar.com/claude-101
2. AI Fluency: Framework & Foundations — anthropic.skilljar.com/ai-fluency-framework-foundations
3. AI Fluency for Students — anthropic.skilljar.com/ai-fluency-for-students
4. AI Fluency for Educators — anthropic.skilljar.com/ai-fluency-for-educators
5. Teaching AI Fluency — anthropic.skilljar.com/teaching-ai-fluency

Section 2 — Developer Fundamentals:
6. Claude Code in Action — anthropic.skilljar.com/claude-code-in-action
7. Building with the Claude API — anthropic.skilljar.com/claude-with-the-anthropic-api
8. Prompt Engineering Tutorial — github.com/anthropics/prompt-eng-interactive-tutorial

Section 3 — Platform Integrations:
9. Claude with Amazon Bedrock — anthropic.skilljar.com/claude-in-amazon-bedrock
10. Claude with Google Cloud Vertex AI — anthropic.skilljar.com/claude-with-google-vertex

Section 4 — Advanced AI Engineering:
11. Introduction to Model Context Protocol — anthropic.skilljar.com/introduction-to-model-context-protocol
12. Model Context Protocol: Advanced Topics — anthropic.skilljar.com/model-context-protocol-advanced-topics
13. AI Fluency for Nonprofits — anthropic.skilljar.com/ai-fluency-for-nonprofits

### AI-native IDE and API mastery

Claude Expert Learning Platform (HTML) — 10-Module Claude Mastery Path

**Overview:** Single-page HTML learning app with 10 modules (L1–L10), approximately 60 lessons total. Focus: Complete Claude AI stack — from basics to autonomous agents.

**Module 0 (L1): Claude Basics & Mindset**
- Claude & Constitutional AI — how Anthropic built Claude using CAI and RLHF (helpful, harmless, honest)
- Claude vs GPT-4 vs Gemini — feature comparison: context window, coding, reasoning, agentic capabilities
- Claude.ai vs API vs Claude Code — three access methods and when to use each
- 12 Core Capabilities: Agentic Code Generation, Deep Context Reasoning, Smart Debugging & Fixes, Native Git Operations, Sub-Agent Parallelism, Auto Checkpoints & Recovery, 200K+ Context Window, MCP Tool Integrations, CI/CD Automation Hooks, Test Generation & Refactors, Task Planning & Execution, Run Anywhere (Local→Cloud)
- Free vs Pro vs API Tiers — pricing, rate limits, model access

**Module 1 (L2): Prompt Engineering Mastery**
- Prompt Anatomy — Role + Context + Task + Format (four pillars)
- System Prompts Deep Dive — persona, constraints, behavior, XML tags for structure
- Few-Shot Examples — 2-5 input→output pairs, reduces format errors by ~60%
- Chain of Thought (CoT) — step-by-step reasoning, `<thinking>` tags, extended thinking mode (budget_tokens)
- XML Tags for Structure — `<context>`, `<task>`, `<format>`, `<example>` — Claude's native structuring
- Prompt Chaining — output of prompt N becomes input of prompt N+1
- Temperature & Model Selection — Haiku (fast/cheap) → Sonnet (balanced) → Opus (most capable)
- Anthropic Prompt Engineering Tutorial — official 9-chapter interactive tutorial

**Module 2 (L3): Claude Code CLI Mastery**
- Installing Claude Code (Node.js 18+), `/init` to scan codebase
- Quick Reference Commands: `/init`, `/compact`, `/doccat`, `Shift+Tab`, `Tab`, `Esc Esc`
- 4-Layer Architecture: L1 CLAUDE.md (Persistent Memory), L2 Skills (Auto-Invoked Knowledge packs), L3 Hooks (Safety Gates: PreToolUse, PostToolUse, Notification, Stop), L4 Sub-Agents (Parallel Context, isolated context per subtask)
- Memory File Hierarchy: `~/.claude/CLAUDE.md` (Global) → `~/CLAUDE.md` (Parent) → `./CLAUDE.md` (Project) → `./frontend/CLAUDE.md` (Subfolder)
- Rules: keep each <200 lines, subfolder files append context
- Daily Workflow Pattern: `cd project && claude` → Plan Mode → Describe intent → Auto Accept → `/compact` → commit → new session per feature

**Module 3 (L4): Claude API & SDK**
- Authentication & First API Call — API key from console.anthropic.com, Python SDK
- Streaming Responses — `client.messages.stream()` for real-time token delivery
- Tool Use (Function Calling) — define tools with JSON Schema, Claude decides when to call
- Vision API — base64 images or URLs, JPEG/PNG/GIF/WebP, max 5MB, up to 20 images
- Batch API for Scale — 10,000 requests/batch, 50% cost reduction, 24-hour turnaround
- Rate Limits & Error Handling — 429/529 errors, exponential backoff with jitter, tier-based limits

**Module 4 (L5): Built-in Skills & Plugins**
- Cowork Mode — desktop Claude app with Linux VM, file access, pre-loaded skills
- Document Skills — create Word docs, PowerPoint decks, Excel sheets, PDFs via natural language
- Plugin Ecosystem — bundles of MCPs + skills + commands
- Email Copilot Plugin — Gmail + Google Calendar integration (triage, draft, schedule)
- Task Management & Memory — TASKS.md + CLAUDE.md for persistent work collaboration

**Module 5 (L6): Agents & Sub-Agents**
- The Agent Loop — perceive → think → act → observe → repeat until done
- Agentic Pipeline Architecture — User Intent → Planner → Sub-Agents → Tools → Codebase → Tests → Deploy
- Parallel Sub-Agent Patterns — spawn multiple agents for independent subtasks
- Task Dispatch & Orchestration — route tasks to specialized sub-agents (code-review, security, docs)
- HITL Design Patterns — AI works independently, humans intervene only at true decision points
- Callback Architecture — agent pauses → serializes state → notifies human (Slack/email/phone) → resumes with input

**Module 6 (L7): MCP & Third-Party Integrations**
- What is Model Context Protocol — open standard for connecting AI to external tools/data
- Configuring MCP Servers — `.claude/settings.json` (project) or `~/.claude/settings.json` (global)
- Slack MCP — read channels, send messages, search, schedule messages, create canvases
- Google Calendar MCP — list events, create/update/delete events, find free time
- Jira & Confluence MCP — create/search issues, create/search Confluence pages
- Amazon Bedrock — Claude on AWS with VPC isolation, IAM controls
- Google Cloud Vertex AI — Claude on GCP with BigQuery/GCS integration

**Module 7 (L8): Custom Plugins, Skills & Projects**
- Writing Your First SKILL.md — name + description (triggers auto-activation) + allowed tools + instructions
- Skill Auto-Activation Patterns — description field quality determines activation reliability
- Claude.ai Projects — persistent memory and shared context across conversations (Pro/Team/Enterprise)
- Creating Effective Projects — role, preferences, domain knowledge, output formats, examples
- Plugin Architecture — MCPs + skills/ + commands/ + plugin.json manifest
- Build a Custom Plugin — "Daily Digest" plugin (Slack + Gmail → morning briefing)
- Context Injection Techniques — template variables, hook-based injection, skill-level loading, command references

**Module 8 (L9): Chrome Automation & Scheduled Tasks**
- Chrome Extension — navigate URLs, read pages, fill forms, click elements, extract data, screenshots
- Web Automation Patterns — navigate+read, form automation, multi-step workflows, error handling
- Scheduled Tasks — recurring AI workflows (cron syntax or natural language), runs with full MCP access
- Creating a Scheduled Task — daily email digest at 8am, daily standup generator
- Dispatch for Agent Coordination — task routing to specialized agents (code-review, docs, data)
- Monitor & Alert Pattern — scheduled check → Claude reasoning → anomaly detection → alert via MCP

**Module 9 (L10): Safety, Governance & Capstone**
- Constitutional AI Deep Dive — CAI principles, self-critique, RLHF with AI feedback
- Responsible Use in Production — no PII in logs, output filtering, human review, prompt injection monitoring, audit logs
- Usage Policies & Legal — prohibited uses, allowed-with-care categories
- Enterprise Governance — SSO/SAML, admin console, per-user rate limits, audit logs, data not used for training
- 15 Free Anthropic Courses — full Skilljar + Coursera roadmap
- Capstone: "AI Calls You While Driving" — Claude agent loop + state persistence + Twilio Voice API + Ngrok webhook + resume endpoint

### Module 2 (L3): Claude Code CLI Mastery


- Installing Claude Code (Node.js 18+), `/init` to scan codebase
- Quick Reference Commands: `/init`, `/compact`, `/doccat`, `Shift+Tab`, `Tab`, `E
- `~/.claude/CLAUDE.md` → Global (all projects)
- `~/CLAUDE.md` → Parent (monorepo root)
- `./CLAUDE.md` → Project (shared on git)
- `./frontend/CLAUDE.md` → Subfolder (scoped context)
- `cd project && claude` → Plan Mode → Describe intent → Auto Accept → `/compact`


- Module 90: Claude Code: 4-Layer Architecture [Core] | Tools: CLAUDE.md, Skills,
- Module 93: GitHub Copilot for AI Development [Core] | Tools: Copilot, VS Code, C


- Claude Code sends an incoming call notification to the developer's Apple Watch
- Developer (Steve) asks: "Hey Steve, which database should I use for your app?"
- Claude Code responds: "SQLite and Postgres are good, search which is better." →
- Claude Code recommends: "Your app is simple so SQLite is a great start!"
- Developer instructs: "Cool, use SQLite and implement the account creation backen
- Claude Code: "Will do! I'll call you when I'm done."
- `Claude > Implementing account creation with SQLite...`
- `Building backend flow...`


- Claude Code Course (Coursera)** — https://www.coursera.org/learn/claude-code-in-

