"""截断 Möbius--log 系数族的有限形式恒等式工具。

用法示例：
  from experiments.prime_matrix_mfac_unconditional_w1_w2_log_saving_audit import (
      formal_mobius_lambda,
  )
  assert formal_mobius_lambda(6) == {2: Fraction(-1, 1), 3: Fraction(-1, 1)}
"""

from __future__ import annotations

from collections.abc import Mapping
from fractions import Fraction

from experiments.prime_matrix_mfac_truncated_mobius_log_coercivity_audit import (
    mobius_value,
)


def _require_index(index: object) -> int:
    """验证形式恒等式使用的正内建整数索引。"""
    if type(index) is not int or index < 1:
        raise ValueError("index 必须是至少为 1 的内建整数")
    return index


def _prime_factor_exponents(index: int) -> dict[int, int]:
    """以试除法返回正整数的素因子指数。"""
    remaining = index
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        if exponent:
            factors[divisor] = exponent
        divisor += 1
    if remaining > 1:
        factors[remaining] = 1
    return factors


def formal_negative_mobius_log(index: object) -> dict[int, Fraction]:
    """把 -μ(n) log n 表示为按素数分组的精确有理形式系数。"""
    checked_index = _require_index(index)
    mobius = mobius_value(checked_index)
    if checked_index == 1 or mobius == 0:
        return {}
    return {
        prime: Fraction(-mobius * exponent, 1)
        for prime, exponent in _prime_factor_exponents(checked_index).items()
    }


def formal_mobius_lambda(index: object) -> dict[int, Fraction]:
    """计算 (μ*Λ)(n) 的按素数对数分组的精确形式系数。"""
    checked_index = _require_index(index)
    coefficients: dict[int, Fraction] = {}
    for divisor in range(1, checked_index + 1):
        if checked_index % divisor:
            continue
        mobius = mobius_value(divisor)
        if mobius == 0:
            continue
        quotient_factors = _prime_factor_exponents(checked_index // divisor)
        if len(quotient_factors) != 1:
            continue
        prime = next(iter(quotient_factors))
        coefficients[prime] = coefficients.get(prime, Fraction(0, 1)) + Fraction(
            mobius, 1
        )
    return {
        prime: coefficient
        for prime, coefficient in coefficients.items()
        if coefficient != 0
    }


def _checked_fraction_mapping(
    mapping: Mapping[int, Fraction],
    name: str,
) -> dict[int, Fraction]:
    """验证 Abel 恒等式的一组非空正整数有理数数据。"""
    if not isinstance(mapping, Mapping) or not mapping:
        raise ValueError(f"{name} 必须是非空 Mapping")
    checked: dict[int, Fraction] = {}
    for index, value in mapping.items():
        _require_index(index)
        if not isinstance(value, Fraction):
            raise ValueError(f"{name} 的值必须是 Fraction")
        checked[index] = value
    return checked


def abel_sum_by_parts(
    values: Mapping[int, Fraction],
    weights: Mapping[int, Fraction],
) -> dict[str, Fraction]:
    """精确验证同一有限索引集上的 Abel 分部求和恒等式。"""
    checked_values = _checked_fraction_mapping(values, "values")
    checked_weights = _checked_fraction_mapping(weights, "weights")
    if checked_values.keys() != checked_weights.keys():
        raise ValueError("values 与 weights 必须具有相同的非空索引集")

    ordered_indices = sorted(checked_values)
    direct = sum(
        (
            checked_values[index] * checked_weights[index]
            for index in ordered_indices
        ),
        Fraction(0, 1),
    )
    prefix = Fraction(0, 1)
    summation_by_parts = Fraction(0, 1)
    for position, index in enumerate(ordered_indices):
        prefix += checked_values[index]
        if position + 1 == len(ordered_indices):
            summation_by_parts += prefix * checked_weights[index]
        else:
            next_index = ordered_indices[position + 1]
            summation_by_parts += prefix * (
                checked_weights[index] - checked_weights[next_index]
            )

    return {
        "direct": direct,
        "summation_by_parts": summation_by_parts,
        "residual": direct - summation_by_parts,
    }
