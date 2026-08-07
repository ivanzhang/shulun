#!/usr/bin/env python3
"""测试 MFAC 半素数局部自然性分解审计。"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_semiprime_local_naturality_factorization_audit import (  # noqa: E402
    build_candidate_families,
    audit_current_corpus,
    classify_candidate,
    find_minimal_collision_certificate,
    write_certificate,
)


DOCS = Path(__file__).resolve().parents[1] / "docs" / "monograph"


class MFACSemiprimeLocalNaturalityFactorizationAuditTest(unittest.TestCase):
    """验证最小 triad 的局部自然性候选分类。"""

    def test_known_families_are_not_actual_noncanonical_declarations(self) -> None:
        """五类既有候选均不能被记作 actual noncanonical declaration。"""
        results = {
            candidate["name"]: classify_candidate(candidate)
            for candidate in build_candidate_families(2, 3)
        }

        self.assertEqual(
            results["canonical_riw_buchstab_t1"]["classification"],
            "canonical_factorization",
        )
        self.assertEqual(
            results["global_mobius_lambda"]["classification"],
            "global_only_zero_sum",
        )
        self.assertEqual(
            results["de_colored_divisor_word"]["classification"],
            "global_only_transport",
        )
        self.assertEqual(
            results["lpf_phi_factor_word"]["classification"],
            "unsigned_or_canonical_support",
        )
        self.assertEqual(
            results["square_base_parity"]["classification"],
            "posterior_state_only",
        )
        self.assertTrue(
            all(
                not result["actual_noncanonical_declaration"]
                for result in results.values()
            )
        )

    def test_same_row_local_log_triad_is_rowwise_zero_sum(self) -> None:
        """同一行的局部对数三项只能给精确零和。"""
        candidate = {
            "name": "same-row-local-log",
            "pre_cauchy": True,
            "independent_of_downstream": True,
            "local_data_only": True,
            "prime_renaming_natural": True,
            "local_coefficient_law": True,
            "adds_primitive_arithmetic_functional": False,
            "row_kind": "same_row",
        }

        result = classify_candidate(candidate)

        self.assertEqual(result["classification"], "rowwise_cancellation")
        self.assertEqual(result["row_coefficient"], 0.0)
        self.assertFalse(result["actual_noncanonical_declaration"])

    def test_complete_synthetic_noncanonical_record_is_collision_certificate(self) -> None:
        """完整独立的非规范记录必须成为最小 collision 证书。"""
        candidate = {
            "name": "synthetic-independent-functional",
            "pre_cauchy": True,
            "independent_of_downstream": True,
            "local_data_only": False,
            "prime_renaming_natural": True,
            "local_coefficient_law": True,
            "adds_primitive_arithmetic_functional": True,
            "row_kind": "noncanonical",
            "origin_selector": "synthetic-origin",
            "actual_emitter_registered": True,
            "orientation": 1,
            "local_factor": 1.0,
            "exact_uv": [1, 1],
            "prepushforward_identity": "synthetic-independent-identity",
        }

        certificate = find_minimal_collision_certificate([candidate])

        self.assertIsNotNone(certificate)
        assert certificate is not None
        self.assertEqual(
            certificate["candidate_name"], "synthetic-independent-functional"
        )
        self.assertFalse(certificate["mathematical_nonexistence_proved"])

    def test_payment_dependent_candidate_is_rejected_before_collision(self) -> None:
        """读取 payment 的候选不能成为 pre-Cauchy collision。"""
        candidate = {
            "name": "payment-derived",
            "pre_cauchy": False,
            "independent_of_downstream": False,
        }

        result = classify_candidate(candidate)

        self.assertEqual(result["classification"], "downstream_dependent_rejected")
        self.assertFalse(result["actual_noncanonical_declaration"])

    def test_current_corpus_has_no_independent_semiprime_declaration_line(self) -> None:
        """当前语料尚未提交独立的半素数 declaration line。"""
        certificate = audit_current_corpus(DOCS)

        self.assertFalse(
            certificate["current_corpus_has_independent_semiprime_declaration_line"]
        )
        self.assertFalse(certificate["minimal_collision_certificate_present"])
        self.assertFalse(certificate["mathematical_nonexistence_proved"])
        self.assertFalse(certificate["rh_proved"])
        self.assertEqual(
            certificate["conditional_scope"], "explicit_local_naturality_model_only"
        )
        self.assertEqual(
            certificate["next_positive_gate"],
            "SemiprimeTriadDeclarationLineFromIndependentArithmeticIdentity",
        )

    def test_writer_states_conditional_scope_and_non_rh_boundary(self) -> None:
        """证书写出必须区分条件审计、语料缺口与 RH 未闭合。"""
        certificate = audit_current_corpus(DOCS)
        with tempfile.TemporaryDirectory() as directory:
            json_path = Path(directory) / "certificate.json"
            markdown_path = Path(directory) / "certificate.md"
            write_certificate(certificate, json_path, markdown_path)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            markdown = markdown_path.read_text(encoding="utf-8")

        self.assertFalse(
            payload["current_corpus_has_independent_semiprime_declaration_line"]
        )
        self.assertIn("仅在显式局部自然性模型内", markdown)
        self.assertIn("不表示数学上不存在", markdown)
        self.assertIn("rh_proved=false", markdown)
        self.assertIn("row_column_unconditional_closed=false", markdown)


if __name__ == "__main__":
    unittest.main()
