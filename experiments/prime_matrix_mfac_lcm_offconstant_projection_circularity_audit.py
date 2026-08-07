#!/usr/bin/env python3
"""审计实际整数 LCM 核中直接去常数投影的循环边界。

用法示例：
  python3 -m unittest experiments.prime_matrix_mfac_lcm_offconstant_projection_circularity_audit_test -v

本模块只审计有限实际整数上的直接秩一 ``e_1`` 投影恒等式及输入来源合同，
不提供任何关于 ψ 误差、零点排除、RH 或全局不存在性的结论。
"""

from __future__ import annotations

import argparse
import json
import math
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

from prime_matrix_mfac_actual_lcm_gram_energy_audit import (
    lcm_gram_entry,
    mobius,
    von_mangoldt,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-lcm-offconstant-projection-circularity-audit"

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


def audit_lcm_offconstant_projection_circularity(limit: int = 60) -> dict[str, Any]:
    """汇总直接秩一 ``e_1`` 投影的有限实际整数循环审计。"""
    checked_limit = _require_positive_integer(limit, "limit")
    uncentered = direct_projection_data(checked_limit, 0.0)
    unique_alpha = float(uncentered["unique_orthogonal_alpha"])
    orthogonalized = direct_projection_data(checked_limit, unique_alpha)
    circular_contract = audit_direct_projection_contract(
        {"alpha_uses": ("psi(X)-X",)}
    )
    independent_named_contract = audit_direct_projection_contract(
        {"alpha_uses": ("independent_arithmetic_name",)}
    )
    identity_residual = abs(
        float(uncentered["g_e1_inner_product"])
        - float(uncentered["chebyshev_error"])
    )
    defect_residual = abs(
        float(orthogonalized["actual_defect"])
        - float(orthogonalized["theoretical_defect"])
    )

    return {
        "slug": SLUG,
        "limit": checked_limit,
        "actual_lcm_e1_projection_identity_available": True,
        "unique_e1_orthogonal_alpha_requires_target_error": True,
        "direct_e1_projection_template_rejected": True,
        "noncircular_offconstant_witness_constructed": False,
        "mathematical_nonexistence": False,
        "actual_chebyshev_mellin_contraction": False,
        "rh": False,
        "next_positive_gate": (
            "NoncircularActualOffConstantCoerciveWitnessBeforeMellin"
        ),
        "uncentered_projection": uncentered,
        "unique_alpha_orthogonalization": orthogonalized,
        "projection_identity_floating_point_audit_residual": identity_residual,
        "orthogonal_defect_floating_point_audit_residual": defect_residual,
        "rejected_direct_target_dependent_contract": circular_contract,
        "independent_named_input_contract": independent_named_contract,
    }


def _render_markdown(payload: Mapping[str, Any]) -> str:
    """渲染直接秩一投影循环审计的边界说明。"""
    uncentered = payload["uncentered_projection"]
    orthogonalized = payload["unique_alpha_orthogonalization"]
    rejected = payload["rejected_direct_target_dependent_contract"]
    independent = payload["independent_named_input_contract"]
    return f"""# MFAC LCM 去常数投影循环审计

## 范围

本证书只审计实际整数区间 \\(1\\le n\\le {payload['limit']}\\) 上的直接秩一
\\(e_1\\) 投影模板。LCM Gram 核为

\\[
K_X(d,e)=\\left\\lfloor\\frac{{X}}{{\\operatorname{{lcm}}(d,e)}}\\right\\rfloor.
\\]

令 \\(w_d=-\\mu(d)\\log d\\)、\\(g=w-e_1\\)。在实数域中，直接计算给出

\\[
\\langle g,e_1\\rangle_{{K_X}}=\\psi(X)-X,
\\qquad \\lVert e_1\\rVert_{{K_X}}^2=X.
\\]

当前有限精度审计的投影残差为
`{payload['projection_identity_floating_point_audit_residual']}`；未中心化读数为
`{uncentered['g_e1_inner_product']}`，Chebyshev 误差读数为
`{uncentered['chebyshev_error']}`。

## 唯一系数与循环

对任意实数 \\(\\alpha\\)，直接缺陷满足

\\[
\\langle g-\\alpha e_1,e_1\\rangle_{{K_X}}
=\\psi(X)-X-\\alpha X.
\\]

因此令其正交的唯一系数为
\\(\\alpha_X=(\\psi(X)-X)/X\\)。本证书的该系数读数为
`{uncentered['unique_orthogonal_alpha']}`，正交化后的有限精度缺陷为
`{orthogonalized['actual_defect']}`，理论缺陷残差为
`{payload['orthogonal_defect_floating_point_audit_residual']}`。

这说明**只拒绝直接秩一** \\(e_1\\) 模板：若它把 `psi(X)-X` 用作系数输入，
分类为 `{rejected['classification']}`，即在中心化定义时读取待控制的目标误差。

## 未被虚构的出口

不读取目标误差的命名输入只被分类为
`{independent['classification']}`，而不是被说成已经构造的独立算术对象。因此本步不排除
非秩一、非后验的实际算术结构；它也不证明所有可能的 coercive 能量机制不存在。

## 结论边界

本步固定
`actual_lcm_e1_projection_identity_available=true`、
`unique_e1_orthogonal_alpha_requires_target_error=true` 与
`direct_e1_projection_template_rejected=true`。它**不是 RH** 证明，也不提供
\\(\\psi\\) 平滑误差、Mellin 收缩或零点排除；
`noncircular_offconstant_witness_constructed=false`、
`mathematical_nonexistence=false`、
`actual_chebyshev_mellin_contraction=false`、`rh=false`。

下一正向数学门为
`{payload['next_positive_gate']}`。
"""


def write_certificate(output_directory: Path, limit: int = 60) -> dict[str, Path]:
    """写出直接秩一投影循环审计的 JSON 与 Markdown 证书。"""
    if not isinstance(output_directory, Path):
        raise ValueError("output_directory 必须为 Path")
    if not output_directory.is_dir():
        raise ValueError("output_directory 必须是存在的目录")

    payload = audit_lcm_offconstant_projection_circularity(limit)
    json_path = output_directory / f"{SLUG}.json"
    markdown_path = output_directory / f"{SLUG}.md"
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    markdown_path.write_text(_render_markdown(payload), encoding="utf-8")
    return {"json_path": json_path, "markdown_path": markdown_path}


def main() -> None:
    """生成 LCM 去常数投影循环证书并打印输出路径。"""
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
