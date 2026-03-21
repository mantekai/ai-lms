"""Validate curriculum embed matches AI Master Tracker blueprint counts."""
import csv
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "data" / "curriculum.json"
JS_PATH = ROOT / "assets" / "js" / "app.js"


class TestCurriculumBlueprint(unittest.TestCase):
    def test_module_and_phase_counts(self):
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        phases = data["phases"]
        self.assertEqual(len(phases), 20)
        total = sum(len(p["modules"]) for p in phases)
        self.assertEqual(total, 133)
        p8 = next(p for p in phases if p["code"] == "P8")
        p9 = next(p for p in phases if p["code"] == "P9")
        self.assertEqual(len(p8["modules"]), 8)
        self.assertEqual(len(p9["modules"]), 5)

    def test_module_numbers_sequential(self):
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        nums = []
        for ph in data["phases"]:
            for m in ph["modules"]:
                nums.append(m["num"])
        self.assertEqual(nums, list(range(1, 134)))

    def test_each_module_has_tabs_content(self):
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        for ph in data["phases"]:
            for m in ph["modules"]:
                self.assertTrue(m.get("learn"))
                self.assertTrue(m.get("steps"))
                self.assertTrue(m.get("code"))
                self.assertTrue(m.get("refs"))

    def test_no_legacy_generic_scaffold_copy(self):
        """All modules should use per-module Learn/Steps, not the old one-size-fits-all checklist."""
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        bad = "Reproduce the code sample locally; change one parameter"
        for ph in data["phases"]:
            for m in ph["modules"]:
                self.assertNotIn(bad, m.get("steps", ""), msg=f"module {m['num']} still uses generic steps")

    def test_platform_logic_js_syntax(self):
        """Composed app bundle must parse — syntax errors break the shell (regenerate via scripts/compose_app_js.py)."""
        r = subprocess.run(
            ["node", "--check", str(JS_PATH)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(r.returncode, 0, msg=r.stderr or r.stdout)

    def test_references_minimum_links(self):
        """Each module should expose several external references (merged + deduped)."""
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        for ph in data["phases"]:
            for m in ph["modules"]:
                n = len(re.findall(r"ext-link", m.get("refs", "")))
                self.assertGreaterEqual(
                    n,
                    6,
                    msg=f"module {m['num']} has only {n} reference links",
                )

    def test_p19_cert_modules_emphasize_gen_ai_not_classic_ml_only(self):
        """Phase P19 rows should describe AI/LLM credentials, not legacy ML-only positioning."""
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        p19 = next(p for p in data["phases"] if p["code"] == "P19")
        titles = [m["title"] for m in p19["modules"]]
        self.assertEqual(len(titles), 6)
        joined = " ".join(titles).lower()
        self.assertIn("generative", joined)
        self.assertIn("vertex", joined)
        self.assertIn("practitioner", joined)
        self.assertIn("llm", joined)
        self.assertNotIn("ml specialty", joined)
        self.assertNotIn("ml engineer)", joined)

    def test_cert_tracker_has_price_tags_and_filters(self):
        """Cert rows live in data/catalog/certs.csv; UI logic in composed assets/js/app.js."""
        js = JS_PATH.read_text(encoding="utf-8")
        self.assertIn("setCertPriceFilter", js)
        self.assertIn("certDefsFiltered", js)
        self.assertIn("cert-toolbar", js)
        self.assertIn("rowsToCerts", js)
        csv_path = ROOT / "data" / "catalog" / "certs.csv"
        self.assertTrue(csv_path.exists())
        with csv_path.open(encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        n_free = sum(1 for r in rows if r.get("price") == "free")
        n_paid = sum(1 for r in rows if r.get("price") == "paid")
        n_mixed = sum(1 for r in rows if r.get("price") == "mixed")
        self.assertGreaterEqual(n_free, 12)
        self.assertGreaterEqual(n_paid, 4)
        self.assertGreaterEqual(n_mixed, 1)


if __name__ == "__main__":
    unittest.main()
