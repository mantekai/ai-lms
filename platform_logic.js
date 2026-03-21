/* AI Master Tracker — app shell, navigation, progress. Manish.AI */
const CURRICULUM = JSON.parse(document.getElementById('CURRICULUM_JSON').textContent);
const PHASES = CURRICULUM.phases;
let COVERAGE = { modules: [], blueprint_crosswalk: [], legend: {} };
(function loadCoverage() {
  try {
    const el = document.getElementById('COVERAGE_JSON');
    if (el && el.textContent.trim()) COVERAGE = JSON.parse(el.textContent);
  } catch (e) {
    console.warn('COVERAGE_JSON parse failed', e);
  }
})();
const KEY = 'ai_master_tracker_v1';

let flatModuleCache = null;
function flatModules() {
  if (flatModuleCache) return flatModuleCache;
  flatModuleCache = [];
  PHASES.forEach((ph, pi) => {
    ph.modules.forEach((m, mi) => {
      flatModuleCache.push({ ...m, phaseIdx: pi, modIdx: mi, phaseName: ph.name, phaseCode: ph.code });
    });
  });
  return flatModuleCache;
}

function loadState() {
  try {
    return JSON.parse(localStorage.getItem(KEY)) || defaultState();
  } catch {
    return defaultState();
  }
}
function defaultState() {
  return { modules: {}, certs: {}, portfolio: [], migrated: true };
}
function saveState(s) {
  localStorage.setItem(KEY, JSON.stringify(s));
}
let state = loadState();

function modKey(id) {
  return 'm' + id;
}
function isDone(id) {
  return !!state.modules[modKey(id)];
}
function setDone(id, v) {
  if (v) state.modules[modKey(id)] = true;
  else delete state.modules[modKey(id)];
  saveState(state);
}

function totalMods() {
  return flatModules().length;
}
function doneCount() {
  return flatModsDone();
}
function flatModsDone() {
  return flatModules().filter((m) => isDone(m.id)).length;
}
function phaseDoneCount(pi) {
  return PHASES[pi].modules.filter((m) => isDone(m.id)).length;
}
function phasePct(pi) {
  const t = PHASES[pi].modules.length;
  return t ? Math.round((phaseDoneCount(pi) / t) * 100) : 0;
}
function globalPct() {
  const t = totalMods();
  return t ? Math.round((doneCount() / t) * 100) : 0;
}

function p0GateOk() {
  return [0, 1, 2].every((id) => isDone(id));
}

const NAV_PAGES = [
  { id: 'dashboard', label: 'Dashboard', icon: '🏠' },
  { id: 'coverage', label: 'Topic coverage', icon: '📋' },
  { id: 'modules', label: 'All Phases', icon: '📚' },
  { id: 'capstone', label: 'Capstones', icon: '🚀' },
  { id: 'hackathons', label: 'Hackathons', icon: '⚡' },
  { id: 'opensource', label: 'Open Source', icon: '📦' },
  { id: 'yc', label: 'YC Ideas', icon: '💡' },
  { id: 'certs', label: 'Cert Tracker', icon: '🎓' },
  { id: 'career', label: 'Career', icon: '💼' },
];

