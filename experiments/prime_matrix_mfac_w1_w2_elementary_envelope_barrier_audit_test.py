"""测试 MFAC W1→W2 初等绝对值包络障碍审计器。"""

import unittest
from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from experiments.prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit import (
    audit_elementary_envelope_barrier,
    default_contract,
    dyadic_envelope_growth_witness,
    finite_elementary_envelope_model,
)


class MFACW1W2ElementaryEnvelopeBarrierAuditTest(unittest.TestCase):
    """验证有限包络审计不会提升全局解析结论。"""

    def test_valid_contract_keeps_all_global_obligations_open(self) -> None:
        """合法合同只能产生有限核验，不能关闭解析义务。"""
        payload = audit_elementary_envelope_barrier(
            default_contract(), limit=12, dyadic_levels=2
        )

        self.assertEqual(payload["finite_inequality_status"], "verified_finite")
        self.assertEqual(payload["finite_growth_status"], "finite_growth_witnessed")
        self.assertEqual(payload["nonuniformity_obligation_status"], "open")
        self.assertEqual(payload["w1_to_w2_status"], "unproved")
        self.assertFalse(payload["rh_proved"])

    def test_finite_model_verifies_exact_tail_and_envelope_inequalities(self) -> None:
        """有限模型必须精确核验尾和恒等式和全部包络余量。"""
        payload = finite_elementary_envelope_model(12)

        self.assertEqual(payload["finite_inequality_status"], "verified_finite")
        self.assertEqual(payload["limit"], 12)
        self.assertEqual(payload["candidate_moduli"], tuple(range(2, 12)))
        for row in payload["rows"]:
            self.assertEqual(row["tail_identity_residual"], "0")
            self.assertGreaterEqual(Fraction(row["pointwise_envelope_slack"]), 0)

        self.assertGreaterEqual(Fraction(payload["aggregate_envelope_slack"]), 0)
        r2_row = next(row for row in payload["rows"] if row["modulus"] == 2)
        self.assertEqual(
            payload["r2_envelope_component"], r2_row["weighted_envelope_component"]
        )

    def test_dyadic_witness_is_exact_and_finite_only(self) -> None:
        """dyadic 见证必须记录精确块增量而不声称全局发散。"""
        payload = dyadic_envelope_growth_witness(32, 3)

        self.assertEqual(payload["dyadic_limits"], (8, 16, 32))
        self.assertEqual(payload["finite_growth_status"], "finite_growth_witnessed")
        self.assertEqual(payload["nonuniformity_obligation_status"], "open")
        for witness in payload["adjacent_witnesses"]:
            self.assertEqual(witness["block_identity_residual"], "0")
            self.assertGreaterEqual(
                Fraction(witness["increment"]), Fraction(witness["block_lower_bound"])
            )
            self.assertGreater(Fraction(witness["increment"]), 0)

    def test_contract_rejects_cycles_and_status_promotions(self) -> None:
        """合同必须拒绝循环来源、未声明来源与任何结论升级。"""
        with self.assertRaisesRegex(ValueError, "contract"):
            audit_elementary_envelope_barrier([], limit=12, dyadic_levels=2)

        forbidden = deepcopy(default_contract())
        forbidden["uses"] += ("RH",)
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_elementary_envelope_barrier(forbidden, limit=12, dyadic_levels=2)

        undeclared = deepcopy(default_contract())
        undeclared["claimed_uses"]["triangle_envelope"] = ("Mellin",)
        with self.assertRaisesRegex(ValueError, "禁止|未声明"):
            audit_elementary_envelope_barrier(undeclared, limit=12, dyadic_levels=2)

        promoted = deepcopy(default_contract())
        promoted["uniform_l2_upper_proved"] = True
        with self.assertRaisesRegex(ValueError, "uniform_l2_upper_proved"):
            audit_elementary_envelope_barrier(promoted, limit=12, dyadic_levels=2)

        closed = deepcopy(default_contract())
        closed["nonuniformity_obligation_status"] = "closed"
        with self.assertRaisesRegex(ValueError, "nonuniformity_obligation_status"):
            audit_elementary_envelope_barrier(closed, limit=12, dyadic_levels=2)

    def test_models_reject_invalid_limits_and_dyadic_levels(self) -> None:
        """有限截断和 dyadic 层数必须拒绝非内建整数与越界值。"""
        for limit in (True, 2, 12.0, "12"):
            with self.assertRaisesRegex(ValueError, "limit"):
                finite_elementary_envelope_model(limit)

        for levels in (True, 0, 2.0, "2", 4):
            with self.assertRaisesRegex(ValueError, "dyadic_levels"):
                dyadic_envelope_growth_witness(12, levels)

    def test_script_path_cli_writes_finite_only_certificate(self) -> None:
        """脚本 CLI 必须写出有限证书并显式保留开放义务。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "barrier.json"
            markdown_path = root / "barrier.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_w1_w2_elementary_envelope_barrier_audit.py",
                    "--limit",
                    "32",
                    "--dyadic-levels",
                    "3",
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
            self.assertEqual(payload["finite_inequality_status"], "verified_finite")
            self.assertEqual(payload["dyadic_limits"], [8, 16, 32])
            self.assertEqual(payload["nonuniformity_obligation_status"], "open")
            self.assertFalse(payload["rh_proved"])
            markdown = markdown_path.read_text(encoding="utf-8")
            self.assertIn("finite_growth_status=finite_growth_witnessed", markdown)
            self.assertIn("nonuniformity_obligation_status=open", markdown)
            self.assertIn("不证明", markdown)


if __name__ == "__main__":
    unittest.main()
