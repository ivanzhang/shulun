"""验证全 epsilon Mertens 条件化 L2--Upper 审计的合同边界。"""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_mertens_conditional_l2_upper_audit import (
    audit_mertens_all_epsilon_contract,
)


class MFACMertensConditionalL2UpperAuditTest(unittest.TestCase):
    """验证全 epsilon Mertens 条件链的合同和结论边界。"""

    def test_all_epsilon_mertens_contract_keeps_constant_nonuniform(self) -> None:
        """全 epsilon 假设只允许常数依赖当前 epsilon。"""
        audit = audit_mertens_all_epsilon_contract(
            {
                "uses": (
                    "finite_divisor_identity",
                    "euler_phi_identity",
                    "Mertens_cancellation",
                    "partial_summation",
                    "coprimality_inclusion_exclusion",
                ),
                "for_every_epsilon": True,
                "epsilon_domain": "positive_real",
                "assumption": "M(x)=O_epsilon(x^(1/2+epsilon))",
                "constant_dependency": "C_epsilon_depends_on_epsilon_only",
                "uniform_in_epsilon": False,
                "epsilon": 0.1,
                "mertens_constant": 3.0,
            }
        )
        self.assertEqual(audit["mertens_assumption_status"], "externally_assumed")
        self.assertEqual(audit["epsilon_instance"], 0.1)
        self.assertFalse(audit["constant_uniform_in_epsilon"])
        self.assertEqual(audit["unconditional_l2_upper_status"], "unproved")
        self.assertFalse(audit["rh_proved"])

    def test_contract_rejects_missing_quantifier_uniform_constant_and_cycle(self) -> None:
        """条件链不得省略量词、伪造一致常数或引用 RH/目标结论。"""
        base = {
            "uses": (
                "finite_divisor_identity",
                "euler_phi_identity",
                "Mertens_cancellation",
                "partial_summation",
                "coprimality_inclusion_exclusion",
            ),
            "for_every_epsilon": True,
            "epsilon_domain": "positive_real",
            "assumption": "M(x)=O_epsilon(x^(1/2+epsilon))",
            "constant_dependency": "C_epsilon_depends_on_epsilon_only",
            "uniform_in_epsilon": False,
            "epsilon": 0.1,
            "mertens_constant": 3.0,
        }
        for field, value, message in (
            ("for_every_epsilon", False, "for_every_epsilon"),
            ("uniform_in_epsilon", True, "uniform_in_epsilon"),
            ("epsilon", 0.0, "epsilon"),
        ):
            broken = dict(base)
            broken[field] = value
            with self.assertRaisesRegex(ValueError, message):
                audit_mertens_all_epsilon_contract(broken)

        cyclic = dict(base)
        cyclic["uses"] = base["uses"] + ("RH", "target_l2_upper")
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_mertens_all_epsilon_contract(cyclic)

    def test_contract_rejects_invalid_shapes_numbers_and_undeclared_bound_uses(self) -> None:
        """合同必须拒绝错误容器、非有限参数和未声明界来源。"""
        base = {
            "uses": (
                "finite_divisor_identity",
                "euler_phi_identity",
                "Mertens_cancellation",
                "partial_summation",
                "coprimality_inclusion_exclusion",
            ),
            "for_every_epsilon": True,
            "epsilon_domain": "positive_real",
            "assumption": "M(x)=O_epsilon(x^(1/2+epsilon))",
            "constant_dependency": "C_epsilon_depends_on_epsilon_only",
            "uniform_in_epsilon": False,
            "epsilon": 0.1,
            "mertens_constant": 3.0,
        }
        with self.assertRaisesRegex(ValueError, "Mapping"):
            audit_mertens_all_epsilon_contract(())
        malformed_uses = dict(base)
        malformed_uses["uses"] = "Mertens_cancellation"
        with self.assertRaisesRegex(ValueError, "uses"):
            audit_mertens_all_epsilon_contract(malformed_uses)
        nonfinite_epsilon = dict(base)
        nonfinite_epsilon["epsilon"] = float("nan")
        with self.assertRaisesRegex(ValueError, "epsilon"):
            audit_mertens_all_epsilon_contract(nonfinite_epsilon)
        undeclared = dict(base)
        undeclared["claimed_bound_uses"] = ("Mellin",)
        with self.assertRaisesRegex(ValueError, "未声明"):
            audit_mertens_all_epsilon_contract(undeclared)

    def test_certificate_and_cli_never_claim_unconditional_l2_or_rh(self) -> None:
        """JSON、Markdown 和脚本路径 CLI 都必须保留条件性边界。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "audit.json"
            markdown_path = root / "audit.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_mertens_conditional_l2_upper_audit.py",
                    "--epsilon",
                    "0.1",
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
                payload["conditional_l2_upper_status"],
                "assumption_chain_registered",
            )
            self.assertEqual(payload["unconditional_l2_upper_status"], "unproved")
            self.assertFalse(payload["rh_proved"])
            self.assertIn("开放证明义务", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
