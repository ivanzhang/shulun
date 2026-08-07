#!/usr/bin/env python3
"""审计实际整数上的 LCM Gram 能量恒等式与中心化输入边界。

用法示例：
  python3 experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py --limit 60

本模块只计算有限实际整数区间内的精确恒等式和普通 Cauchy 界，
不提供任何关于 ψ 平滑误差、零点位置或 RH 的结论。
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Mapping
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-actual-lcm-gram-energy-audit"

FORBIDDEN_CENTERING_INPUTS = frozenset(
    {
        "psi(X)",
        "E_psi(X)",
        "prime_count_error_bound",
        "zero_location",
        "zero_free_region",
        "explicit_formula_remainder",
    }
)


def _require_positive_integer(value: object, name: str) -> int:
    """验证并返回正整数，拒绝布尔值和非整数输入。"""
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} 必须为正整数")
    return value


def _require_divisor_within_limit(limit: object, divisor: object, name: str) -> int:
    """验证除数属于给定实际整数区间。"""
    checked_limit = _require_positive_integer(limit, "limit")
    checked_divisor = _require_positive_integer(divisor, name)
    if checked_divisor > checked_limit:
        raise ValueError(f"{name} 不能超过 limit")
    return checked_divisor


def mobius(value: int) -> int:
    """以试除分解计算 Möbius 函数，单位元取值为一。"""
    remaining = _require_positive_integer(value, "value")
    distinct_prime_count = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            if remaining % divisor == 0:
                return 0
            distinct_prime_count += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        distinct_prime_count += 1
    return -1 if distinct_prime_count % 2 else 1


def von_mangoldt(value: int) -> float:
    """仅在输入为单一素数幂时返回该素数的自然对数。"""
    remaining = _require_positive_integer(value, "value")
    if remaining == 1:
        return 0.0

    divisor = 2
    while divisor * divisor <= remaining and remaining % divisor:
        divisor = 3 if divisor == 2 else divisor + 2
    if divisor * divisor > remaining:
        return math.log(remaining)

    prime_base = divisor
    while remaining % prime_base == 0:
        remaining //= prime_base
    if remaining != 1:
        return 0.0
    return math.log(prime_base)


def lcm_gram_entry(limit: int, left: int, right: int) -> int:
    """精确计算区间内同时被两个除数整除的整数数量。"""
    checked_limit = _require_positive_integer(limit, "limit")
    checked_left = _require_divisor_within_limit(checked_limit, left, "left")
    checked_right = _require_divisor_within_limit(checked_limit, right, "right")
    return checked_limit // math.lcm(checked_left, checked_right)


def lcm_gram_quadratic_form(
    limit: int, coefficients: Mapping[int, float]
) -> float:
    """计算 LCM Gram 核对应的有限系数二次型。"""
    checked_limit = _require_positive_integer(limit, "limit")
    if not isinstance(coefficients, Mapping):
        raise ValueError("coefficients 必须为有限 Mapping")

    checked_coefficients: dict[int, float] = {}
    for divisor, weight in coefficients.items():
        checked_divisor = _require_divisor_within_limit(
            checked_limit, divisor, "coefficient divisor"
        )
        checked_coefficients[checked_divisor] = float(weight)

    return sum(
        left_weight
        * right_weight
        * lcm_gram_entry(checked_limit, left, right)
        for left, left_weight in checked_coefficients.items()
        for right, right_weight in checked_coefficients.items()
    )


def lcm_mobius_energy(limit: int) -> float:
    """用 -μ(d)log(d) 权重计算有限 LCM Gram 能量。"""
    checked_limit = _require_positive_integer(limit, "limit")
    coefficients = {
        divisor: -mobius(divisor) * math.log(divisor)
        for divisor in range(1, checked_limit + 1)
    }
    return lcm_gram_quadratic_form(checked_limit, coefficients)


def lambda_square_energy(limit: int) -> float:
    """逐项计算有限区间内 von Mangoldt 函数的平方和。"""
    checked_limit = _require_positive_integer(limit, "limit")
    return sum(von_mangoldt(value) ** 2 for value in range(1, checked_limit + 1))


def chebyshev_increment_energy(limit: int) -> float:
    """计算有限 Chebyshev 增量 Λ(n)-1 的平方能量。"""
    checked_limit = _require_positive_integer(limit, "limit")
    return sum(
        (von_mangoldt(value) - 1.0) ** 2
        for value in range(1, checked_limit + 1)
    )


def ordinary_cauchy_projection_bound(limit: int) -> dict[str, float | int]:
    """记录常数方向的精确投影和普通 Cauchy 上界。"""
    checked_limit = _require_positive_integer(limit, "limit")
    chebyshev_error = sum(
        von_mangoldt(value) - 1.0 for value in range(1, checked_limit + 1)
    )
    increment_energy = chebyshev_increment_energy(checked_limit)
    return {
        "chebyshev_error": chebyshev_error,
        "error_sum_squared": chebyshev_error**2,
        "increment_energy": increment_energy,
        "constant_direction_norm_squared": checked_limit,
        "cauchy_upper_bound": checked_limit * increment_energy,
    }


def six_multiple_non_prime_power_witnesses(limit: int) -> tuple[int, ...]:
    """列举区间内的六倍数，并防御性核验它们均非素数幂。"""
    checked_limit = _require_positive_integer(limit, "limit")
    witnesses = tuple(range(6, checked_limit + 1, 6))
    if any(von_mangoldt(value) != 0.0 for value in witnesses):
        raise AssertionError("六倍数见证意外成为素数幂")
    return witnesses


def audit_centering_contract(contract: Mapping[str, Any]) -> dict[str, object]:
    """拒绝中心化核读取待估目标或预先禁止的解析输入。"""
    uses = contract.get("uses", ())
    if isinstance(uses, str):
        uses = (uses,)
    try:
        forbidden_inputs = tuple(sorted(set(uses).intersection(FORBIDDEN_CENTERING_INPUTS)))
    except TypeError as error:
        raise ValueError("contract uses 必须为可哈希输入的可迭代对象") from error

    classification = (
        "centered_kernel_uses_target_or_forbidden_analytic_input"
        if forbidden_inputs
        else "centering_input_not_rejected_by_forbidden_input_audit"
    )
    return {
        "classification": classification,
        "forbidden_inputs": forbidden_inputs,
    }


def write_certificate(output_directory: Path, limit: int = 60) -> None:
    """保留第三任务的证书 API，本任务不生成任何文件。"""
    del output_directory, limit
    raise NotImplementedError("证书写出将在任务三实现")


def main() -> None:
    """输出有限 LCM Gram 能量与普通 Cauchy 界的命令行摘要。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=60, help="审计的正整数上限")
    arguments = parser.parse_args()
    limit = _require_positive_integer(arguments.limit, "limit")
    print(
        json.dumps(
            {
                "slug": SLUG,
                "limit": limit,
                "lcm_mobius_energy": lcm_mobius_energy(limit),
                "lambda_square_energy": lambda_square_energy(limit),
                "ordinary_cauchy_projection_bound": ordinary_cauchy_projection_bound(limit),
                "six_multiple_non_prime_power_witnesses": six_multiple_non_prime_power_witnesses(
                    limit
                ),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
