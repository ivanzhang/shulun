"""测试 MFAC W1→W2 双线性核对角—非对角抵消审计器。"""

import unittest
from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from experiments.prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit import (
    audit_bilinear_kernel_cancellation,
    default_contract,
    finite_bilinear_kernel_model,
)


class MFACW1W2BilinearKernelCancellationAuditTest(unittest.TestCase):
    """验证有限核审计不提升全局解析结论。"""

    def test_valid_contract_keeps_uniform_conclusions_open(self) -> None:
        """合法合同只能报告有限核，不得关闭统一性义务。"""
        payload = audit_bilinear_kernel_cancellation(default_contract(), limit=12)

        self.assertEqual(payload["finite_kernel_identity_status"], "verified_finite")
        self.assertEqual(payload["finite_gram_positivity_status"], "verified_finite")
        self.assertEqual(payload["diagonal_cancellation_obligation_status"], "open")
        self.assertEqual(payload["coprime_restricted_tail_bound_status"], "open")
        self.assertEqual(payload["w1_to_w2_status"], "unproved")
        self.assertFalse(payload["rh_proved"])

    def test_model_matches_divisor_kernel_gram_and_diagonal_split(self) -> None:
        """三种有限能量表示和对角分解必须精确一致。"""
        payload = finite_bilinear_kernel_model(12)
        self.assertEqual(payload["candidate_indices"], tuple(range(2, 12)))
        self.assertEqual(payload["divisor_kernel_residual"], "0")
        self.assertEqual(payload["kernel_gram_residual"], "0")
        self.assertEqual(payload["diagonal_offdiagonal_residual"], "0")
        self.assertGreaterEqual(Fraction(payload["gram_energy"]), 0)
        self.assertEqual(payload["offdiagonal_energy"], "-277/450")
        self.assertEqual(payload["finite_cancellation_status"], "finite_cancellation_witnessed")
        self.assertEqual(payload["diagonal_cancellation_obligation_status"], "open")

    def test_contract_rejects_unallowed_sources_extra_claims_and_promotions(self) -> None:
        """合同必须拒绝来源绕过、伪造抵消和证明结论。"""
        unknown = deepcopy(default_contract())
        unknown["uses"] += ("unregistered_source",)
        with self.assertRaisesRegex(ValueError, "未允许"):
            audit_bilinear_kernel_cancellation(unknown, limit=12)

        extra = deepcopy(default_contract())
        extra["claimed_uses"]["hidden"] = ("Mellin",)
        with self.assertRaisesRegex(ValueError, "claimed_uses"):
            audit_bilinear_kernel_cancellation(extra, limit=12)

        forged = deepcopy(default_contract())
        forged["offdiagonal_cancellation_lemma"] = True
        with self.assertRaisesRegex(ValueError, "offdiagonal_cancellation_lemma"):
            audit_bilinear_kernel_cancellation(forged, limit=12)

        promoted = deepcopy(default_contract())
        promoted["uniform_l2_upper_proved"] = True
        with self.assertRaisesRegex(ValueError, "uniform_l2_upper_proved"):
            audit_bilinear_kernel_cancellation(promoted, limit=12)

    def test_models_reject_invalid_limits(self) -> None:
        """有限模型必须拒绝非法截断。"""
        for limit in (True, 2, 12.0, "12"):
            with self.assertRaisesRegex(ValueError, "limit"):
                finite_bilinear_kernel_model(limit)

    def test_script_path_cli_writes_finite_only_certificate(self) -> None:
        """CLI 必须写出有限证书且保持统一性义务开放。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "kernel.json"
            markdown_path = root / "kernel.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_w1_w2_bilinear_kernel_cancellation_audit.py",
                    "--limit", "12", "--json-out", str(json_path),
                    "--markdown-out", str(markdown_path),
                ], cwd=Path.cwd(), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["offdiagonal_energy"], "-277/450")
            self.assertEqual(payload["diagonal_cancellation_obligation_status"], "open")
            self.assertFalse(payload["rh_proved"])
            markdown = markdown_path.read_text(encoding="utf-8")
            self.assertIn("finite_kernel_identity_status=verified_finite", markdown)
            self.assertIn("不证明统一 L² 上界", markdown)


if __name__ == "__main__":
    unittest.main()
