"""形式 Möbius--Lambda 与 Abel 恒等式的有限测试。

用法示例：
  python3 -m unittest experiments.prime_matrix_mfac_unconditional_w1_w2_log_saving_audit_test -v
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from experiments.prime_matrix_mfac_unconditional_w1_w2_log_saving_audit import (
    ALLOWED_SOURCES,
    FORBIDDEN_SOURCES,
    abel_sum_by_parts,
    audit_log_saving_diagnostic,
    audit_unconditional_w1_contract,
    default_contract,
    formal_mobius_lambda,
    formal_negative_mobius_log,
    render_markdown,
    write_certificate,
)


class _IntegerSubclass(int):
    """用于验证公开接口拒绝内建 int 的子类。"""


class _StringSubclass(str):
    """用于验证合同来源只接受内建 str。"""


class MFACUnconditionalW1W2LogSavingAuditTest(unittest.TestCase):
    """验证有限形式对数系数恒等式，不涉及 W1、W2 或 RH。"""

    def test_mobius_lambda_matches_negative_mobius_log_through_64(self) -> None:
        """逐项有限检验 (μ*Λ)(n) = -μ(n) log n 的形式素数系数。"""
        for index in range(1, 65):
            self.assertEqual(
                formal_mobius_lambda(index),
                formal_negative_mobius_log(index),
                index,
            )

    def test_formal_log_coefficients_match_independent_small_fixtures(self) -> None:
        """已知小整数的形式系数必须匹配独立写出的数学夹具。"""
        fixtures = {
            1: {},
            2: {2: Fraction(1, 1)},
            6: {2: Fraction(-1, 1), 3: Fraction(-1, 1)},
            8: {},
            12: {},
        }
        for index, expected in fixtures.items():
            with self.subTest(index=index):
                self.assertEqual(formal_negative_mobius_log(index), expected)
                self.assertEqual(formal_mobius_lambda(index), expected)

    def test_abel_sum_by_parts_has_zero_rational_residual(self) -> None:
        """有理夹具必须精确满足有限 Abel 求和恒等式。"""
        result = abel_sum_by_parts(
            {
                2: Fraction(3, 2),
                5: Fraction(-4, 3),
                9: Fraction(7, 5),
            },
            {
                2: Fraction(11, 7),
                5: Fraction(-2, 5),
                9: Fraction(13, 4),
            },
        )

        self.assertEqual(result["residual"], Fraction(0, 1))
        self.assertEqual(result["direct"], result["summation_by_parts"])

    def test_public_apis_reject_invalid_inputs(self) -> None:
        """公开接口必须拒绝非内建正整数索引与非法 Abel 数据。"""
        with self.assertRaises(ValueError):
            formal_negative_mobius_log(True)
        with self.assertRaises(ValueError):
            formal_mobius_lambda(0)

        invalid_abel_inputs = (
            ({}, {}),
            ([], {2: Fraction(1, 2)}),
            ({2: Fraction(1, 2)}, []),
            ({True: Fraction(1, 2)}, {True: Fraction(1, 2)}),
            (
                {_IntegerSubclass(2): Fraction(1, 2)},
                {_IntegerSubclass(2): Fraction(1, 2)},
            ),
            ({2: 1}, {2: Fraction(1, 2)}),
            (
                {2: Fraction(1, 2)},
                {2: Fraction(1, 2), 3: Fraction(1, 3)},
            ),
        )
        for values, weights in invalid_abel_inputs:
            with self.subTest(values=values, weights=weights):
                with self.assertRaises(ValueError):
                    abel_sum_by_parts(values, weights)

        with self.assertRaises(ValueError):
            abel_sum_by_parts({2: Fraction(1, 2)}, {2: 1})

    def test_default_contract_registers_only_open_finite_obligations(self) -> None:
        """默认合同只登记允许的有限来源与未解决状态。"""
        contract = default_contract()

        self.assertEqual(
            contract["uses"],
            (
                "finite_dirichlet_convolution",
                "abel_summation_identity",
                "euler_phi_identity",
            ),
        )
        self.assertEqual(contract["uniformity_variable"], "truncation")
        self.assertEqual(contract["constant_dependency"], ())
        self.assertEqual(contract["w1_l2_upper_status"], "open")
        self.assertEqual(contract["balanced_remainder_status"], "open")
        self.assertIs(contract["rh_proved"], False)
        self.assertTrue(set(contract["uses"]).issubset(ALLOWED_SOURCES))

    def test_contract_rejects_forbidden_and_unknown_sources(self) -> None:
        """禁止来源与未知来源均不得进入无条件合同。"""
        for source in FORBIDDEN_SOURCES:
            contract = default_contract()
            contract["uses"] = (source,)
            with self.subTest(source=source):
                with self.assertRaisesRegex(ValueError, "禁止"):
                    audit_unconditional_w1_contract(contract)

        contract = default_contract()
        contract["uses"] = ("unregistered_source",)
        with self.assertRaises(ValueError):
            audit_unconditional_w1_contract(contract)

    def test_contract_rejects_invalid_scope_dependencies_and_uses(self) -> None:
        """合同字段必须保持指定的统一性、常数依赖及来源数据类型。"""
        invalid_contracts = (
            {"uniformity_variable": "scale"},
            {"constant_dependency": ("parameter",)},
            {"constant_dependency": "parameter"},
            {"constant_dependency": ["parameter"]},
            {"uses": "finite_dirichlet_convolution"},
            {"uses": ["finite_dirichlet_convolution"]},
            {"uses": ()},
            {"uses": (1,)},
            {"uses": (_StringSubclass("finite_dirichlet_convolution"),)},
        )
        for overrides in invalid_contracts:
            contract = default_contract()
            contract.update(overrides)
            with self.subTest(overrides=overrides):
                with self.assertRaises(ValueError):
                    audit_unconditional_w1_contract(contract)

        with self.assertRaises(ValueError):
            audit_unconditional_w1_contract([])

    def test_contract_rejects_any_claim_promotion(self) -> None:
        """合同不得把 W1、平衡余项或 RH 升格为已证明。"""
        invalid_contracts = (
            {"w1_l2_upper_status": "proved"},
            {"balanced_remainder_status": "proved"},
            {"rh_proved": True},
            {"rh_proved": 1},
            {"rh_proved": 0},
        )
        for overrides in invalid_contracts:
            contract = default_contract()
            contract.update(overrides)
            with self.subTest(overrides=overrides):
                with self.assertRaises(ValueError):
                    audit_unconditional_w1_contract(contract)

    def test_contract_returns_registered_open_status_without_proof_claim(self) -> None:
        """审计结果只回传允许来源和固定开放状态。"""
        contract = default_contract()
        contract["uses"] = (
            "finite_dirichlet_convolution",
            "classical_sieve_bound",
        )

        result = audit_unconditional_w1_contract(contract)

        self.assertEqual(result["uses"], contract["uses"])
        self.assertEqual(result["w1_l2_upper_status"], "open")
        self.assertEqual(result["balanced_remainder_status"], "open")
        self.assertIs(result["rh_proved"], False)

    def test_log_saving_diagnostic_is_numerical_and_keeps_w1_open(self) -> None:
        """有限能量诊断须区分形式核验、数值结果与开放命题。"""
        certificate = audit_log_saving_diagnostic(64)

        self.assertEqual(
            certificate["certificate_type"],
            "prime_matrix_mfac_unconditional_w1_w2_log_saving_audit",
        )
        self.assertEqual(certificate["cutoff"], 64)
        self.assertEqual(certificate["formal_convolution_status"], "verified_finite")
        self.assertEqual(certificate["actual_log_window_status"], "numerical_only")
        self.assertLess(certificate["euler_phi_energy_residual"], 1e-10)
        self.assertEqual(certificate["baseline_bound_status"], "not_proved")
        self.assertEqual(certificate["balanced_remainder_status"], "open")
        self.assertEqual(certificate["w1_l2_upper_status"], "open")
        self.assertIs(certificate["rh_proved"], False)

    def test_log_saving_diagnostic_rejects_invalid_cutoffs(self) -> None:
        """诊断入口只接受至少为三的内建整数截断点。"""
        for cutoff in (True, False, 2, 0, -1, 3.0, _IntegerSubclass(64)):
            with self.subTest(cutoff=cutoff):
                with self.assertRaises(ValueError):
                    audit_log_saving_diagnostic(cutoff)

    def test_certificate_writers_emit_sorted_json_and_boundary_markdown(self) -> None:
        """证书写入器必须生成可解析 JSON 与明确的开放边界说明。"""
        certificate = audit_log_saving_diagnostic(64)
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            json_path = root / "nested" / "certificate.json"
            markdown_path = root / "nested" / "certificate.md"

            write_certificate(certificate, json_path, markdown_path)

            self.assertEqual(json.loads(json_path.read_text(encoding="utf-8")), certificate)
            self.assertEqual(
                json_path.read_text(encoding="utf-8").splitlines()[1],
                '  "actual_log_window_status": "numerical_only",',
            )
            markdown = markdown_path.read_text(encoding="utf-8")
            for field in (
                "formal_convolution_status=verified_finite",
                "actual_log_window_status=numerical_only",
                "balanced_remainder_status=open",
                "w1_l2_upper_status=open",
                "rh_proved=false",
                "不证明统一对数节省、W2 或 RH",
            ):
                with self.subTest(field=field):
                    self.assertIn(field, markdown)
            self.assertEqual(render_markdown(certificate), markdown)

    def test_cli_writes_parseable_certificate_with_open_boundaries(self) -> None:
        """脚本路径 CLI 必须写出可解析证书和不越界的 Markdown。"""
        script = Path(__file__).with_name(
            "prime_matrix_mfac_unconditional_w1_w2_log_saving_audit.py"
        )
        with TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            json_path = root / "result.json"
            markdown_path = root / "result.md"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--cutoff",
                    "64",
                    "--json-out",
                    str(json_path),
                    "--markdown-out",
                    str(markdown_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            certificate = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(certificate["cutoff"], 64)
            self.assertEqual(certificate["w1_l2_upper_status"], "open")
            self.assertIn(str(json_path), completed.stdout)
            self.assertIn("不证明统一对数节省、W2 或 RH", markdown_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
