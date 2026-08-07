#!/usr/bin/env python3
"""测试 MFAC Mellin 前非循环去常数强制见证。"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_noncircular_actual_offconstant_coercive_witness_audit import (  # noqa: E402
    actual_offconstant_coercive_witness_data,
)


class BuiltinIntSubclass(int):
    """用于验证输入必须是内建整数类型。"""


class BuiltinFloatSubclass(float):
    """用于验证输入必须是内建浮点类型。"""


class MFACNoncircularActualOffconstantCoerciveWitnessAuditTest(unittest.TestCase):
    """验证实际 LCM Gram 的一维去常数强制见证。"""

    def test_actual_witness_is_exactly_offconstant_and_positive(self) -> None:
        """见证精确正交于常数，且能量满足强制下界。"""
        for limit, numerator, denominator in ((2, 1, 2), (3, 2, 3), (60, 15, 1)):
            with self.subTest(limit=limit):
                data = actual_offconstant_coercive_witness_data(limit)

                self.assertEqual(data["constant_orthogonality_exact_numerator"], 0)
                self.assertEqual(data["energy_exact_numerator"], numerator)
                self.assertEqual(data["energy_exact_denominator"], denominator)
                self.assertGreater(data["energy"], 0.0)
                self.assertGreaterEqual(
                    data["energy"], data["coercivity_lower_bound"]
                )

    def test_witness_uses_only_actual_lcm_gram_entries(self) -> None:
        """见证只使用实际 LCM Gram 条目且在 Mellin 前构造。"""
        data = actual_offconstant_coercive_witness_data(5)

        self.assertEqual(data["coefficient_source"], "K_X(1,2)/K_X(1,1)")
        self.assertEqual(data["coefficient_exact_numerator"], 2)
        self.assertEqual(data["coefficient_exact_denominator"], 5)
        self.assertTrue(data["witness_constructed_before_mellin"])
        self.assertFalse(data["uses_target_error"])
        self.assertFalse(data["uses_mellin_input"])

    def test_scalar_direction_obeys_declared_coercivity(self) -> None:
        """缩放方向的能量和强制下界都按平方缩放。"""
        data = actual_offconstant_coercive_witness_data(3, scalar=-3)

        self.assertTrue(math.isclose(data["scaled_energy"], 6.0, abs_tol=1e-12))
        self.assertTrue(
            math.isclose(
                data["scaled_coercivity_lower_bound"], 6.0, abs_tol=1e-12
            )
        )

    def test_invalid_limits_and_scalars_are_rejected(self) -> None:
        """限制与缩放因子必须满足内建有限数值合同。"""
        for limit in (True, BuiltinIntSubclass(2), 1, 2.0, "2"):
            with self.subTest(limit=limit):
                with self.assertRaises(ValueError):
                    actual_offconstant_coercive_witness_data(limit)

        for scalar in (
            True,
            BuiltinIntSubclass(1),
            BuiltinFloatSubclass(1.0),
            "1",
            float("inf"),
            float("nan"),
        ):
            with self.subTest(scalar=scalar):
                with self.assertRaises(ValueError):
                    actual_offconstant_coercive_witness_data(2, scalar=scalar)


if __name__ == "__main__":
    unittest.main()
