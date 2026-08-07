#!/usr/bin/env python3
"""MFAC-1B 双色除数字词传输审计测试。

用法示例：
  python3 experiments/prime_matrix_mfac_colored_divisor_word_transport_audit_test.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_colored_divisor_word_transport_audit import (  # noqa: E402
    append_rough_factor,
    build_certificate,
    build_colored_record,
    reconstruct_source_pair,
)


class MFACColoredDivisorWordTransportTest(unittest.TestCase):
    """验证完整 divisor-history 的逐项算术传输。"""

    def test_colored_word_reconstructs_each_nonzero_source_pair(self) -> None:
        """完整 D/E 着色必须精确恢复原 divisor 与补因子。"""
        record = build_colored_record(n=12, divisor=6)
        self.assertEqual(record["owner_p"], 2)
        self.assertEqual(record["divisor"], 6)
        self.assertEqual(reconstruct_source_pair(record), (6, 2))

    def test_append_q_has_exact_d_and_e_branches(self) -> None:
        """新粗辅因子必须给出独立的 D/E 精确 child records。"""
        record = build_colored_record(n=6, divisor=3)
        branches = append_rough_factor(record, 5)
        self.assertEqual(branches["E"]["divisor"], 3)
        self.assertEqual(branches["D"]["divisor"], 15)
        self.assertEqual(branches["D"]["mu_d"], 1)

    def test_repeated_d_color_is_explicit_zero_mobius_branch(self) -> None:
        """重复把同一素数染为 D 色必须显式进入零 Möbius 分支。"""
        record = build_colored_record(n=6, divisor=3)
        branches = append_rough_factor(record, 3)
        self.assertIsNone(branches["D"])
        self.assertEqual(branches["D_return_tag"], "zero_mobius_repeated_divisor_prime")

    def test_certificate_preserves_all_nonzero_mobius_payloads(self) -> None:
        """有限证书必须验证精确传输而不得越界宣称 primitive-unit 绑定。"""
        certificate = build_certificate(120)
        self.assertTrue(certificate["record_reconstruction_verified"])
        self.assertTrue(certificate["one_step_transport_verified"])
        self.assertTrue(certificate["global_payload_conservation_verified"])
        self.assertFalse(certificate["actual_primitive_unit_binding_constructed"])
        self.assertFalse(certificate["mfac_1a_general_transport_constructed"])


if __name__ == "__main__":
    unittest.main()
