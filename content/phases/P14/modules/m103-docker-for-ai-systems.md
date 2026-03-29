---
journey_id: '14.4'
module_num: 103
phase_code: P14
title: 'Docker for AI Systems'
tools: 'Docker, docker-compose'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 14.4 — Docker for AI Systems

**14.4 — Docker for AI Systems** [Core] | Tools: `Docker, docker-compose`
- Learn: OverviewModule 103 (P14) — Docker for AI Systems. Tools focus: Docker, docker-compose. Core path — prioritize in your sprint.Docker packages dependencies reproducibly; multi-stage builds shrink images. For AI images, watch CUDA base sizes and layer caching for model weights.
- Practice: Write Dockerfile for FastAPI app; run locally.Add docker-compose with depends_on + healthcheck.Use .dockerignore to skip models and secrets.Scan image with trivy or docker scout; patch criticals.Document promote path: dev → staging tags.
- Code: `docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
# Open http://localhost:5678 — build a webhook → HTTP Request → LLM flow`
