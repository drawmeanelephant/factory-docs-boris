import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


profile_script = load_script("pages-profile")
artifact_script = load_script("prepare-pages")


class PagesProfileTests(unittest.TestCase):
    def setUp(self):
        self.profile = json.loads((ROOT / "boris.json").read_text())

    def test_project_and_root_locations_update_all_metadata(self):
        for url, origin, base_path in [
            ("https://owner.github.io/project/", "https://owner.github.io", "/project"),
            ("https://owner.github.io/", "https://owner.github.io", ""),
            ("https://docs.example.com/", "https://docs.example.com", ""),
        ]:
            with self.subTest(url=url):
                result = profile_script.pages_profile(copy.deepcopy(self.profile), url)
                self.assertEqual(result["publication"]["origin"], origin)
                self.assertEqual(result["publication"]["base_path"], base_path)
                self.assertEqual(result["site"]["url"], origin + base_path)
                self.assertEqual(result["targets"][0]["head"]["base_url"], origin + base_path)

    def test_invalid_locations_are_rejected(self):
        for url in [
            "http://owner.github.io/project",
            "https://owner.github.io/project?token=example",
            "https://owner.github.io/project#fragment",
            "https://user:password@owner.github.io/project",
            "https://owner.github.io/../project",
        ]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                profile_script.pages_profile(copy.deepcopy(self.profile), url)


class PagesArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "dist"
        self.destination = self.root / "public"
        self.source.mkdir()
        (self.source / "index.html").write_text("<h1>Site</h1>")
        (self.source / "_boris/proof").mkdir(parents=True)
        (self.source / "_boris/proof/checks.json").write_text("{}")
        (self.source / ".boris-cache").mkdir()
        (self.source / ".boris-cache/local.json").write_text("{}")
        content = (self.source / "index.html").read_bytes()
        self.record = {
            "path": "index.html",
            "status": "committed",
            "bytes": len(content),
            "sha256": hashlib.sha256(content).hexdigest(),
        }
        self.write_inventory([self.record])

    def write_inventory(self, records):
        (self.source / "_boris/proof/artifacts.json").write_text(json.dumps({
            "format": "boris-publication-artifacts",
            "schema_version": 1,
            "target": "public",
            "artifacts": records,
        }))

    def test_only_verified_payloads_are_published(self):
        summary = artifact_script.prepare(self.source, self.destination)
        self.assertEqual(summary["files"], 1)
        self.assertEqual(summary["bytes"], self.record["bytes"])
        self.assertEqual((self.destination / "index.html").read_bytes(),
                         (self.source / "index.html").read_bytes())
        self.assertFalse((self.destination / "_boris").exists())
        self.assertFalse((self.destination / ".boris-cache").exists())

    def test_changed_payload_is_rejected(self):
        (self.source / "index.html").write_text("changed")
        with self.assertRaisesRegex(ValueError, "mismatch"):
            artifact_script.prepare(self.source, self.destination)

    def test_unsafe_or_private_inventory_paths_are_rejected(self):
        for name in ["../secret", "/absolute", "nested//file", "_boris/proof/checks.json",
                     ".boris-cache/local.json", "nested\\file"]:
            with self.subTest(path=name):
                self.write_inventory([{**self.record, "path": name}])
                with self.assertRaises(ValueError):
                    artifact_script.prepare(self.source, self.destination)

    def test_duplicate_or_uncommitted_records_are_rejected(self):
        self.write_inventory([self.record, self.record])
        with self.assertRaises(ValueError):
            artifact_script.prepare(self.source, self.destination)
        second_destination = self.root / "other"
        self.write_inventory([{**self.record, "status": "planned"}])
        with self.assertRaises(ValueError):
            artifact_script.prepare(self.source, second_destination)

    def test_symlinked_destination_is_rejected(self):
        (self.root / "real").mkdir()
        self.destination.symlink_to(self.root / "real", target_is_directory=True)
        with self.assertRaises(ValueError):
            artifact_script.prepare(self.source, self.destination)

    def test_symlinked_artifact_is_rejected(self):
        original = self.source / "index.html"
        original.rename(self.source / "real.html")
        original.symlink_to("real.html")
        with self.assertRaises(ValueError):
            artifact_script.prepare(self.source, self.destination)

    def test_existing_destination_is_not_overwritten(self):
        self.destination.mkdir()
        keep = self.destination / "keep.txt"
        keep.write_text("user file")
        with self.assertRaises(ValueError):
            artifact_script.prepare(self.source, self.destination)
        self.assertEqual(keep.read_text(), "user file")


if __name__ == "__main__":
    unittest.main()
