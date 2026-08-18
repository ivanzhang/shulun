#!/usr/bin/env python3
"""MFAC 截断 Möbius--log 强制性审计的红灯测试。

用法：python3 -m unittest \
    experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit_test -v
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    audit_truncated_mobius_log_coercivity,
    audit_coefficient_contract,
    comparison_witness_profiles,
    cutoff_from_theta,
    direct_centered_energy,
    linear_window,
    normalized_energy_ratio,
    write_certificate,
    quadratic_centered_energy,
    truncated_mobius_log_coefficients,
    weighted_mass,
)


class MFACTruncatedMobiusLogCoercivityAuditTest(unittest.TestCase):
    """验证预注册截断系数族及其依赖合同。"""

    def test_linear_window_has_fixed_endpoints(self) -> None:
        """线性窗口必须在预注册端点取固定值。"""
        self.assertEqual(linear_window(0.0), 1.0)
        self.assertEqual(linear_window(1.0), 0.0)
        self.assertAlmostEqual(linear_window(0.25), 0.75)

    def test_coefficients_use_squarefree_mobius_log_linear_window(self) -> None:
        """平方自由 Möbius--log 系数必须使用实际线性窗口定义。"""
        coefficients = truncated_mobius_log_coefficients(limit=1024, theta=0.4)
        cutoff = cutoff_from_theta(1024, 0.4)

        self.assertEqual(cutoff, 16)
        self.assertAlmostEqual(coefficients[2], math.log(2.0) * 0.75)
        expected_for_six = -math.log(6.0) * (
            1.0 - math.log(6.0) / math.log(float(cutoff))
        )
        self.assertAlmostEqual(coefficients[6], expected_for_six)
        self.assertNotIn(4, coefficients)
        self.assertNotIn(cutoff, coefficients)

    def test_cutoff_uses_exact_floor_and_rejects_empty_divisor_range(self) -> None:
        """截断上界必须精确遵守 floor(X^theta)，不能强行抬高到 2。"""
        self.assertEqual(cutoff_from_theta(2, 0.25), 1)

        with self.assertRaisesRegex(ValueError, "无有效整除索引"):
            truncated_mobius_log_coefficients(2, 0.25)

    def test_contract_rejects_target_and_analytic_inputs(self) -> None:
        """系数合同必须标识读取目标误差或禁止解析输入的情形。"""
        audit = audit_coefficient_contract(
            {"uses": ("X", "d", "mobius", "log", "fixed_linear_window")}
        )
        self.assertEqual(audit["classification"], "coefficient_input_not_rejected")

        rejected = audit_coefficient_contract(
            {"uses": ("X", "psi(X)-X", "Mellin")}
        )
        self.assertEqual(
            rejected["classification"],
            "coefficient_uses_target_or_forbidden_analytic_input",
        )
        self.assertEqual(rejected["forbidden_inputs"], ("Mellin", "psi(X)-X"))

    def test_direct_and_quadratic_centered_energy_agree_for_safe_cutoff(self) -> None:
        """直接能量与二次型能量必须在合法 theta 下给出一致正值。"""
        limit = 64
        theta = 0.4
        cutoff = cutoff_from_theta(limit, theta)
        self.assertGreaterEqual(cutoff, 2)

        coefficients = truncated_mobius_log_coefficients(limit, theta)
        direct_energy = direct_centered_energy(limit, coefficients)
        quadratic_energy = quadratic_centered_energy(limit, coefficients)
        mass = weighted_mass(limit, coefficients)
        ratio = normalized_energy_ratio(limit, coefficients)

        self.assertGreater(direct_energy, 0.0)
        self.assertGreater(quadratic_energy, 0.0)
        self.assertAlmostEqual(direct_energy, quadratic_energy, places=10)
        self.assertGreater(mass, 0.0)
        self.assertTrue(math.isfinite(mass))
        self.assertGreater(ratio, 0.0)
        self.assertTrue(math.isfinite(ratio))

    def test_weighted_mass_includes_limit_factor(self) -> None:
        """加权质量必须等于 limit 乘以 sum(a_d^2/d)。"""
        coefficients = {2: 3.0, 5: -4.0}
        expected = 30.0 * ((3.0 * 3.0 / 2.0) + (4.0 * 4.0 / 5.0))

        self.assertAlmostEqual(weighted_mass(30, coefficients), expected)

    def test_audit_reports_finite_structured_coercivity_profile_only(self) -> None:
        """顶层审计只能报告有限结构读数，不得升级为 RH 证明。"""
        audit = audit_truncated_mobius_log_coercivity(64, 0.4)

        self.assertEqual(
            audit["status"],
            "numerical_only_finite_structured_coercivity_profile",
        )
        self.assertEqual(audit["structured_coercivity_status"], "unproved")
        self.assertIs(audit["rh_proved"], False)
        self.assertGreater(audit["normalized_energy_ratio"], 0.0)

    def test_comparison_witness_profiles_are_finite_reverse_pressure_only(self) -> None:
        """四类对照见证必须是确定性有限反向压力测试。"""
        profiles = comparison_witness_profiles(512, 0.4)

        self.assertEqual(
            set(profiles),
            {
                "squarefree_mobius",
                "primorial",
                "single_prime_layer",
                "high_divisor_composite",
            },
        )
        for name, profile in profiles.items():
            with self.subTest(profile=name):
                self.assertEqual(profile["kind"], name)
                self.assertIn("coefficient_support", profile)
                self.assertIn("coefficient_count", profile)
                self.assertIn("weighted_mass", profile)
                self.assertIn("quadratic_centered_energy", profile)
                self.assertIn("normalized_energy_ratio", profile)

                if profile.get("status") == "empty_at_finite_scale":
                    self.assertEqual(profile["coefficient_support"], ())
                    self.assertEqual(profile["coefficient_count"], 0)
                    self.assertIsNone(profile["weighted_mass"])
                    self.assertIsNone(profile["quadratic_centered_energy"])
                    self.assertIsNone(profile["normalized_energy_ratio"])
                    continue

                self.assertGreater(profile["coefficient_count"], 0)
                self.assertGreater(profile["weighted_mass"], 0.0)
                self.assertGreater(profile["quadratic_centered_energy"], 0.0)
                self.assertTrue(math.isfinite(profile["normalized_energy_ratio"]))

        self.assertEqual(
            profiles["squarefree_mobius"]["coefficient_support"],
            (2, 3, 5, 6, 7, 10, 11),
        )
        self.assertEqual(profiles["primorial"]["coefficient_support"], (6,))

    def test_audit_payload_includes_final_review_status_and_profiles(self) -> None:
        """最终规格状态字段和对照见证必须写入 JSON 可序列化载荷。"""
        audit = audit_truncated_mobius_log_coercivity(512, 0.4)

        self.assertEqual(audit["window"], "linear")
        self.assertEqual(audit["coefficient_family_status"], "specified")
        self.assertIs(audit["coefficient_independence_verified"], True)
        self.assertEqual(audit["finite_profile_status"], "completed_numerical_only")
        self.assertEqual(audit["chebyshev_bridge_status"], "not_started")
        self.assertEqual(audit["mellin_status"], "not_started")
        self.assertEqual(
            set(audit["comparison_witness_profiles"]),
            {
                "squarefree_mobius",
                "primorial",
                "single_prime_layer",
                "high_divisor_composite",
            },
        )
        json.dumps(audit, ensure_ascii=False, sort_keys=True)

    def test_write_certificate_preserves_numerical_only_rh_boundary(self) -> None:
        """证书写出必须保留数值-only 边界且明示不构成 RH 证明。"""
        audit = audit_truncated_mobius_log_coercivity(128, 0.4)

        with tempfile.TemporaryDirectory() as temporary_directory:
            json_path = f"{temporary_directory}/audit.json"
            markdown_path = f"{temporary_directory}/audit.md"

            write_certificate(audit, json_path, markdown_path)

            with open(json_path, encoding="utf-8") as handle:
                payload = json.load(handle)
            with open(markdown_path, encoding="utf-8") as handle:
                markdown = handle.read()

        self.assertIs(payload["rh_proved"], False)
        self.assertEqual(
            payload["status"],
            "numerical_only_finite_structured_coercivity_profile",
        )
        self.assertEqual(payload["window"], "linear")
        self.assertEqual(payload["coefficient_family_status"], "specified")
        self.assertIn("comparison_witness_profiles", payload)
        self.assertIn("finite_profile_status=completed_numerical_only", markdown)
        self.assertIn("chebyshev_bridge_status=not_started", markdown)
        self.assertIn("mellin_status=not_started", markdown)
        self.assertIn("不构成统一强制性", markdown)
        self.assertIn("Chebyshev 能量桥", markdown)
        self.assertIn("Mellin 收缩", markdown)
        self.assertIn("不构成 RH 证明", markdown)

    def test_cli_path_execution_writes_json_and_markdown_outputs(self) -> None:
        """直接用脚本路径执行 CLI 时必须成功写出 JSON 与 Markdown 文件。"""
        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            json_path = temporary_path / "audit.json"
            markdown_path = temporary_path / "audit.md"

            result = subprocess.run(
                [
                    sys.executable,
                    str(
                        Path(
                            "experiments/prime_matrix_mfac_truncated_mobius_log_coercivity_audit.py"
                        )
                    ),
                    "--limit",
                    "64",
                    "--theta",
                    "0.4",
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
            self.assertTrue(json_path.exists())
            self.assertTrue(markdown_path.exists())


if __name__ == "__main__":
    unittest.main()
