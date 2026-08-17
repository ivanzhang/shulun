"""测试 MFAC W1→W2 非循环 Möbius 尾和 L² 桥审计。"""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit import (
    REQUIRED_OBLIGATIONS,
    audit_noncircular_mobius_tail_l2,
    default_contract,
    finite_coprime_mobius_tail_model,
)


class MFACW1W2NoncircularMobiusTailL2AuditTest(unittest.TestCase):
    """验证有限模型不升级 W1→W2 或 RH 结论。"""

    def test_valid_contract_keeps_every_analytic_obligation_open(self) -> None:
        """合法合同只能登记有限层，三项解析义务必须保持开放。"""
        payload = audit_noncircular_mobius_tail_l2(default_contract(), limit=12)

        self.assertEqual(
            REQUIRED_OBLIGATIONS,
            (
                "coprime_restricted_tail_bound",
                "euler_phi_l2_aggregation",
                "chebyshev_energy_transfer",
            ),
        )
        self.assertEqual(payload["w1_to_w2_status"], "unproved")
        self.assertEqual(payload["coprime_restricted_tail_bound_status"], "open")
        self.assertEqual(payload["euler_phi_l2_aggregation_status"], "open")
        self.assertEqual(payload["chebyshev_energy_transfer_status"], "open")
        self.assertFalse(payload["rh_proved"])

    def test_contract_rejects_circular_inputs_missing_quantifiers_and_promotions(
        self,
    ) -> None:
        """循环来源、量词缺失和目标结论提升都必须被拒绝。"""
        base = default_contract()
        for source in ("RH", "Mertens", "PNT", "zeta_zero", "Mellin"):
            broken = deepcopy(base)
            broken["uses"] += (source,)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_noncircular_mobius_tail_l2(broken, limit=12)

        undeclared = deepcopy(base)
        undeclared["claimed_uses"]["euler_phi_l2_aggregation"] = ("Mellin",)
        with self.assertRaisesRegex(ValueError, "未声明|禁止"):
            audit_noncircular_mobius_tail_l2(undeclared, limit=12)

        missing = deepcopy(base)
        del missing["claimed_uses"]["chebyshev_energy_transfer"]
        with self.assertRaisesRegex(ValueError, "claimed_uses"):
            audit_noncircular_mobius_tail_l2(missing, limit=12)

        for field, value in (
            ("uniformity_variable", "scale"),
            ("constant_dependency", "truncation"),
            ("rh_proved", True),
            ("w2_closed", True),
        ):
            broken = deepcopy(base)
            broken[field] = value
            with self.assertRaises(ValueError):
                audit_noncircular_mobius_tail_l2(broken, limit=12)

    def test_contract_rejects_unallowed_and_unchecked_claimed_sources(self) -> None:
        """来源白名单必须拒绝未知来源和未核验的额外义务。"""
        unknown_source = deepcopy(default_contract())
        unknown_source["uses"] += ("unregistered_source",)
        with self.assertRaisesRegex(ValueError, "未允许"):
            audit_noncircular_mobius_tail_l2(unknown_source, limit=12)

        extra_obligation = deepcopy(default_contract())
        extra_obligation["claimed_uses"]["hidden_obligation"] = ("Mellin",)
        with self.assertRaisesRegex(ValueError, "claimed_uses"):
            audit_noncircular_mobius_tail_l2(extra_obligation, limit=12)

    def test_finite_model_matches_direct_and_euler_phi_energies(self) -> None:
        """有限 Möbius 尾和的两种写法与 Euler--φ 重排必须精确一致。"""
        payload = finite_coprime_mobius_tail_model(12)

        self.assertEqual(payload["finite_model_status"], "verified_finite")
        self.assertEqual(payload["limit"], 12)
        self.assertEqual(payload["candidate_moduli"], tuple(range(2, 12)))
        self.assertEqual(payload["energy_identity_residual"], "0")
        self.assertEqual(payload["coprime_tail_identity_residual"], "0")
        self.assertEqual(
            payload["direct_finite_energy"], payload["euler_phi_finite_energy"]
        )

    def test_finite_model_rejects_invalid_limits(self) -> None:
        """有限模型只能接受至少为 3 的内建整数截断。"""
        for limit in (True, 1, 2.0, "12"):
            with self.assertRaisesRegex(ValueError, "limit"):
                finite_coprime_mobius_tail_model(limit)

    def test_audit_includes_finite_model_without_promoting_analytic_status(self) -> None:
        """审计载荷必须并列有限核验与未证明的解析义务。"""
        payload = audit_noncircular_mobius_tail_l2(default_contract(), limit=12)

        self.assertEqual(payload["finite_model_status"], "verified_finite")
        self.assertEqual(payload["energy_identity_residual"], "0")
        self.assertEqual(payload["w1_to_w2_status"], "unproved")
        self.assertEqual(payload["euler_phi_l2_aggregation_status"], "open")

    def test_script_path_cli_writes_finite_but_unproved_certificate(self) -> None:
        """CLI 证书必须区分有限恒等式核验与未证明的解析桥。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "audit.json"
            markdown_path = root / "audit.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_w1_w2_noncircular_mobius_tail_l2_audit.py",
                    "--limit",
                    "12",
                    "--json-out",
                    str(json_path),
                    "--markdown-out",
                    str(markdown_path),
                ],
                cwd=Path.cwd(),
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["finite_model_status"], "verified_finite")
            self.assertEqual(payload["w1_to_w2_status"], "unproved")
            self.assertFalse(payload["rh_proved"])
            markdown = markdown_path.read_text(encoding="utf-8")
            self.assertIn("euler_phi_l2_aggregation_status=open", markdown)
            self.assertIn("不证明", markdown)


if __name__ == "__main__":
    unittest.main()
