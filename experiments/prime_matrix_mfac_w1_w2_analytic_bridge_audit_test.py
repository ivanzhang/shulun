"""测试 MFAC W1→W2 解析桥合同审计。"""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_w1_w2_analytic_bridge_audit import (
    REQUIRED_LEMMAS,
    audit_w1_w2_analytic_bridge,
    default_contract,
)


class MFACW1W2AnalyticBridgeAuditTest(unittest.TestCase):
    """验证 W1→W2 只登记外部解析证明包。"""

    def test_valid_contract_registers_chain_without_proving_bridge_or_rh(self) -> None:
        """完整合同只能登记条件链，不能升级 Chebyshev 桥或 RH。"""
        payload = audit_w1_w2_analytic_bridge(default_contract())

        self.assertEqual(payload["w1_to_w2_status"], "assumption_chain_registered")
        self.assertEqual(payload["chebyshev_energy_bridge_status"], "unproved")
        self.assertFalse(payload["rh_proved"])

    def test_contract_rejects_missing_lemmas_nonuniformity_cycles_and_rh_promotion(
        self,
    ) -> None:
        """缺失引理、非统一常数和各种循环来源都必须被拒绝。"""
        base = default_contract()
        for field in REQUIRED_LEMMAS:
            broken = deepcopy(base)
            broken[field] = False
            with self.assertRaisesRegex(ValueError, field):
                audit_w1_w2_analytic_bridge(broken)

        nonuniform = deepcopy(base)
        nonuniform["uniformity_variable"] = "scale"
        with self.assertRaisesRegex(ValueError, "uniformity_variable"):
            audit_w1_w2_analytic_bridge(nonuniform)

        for source in ("RH", "Mellin", "Chebyshev_error", "finite_profile"):
            cyclic = deepcopy(base)
            cyclic["uses"] += (source,)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_w1_w2_analytic_bridge(cyclic)

        claimed_cycle = deepcopy(base)
        claimed_cycle["claimed_bridge_uses"] += ("Mellin",)
        with self.assertRaisesRegex(ValueError, "禁止"):
            audit_w1_w2_analytic_bridge(claimed_cycle)

        promoted = deepcopy(base)
        promoted["rh_proved"] = True
        with self.assertRaisesRegex(ValueError, "rh_proved"):
            audit_w1_w2_analytic_bridge(promoted)

    def test_script_path_cli_writes_non_proof_certificate(self) -> None:
        """脚本路径 CLI 必须写出明确保持未证明边界的证书。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "bridge.json"
            markdown_path = root / "bridge.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_w1_w2_analytic_bridge_audit.py",
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
            self.assertEqual(
                payload["chebyshev_energy_bridge_status"], "unproved"
            )
            self.assertFalse(payload["rh_proved"])
            markdown = markdown_path.read_text(encoding="utf-8")
            self.assertIn("chebyshev_energy_bridge_status=unproved", markdown)
            self.assertIn("不证明", markdown)


if __name__ == "__main__":
    unittest.main()
