<!-- Extracted from content/spec/agentiq_platform_spec.md — run: python3 scripts/extract_platform_docs.py — Manish.AI -->

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
