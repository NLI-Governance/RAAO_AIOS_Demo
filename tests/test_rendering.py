"""Run with: python -m unittest discover -s tests -v.

Tests use a disposable app copy so form submissions never write real HR data.
"""
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

import pandas as pd
from streamlit.testing.v1 import AppTest


class RenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_cwd = Path.cwd()
        cls.sandbox = tempfile.TemporaryDirectory()
        cls.root = Path(cls.sandbox.name)
        source = Path(__file__).resolve().parents[1]
        shutil.copy2(source / "main.py", cls.root / "main.py")
        for folder in ("pages", "components", "assets"):
            shutil.copytree(source / folder, cls.root / folder)
        (cls.root / "tools").mkdir()
        for name in ("__init__.py", "shared_ui_components.py"):
            shutil.copy2(source / "tools" / name, cls.root / "tools" / name)
        sys.path.insert(0, str(cls.root))
        os.chdir(cls.root)

    @classmethod
    def tearDownClass(cls):
        os.chdir(cls.original_cwd)
        sys.path.remove(str(cls.root))
        cls.sandbox.cleanup()

    def app(self, page=None):
        app = AppTest.from_file(str(self.root / "main.py"), default_timeout=20).run()
        if page:
            app.switch_page(f"pages/{page}").run()
        return app

    def assert_renders(self, app):
        self.assertEqual([e.message for e in app.exception], [])

    def test_all_entry_points_render(self):
        self.assert_renders(self.app())
        for page in sorted((self.root / "pages").glob("*.py")):
            if page.name == "__init__.py":
                continue
            with self.subTest(page=page.name):
                self.assert_renders(self.app(page.name))

    def test_nda_consent_controls_entry_link(self):
        app = self.app("nda_gate_page.py")
        self.assert_renders(app)
        self.assertTrue(app.error)
        self.assertEqual(len(app.get("page_link")), 0)
        app.checkbox[0].check().run()
        self.assert_renders(app)
        self.assertTrue(app.success)
        self.assertEqual(len(app.get("page_link")), 1)
        self.assertIn("Enter System", app.get("page_link")[0].proto.label)
        app.switch_page("pages/navigation_menu_gui.py").run()
        self.assert_renders(app)
        app.switch_page("pages/nda_gate_page.py").run()
        app.checkbox[0].uncheck().run()
        self.assert_renders(app)
        self.assertEqual(len(app.get("page_link")), 0)

    def test_language_and_unconfigured_assistant(self):
        for page in ("nda_gate_page.py", "disciplinary_actions_gui.py", "training_tracker_gui.py"):
            with self.subTest(page=page):
                app = self.app(page)
                app.selectbox(key="language_toggle").select("Français").run()
                self.assert_renders(app)
                self.assertEqual(app.selectbox(key="language_toggle").value, "Français")
                question = next(w for w in app.text_input if w.label.startswith("Ask a question"))
                question.set_value("Where can I find help?").run()
                self.assert_renders(app)
                self.assertTrue(any("contact your supervisor" in x.value for x in app.info))

    def test_employee_back_navigation(self):
        app = self.app("employee_app_gui.py")
        self.assert_renders(app)
        app.button[0].click().run()
        self.assert_renders(app)
        self.assertFalse(app.title)
        self.assertTrue(any("AIOS" in x.value for x in app.markdown))

    def test_disciplinary_submission_appends_one_header(self):
        path = self.root / "data" / "disciplinary_records.csv"
        app = self.app("disciplinary_actions_gui.py")
        app.text_input[0].set_value("Test Employee")
        app.text_input[1].set_value("TEST-001")
        app.button[0].click().run()
        self.assert_renders(app)
        self.assertTrue(app.success)
        app.button[0].click().run()
        self.assert_renders(app)
        records = pd.read_csv(path)
        self.assertEqual(len(records), 2)
        self.assertEqual(records["Employee ID"].tolist(), ["TEST-001", "TEST-001"])
        self.assertEqual(path.read_text(encoding="utf-8").count("Employee Name,"), 1)


if __name__ == "__main__":
    unittest.main()
