#!/usr/bin/env python3
"""MFAC-1A 粗辅因子 Möbius 带符号传输审计测试。

用法示例：
  python3 experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit_test.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit import (  # noqa: E402
    build_certificate,
    build_source_pairs,
    find_minimal_collisions,
    lpf_local_state,
    mobius_values,
    verify_lambda_identity,
)


class MFACRoughCofactorAuditTest(unittest.TestCase):
    """验证 MFAC-1A 审计的精确 source-pair 基础。"""

    def test_mobius_von_mangoldt_identity_for_small_range(self) -> None:
        """全局 Möbius 除数和在小范围逐点恢复 von Mangoldt 权重。"""
        mobius = mobius_values(30)
        for value in range(1, 31):
            self.assertTrue(verify_lambda_identity(value, mobius), value)

    def test_source_pairs_preserve_every_nonzero_mobius_divisor(self) -> None:
        """source pair 枚举不得丢失合数的非零 Möbius 除数。"""
        mobius = mobius_values(30)
        pairs = build_source_pairs(30, mobius)
        divisors_of_twelve = [pair["d"] for pair in pairs if pair["n"] == 12]
        self.assertEqual(divisors_of_twelve, [1, 2, 3, 6])

    def test_lpf_only_state_has_a_signed_payload_collision(self) -> None:
        """不含除数历史的 LPF-local 投影必须暴露带符号 payload 碰撞。"""
        mobius = mobius_values(30)
        pairs = build_source_pairs(30, mobius)
        state_to_payloads: dict[tuple[object, ...], set[tuple[object, ...]]] = {}
        for pair in pairs:
            state = lpf_local_state(pair, include_divisor_history=False)
            payload = (pair["mu_d"], pair["log_d_parts"])
            state_to_payloads.setdefault(state, set()).add(payload)
        self.assertTrue(any(len(payloads) > 1 for payloads in state_to_payloads.values()))

    def test_minimal_collision_keeps_recomputable_source_pairs(self) -> None:
        """最小见证必须保留可直接复算的两个 source pair。"""
        mobius = mobius_values(30)
        collisions = find_minimal_collisions(build_source_pairs(30, mobius))
        self.assertEqual(collisions[0]["members"][0]["d"], 3)
        self.assertEqual(collisions[0]["members"][1]["d"], 6)

    def test_certificate_reports_the_no_go_boundary_without_rh_claim(self) -> None:
        """证书必须把局部状态不足与未构造一般传输律同时写明。"""
        certificate = build_certificate(30)
        self.assertTrue(certificate["mobius_von_mangoldt_identity_verified"])
        self.assertTrue(certificate["source_pair_partition_verified"])
        self.assertTrue(certificate["lpf_local_state_collision_found"])
        self.assertTrue(certificate["divisor_history_augmentation_removes_payload_collision"])
        self.assertFalse(certificate["mfac_1a_constructed"])
        self.assertFalse(certificate["row_column_unconditional_closed"])


if __name__ == "__main__":
    unittest.main()
