"""形式 Möbius--Lambda 与 Abel 恒等式的有限测试。

用法示例：
  python3 -m unittest experiments.prime_matrix_mfac_unconditional_w1_w2_log_saving_audit_test -v
"""

from __future__ import annotations

from fractions import Fraction
import unittest

from experiments.prime_matrix_mfac_unconditional_w1_w2_log_saving_audit import (
    abel_sum_by_parts,
    formal_mobius_lambda,
    formal_negative_mobius_log,
)


class MFACUnconditionalW1W2LogSavingAuditTest(unittest.TestCase):
    """验证有限形式对数系数恒等式，不涉及 W1、W2 或 RH。"""

    def test_mobius_lambda_matches_negative_mobius_log_through_64(self) -> None:
        """逐项有限检验 (μ*Λ)(n) = -μ(n) log n 的形式素数系数。"""
        for index in range(1, 65):
            self.assertEqual(
                formal_mobius_lambda(index),
                formal_negative_mobius_log(index),
                index,
            )

    def test_abel_sum_by_parts_has_zero_rational_residual(self) -> None:
        """有理夹具必须精确满足有限 Abel 求和恒等式。"""
        result = abel_sum_by_parts(
            {
                2: Fraction(3, 2),
                5: Fraction(-4, 3),
                9: Fraction(7, 5),
            },
            {
                2: Fraction(11, 7),
                5: Fraction(-2, 5),
                9: Fraction(13, 4),
            },
        )

        self.assertEqual(result["residual"], Fraction(0, 1))
        self.assertEqual(result["direct"], result["summation_by_parts"])

    def test_public_apis_reject_invalid_inputs(self) -> None:
        """公开接口必须拒绝布尔索引与非 Fraction 的 Abel 权重。"""
        with self.assertRaises(ValueError):
            formal_negative_mobius_log(True)
        with self.assertRaises(ValueError):
            formal_mobius_lambda(0)
        with self.assertRaises(ValueError):
            abel_sum_by_parts(
                {2: Fraction(1, 2)},
                {2: Fraction(1, 2), 3: Fraction(1, 3)},
            )
        with self.assertRaises(ValueError):
            abel_sum_by_parts({2: Fraction(1, 2)}, {2: 1})


if __name__ == "__main__":
    unittest.main()
