#!/usr/bin/env python3
"""MFAC Mellin 前非循环去常数强制见证。"""

from __future__ import annotations

import json
import math
from collections.abc import Iterable, Mapping
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-noncircular-actual-offconstant-coercive-witness-audit"

FORBIDDEN_WITNESS_DEPENDENCIES = frozenset(
    {
        "psi(X)-X",
        "Chebyshev_error",
        "Mellin",
        "zeta_zero",
        "explicit_formula",
    }
)


def _require_integer_at_least_two(value: object, name: str) -> int:
    """验证参数是至少为二的内建整数。"""
    if type(value) is not int or value < 2:
        raise ValueError(f"{name} 必须是至少为 2 的内建 int")
    return value


def _require_finite_builtin_number(value: object, name: str) -> int | float:
    """验证参数是有限的内建整数或浮点数。"""
    if type(value) not in (int, float):
        raise ValueError(f"{name} 必须是有限的内建 int 或 float")
    if type(value) is float and not math.isfinite(value):
        raise ValueError(f"{name} 必须是有限的内建 int 或 float")
    return value


def _finite_json_float(value: Fraction, name: str) -> float:
    """将精确分数转换为有限且可安全写入 JSON 的浮点数。"""
    try:
        converted = float(value)
    except OverflowError as error:
        raise ValueError(f"{name} 必须能表示为有限 JSON 数值") from error
    if not math.isfinite(converted):
        raise ValueError(f"{name} 必须能表示为有限 JSON 数值")
    if value and converted == 0.0:
        raise ValueError(f"{name} 不得在 JSON 数值中下溢为零")
    return converted


def _checked_string_iterable(
    contract: Mapping[str, Any], name: str
) -> tuple[str, ...]:
    """验证合同字段是非裸字符串的内建字符串可迭代对象。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")

    values = contract.get(name)
    try:
        if isinstance(values, str) or not isinstance(values, Iterable):
            raise ValueError(f"{name} 必须为非裸字符串的可迭代对象")
        checked_values = tuple(values)
    except TypeError as error:
        raise ValueError(f"{name} 必须为非裸字符串的可迭代对象") from error

    if not all(type(value) is str for value in checked_values):
        raise ValueError(f"{name} 的所有元素必须为内建 str")
    return checked_values


def actual_offconstant_coercive_witness_data(
    limit: int, scalar: int | float = 1.0
) -> dict[str, int | float | bool | str]:
    """返回实际 LCM Gram 模型中 Mellin 前一维见证的精确数据。"""
    checked_limit = _require_integer_at_least_two(limit, "limit")
    checked_scalar = _require_finite_builtin_number(scalar, "scalar")
    half_limit = checked_limit // 2
    kernel_11 = Fraction(checked_limit, 1)
    kernel_12 = Fraction(half_limit, 1)
    coefficient = Fraction(half_limit, checked_limit)
    orthogonality = kernel_12 - coefficient * kernel_11
    energy = Fraction(half_limit * (checked_limit - half_limit), checked_limit)
    lower_bound = Fraction(2 * checked_limit, 9)
    scalar_squared = Fraction(checked_scalar) ** 2
    energy_value = _finite_json_float(energy, "energy")
    lower_bound_value = _finite_json_float(lower_bound, "coercivity_lower_bound")
    scaled_energy = _finite_json_float(scalar_squared * energy, "scaled_energy")
    scaled_lower_bound = _finite_json_float(
        scalar_squared * lower_bound, "scaled_coercivity_lower_bound"
    )

    return {
        "limit": checked_limit,
        "coefficient_source": "K_X(1,2)/K_X(1,1)",
        "K11_exact_numerator": kernel_11.numerator,
        "K12_exact_numerator": kernel_12.numerator,
        "coefficient_exact_numerator": coefficient.numerator,
        "coefficient_exact_denominator": coefficient.denominator,
        "constant_orthogonality_exact_numerator": orthogonality.numerator,
        "constant_orthogonality_exact_denominator": orthogonality.denominator,
        "energy_exact_numerator": energy.numerator,
        "energy_exact_denominator": energy.denominator,
        "energy": energy_value,
        "coercivity_lower_bound": lower_bound_value,
        "scaled_energy": scaled_energy,
        "scaled_coercivity_lower_bound": scaled_lower_bound,
        "witness_constructed_before_mellin": True,
        "uses_target_error": False,
        "uses_mellin_input": False,
    }


def audit_witness_dependency_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    """审计见证是否读取被禁止的目标或解析依赖。"""
    checked_uses = _checked_string_iterable(contract, "witness_uses")
    forbidden_uses = tuple(
        value for value in checked_uses if value in FORBIDDEN_WITNESS_DEPENDENCIES
    )
    classification = (
        "forbidden_target_or_analytic_dependency"
        if forbidden_uses
        else "noncircular_actual_gram_witness"
    )
    return {
        "witness_uses": checked_uses,
        "forbidden_uses": forbidden_uses,
        "classification": classification,
        "actual_non_circular_witness_constructed": not forbidden_uses,
    }


def audit_noncircular_actual_offconstant_coercive_witness_before_mellin(
    limit: int = 60,
) -> dict[str, Any]:
    """汇总 Mellin 前实际去常数一维见证及尚未闭合的正向门。"""
    witness = actual_offconstant_coercive_witness_data(limit)
    dependency_contract = audit_witness_dependency_contract(
        {
            "witness_uses": (
                "integer_limit_X",
                "K_X(1,1)",
                "K_X(1,2)",
            )
        }
    )
    return {
        "slug": SLUG,
        "limit": witness["limit"],
        "witness": witness,
        "dependency_contract": dependency_contract,
        "noncircular_actual_offconstant_coercive_witness_constructed": True,
        "one_dimensional_coercivity_established": True,
        "full_offconstant_spectral_gap_established": False,
        "actual_chebyshev_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": (
            "UniformOffConstantCoercivityOrActualChebyshevMellinContractionLaw"
        ),
    }


def _render_markdown(payload: Mapping[str, Any]) -> str:
    """渲染 Mellin 前非循环一维强制见证的边界说明。"""
    witness = payload["witness"]
    dependency_contract = payload["dependency_contract"]
    return f"""# MFAC 非循环实际去常数强制见证（Mellin 前）

