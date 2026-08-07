#!/usr/bin/env python3
"""MFAC 半素数三项 dispatch 审计测试。"""

from __future__ import annotations

import json
import math
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_semiprime_triad_dispatch_audit import (  # noqa: E402
    audit_triad_dispatch,
    audit_current_corpus,
    build_semiprime_triad,
    complete_synthetic_dispatch,
    same_row_zero_sum_dispatch,
    write_certificate,
)


DOCS = Path(__file__).resolve().parents[1] / "docs" / "monograph"


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

    def test_current_corpus_reconstructs_triad_but_has_no_actual_dispatch(self) -> None:
        """当前语料只有 global triad，尚未登记 actual dispatch。"""
        certificate = audit_current_corpus(DOCS)

        self.assertTrue(certificate["global_triad_reconstructed"])
        self.assertFalse(certificate["actual_dispatch_present"])
        self.assertEqual(certificate["earliest_missing_field"], "origin_selector")
        self.assertFalse(certificate["canonical_zero_sum_collapse"])

    def test_writer_keeps_nonexistence_and_rh_boundary(self) -> None:
        """证书必须区分语料缺口、数学不存在性与 RH。"""
        certificate = audit_current_corpus(DOCS)
        with tempfile.TemporaryDirectory() as directory:
            json_out = Path(directory) / "certificate.json"
            markdown_out = Path(directory) / "certificate.md"
            write_certificate(certificate, json_out, markdown_out)
            payload = json.loads(json_out.read_text(encoding="utf-8"))
            markdown = markdown_out.read_text(encoding="utf-8")

        self.assertTrue(payload["global_triad_reconstructed"])
        self.assertIn("当前语料未提交", markdown)
        self.assertIn("不表示数学上不可能", markdown)
        self.assertIn("rh_proved=false", markdown)


if __name__ == "__main__":
    unittest.main()
