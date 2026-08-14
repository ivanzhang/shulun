"""验证 MFAC 独立投影—LCM Gram 恒等式合同。"""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_lcm_gram_independent_projection_audit import (
    audit_lcm_gram_independent_projection_contract,
)


class MFACLCMGramIndependentProjectionAuditTest(unittest.TestCase):
    """验证独立投影—LCM Gram 恒等式合同。"""

    @staticmethod
    def valid_contract() -> dict[str, object]:
        """返回每个测试可独立修改的最小合法合同。"""
        return {
            "uses": ("finite_lcm_overlap_identity", "independent_feature_registration"),
            "projection_contract": {
                "space": "L2([X,2X])",
                "quantifier": "exists_X0_for_all_real_X_ge_X0_and_all_f_in_HX",
                "feature_family": "independent_divisibility_features",
                "feature_independence": "registered_independent_of_chebyshev_target",
                "closed_subspace": True,
                "orthogonal_projection": True,
                "constant_projection": "off_constant_projection",
                "uses": ("finite_lcm_overlap_identity",),
            },
            "gram_contract": {
                "kernel": "registered_lcm_gram_kernel",
                "coefficient_coordinates": "projection_coordinates",
                "normalization": "dyadic_L2_normalization",
                "lcm_overlap": "registered_lcm_divisibility_overlap",
                "constant_projection": "off_constant_projection",
                "uses": ("finite_lcm_overlap_identity",),
            },
            "claimed_identity_uses": ("finite_lcm_overlap_identity",),
        }

    def test_valid_contract_only_registers_unproved_projection_identity(self) -> None:
        """完整合同只能登记投影接口，不升级 Chebyshev、W2 或 RH。"""
        audit = audit_lcm_gram_independent_projection_contract(self.valid_contract())
        self.assertEqual(audit["projection_space_status"], "registered_unproved")
        self.assertEqual(audit["lcm_gram_identity_status"], "registered_unproved")
        self.assertEqual(audit["actual_chebyshev_projection_status"], "not_started")
        self.assertFalse(audit["rh_proved"])

    def test_contract_rejects_cycles_alignment_errors_and_undeclared_sources(self) -> None:
        """目标/解析循环、投影错配和未声明来源均必须被拒绝。"""
        for location, forbidden in (
            ("uses", "Chebyshev_error"),
            ("projection", "Mellin"),
            ("gram", "RH"),
            ("uses", "PNT"),
        ):
            broken = deepcopy(self.valid_contract())
            if location == "uses":
                broken["uses"] += (forbidden,)
            elif location == "projection":
                broken["projection_contract"]["uses"] += (forbidden,)
            else:
                broken["gram_contract"]["uses"] += (forbidden,)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_lcm_gram_independent_projection_contract(broken)
        mismatch = deepcopy(self.valid_contract())
        mismatch["gram_contract"]["constant_projection"] = "constant_projection"
        with self.assertRaisesRegex(ValueError, "一致"):
            audit_lcm_gram_independent_projection_contract(mismatch)
        undeclared = deepcopy(self.valid_contract())
        undeclared["claimed_identity_uses"] = ("unregistered_source",)
        with self.assertRaisesRegex(ValueError, "未声明"):
            audit_lcm_gram_independent_projection_contract(undeclared)
        cyclic = deepcopy(self.valid_contract())
        cyclic["projection_identity_proved"] = False
        with self.assertRaisesRegex(ValueError, "目标结论"):
            audit_lcm_gram_independent_projection_contract(cyclic)

    def test_certificate_and_cli_keep_projection_and_rh_unproved(self) -> None:
        """CLI 证书必须保持投影、W2 和 RH 均未证明。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "projection.json"
            markdown_path = root / "projection.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_lcm_gram_independent_projection_audit.py",
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
                payload["lcm_gram_identity_status"], "registered_unproved"
            )
            self.assertEqual(
                payload["actual_chebyshev_projection_status"], "not_started"
            )
            self.assertFalse(payload["rh_proved"])
            self.assertIn("不证明", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