/** Cert & learning resources: price = free | paid | mixed (free prep, paid exam). Manish.AI */
const CERT_DEFS = [
  {
    id: 'google_ml',
    provider: 'Google Cloud',
    name: 'Generative AI Leader (+ PMLE depth)',
    url: 'https://cloud.google.com/learn/certification/generative-ai-leader',
    price: 'paid',
    kind: 'credential',
    studyPhases: 'P2, P3, P6, P7, P14',
    note: 'Separate exams; PMLE → cloud.google.com/learn/certification/machine-learning-engineer',
  },
  {
    id: 'google_skill_intro_genai',
    provider: 'Google Cloud',
    name: 'Introduction to Generative AI (Skills Boost)',
    url: 'https://www.cloudskillsboost.google/course_templates/536',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P2',
    note: 'Micro-course + optional skill badge',
  },
  {
    id: 'google_skill_path_leader',
    provider: 'Google Cloud',
    name: 'Generative AI Leader — prep path (Skills Boost)',
    url: 'https://www.cloudskillsboost.google/paths/1951',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P2, P3, P14',
    note: 'Aligns with GAL exam domains',
  },
  {
    id: 'google_skill_path_dev',
    provider: 'Google Cloud',
    name: 'Advanced: Generative AI for Developers (Skills Boost)',
    url: 'https://www.cloudskillsboost.google/paths/183',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P3, P6, P7',
    note: 'Technical path; labs may need GCP credits',
  },
  {
    id: 'aws_ai',
    provider: 'AWS',
    name: 'Certified AI Practitioner (AIF-C01)',
    url: 'https://aws.amazon.com/certification/certified-ai-practitioner/',
    price: 'paid',
    kind: 'credential',
    studyPhases: 'P3, P4, P7, P14, P16',
    note: 'Official proctored exam',
  },
  {
    id: 'aws_genai_hub',
    provider: 'AWS',
    name: 'Learn About Generative AI (training hub)',
    url: 'https://aws.amazon.com/training/learn-about/generative-ai/',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P3, P4',
    note: 'Curated digital courses & learning plans',
  },
  {
    id: 'aws_lp_genai_dev',
    provider: 'AWS',
    name: 'Generative AI Learning Plan for Developers (Skill Builder)',
    url: 'https://skillbuilder.aws/learning-plan/5C9XQBTXBB/generative-ai-learning-plan-for-developers-includes-labs/EGATKJP13J',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P3, P6, P7',
    note: 'Includes labs; free digital training',
  },
  {
    id: 'aws_lp_ai_practitioner',
    provider: 'AWS',
    name: 'AWS AI Practitioner Learning Plan (Skill Builder)',
    url: 'https://skillbuilder.aws/learning-plan/G8ENMJ5QBE/aws-artificial-intelligence-practitioner-learning-plan/SU2A1EJM1A',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P3, P4, P16',
    note: 'Prepares concepts used on AIF-C01',
  },
  {
    id: 'aws_bedrock_build',
    provider: 'AWS',
    name: 'Building Gen AI Apps with Amazon Bedrock (course)',
    url: 'https://skillbuilder.aws/learn/TM4ZAXTGEZ/building-generative-ai-applications-using-amazon-bedrock/WM6Z6ZHU7K',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P3, P6, P7',
    note: 'Bedrock APIs & patterns',
  },
  {
    id: 'azure_ai',
    provider: 'Microsoft',
    name: 'Azure AI Engineer (AI-102)',
    url: 'https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/',
    price: 'paid',
    kind: 'credential',
    studyPhases: 'P3, P4, P6, P7, P14',
    note: 'Proctored certification exam',
  },
  {
    id: 'azure_ai900',
    provider: 'Microsoft',
    name: 'Azure AI Fundamentals (AI-900)',
    url: 'https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/',
    price: 'mixed',
    kind: 'credential',
    studyPhases: 'P1, P3',
    note: 'Free Microsoft Learn prep; exam fee paid',
  },
  {
    id: 'ms_ai900_prep',
    provider: 'Microsoft',
    name: 'Get started with Azure AI Fundamentals (Learn path)',
    url: 'https://learn.microsoft.com/en-us/training/paths/get-started-azure-ai-fundamentals/',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P3',
    note: 'Maps to AI-900 topics',
  },
  {
    id: 'ms_browse_ai_paths',
    provider: 'Microsoft',
    name: 'Browse AI & ML learning paths (Microsoft Learn)',
    url: 'https://learn.microsoft.com/en-us/training/browse/?resource_type=learning%20path&products=azure&subjects=artificial-intelligence',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1–P16',
    note: 'Filter Azure + AI paths',
  },
  {
    id: 'nvidia',
    provider: 'NVIDIA',
    name: 'Generative AI LLM (NCA-GENL / NCP-GENL)',
    url: 'https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/',
    price: 'paid',
    kind: 'credential',
    studyPhases: 'P0, P1, P4, P6, P7',
    note: 'Professional track → nvidia.com/.../generative-ai-llm-professional/',
  },
  {
    id: 'nvidia_training',
    provider: 'NVIDIA',
    name: 'NVIDIA Training & DLI course catalog',
    url: 'https://www.nvidia.com/en-us/training/',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P0, P1, P11',
    note: 'Mix of free & paid workshops',
  },
  {
    id: 'ibm',
    provider: 'IBM',
    name: 'Generative AI Engineering (Coursera Professional Certificate)',
    url: 'https://www.coursera.org/professional-certificates/ibm-generative-ai-engineering',
    price: 'paid',
    kind: 'credential',
    studyPhases: 'P2, P4, P6, P16',
    note: 'Subscription / Coursera fee',
  },
  {
    id: 'ibm_skillsbuild_ai',
    provider: 'IBM',
    name: 'SkillsBuild — free learning (search AI courses)',
    url: 'https://skillsbuild.org/learners',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P2',
    note: 'Use catalog search for artificial intelligence topics',
  },
  {
    id: 'hf',
    provider: 'Hugging Face',
    name: 'Learn hub — LLM, Agents, audio, CV',
    url: 'https://huggingface.co/learn',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P4, P6, P7, P11',
    note: 'Courses & certificates of completion',
  },
  {
    id: 'hf_llm_course',
    provider: 'Hugging Face',
    name: 'LLM Course (chapter 1)',
    url: 'https://huggingface.co/learn/llm-course/chapter1/1',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P4, P7',
    note: 'Open models & transformers',
  },
  {
    id: 'hf_agents_course',
    provider: 'Hugging Face',
    name: 'Agents Course (introduction)',
    url: 'https://huggingface.co/learn/agents-course/unit0/introduction',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P4, P6',
    note: 'Tool use & agent loops',
  },
  {
    id: 'databricks_genai',
    provider: 'Databricks',
    name: 'Generative AI Fundamentals (accreditation)',
    url: 'https://www.databricks.com/resources/learn/training/generative-ai-fundamentals',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P7',
    note: 'Short videos + knowledge test + digital badge',
  },
  {
    id: 'kaggle_genai_5day',
    provider: 'Kaggle',
    name: '5-Day Intensive Generative AI (guide)',
    url: 'https://www.kaggle.com/learn-guide/5-day-genai',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P2, P7',
    note: 'Partner content; self-paced',
  },
  {
    id: 'kaggle_agents_5day',
    provider: 'Kaggle',
    name: '5-Day AI Agents Intensive (guide)',
    url: 'https://www.kaggle.com/learn-guide/5-day-agents',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P4, P6',
    note: 'Agent patterns & deployment topics',
  },
  {
    id: 'kaggle_ai_ethics',
    provider: 'Kaggle',
    name: 'Intro to AI Ethics (course)',
    url: 'https://www.kaggle.com/learn/intro-to-ai-ethics',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P2, P16',
    note: 'Responsible-AI foundations',
  },
  {
    id: 'deeplearning_ai',
    provider: 'DeepLearning.AI',
    name: 'Short courses (LLM apps, agents, RAG, etc.)',
    url: 'https://www.deeplearning.ai/courses/',
    price: 'mixed',
    kind: 'learning',
    studyPhases: 'P2, P4, P6, P7',
    note: 'Often free to audit; certificate paid',
  },
  {
    id: 'anthropic_courses_gh',
    provider: 'Anthropic',
    name: 'Educational course materials (GitHub)',
    url: 'https://github.com/anthropics/courses',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P2, P3, P4',
    note: 'Prompting & Claude-related exercises; no vendor exam',
  },
  {
    id: 'anthropic_docs',
    provider: 'Anthropic',
    name: 'Claude API — documentation',
    url: 'https://docs.anthropic.com/',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P3, P4, P16',
    note: 'Official API & safety docs',
  },
  {
    id: 'openai_cookbook',
    provider: 'OpenAI',
    name: 'OpenAI Cookbook (patterns & examples)',
    url: 'https://cookbook.openai.com/',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P3, P6, P7',
    note: 'No OpenAI exam; dev-focused',
  },
  {
    id: 'openai_docs',
    provider: 'OpenAI',
    name: 'OpenAI Platform documentation',
    url: 'https://platform.openai.com/docs',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P3, P4',
    note: 'API reference & guides',
  },
  {
    id: 'meta_blueprint',
    provider: 'Meta',
    name: 'Blueprint — training catalog',
    url: 'https://www.facebookblueprint.com/student/catalog',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P14',
    note: 'Ads & marketing AI topics; not an LLM-dev cert',
  },
  {
    id: 'oracle_ai_cert',
    provider: 'Oracle',
    name: 'Oracle certification program (AI & data exams)',
    url: 'https://education.oracle.com/oracle-certification-program',
    price: 'paid',
    kind: 'credential',
    studyPhases: 'P7, P14',
    note: 'Check catalog for current AI / OCI exams',
  },
  {
    id: 'sap_ai_learning',
    provider: 'SAP',
    name: 'SAP Learning Hub — search AI topics',
    url: 'https://learning.sap.com/',
    price: 'mixed',
    kind: 'learning',
    studyPhases: 'P14, P17',
    note: 'Enterprise AI courses; subscription varies',
  },
  {
    id: 'snowflake_ai_learn',
    provider: 'Snowflake',
    name: 'Snowflake Learning — AI & ML catalog',
    url: 'https://learn.snowflake.com/',
    price: 'mixed',
    kind: 'learning',
    studyPhases: 'P7, P14',
    note: 'Free & paid modules; filter for AI/ML',
  },
  {
    id: 'mongo_db_ai',
    provider: 'MongoDB',
    name: 'MongoDB University — AI & vector search topics',
    url: 'https://learn.mongodb.com/catalog',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P7',
    note: 'RAG-friendly data patterns',
  },
  {
    id: 'fast_ai_practical',
    provider: 'fast.ai',
    name: 'Practical Deep Learning for Coders',
    url: 'https://course.fast.ai/',
    price: 'free',
    kind: 'learning',
    studyPhases: 'P1, P11',
    note: 'Practical ML; complements LLM modules',
  },
];

let certTrackerUi = { price: 'all', q: '' };

function certPriceCounts() {
  const o = { free: 0, paid: 0, mixed: 0 };
  CERT_DEFS.forEach((c) => {
    if (Object.prototype.hasOwnProperty.call(o, c.price)) o[c.price] += 1;
  });
  return o;
}

function setCertPriceFilter(v) {
  certTrackerUi.price = v;
  renderCertTracker();
}

function certDefsFiltered() {
  const price = certTrackerUi.price;
  const q = (certTrackerUi.q || '').trim().toLowerCase();
  return CERT_DEFS.filter((c) => {
    if (price !== 'all' && c.price !== price) return false;
    if (!q) return true;
    const blob = `${c.provider} ${c.name} ${c.note || ''} ${c.studyPhases || ''}`.toLowerCase();
    return blob.includes(q);
  });
}

function escapeAttr(s) {
  return String(s || '')
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/</g, '&lt;');
}

function onCertSearchInput(value) {
  certTrackerUi.q = value;
  clearTimeout(onCertSearchInput._t);
  onCertSearchInput._t = setTimeout(() => renderCertTracker(), 220);
}

