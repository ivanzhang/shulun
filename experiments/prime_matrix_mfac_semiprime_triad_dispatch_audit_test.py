#!/usr/bin/env python3
"""MFAC 半素数三项 dispatch 审计测试。"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_semiprime_triad_dispatch_audit import (  # noqa: E402
    audit_triad_dispatch,
    build_semiprime_triad,
    complete_synthetic_dispatch,
    same_row_zero_sum_dispatch,
)


class MFACSemiprimeTriadDispatchAuditTest(unittest.TestCase):
    """验证半素数三项不能被无证据地升级为 actual dispatch。"""

    def test_offdiagonal_triad_has_exact_zero_global_payload(self) -> None:
        """offdiagonal 半素数的三项全局 payload 必须精确相消。"""
        triad = build_semiprime_triad(2, 3)

        self.assertEqual(
            [(row["divisor"], row["cofactor"]) for row in triad],
            [(2, 3), (3, 2), (6, 1)],
        )
        self.assertTrue(
            math.isclose(
                sum(row["global_payload"] for row in triad), 0.0, abs_tol=1e-12
            )
        )

    def test_same_row_synthetic_triad_is_zero_sum_collapse(self) -> None:
        """完整但同-row 的零和 triad 只能形成 canonical collapse。"""
        certificate = audit_triad_dispatch(same_row_zero_sum_dispatch())

        self.assertTrue(certificate["canonical_zero_sum_collapse"])
        self.assertFalse(certificate["actual_dispatch_present"])

    def test_complete_synthetic_dispatch_is_admissible(self) -> None:
        """完整前向 synthetic dispatch 证明判据不是恒为负。"""
        certificate = audit_triad_dispatch(complete_synthetic_dispatch())

        self.assertTrue(certificate["actual_dispatch_present"])
        self.assertFalse(certificate["canonical_zero_sum_collapse"])

    def test_payment_dependent_dispatch_is_rejected(self) -> None:
        """读取 payment 的 dispatch 不具有 pre-Cauchy 独立性。"""
        dispatch = complete_synthetic_dispatch()
        dispatch["entries"][0]["independent_of_downstream"] = False
        certificate = audit_triad_dispatch(dispatch)

        self.assertFalse(certificate["actual_dispatch_present"])
        self.assertIn(
            "independent_of_downstream",
            certificate["entries"][0]["missing_fields"],
        )


if __name__ == "__main__":
    unittest.main()
