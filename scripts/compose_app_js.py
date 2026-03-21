#!/usr/bin/env python3
# Manish.AI — Build assets/js/app.js from platform_logic.js + CSV bootstrap header.
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "platform_logic.js"
OUT = ROOT / "assets" / "js" / "app.js"

HEAD = r"""/* AI Master Tracker — loads data/curriculum.json + data/catalog/*.csv. Manish.AI */
let CURRICULUM = null;
let PHASES = [];
let COVERAGE = { modules: [], blueprint_crosswalk: [], legend: {} };
const KEY = 'ai_master_tracker_v1';

let CERT_DEFS = [];
let NAV_PAGES = [];
let CAPSTONES = [];
let HACKATHONS = [];
let OPENSOURCE = [];
let YC_IDEAS = [];

function parseCsv(text) {
  const rows = [];
  let field = '';
  let row = [];
  let inQuotes = false;
  const pushField = () => { row.push(field); field = ''; };
  const pushRow = () => { rows.push(row); row = []; };
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (inQuotes) {
      if (c === '"') {
        if (text[i + 1] === '"') { field += '"'; i++; continue; }
        inQuotes = false;
        continue;
      }
      field += c;
      continue;
    }
    if (c === '"') { inQuotes = true; continue; }
    if (c === ',') { pushField(); continue; }
    if (c === '\r') continue;
    if (c === '\n') { pushField(); pushRow(); continue; }
    field += c;
  }
  pushField();
  if (row.length && row.some((x) => x !== '')) pushRow();
  if (!rows.length) return [];
  const headers = rows[0].map((h) => h.trim());
  const out = [];
  for (let r = 1; r < rows.length; r++) {
    const o = {};
    headers.forEach((h, j) => { o[h] = (rows[r][j] ?? '').trim(); });
    out.push(o);
  }
  return out;
}

function rowsToCerts(rows) {
  return rows.map((r) => ({
    id: r.id,
    provider: r.provider,
    name: r.name,
    url: r.url,
    price: r.price,
    kind: r.kind,
    studyPhases: r.studyPhases,
    note: r.note || '',
  }));
}

function rowsToNav(rows) {
  return rows
    .slice()
    .sort((a, b) => parseInt(a.sort_order, 10) - parseInt(b.sort_order, 10))
    .map((r) => ({ id: r.page_id, label: r.label, icon: r.icon }));
}

function parseMetaCell(s) {
  if (!s) return [];
  const m = s.match(/'([^']*)'/g);
  if (!m) return [s.trim()].filter(Boolean);
  return m.map((x) => x.slice(1, -1));
}

function rowsToHackathons(rows) {
  return rows.map((r) => ({
    icon: r.icon,
    title: r.title,
    org: r.org,
    prize: r.prize,
    deadline: r.deadline,
    theme: r.theme,
    prep: r.prep,
    template: r.template,
    winners: r.winners,
    desc: r.desc,
    meta: parseMetaCell(r.meta),
    link: r.link,
  }));
}

function rowsToOSS(rows) {
  return rows.map((r) => ({
    icon: r.icon,
    title: r.title,
    org: r.org,
    diff: r.diff,
    desc: r.desc,
    tags: (r.tags || '').split(';').filter(Boolean),
    link: r.link,
  }));
}

function rowsToYc(rows) {
  return rows.map((r) => ({
    title: r.title,
    problem: r.problem,
    solution: r.solution,
    stack: r.stack,
    market: r.market,
    mvp: r.mvp,
  }));
}

function mergeCapstoneRows(capRows, stepRows, detail) {
  const stepsBy = {};
  stepRows.forEach((s) => {
    if (!stepsBy[s.capstone_id]) stepsBy[s.capstone_id] = [];
    stepsBy[s.capstone_id].push({ n: s.step_n, title: s.title, desc: s.description });
  });
  return capRows.map((c) => ({
    id: c.id,
    title: c.title,
    subtitle: c.subtitle,
    stack: (c.stack || '').split(';').filter(Boolean),
    difficulty: c.difficulty,
    time: c.time,
    desc: c.desc,
    why: c.why,
    arch: stepsBy[c.id] || [],
    build: (detail[c.id] && detail[c.id].build) || '',
    github: c.github,
  }));
}

async function fetchText(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error(path + ' HTTP ' + r.status);
  return r.text();
}

async function fetchJson(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error(path + ' HTTP ' + r.status);
  return r.json();
}

async function loadAllData() {
  CURRICULUM = await fetchJson('data/curriculum.json');
  PHASES = CURRICULUM.phases;
  try {
    COVERAGE = await fetchJson('data/coverage.json');
  } catch (e) {
    console.warn('coverage.json', e);
  }
  CERT_DEFS = rowsToCerts(parseCsv(await fetchText('data/catalog/certs.csv')));
  NAV_PAGES = rowsToNav(parseCsv(await fetchText('data/catalog/nav_pages.csv')));
  HACKATHONS = rowsToHackathons(parseCsv(await fetchText('data/catalog/hackathons.csv')));
  OPENSOURCE = rowsToOSS(parseCsv(await fetchText('data/catalog/opensource.csv')));
  YC_IDEAS = rowsToYc(parseCsv(await fetchText('data/catalog/yc_ideas.csv')));
  const capDetail = await fetchJson('data/catalog/capstones_detail.json');
  CAPSTONES = mergeCapstoneRows(
    parseCsv(await fetchText('data/catalog/capstones.csv')),
    parseCsv(await fetchText('data/catalog/capstone_steps.csv')),
    capDetail,
  );
}

function exportModulesProgressCsv() {
  const lines = ['module_num,done,notes'];
  flatModules().forEach((m) => {
    lines.push(`${m.num},${isDone(m.id) ? 'true' : 'false'},`);
  });
  downloadText('modules_progress.csv', lines.join('\n'), 'text/csv;charset=utf-8');
  showToast('Exported modules_progress.csv');
}

function importModulesProgressCsv(ev) {
  const f = ev.target.files && ev.target.files[0];
  if (!f) return;
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const rows = parseCsv(reader.result);
      rows.forEach((r) => {
        const n = parseInt(r.module_num, 10);
        if (!n || Number.isNaN(n)) return;
        const id = n - 1;
        if (r.done === 'true' || r.done === '1' || r.done === 'yes') setDone(id, true);
        else setDone(id, false);
      });
      flatModuleCache = null;
      updateSidebarProgress();
      refreshView();
      showToast('Imported module progress from CSV');
    } catch (e) {
      alert('CSV import failed: ' + e);
    }
    ev.target.value = '';
  };
  reader.readAsText(f, 'UTF-8');
}

"""