const CAPSTONES = [
  {
    id: 'c1',
    title: 'Capstone 1 — AI That Calls You',
    subtitle: 'Human-in-the-loop voice escalation (blueprint)',
    stack: ['LangGraph', 'Twilio Voice', 'FastAPI', 'Ollama', 'Redis'],
    difficulty: 'Advanced',
    time: '1–2 weeks',
    desc: 'Autonomous agent pauses at risky decisions, places an outbound call, collects keypad input, resumes with full trace logging.',
    why: 'Demonstrates orchestration, HitL, telephony integration, and production-style state persistence.',
    arch: [
      { n: '1', title: 'Trigger', desc: 'Task starts via API; agent runs with local or hosted LLM.' },
      { n: '2', title: 'Execute', desc: 'Tools + memory; confidence and risk scored each step.' },
      { n: '3', title: 'Escalate', desc: 'Below-threshold confidence opens voice flow (Twilio).' },
      { n: '4', title: 'Decide', desc: 'User approves or rejects via keypad; webhook resumes graph.' },
      { n: '5', title: 'Audit', desc: 'Structured logs for compliance-style reviews.' },
    ],
    build: `<div class="cap-section"><h4>Deliverables</h4><div class="cb-text"><ul>
<li>Git repo with README and architecture diagram</li>
<li>FastAPI webhook for voice callback</li>
<li>2-minute demo recording</li>
</ul></div></div>
<div class="cap-section"><h4>Starter commands</h4>
<div class="code-block"><button class="copy-code" onclick="copyCode(this)">Copy</button><pre>pip install fastapi uvicorn twilio langgraph redis
<span class="cmt"># Use env vars for Twilio credentials — never commit secrets</span></pre></div></div>`,
    github: 'https://github.com/search?q=langgraph+twilio+human-in-the-loop&type=repositories',
  },
  {
    id: 'c2',
    title: 'Capstone 2 — AI Payment Risk Analyst',
    subtitle: 'RAG + compliance reasoning + reporting',
    stack: ['FastAPI', 'Vector DB', 'RAG', 'Streamlit', 'Claude or GPT-4'],
    difficulty: 'Advanced',
    time: '2–3 weeks',
    desc: 'Ingest policy and compliance text into a vector store, score synthetic transactions, produce explainable reports with cited clauses.',
    why: 'Shows RAG, structured risk output, and stakeholder-facing UI — common enterprise consulting deliverable.',
    arch: [
      { n: '1', title: 'Ingest', desc: 'Chunk and embed policy docs (synthetic sample data only).' },
      { n: '2', title: 'Retrieve', desc: 'Hybrid search for rules relevant to each transaction.' },
      { n: '3', title: 'Reason', desc: 'LLM outputs score, summary, and cited rule IDs.' },
      { n: '4', title: 'Review UI', desc: 'Streamlit for officers to browse flagged items.' },
    ],
    build: `<div class="cap-section"><h4>Sample FastAPI shape</h4>
<div class="code-block"><button class="copy-code" onclick="copyCode(this)">Copy</button><pre><span class="kw">from</span> fastapi <span class="kw">import</span> FastAPI
app = FastAPI()

@app.post(<span class="str">"/risk_score"</span>)
<span class="kw">def</span> <span class="fn">risk_score</span>(txn: dict):
    <span class="cmt"># 1) retrieve rules  2) LLM structured output  3) return JSON</span>
    <span class="kw">return</span> {<span class="str">"score"</span>: <span class="num">0</span>, <span class="str">"citations"</span>: [], <span class="str">"rationale"</span>: <span class="str">""</span>}</pre></div></div>`,
    github: 'https://github.com/search?q=rag+fraud+compliance+fastapi&type=repositories',
  },
  {
    id: 'c3',
    title: 'Capstone 3 — Local Perplexity-Style Search',
    subtitle: 'Ollama + SearXNG + cited answers',
    stack: ['Ollama', 'SearXNG', 'Docker', 'Streamlit', 'LangChain'],
    difficulty: 'Intermediate',
    time: '3–7 days',
    desc: 'Self-hosted meta-search plus local LLM to synthesize answers with source cards — no paid LLM required.',
    why: 'Proves you can ship privacy-preserving research tooling entirely on your hardware.',
    arch: [
      { n: '1', title: 'Search', desc: 'SearXNG returns ranked URLs and snippets.' },
      { n: '2', title: 'Fetch', desc: 'Optional light fetch for top hits (respect robots.txt).' },
      { n: '3', title: 'Synthesize', desc: 'Local model cites sources in the response.' },
      { n: '4', title: 'Chat UI', desc: 'Streamlit with history and model picker.' },
    ],
    build: `<div class="cap-section"><h4>Docker Compose sketch</h4>
<div class="code-block"><button class="copy-code" onclick="copyCode(this)">Copy</button><pre><span class="cmt"># services: searxng, ollama (or use host), streamlit app</span>
<span class="cmt"># Keep all endpoints on localhost for a safe default</span></pre></div></div>`,
    github: 'https://github.com/search?q=ollama+searxng+langchain&type=repositories',
  },
];

const HACKATHONS = [
  {
    icon: '⚡',
    title: 'Anthropic AI Safety Hackathon',
    org: 'Anthropic',
    prize: '~$50K (varies by event)',
    deadline: 'Check official site for next dates',
    theme: 'Safety, interpretability, alignment',
    prep: 'Complete P2 Prompting + P16 Security modules first',
    template: 'Guardrailed agent + eval harness + short policy doc',
    winners: 'Winning teams often combine strong eval metrics with crisp demos (Streamlit/FastAPI).',
    desc: 'Build systems with safety or interpretability focus; mentor access from lab engineers.',
    meta: ['🟢 Recurring', '💰 Prizes', '🌍 Online'],
    link: 'https://www.anthropic.com/',
  },
  {
    icon: '🤗',
    title: 'Hugging Face Open-Source Sprint',
    org: 'HuggingFace',
    prize: 'Hub credits + visibility',
    deadline: 'Quarterly sprints',
    theme: 'Models, datasets, Spaces',
    prep: 'P1 foundations + P6 frameworks + P7 RAG',
    template: 'Gradio Space + dataset card + small model or adapter',
    winners: 'Top entries ship clean cards, reproducible training, and eval tables.',
    desc: '48-hour style sprints for Hub-ready artifacts.',
    meta: ['🟢 Quarterly', '🆓 Free entry', '🌍 Global'],
    link: 'https://huggingface.co/',
  },
  {
    icon: '🏆',
    title: 'Devpost AI Hackathons',
    org: 'Devpost',
    prize: '$10K–$100K depending on sponsor',
    deadline: 'Rolling calendar',
    theme: 'Sponsor-specific (Gemini, AWS, Azure, …)',
    prep: 'P3 LLM APIs + P14 deployment',
    template: 'MVP API + minimal UI + 90-second demo video',
    winners: 'Clear problem statement + live demo + public repo fork win most tracks.',
    desc: 'Filter by AI; many enterprise-sponsored challenges.',
    meta: ['🟢 Ongoing', '💰 Variable', '🌍 Global'],
    link: 'https://devpost.com/hackathons?themes=ai',
  },
  {
    icon: '🔵',
    title: 'LangGraph Build Challenge',
    org: 'LangChain',
    prize: 'Credits + ecosystem visibility',
    deadline: 'Periodic announcements',
    theme: 'Production agents',
    prep: 'P4 Agents + P6 LangGraph depth',
    template: 'StateGraph + tool routing + LangSmith traces',
    winners: 'Projects with traces, tests, and Dockerfile score highest.',
    desc: 'Focus on durable, deployable LangGraph apps.',
    meta: ['🟡 Periodic', '💰 Credits', '🌍 Global'],
    link: 'https://python.langchain.com/',
  },
  {
    icon: '🌐',
    title: 'Google AI Hackathon (Gemini)',
    org: 'Google',
    prize: 'Large pooled prizes (see site)',
    deadline: 'Annual / regional',
    theme: 'Gemini API apps',
    prep: 'P3 multimodal + P14 FastAPI/Streamlit',
    template: 'Gemini tool use + OAuth + hosted demo',
    winners: 'Creative multimodal UX with latency under control.',
    desc: 'Build on Gemini with mentor office hours.',
    meta: ['🟢 Major events', '💰 High pool', '🌍 Global'],
    link: 'https://ai.google.dev/',
  },
  {
    icon: '🤖',
    title: 'CrewAI Multi-Agent Challenge',
    org: 'CrewAI',
    prize: 'Cash + enterprise intros',
    deadline: 'Periodic',
    theme: 'Multi-agent crews',
    prep: 'P4 collaboration + P6 CrewAI module',
    template: 'Defined roles + sequential process + task outputs',
    winners: 'Clear agent boundaries and measurable task success.',
    desc: 'Enterprise-flavored multi-agent builds.',
    meta: ['🟡 Periodic', '💰 Mixed', '🌍 Global'],
    link: 'https://www.crewai.com/',
  },
  {
    icon: '💡',
    title: 'n8n Automation Hackathon',
    org: 'n8n',
    prize: '~$5K (see rules)',
    deadline: 'Quarterly',
    theme: 'Workflow + AI nodes',
    prep: 'P13 automation modules',
    template: 'Webhook → LLM → CRM/Slack with error branch',
    winners: 'Reusable templates published to marketplace trend well.',
    desc: 'AI-powered automations in n8n.',
    meta: ['🟢 Quarterly', '💰 Prizes', '🌍 Global'],
    link: 'https://n8n.io/',
  },
];

const OPENSOURCE = [
  {
    icon: '🤗',
    title: 'Hugging Face smol-course',
    org: 'HuggingFace',
    diff: 'Beginner → Intermediate',
    desc: 'Small-model training curriculum; contribute notebooks and examples.',
    tags: ['Python', 'PyTorch'],
    link: 'https://github.com/huggingface/smol-course',
  },
  {
    icon: '🔗',
    title: 'LangGraph',
    org: 'LangChain',
    diff: 'Intermediate',
    desc: 'Stateful agents; fix docs, add tools, improve examples.',
    tags: ['Python', 'TS'],
    link: 'https://github.com/langchain-ai/langgraph',
  },
  {
    icon: '🦙',
    title: 'Ollama',
    org: 'Ollama',
    diff: 'Beginner-friendly',
    desc: 'Local model runner; Modelfiles and docs welcome.',
    tags: ['Go'],
    link: 'https://github.com/ollama/ollama',
  },
  {
    icon: '🔌',
    title: 'MCP Servers',
    org: 'Model Context Protocol',
    diff: 'Intermediate → Advanced',
    desc: 'Reference servers and patterns for tool exposure.',
    tags: ['Python', 'TypeScript'],
    link: 'https://github.com/modelcontextprotocol/servers',
  },
  {
    icon: '🚀',
    title: 'Dify',
    org: 'Community',
    diff: 'Intermediate',
    desc: 'Open LLMOps UI; plugins and integrations.',
    tags: ['Python', 'Vue'],
    link: 'https://github.com/langgenius/dify',
  },
];

