#!/usr/bin/env python3
"""审计实际整数上的 LCM Gram 能量恒等式与中心化输入边界。

用法示例：
  python3 experiments/prime_matrix_mfac_actual_lcm_gram_energy_audit.py --limit 60

本模块只计算有限实际整数区间内的代数恒等式及其有限精度数值实例和普通 Cauchy 界，
不提供任何关于 ψ 平滑误差、零点位置或 RH 的结论。
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Iterable, Mapping
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
    limit: int, coefficients: Mapping[int, int | float]
) -> float:
    """计算内建有限实系数 LCM Gram 核对应的有限精度二次型。"""
    checked_limit = _require_positive_integer(limit, "limit")
    if not isinstance(coefficients, Mapping):
        raise ValueError("coefficients 必须为有限 Mapping")

    checked_coefficients: dict[int, float] = {}
    for divisor, weight in coefficients.items():
        checked_divisor = _require_divisor_within_limit(
            checked_limit, divisor, "coefficient divisor"
        )
        if type(weight) not in (int, float):
            raise ValueError("coefficient weight 必须为非布尔的内建 int 或 float")
        try:
            checked_weight = float(weight)
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("coefficient weight 必须可转换为有限实数") from error
        if not math.isfinite(checked_weight):
            raise ValueError("coefficient weight 必须为有限实数")
        checked_coefficients[checked_divisor] = checked_weight

    terms: list[float] = []
    for left, left_weight in checked_coefficients.items():
        for right, right_weight in checked_coefficients.items():
            term = (
                left_weight
                * right_weight
                * lcm_gram_entry(checked_limit, left, right)
            )
            if not math.isfinite(term):
                raise ValueError("LCM Gram 二次型乘积项必须为有限实数")
            terms.append(term)
    try:
        result = math.fsum(terms)
    except OverflowError as error:
        raise ValueError("LCM Gram 二次型总和必须为有限实数") from error
    if not math.isfinite(result):
        raise ValueError("LCM Gram 二次型总和必须为有限实数")
    return result


def lcm_mobius_energy(limit: int) -> float:
    """有限精度数值验证对应实数域精确恒等式的 LCM Gram 能量。"""
    checked_limit = _require_positive_integer(limit, "limit")
    coefficients = {
        divisor: -mobius(divisor) * math.log(divisor)
        for divisor in range(1, checked_limit + 1)
    }
    return lcm_gram_quadratic_form(checked_limit, coefficients)


def lambda_square_energy(limit: int) -> float:
    """以有限精度逐项计算对应实数平方和的数值实例。"""
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
    """记录常数方向的有限精度投影和普通 Cauchy 上界。"""
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
    if not isinstance(contract, Mapping):
        raise ValueError("contract 必须为 Mapping")
    uses = contract.get("uses", ())
    try:
        if isinstance(uses, str) or not isinstance(uses, Iterable):
            raise ValueError("contract uses 必须为非裸字符串的可迭代字符串对象")
        checked_uses = tuple(uses)
    except TypeError as error:
        raise ValueError("contract uses 必须为非裸字符串的可迭代字符串对象") from error
    if not all(isinstance(item, str) for item in checked_uses):
        raise ValueError("contract uses 的所有元素必须为字符串")
    forbidden_inputs = tuple(
        sorted(set(checked_uses).intersection(FORBIDDEN_CENTERING_INPUTS))
    )

    classification = (
        "centered_kernel_uses_target_or_forbidden_analytic_input"
        if forbidden_inputs
        else "centering_input_not_rejected_by_forbidden_input_audit"
    )
    return {
        "classification": classification,
        "forbidden_inputs": forbidden_inputs,
    }


def audit_actual_lcm_gram_energy(limit: int) -> dict[str, Any]:
    """汇总实际整数 LCM Gram 能量的有限读数与未闭合边界。"""
    checked_limit = _require_positive_integer(limit, "limit")
    mobius_energy = lcm_mobius_energy(checked_limit)
    lambda_energy = lambda_square_energy(checked_limit)
    centering_contract = audit_centering_contract({"uses": ("psi(X)",)})

    return {
        "slug": SLUG,
        "limit": checked_limit,
        "actual_lcm_gram_identity_available": True,
        "fixed_actual_integer_embedding": True,
        "fixed_actual_chebyshev_measure": True,
        "non_tagged_signed_kernel_available": True,
        "positive_semidefinite_energy_identity_available": True,
        "ordinary_cauchy_constant_direction_obstruction_present": True,
        "centered_kernel_independent_arithmetic_input_constructed": False,
        "actual_chebyshev_mellin_contraction_present": False,
        "mathematical_nonexistence_proved": False,
        "rh_proved": False,
        "next_positive_gate": "ActualOffConstantCoerciveEnergyIdentityBeforeMellin",
        "mobius_lcm_energy": mobius_energy,
        "lambda_square_energy": lambda_energy,
        "mobius_lambda_floating_point_audit_residual": abs(
            mobius_energy - lambda_energy
        ),
        "chebyshev_increment_energy": chebyshev_increment_energy(checked_limit),
        "ordinary_cauchy_projection": ordinary_cauchy_projection_bound(checked_limit),
        "six_multiple_non_prime_power_witnesses": six_multiple_non_prime_power_witnesses(
            checked_limit
        ),
        "rejected_psi_centering_contract_example": centering_contract,
    }


def _render_markdown(payload: Mapping[str, Any]) -> str:
    """把有限审计载荷渲染为带数学边界的中文 Markdown。"""
    projection = payload["ordinary_cauchy_projection"]
    witnesses = ", ".join(
        str(value) for value in payload["six_multiple_non_prime_power_witnesses"]
    )
    return rf"""# MFAC 实际 LCM Gram 能量审计

