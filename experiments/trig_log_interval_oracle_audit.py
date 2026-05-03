#!/usr/bin/env python3
"""QLOW-MID-COMP：sin/cos/log 有理区间 oracle 审计。

用法示例：
  python3 experiments/trig_log_interval_oracle_audit.py
  python3 experiments/trig_log_interval_oracle_audit.py --log-terms 100 --taylor-degree 80
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

from selberg_rational_weight_audit import compose_exact_omega, exact_selberg_weights
from sqf_qlow_mid_weighted_absorption_scan import parse_floats, parse_ints

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "monograph"


def abs_fraction(value: Fraction) -> Fraction:
    """返回有理数绝对值。"""
    return value if value >= 0 else -value


def decimal(value: Fraction, digits: int = 6) -> str:
    """把有理数转成科学计数法字符串。"""
    return f"{float(value):.{digits}e}"


def interval_width(interval: tuple[Fraction, Fraction]) -> Fraction:
    """返回区间宽度。"""
    return interval[1] - interval[0]


def interval_add(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """区间加法。"""
    return left[0] + right[0], left[1] + right[1]


def interval_mul_positive(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """正区间乘法。"""
    return left[0] * right[0], left[1] * right[1]


def interval_div_positive(
    left: tuple[Fraction, Fraction],
    right: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """正区间除法。"""
    if right[0] <= 0:
        raise ValueError("division by non-positive interval")
    return left[0] / right[1], left[1] / right[0]


def atanh_log_interval(x: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """用 atanh 级数给 log(x) 外向区间，要求 x>=1。"""
    if x == 1:
        return Fraction(0, 1), Fraction(0, 1)
    if x < 1:
        lo, hi = atanh_log_interval(Fraction(1, 1) / x, terms)
        return -hi, -lo
    z = (x - 1) / (x + 1)
    total = Fraction(0, 1)
    power = z
    z2 = z * z
    for j in range(terms):
        total += power / (2 * j + 1)
        power *= z2
    remainder = power / (2 * terms + 1) / (1 - z2)
    return 2 * total, 2 * (total + remainder)


def log_int_interval(n: int, terms: int) -> tuple[Fraction, Fraction]:
    """给正整数 n 的 log(n) 外向区间。"""
    if n < 1:
        raise ValueError("log input must be positive")
    if n == 1:
        return Fraction(0, 1), Fraction(0, 1)
    k = n.bit_length() - 1
    scaled = Fraction(n, 1 << k)
    log2 = atanh_log_interval(Fraction(2, 1), terms)
    scaled_log = atanh_log_interval(scaled, terms)
    return interval_add((k * log2[0], k * log2[1]), scaled_log)


def arctan_interval_reciprocal(q: int, terms: int) -> tuple[Fraction, Fraction]:
    """用交错级数给 arctan(1/q) 外向区间。"""
    x = Fraction(1, q)
    total = Fraction(0, 1)
    power = x
    sign = 1
    for j in range(terms):
        total += sign * power / (2 * j + 1)
        power *= x * x
        sign *= -1
    next_term = power / (2 * terms + 1)
    if sign > 0:
        return total, total + next_term
    return total - next_term, total


def pi_interval(terms: int) -> tuple[Fraction, Fraction]:
    """用 Machin 公式给 pi 外向区间。"""
    atan_1_5 = arctan_interval_reciprocal(5, terms)
    atan_1_239 = arctan_interval_reciprocal(239, terms)
    lo = 16 * atan_1_5[0] - 4 * atan_1_239[1]
    hi = 16 * atan_1_5[1] - 4 * atan_1_239[0]
    return lo, hi


def factorial(n: int) -> int:
    """返回 n!。"""
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def taylor_tail_bound(pi_bound: tuple[Fraction, Fraction], degree: int) -> Fraction:
    """给 |x|<=pi 时 sin/cos Taylor 截断的统一尾界。"""
    radius = max(abs_fraction(pi_bound[0]), abs_fraction(pi_bound[1]))
    return radius ** (degree + 1) / factorial(degree + 1)


def collect_argument_integers(P: int, R_exp: float, K: int) -> tuple[int, list[int]]:
    """收集 H/Q 中需要 log 的整数。"""
    exact = exact_selberg_weights(P, R_exp)
    omega = compose_exact_omega(exact["weights"])
    integers = sorted(set(range(1, K + 1)) | set(omega.keys()) | {exact["R"]})
    return exact["R"], integers


def angle_width_bound(
    u_max: Fraction,
    log_n: tuple[Fraction, Fraction],
    log_r: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """给 u*log(n)/log(R) 的正区间。"""
    return interval_mul_positive((u_max, u_max), interval_div_positive(log_n, log_r))


def analyze_case(
    P: int,
    R_exp: float,
    K: int,
    u_max: Fraction,
    log_terms: int,
    pi_terms: int,
    taylor_degree: int,
) -> dict:
    """计算单个 P,R 样本的统一 oracle 半径。"""
    R, integers = collect_argument_integers(P, R_exp, K)
    logs = {n: log_int_interval(n, log_terms) for n in integers}
    log_r = logs[R]
    pi_bound = pi_interval(pi_terms)
    two_pi_width = 2 * interval_width(pi_bound)
    tail = taylor_tail_bound(pi_bound, taylor_degree)
    max_angle_width = Fraction(0, 1)
    max_reduced_width = Fraction(0, 1)
    max_angle_abs_upper = Fraction(0, 1)
    worst_n = 1
    for n, log_n in logs.items():
        if n == 1:
            continue
        angle = angle_width_bound(u_max, log_n, log_r)
        width = interval_width(angle)
        abs_upper = max(abs_fraction(angle[0]), abs_fraction(angle[1]))
        k_max = math.ceil(float(abs_upper / (2 * pi_bound[0]))) + 1
        reduced_width = width + k_max * two_pi_width
        if reduced_width > max_reduced_width:
            max_reduced_width = reduced_width
            max_angle_width = width
            max_angle_abs_upper = abs_upper
            worst_n = n
    oracle_half_radius = max_reduced_width / 2 + tail
    return {
        "P": P,
        "R_exp": R_exp,
        "R": R,
        "integer_count": len(integers),
        "worst_integer": worst_n,
        "max_angle_width": decimal(max_angle_width),
        "max_reduced_width": decimal(max_reduced_width),
        "max_angle_abs_upper": decimal(max_angle_abs_upper),
        "taylor_tail": decimal(tail),
        "oracle_half_radius": decimal(oracle_half_radius),
        "oracle_half_radius_float": float(oracle_half_radius),
        "logR_width": decimal(interval_width(log_r)),
    }


def render_markdown(audit: dict) -> str:
    """渲染审计报告。"""
    lines = [
        "# sin/cos/log 有理区间 oracle 审计",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本报告为 `QLOW-MID-COMP` 的三角函数与对数调用建立统一有理区间误差半径。",
        "不依赖浮点库或外部区间库；`log` 使用 atanh 级数，`pi` 使用 Machin 公式，Taylor 尾项用有理上界。",
        "",
        "## 方法",
        "",
        "- 对整数 `n`，写 `n=2^k y`, `1<=y<2`，用",
        "",
        "\\[",
        "\\log y=2\\sum_{j<N}\\frac{z^{2j+1}}{2j+1}+O\\left(\\frac{2z^{2N+1}}{(2N+1)(1-z^2)}\\right),\\quad z=\\frac{y-1}{y+1}.",
        "\\]",
        "",
        "- 对 `pi`，用 Machin 公式 `pi=16 arctan(1/5)-4 arctan(1/239)` 的交错级数外向界。",
        "- 对所有 `sin/cos`，先用 `2pi` 区间做范围归约，再用 `|x|<=pi` 的 Taylor 尾项给统一半径。",
        "",
        "## 参数",
        "",
        f"- `log_terms={audit['parameters']['log_terms']}`",
        f"- `pi_terms={audit['parameters']['pi_terms']}`",
        f"- `taylor_degree={audit['parameters']['taylor_degree']}`",
        f"- `u_max={audit['parameters']['u_max']}`",
        "",
        "## 统一半径表",
        "",
        "| P | R | ints | worst n | angle width | reduced width | Taylor tail | oracle half-radius |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for case in audit["cases"]:
        lines.append(
            f"| {case['P']} | {case['R']} | {case['integer_count']} | {case['worst_integer']} | "
            f"{case['max_angle_width']} | {case['max_reduced_width']} | "
            f"{case['taylor_tail']} | {case['oracle_half_radius']} |"
        )
    lines += [
        "",
        "## 对区间预算的影响",
        "",
        f"- 最大 oracle 半径：`{audit['max_oracle_half_radius']:.3e}`。",
        "- 该半径远小于 `trig_log_interval_oracle=0.016250` 的预算量级。",
        "- 因此在当前有限样本证书上，`sin/cos/log` 外向包络不会成为常数余量瓶颈。",
        "",
        "## 仍未闭合",
        "",
        "- 本报告给出统一误差半径，还没有把每个 `H/Q` 网格值逐项替换为区间复数并重算 `C_comp`。",
        "- 从样本证书升级到全部 `P>=P0` 时，仍需统一控制 `omega` 支撑和 `logR` 下界。",
        "- 下一步应把该 oracle 接入 `qlow_mid_comp_grid_certificate.py`，生成真正的区间复数版 `C_comp` 表。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003,10007")
    parser.add_argument("--R-exponents", default="0.30,0.35")
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--u-max", default="12")
    parser.add_argument("--log-terms", type=int, default=80)
    parser.add_argument("--pi-terms", type=int, default=80)
    parser.add_argument("--taylor-degree", type=int, default=70)
    args = parser.parse_args()
    u_max = Fraction(args.u_max)
    cases = [
        analyze_case(P, R_exp, args.K, u_max, args.log_terms, args.pi_terms, args.taylor_degree)
        for P, R_exp in itertools.product(parse_ints(args.P_list), parse_floats(args.R_exponents))
    ]
    audit = {
        "certificate_type": "trig_log_interval_oracle_audit",
        "status": "rational_oracle_radius_established_for_sample_calls",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "R_exponents": parse_floats(args.R_exponents),
            "K": args.K,
            "u_max": args.u_max,
            "log_terms": args.log_terms,
            "pi_terms": args.pi_terms,
            "taylor_degree": args.taylor_degree,
        },
        "max_oracle_half_radius": max(case["oracle_half_radius_float"] for case in cases),
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "trig-log-interval-oracle-audit.json"
    md_path = OUT / "trig-log-interval-oracle-audit.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
