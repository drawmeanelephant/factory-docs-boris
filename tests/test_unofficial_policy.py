import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"pricing", "support", "jp/pricing", "jp/support"}
spec = importlib.util.spec_from_file_location("converter", ROOT / "convert_factory_to_boris.py")
converter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(converter)


class UnofficialSitePolicyTests(unittest.TestCase):
    def test_both_layouts_have_static_disclaimers_and_noindex(self):
        for name in ["main.html", "trunk.html"]:
            with self.subTest(layout=name):
                text = (ROOT / "themes/factory/layouts" / name).read_text()
                self.assertIn('name="robots" content="noindex, nofollow, noarchive"', text)
                self.assertIn("UNOFFICIAL / 非公式", text)
                self.assertIn("Not affiliated with, endorsed by, sponsored by, or maintained by", text)
                self.assertIn('class="factory-article-disclaimer"', text)
                self.assertIn("Unofficial Boris Demo</title>", text)
                self.assertNotIn('data-topbar-target="pricing"', text)
                self.assertNotIn('data-topbar-target="support"', text)
                self.assertNotIn('alt="Factory"', text)

    def test_excluded_pages_and_internal_links_are_absent(self):
        for page_id in EXCLUDED:
            self.assertFalse((ROOT / "content" / (page_id + ".md")).exists())
        for path in (ROOT / "content").rglob("*.md"):
            self.assertIsNone(re.search(r"\[\[(?:jp/)?(?:pricing|support)(?:[|#\]])",
                                        path.read_text()), str(path))

    def test_robot_crawling_is_allowed_so_noindex_can_be_read(self):
        robots = (ROOT / "static/robots.txt").read_text()
        self.assertIn("Allow: /", robots)
        self.assertNotRegex(robots, r"(?m)^Disallow:\s*/")
        self.assertIn('name="robots" content="noindex, nofollow, noarchive"',
                      (ROOT / "static/404.html").read_text())

    def test_converter_sends_pricing_and_support_to_official_site(self):
        for href, current, expected in [
            ("/pricing", "index", "https://docs.factory.ai/pricing"),
            ("../../support.md", "cli/configuration/settings", "https://docs.factory.ai/support"),
            ("/support", "jp/index", "https://docs.factory.ai/jp/support"),
            ("https://docs.factory.ai/pricing#plans", "jp/index",
             "https://docs.factory.ai/pricing#plans"),
        ]:
            with self.subTest(href=href):
                self.assertEqual(converter.official_only_url(href, current), expected)
                self.assertIsNone(converter.resolve_internal_target(href, current, EXCLUDED))
        self.assertIsNone(converter.official_only_url("https://example.com/support", "index"))
        body = converter.convert_mdx_body('<Card title="Support" href="/support" />',
                                          "index", EXCLUDED)
        self.assertIn("https://docs.factory.ai/support", body)
        self.assertNotIn("[[support", body)

    def test_converter_does_not_regenerate_excluded_pages(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / "source"
            source.mkdir()
            (source / "index.mdx").write_text(
                '---\ntitle: Demo\n---\n## Links\n[Pricing](/pricing)\n[Support](/support)\n'
            )
            for page_id in EXCLUDED:
                target = source / (page_id + ".mdx")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("---\ntitle: Must not be mirrored\n---\nPrivate mirror policy fixture.\n")
            api = root / "openapi.json"
            api.write_text(json.dumps({"paths": {}, "components": {"schemas": {}}}))
            content = root / "content"
            with patch.multiple(converter, BORIS_ROOT=str(root), FACTORY_DOCS=str(source),
                                CONTENT_DIR=str(content), STATIC_DIR=str(root / "static"),
                                OPENAPI_SPEC=str(api)), \
                    patch.object(converter, "copy_static_assets", return_value=0), \
                    patch.object(converter, "build_leaderboard_includes", return_value={}):
                converter.main()
            self.assertEqual([p.relative_to(content).as_posix() for p in content.rglob("*.md")],
                             ["index.md"])
            rendered = (content / "index.md").read_text()
            self.assertIn("https://docs.factory.ai/pricing", rendered)
            self.assertIn("https://docs.factory.ai/support", rendered)


if __name__ == "__main__":
    unittest.main()