## 范围

本证书只审计实际整数区间 \(1\\le n\\le {payload['limit']}\) 内的有限结构。LCM Gram
核为

\[
K_X(d,e)=\\left\\lfloor\\frac{{X}}{{\\operatorname{{lcm}}(d,e)}}\\right\\rfloor,
\]

它精确等于两个实际整除特征函数在该有限区间内的 Gram 内积。因此，该核给出一个
非标签的正半定实际整数核；这不是任意自由模型或后验标签化结构。

## Möbius--Lambda 能量

实数域中有精确恒等式

\[
\\Lambda(n)=-\\sum_{{d\\mid n}}\\mu(d)\\log d,
\qquad
\\sum_{{n\\le X}}\\Lambda(n)^2
=\\sum_{{d,e\\le X}}\\mu(d)\\mu(e)\\log d\\log e\,K_X(d,e).
\]

代码对上式在浮点运算下作有限精度数值审计，而不把数值残差称为任何 \(\\psi\)
误差项。当前读数为：LCM Möbius 能量 `{payload['mobius_lcm_energy']}`，
Lambda 平方能量 `{payload['lambda_square_energy']}`，浮点审计残差
`{payload['mobius_lambda_floating_point_audit_residual']}`。

## 常数方向障碍

对 \(\\Lambda(n)-1\) 的普通 Cauchy 投影，常数方向的范数平方为
`{projection['constant_direction_norm_squared']}`，故只产生
\(|\\sum(\\Lambda(n)-1)|^2\\le X\\sum(\\Lambda(n)-1)^2\) 型界。其 \(\\sqrt X\)
常数方向规模正是本审计记录的障碍：仅靠普通 Cauchy 不能导出所需的 off-constant
coercivity 或 Mellin 收缩。六倍数非素数幂见证为：`{witnesses}`。

## 中心化输入边界

中心化合同样本读取 `psi(X)` 时被拒绝，分类为
`{payload['rejected_psi_centering_contract_example']['classification']}`。这只说明该样本
不构成独立算术输入；并未证明数学上所有可能的中心化或收缩机制都不存在。

## 结论边界

本成果固定了实际整数嵌入、实际 Chebyshev 测度、非标签带符号 LCM 核及其正半定
能量身份，并记录普通 Cauchy 的常数方向障碍。它**不是** \(\\psi\) 平滑误差估计、
零点排除或 RH 证明；`actual_chebyshev_mellin_contraction_present=false`、
`mathematical_nonexistence_proved=false`、`rh_proved=false`。

下一正向数学门为
`ActualOffConstantCoerciveEnergyIdentityBeforeMellin`。
"""


def write_certificate(output_directory: Path, limit: int = 60) -> dict[str, Path]:
    """写出实际 LCM Gram 能量审计的 JSON 与 Markdown 证书。"""
    if not isinstance(output_directory, Path):
        raise ValueError("output_directory 必须为 Path")
    if not output_directory.is_dir():
        raise ValueError("output_directory 必须是存在的目录")

    payload = audit_actual_lcm_gram_energy(limit)
    json_path = output_directory / f"{SLUG}.json"
    markdown_path = output_directory / f"{SLUG}.md"
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_path.write_text(_render_markdown(payload), encoding="utf-8")
    return {"json_path": json_path, "markdown_path": markdown_path}


def main() -> None:
    """生成有限 LCM Gram 能量证书并打印输出路径。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=60, help="审计的正整数上限")
    parser.add_argument(
        "--output-directory",
        type=Path,
        default=DOCS,
        help="证书输出目录，默认 docs/monograph",
    )
    arguments = parser.parse_args()
    paths = write_certificate(arguments.output_directory, arguments.limit)
    print(paths["json_path"])
    print(paths["markdown_path"])


if __name__ == "__main__":
    main()
