"""验证 MFAC 全项目保守库存审计。"""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_project_inventory_audit import (
    build_inventory,
    discover_modules,
)


class MFACProjectInventoryAuditTest(unittest.TestCase):
    """验证 MFAC 模块库存的保守索引规则。"""

    def test_discover_modules_matches_sorted_expected_json_paths(self) -> None:
        """模块 stem 必须稳定映射到预期 JSON 证书路径。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experiments = root / "experiments"
            monograph = root / "docs" / "monograph"
            experiments.mkdir(parents=True)
            monograph.mkdir(parents=True)
            (experiments / "prime_matrix_mfac_zeta_audit.py").write_text(
                "", encoding="utf-8"
            )
            (experiments / "prime_matrix_mfac_alpha_audit.py").write_text(
                "", encoding="utf-8"
            )

            records = discover_modules(root)

            self.assertEqual(
                [record["module_name"] for record in records], ["alpha", "zeta"]
            )
            self.assertEqual(
                records[0]["certificate_path"],
                "docs/monograph/prime-matrix-mfac-alpha-audit.json",
            )

    def test_inventory_keeps_false_rh_for_open_conditional_and_claimed_true_inputs(
        self,
    ) -> None:
        """任何输入组合都不得把库存顶层升级为 RH 闭合。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experiments = root / "experiments"
            monograph = root / "docs" / "monograph"
            experiments.mkdir(parents=True)
            monograph.mkdir(parents=True)
            for name in ("conditional", "open", "claimed_true", "missing"):
                (experiments / f"prime_matrix_mfac_{name}_audit.py").write_text(
                    "", encoding="utf-8"
                )
            (monograph / "prime-matrix-mfac-conditional-audit.json").write_text(
                '{"status":"conditional_external_input","rh_proved":false}',
                encoding="utf-8",
            )
            (monograph / "prime-matrix-mfac-open-audit.json").write_text(
                '{"l2_upper_status":"unproved","rh_proved":false}',
                encoding="utf-8",
            )
            (monograph / "prime-matrix-mfac-claimed-true-audit.json").write_text(
                '{"rh_proved":true}', encoding="utf-8"
            )

            inventory = build_inventory(root)

            self.assertFalse(inventory["rh_proved"])
            self.assertEqual(inventory["rh_closed_module_count"], 0)
            self.assertEqual(
                inventory["classification_counts"][
                    "missing_or_unreadable_certificate"
                ],
                1,
            )
            by_name = {record["module_name"]: record for record in inventory["modules"]}
            self.assertEqual(
                by_name["conditional"]["classification"],
                "conditional_or_external_dependency",
            )
            self.assertEqual(by_name["open"]["classification"], "open_or_unresolved")
            self.assertEqual(
                by_name["claimed_true"]["classification"],
                "requires_manual_rh_review",
            )

    def test_cli_writes_inventory_and_bad_json_stays_unreadable(self) -> None:
        """CLI 必须可执行，坏 JSON 必须保守登记而非崩溃或推断。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experiments = root / "experiments"
            monograph = root / "docs" / "monograph"
            experiments.mkdir()
            monograph.mkdir(parents=True)
            (experiments / "prime_matrix_mfac_bad_audit.py").write_text(
                "", encoding="utf-8"
            )
            (monograph / "prime-matrix-mfac-bad-audit.json").write_text(
                "{", encoding="utf-8"
            )
            json_path = root / "inventory.json"
            markdown_path = root / "inventory.md"

            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_project_inventory_audit.py",
                    "--repo-root",
                    str(root),
                    "--json-out",
                    str(json_path),
                    "--markdown-out",
                    str(markdown_path),
                ],
                cwd=Path.cwd(),
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(
                payload["modules"][0]["classification"],
                "missing_or_unreadable_certificate",
            )
            self.assertFalse(payload["rh_proved"])
            self.assertIn("不构成 RH 证明", markdown_path.read_text(encoding="utf-8"))

    def test_non_object_and_unknown_rh_certificate_stay_conservatively_open(self) -> None:
        """非对象和缺少 RH 字段的证书均不得被乐观视为有限闭合。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experiments = root / "experiments"
            monograph = root / "docs" / "monograph"
            experiments.mkdir()
            monograph.mkdir(parents=True)
            for name in ("array", "unknown"):
                (experiments / f"prime_matrix_mfac_{name}_audit.py").write_text(
                    "", encoding="utf-8"
                )
            (monograph / "prime-matrix-mfac-array-audit.json").write_text(
                "[]", encoding="utf-8"
            )
            (monograph / "prime-matrix-mfac-unknown-audit.json").write_text(
                '{"finite_identity_verified":true}', encoding="utf-8"
            )

            inventory = build_inventory(root)
            by_name = {record["module_name"]: record for record in inventory["modules"]}

            self.assertEqual(
                by_name["array"]["classification"],
                "missing_or_unreadable_certificate",
            )
            self.assertEqual(by_name["unknown"]["classification"], "open_or_unresolved")


if __name__ == "__main__":
    unittest.main()
