from fractions import Fraction
import json
import math
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_mobius_tail_l2_audit import (
    audit_l2_upper_contract,
    audit_mobius_tail_l2,
    euler_phi_square_energy,
    euler_phi_square_energy_float,
    limit_kernel_energy,
    limit_kernel_energy_float,
    mobius_log_tail_sum,
    truncated_mobius_log_limit_coefficients,
    write_certificate,
)


class MFACMobiusTailL2AuditTest(unittest.TestCase):
    """验证 Möbius 尾和 L² 门槛的有限代数恒等式。"""

    def test_euler_phi_square_sum_matches_limit_kernel_for_rational_coefficients(self) -> None:
        """Euler--phi 平方和必须精确等于极限核二次型。"""
        coefficients = {
            2: Fraction(3, 2),
            3: Fraction(-2, 3),
            6: Fraction(5, 7),
        }
        self.assertEqual(
            limit_kernel_energy(coefficients),
            euler_phi_square_energy(coefficients),
        )

    def test_squarefree_tail_formula_agrees_with_direct_divisor_tail(self) -> None:
        """平方自由 r 的闭式 Möbius 尾和必须匹配直接因子求和。"""
        cutoff = 64
        coefficients = truncated_mobius_log_limit_coefficients(cutoff)
        self.assertAlmostEqual(
            mobius_log_tail_sum(cutoff, 6),
            sum(
                value / index
                for index, value in coefficients.items()
                if index % 6 == 0
            ),
            places=12,
        )
        self.assertEqual(mobius_log_tail_sum(cutoff, 4), 0.0)

    def test_float_euler_phi_energy_matches_direct_limit_kernel(self) -> None:
        """含 log 的浮点系数也必须保留可报告的代数残差。"""
        coefficients = truncated_mobius_log_limit_coefficients(64)
        direct = limit_kernel_energy_float(coefficients)
        decomposed = euler_phi_square_energy_float(coefficients)
        self.assertGreater(direct, 0.0)
        self.assertAlmostEqual(direct, decomposed, places=10)
        self.assertTrue(math.isfinite(decomposed))

    def test_l2_contract_rejects_undeclared_mertens_and_zero_inputs(self) -> None:
        """L2--Upper 不得把 Mertens 或零点输入伪装成结构自足推导。"""
        independent = audit_l2_upper_contract(
            {"uses": ("finite_divisor_identity", "euler_phi_identity")}
        )
        self.assertEqual(
            independent["classification"], "no_external_mobius_estimate_declared"
        )

        conditional = audit_l2_upper_contract(
            {"uses": ("Mertens_cancellation", "PNT")}
        )
        self.assertEqual(
            conditional["classification"], "conditional_on_named_mobius_estimate"
        )
        self.assertEqual(
            conditional["analytic_dependencies"], ("Mertens_cancellation", "PNT")
        )

        with self.assertRaisesRegex(ValueError, "未声明"):
            audit_l2_upper_contract(
                {
                    "uses": ("finite_divisor_identity",),
                    "claimed_bound_uses": ("Mellin",),
                }
            )

    def test_certificate_never_promotes_l2_profile_to_theorem(self) -> None:
        """文件证书必须保留 L² 上界未证明与 RH 边界。"""
        with TemporaryDirectory() as directory:
            json_path = Path(directory) / "audit.json"
            markdown_path = Path(directory) / "audit.md"
            certificate = audit_mobius_tail_l2(64)
            certificate["l2_upper_contract"] = audit_l2_upper_contract(
                {"uses": ("finite_divisor_identity", "euler_phi_identity")}
            )
            write_certificate(certificate, json_path, markdown_path)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["l2_upper_status"], "unproved")
            self.assertFalse(payload["rh_proved"])
            self.assertIn(
                "不构成 L2--Upper", markdown_path.read_text(encoding="utf-8")
            )

    def test_cli_path_execution_writes_json_and_markdown_outputs(self) -> None:
        """直接用脚本路径执行 CLI 时必须成功写出 JSON 和 Markdown。"""
        with TemporaryDirectory() as directory:
            directory_path = Path(directory)
            json_path = directory_path / "audit.json"
            markdown_path = directory_path / "audit.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_mobius_tail_l2_audit.py",
                    "--cutoff",
                    "64",
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
            self.assertTrue(json_path.exists())
            self.assertTrue(markdown_path.exists())


if __name__ == "__main__":
    unittest.main()
