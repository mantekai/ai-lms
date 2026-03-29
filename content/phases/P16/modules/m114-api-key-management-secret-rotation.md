---
journey_id: '16.2'
module_num: 114
phase_code: P16
title: 'API Key Management & Secret Rotation'
tools: 'Vault, AWS Secrets Manager'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 16.2 — API Key Management & Secret Rotation

**16.2 — API Key Management & Secret Rotation** [Core] | Tools: `Vault, AWS Secrets Manager`
- Learn: OverviewModule 114 (P16) — API Key Management & Secret Rotation. Tools focus: Vault, AWS Secrets Manager. Core path — prioritize in your sprint.API keys belong in vaults (Vault, cloud secret managers) with rotation, audit, and least privilege paths. Never log secret values.
- Practice: Store one secret in Vault or cloud SM; read from app at boot.Rotate key; verify zero-downtime reload strategy.grep/scan repo for accidental keys (gitleaks).Define break-glass access procedure.Document quarterly rotation calendar.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`
