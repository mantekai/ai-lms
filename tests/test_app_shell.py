"""index.html shell wires external CSS/JS and data-driven boot."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestAppShell(unittest.TestCase):
    def test_index_html_loads_assets(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="assets/css/app.css"', html)
        self.assertIn('src="assets/js/app.js"', html)
        self.assertIn('id="app-loading"', html)
        self.assertNotIn("CURRICULUM_JSON", html)
        self.assertIn("exportModulesProgressCsv", html)
        self.assertIn("importModulesProgressCsv", html)

    def test_curriculum_mirror_matches_primary_when_both_exist(self):
        primary = ROOT / "data" / "curriculum.json"
        legacy = ROOT / "curriculum.embed.json"
        if not primary.exists() or not legacy.exists():
            self.skipTest("run build_curriculum.py to generate both JSON outputs")
        self.assertEqual(
            primary.read_text(encoding="utf-8"),
            legacy.read_text(encoding="utf-8"),
            msg="curriculum.embed.json should mirror data/curriculum.json after build",
        )


if __name__ == "__main__":
    unittest.main()
