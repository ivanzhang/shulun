#!/usr/bin/env python3
"""MFAC registration 与哈希边界审计测试。"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent))

from prime_matrix_mfac_registration_hash_audit import (  # noqa: E402
    DEFAULT_PATHS,
    audit_registration_evidence,
    complete_registration_fixture,
)


class MFACRegistrationHashAuditTest(unittest.TestCase):
    """验证 hash 容器字段不能代替 actual emitter registration。"""

    def test_current_hashes_do_not_recover_registration(self) -> None:
        """当前语料不含 registration 三元组且 source table 未构造。"""
        certificate = audit_registration_evidence(DEFAULT_PATHS)

        self.assertFalse(certificate["hash_contains_registration_fields"])
        self.assertFalse(certificate["actual_source_table_constructed"])
        self.assertFalse(certificate["registration_recoverable_from_hash"])
        self.assertEqual(certificate["earliest_missing_registration_field"], "emitter_id")
        self.assertFalse(certificate["downstream_recovery_used"])

    def test_complete_explicit_registration_fixture_passes(self) -> None:
        """显式前向 registration 三元组与源表同时存在时允许通过。"""
        with tempfile.TemporaryDirectory() as directory:
            certificate = audit_registration_evidence(
                complete_registration_fixture(Path(directory))
            )

        self.assertTrue(certificate["hash_contains_registration_fields"])
        self.assertTrue(certificate["actual_source_table_constructed"])
        self.assertTrue(certificate["registration_recoverable_from_hash"])
        self.assertIsNone(certificate["earliest_missing_registration_field"])
        self.assertFalse(certificate["downstream_recovery_used"])

    def test_missing_same_unit_certificate_blocks_registration(self) -> None:
        """缺失同 formal-unit 证书时不得以 hash 代替 registration。"""
        with tempfile.TemporaryDirectory() as directory:
            paths = complete_registration_fixture(Path(directory))
            payload = json.loads(paths["manifest"].read_text(encoding="utf-8"))
            del payload["registration"]["same_formal_unit_certificate"]
            paths["manifest"].write_text(
                json.dumps(payload, ensure_ascii=False), encoding="utf-8"
            )
            certificate = audit_registration_evidence(paths)

        self.assertFalse(certificate["registration_recoverable_from_hash"])
        self.assertEqual(
            certificate["earliest_missing_registration_field"],
            "same_formal_unit_certificate",
        )

    def test_payment_dependent_registration_is_rejected(self) -> None:
        """读取 payment 的 registration 是后验恢复，必须拒绝。"""
        with tempfile.TemporaryDirectory() as directory:
            paths = complete_registration_fixture(Path(directory))
            payload = json.loads(paths["manifest"].read_text(encoding="utf-8"))
            payload["constructor"]["dependencies"].append("payment")
            paths["manifest"].write_text(
                json.dumps(payload, ensure_ascii=False), encoding="utf-8"
            )
            certificate = audit_registration_evidence(paths)

        self.assertTrue(certificate["downstream_recovery_used"])
        self.assertFalse(certificate["registration_recoverable_from_hash"])


if __name__ == "__main__":
    unittest.main()