## 有限实际见证

本证书只使用有限实际整数区间 \\(1\\le n\\le {payload['limit']}\\) 的有限整数 LCM Gram 条目。

\\[
K_X(d,e)=\\left\\lfloor\\frac{{X}}{{\\operatorname{{lcm}}(d,e)}}\\right\\rfloor.
\\]

取实际一维方向

\\[
h_X=e_2-\\frac{{\\lfloor X/2\\rfloor}}{{X}}e_1.
\\]

等价地，见证可记为 `h_X=e_2-floor(X/2)e_1/X`。

系数来源为 `{witness['coefficient_source']}`；因此
\\(\\langle h_X,e_1\\rangle_{{K_X}}=0\\)。精确能量为

\\[
\\lVert h_X\\rVert_{{K_X}}^2
=\\frac{{m_X(X-m_X)}}{{X}},
\\qquad m_X=\\lfloor X/2\\rfloor,
\\]

并满足一维下界 \\(\\lVert h_X\\rVert_{{K_X}}^2\\ge 2X/9\\)。当前
`limit={payload['limit']}` 的精确能量为
`{witness['energy_exact_numerator']}/{witness['energy_exact_denominator']}`，
下界读数为 `{witness['coercivity_lower_bound']}`。

## 非循环合同

见证使用 `{', '.join(dependency_contract['witness_uses'])}`，禁止依赖未被使用；
`forbidden_uses={dependency_contract['forbidden_uses']}`。它不读取 Chebyshev 目标误差，
不读取 Mellin 输入、零点或显式公式输入，因而只是 Mellin 前的实际有限整数构造。

## 结论边界

这仅是实际一维方向强制性，不是全空间谱隙，也不是 Mellin 收缩。它不是
Chebyshev 误差界、非零点排除、非 RH；更具体地说，
`actual_chebyshev_mellin_contraction_present=false`、`rh_proved=false`。
它不宣称全空间去常数方向的一致强制性，也不提供任何解析收缩律。

下一正向数学门为 `{payload['next_positive_gate']}`。
"""


def write_certificate(output_directory: Path, limit: int = 60) -> dict[str, Path]:
    """写出非循环实际去常数强制见证的 JSON 与 Markdown 证书。"""
    if not isinstance(output_directory, Path):
        raise ValueError("output_directory 必须为 Path")

    output_directory.mkdir(parents=True, exist_ok=True)
    payload = audit_noncircular_actual_offconstant_coercive_witness_before_mellin(limit)
    json_path = output_directory / f"{SLUG}.json"
    markdown_path = output_directory / f"{SLUG}.md"
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_path.write_text(_render_markdown(payload), encoding="utf-8")
    return {"json_path": json_path, "markdown_path": markdown_path}


def main() -> None:
    """将默认有限审计证书写入仓库 docs/monograph。"""
    paths = write_certificate(DOCS)
    print(paths["json_path"])
    print(paths["markdown_path"])


if __name__ == "__main__":
    main()
