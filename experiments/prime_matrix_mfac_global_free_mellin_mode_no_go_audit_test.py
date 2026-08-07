#!/usr/bin/env python3
"""测试 MFAC 全局自由 Mellin 增长模反模型审计。"""

from __future__ import annotations

import json
import math
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_global_free_mellin_mode_no_go_audit import (  # noqa: E402
    FreeMonoidModel,
    audit_divisor_lattice_identity,
    audit_current_corpus,
    classify_contraction_contract,
    complete_synthetic_contraction_contract,
    normalized_mellin_mode,
    positivity_threshold,
    target_theta_derivative,
    write_certificate,
)


ROOT = Path(__file__).resolve().parents[1]


class MFACGlobalFreeMellinModeNoGoAuditTest(unittest.TestCase):
    """验证自由模型保留交替恒等式而非实际 RH 输入。"""

    def test_free_monoid_preserves_lambda_negative_mu_convolution_log(self) -> None:
        """有限自由单子逐点满足精确 divisor-lattice 恒等式。"""
        model = FreeMonoidModel({"a": 2.0, "b": 3.0, "c": 5.0})

        certificate = audit_divisor_lattice_identity(model, bound=30.0)

        self.assertTrue(certificate["identity_holds"])
        self.assertGreater(certificate["element_count"], 3)
        self.assertIsNone(certificate["first_failure"])

    def test_squarefree_depth_controls_alternating_divisor_sign(self) -> None:
        """squarefree 素因子深度精确决定 Möbius 交替符号。"""
        model = FreeMonoidModel({"a": 2.0, "b": 3.0})

        self.assertEqual(model.mobius((1, 1)), 1)
        self.assertEqual(model.mobius((1, 0)), -1)
        self.assertEqual(model.mobius((0, 1)), -1)
        self.assertEqual(model.mobius((2, 0)), 0)

    def test_beta_above_half_has_unbounded_normalized_mellin_subsequence(self) -> None:
        """beta 大于二分之一时，峰值子序列在归一化后增长。"""
        beta = 0.75
        tau = 1.0
        epsilon = 0.1
        first = normalized_mellin_mode(2.0 * math.pi, beta, tau, epsilon)
        second = normalized_mellin_mode(4.0 * math.pi, beta, tau, epsilon)

        self.assertGreater(abs(second), abs(first))
        self.assertGreater(second / first, 1.0)

    def test_target_shell_derivative_is_positive_after_explicit_threshold(self) -> None:
        """连续 shell 轮廓在充分阈值后导数严格为正。"""
        threshold = positivity_threshold(beta=0.75, tau=3.0, epsilon=0.1)

        self.assertGreater(threshold, 0.0)
        self.assertGreater(
            target_theta_derivative(threshold * 2.0, 0.75, 3.0, 0.1), 0.0
        )

    def test_free_model_is_rejected_without_actual_integer_embedding(self) -> None:
        """缺少实际整数嵌入的自由模型不能称作 RH 攻击。"""
        result = classify_contraction_contract(
            {
                "fixed_actual_integer_embedding": False,
                "fixed_actual_chebyshev_measure": False,
            }
        )

        self.assertEqual(
            result["classification"], "free_model_not_actual_integer_rh_attack"
        )
        self.assertFalse(result["actual_chebyshev_mellin_contraction_present"])

    def test_complete_synthetic_contraction_contract_is_not_actual_proof(self) -> None:
        """完整 synthetic 合同只验证分类器，不构成实际收缩证明。"""
        result = classify_contraction_contract(complete_synthetic_contraction_contract())

        self.assertEqual(
            result["classification"], "synthetic_complete_contraction_contract"
        )
        self.assertFalse(result["actual_chebyshev_mellin_contraction_present"])
        self.assertFalse(result["rh_proved"])

    def test_current_corpus_has_no_actual_chebyshev_mellin_contraction(self) -> None:
        """当前语料没有实际整数上的 Mellin 收缩律。"""
        certificate = audit_current_corpus(ROOT)

        self.assertTrue(certificate["exact_divisor_lattice_identity_available"])
        self.assertTrue(certificate["free_mellin_growth_countermodel_constructed"])
        self.assertFalse(certificate["alternation_only_implies_sqrt_cancellation"])
        self.assertFalse(certificate["actual_chebyshev_mellin_contraction_present"])
        self.assertEqual(
            certificate["next_positive_gate"],
            "ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula",
        )
        self.assertFalse(certificate["rh_proved"])

    def test_writer_keeps_countermodel_distinct_from_rh_counterexample(self) -> None:
        """证书必须把自由增长轮廓与实际素数/RH 反例严格分开。"""
        certificate = audit_current_corpus(ROOT)
        with tempfile.TemporaryDirectory() as directory:
            json_path = Path(directory) / "certificate.json"
            markdown_path = Path(directory) / "certificate.md"
            write_certificate(certificate, json_path, markdown_path)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            markdown = markdown_path.read_text(encoding="utf-8")

        self.assertFalse(payload["actual_chebyshev_mellin_contraction_present"])
        self.assertIn("不是自然数素数的反例", markdown)
        self.assertIn("不对应实际 zeta 零点", markdown)
        self.assertIn("rh_proved=false", markdown)
        self.assertIn("row_column_unconditional_closed=false", markdown)


if __name__ == "__main__":
    unittest.main()
