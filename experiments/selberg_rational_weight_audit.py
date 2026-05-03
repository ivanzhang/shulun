#!/usr/bin/env python3
"""Selberg 最优权的有理线性代数审计。

用法示例：
  python3 experiments/selberg_rational_weight_audit.py
  python3 experiments/selberg_rational_weight_audit.py --P-list 2003 --R-exponents 0.30
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

from sqf_qlow_mid_weighted_absorption_scan import (
    lcm,
    optimal_q0_weights,
    parse_floats,
    parse_ints,
    primes_upto,
    squarefree_products,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "monograph"


def fraction_to_decimal(value: Fraction, digits: int = 18) -> str:
    """把有理数转为固定精度小数字符串，便于审稿表阅读。"""
    return f"{float(value):.{digits}g}"


def solve_fraction_system(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    """使用有理高斯消元精确求解线性方程组。"""
    n = len(rhs)
    rows = [matrix[i][:] + [rhs[i]] for i in range(n)]
    for col in range(n):
        pivot = None
        for row in range(col, n):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            raise ValueError("singular rational matrix")
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [entry / divisor for entry in rows[col]]
        for row in range(n):
            if row == col:
                continue
            factor = rows[row][col]
            if factor == 0:
                continue
            rows[row] = [rows[row][j] - factor * rows[col][j] for j in range(n + 1)]
    return [rows[i][n] for i in range(n)]


def exact_selberg_weights(P: int, R_exp: float) -> dict:
    """精确求解 λ1=1 的 Selberg 二次型最优权。"""
    R = max(2, int(P**R_exp))
    primes = primes_upto(math.isqrt(P))
    divisors = [d for d, _ in squarefree_products(primes, R)]
    matrix = [[Fraction(1, lcm(d, e)) for e in divisors] for d in divisors]
    rhs = [Fraction(1 if d == 1 else 0, 1) for d in divisors]
    inv_e1 = solve_fraction_system(matrix, rhs)
    denom = inv_e1[0]
    weights = {divisors[i]: inv_e1[i] / denom for i in range(len(divisors))}
    q0 = Fraction(1, 1) / denom
    return {
        "R": R,
        "divisors": divisors,
        "matrix": matrix,
        "weights": weights,
        "q0": q0,
    }


def compose_exact_omega(weights: dict[int, Fraction]) -> dict[int, Fraction]:
    """精确合成 omega_l=sum_[d,e]=l λ_d λ_e。"""
    omega: dict[int, Fraction] = {}
    items = list(weights.items())
    for d1, weight1 in items:
        for d2, weight2 in items:
            ell = lcm(d1, d2)
            omega[ell] = omega.get(ell, Fraction(0, 1)) + weight1 * weight2
    return omega


def verify_normal_equations(
    matrix: list[list[Fraction]],
    divisors: list[int],
    weights: dict[int, Fraction],
    q0: Fraction,
) -> dict:
    """验证 Aλ=q0 e1 和 λ1=1。"""
    max_residual = Fraction(0, 1)
    residuals = []
    for row, d in enumerate(divisors):
        total = sum(matrix[row][col] * weights[divisors[col]] for col in range(len(divisors)))
        target = q0 if d == 1 else Fraction(0, 1)
        residual = total - target
        residuals.append(residual)
        max_residual = max(max_residual, abs(residual))
    lambda_one_residual = weights.get(1, Fraction(0, 1)) - Fraction(1, 1)
    return {
        "max_normal_residual": max_residual,
        "lambda_one_residual": lambda_one_residual,
        "all_exact_zero": max_residual == 0 and lambda_one_residual == 0,
        "residuals": residuals,
    }


def fraction_bit_size(value: Fraction) -> int:
    """估计有理数分子分母的二进制复杂度。"""
    return max(abs(value.numerator).bit_length(), value.denominator.bit_length())


def analyze_case(P: int, R_exp: float) -> dict:
    """对一个 P,R 组合生成精确审计结果。"""
    exact = exact_selberg_weights(P, R_exp)
    omega = compose_exact_omega(exact["weights"])
    verification = verify_normal_equations(
        exact["matrix"],
        exact["divisors"],
        exact["weights"],
        exact["q0"],
    )
    _, float_weights = optimal_q0_weights(P, R_exp)
    max_float_diff = max(
        abs(float(exact["weights"][d]) - float_weights.get(d, 0.0))
        for d in exact["divisors"]
    )
    q0_from_omega = sum(weight / ell for ell, weight in omega.items())
    variation = sum(abs(weight) / ell for ell, weight in omega.items())
    signed_l1 = sum(abs(weight) for weight in omega.values())
    max_weight_bits = max(fraction_bit_size(weight) for weight in exact["weights"].values())
    max_omega_bits = max(fraction_bit_size(weight) for weight in omega.values())
    return {
        "P": P,
        "R_exp": R_exp,
        "R": exact["R"],
        "matrix_size": len(exact["divisors"]),
        "omega_size": len(omega),
        "divisors": exact["divisors"],
        "q0": {
            "numerator": exact["q0"].numerator,
            "denominator": exact["q0"].denominator,
            "decimal": fraction_to_decimal(exact["q0"]),
        },
        "q0_from_omega_matches": q0_from_omega == exact["q0"],
        "variation": {
            "numerator": variation.numerator,
            "denominator": variation.denominator,
            "decimal": fraction_to_decimal(variation),
        },
        "omega_signed_l1": {
            "numerator": signed_l1.numerator,
            "denominator": signed_l1.denominator,
            "decimal": fraction_to_decimal(signed_l1),
        },
        "max_float_weight_diff": max_float_diff,
        "max_weight_bits": max_weight_bits,
        "max_omega_bits": max_omega_bits,
        "normal_equations_exact": verification["all_exact_zero"],
        "max_normal_residual": str(verification["max_normal_residual"]),
        "lambda_one_residual": str(verification["lambda_one_residual"]),
    }


def render_markdown(audit: dict) -> str:
    """渲染审计报告。"""
    lines = [
        "# Selberg 最优权有理线性代数审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告把 `QLOW-MID-COMP` 中的 Selberg 最优权求解从浮点线性代数替换为有理精确审计。",
        "审计对象是有限样本中的矩阵",
        "",
        "\\[",
        "A_{d,e}=\\frac1{[d,e]},\\qquad d,e\\le R,\\quad d,e\\ \\text{squarefree},",
        "\\]",
        "",
        "以及约束 `λ_1=1` 下的最小二次型。精确解满足",
        "",
        "\\[",
        "A\\lambda=q_0 e_1,\\qquad \\lambda_1=1.",
        "\\]",
        "",
        "## 审计摘要",
        "",
        "| P | R | size | q0 | Vomega | exact normal eq | max float diff | bits λ/ω |",
        "|---:|---:|---:|---:|---:|:---:|---:|---:|",
    ]
    for case in audit["cases"]:
        lines.append(
            f"| {case['P']} | {case['R']} | {case['matrix_size']} | "
            f"{case['q0']['decimal']} | {case['variation']['decimal']} | "
            f"{'Y' if case['normal_equations_exact'] else 'N'} | "
            f"{case['max_float_weight_diff']:.3e} | "
            f"{case['max_weight_bits']}/{case['max_omega_bits']} |"
        )
    lines += [
        "",
        "## 对区间预算的影响",
        "",
        "该审计精确闭合了有限样本的 Selberg 线性系统：",
        "",
        "```text",
        "lambda_1=1, A lambda=q0 e1, q0=sum omega_l/l",
        "```",
        "",
        "因此 `selberg_weight_solver` 的数值求解误差在这些样本上可降为零。原预算项 `0.013` 不应再解释为浮点消元误差，而应改解释为：",
        "",
        "1. 有理数表格抄录与外向输出误差；",
        "2. 从有限样本到 `P>=P0` 的统一 Selberg 矩常数证明；",
        "3. `sum |omega_l| log(l)/l` 中对数 oracle 的区间误差。",
        "",
        "这一步没有闭合 `Phihat` 与三角函数区间问题，但它移除了最容易被审稿质疑的浮点线性代数黑箱。",
        "",
        "## 仍未闭合",
        "",
        "- 本审计只覆盖输入样本中的有限矩阵。",
        "- `log(l)` 的有理区间包络仍属于 `trig_log_interval_oracle`。",
        "- 若要证明全部 `P>=P0`，还需给出 `V_omega` 与对数矩的统一解析上界。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003,10007")
    parser.add_argument("--R-exponents", default="0.30,0.35")
    args = parser.parse_args()
    cases = [
        analyze_case(P, R_exp)
        for P, R_exp in itertools.product(parse_ints(args.P_list), parse_floats(args.R_exponents))
    ]
    audit = {
        "certificate_type": "selberg_rational_weight_audit",
        "status": "rational_linear_algebra_closed_for_sample_matrices",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "R_exponents": parse_floats(args.R_exponents),
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "selberg-rational-weight-audit.json"
    md_path = OUT / "selberg-rational-weight-audit.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
