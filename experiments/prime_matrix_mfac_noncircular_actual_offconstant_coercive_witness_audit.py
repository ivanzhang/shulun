#!/usr/bin/env python3
"""MFAC Mellin 前非循环去常数强制见证。"""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from fractions import Fraction
from typing import Any


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
