from pathlib import Path
import tempfile
import unittest
from hobbly.core import run


class ReproductionTest(unittest.TestCase):
    def test_reproduction_writes_results_and_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "artifacts").mkdir()
            (root / "data").mkdir()
            result = run(root)
            self.assertEqual(result["project_id"], "PRJ-HOBBLY-PROTOTYPE")
            self.assertTrue((root / "artifacts" / "results.json").is_file())
            self.assertTrue((root / "artifacts" / "evidence-manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()