const YC_IDEAS = [
  {
    title: 'AI policy copilot for regulated orgs',
    problem: 'Teams drown in internal policy updates.',
    solution: 'RAG over policy corpuses with citation-only answers.',
    stack: 'P7 RAG, P8 MCP, P14 FastAPI',
    market: 'Large governance / compliance software TAM (indicative billions class).',
    mvp: 'Upload PDFs → query API → Slack bot in 2 weeks.',
  },
  {
    title: 'Meeting → action-item router',
    problem: 'Action items die in notes after calls.',
    solution: 'Transcript → structured tasks → Jira/Asana via agents.',
    stack: 'P4 Agents, P5 tools, P13 n8n',
    market: 'Productivity / collaboration segment.',
    mvp: 'Webhook + single integration + reviewer UI.',
  },
  {
    title: 'Sales email personalizer (bounded)',
    problem: 'Generic outreach converts poorly.',
    solution: 'Template-safe LLM that only fills approved slots from CRM fields.',
    stack: 'P2 prompting, P16 safety, P3 APIs',
    market: 'GTM tooling; crowded but always in demand.',
    mvp: 'CSV in → CSV out with moderation filter.',
  },
  {
    title: 'Onboarding assistant for internal wikis',
    problem: 'New hires cannot find canonical docs.',
    solution: 'Agent answers from verified sources with links.',
    stack: 'P7 RAG, P10 unified stack, P14 hosting',
    market: 'Enterprise internal tools.',
    mvp: 'Single Confluence space + chat UI.',
  },
  {
    title: 'Agent observability starter pack',
    problem: 'No tracing for ad-hoc LLM scripts.',
    solution: 'Drop-in OpenTelemetry + LangSmith-style dashboard template.',
    stack: 'P15 monitoring, P10 observability layer',
    market: 'Developer tooling for AI teams.',
    mvp: 'One FastAPI service with exemplar traces.',
  },
];

let currentPage = 'dashboard';

let coverageFilter = { phase: '', tier: '', q: '' };

function setCovFilter(key, value) {
  coverageFilter[key] = value;
  renderCoverage();
}

