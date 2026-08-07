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
    if type(value) not in (int, float) or not math.isfinite(value):
        raise ValueError(f"{name} 必须是有限的内建 int 或 float")
    return value


def actual_offconstant_coercive_witness_data(
    limit: int, scalar: int | float = 1.0
) -> dict[str, int | float | bool | str]:
    """返回实际 LCM Gram 模型中 Mellin 前一维见证的精确数据。"""
    checked_limit = _require_integer_at_least_two(limit, "limit")
    checked_scalar = _require_finite_builtin_number(scalar, "scalar")
    half_limit = checked_limit // 2
    coefficient = Fraction(half_limit, checked_limit)
    energy = Fraction(half_limit * (checked_limit - half_limit), checked_limit)
    lower_bound = Fraction(2 * checked_limit, 9)
    scalar_squared = Fraction(checked_scalar) ** 2

    return {
        "limit": checked_limit,
        "coefficient_source": "K_X(1,2)/K_X(1,1)",
        "coefficient_exact_numerator": coefficient.numerator,
        "coefficient_exact_denominator": coefficient.denominator,
        "constant_orthogonality_exact_numerator": 0,
        "energy_exact_numerator": energy.numerator,
        "energy_exact_denominator": energy.denominator,
        "energy": float(energy),
        "coercivity_lower_bound": float(lower_bound),
        "scaled_energy": float(scalar_squared * energy),
        "scaled_coercivity_lower_bound": float(scalar_squared * lower_bound),
        "witness_constructed_before_mellin": True,
        "uses_target_error": False,
        "uses_mellin_input": False,
    }
