# Validates reconstructed content layout. Manish.AI
import csv
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestContentRebuild(unittest.TestCase):
    def test_module_csv_row_count(self):
        with (ROOT / "input" / "modules.csv").open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 133)
        nums = sorted(int(r["module_num"]) for r in rows)
        self.assertEqual(nums[0], 1)
        self.assertEqual(nums[-1], 133)

    def test_phases_csv_row_count(self):
        with (ROOT / "input" / "phases.csv").open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 20)

    def test_canonical_prd_is_journey_focused(self):
        path = ROOT / "docs" / "PRD_AgentIQ.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
        self.assertGreater(len(text.splitlines()), 400)
        self.assertLess(len(text.splitlines()), 5000)
        self.assertIn("## Part A — Context", text)
        self.assertIn("## Part B — Curriculum by phase", text)
        self.assertIn("Phase P0 — Local AI Setup", text)
        self.assertIn("| `0.1` | 1 |", text)
        self.assertIn("content/phases/P0/modules/", text)
        self.assertIn("## Part C — Hackathons", text)
        self.assertIn("content/categories/hackathons.md", text)
        self.assertIn("## Part D — Startup ideas", text)
        self.assertIn("## Part E — Platform specification", text)
        self.assertNotIn("## Additional depth", text)
        self.assertNotRegex(text, r"(?i)patch\s*—\s*lines\s+\d+")
        self.assertNotIn("PRD_AgentIQ_Complete", text)
        self.assertNotIn("wtmp begins", text)

    def test_module_files_use_journey_id_under_phase(self):
        m1 = next((ROOT / "content" / "phases" / "P0" / "modules").glob("m001-*.md"))
        t = m1.read_text(encoding="utf-8")
        self.assertIn("journey_id: '0.1'", t)
        self.assertRegex(t, r"(?m)^#\s+0\.1\s+—")

    def test_layered_spec_no_duplicate_curriculum(self):
        slim = (ROOT / "content" / "spec" / "agentiq_platform_spec.md").read_text(encoding="utf-8")
        self.assertIn("## 7. PLATFORM FEATURES", slim)
        self.assertIn("## 9. AI AGENT SYSTEM", slim)
        self.assertNotIn("## 27. COMPLETE TOPIC COVERAGE", slim)
        cur = ROOT / "content" / "curriculum" / "section-6-modules.md"
        self.assertTrue(cur.is_file())
        self.assertIn("**Module 1:", cur.read_text(encoding="utf-8"))
        res = ROOT / "content" / "research" / "topic-and-extract-corpus.md"
        self.assertTrue(res.is_file())
        self.assertIn("## 27. COMPLETE TOPIC COVERAGE", res.read_text(encoding="utf-8"))

    def test_phase_supplement_and_categories(self):
        self.assertTrue((ROOT / "content" / "phases" / "P1" / "supplement.md").is_file())
        self.assertTrue((ROOT / "content" / "categories" / "hackathons.md").is_file())
        self.assertTrue((ROOT / "content" / "categories" / "startup-ideas.md").is_file())

    def test_one_markdown_file_per_curriculum_module(self):
        files = sorted((ROOT / "content" / "phases").glob("P*/modules/m*.md"))
        self.assertEqual(len(files), 133)

    def test_phase_index_files(self):
        for i in range(20):
            p = ROOT / "content" / "phases" / f"P{i}" / "index.md"
            self.assertTrue(p.is_file(), msg=f"missing {p}")

    def test_build_learner_phase_corpus_runs(self):
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_learner_phase_corpus.py")],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, msg=r.stderr or r.stdout)


if __name__ == "__main__":
    unittest.main()