function exportCoverageModuleCSV() {
  const hdr = [
    'phase_code',
    'module_num',
    'module_title',
    'priority',
    'content_tier',
    'self_contained_on_page',
    'blueprint_ref',
    'coverage_notes',
  ];
  const rows = [hdr];
  (COVERAGE.modules || []).forEach((m) => {
    rows.push([
      m.phase_code,
      m.module_num,
      m.module_title,
      m.priority,
      m.content_tier,
      m.self_contained_on_page,
      m.blueprint_ref || '',
      (m.coverage_notes || '').replace(/\r?\n/g, ' '),
    ]);
  });
  const esc = (c) => (/[",\n]/.test(String(c)) ? '"' + String(c).replace(/"/g, '""') + '"' : c);
  downloadText(
    'topics_coverage_export.csv',
    rows.map((r) => r.map(esc).join(',')).join('\n'),
    'text/csv',
  );
  showToast('CSV exported');
}

function renderCoverage() {
  const el = document.getElementById('page-coverage');
  if (!el) return;
  const mods = COVERAGE.modules || [];
  const cx = COVERAGE.blueprint_crosswalk || [];
  const phases = [...new Set(mods.map((m) => m.phase_code))];
  const filtered = mods.filter((m) => {
    if (coverageFilter.phase && m.phase_code !== coverageFilter.phase) return false;
    if (coverageFilter.tier && m.self_contained_on_page !== coverageFilter.tier) return false;
    if (coverageFilter.q && !String(m.module_title).toLowerCase().includes(coverageFilter.q.toLowerCase())) return false;
    return true;
  });
  let yes = 0;
  let partial = 0;
  let no = 0;
  mods.forEach((m) => {
    if (m.self_contained_on_page === 'yes') yes++;
    else if (m.self_contained_on_page === 'partial') partial++;
    else no++;
  });
  const badge = (v) => {
    if (v === 'yes') return '<span class="badge-yes">yes</span>';
    if (v === 'partial') return '<span class="badge-partial">partial</span>';
    return '<span class="badge-no">no</span>';
  };
  el.innerHTML = `
<div class="dash-hero">
  <h1>Topic &amp; content coverage</h1>
  <p>Aligned to the Master Tracker blueprint: primary learning for each module lives in <strong>Learn / Steps / Code</strong> tabs. Use <code>content/modules/mNNN.json</code> only when you want to override or extend a row.</p>
</div>
<div class="stats-grid" style="grid-template-columns:repeat(3,1fr);margin-bottom:18px">
  <div class="stat-card sc-green"><div class="sc-label">On-page (full)</div><div class="sc-val">${yes}</div><div class="sc-sub">modules</div></div>
  <div class="stat-card sc-orange"><div class="sc-label">Partial</div><div class="sc-val">${partial}</div><div class="sc-sub">modules</div></div>
  <div class="stat-card sc-blue"><div class="sc-label">Scaffold only</div><div class="sc-val">${no}</div><div class="sc-sub">need enrichment</div></div>
</div>
<div class="coverage-toolbar">
  <label>Phase <select id="cov-sel-ph" onchange="setCovFilter('phase',this.value)">
    <option value="">All</option>
    ${phases.map((p) => `<option value="${p}" ${coverageFilter.phase === p ? 'selected' : ''}>${p}</option>`).join('')}
  </select></label>
  <label>On-page <select id="cov-sel-tier" onchange="setCovFilter('tier',this.value)">
    <option value="">Any</option>
    <option value="yes" ${coverageFilter.tier === 'yes' ? 'selected' : ''}>yes</option>
    <option value="partial" ${coverageFilter.tier === 'partial' ? 'selected' : ''}>partial</option>
    <option value="no" ${coverageFilter.tier === 'no' ? 'selected' : ''}>no</option>
  </select></label>
  <input type="search" placeholder="Search title…" value="${escapeHtml(coverageFilter.q)}" oninput="setCovFilter('q',this.value)" style="min-width:180px;flex:1;max-width:280px" />
  <button type="button" class="topbar-action" onclick="exportCoverageModuleCSV()">⬇ Export tracker CSV</button>
</div>
<div class="cov-table-wrap">
<table class="cov-table">
<thead><tr>
  <th>Phase</th><th>#</th><th>Module</th><th>Priority</th><th>Tier</th><th>On-page</th><th>Blueprint ref</th><th>Notes</th>
</tr></thead>
<tbody>
${filtered
  .map(
    (m) => `<tr>
  <td>${m.phase_code}</td>
  <td>${m.module_num}</td>
  <td><a href="#" onclick="event.preventDefault();showPage('mod-${m.module_num - 1}');" class="ext-link">${escapeHtml(m.module_title)}</a></td>
  <td>${m.priority === 'MUST DO' ? 'Core' : 'Opt'}</td>
  <td>${m.content_tier}</td>
  <td>${badge(m.self_contained_on_page)}</td>
  <td style="font-size:10px;color:var(--muted)">${escapeHtml(m.blueprint_ref || '')}</td>
  <td style="font-size:10px;color:var(--muted)">${escapeHtml(m.coverage_notes || '')}</td>
</tr>`,
  )
  .join('')}
</tbody>
</table>
</div>
<p style="font-size:11px;color:var(--muted);margin:10px 0 20px">Showing ${filtered.length} of ${mods.length} modules.</p>
<div class="section-hd">Blueprint crosswalk <span class="cnt">doc §2 → modules</span></div>
<div style="margin-bottom:24px">
${cx
  .map(
    (c) => `<div class="crosswalk-card">
  <div class="cx-topic">${escapeHtml(c.topic)}</div>
  <div class="cx-meta"><strong>${escapeHtml(c.doc_ref)}</strong> · status: ${escapeHtml(c.tracker_status)} · modules: ${(c.module_nums || []).join(', ')}</div>
</div>`,
  )
  .join('')}
</div>`;
}

function buildSidebar() {
  const nav = document.getElementById('sb-nav');
  nav.innerHTML = '';
  nav.innerHTML += `<div class="nav-section">Navigation</div>`;
  NAV_PAGES.forEach((p) => {
    let badge = '';
    if (p.id === 'capstone') badge = `<span class="ni-badge">${CAPSTONES.length}</span>`;
    if (p.id === 'hackathons') badge = `<span class="ni-badge">${HACKATHONS.length}</span>`;
    if (p.id === 'opensource') badge = `<span class="ni-badge">${OPENSOURCE.length}</span>`;
    if (p.id === 'yc') badge = `<span class="ni-badge">${YC_IDEAS.length}</span>`;
    if (p.id === 'certs') badge = `<span class="ni-badge">${CERT_DEFS.length}</span>`;
    if (p.id === 'coverage') {
      const full = (COVERAGE.modules || []).filter((r) => r.self_contained_on_page === 'yes').length;
      badge = `<span class="ni-badge">${full}/${COVERAGE.modules?.length || 0}</span>`;
    }
    nav.innerHTML += `<div class="nav-item ${currentPage === p.id ? 'active' : ''}" onclick="showPage('${p.id}')" id="nav-${p.id}">
      <span class="ni-icon">${p.icon}</span>${p.label}${badge}
    </div>`;
  });
  nav.innerHTML += `<div class="nav-section">Phases (20)</div>`;
  PHASES.forEach((ph, pi) => {
    const pct = phasePct(pi);
    nav.innerHTML += `<div class="nav-item ${currentPage === 'phase-' + pi ? 'active' : ''}" onclick="showPage('phase-${pi}')" id="nav-phase-${pi}">
      <span class="ni-icon">${ph.icon}</span>${ph.code}: ${ph.name}
      <span class="ni-prog">${pct}%</span>
    </div>`;
  });
}

function updateSidebarProgress() {
  const pct = globalPct();
  document.getElementById('sb-pct').textContent = pct + '%';
  document.getElementById('sb-fill').style.width = pct + '%';
  PHASES.forEach((_, pi) => {
    const el = document.getElementById('nav-phase-' + pi);
    if (el) {
      const pr = el.querySelector('.ni-prog');
      if (pr) pr.textContent = phasePct(pi) + '%';
    }
  });
}

let sidebarCollapsed = false;
function toggleSidebar() {
  sidebarCollapsed = !sidebarCollapsed;
  document.getElementById('sidebar').classList.toggle('collapsed', sidebarCollapsed);
  const ov = document.getElementById('overlay');
  if (window.innerWidth <= 768) ov.classList.toggle('show', !sidebarCollapsed);
}

function showPage(id) {
  currentPage = id;
  document.querySelectorAll('.page').forEach((p) => p.classList.remove('active'));
  document.getElementById('main').scrollTop = 0;
  buildSidebar();

  if (id === 'dashboard') {
    renderDashboard();
    document.getElementById('page-dashboard').classList.add('active');
    document.getElementById('topbar-title').textContent = 'Dashboard';
  } else if (id === 'coverage') {
    renderCoverage();
    document.getElementById('page-coverage').classList.add('active');
    document.getElementById('topbar-title').textContent = 'Topic coverage';
  } else if (id === 'modules') {
    renderAllPhases();
    document.getElementById('page-modules').classList.add('active');
    document.getElementById('topbar-title').textContent = 'All Phases';
  } else if (id.startsWith('phase-')) {
    const pi = parseInt(id.split('-')[1], 10);
    renderPhase(pi);
    document.getElementById('page-modules').classList.add('active');
    document.getElementById('topbar-title').textContent = PHASES[pi].name;
  } else if (id.startsWith('mod-')) {
    const mid = parseInt(id.split('-')[1], 10);
    renderModule(mid);
    document.getElementById('page-modules').classList.add('active');
    const m = flatModules().find((x) => x.id === mid);
    document.getElementById('topbar-title').textContent = m ? m.title : 'Module';
  } else if (id === 'capstone') {
    renderCapstone();
    document.getElementById('page-capstone').classList.add('active');
    document.getElementById('topbar-title').textContent = 'Capstones';
  } else if (id === 'hackathons') {
    renderHackathons();
    document.getElementById('page-hackathons').classList.add('active');
    document.getElementById('topbar-title').textContent = 'Hackathons';
  } else if (id === 'opensource') {
    renderOSS();
    document.getElementById('page-opensource').classList.add('active');
    document.getElementById('topbar-title').textContent = 'Open Source';
  } else if (id === 'yc') {
    renderYC();
    document.getElementById('page-yc').classList.add('active');
    document.getElementById('topbar-title').textContent = 'YC-Style Ideas';
  } else if (id === 'certs') {
    renderCertTracker();
    document.getElementById('page-certs').classList.add('active');
    document.getElementById('topbar-title').textContent = 'Certifications';
  } else if (id === 'career') {
    renderCareer();
    document.getElementById('page-career').classList.add('active');
    document.getElementById('topbar-title').textContent = 'Career';
  }

  if (window.innerWidth <= 768 && !sidebarCollapsed) toggleSidebar();
}

function renderDashboard() {
  const el = document.getElementById('page-dashboard');
  const done = doneCount();
  const total = totalMods();
  const pct = globalPct();
  const cc = certCounts();
  el.innerHTML = `
<div class="dash-hero">
  <h1>AI Master Tracker</h1>
  <p>133 modules · 20 phases · local-first progress (JSON + CSV). ${pct > 0 ? pct + '% complete.' : 'Start with P0 Local AI Setup.'}</p>
</div>
${!p0GateOk() ? `<div class="gate-banner">Complete <strong>P0 modules 1–3</strong> (Ollama, LM Studio, Open WebUI) before deep-diving later phases — blueprint rule #1. You can still browse.</div>` : ''}
<div class="stats-grid stats-grid-5">
  <div class="stat-card sc-purple"><div class="sc-label">Modules done</div><div class="sc-val">${done}</div><div class="sc-sub">of ${total}</div></div>
  <div class="stat-card sc-gold"><div class="sc-label">Certs passed</div><div class="sc-val">${cc.passed}</div><div class="sc-sub">of ${cc.total} · ${cc.inProgress} in progress</div></div>
  <div class="stat-card sc-green"><div class="sc-label">Phases touched</div><div class="sc-val">${PHASES.filter((_, i) => phaseDoneCount(i) > 0).length}</div><div class="sc-sub">of ${PHASES.length}</div></div>
  <div class="stat-card sc-orange"><div class="sc-label">Progress</div><div class="sc-val">${pct}%</div><div class="sc-sub">global modules</div></div>
  <div class="stat-card sc-blue"><div class="sc-label">Remaining</div><div class="sc-val">${total - done}</div><div class="sc-sub">modules</div></div>
</div>
<div class="section-hd">Phases <span class="cnt">${PHASES.length}</span></div>
<div class="module-grid">${PHASES.map((ph, pi) => {
  const p = phasePct(pi);
  const d = phaseDoneCount(pi);
  const t = ph.modules.length;
  return `<div class="mod-card ${ph.color}" onclick="showPage('phase-${pi}')">
    <div class="mod-card-hd"><div class="mod-icon">${ph.icon}</div><div><div class="mod-title">${ph.code} — ${ph.name}</div><div class="mod-desc">${ph.purpose}</div></div></div>
    <div class="mod-stats"><span>${d} / ${t} modules</span></div>
    <div class="mod-prog"><div class="mod-prog-fill" style="background:${phaseColor(ph.color)};width:${p}%"></div></div>
    <div class="mod-footer"><span class="mod-pct">${p}%</span></div>
  </div>`;
}).join('')}</div>
<div class="section-hd">Shortcuts</div>
<div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:24px">
  <div class="mod-card mc-5" style="min-width:200px;cursor:pointer" onclick="showPage('capstone')"><div class="mod-card-hd"><div class="mod-icon">🚀</div><div><div class="mod-title">Capstones</div><div class="mod-desc">${CAPSTONES.length} blueprint projects</div></div></div></div>
  <div class="mod-card mc-6" style="min-width:200px;cursor:pointer" onclick="showPage('hackathons')"><div class="mod-card-hd"><div class="mod-icon">⚡</div><div><div class="mod-title">Hackathons</div><div class="mod-desc">Prep paths + templates</div></div></div></div>
  <div class="mod-card mc-7" style="min-width:200px;cursor:pointer" onclick="showPage('career')"><div class="mod-card-hd"><div class="mod-icon">💼</div><div><div class="mod-title">Career</div><div class="mod-desc">Readiness + LinkedIn</div></div></div></div>
  <div class="mod-card mc-1" style="min-width:200px;cursor:pointer" onclick="showPage('coverage')"><div class="mod-card-hd"><div class="mod-icon">📋</div><div><div class="mod-title">Topic coverage</div><div class="mod-desc">CSV tracker · blueprint map</div></div></div></div>
</div>`;
}

function phaseColor(cls) {
  const colors = {
    'mc-0': '#60a5fa',
    'mc-1': '#c084fc',
    'mc-2': '#fb923c',
    'mc-3': '#4ade80',
    'mc-4': '#f87171',
    'mc-5': '#34d399',
    'mc-6': '#fbbf24',
    'mc-7': '#818cf8',
    'mc-8': '#e879f9',
    'mc-9': '#2dd4bf',
    'mc-10': '#f87171',
    'mc-11': '#a78bfa',
    'mc-12': '#f472b6',
  };
  return colors[cls] || '#c084fc';
}

function renderAllPhases() {
  const el = document.getElementById('page-modules');
  el.innerHTML = `<div class="back-btn" onclick="showPage('dashboard')">← Dashboard</div>
<div class="section-hd">All phases</div>
<div class="module-grid">${PHASES.map((ph, pi) => {
  const p = phasePct(pi);
  const d = phaseDoneCount(pi);
  const t = ph.modules.length;
  return `<div class="mod-card ${ph.color}" onclick="showPage('phase-${pi}')">
    <div class="mod-card-hd"><div class="mod-icon">${ph.icon}</div><div><div class="mod-title">${ph.code} — ${ph.name}</div><div class="mod-desc">${ph.purpose}</div></div></div>
    <div class="mod-stats"><span>${d} / ${t}</span></div>
    <div class="mod-prog"><div class="mod-prog-fill" style="background:${phaseColor(ph.color)};width:${p}%"></div></div>
    <div class="mod-footer"><span class="mod-pct">${p}%</span></div>
  </div>`;
}).join('')}</div>`;
}

function renderPhase(pi) {
  const ph = PHASES[pi];
  const el = document.getElementById('page-modules');
  const doneN = phaseDoneCount(pi);
  const totalN = ph.modules.length;
  const banner = doneN === totalN && totalN ? `<div class="done-banner show">Phase complete — ${ph.name}</div>` : '';
  let list = ph.modules
    .map((m) => {
      const done = isDone(m.id);
      return `
<div class="lesson-item ${done ? 'done' : ''}" id="row-mod-${m.id}">
  <div class="lesson-header" onclick="showPage('mod-${m.id}')">
    <div class="lesson-num">${m.num}</div>
    <div class="lesson-check" onclick="event.stopPropagation();toggleModDone(${m.id})" title="Toggle done">${done ? '✓' : ''}</div>
    <div class="lesson-title">${escapeHtml(m.title)}</div>
    <div class="lesson-badges">
      <span class="lbadge ${m.priority === 'MUST DO' ? 'hands-on' : 'reference'}">${m.priority === 'MUST DO' ? 'Core' : 'Optional'}</span>
    </div>
    <span class="lesson-expand-icon">→</span>
  </div>
</div>`;
    })
    .join('');
  el.innerHTML = `
<div class="back-btn" onclick="showPage('modules')">← All phases</div>
${banner}
<div class="course-hd">
  <div class="course-hd-icon">${ph.icon}</div>
  <div class="course-hd-text">
    <h2>${ph.code} — ${ph.name}</h2>
    <p>${ph.purpose}</p>
  </div>
</div>
<div class="course-prog-banner">
  <div><div class="cpb-pct">${phasePct(pi)}%</div><div class="cpb-lbl">phase</div></div>
  <div class="cpb-bar"><div class="cpb-fill" style="width:${phasePct(pi)}%"></div></div>
  <div class="cpb-done">${doneN} / ${totalN} modules</div>
</div>
<div class="linkedin-box">
  <div class="li-hd">Artifact — LinkedIn draft</div>
  <div class="li-text" id="phase-li-${pi}">${linkedinBlurb(ph, doneN, totalN)}</div>
  <button type="button" class="copy-li-btn" onclick="copyPhaseLi(${pi})">Copy</button>
</div>
<div class="lessons-list">${list}</div>`;
}

function linkedinBlurb(ph, doneN, totalN) {
  return `Completed ${ph.code} — ${ph.name} (${doneN}/${totalN} modules) on my AI Master Tracker path.\nFocus: ${ph.purpose}\n\n#AI #AgenticAI #ContinuousLearning`;
}

function copyPhaseLi(pi) {
  const t = document.getElementById('phase-li-' + pi);
  if (!t) return;
  navigator.clipboard.writeText(t.textContent).then(() => showToast('Copied LinkedIn draft'));
}

function escapeHtml(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

function renderModule(mid) {
  const m = flatModules().find((x) => x.id === mid);
  if (!m) return;
  const ph = PHASES[m.phaseIdx];
  const done = isDone(mid);
  const el = document.getElementById('page-modules');
  const codeHtml = escapeHtml(m.code);
  el.innerHTML = `
<div class="back-btn" onclick="showPage('phase-${m.phaseIdx}')">← ${ph.code}</div>
<div class="course-hd">
  <div class="course-hd-icon">${ph.icon}</div>
  <div class="course-hd-text">
    <h2>Module ${m.num}: ${escapeHtml(m.title)}</h2>
    <p>Tools: ${escapeHtml(m.tools)} · ${m.priority === 'MUST DO' ? 'Core' : 'Optional'}</p>
    <div class="tags-row">
      <span class="ctag">${ph.code}</span>
      <span class="ctag intermediate">${m.priority === 'MUST DO' ? 'Core' : 'Optional depth'}</span>
    </div>
  </div>
</div>
<div class="mod-complete-row">
  <label class="mod-done-label"><input type="checkbox" ${done ? 'checked' : ''} onchange="onModCheck(${mid},this.checked)"> Mark module complete</label>
</div>
<div class="lesson-item expanded" style="margin-top:14px">
  <div class="lesson-body" style="display:block">
      <div class="lesson-body-inner">
      <p class="tab-legend"><strong>How to use these tabs:</strong>
        <strong class="tl-k">Learn</strong> — concepts and explanations on this page (your primary read).
        <strong class="tl-k">Practice</strong> — ordered checklist or “done when…” criteria so you know exactly how to finish the module (separate from reading).
        <strong class="tl-k">Code</strong> — starter commands or snippets to run locally.
        <strong class="tl-k">References</strong> — official docs and deeper articles; optional unless you need detail.</p>
      <div class="ltabs" role="tablist" aria-label="Module content tabs">
        <button type="button" class="ltab active" onclick="switchLTab(this,'llearn-${mid}')" title="Concepts and explanations">Learn</button>
        <button type="button" class="ltab" onclick="switchLTab(this,'lsteps-${mid}')" title="Checklist: what to do to complete this module">Practice</button>
        <button type="button" class="ltab" onclick="switchLTab(this,'lcode-${mid}')" title="Runnable starter code">Code</button>
        <button type="button" class="ltab" onclick="switchLTab(this,'lrefs-${mid}')" title="Official docs and further reading">References</button>
      </div>
      <div id="llearn-${mid}" class="ltab-panel active cb-text">${m.learn}</div>
      <div id="lsteps-${mid}" class="ltab-panel cb-text">${m.steps}</div>
      <div id="lcode-${mid}" class="ltab-panel"><div class="code-block"><button class="copy-code" onclick="copyCode(this)">Copy</button><pre>${codeHtml}</pre></div></div>
      <div id="lrefs-${mid}" class="ltab-panel cb-text">${m.refs}</div>
    </div>
  </div>
</div>`;
}

function switchLTab(btn, panelId) {
  const wrap = btn.parentElement.parentElement;
  wrap.querySelectorAll('.ltab').forEach((b) => b.classList.remove('active'));
  wrap.querySelectorAll('.ltab-panel').forEach((p) => p.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById(panelId).classList.add('active');
}

function toggleModDone(id) {
  onModCheck(id, !isDone(id));
}

function onModCheck(id, checked) {
  setDone(id, checked);
  if (checked) confetti();
  updateSidebarProgress();
  if (currentPage.startsWith('mod-')) renderModule(id);
  else if (currentPage.startsWith('phase-')) renderPhase(parseInt(currentPage.split('-')[1], 10));
  else if (currentPage === 'dashboard') renderDashboard();
  showToast(checked ? 'Module complete' : 'Marked incomplete');
}

function renderCapstone() {
  const el = document.getElementById('page-capstone');
  el.innerHTML = `
<div class="dash-hero"><h1>Capstone projects</h1><p>Three blueprint builds aligned to modules 125–127.</p></div>
<div class="cap-grid">${CAPSTONES.map((c) => `
<div class="cap-card" id="cap-${c.id}">
  <div class="cap-card-hd" onclick="toggleCap('${c.id}')">
    <div>
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
        <span class="cap-num">${c.id.toUpperCase()}</span>
        <span style="font-size:11px;color:var(--muted)">${c.difficulty} · ${c.time}</span>
      </div>
      <div class="cap-title">${c.title}</div>
      <div class="cap-subtitle">${c.subtitle}</div>
      <div class="cap-stack">${c.stack.map((s) => `<span class="cap-tag">${s}</span>`).join('')}</div>
    </div>
    <div class="cap-expand">+</div>
  </div>
  <div class="cap-body">
    <div class="cap-section"><h4>What & why</h4><div class="cb-text"><p>${c.desc}</p><p style="margin-top:6px;color:var(--muted)">${c.why}</p></div></div>
    <div class="cap-section"><h4>Architecture</h4>
      <div class="arch-steps">${c.arch.map((s) => `<div class="arch-step"><div class="as-num">${s.n}</div><div class="as-title">${s.title}</div><div class="as-desc">${s.desc}</div></div>`).join('')}</div>
    </div>
    <div class="cap-section"><h4>Build</h4>${c.build}</div>
    <div class="cap-section"><h4>Similar repos</h4>
      <a href="${c.github}" target="_blank" rel="noopener" class="cert-item cert-free">Search GitHub ↗</a>
    </div>
  </div>
</div>`).join('')}</div>`;
}

function toggleCap(id) {
  document.getElementById('cap-' + id).classList.toggle('open');
}

function renderHackathons() {
  const el = document.getElementById('page-hackathons');
  el.innerHTML = `
<div class="dash-hero"><h1>Hackathons</h1><p>Prize hints, prep modules, templates, and winner patterns.</p></div>
<div class="hack-grid">${HACKATHONS.map((h) => `
<div class="hack-card">
  <div class="hack-card-hd"><div class="hack-icon">${h.icon}</div><div><div class="hack-title">${h.title}</div><div class="hack-org">${h.org}</div></div></div>
  <div class="hack-desc">${h.desc}</div>
  <div class="hack-detail"><strong>Prize pool:</strong> ${h.prize}</div>
  <div class="hack-detail"><strong>Deadline:</strong> ${h.deadline}</div>
  <div class="hack-detail"><strong>Theme:</strong> ${h.theme}</div>
  <div class="hack-detail"><strong>Prep:</strong> ${h.prep}</div>
  <div class="hack-detail"><strong>Quick-start:</strong> ${h.template}</div>
  <div class="hack-detail"><strong>Past winners:</strong> ${h.winners}</div>
  <div class="hack-meta">${h.meta.map((m) => `<span class="hmeta">${m}</span>`).join('')}</div>
  <a href="${h.link}" target="_blank" rel="noopener" class="hack-link">Official site ↗</a>
</div>`).join('')}</div>`;
}

function renderOSS() {
  const el = document.getElementById('page-opensource');
  el.innerHTML = `
<div class="dash-hero"><h1>Open source</h1><p>Contribution-friendly repos by difficulty.</p></div>
<div class="hack-grid">${OPENSOURCE.map((p) => `
<div class="hack-card">
  <div class="hack-card-hd"><div class="hack-icon">${p.icon}</div><div><div class="hack-title">${p.title}</div><div class="hack-org">${p.org} · ${p.diff}</div></div></div>
  <div class="hack-desc">${p.desc}</div>
  <div class="hack-meta">${p.tags.map((t) => `<span class="hmeta">${t}</span>`).join('')}</div>
  <a href="${p.link}" target="_blank" rel="noopener" class="hack-link">Repository ↗</a>
</div>`).join('')}</div>`;
}

function renderYC() {
  const el = document.getElementById('page-yc');
  el.innerHTML = `
<div class="dash-hero"><h1>YC-style project ideas</h1><p>Problem → AI solution → stack from this curriculum → MVP scope.</p></div>
<div class="cap-grid">${YC_IDEAS.map((y, i) => `
<div class="hack-card" style="text-align:left">
  <div class="hack-title" style="margin-bottom:8px">${i + 1}. ${y.title}</div>
  <div class="hack-detail"><strong>Problem:</strong> ${y.problem}</div>
  <div class="hack-detail"><strong>Solution:</strong> ${y.solution}</div>
  <div class="hack-detail"><strong>Stack:</strong> ${y.stack}</div>
  <div class="hack-detail"><strong>Market (rough):</strong> ${y.market}</div>
  <div class="hack-detail"><strong>2-week MVP:</strong> ${y.mvp}</div>
</div>`).join('')}</div>`;
}

function certState(id) {
  return state.certs[id] || { status: 'not_started', exam: '' };
}

function certCounts() {
  let passed = 0;
  let inProgress = 0;
  CERT_DEFS.forEach((c) => {
    const st = certState(c.id).status;
    if (st === 'passed') passed++;
    else if (st === 'in_progress') inProgress++;
  });
  const total = CERT_DEFS.length;
  return { total, passed, inProgress, notStarted: total - passed - inProgress };
}

function setCertField(id, field, value) {
  if (!state.certs[id]) state.certs[id] = { status: 'not_started', exam: '' };
  state.certs[id][field] = value;
  saveState(state);
  if (currentPage === 'dashboard') renderDashboard();
}

function renderCertTracker() {
  const el = document.getElementById('page-certs');
  const pc = certPriceCounts();
  const list = certDefsFiltered();
  const f = certTrackerUi.price;
  const priceCls = (p) => (p === 'free' ? 'cert-price-free' : p === 'paid' ? 'cert-price-paid' : 'cert-price-mixed');
  const kindCls = (k) => (k === 'credential' ? 'cert-kind-credential' : 'cert-kind-learning');
  const kindLabel = (k) => (k === 'credential' ? 'Exam / cert' : 'Learning');
  el.innerHTML = `
<div class="dash-hero"><h1>Certifications & AI learning</h1><p>Vendor exams, free courses, and prep paths from major AI ecosystem players. Filter by cost; progress still saves locally in your JSON.</p></div>
<div class="cert-toolbar">
  <span class="cert-filter-label">Cost</span>
  <button type="button" class="cert-filter-btn${f === 'all' ? ' active' : ''}" onclick="setCertPriceFilter('all')">All (${CERT_DEFS.length})</button>
  <button type="button" class="cert-filter-btn${f === 'free' ? ' active' : ''}" onclick="setCertPriceFilter('free')">Free (${pc.free})</button>
  <button type="button" class="cert-filter-btn${f === 'mixed' ? ' active' : ''}" onclick="setCertPriceFilter('mixed')">Mixed (${pc.mixed})</button>
  <button type="button" class="cert-filter-btn${f === 'paid' ? ' active' : ''}" onclick="setCertPriceFilter('paid')">Paid (${pc.paid})</button>
  <span class="cert-toolbar-sep"></span>
  <label class="cert-search-wrap"><span class="cert-filter-label">Search</span>
    <input type="search" id="cert-search-q" class="cert-search-input" placeholder="Provider, topic…" autocomplete="off" value="${escapeAttr(certTrackerUi.q)}" oninput="onCertSearchInput(this.value)" />
  </label>
</div>
<p class="cert-filter-meta">Showing <strong>${list.length}</strong> of ${CERT_DEFS.length} · <span class="cert-price-tag ${priceCls('free')}">Free</span> training is $0; <span class="cert-price-tag ${priceCls('mixed')}">Mixed</span> = free prep with a paid exam or optional paid certificate; <span class="cert-price-tag ${priceCls('paid')}">Paid</span> = exam or paid program.</p>
<div class="cert-table">${
    list.length === 0
      ? '<p class="cert-empty">No entries match these filters. Try <strong>All</strong> or clear search.</p>'
      : list
          .map((c) => {
            const st = certState(c.id);
            return `
<div class="cert-track-row" data-cert-price="${c.price}">
  <div class="cert-track-main">
    <div class="cert-track-tags">
      <span class="cert-price-tag ${priceCls(c.price)}">${c.price === 'free' ? 'Free' : c.price === 'paid' ? 'Paid' : 'Mixed'}</span>
      <span class="cert-kind-tag ${kindCls(c.kind)}">${kindLabel(c.kind)}</span>
      <span class="cert-provider-tag">${escapeHtml(c.provider)}</span>
    </div>
    <div class="cert-track-name"><a href="${c.url}" target="_blank" rel="noopener" class="ext-link">${escapeHtml(c.name)} ↗</a></div>
    ${c.note ? `<div class="cert-track-note">${escapeHtml(c.note)}</div>` : ''}
    <div class="cert-track-study">Curriculum map: ${escapeHtml(c.studyPhases)}</div>
  </div>
  <div class="cert-track-controls">
    <select onchange="setCertField('${c.id}','status',this.value)">
      <option value="not_started" ${st.status === 'not_started' ? 'selected' : ''}>Not started</option>
      <option value="in_progress" ${st.status === 'in_progress' ? 'selected' : ''}>In progress</option>
      <option value="passed" ${st.status === 'passed' ? 'selected' : ''}>Done / passed</option>
    </select>
    <input type="date" value="${st.exam || ''}" onchange="setCertField('${c.id}','exam',this.value)" title="Target date (exam or finish)" />
    <a class="cal-link" href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=${encodeURIComponent((c.kind === 'credential' ? 'Exam: ' : 'Finish: ') + c.name)}" target="_blank" rel="noopener">Calendar ↗</a>
  </div>
</div>`;
          })
          .join('')
  }</div>`;
}

function renderCareer() {
  const el = document.getElementById('page-career');
  const pct = globalPct();
  const bullets = PHASES.filter((_, pi) => phasePct(pi) === 100).map((ph) => `<li>Delivered ${ph.code} — ${ph.name}: production-style artifacts and hands-on modules.</li>`);
  const partial = PHASES.filter((_, pi) => {
    const p = phasePct(pi);
    return p > 0 && p < 100;
  }).map((ph) => `<li>In progress: ${ph.code} — ${ph.name}</li>`);
  const skills = PHASES.filter((_, pi) => phasePct(pi) >= 50).map((ph) => ph.name);
  const pf = (state.portfolio || []).join('\n');
  el.innerHTML = `
<div class="dash-hero"><h1>Career dashboard</h1><p>Readiness score from module completion. Copy bullets and LinkedIn snippets below.</p></div>
<div class="stats-grid" style="margin-bottom:20px">
  <div class="stat-card sc-purple"><div class="sc-label">Consultant readiness</div><div class="sc-val">${pct}%</div><div class="sc-sub">based on ${doneCount()}/${totalMods()} modules</div></div>
</div>
<div class="section-hd">Skills strong (≥50% within phase)</div>
<div class="cb-text" style="margin-bottom:16px">${skills.length ? '<ul>' + skills.map((s) => '<li>' + escapeHtml(s) + '</li>').join('') + '</ul>' : '<p>Complete half of any phase to populate this list.</p>'}</div>
<div class="section-hd">Resume bullet bank (100% phases)</div>
<div class="cb-text"><ul>${bullets.length ? bullets.join('') : '<li>Finish entire phases to unlock bullets.</li>'}</ul></div>
<div class="section-hd">In-progress lines</div>
<div class="cb-text"><ul>${partial.length ? partial.join('') : '<li>No partial phases yet.</li>'}</ul></div>
<div class="linkedin-box">
  <div class="li-hd">LinkedIn post composer</div>
  <textarea id="li-composer" class="career-textarea">${linkedinComposer()}</textarea>
  <button type="button" class="copy-li-btn" onclick="copyComposer()">Copy</button>
</div>
<div class="section-hd">Portfolio links (one per line, saved locally)</div>
<textarea id="portfolio-area" class="career-textarea" onchange="savePortfolio(this.value)">${escapeHtml(pf)}</textarea>`;
}

function linkedinComposer() {
  const done = doneCount();
  const highlights = PHASES.filter((_, pi) => phaseDoneCount(pi) > 0)
    .map((ph) => ph.code)
    .slice(0, 6)
    .join(', ');
  return `Update: completed ${done} modules on my AI Master Tracker (20-phase agentic AI path).\nPhases in motion: ${highlights || 'starting P0'}.\n\n#AI #AgenticAI #MCP #Consulting`;
}

function copyComposer() {
  const t = document.getElementById('li-composer');
  if (!t) return;
  navigator.clipboard.writeText(t.value).then(() => showToast('Copied'));
}

function savePortfolio(text) {
  state.portfolio = text
    .split('\n')
    .map((s) => s.trim())
    .filter(Boolean);
  saveState(state);
}

function toggleThemeDD() {
  document.getElementById('themeDD').classList.toggle('open');
}
document.addEventListener('click', (e) => {
  if (!e.target.closest('.theme-wrap')) document.getElementById('themeDD').classList.remove('open');
});
function setTheme(t) {
  document.documentElement.setAttribute('data-theme', t);
  localStorage.setItem('ai_theme', t);
  syncThemeOpts();
  showToast('Theme: ' + t);
}
function syncThemeOpts() {
  const t = document.documentElement.getAttribute('data-theme') || 'dark';
  document.querySelectorAll('.theme-opt').forEach((o) => {
    o.classList.toggle('active', o.dataset.theme === t);
  });
}
const savedTheme = localStorage.getItem('ai_theme');
if (savedTheme) document.documentElement.setAttribute('data-theme', savedTheme);

function exportCSV() {
  const rows = [['ModuleNum', 'Done']];
  flatModules().forEach((m) => {
    rows.push([m.num, isDone(m.id) ? 'Yes' : 'No']);
  });
  downloadText('ai_master_progress.csv', rows.map((r) => r.join(',')).join('\n'), 'text/csv');
  showToast('CSV exported');
}

function importCSV(e) {
  const f = e.target.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = (ev) => {
    let n = 0;
    ev.target.result.split('\n').slice(1).forEach((line) => {
      const p = line.trim().split(',');
      if (p.length >= 2 && p[1].trim().toLowerCase() === 'yes') {
        const num = parseInt(p[0], 10);
        const mod = flatModules().find((m) => m.num === num);
        if (mod) {
          state.modules[modKey(mod.id)] = true;
          n++;
        }
      }
    });
    saveState(state);
    showToast('Imported ' + n + ' modules');
    refreshView();
  };
  r.readAsText(f);
  e.target.value = '';
}

function exportJSON() {
  const payload = {
    version: 1,
    exportedAt: new Date().toISOString(),
    modules: state.modules,
    certs: state.certs,
    portfolio: state.portfolio,
  };
  downloadText('ai_master_tracker_state.json', JSON.stringify(payload, null, 2), 'application/json');
  showToast('JSON exported (flat file backup)');
}

function importJSON(e) {
  const f = e.target.files[0];
  if (!f) return;
  const r = new FileReader();
  r.onload = (ev) => {
    try {
      const data = JSON.parse(ev.target.result);
      if (data.modules) state.modules = data.modules;
      if (data.certs) state.certs = data.certs;
      if (data.portfolio) state.portfolio = data.portfolio;
      saveState(state);
      showToast('JSON imported');
      refreshView();
    } catch {
      showToast('Invalid JSON');
    }
  };
  r.readAsText(f);
  e.target.value = '';
}

function downloadText(name, text, mime) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], { type: mime }));
  a.download = name;
  a.click();
}

