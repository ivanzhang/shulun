#!/usr/bin/env python3
"""MFAC 平方基 seed 与 primitive-binding 缺口审计测试。"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_square_base_seed_binding_audit import (  # noqa: E402
    build_certificate,
    square_base_active_source,
)


class MFACSquareBaseSeedBindingAuditTest(unittest.TestCase):
    """验证平方基的全局 seed 与未绑定边界。"""

    def test_square_base_has_unique_active_mobius_source(self) -> None:
        """p² 的唯一非零 payload source 必为 (d,e)=(p,p)。"""
        source = square_base_active_source(5)
        self.assertEqual((source["divisor"], source["cofactor"]), (5, 5))
        self.assertEqual(source["color_word"], ("D", "E"))
        self.assertTrue(math.isclose(source["payload"], math.log(5), abs_tol=1e-12))

    def test_certificate_keeps_actual_primitive_binding_open(self) -> None:
        """全局 square-base seed 不得被误报为 actual signed coefficient。"""
        certificate = build_certificate(29)
        self.assertTrue(certificate["global_square_base_seed_verified"])
        self.assertTrue(certificate["unique_active_source_verified"])
        self.assertFalse(certificate["actual_square_base_signed_coefficient_bound"])
        self.assertFalse(certificate["primitive_orientation_local_factor_law_bound"])


if __name__ == "__main__":
    unittest.main()
