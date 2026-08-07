#!/usr/bin/env python3
"""MFAC 实际原子记录构造审计测试。"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_actual_record_constructor_audit import (  # noqa: E402
    audit_constructor_evidence,
    complete_manifest,
    write_certificate,
)


DOCS = Path(__file__).resolve().parents[1] / "docs" / "monograph"


class MFACActualRecordConstructorAuditTest(unittest.TestCase):
    """验证实际原子记录必须由非循环构造器显式发射。"""

    def test_current_corpus_has_no_actual_atomic_constructor(self) -> None:
        """现有路由闭合不能代替 witness 到 record 的构造。"""
        certificate = audit_constructor_evidence(DOCS)

        self.assertFalse(certificate["witness_to_record_constructor_present"])
        self.assertFalse(certificate["actual_noncanonical_atomic_record_present"])
        self.assertEqual(certificate["earliest_missing_field"], "origin_selector")
        self.assertFalse(certificate["branch_alphabet_domain_defined"])
        self.assertFalse(certificate["downstream_recovery_used"])

    def test_complete_synthetic_manifest_defines_branch_alphabet(self) -> None:
        """完整且前向的合成 manifest 证明判据并非恒为负。"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "complete.json"
            path.write_text(
                json.dumps(complete_manifest(), ensure_ascii=False), encoding="utf-8"
            )

            certificate = audit_constructor_evidence(Path(directory))

        self.assertTrue(certificate["witness_to_record_constructor_present"])
        self.assertTrue(certificate["actual_noncanonical_atomic_record_present"])
        self.assertTrue(certificate["branch_alphabet_domain_defined"])
        self.assertIsNone(certificate["earliest_missing_field"])
        self.assertFalse(certificate["downstream_recovery_used"])

    def test_manifest_using_payment_is_rejected(self) -> None:
        """读取 payment 的构造器属于后验恢复，不能定义原子来源。"""
        payload = complete_manifest()
        payload["constructor"]["dependencies"].append("payment")

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "downstream-leak.json"
            path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            certificate = audit_constructor_evidence(Path(directory))

        self.assertTrue(certificate["witness_to_record_constructor_present"])
        self.assertFalse(certificate["actual_noncanonical_atomic_record_present"])
        self.assertFalse(certificate["branch_alphabet_domain_defined"])
        self.assertTrue(certificate["downstream_recovery_used"])

    def test_certificate_writer_marks_corpus_gap_not_mathematical_impossibility(self) -> None:
        """证书必须把当前语料缺口与数学否定严格区分。"""
        certificate = audit_constructor_evidence(DOCS)

        with tempfile.TemporaryDirectory() as directory:
            json_out = Path(directory) / "certificate.json"
            markdown_out = Path(directory) / "certificate.md"
            write_certificate(certificate, json_out, markdown_out)
            markdown = markdown_out.read_text(encoding="utf-8")
            json_exists = json_out.exists()

        self.assertTrue(json_exists)
        self.assertIn("earliest_missing_field=origin_selector", markdown)
        self.assertIn("当前语料未提交", markdown)
        self.assertIn("不表示数学上不可能", markdown)


if __name__ == "__main__":
    unittest.main()
