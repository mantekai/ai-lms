<!-- Extracted from content/spec/agentiq_platform_spec.md — run: python3 scripts/extract_platform_docs.py — Manish.AI -->

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
