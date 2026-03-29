<!-- Extracted from content/spec/agentiq_platform_spec.md — run: python3 scripts/extract_platform_docs.py — Manish.AI -->

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
