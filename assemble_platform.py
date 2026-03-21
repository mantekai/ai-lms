#!/usr/bin/env python3
"""Assemble single-file AI Master Tracker HTML. Manish.AI"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

EXTRA_CSS = """
[data-theme="sunset"]{--bg:#1a0f14;--surf:#24161c;--surf2:#2e1f28;--surf3:#3d2a35;--brd:#4a3542;--text:#fdf2f8;--muted:#b8a5af;--muted2:#7d6a72;--acc:#fb7185;--acc2:#f43f5e;--acc3:#e11d48;--green:#4ade80;--orange:#fb923c;--blue:#93c5fd;--yellow:#fde047;--red:#fca5a5;--local:#34d399;--localBg:#0f1f18;--gold:#fde047;--sidebar-w:252px}
.mc-12::before{background:linear-gradient(90deg,#f472b6,#ec4899)}
.ltabs{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap;border-bottom:1px solid var(--brd);padding-bottom:8px}
.ltab{font-size:11px;padding:6px 12px;border-radius:6px;border:1px solid var(--brd);background:var(--surf2);color:var(--muted);cursor:pointer}
.ltab:hover{border-color:var(--acc3);color:var(--text)}
.ltab.active{background:var(--acc3);border-color:var(--acc3);color:#fff}
.ltab-panel{display:none;padding-top:4px}
.ltab-panel.active{display:block}
.tab-legend{font-size:11.5px;color:var(--muted);line-height:1.6;margin:0 0 12px;padding:10px 12px;background:var(--surf2);border:1px solid var(--brd);border-radius:8px}
.tab-legend .tl-k{color:var(--acc);font-weight:600}
.refs-intro{font-size:12px;color:var(--muted);line-height:1.55;margin:0 0 10px}
.refs-list{margin:0;padding-left:1.1rem}
.refs-list li{margin-bottom:6px}
.mod-complete-row{margin-bottom:12px;padding:10px 14px;background:var(--surf);border:1px solid var(--brd);border-radius:8px}
.mod-done-label{display:flex;align-items:center;gap:8px;font-size:12px;cursor:pointer}
.mod-done-label input{width:16px;height:16px;accent-color:var(--acc)}
.gate-banner{background:var(--surf2);border:1px solid var(--yellow);color:var(--yellow);padding:12px 14px;border-radius:8px;margin-bottom:18px;font-size:12px;line-height:1.5}
.hack-detail{font-size:11px;color:var(--muted);margin-bottom:6px;line-height:1.45}
.cert-table{display:flex;flex-direction:column;gap:12px}
.cert-toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:10px;padding:12px 14px;background:var(--surf2);border:1px solid var(--brd);border-radius:10px}
.cert-filter-label{font-size:11px;font-weight:600;color:var(--muted);margin-right:2px}
.cert-filter-btn{font-size:11px;padding:6px 12px;border-radius:7px;border:1px solid var(--brd);background:var(--surf);color:var(--muted);cursor:pointer;transition:all .15s}
.cert-filter-btn:hover{border-color:var(--acc);color:var(--text)}
.cert-filter-btn.active{background:var(--acc3);border-color:var(--acc3);color:#fff}
.cert-toolbar-sep{flex:1;min-width:8px}
.cert-search-wrap{display:inline-flex;align-items:center;gap:6px;flex-wrap:wrap}
.cert-search-input{font-size:11px;padding:6px 10px;border-radius:6px;border:1px solid var(--brd);background:var(--surf);color:var(--text);min-width:160px;max-width:280px}
.cert-filter-meta{font-size:11px;color:var(--muted);line-height:1.55;margin:0 0 12px}
.cert-empty{font-size:12px;color:var(--muted);padding:16px;text-align:center}
.cert-track-row{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start;padding:14px 16px;background:var(--surf);border:1px solid var(--brd);border-radius:10px;justify-content:space-between}
.cert-track-main{flex:1;min-width:220px}
.cert-track-tags{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:8px}
.cert-price-tag{font-size:9px;font-weight:700;padding:3px 8px;border-radius:99px;text-transform:uppercase;letter-spacing:.04em}
.cert-price-free{background:rgba(52,211,153,.14);color:var(--local);border:1px solid var(--local)}
.cert-price-paid{background:rgba(253,224,71,.12);color:var(--gold);border:1px solid rgba(253,224,71,.45)}
.cert-price-mixed{background:rgba(251,146,60,.12);color:var(--orange);border:1px solid var(--orange)}
.cert-kind-tag{font-size:9px;font-weight:700;padding:3px 8px;border-radius:99px;letter-spacing:.03em;text-transform:uppercase}
.cert-kind-credential{background:rgba(147,197,253,.12);color:var(--blue);border:1px solid var(--blue)}
.cert-kind-learning{background:var(--surf3);color:var(--muted2);border:1px solid var(--brd)}
.cert-provider-tag{font-size:10px;color:var(--muted2);padding:2px 0}
.cert-track-name{font-size:13px;font-weight:600}
.cert-track-note{font-size:11px;color:var(--muted);margin-top:4px;line-height:1.45}
.cert-track-study{font-size:11px;color:var(--muted);margin-top:4px}
.cert-track-controls{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.cert-track-controls select,.cert-track-controls input{font-size:11px;padding:5px 8px;border-radius:6px;border:1px solid var(--brd);background:var(--surf2);color:var(--text)}
.cal-link{font-size:11px;color:var(--blue)}
.career-textarea{width:100%;min-height:120px;margin-top:8px;padding:10px 12px;border-radius:8px;border:1px solid var(--brd);background:var(--surf2);color:var(--text);font-size:12px;font-family:inherit;resize:vertical}
.term-list dt{font-size:12.5px;font-weight:700;color:var(--acc);margin-top:10px;margin-bottom:3px}
.term-list dd{font-size:12px;line-height:1.65;color:var(--text);margin-left:0;margin-bottom:6px;padding-left:12px;border-left:2px solid var(--surf3)}
.coverage-toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:14px}
.coverage-toolbar input,.coverage-toolbar select{font-size:11px;padding:6px 10px;border-radius:6px;border:1px solid var(--brd);background:var(--surf2);color:var(--text)}
.cov-table-wrap{overflow-x:auto;border:1px solid var(--brd);border-radius:10px;background:var(--surf)}
table.cov-table{width:100%;border-collapse:collapse;font-size:11.5px}
.cov-table th,.cov-table td{padding:8px 10px;text-align:left;border-bottom:1px solid var(--brd);vertical-align:top}
.cov-table th{background:var(--surf2);color:var(--muted);font-weight:700;text-transform:uppercase;font-size:10px;letter-spacing:.04em}
.cov-table tr:hover td{background:var(--surf2)}
.badge-yes{color:var(--green);font-weight:600}
.badge-partial{color:var(--yellow);font-weight:600}
.badge-no{color:var(--muted)}
.crosswalk-card{background:var(--surf);border:1px solid var(--brd);border-radius:10px;padding:12px 14px;margin-bottom:10px}
.crosswalk-card .cx-topic{font-weight:600;font-size:12.5px;margin-bottom:4px}
.crosswalk-card .cx-meta{font-size:11px;color:var(--muted);line-height:1.5}
"""

# Injected on re-assemble when main EXTRA_CSS was skipped (already present).
CSS_TERM_COVERAGE_ONLY = """
.term-list dt{font-size:12.5px;font-weight:700;color:var(--acc);margin-top:10px;margin-bottom:3px}
.term-list dd{font-size:12px;line-height:1.65;color:var(--text);margin-left:0;margin-bottom:6px;padding-left:12px;border-left:2px solid var(--surf3)}
.coverage-toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:14px}
.coverage-toolbar input,.coverage-toolbar select{font-size:11px;padding:6px 10px;border-radius:6px;border:1px solid var(--brd);background:var(--surf2);color:var(--text)}
.cov-table-wrap{overflow-x:auto;border:1px solid var(--brd);border-radius:10px;background:var(--surf)}
table.cov-table{width:100%;border-collapse:collapse;font-size:11.5px}
.cov-table th,.cov-table td{padding:8px 10px;text-align:left;border-bottom:1px solid var(--brd);vertical-align:top}
.cov-table th{background:var(--surf2);color:var(--muted);font-weight:700;text-transform:uppercase;font-size:10px;letter-spacing:.04em}
.cov-table tr:hover td{background:var(--surf2)}
.badge-yes{color:var(--green);font-weight:600}
.badge-partial{color:var(--yellow);font-weight:600}
.badge-no{color:var(--muted)}
.crosswalk-card{background:var(--surf);border:1px solid var(--brd);border-radius:10px;padding:12px 14px;margin-bottom:10px}
.crosswalk-card .cx-topic{font-weight:600;font-size:12.5px;margin-bottom:4px}
.crosswalk-card .cx-meta{font-size:11px;color:var(--muted);line-height:1.5}
"""

TAB_LEGEND_REFS_CSS = """
.tab-legend{font-size:11.5px;color:var(--muted);line-height:1.6;margin:0 0 12px;padding:10px 12px;background:var(--surf2);border:1px solid var(--brd);border-radius:8px}
.tab-legend .tl-k{color:var(--acc);font-weight:600}
.refs-intro{font-size:12px;color:var(--muted);line-height:1.55;margin:0 0 10px}
.refs-list{margin:0;padding-left:1.1rem}
.refs-list li{margin-bottom:6px}
"""


def main():
    path = ROOT / "ai-consultant-roadmap.html"
    text = path.read_text(encoding="utf-8")

    if ".ltabs{" not in text:
        text = text.replace("</style>", EXTRA_CSS + "\n</style>", 1)
    elif ".term-list dt" not in text:
        text = text.replace("</style>", CSS_TERM_COVERAGE_ONLY + "\n</style>", 1)
    if ".tab-legend{" not in text:
        text = text.replace("</style>", TAB_LEGEND_REFS_CSS + "\n</style>", 1)
    if "AI Mastery OS — Manish Taneja" in text:
        text = text.replace(
            "<title>AI Mastery OS — Manish Taneja</title>",
            "<title>AI Master Tracker — Learning OS</title>",
            1,
        )

    old_sb = """    <div class="sb-actions">
      <button class="sb-btn" onclick="exportCSV()">⬇ Export</button>
      <label class="sb-btn" style="cursor:pointer">⬆ Import<input type="file" accept=".csv" style="display:none" onchange="importCSV(event)"></label>
      <button class="sb-btn danger" onclick="confirmReset()">↺ Reset</button>
    </div>
    v8.0 · 12 phases · Zero 13s 🍀"""

    new_sb = """    <div class="sb-actions">
      <button class="sb-btn" onclick="exportJSON()">⬇ JSON</button>
      <label class="sb-btn" style="cursor:pointer">⬆ JSON<input type="file" accept=".json,application/json" style="display:none" onchange="importJSON(event)"></label>
      <button class="sb-btn" onclick="exportCSV()">⬇ CSV</button>
      <label class="sb-btn" style="cursor:pointer">⬆ CSV<input type="file" accept=".csv,text/csv" style="display:none" onchange="importCSV(event)"></label>
      <button class="sb-btn danger" onclick="confirmReset()">↺ Reset</button>
    </div>
    v9 · 133 modules · 20 phases"""

    if old_sb in text:
        text = text.replace(old_sb, new_sb, 1)

    old_theme = """        <div class="theme-dropdown" id="themeDD">
          <div class="theme-opt" onclick="setTheme('dark')">🌙 Dark</div>
          <div class="theme-opt" onclick="setTheme('light')">☀️ Light</div>
          <div class="theme-opt" onclick="setTheme('ocean')">🌊 Ocean</div>
          <div class="theme-opt" onclick="setTheme('mint')">🌿 Mint</div>
        </div>"""

    new_theme = """        <div class="theme-dropdown" id="themeDD">
          <div class="theme-opt" data-theme="dark" onclick="setTheme('dark')">🌙 Dark</div>
          <div class="theme-opt" data-theme="light" onclick="setTheme('light')">☀️ Light</div>
          <div class="theme-opt" data-theme="ocean" onclick="setTheme('ocean')">🌊 Ocean</div>
          <div class="theme-opt" data-theme="mint" onclick="setTheme('mint')">🌿 Mint</div>
          <div class="theme-opt" data-theme="sunset" onclick="setTheme('sunset')">🌅 Sunset</div>
        </div>"""

    if old_theme in text:
        text = text.replace(old_theme, new_theme, 1)

    old_top = """      <button class="topbar-action" onclick="exportCSV()">⬇ Export CSV</button>
      <label class="topbar-action" style="cursor:pointer">⬆ Import<input type="file" accept=".csv" style="display:none" onchange="importCSV(event)"></label>"""

    new_top = """      <button class="topbar-action" onclick="exportJSON()">⬇ JSON</button>
      <label class="topbar-action" style="cursor:pointer">⬆ JSON<input type="file" accept=".json,application/json" style="display:none" onchange="importJSON(event)"></label>
      <button class="topbar-action" onclick="exportCSV()">⬇ CSV</button>
      <label class="topbar-action" style="cursor:pointer">⬆ CSV<input type="file" accept=".csv,text/csv" style="display:none" onchange="importCSV(event)"></label>"""

    if old_top in text:
        text = text.replace(old_top, new_top, 1)

    if 'id="page-yc"' not in text:
        text = text.replace(
            """    <div id="page-opensource" class="page"></div>
  </main>""",
            """    <div id="page-opensource" class="page"></div>
    <div id="page-yc" class="page"></div>
    <div id="page-certs" class="page"></div>
    <div id="page-career" class="page"></div>
  </main>""",
            1,
        )
    if 'id="page-coverage"' not in text:
        text = text.replace(
            '    <div id="page-career" class="page"></div>\n  </main>',
            '    <div id="page-coverage" class="page"></div>\n    <div id="page-career" class="page"></div>\n  </main>',
            1,
        )

    text = text.replace(
        '<div class="topbar-title" id="topbar-title">AI Mastery OS</div>',
        '<div class="topbar-title" id="topbar-title">AI Master Tracker</div>',
        1,
    )
    text = text.replace(
        '<div class="sb-logo-text">AI Mastery OS</div>',
        '<div class="sb-logo-text">AI Master Tracker</div>',
        1,
    )

    curriculum_path = ROOT / "data" / "curriculum.json"
    if not curriculum_path.exists():
        curriculum_path = ROOT / "curriculum.embed.json"
    json_raw = curriculum_path.read_text(encoding="utf-8")
    cov_path = ROOT / "data" / "coverage.json"
    if not cov_path.exists():
        cov_path = ROOT / "coverage.embed.json"
    cov_raw = (
        cov_path.read_text(encoding="utf-8")
        if cov_path.exists()
        else '{"version":1,"modules":[],"blueprint_crosswalk":[],"legend":{}}'
    )
    logic = (ROOT / "platform_logic.js").read_text(encoding="utf-8")
    embed = (
        f'<script type="application/json" id="COVERAGE_JSON">{cov_raw}</script>\n'
        f'<script type="application/json" id="CURRICULUM_JSON">{json_raw}</script>\n'
        f"<script>\n{logic}\n</script>"
    )

    toast_marker = '<div class="toast" id="toast"></div>'
    if toast_marker in text:
        ix = text.index(toast_marker) + len(toast_marker)
        while ix < len(text) and text[ix] in "\n\r\t ":
            ix += 1
        s0 = ix
        body_end = text.index("</body>")
        last_sc = text.rindex("</script>", s0, body_end)
        chunk_end = last_sc + len("</script>")
        text = text[:s0] + "\n" + embed + "\n" + text[chunk_end:]
    elif 'id="CURRICULUM_JSON"' in text:
        i = text.index('<script type="application/json" id="CURRICULUM_JSON">')
        j = text.index("<script>", text.index("</script>", i) + 1)
        m = text.index("</script>", j) + len("</script>")
        text = text[:i] + embed + text[m:]
    else:
        script_start = text.index("<script>")
        script_end = text.rindex("</script>") + len("</script>")
        text = text[:script_start] + embed + text[script_end:]

    banner = "<!-- AI Master Tracker: 133-module curriculum shell, tabs, JSON/CSV sync. Manish.AI -->\n"
    if "<!-- AI Master Tracker:" not in text[:500]:
        text = text.replace("<!DOCTYPE html>\n", "<!DOCTYPE html>\n" + banner, 1)

    path.write_text(text, encoding="utf-8")
    print("Wrote", path, "bytes:", path.stat().st_size)


if __name__ == "__main__":
    main()
