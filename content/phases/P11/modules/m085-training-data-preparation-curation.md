---
journey_id: '11.4'
module_num: 85
phase_code: P11
title: 'Training Data Preparation & Curation'
tools: 'datasets, Argilla, Label Studio'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 11.4 — Training Data Preparation & Curation

**11.4 — Training Data Preparation & Curation** [Core] | Tools: `datasets, Argilla, Label Studio`
- Learn: OverviewModule 85 (P11) — Training Data Preparation & Curation. Tools focus: datasets, Argilla, Label Studio. Core path — prioritize in your sprint.Data curation beats raw scale: dedupe, toxicity filters, format normalization, and human review for high-stakes labels. Argilla/Label Studio structure feedback loops.
- Practice: Ingest 100 rows; profile duplicates and label imbalance.Define annotation guidelines for one task; run 20 double-labels.Compute inter-annotator agreement roughly.Export JSONL for training; scrub PII with regex + manual spot check.Write data versioning plan (DVC or simple manifest).
- Code: `# Module 85 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 85, "topic": "Training Data Preparation & Curatio`
