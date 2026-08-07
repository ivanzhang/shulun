#!/usr/bin/env python3
"""审计实际整数 LCM 核中直接去常数投影的循环边界。

用法示例：
  python3 -m unittest experiments.prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test -v

本模块只审计有限实际整数上的直接秩一 ``e_1`` 投影恒等式及输入来源合同，
不提供任何关于 ψ 误差、零点排除、RH 或全局不存在性的结论。
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from prime_matrix_mfac_actual_lcm_gram_energy_audit import (
    lcm_gram_entry,
    mobius,
    von_mangoldt,
)


FORBIDDEN_DIRECT_PROJECTION_INPUTS = frozenset(
    {
        "psi(X)",
        "E_psi(X)",
        "psi(X)-X",
        "target_error",
        "zero_location",
        "zero_free_region",
        "explicit_formula_remainder",
    }
)


def _require_positive_integer(value: object, name: str) -> int:
    """验证有限实际区间所需的正整数参数。"""
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} 必须为正整数")
    return value


def _require_finite_builtin_number(value: object, name: str) -> float:
    """验证非布尔且有限的内建实数。"""
    if type(value) not in (int, float):
        raise ValueError(f"{name} 必须为非布尔的内建 int 或 float")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{name} 必须为有限实数")
    return number


def _checked_vector(
    limit: int, vector: Mapping[int, int | float], name: str
) -> dict[int, float]:
    """验证一个以实际除数为坐标的有限实向量。"""
    if not isinstance(vector, Mapping):
        raise ValueError(f"{name} 必须为有限 Mapping")

    checked: dict[int, float] = {}
    for divisor, weight in vector.items():
        checked_divisor = _require_positive_integer(divisor, f"{name} divisor")
        if checked_divisor > limit:
            raise ValueError(f"{name} divisor 不能超过 limit")
        checked[checked_divisor] = _require_finite_builtin_number(
            weight, f"{name} weight"
        )
    return checked


def chebyshev_psi(limit: int) -> float:
    """独立逐项求和得到有限实际 Chebyshev ψ 值。"""
    checked_limit = _require_positive_integer(limit, "limit")
    return math.fsum(von_mangoldt(value) for value in range(1, checked_limit + 1))


def g_weight(divisor: int) -> float:
    """返回 ``g=w-e_1`` 的实际 divisor 坐标。"""
    checked_divisor = _require_positive_integer(divisor, "divisor")
    return -mobius(checked_divisor) * math.log(checked_divisor) - (
        1.0 if checked_divisor == 1 else 0.0
    )


def lcm_inner_product(
    limit: int,
    left: Mapping[int, int | float],
    right: Mapping[int, int | float],
) -> float:
    """计算两个有限 divisor 向量的实际 LCM Gram 内积。"""
    checked_limit = _require_positive_integer(limit, "limit")
    checked_left = _checked_vector(checked_limit, left, "left")
    checked_right = _checked_vector(checked_limit, right, "right")

    terms: list[float] = []
    for left_divisor, left_weight in checked_left.items():
        for right_divisor, right_weight in checked_right.items():
            term = (
                left_weight
                * right_weight
                * lcm_gram_entry(checked_limit, left_divisor, right_divisor)
            )
            if not math.isfinite(term):
                raise ValueError("LCM 内积乘积项必须为有限实数")
            terms.append(term)

    try:
        result = math.fsum(terms)
    except OverflowError as error:
        raise ValueError("LCM 内积总和必须为有限实数") from error
    if not math.isfinite(result):
        raise ValueError("LCM 内积总和必须为有限实数")
    return result


def direct_projection_data(limit: int, alpha: int | float) -> dict[str, float | int]:
    """审计 ``g-alpha*e_1`` 的实际投影缺陷及唯一正交系数。"""
    checked_limit = _require_positive_integer(limit, "limit")
    checked_alpha = _require_finite_builtin_number(alpha, "alpha")
    psi_value = chebyshev_psi(checked_limit)
    chebyshev_error = psi_value - checked_limit
    e1 = {1: 1.0}
    g = {divisor: g_weight(divisor) for divisor in range(1, checked_limit + 1)}
    g_e1 = lcm_inner_product(checked_limit, g, e1)
    e1_norm = lcm_inner_product(checked_limit, e1, e1)
    centered_g = dict(g)
    centered_g[1] = centered_g[1] - checked_alpha
    actual_defect = lcm_inner_product(checked_limit, centered_g, e1)

    return {
        "limit": checked_limit,
        "psi_value": psi_value,
        "chebyshev_error": chebyshev_error,
        "g_e1_inner_product": g_e1,
        "e1_norm_squared": e1_norm,
        "alpha": checked_alpha,
        "actual_defect": actual_defect,
        "theoretical_defect": chebyshev_error - checked_alpha * checked_limit,
        "unique_orthogonal_alpha": chebyshev_error / checked_limit,
    }


def audit_direct_projection_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    """分类直接 ``e_1`` 投影系数的输入来源，不虚构独立性。"""
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")

    alpha_uses = contract.get("alpha_uses")
    if isinstance(alpha_uses, str) or not isinstance(alpha_uses, Iterable):
        raise ValueError("alpha_uses 必须为非裸字符串的 Iterable[str]")

    checked_uses = tuple(alpha_uses)
    if any(type(value) is not str for value in checked_uses):
        raise ValueError("alpha_uses 的元素必须为字符串")

    forbidden_inputs = tuple(
        value
        for value in checked_uses
        if value in FORBIDDEN_DIRECT_PROJECTION_INPUTS
    )
    if forbidden_inputs:
        classification = (
            "direct_e1_projection_uses_target_or_forbidden_analytic_input"
        )
    else:
        classification = "direct_e1_projection_independence_unverified"

    return {
        "alpha_uses": checked_uses,
        "forbidden_inputs": forbidden_inputs,
        "classification": classification,
        "actual_non_circular_witness_constructed": False,
        "mathematical_nonexistence_proved": False,
        "rh_proved": False,
    }


def write_certificate(output_directory: Path, limit: int = 60) -> dict[str, Path]:
    """保留证书 API；完整写出在任务三实现。"""
    raise NotImplementedError("证书写出将在任务三实现")