function refreshView() {
  updateSidebarProgress();
  if (currentPage === 'dashboard') renderDashboard();
  else if (currentPage === 'modules') renderAllPhases();
  else if (currentPage.startsWith('phase-')) renderPhase(parseInt(currentPage.split('-')[1], 10));
  else if (currentPage.startsWith('mod-')) renderModule(parseInt(currentPage.split('-')[1], 10));
  else if (currentPage === 'career') renderCareer();
  else if (currentPage === 'certs') renderCertTracker();
  else if (currentPage === 'coverage') renderCoverage();
}

function confirmReset() {
  if (confirm('Reset all local progress, certs, and portfolio notes? Export JSON first if needed.')) {
    state = defaultState();
    saveState(state);
    updateSidebarProgress();
    refreshView();
    showToast('Reset complete');
  }
}

function copyCode(btn) {
  const pre = btn.parentElement.querySelector('pre');
  navigator.clipboard.writeText(pre.innerText).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => (btn.textContent = 'Copy'), 2000);
  });
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2200);
}

function confetti() {
  const colors = ['#c084fc', '#4ade80', '#fb923c', '#60a5fa', '#fbbf24'];
  for (let i = 0; i < 6; i++) {
    const c = document.createElement('div');
    c.className = 'confetti-p';
    c.style.cssText = `left:${Math.random() * 100}vw;top:60vh;background:${colors[Math.floor(Math.random() * colors.length)]}`;
    document.body.appendChild(c);
    setTimeout(() => c.remove(), 1200);
  }
}

buildSidebar();
updateSidebarProgress();
renderDashboard();
syncThemeOpts();
