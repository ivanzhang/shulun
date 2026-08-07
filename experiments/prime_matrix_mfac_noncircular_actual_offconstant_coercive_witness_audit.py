#!/usr/bin/env python3
"""MFAC Mellin 前非循环去常数强制见证。"""

from __future__ import annotations

import math
from fractions import Fraction


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