def main() -> None:
    src = SRC.read_text(encoding="utf-8")
    core_start = src.index("let flatModuleCache")
    core_end = src.index("const NAV_PAGES")
    core = src[core_start:core_end]
    core = core.replace("let state = loadState();\n\n", "let state;\n\n")
    tail = src[src.index("let currentPage = 'dashboard';") :]
    # drop 2-arg downloadText if present before exportCoverage
    lines = tail.splitlines(keepends=True)
    out_lines = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("function downloadText(name, text) {"):
            depth = 0
            while i < len(lines):
                depth += lines[i].count("{") - lines[i].count("}")
                i += 1
                if depth <= 0:
                    break
            continue
        out_lines.append(lines[i])
        i += 1
    tail = "".join(out_lines)
    tail = tail.replace(
        "function downloadText(name, text, mime) {\n  const a = document.createElement('a');\n  a.href = URL.createObjectURL(new Blob([text], { type: mime }));",
        "function downloadText(name, text, mime) {\n  const a = document.createElement('a');\n  const t = mime || 'text/csv;charset=utf-8';\n  a.href = URL.createObjectURL(new Blob([text], { type: t }));",
    )
    old_boot = """buildSidebar();
updateSidebarProgress();
renderDashboard();
syncThemeOpts();
"""
    new_boot = """async function boot() {
  const loadEl = document.getElementById('app-loading');
  try {
    await loadAllData();
    state = loadState();
    flatModuleCache = null;
    if (loadEl) loadEl.style.display = 'none';
    buildSidebar();
    updateSidebarProgress();
    renderDashboard();
    syncThemeOpts();
  } catch (e) {
    console.error(e);
    if (loadEl) {
      loadEl.textContent =
        'Could not load data. Run: python3 build_curriculum.py then serve the repo root (python3 -m http.server 8000) and open http://localhost:8000/index.html — ' +
        e;
    }
  }
}
boot();
"""
    if old_boot not in tail:
        raise SystemExit("expected sync boot block missing")
    tail = tail.replace(old_boot, new_boot)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(HEAD + core + tail, encoding="utf-8")
    print("Wrote", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
