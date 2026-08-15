"""测试 MFAC Euler–Gauss–Riemann 三层因子化审计。"""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_euler_gauss_riemann_factorization_audit import (
    audit_euler_gauss_riemann_factorization,
    default_mellin_contract,
)


class MFACEulerGaussRiemannFactorizationAuditTest(unittest.TestCase):
    """验证有限三层恒等式与未证明边界。"""

    def test_finite_factorization_matches_lambda_gram_and_continuous_correction(
        self,
    ) -> None:
        """Möbius 反演、LCM Gram 和离散校正必须在有限范围精确一致。"""
        audit = audit_euler_gauss_riemann_factorization(limit=30)

        self.assertEqual(audit["euler_inversion_mismatch_count"], 0)
        self.assertAlmostEqual(audit["gauss_gram_residual"], 0.0)
        self.assertAlmostEqual(audit["discrete_continuous_correction_residual"], 0.0)
        self.assertFalse(audit["rh_proved"])

    def test_mellin_contract_rejects_bad_domain_cycles_and_promoted_conclusions(
        self,
    ) -> None:
        """Mellin 公式只能登记在 Re(s)>1，且不得读取循环结论。"""
        base = default_mellin_contract()
        for real_part in (1.0, float("nan"), True):
            broken = deepcopy(base)
            broken["real_part"] = real_part
            with self.assertRaisesRegex(ValueError, "real_part"):
                audit_euler_gauss_riemann_factorization(12, broken)

        for source in ("RH", "Mellin_contraction", "finite_profile"):
            broken = deepcopy(base)
            broken["claimed_identity_uses"] += (source,)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_euler_gauss_riemann_factorization(12, broken)

        promoted = deepcopy(base)
        promoted["rh_proved"] = False
        with self.assertRaisesRegex(ValueError, "目标结论"):
            audit_euler_gauss_riemann_factorization(12, promoted)

    def test_script_path_cli_writes_open_gate_certificate(self) -> None:
        """脚本路径 CLI 必须保留跨尺度门与 RH 均未证明。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "factorization.json"
            markdown_path = root / "factorization.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_euler_gauss_riemann_factorization_audit.py",
                    "--limit",
                    "48",
                    "--json-out",
                    str(json_path),
                    "--markdown-out",
                    str(markdown_path),
                ],
                cwd=Path.cwd(),
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stderr)
            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["euler_inversion_mismatch_count"], 0)
            self.assertEqual(payload["cross_scale_prefix_coercivity_status"], "unproved")
            self.assertFalse(payload["rh_proved"])
            self.assertIn("不证明", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
