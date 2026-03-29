---
journey_id: '3.5'
module_num: 26
phase_code: P3
title: 'API Authentication & Rate Limiting'
tools: 'API keys, backoff, tenacity'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 3.5 — API Authentication & Rate Limiting

**3.5 — API Authentication & Rate Limiting** [Core] | Tools: `API keys, backoff, tenacity`
- Learn: OverviewModule 26 (P3) — API Authentication & Rate Limiting. Tools focus: API keys, backoff, tenacity. Core path — prioritize in your sprint.Production API usage requires key rotation, least privilege keys, exponential backoff on 429/5xx, and idempotency for retried writes. Centralize secrets in vaults or managed stores.Practice reading Retry-After headers and structuring tenacity (or equivalent) policies.
- Practice: Implement retries with jitter; never retry non-idempotent POSTs blindly without design.Log HTTP status and request id only — not payloads with PII.Simulate rate limits with a mock server or tiny limit in a test key.Document key rotation procedure for your team (who, how often, blast radius).Add a circuit breaker sketch: after N failures, fail fast and alert.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
