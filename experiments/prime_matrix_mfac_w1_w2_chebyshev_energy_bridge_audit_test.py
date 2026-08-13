"""验证 MFAC W1 到 W2 Chebyshev 能量桥合同。"""

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit import (
    audit_chebyshev_energy_bridge_contract,
)


class MFACW1W2ChebyshevEnergyBridgeAuditTest(unittest.TestCase):
    """验证 W1 到 W2 最小无条件能量桥合同。"""

    @staticmethod
    def valid_contract() -> dict[str, object]:
        """返回每个测试均可独立修改的最小合法合同。"""
        return {
            "uses": (
                "finite_gram_identity",
                "independent_kernel_registration",
            ),
            "absolute_constant": "exists_A_positive_independent_of_X_and_candidate",
            "large_scale_quantifier": "exists_X0_for_all_X_ge_X0",
            "gram_contract": {
                "coefficient_family": "pre_registered_actual_coefficients",
                "kernel": "pre_registered_nonnegative_gram_kernel",
                "interval_correspondence": "dyadic_X_to_2X",
                "constant_projection": "off_constant_projection",
                "nonnegative": True,
                "uses": ("finite_gram_identity",),
            },
            "error_contract": {
                "source": "independent_remainder_decomposition",
                "eta": 0.5,
                "absorption_target": "B(X)<=eta*G(X)",
                "uses": ("independent_remainder_decomposition",),
            },
            "claimed_bound_uses": ("finite_gram_identity",),
        }

    def test_valid_bridge_contract_stays_registered_and_unproved(self) -> None:
        """完整合同只能登记桥接义务，不能升级 W2 或 RH。"""
        audit = audit_chebyshev_energy_bridge_contract(self.valid_contract())
        self.assertEqual(
            audit["bridge_structure_status"], "registered_unproved_contract"
        )
        self.assertEqual(
            audit["error_absorption_status"], "absorption_obligation_open"
        )
        self.assertEqual(
            audit["w2_actual_chebyshev_energy_bridge_status"], "unproved"
        )
        self.assertFalse(audit["rh_proved"])

    def test_contract_rejects_forbidden_inputs_invalid_eta_and_target_cycle(self) -> None:
        """桥接不得读取目标/外部输入，也不得接受非法 eta 或目标结论字段。"""
        for location, forbidden in (
            ("uses", "Chebyshev_error"),
            ("gram_contract.uses", "Mellin"),
            ("error_contract.uses", "RH"),
            ("uses", "PNT"),
            ("uses", "Mertens_cancellation"),
        ):
            broken = deepcopy(self.valid_contract())
            if location == "uses":
                broken["uses"] = broken["uses"] + (forbidden,)
            elif location == "gram_contract.uses":
                broken["gram_contract"]["uses"] += (forbidden,)
            else:
                broken["error_contract"]["uses"] += (forbidden,)
            with self.assertRaisesRegex(ValueError, "禁止"):
                audit_chebyshev_energy_bridge_contract(broken)

        for eta in (-0.1, 1.0, float("nan"), True):
            broken = deepcopy(self.valid_contract())
            broken["error_contract"]["eta"] = eta
            with self.assertRaisesRegex(ValueError, "eta"):
                audit_chebyshev_energy_bridge_contract(broken)

        cyclic = deepcopy(self.valid_contract())
        cyclic["rh_proved"] = False
        with self.assertRaisesRegex(ValueError, "目标结论"):
            audit_chebyshev_energy_bridge_contract(cyclic)

    def test_contract_rejects_incomplete_gram_and_undeclared_bound_sources(self) -> None:
        """Gram 语义、非负性和界来源均须显式且有效。"""
        missing_kernel = deepcopy(self.valid_contract())
        missing_kernel["gram_contract"]["kernel"] = ""
        with self.assertRaisesRegex(ValueError, "gram_contract"):
            audit_chebyshev_energy_bridge_contract(missing_kernel)

        non_boolean_nonnegative = deepcopy(self.valid_contract())
        non_boolean_nonnegative["gram_contract"]["nonnegative"] = 1
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            audit_chebyshev_energy_bridge_contract(non_boolean_nonnegative)

        bare_error_uses = deepcopy(self.valid_contract())
        bare_error_uses["error_contract"]["uses"] = "remainder"
        with self.assertRaisesRegex(ValueError, "error_contract.uses"):
            audit_chebyshev_energy_bridge_contract(bare_error_uses)

        undeclared_source = deepcopy(self.valid_contract())
        undeclared_source["claimed_bound_uses"] = ("unregistered_source",)
        with self.assertRaisesRegex(ValueError, "未声明"):
            audit_chebyshev_energy_bridge_contract(undeclared_source)

    def test_certificate_and_cli_never_promote_bridge_to_w2_or_rh(self) -> None:
        """CLI 产物必须保留桥接、W2 和 RH 均未证明的边界。"""
        with TemporaryDirectory() as directory:
            root = Path(directory)
            json_path = root / "bridge.json"
            markdown_path = root / "bridge.md"
            result = subprocess.run(
                [
                    sys.executable,
                    "experiments/prime_matrix_mfac_w1_w2_chebyshev_energy_bridge_audit.py",
                    "--eta",
                    "0.5",
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
                payload["w2_actual_chebyshev_energy_bridge_status"], "unproved"
            )
            self.assertEqual(
                payload["error_absorption_status"], "absorption_obligation_open"
            )
            self.assertFalse(payload["rh_proved"])
            self.assertIn("不证明 W2", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
