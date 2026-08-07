#!/usr/bin/env python3
"""测试 MFAC 实际 LCM Gram 能量审计。"""

from __future__ import annotations

import itertools
import math
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_actual_lcm_gram_energy_audit import (  # noqa: E402
    audit_centering_contract,
    chebyshev_increment_energy,
    lambda_square_energy,
    lcm_gram_entry,
    lcm_gram_quadratic_form,
    lcm_mobius_energy,
    mobius,
    ordinary_cauchy_projection_bound,
    six_multiple_non_prime_power_witnesses,
    von_mangoldt,
    write_certificate,
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

    def test_quadratic_form_exhaustively_audits_small_bounded_integer_vectors(
        self,
    ) -> None:
        """有限穷举 625 个小整数向量，审计 Gram 恒等式及非负性。"""
        limit = 12
        divisors = (1, 2, 3, 6)
        coefficient_alphabet = (-2, -1, 0, 1, 2)

        for weights in itertools.product(coefficient_alphabet, repeat=len(divisors)):
            with self.subTest(weights=weights):
                coefficients = dict(zip(divisors, weights))
                expected = sum(
                    (
                        sum(
                            weight
                            for divisor, weight in coefficients.items()
                            if number % divisor == 0
                        )
                    )
                    ** 2
                    for number in range(1, limit + 1)
                )
                result = lcm_gram_quadratic_form(limit, coefficients)

                self.assertEqual(result, expected)
                self.assertGreaterEqual(result, 0)

    def test_quadratic_form_rejects_nonfinite_coefficients(self) -> None:
        """有限实 Gram 二次型拒绝非有限系数。"""
        for coefficient in (math.nan, math.inf):
            with self.subTest(coefficient=coefficient):
                with self.assertRaises(ValueError):
                    lcm_gram_quadratic_form(24, {1: coefficient})

    def test_quadratic_form_rejects_overflowing_products(self) -> None:
        """有限系数若使 Gram 乘积溢出也必须受控拒绝。"""
        with self.assertRaises(ValueError):
            lcm_gram_quadratic_form(1, {1: 1e308})

    def test_quadratic_form_keeps_finite_strong_cancellation(self) -> None:
        """有限强消去的 Gram 二次型保持有限而不被误拒绝。"""
        result = lcm_gram_quadratic_form(100, {1: 1e153, 2: -1e153})

        self.assertTrue(math.isfinite(result))

    def test_quadratic_form_rejects_non_numeric_contract_weights(self) -> None:
        """有限实系数合同只接受非布尔的内建 int 或 float。"""
        for coefficient in (True, "1.0", Decimal("1.0")):
            with self.subTest(coefficient=coefficient):
                with self.assertRaises(ValueError):
                    lcm_gram_quadratic_form(24, {1: coefficient})

    def test_mobius_lcm_energy_recovers_lambda_square_energy(self) -> None:
        """有限精度数值验证实数域中的 Möbius-Lambda 能量恒等式。"""
        self.assertTrue(
            math.isclose(
                lcm_mobius_energy(60),
                lambda_square_energy(60),
                rel_tol=1e-12,
                abs_tol=1e-12,
            )
        )

    def test_mobius_point_values_and_invalid_inputs(self) -> None:
        """Möbius 点值及非正和布尔输入均遵守有限整数合同。"""
        for value, expected in ((1, 1), (4, 0), (12, 0), (30, -1)):
            with self.subTest(value=value):
                self.assertEqual(mobius(value), expected)
        for value in (0, -1, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    mobius(value)

    def test_von_mangoldt_point_values_and_invalid_inputs(self) -> None:
        """von Mangoldt 点值及非正和布尔输入均遵守有限整数合同。"""
        for value, expected in (
            (1, 0.0),
            (8, math.log(2)),
            (12, 0.0),
            (49, math.log(7)),
            (97, math.log(97)),
        ):
            with self.subTest(value=value):
                self.assertTrue(math.isclose(von_mangoldt(value), expected))
        for value in (0, -1, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    von_mangoldt(value)

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

    def test_centering_contract_requires_iterable_string_uses(self) -> None:
        """中心化合同的 uses 必须为字符串 iterable，而不能是裸字符串。"""
        for uses in ("psi(X)", 1, (1,)):
            with self.subTest(uses=uses):
                with self.assertRaises(ValueError):
                    audit_centering_contract({"uses": uses})

        for uses in (("local_input",), ["local_input"], {"local_input"}):
            with self.subTest(uses=uses):
                result = audit_centering_contract({"uses": uses})
                self.assertEqual(
                    result["classification"],
                    "centering_input_not_rejected_by_forbidden_input_audit",
                )

    def test_certificate_writer_is_task_three_placeholder(self) -> None:
        """证书写出 API 在任务三前稳定保持占位错误。"""
        with tempfile.TemporaryDirectory() as temporary_directory:
            with self.assertRaisesRegex(
                NotImplementedError, "证书写出将在任务三实现"
            ):
                write_certificate(Path(temporary_directory), 60)


if __name__ == "__main__":
    unittest.main()
