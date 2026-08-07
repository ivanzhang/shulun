#!/usr/bin/env python3
"""测试 MFAC 实际 LCM Gram 能量审计。"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_actual_lcm_gram_energy_audit import (  # noqa: E402
    audit_centering_contract,
    chebyshev_increment_energy,
    lambda_square_energy,
    lcm_gram_entry,
    lcm_gram_quadratic_form,
    lcm_mobius_energy,
    ordinary_cauchy_projection_bound,
    six_multiple_non_prime_power_witnesses,
    write_certificate,  # noqa: F401 - 预先固定第三任务的证书 API 合同。
)


class MFACActualLCMGramEnergyAuditTest(unittest.TestCase):
    """验证实际整数上的 LCM Gram 核及其边界合同。"""

    def test_lcm_entry_is_actual_divisibility_overlap(self) -> None:
        """LCM Gram 元精确计数两个整除条件的公共倍数。"""
        self.assertEqual(lcm_gram_entry(30, 6, 10), 1)
        self.assertEqual(lcm_gram_entry(30, 4, 6), 2)

    def test_quadratic_form_equals_divisor_feature_square_sum(self) -> None:
        """Gram 二次型等于有限区间内除数特征和的平方和。"""
        coefficients = {1: 2.0, 2: -1.0, 3: 4.0, 6: -2.0}
        expected = sum(
            sum(
                weight
                for divisor, weight in coefficients.items()
                if number % divisor == 0
            )
            ** 2
            for number in range(1, 25)
        )

        self.assertAlmostEqual(lcm_gram_quadratic_form(24, coefficients), expected)

    def test_quadratic_form_rejects_nonfinite_coefficients(self) -> None:
        """有限实 Gram 二次型拒绝非有限系数。"""
        for coefficient in (math.nan, math.inf):
            with self.subTest(coefficient=coefficient):
                with self.assertRaises(ValueError):
                    lcm_gram_quadratic_form(24, {1: coefficient})

    def test_mobius_lcm_energy_recovers_lambda_square_energy(self) -> None:
        """Möbius 加权 LCM 能量精确恢复 Lambda 平方和。"""
        self.assertAlmostEqual(lcm_mobius_energy(60), lambda_square_energy(60))

    def test_increment_energy_has_ordinary_cauchy_projection_bound(self) -> None:
        """常数方向投影记录普通 Cauchy 界与实际增量能量。"""
        certificate = ordinary_cauchy_projection_bound(60)

        self.assertEqual(certificate["constant_direction_norm_squared"], 60)
        self.assertAlmostEqual(
            certificate["error_sum_squared"], certificate["chebyshev_error"] ** 2
        )
        self.assertLessEqual(
            certificate["error_sum_squared"], certificate["cauchy_upper_bound"]
        )
        self.assertGreater(chebyshev_increment_energy(60), 0.0)

    def test_six_multiples_are_not_prime_powers(self) -> None:
        """记录的六倍数见证均不是素数幂。"""
        self.assertEqual(
            six_multiple_non_prime_power_witnesses(30), (6, 12, 18, 24, 30)
        )

    def test_centering_contract_rejects_target_or_forbidden_input(self) -> None:
        """中心化合同不得读取待估目标或被禁止的解析输入。"""
        result = audit_centering_contract({"uses": ("psi(X)",)})

        self.assertEqual(
            result["classification"],
            "centered_kernel_uses_target_or_forbidden_analytic_input",
        )

    def test_centering_contract_rejects_non_mapping_input(self) -> None:
        """中心化合同仅接受可读取 uses 字段的 Mapping。"""
        for contract in (None, [], 1):
            with self.subTest(contract=contract):
                with self.assertRaises(ValueError):
                    audit_centering_contract(contract)


if __name__ == "__main__":
    unittest.main()
