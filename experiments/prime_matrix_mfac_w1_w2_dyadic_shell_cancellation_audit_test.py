"""测试 MFAC W1→W2 dyadic 壳抵消审计器。"""

import unittest
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

from experiments.prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit import (
    audit_dyadic_shell_cancellation,
    default_contract,
    finite_dyadic_shell_ledger,
)


class MFACW1W2DyadicShellCancellationAuditTest(unittest.TestCase):
    """验证壳账本不会提升解析义务。"""

    def test_valid_contract_keeps_all_shell_obligations_open(self) -> None:
        """合法合同只能登记有限壳，不得关闭解析义务。"""
        payload = audit_dyadic_shell_cancellation(default_contract(), limit=12)
        self.assertEqual(payload["finite_shell_ledger_status"], "verified_finite")
        self.assertEqual(payload["adjacent_shell_cancellation_obligation_status"], "open")
        self.assertEqual(payload["summable_residual_obligation_status"], "open")
        self.assertEqual(payload["far_shell_aggregation_obligation_status"], "open")
        self.assertEqual(payload["w1_to_w2_status"], "unproved")
        self.assertFalse(payload["rh_proved"])

    def test_finite_ledger_reassembles_kernel_and_marks_boundary_shell(self) -> None:
        """壳账本必须精确重组有限核并标记截断边界壳。"""
        payload = finite_dyadic_shell_ledger(12)
        self.assertEqual(payload["block_reassembly_residual"], "0")
        self.assertEqual(payload["near_far_reassembly_residual"], "0")
        self.assertEqual(payload["kernel_identity_residual"], "0")
        self.assertEqual(payload["shells"][-1]["start"], 8)
        self.assertEqual(payload["shells"][-1]["stop"], 12)
        self.assertTrue(payload["shells"][-1]["is_truncated"])

    def test_contract_rejects_promoted_shell_lemmas(self) -> None:
        """合同必须拒绝伪造壳抵消引理和循环来源。"""
        forged = deepcopy(default_contract())
        forged["adjacent_shell_cancellation_lemma"] = True
        with self.assertRaisesRegex(ValueError, "adjacent_shell_cancellation_lemma"):
            audit_dyadic_shell_cancellation(forged, 12)
        circular = deepcopy(default_contract())
        circular["uses"] += ("Mellin",)
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_dyadic_shell_cancellation(circular, 12)

    def test_cli_writes_open_shell_certificate(self) -> None:
        """CLI 必须写出有限壳证书并保留开放义务。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path, markdown_path = root / "shell.json", root / "shell.md"
            result = subprocess.run([
                sys.executable, "experiments/prime_matrix_mfac_w1_w2_dyadic_shell_cancellation_audit.py",
                "--limit", "12", "--json-out", str(json_path), "--markdown-out", str(markdown_path),
            ], cwd=Path.cwd(), capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["far_shell_aggregation_obligation_status"], "open")
            self.assertIn("不证明统一 L² 上界", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
