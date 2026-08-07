#!/usr/bin/env python3
"""MFAC 取向来源 no-go 审计测试。"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_orientation_provenance_no_go_audit import (  # noqa: E402
    audit_candidate_sources,
    audit_orientation_provenance,
    complete_synthetic_source,
    mobius_parity_shadow_source,
)


DOCS = Path(__file__).resolve().parents[1] / "docs" / "monograph"


class MFACOrientationProvenanceNoGoAuditTest(unittest.TestCase):
    """验证取向来源必须在推前前完整登记。"""

    def test_current_corpus_has_no_admissible_orientation_source(self) -> None:
        """当前语料未提交 actual primitive orientation 的前向来源。"""
        certificate = audit_orientation_provenance(DOCS)

        self.assertFalse(certificate["admissible_orientation_source_present"])
        self.assertEqual(certificate["earliest_missing_forward_field"], "origin_selector")
        self.assertEqual(
            certificate["next_positive_gate"],
            "PrimitiveOrientationLocalFactorProductLawBeforePushforward",
        )
        self.assertFalse(certificate["mathematical_nonexistence_proved"])

    def test_complete_synthetic_source_is_admissible(self) -> None:
        """完整合成来源证明判据不是恒为负。"""
        certificate = audit_candidate_sources([complete_synthetic_source()])

        self.assertTrue(certificate["admissible_orientation_source_present"])
        self.assertTrue(certificate["candidate_sources"][0]["admissible"])
        self.assertEqual(certificate["candidate_sources"][0]["missing_fields"], [])

    def test_mobius_shadow_without_emitter_identity_is_rejected(self) -> None:
        """Möbius/parity 影子不能代替 actual emitter 的精确来源。"""
        certificate = audit_candidate_sources([mobius_parity_shadow_source()])

        self.assertFalse(certificate["admissible_orientation_source_present"])
        self.assertIn(
            "actual_emitter_registered",
            certificate["candidate_sources"][0]["missing_fields"],
        )

    def test_downstream_dependent_source_is_rejected(self) -> None:
        """读取下游数据的来源不满足 pre-Cauchy 独立性。"""
        source = complete_synthetic_source()
        source["independent_of_downstream"] = False
        certificate = audit_candidate_sources([source])

        self.assertFalse(certificate["admissible_orientation_source_present"])
        self.assertIn(
            "independent_of_downstream",
            certificate["candidate_sources"][0]["missing_fields"],
        )


if __name__ == "__main__":
    unittest.main()
