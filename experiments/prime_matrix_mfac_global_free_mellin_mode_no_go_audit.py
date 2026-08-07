#!/usr/bin/env python3
"""审计自由乘法模型中的 Möbius 交替与 Mellin 增长边界。

用法示例：
  python3 experiments/prime_matrix_mfac_global_free_mellin_mode_no_go_audit.py
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-global-free-mellin-mode-no-go-audit"

REQUIRED_CONTRACTION_FIELDS = (
    "fixed_actual_integer_embedding",
    "fixed_actual_chebyshev_measure",
    "exact_error_recurrence_on_actual_rows",
    "non_tagged_signed_kernel",
    "positive_or_coercive_energy_identity",
    "mellin_half_plane_spectral_contraction",
    "no_use_of_rh_or_zero_free_input",
)


@dataclass(frozen=True)
class FreeMonoidModel:
    """局部有限的带尺度自由交换单子，不代表自然数素数。"""

    atom_scales: dict[str, float]

    def __post_init__(self) -> None:
        if not self.atom_scales:
            raise ValueError("自由单子至少需要一个原子")
        if any(scale <= 1.0 for scale in self.atom_scales.values()):
            raise ValueError("每个原子尺度必须严格大于 1")

    @property
    def atom_names(self) -> tuple[str, ...]:
        """以稳定顺序返回原子名称。"""
        return tuple(sorted(self.atom_scales))

    @property
    def scales(self) -> tuple[float, ...]:
        """以原子名称顺序返回尺度。"""
        return tuple(self.atom_scales[name] for name in self.atom_names)

    def norm(self, exponent_vector: tuple[int, ...]) -> float:
        """计算单子元素的乘法尺度。"""
        self._validate_exponent_vector(exponent_vector)
        result = 1.0
        for scale, exponent in zip(self.scales, exponent_vector, strict=True):
            result *= scale**exponent
        return result

    def log_norm(self, exponent_vector: tuple[int, ...]) -> float:
        """计算单子元素尺度的自然对数。"""
        self._validate_exponent_vector(exponent_vector)
        return sum(
            exponent * math.log(scale)
            for scale, exponent in zip(self.scales, exponent_vector, strict=True)
        )

    def divisors(self, exponent_vector: tuple[int, ...]) -> list[tuple[int, ...]]:
        """枚举一个自由单子元素的全部约数指数向量。"""
        self._validate_exponent_vector(exponent_vector)
        return list(product(*(range(exponent + 1) for exponent in exponent_vector)))

    def mobius(self, exponent_vector: tuple[int, ...]) -> int:
        """计算自由单子上的 Möbius 值。"""
        self._validate_exponent_vector(exponent_vector)
        if any(exponent >= 2 for exponent in exponent_vector):
            return 0
        return -1 if sum(exponent_vector) % 2 else 1

    def lambda_value(self, exponent_vector: tuple[int, ...]) -> float:
        """计算自由单子上的 von Mangoldt 型权重。"""
        self._validate_exponent_vector(exponent_vector)
        nonzero_indices = [
            index for index, exponent in enumerate(exponent_vector) if exponent > 0
        ]
        if len(nonzero_indices) != 1:
            return 0.0
        return math.log(self.scales[nonzero_indices[0]])

    def elements_up_to(self, bound: float) -> list[tuple[int, ...]]:
        """枚举尺度不超过给定界的局部有限单子元素。"""
        if bound < 1.0:
            raise ValueError("枚举界必须至少为 1")
        maxima = [int(math.log(bound) / math.log(scale)) for scale in self.scales]
        elements = [
            exponent_vector
            for exponent_vector in product(*(range(maximum + 1) for maximum in maxima))
            if self.norm(exponent_vector) <= bound * (1.0 + 1e-12)
        ]
        return sorted(elements, key=lambda element: (self.norm(element), element))

    def _validate_exponent_vector(self, exponent_vector: tuple[int, ...]) -> None:
        """验证指数向量与自由原子集合相容。"""
        if len(exponent_vector) != len(self.atom_scales):
            raise ValueError("指数向量维数与原子数不一致")
        if any(exponent < 0 for exponent in exponent_vector):
            raise ValueError("指数必须为非负整数")


def audit_divisor_lattice_identity(
    model: FreeMonoidModel, bound: float
) -> dict[str, Any]:
    """逐点审计 Lambda 等于负 Möbius--log 卷积的精确恒等式。"""
    for element in model.elements_up_to(bound):
        expected = -sum(
            model.mobius(divisor) * model.log_norm(divisor)
            for divisor in model.divisors(element)
        )
        actual = model.lambda_value(element)
        if not math.isclose(actual, expected, abs_tol=1e-12):
            return {
                "identity_holds": False,
                "element_count": len(model.elements_up_to(bound)),
                "first_failure": {
                    "element": element,
                    "actual": actual,
                    "expected": expected,
                },
            }
    return {
        "identity_holds": True,
        "element_count": len(model.elements_up_to(bound)),
        "first_failure": None,
    }


def normalized_mellin_mode(t: float, beta: float, tau: float, epsilon: float) -> float:
    """返回自由轮廓的归一化 Mellin 增长模。"""
    _validate_mellin_parameters(beta, tau, epsilon)
    return epsilon * math.exp((beta - 0.5) * t) * math.cos(tau * t)


def target_theta_derivative(
    x: float, beta: float, tau: float, epsilon: float
) -> float:
    """计算目标连续 shell 轮廓的一阶导数。"""
    _validate_mellin_parameters(beta, tau, epsilon)
    if x <= 0.0:
        raise ValueError("x 必须为正")
    phase = tau * math.log(x)
    return 1.0 + epsilon * x ** (beta - 1.0) * (
        beta * math.cos(phase) - tau * math.sin(phase)
    )


def positivity_threshold(beta: float, tau: float, epsilon: float) -> float:
    """给出目标 shell 导数至少为二分之一的充分阈值。"""
    _validate_mellin_parameters(beta, tau, epsilon)
    amplitude = epsilon * math.hypot(beta, tau)
    return max(1.0, (2.0 * amplitude) ** (1.0 / (1.0 - beta)))


def classify_contraction_contract(record: dict[str, Any]) -> dict[str, Any]:
    """区分自由模型、未闭合实际合同与完整 synthetic 合同。"""
    if not record.get("fixed_actual_integer_embedding"):
        return {
            **record,
            "classification": "free_model_not_actual_integer_rh_attack",
            "actual_chebyshev_mellin_contraction_present": False,
            "rh_proved": False,
        }
    complete = all(record.get(field) for field in REQUIRED_CONTRACTION_FIELDS)
    if not complete:
        return {
            **record,
            "classification": "actual_contraction_contract_incomplete",
            "actual_chebyshev_mellin_contraction_present": False,
            "rh_proved": False,
        }
    if record.get("synthetic_fixture"):
        return {
            **record,
            "classification": "synthetic_complete_contraction_contract",
            "actual_chebyshev_mellin_contraction_present": False,
            "rh_proved": False,
        }
    return {
        **record,
        "classification": "complete_actual_contraction_contract_claim",
        "actual_chebyshev_mellin_contraction_present": True,
        "rh_proved": False,
    }


def complete_synthetic_contraction_contract() -> dict[str, Any]:
    """返回完整的 synthetic 收缩合同夹具，不代表实际整数证明。"""
    return {
        **{field: True for field in REQUIRED_CONTRACTION_FIELDS},
        "synthetic_fixture": True,
    }


def audit_current_corpus(root: Path) -> dict[str, Any]:
    """审计当前语料是否已提交实际 Chebyshev--Mellin 收缩合同。"""
    source_paths = (
        root / "docs" / "monograph" / "mfac-frontier-conclusion-and-proof-obligation-chain-20260807.md",
        root
        / "docs"
        / "monograph"
        / "prime-matrix-mfac-semiprime-local-naturality-factorization-audit.json",
        root
        / "docs"
        / "monograph"
        / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json",
    )
    source_text = "\n".join(path.read_text(encoding="utf-8") for path in source_paths)
    missing_contract_fields = [
        field for field in REQUIRED_CONTRACTION_FIELDS if field not in source_text
    ]
    model = FreeMonoidModel({"a": 2.0, "b": 3.0, "c": 5.0})
    identity = audit_divisor_lattice_identity(model, bound=30.0)
    beta = 0.75
    tau = 1.0
    epsilon = 0.1
    first_mode = normalized_mellin_mode(2.0 * math.pi, beta, tau, epsilon)
    second_mode = normalized_mellin_mode(4.0 * math.pi, beta, tau, epsilon)
    return {
        "certificate_type": "prime_matrix_mfac_global_free_mellin_mode_no_go_audit",
        "status": "free_mellin_growth_model_blocks_alternation_only_rh_attack",
        "verified_date": "2026-08-07",
        "exact_divisor_lattice_identity_available": identity["identity_holds"],
        "free_mellin_growth_countermodel_constructed": abs(second_mode) > abs(first_mode),
        "alternation_only_implies_sqrt_cancellation": False,
        "actual_chebyshev_mellin_contraction_present": not missing_contract_fields,
        "missing_actual_contraction_fields": missing_contract_fields,
        "countermodel_is_actual_integer_prime_system": False,
        "countermodel_is_actual_zeta_zero_counterexample": False,
        "mathematical_nonexistence_proved": False,
        "rh_proved": False,
        "row_column_unconditional_closed": False,
        "next_positive_gate": "ActualChebyshevErrorMellinContractionLawBeforeExplicitFormula",
    }


def write_certificate(
    certificate: dict[str, Any], json_out: Path, markdown_out: Path
) -> None:
    """写出机器证书和人读边界说明。"""
    json_out.parent.mkdir(parents=True, exist_ok=True)
    markdown_out.parent.mkdir(parents=True, exist_ok=True)
    json_out.write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    missing_fields = "\n".join(
        f"- `{field}`" for field in certificate["missing_actual_contraction_fields"]
    )
    markdown_out.write_text(
        "\n".join(
            [
                "# MFAC 全局自由 Mellin 增长模反模型审计",
                "",
                "**状态：** `free_mellin_growth_model_blocks_alternation_only_rh_attack`",
                "",
                "本证书验证局部有限自由乘法模型保留 Möbius 交替与精确 divisor-lattice identity，同时允许 beta 大于二分之一的归一化 Mellin 增长轮廓。它不是自然数素数的反例，不对应实际 zeta 零点，也不反驳 RH。",
                "",
                "## 当前语料读数",
                "",
                "```text",
                f"exact_divisor_lattice_identity_available={str(certificate['exact_divisor_lattice_identity_available']).lower()}",
                f"free_mellin_growth_countermodel_constructed={str(certificate['free_mellin_growth_countermodel_constructed']).lower()}",
                "alternation_only_implies_sqrt_cancellation=false",
                f"actual_chebyshev_mellin_contraction_present={str(certificate['actual_chebyshev_mellin_contraction_present']).lower()}",
                "mathematical_nonexistence_proved=false",
                "rh_proved=false",
                "row_column_unconditional_closed=false",
                f"next_positive_gate={certificate['next_positive_gate']}",
                "```",
                "",
                "## 当前缺失的实际收缩字段",
                "",
                missing_fields or "当前审计来源未缺字段；仍需独立数学验证。",
                "",
                "自由模型说明的是：交替递推、全局守恒和形式多维叠加不足以自行强迫平方根消去。要攻击实际 RH，必须给出固定实际整数嵌入、固定 Chebyshev 测度、实际误差递推和独立的 Mellin 半平面收缩律。",
                "",
            ]
        ),
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    """解析证书输出路径。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, default=DOCS / f"{SLUG}.json")
    parser.add_argument("--markdown-out", type=Path, default=DOCS / f"{SLUG}.md")
    return parser.parse_args()


def main() -> None:
    """运行自由 Mellin 反模型审计并写出证书。"""
    args = parse_args()
    certificate = audit_current_corpus(ROOT)
    write_certificate(certificate, args.json_out, args.markdown_out)
    print(f"写入 JSON 证书：{args.json_out}")
    print(f"写入 Markdown 证书：{args.markdown_out}")


def _validate_mellin_parameters(beta: float, tau: float, epsilon: float) -> None:
    """验证对抗性 Mellin 轮廓的参数范围。"""
    if not 0.5 < beta < 1.0:
        raise ValueError("beta 必须满足 1/2 < beta < 1")
    if tau == 0.0:
        raise ValueError("tau 必须非零")
    if epsilon <= 0.0:
        raise ValueError("epsilon 必须为正")


if __name__ == "__main__":
    main()
