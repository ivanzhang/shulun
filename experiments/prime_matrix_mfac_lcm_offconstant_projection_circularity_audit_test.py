#!/usr/bin/env python3
"""测试 MFAC LCM 去常数投影循环审计。"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_lcm_offconstant_projection_circularity_audit import (  # noqa: E402
    audit_direct_projection_contract,
    direct_projection_data,
    write_certificate,
)


class MFACLCMOffConstantProjectionCircularityAuditTest(unittest.TestCase):
    """验证实际整数直接秩一投影的循环边界。"""

    def test_actual_lcm_projection_reads_chebyshev_error(self) -> None:
        """实际整数投影读数在有限精度下等于 Chebyshev 误差。"""
        data = direct_projection_data(limit=30, alpha=0.0)

        self.assertTrue(
            math.isclose(
                data["g_e1_inner_product"],
                data["chebyshev_error"],
                rel_tol=1e-12,
                abs_tol=1e-12,
            )
        )
        self.assertEqual(data["e1_norm_squared"], 30)
        self.assertTrue(
            math.isclose(
                data["actual_defect"],
                data["theoretical_defect"],
                rel_tol=1e-12,
                abs_tol=1e-12,
            )
        )

    def test_unique_orthogonal_alpha_cancels_direct_defect(self) -> None:
        """唯一正交系数恰为目标误差归一化值，直接模板因此循环。"""
        uncentered = direct_projection_data(limit=30, alpha=0.0)
        alpha = uncentered["unique_orthogonal_alpha"]
        centered = direct_projection_data(limit=30, alpha=alpha)

        self.assertTrue(
            math.isclose(
                centered["actual_defect"],
                0.0,
                rel_tol=1e-12,
                abs_tol=1e-12,
            )
        )
        self.assertTrue(
            math.isclose(
                alpha,
                uncentered["chebyshev_error"] / 30,
                rel_tol=1e-12,
                abs_tol=1e-12,
            )
        )

    def test_parameterized_alpha_matches_theoretical_defect(self) -> None:
        """任意有限候选系数的实际投影缺陷符合精确缺陷公式。"""
        for alpha in (-2.0, 0.0, 0.5, 3.0):
            with self.subTest(alpha=alpha):
                data = direct_projection_data(limit=30, alpha=alpha)
                self.assertTrue(
                    math.isclose(
                        data["actual_defect"],
                        data["theoretical_defect"],
                        rel_tol=1e-12,
                        abs_tol=1e-12,
                    )
                )

    def test_target_dependent_alpha_is_rejected_as_directly_circular(self) -> None:
        """读取 psi(X)-X 的直接投影系数必须被分类为循环模板。"""
        result = audit_direct_projection_contract({"alpha_uses": ("psi(X)-X",)})

        self.assertEqual(
            result["classification"],
            "direct_e1_projection_uses_target_or_forbidden_analytic_input",
        )

    def test_independent_named_alpha_remains_unverified(self) -> None:
        """未读取目标的命名输入不能被虚构为已经独立构造。"""
        result = audit_direct_projection_contract(
            {"alpha_uses": ("independent_arithmetic_name",)}
        )

        self.assertEqual(
            result["classification"],
            "direct_e1_projection_independence_unverified",
        )


if __name__ == "__main__":
    unittest.main()
