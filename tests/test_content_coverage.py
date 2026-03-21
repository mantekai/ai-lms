"""Coverage tracker CSV and enriched modules."""
import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestContentCoverage(unittest.TestCase):
    def test_topics_csv_has_133_rows(self):
        p = ROOT / "data" / "topics_coverage.csv"
        self.assertTrue(p.exists())
        with p.open(encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 133)

    def test_module_7_full_tier(self):
        with (ROOT / "data" / "curriculum.json").open(encoding="utf-8") as f:
            data = json.load(f)
        m7 = next(m for ph in data["phases"] for m in ph["modules"] if m["num"] == 7)
        self.assertEqual(m7["content_tier"], "full")
        self.assertIn("AGI", m7["learn"])
        self.assertIn("term-list", m7["learn"])
        self.assertIn("tiktoken", m7["code"])

    def test_all_modules_content_tier_full(self):
        with (ROOT / "data" / "curriculum.json").open(encoding="utf-8") as f:
            data = json.load(f)
        for ph in data["phases"]:
            for m in ph["modules"]:
                self.assertEqual(
                    m.get("content_tier"),
                    "full",
                    msg=f"module {m['num']} should be content_tier full",
                )

    def test_coverage_embed(self):
        p = ROOT / "data" / "coverage.json"
        self.assertTrue(p.exists(), msg="run python3 build_curriculum.py to generate data/coverage.json")
        cov = json.loads(p.read_text(encoding="utf-8"))
        self.assertEqual(len(cov["modules"]), 133)
        row7 = next(r for r in cov["modules"] if int(r["module_num"]) == 7)
        self.assertEqual(row7["self_contained_on_page"], "yes")
        self.assertGreater(len(cov.get("blueprint_crosswalk", [])), 0)


if __name__ == "__main__":
    unittest.main()
