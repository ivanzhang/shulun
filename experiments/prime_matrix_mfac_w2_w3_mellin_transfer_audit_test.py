"""测试 MFAC W2→W3 实际 Mellin 传递合同审计。"""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_w2_w3_mellin_transfer_audit import (
    REQUIRED_LEMMAS,
    audit_w2_w3_mellin_transfer,
    default_contract,
)


class MFACW2W3MellinTransferAuditTest(unittest.TestCase):
    """验证 W2→W3 只登记外部实际传递证明包。"""

    def test_valid_contract_only_registers_mellin_transfer_chain(self) -> None:
        """完整合同只能登记传递链，不能升级 W3 或 RH。"""
        payload = audit_w2_w3_mellin_transfer(default_contract())

        self.assertEqual(payload["w2_to_w3_status"], "assumption_chain_registered")
        self.assertEqual(
            payload["actual_mellin_half_plane_contraction_status"], "unproved"
        )
        self.assertEqual(payload["w3_spectral_contraction_status"], "unproved")
        self.assertFalse(payload["rh_proved"])

    def test_contract_rejects_empty_sources_cycles_bad_parameters_and_promoted_fields(
        self,
    ) -> None:
        """来源、引理、测度、参数和结论边界都必须严格验证。"""
        base = default_contract()
        empty_sources = deepcopy(base)
        empty_sources["uses"] = ()
        empty_sources["claimed_transfer_uses"] = ()
        with self.assertRaisesRegex(ValueError, "uses 不能为空"):
            audit_w2_w3_mellin_transfer(empty_sources)

        for field in REQUIRED_LEMMAS:
            broken = deepcopy(base)
            broken[field] = False
            with self.assertRaisesRegex(ValueError, field):
                audit_w2_w3_mellin_transfer(broken)

        for source in ("RH", "Mellin_contraction", "finite_profile"):
            cyclic = deepcopy(base)
            cyclic["claimed_transfer_uses"] += (source,)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_w2_w3_mellin_transfer(cyclic)

        for parameter in (0.5, 1.0, float("nan"), True):
            broken = deepcopy(base)
            broken["half_plane_parameter"] = parameter
            with self.assertRaisesRegex(ValueError, "half_plane_parameter"):
                audit_w2_w3_mellin_transfer(broken)

        wrong_measure = deepcopy(base)
        wrong_measure["mellin_measure"] = "dt_over_t"
        with self.assertRaisesRegex(ValueError, "mellin_measure"):
            audit_w2_w3_mellin_transfer(wrong_measure)

        promoted = deepcopy(base)
        promoted["w3_closed"] = False
        with self.assertRaisesRegex(ValueError, "目标结论"):
            audit_w2_w3_mellin_transfer(promoted)

    def test_script_path_cli_writes_non_proof_certificate(self) -> None:
        """脚本路径 CLI 必须写出明确保持 W3/RH 未证明的证书。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "transfer.json"
            markdown_path = root / "transfer.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_w2_w3_mellin_transfer_audit.py",
                    "--half-plane-parameter",
                    "0.75",
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
            self.assertEqual(payload["w3_spectral_contraction_status"], "unproved")
            self.assertFalse(payload["rh_proved"])
            markdown = markdown_path.read_text(encoding="utf-8")
            self.assertIn("w3_spectral_contraction_status=unproved", markdown)
            self.assertIn("不证明", markdown)


if __name__ == "__main__":
    unittest.main()
