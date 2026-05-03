#!/usr/bin/env python3
"""显式阈值 P_* 账本计算器。

用法示例：
  python3 experiments/explicit_threshold_ledger.py --show-template
  python3 experiments/explicit_threshold_ledger.py --constants constants.json

说明：
  该脚本只做机械阈值搜索，不替代数学证明。
  若某个原子常数尚未赋值，脚本会明确报错，而不是伪造 P_*。
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

REQUIRED_KEYS = [
    "C_Bell",
    "C_tree",
    "C_edge",
    "C_Rank",
    "C_leaf",
    "C_bd",
    "C_Cheb",
    "A1",
    "mu_row",
    "a_row",
    "mu_col",
    "a_col",
    "delta_row",
    "delta_col",
    "d_row",
    "row_union_mode",
    "A_row",
    "usc_mode",
    "tail_mode",
    "low_moment_C",
    "low_moment_cutoff",
    "c0_safety",
    "C_d4_gate",
    "C_4loc_gate",
    "C_row_err",
    "A_row_err",
    "C_col_err",
    "A_col_err",
    "C_ht",
    "C_rk_star",
    "C_dy",
    "C_co",
    "C_st",
    "C_LV",
    "C_AE",
    "C_L",
    "C_KS",
    "C_poly",
    "B_fourier",
]

POSITIVE_KEYS = [
    "C_Bell",
    "C_tree",
    "C_edge",
    "C_Rank",
    "C_leaf",
    "C_bd",
    "C_Cheb",
    "A1",
    "mu_row",
    "mu_col",
    "delta_row",
    "delta_col",
    "d_row",
    "A_row",
    "low_moment_C",
    "low_moment_cutoff",
    "c0_safety",
    "C_d4_gate",
    "C_4loc_gate",
    "C_row_err",
    "A_row_err",
    "C_col_err",
    "A_col_err",
    "C_ht",
    "C_rk_star",
    "C_dy",
    "C_co",
    "C_st",
    "C_LV",
    "C_AE",
    "C_L",
    "C_KS",
    "B_fourier",
]

NONNEGATIVE_KEYS = ["a_row", "a_col", "C_poly"]

TEMPLATE = {
    "C_Bell": 16,
    "C_tree": 16,
    "C_edge": 4,
    "C_Rank": 16,
    "C_leaf": 8,
    "C_bd": 4,
    "C_Cheb": 2,
    "A1": 50,
    "mu_row": 1,
    "a_row": 1,
    "mu_col": 0.125,
    "a_col": 1,
    "delta_row": 0.25,
    "delta_col": 0.1,
    "d_row": 2.0,
    "row_union_mode": "cluster",
    "A_row": 4.0,
    "usc_mode": "linear",
    "tail_mode": "direct",
    "low_moment_C": 4.0,
    "low_moment_cutoff": 2.0,
    "low_moment_uncapped": True,
    "c0_safety": 12.0,
    "C_d4_gate": 1.0e4,
    "C_4loc_gate": 1.0e8,
    "C_row_err": 1.0e12,
    "A_row_err": 8.0,
    "C_col_err": 1.0e12,
    "A_col_err": 8.0,
    "C_ht": 120.0,
    "C_rk_star": 80.0,
    "C_dy": 120.0,
    "C_co": 160.0,
    "C_st": 80.0,
    "C_LV": 160.0,
    "C_AE": 160.0,
    "C_L": 80.0,
    "C_KS": 80.0,
    "C_poly": 0.0,
    "B_fourier": 20.0,
}


def d4poly_stieltjes_coeffs() -> list[float]:
    """返回 d_4 主项 P3 的系数 a0,a1,a2,a3（升幂）。"""
    gamma = 0.5772156649015328606
    gamma1 = -0.0728158454836767249
    gamma2 = -0.00969036319287231848
    a3 = 1.0 / 6.0
    a2 = -0.5 + 2.0 * gamma
    a1 = 1.0 - 4.0 * gamma + 6.0 * gamma * gamma - 4.0 * gamma1
    a0 = (
        -1.0
        + 4.0 * gamma
        - 6.0 * gamma * gamma
        + 4.0 * gamma1
        + 4.0 * gamma ** 3
        - 12.0 * gamma * gamma1
        + 2.0 * gamma2
    )
    return [a0, a1, a2, a3]


def load_constants(path: Path) -> dict[str, float]:
    data: dict[str, Any] = json.loads(path.read_text())
    missing = [key for key in REQUIRED_KEYS if data.get(key) is None]
    if missing:
        raise SystemExit("缺少原子常数，不能计算 P_*：" + ", ".join(missing))

    constants: dict[str, float | str] = {}
    for key in REQUIRED_KEYS:
        if key in {"row_union_mode", "usc_mode", "tail_mode"}:
            constants[key] = str(data[key])
        else:
            constants[key] = float(data[key])
    bad_positive = [key for key in POSITIVE_KEYS if constants[key] <= 0.0]
    bad_nonnegative = [key for key in NONNEGATIVE_KEYS if constants[key] < 0.0]
    if bad_positive or bad_nonnegative:
        raise SystemExit(
            "常数取值不合法："
            + ", ".join([*bad_positive, *bad_nonnegative])
            + "。正常数必须 >0，指数参数必须 >=0。"
        )
    if constants["delta_row"] > 1.0 or constants["delta_col"] > 1.0:
        raise SystemExit("delta_row 与 delta_col 必须不超过 1。")
    if constants["A_row_err"] <= 1.0 or constants["A_col_err"] <= 1.0:
        raise SystemExit("A_row_err 与 A_col_err 必须大于 1，才能吸收主量误差。")
    if constants["row_union_mode"] not in {"point", "cluster"}:
        raise SystemExit("row_union_mode 必须为 point 或 cluster。")
    if constants["usc_mode"] not in {"quadratic", "linear"}:
        raise SystemExit("usc_mode 必须为 quadratic 或 linear。")
    if constants["tail_mode"] not in {"standard", "optimized", "direct", "chernoff"}:
        raise SystemExit("tail_mode 必须为 standard、optimized、direct 或 chernoff。")
    constants["low_moment_uncapped"] = bool(data.get("low_moment_uncapped", False))
    return constants  # type: ignore[return-value]


def apply_optimization_profile(c: dict[str, float], profile: str) -> None:
    """应用阈值优化预设；只改诊断参数，不替代数学证明。"""
    if profile == "conservative":
        c["A_row"] = 4.0
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
    elif profile == "row2":
        # 对应 6.19a/B.4.1d 二维行簇并合审稿通过档。
        c["A_row"] = 2.0
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
    elif profile == "sub70":
        # 诊断档：需要额外证明 A_row≈1.28 与 delta_col≈0.2。
        c["A_row"] = 1.28
        c["delta_col"] = 0.2
        c["mu_col"] = 0.125
    elif profile == "chernoff52":
        # 诊断档：需要 CH-tail，并强化列误差闸门。
        c["A_row"] = 2.0
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
        c["tail_mode"] = "chernoff"
        c["C_col_err"] = 1.0e11
    elif profile == "chernoff39":
        # 诊断档：需要 CH-tail，并同时强化行列误差闸门。
        c["A_row"] = 2.0
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
        c["tail_mode"] = "chernoff"
        c["C_row_err"] = 1.0e10
        c["C_col_err"] = 1.0e10
    elif profile == "chernoff36":
        # 诊断档：CH-tail + 强化行列误差 + D4-low。
        c["A_row"] = 2.0
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
        c["tail_mode"] = "chernoff"
        c["C_row_err"] = 1.0e10
        c["C_col_err"] = 1.0e10
        c["C_d4_gate"] = 1.0
    elif profile == "chernoff17":
        # 极强诊断档：CH-tail + ERR-row/col 深化 + D4-low。
        c["A_row"] = 2.0
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
        c["tail_mode"] = "chernoff"
        c["C_row_err"] = 1.0e5
        c["C_col_err"] = 1.0e7
        c["C_d4_gate"] = 1.0
    elif profile == "chernoff13":
        # 极限诊断档：进一步提高行坏窗口阈值；由列 Chernoff 尾界卡住。
        c["A_row"] = 2.0
        c["delta_row"] = 0.7
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
        c["tail_mode"] = "chernoff"
        c["C_row_err"] = 1.0e5
        c["C_col_err"] = 1.0e7
        c["C_d4_gate"] = 1.0
    elif profile == "chernoff12":
        # 极限诊断档：列侧已无影响，行 Chernoff 尾界卡住。
        c["A_row"] = 2.0
        c["delta_row"] = 0.7
        c["delta_col"] = 0.1
        c["mu_col"] = 0.125
        c["tail_mode"] = "chernoff"
        c["C_row_err"] = 1.0e5
        c["C_col_err"] = 1.0
        c["C_d4_gate"] = 1.0
    elif profile == "chernoff5":
        # 超强诊断档：在 chernoff12 上进一步强化列阈值、主量和效率。
        c["A_row"] = 2.0
        c["delta_row"] = 0.7
        c["delta_col"] = 0.9
        c["mu_col"] = 1.0
        c["tail_mode"] = "chernoff"
        c["chernoff_efficiency"] = 10.0
        c["C_row_err"] = 1.0e5
        c["C_col_err"] = 1.0
        c["C_d4_gate"] = 1.0
    elif profile == "chernoff1":
        # 极限诊断档：继续强化行误差闸门，接近有限验证区间。
        c["A_row"] = 2.0
        c["delta_row"] = 0.7
        c["delta_col"] = 0.9
        c["mu_col"] = 1.0
        c["tail_mode"] = "chernoff"
        c["chernoff_efficiency"] = 10.0
        c["C_row_err"] = 1.0
        c["A_row_err"] = 8.0
        c["C_col_err"] = 1.0
        c["C_d4_gate"] = 1.0
    else:
        raise SystemExit(f"未知 optimization profile: {profile}")


def derived_constants(c: dict[str, float]) -> dict[str, float]:
    c_sk = 10.0 * (c["C_Bell"] + c["C_tree"] + c["C_edge"] + c["C_leaf"] + 1.0)
    c_euler = 10.0 * (c_sk + c["C_Rank"] + c["C_bd"] + 1.0)
    if c.get("usc_mode") == "linear":
        c_usc = 10.0 * (
            c["C_Bell"] + c["C_tree"] + c["C_edge"] + c["C_Rank"] + c["C_leaf"] + c["C_bd"] + 10.0
        )
    else:
        c_usc = 100.0 * (c_euler + 1.0) ** 2
    c0 = 1.0 / (c["c0_safety"] * c["C_Cheb"] * c["A1"])
    if c.get("tail_mode") == "optimized":
        # 优化模式：仍逐点检查 7.3.5，只减少 m 取整和 beta/(8C) 的安全冗余。
        k_row = min(c0 / 3.0, 1.0 / (8.0 * c_usc))
        k_col = min(c0 / 3.0, 1.0 / (4.0 * c_usc))
        c_row = k_row / 6.0
        c_col = k_col / 3.0
    else:
        k_row = min(c0 / 4.0, 1.0 / (16.0 * c_usc))
        k_col = min(c0 / 4.0, 1.0 / (8.0 * c_usc))
        c_row = k_row / 8.0
        c_col = k_col / 4.0
    c_star = max(
        c["C_ht"],
        c["C_rk_star"],
        c["C_dy"],
        c["C_co"],
        c["C_st"],
        c["C_LV"],
        c["C_AE"],
        c["C_L"],
        c["C_KS"],
        c.get("C_poly", 0.0),
    )
    b_fourier = c["B_fourier"]
    b4 = 4.0 * b_fourier + 4.0 * c_star + 100.0
    b2 = 6.0 * b_fourier + 4.0 * c_star + 120.0
    b1 = 8.0 * b_fourier + 4.0 * c_star + 160.0
    b5 = b_fourier + c["C_st"] + 4.0
    return {
        "C_sk": c_sk,
        "C_Euler": c_euler,
        "C_USC": c_usc,
        "c0": c0,
        "kappa_row": k_row,
        "kappa_col": k_col,
        "c_row": c_row,
        "c_col": c_col,
        "C_star": c_star,
        "B1": b1,
        "B2": b2,
        "B4": b4,
        "B5": b5,
    }




def best_log_probability(
    log_p: float,
    beta: float,
    mu0: float,
    a: float,
    delta: float,
    c_usc: float,
    c0: float,
    low_moment_c: float | None = None,
    low_moment_cutoff: float = 0.0,
    low_moment_uncapped: bool = False,
) -> dict[str, float]:
    # 直接优化 Markov 指数：log Pr <= min_m m log(B(m))。
    # B(m)= (C m)^C log^C(P)/(delta^2 mu)，mu>=mu0 P^beta/log^a(P)。
    m_max = c0 * log_p / 2.0
    if m_max < 1.0 and not low_moment_uncapped:
        return {"log_prob": 0.0, "m": 0.0, "log_bracket": float("inf")}

    def effective_c(m: float) -> float:
        if low_moment_c is not None and m <= low_moment_cutoff:
            return low_moment_c
        return c_usc

    def log_bracket(m: float) -> float:
        c_eff = effective_c(m)
        return (
            c_eff * math.log(c_eff * m)
            + (c_eff + a) * math.log(log_p)
            - 2.0 * math.log(delta)
            - math.log(mu0)
            - beta * log_p
        )

    # moment 阶数必须是整数。早期诊断曾允许连续 m，会在 1<m<2 时过于乐观。
    # 这里枚举端点、low_moment_cutoff 附近和连续临界点附近的整数。
    max_int_m = int(math.floor(m_max))
    if low_moment_uncapped and low_moment_cutoff >= 1.0:
        max_int_m = max(max_int_m, int(math.floor(low_moment_cutoff)))
    if max_int_m < 1:
        return {"log_prob": 0.0, "m": 0.0, "log_bracket": float("inf")}
    candidates_int: set[int] = {1, max_int_m}
    if low_moment_cutoff >= 1.0:
        for value in [math.floor(low_moment_cutoff), math.ceil(low_moment_cutoff)]:
            if 1 <= value <= max_int_m:
                candidates_int.add(int(value))
    critical_log_m = (
        -c_usc
        - (c_usc + a) * math.log(log_p)
        + 2.0 * math.log(delta)
        + math.log(mu0)
        + beta * log_p
    ) / c_usc - math.log(c_usc)
    if critical_log_m < 700.0:
        critical_m = math.exp(critical_log_m)
        for value in range(math.floor(critical_m) - 2, math.floor(critical_m) + 4):
            if 1 <= value <= max_int_m:
                candidates_int.add(value)
    best_m = min(candidates_int, key=lambda m: m * log_bracket(float(m)))
    best_m_float = float(best_m)
    return {"log_prob": best_m_float * log_bracket(best_m_float), "m": best_m_float, "log_bracket": log_bracket(best_m_float)}

def tail_condition(
    log_p: float,
    beta: float,
    mu0: float,
    a: float,
    delta: float,
    c_usc: float,
    kappa: float,
) -> bool:
    # 对数形式检查 7.3.5，避免巨大数溢出。
    left = math.log(mu0) + 2.0 * math.log(delta) + (beta / 2.0) * log_p
    right = c_usc * math.log(c_usc * kappa * log_p) + (c_usc + a) * math.log(log_p)
    return left >= right


def safe_exp(x: float) -> float | str:
    # Python 浮点无法表示极大阈值时，保留指数形式。
    if x > 700.0:
        return f"exp({x:.6g})"
    return math.exp(x)


def chernoff_log_probability(log_p: float, beta: float, mu0: float, a: float, delta: float, efficiency: float = 1.0) -> dict[str, float]:
    """Poisson/Chernoff 型诊断尾界；不是当前已证默认尾界。"""
    if delta <= 0.0 or efficiency <= 0.0:
        return {"log_prob": 0.0, "m": 0.0, "log_bracket": float("inf")}
    log_mu = math.log(mu0) + beta * log_p - a * math.log(log_p)
    log_coeff = math.log(efficiency) + 2.0 * math.log(delta) - math.log(3.0)
    log_exponent_abs = log_coeff + log_mu
    if log_exponent_abs > 690.0:
        exponent = -1.0e300
    else:
        exponent = -math.exp(log_exponent_abs)
    return {"log_prob": exponent, "m": -1.0, "log_bracket": exponent}


def condition_report(x: float, c: dict[str, float], d: dict[str, float]) -> dict[str, float | bool]:
    # 返回各条件在 log P = x 处的余量，正数表示通过。
    if c.get("tail_mode") in {"direct", "chernoff"}:
        if c.get("tail_mode") == "chernoff":
            efficiency = c.get("chernoff_efficiency", 1.0)
            row_prob = chernoff_log_probability(x, 0.5, c["mu_row"], c["a_row"], c["delta_row"], efficiency)
            col_prob = chernoff_log_probability(x, 1.0, c["mu_col"], c["a_col"], c["delta_col"], efficiency)
        else:
            row_prob = best_log_probability(
                x, 0.5, c["mu_row"], c["a_row"], c["delta_row"], d["C_USC"], d["c0"], c.get("low_moment_C"), c.get("low_moment_cutoff", 0.0), bool(c.get("low_moment_uncapped", False))
            )
            col_prob = best_log_probability(
                x, 1.0, c["mu_col"], c["a_col"], c["delta_col"], d["C_USC"], d["c0"], c.get("low_moment_C"), c.get("low_moment_cutoff", 0.0), bool(c.get("low_moment_uncapped", False))
            )
        row_needed = c["A_row"] * math.log(x) if c.get("row_union_mode") == "cluster" else c["d_row"] * x
        row_tail_margin_direct = -row_prob["log_prob"] - row_needed
        col_tail_margin_direct = -col_prob["log_prob"] - x
    row_left = math.log(c["mu_row"]) + 2.0 * math.log(c["delta_row"]) + 0.25 * x
    row_right = d["C_USC"] * math.log(d["C_USC"] * d["kappa_row"] * x) + (d["C_USC"] + c["a_row"]) * math.log(x)
    col_left = math.log(c["mu_col"]) + 2.0 * math.log(c["delta_col"]) + 0.5 * x
    col_right = d["C_USC"] * math.log(d["C_USC"] * d["kappa_col"] * x) + (d["C_USC"] + c["a_col"]) * math.log(x)
    if c.get("tail_mode") in {"direct", "chernoff"}:
        # direct/chernoff 模式的 row/col tail_margin 已经扣除了并合数量，避免重复整数化。
        row_int_margin = float("inf")
        col_int_margin = float("inf")
    elif c.get("row_union_mode") == "cluster":
        row_int_margin = d["c_row"] * x * x - c["A_row"] * math.log(x)
        col_int_margin = d["c_col"] * x * x - x
    else:
        row_int_margin = d["c_row"] * x * x - c["d_row"] * x
        col_int_margin = d["c_col"] * x * x - x
    loglog_p = math.log(x)
    low_c = c.get("low_moment_C", 10.0)
    # 低阶矩锋利闸门使用 x=log P，而不是 log x。
    # 二点：C_d4 x^3 <= C^C x^C；四点 connected：C_4loc μ x^3 <= (2C)^(2C) μ^2 x^(2C)。
    d4_gate_margin = (low_c ** low_c) * (x ** (low_c - 3.0)) - c.get("C_d4_gate", 0.0)
    log_row_mu_lower = math.log(c["mu_row"]) + 0.5 * x - c["a_row"] * math.log(x)
    loc4_gate_log_margin = (
        2.0 * low_c * math.log(2.0 * low_c)
        + log_row_mu_lower
        + (2.0 * low_c - 3.0) * math.log(x)
        - math.log(c.get("C_4loc_gate", 1.0))
    )
    loc4_gate_margin = loc4_gate_log_margin
    row_error_margin = (x ** (c["A_row_err"] - 1.0)) - c["C_row_err"]
    col_error_margin = (x ** (c["A_col_err"] - 1.0)) - 8.0 * c["C_col_err"]
    b1_margin = d["B1"] - (d["C_star"] + c["B_fourier"] + 10.0)
    b2_margin = d["B2"] - (d["C_star"] + 2.0 * c["B_fourier"] + 20.0)
    b4_margin = d["B4"] - (d["C_star"] + 2.0 * c["B_fourier"] + 20.0)
    b5_margin = d["B5"] - (c["B_fourier"] + c["C_st"] + 3.0)
    ks_margin = min(d["B1"], d["B2"]) - (4.0 * c["C_KS"] + 3.0 * c["C_L"] + d["C_star"] + 20.0)
    report = {
        "log_P": x,
        "row_tail_margin": row_tail_margin_direct if c.get("tail_mode") in {"direct", "chernoff"} else row_left - row_right,
        "col_tail_margin": col_tail_margin_direct if c.get("tail_mode") in {"direct", "chernoff"} else col_left - col_right,
        "row_integer_margin": row_int_margin,
        "col_integer_margin": col_int_margin,
        "d4_gate_margin": d4_gate_margin,
        "loc4_gate_margin": loc4_gate_margin,
        "row_error_margin": row_error_margin,
        "col_error_margin": col_error_margin,
        "B1_margin": b1_margin,
        "B2_margin": b2_margin,
        "B4_margin": b4_margin,
        "B5_margin": b5_margin,
        "KS_margin": ks_margin,
    }
    if c.get("tail_mode") in {"direct", "chernoff"}:
        report.update({
            "row_best_m": row_prob["m"],
            "row_log_bracket": row_prob["log_bracket"],
            "col_best_m": col_prob["m"],
            "col_log_bracket": col_prob["log_bracket"],
        })
    return report


def search_threshold(c: dict[str, float], d: dict[str, float], max_log_p: float) -> dict[str, float | str | dict[str, float | bool]]:
    # 用自适应对数网格搜索满足尾界与整数化的 exp(log P)。最终有限验证时再取素数上界。
    start = max(math.log(3.0), 2.0 / d["c0"])
    x = start
    step = max(0.01, start / 1000.0)
    last_report = condition_report(x, c, d)
    while x <= max_log_p:
        if c.get("tail_mode") in {"direct", "chernoff"}:
            report = condition_report(x, c, d)
            row_tail = report["row_tail_margin"] > 0.0
            col_tail = report["col_tail_margin"] > 0.0
        else:
            row_tail = tail_condition(x, 0.5, c["mu_row"], c["a_row"], c["delta_row"], d["C_USC"], d["kappa_row"])
            col_tail = tail_condition(x, 1.0, c["mu_col"], c["a_col"], c["delta_col"], d["C_USC"], d["kappa_col"])
        if c.get("tail_mode") in {"direct", "chernoff"}:
            row_int = True
            col_int = True
        else:
            row_int = (
                d["c_row"] * x * x - c["A_row"] * math.log(x) > 0.0
                if c.get("row_union_mode") == "cluster"
                else c["d_row"] * x - d["c_row"] * x * x < 0.0
            )
            col_int = x - d["c_col"] * x * x < 0.0
        if row_tail and col_tail and row_int and col_int:
            return {"log_P_tail": x, "P_tail_upper": safe_exp(x), "report": condition_report(x, c, d)}
        last_report = condition_report(x, c, d)
        x += step
    raise SystemExit(
        "在 log P <= {0:g} 内未找到满足条件的阈值；最后余量为：{1}".format(
            max_log_p, json.dumps(last_report, ensure_ascii=False)
        )
    )




def all_conditions_hold(x: float, c: dict[str, float], d: dict[str, float]) -> bool:
    if c.get("tail_mode") in {"direct", "chernoff"}:
        report = condition_report(x, c, d)
        tail_ok = report["row_tail_margin"] > 0.0 and report["col_tail_margin"] > 0.0
    else:
        tail_ok = (
            tail_condition(x, 0.5, c["mu_row"], c["a_row"], c["delta_row"], d["C_USC"], d["kappa_row"])
            and tail_condition(x, 1.0, c["mu_col"], c["a_col"], c["delta_col"], d["C_USC"], d["kappa_col"])
        )
    gate_report = condition_report(x, c, d)
    gates_ok = (
        gate_report["d4_gate_margin"] >= 0.0
        and gate_report["loc4_gate_margin"] >= 0.0
        and gate_report["row_error_margin"] >= 0.0
        and gate_report["col_error_margin"] >= 0.0
        and gate_report["B1_margin"] > 0.0
        and gate_report["B2_margin"] > 0.0
        and gate_report["B4_margin"] > 0.0
        and gate_report["B5_margin"] > 0.0
        and gate_report["KS_margin"] > 0.0
    )
    if c.get("tail_mode") in {"direct", "chernoff"}:
        return tail_ok and gates_ok
    return (
        tail_ok
        and (
            (d["c_row"] * x * x - c["A_row"] * math.log(x) > 0.0)
            if c.get("row_union_mode") == "cluster"
            else (c["d_row"] * x - d["c_row"] * x * x < 0.0)
        )
        and x - d["c_col"] * x * x < 0.0
        and gates_ok
    )


def bisect_threshold(c: dict[str, float], d: dict[str, float], max_log_p: float) -> dict[str, float | str | dict[str, float | bool]]:
    # 二分搜索比线性网格更适合天文阈值诊断。
    low = math.log(3.0) if c.get("low_moment_uncapped", False) else max(math.log(3.0), 2.0 / d["c0"])
    high = max(low * 2.0, 10.0)
    while high <= max_log_p and not all_conditions_hold(high, c, d):
        low = high
        high *= 2.0
    if high > max_log_p:
        if all_conditions_hold(max_log_p, c, d):
            high = max_log_p
        else:
            raise SystemExit(
                "在 log P <= {0:g} 内未找到满足条件的阈值；最后余量为：{1}".format(
                    max_log_p, json.dumps(condition_report(max_log_p, c, d), ensure_ascii=False)
                )
            )
    for _ in range(100):
        mid = (low + high) / 2.0
        if all_conditions_hold(mid, c, d):
            high = mid
        else:
            low = mid
    return {"log_P_tail": high, "P_tail_upper": safe_exp(high), "report": condition_report(high, c, d)}


def target_cusc_scan(c: dict[str, float], target_log_p: float) -> dict[str, float | str]:
    # 反推：若保持 7.3 形式，要让给定 log P 通过，大约需要 C_USC 不超过多少。
    # 这里临时用 C_USC 作为变量，并沿用 kappa = min(c0/4, 1/(16C)) / 1/(8C) 的规则。
    def report_for(c_usc: float) -> dict[str, float | bool]:
        d = derived_constants(c)
        d["C_USC"] = c_usc
        if c.get("tail_mode") == "optimized":
            d["kappa_row"] = min(d["c0"] / 3.0, 1.0 / (8.0 * c_usc))
            d["kappa_col"] = min(d["c0"] / 3.0, 1.0 / (4.0 * c_usc))
            d["c_row"] = d["kappa_row"] / 6.0
            d["c_col"] = d["kappa_col"] / 3.0
        else:
            d["kappa_row"] = min(d["c0"] / 4.0, 1.0 / (16.0 * c_usc))
            d["kappa_col"] = min(d["c0"] / 4.0, 1.0 / (8.0 * c_usc))
            d["c_row"] = d["kappa_row"] / 8.0
            d["c_col"] = d["kappa_col"] / 4.0
        r = condition_report(target_log_p, c, d)
        r["works"] = all_conditions_hold(target_log_p, c, d)
        return r

    def works(c_usc: float) -> bool:
        return bool(report_for(c_usc)["works"])

    if not works(1.0):
        return {
            "target_log_P": target_log_p,
            "max_C_USC": 0.0,
            "status": "即使 C_USC=1 也不能通过当前尾界/整数化条件",
            "report_at_C_USC_1": report_for(1.0),
            "current_C_USC": derived_constants(c)["C_USC"],
        }

    low, high = 1.0, 2.0
    while works(high):
        low = high
        high *= 2.0
        if high > 1e18:
            return {"target_log_P": target_log_p, "max_C_USC_at_least": high, "current_C_USC": derived_constants(c)["C_USC"]}
    for _ in range(100):
        mid = (low + high) / 2.0
        if works(mid):
            low = mid
        else:
            high = mid
    return {"target_log_P": target_log_p, "max_C_USC": low, "current_C_USC": derived_constants(c)["C_USC"]}



def d4_threshold(c_d4: float, max_log_p: float = 1000.0) -> dict[str, float | str]:
    """求解 D4-low 充分条件 sqrt(P) >= C_d4 * log(P)^2。"""
    if c_d4 <= 0.0:
        raise SystemExit("C_d4 必须为正。")

    def margin(x: float) -> float:
        return 0.5 * x - math.log(c_d4) - 2.0 * math.log(x)

    low = math.log(3.0)
    high = max(10.0, low * 2.0)
    while high <= max_log_p and margin(high) < 0.0:
        low = high
        high *= 2.0
    if high > max_log_p and margin(max_log_p) < 0.0:
        raise SystemExit(f"在 log P <= {max_log_p:g} 内 D4-low 条件仍未通过。")
    high = min(high, max_log_p)
    for _ in range(100):
        mid = (low + high) / 2.0
        if margin(mid) >= 0.0:
            high = mid
        else:
            low = mid
    return {
        "C_d4_sharp": c_d4,
        "condition": "sqrt(P) >= C_d4_sharp * log(P)^2",
        "log_P_D4": high,
        "P_D4_upper": safe_exp(high),
        "margin_at_threshold": margin(high),
    }


def loc4_threshold(
    c_4loc: float,
    low_c: float = 4.0,
    mu_row: float = 1.0,
    a_row: float = 1.0,
    max_log_p: float = 1000.0,
) -> dict[str, float | str]:
    """求解 LOC4-sharp 主量吸收闸门。"""
    if c_4loc <= 0.0 or low_c <= 0.0 or mu_row <= 0.0:
        raise SystemExit("C_4loc、low_moment_C 与 mu_row 必须为正。")

    def log_margin(x: float) -> float:
        return (
            2.0 * low_c * math.log(2.0 * low_c)
            + math.log(mu_row)
            + 0.5 * x
            + (2.0 * low_c - a_row - 3.0) * math.log(x)
            - math.log(c_4loc)
        )

    low = math.log(3.0)
    high = max(2.0, low * 2.0)
    while high <= max_log_p and log_margin(high) < 0.0:
        low = high
        high *= 2.0
    if high > max_log_p and log_margin(max_log_p) < 0.0:
        raise SystemExit(f"在 log P <= {max_log_p:g} 内 LOC4-sharp 条件仍未通过。")
    high = min(high, max_log_p)
    for _ in range(100):
        mid = (low + high) / 2.0
        if log_margin(mid) >= 0.0:
            high = mid
        else:
            low = mid
    return {
        "C_4loc_sharp": c_4loc,
        "low_moment_C": low_c,
        "condition": "C_4loc*log(P)^3 <= (2C)^(2C)*mu*log(P)^(2C)",
        "log_P_LOC4": high,
        "P_LOC4_upper": safe_exp(high),
        "log_margin_at_threshold": log_margin(high),
    }


def loc4_capacity(
    log_p: float,
    low_c: float = 4.0,
    mu_row: float = 1.0,
    a_row: float = 1.0,
) -> dict[str, float]:
    """给定 logP，计算 LOC4-sharp 可承受的最大 C_4loc。"""
    if log_p <= 0.0 or low_c <= 0.0 or mu_row <= 0.0:
        raise SystemExit("logP、low_moment_C 与 mu_row 必须为正。")
    capacity = math.exp(
        2.0 * low_c * math.log(2.0 * low_c)
        + math.log(mu_row)
        + 0.5 * log_p
        + (2.0 * low_c - a_row - 3.0) * math.log(log_p)
    )
    return {
        "log_P": log_p,
        "low_moment_C": low_c,
        "C_4loc_max_allowed": capacity,
    }


def target_prime5_audit(c: dict[str, float], d: dict[str, float]) -> dict[str, object]:
    """审查把最终有限验证阈值压到 P<=5 时的各闸门余量。"""
    # 若只有限验证 P<=5，理论部分必须从下一个奇素数 P=7 起接管。
    p_start = 7.0
    x = math.log(p_start)
    report = condition_report(x, c, d)
    d4_capacity = d4poly_k_capacity(d4poly_stieltjes_coeffs(), x)
    loc4_cap = loc4_capacity(x, c["low_moment_C"], c["mu_row"], c["a_row"])
    return {
        "finite_verification_up_to_P": 5,
        "theory_must_start_at_P": int(p_start),
        "log_P_start": x,
        "chernoff_gate_margins_at_P7": {
            key: report[key]
            for key in [
                "row_tail_margin",
                "col_tail_margin",
                "d4_gate_margin",
                "loc4_gate_margin",
                "row_error_margin",
                "col_error_margin",
                "B1_margin",
                "B2_margin",
                "B4_margin",
                "B5_margin",
                "KS_margin",
            ]
        },
        "D4poly_capacity_at_P7": d4_capacity,
        "LOC4_capacity_at_P7": loc4_cap,
        "blocking_observation": "若要求单一 K=5 余项从 P=7 直接统一生效，则 P=7 容量不足；但可用 7<=P<=149 的 D4 有限桥接证书补上，理论尾部仍从 P>=149 接管。",
    }


def d4poly_unit_threshold(
    p3_coeffs: list[float],
    k_d4: float,
    x_d4: float,
    max_log_p: float = 1000.0,
) -> dict[str, object]:
    """求解 P_3(log P)/log^3(P)+K_d4 P^{-1/4}/log^3(P) <= 1。

    p3_coeffs 按升幂给出：a0+a1*t+a2*t^2+a3*t^3。
    """
    if len(p3_coeffs) != 4:
        raise SystemExit("--d4poly-coeffs 需要 4 个逗号分隔系数：a0,a1,a2,a3。")
    if k_d4 < 0.0 or x_d4 < 1.0:
        raise SystemExit("K_d4 必须非负，X_d4 必须 >= 1。")

    def p3(t: float) -> float:
        return sum(coef * (t ** i) for i, coef in enumerate(p3_coeffs))

    def lhs(x: float) -> float:
        return p3(x) / (x ** 3) + k_d4 * math.exp(-0.25 * x) / (x ** 3)

    low = max(math.log(3.0), math.log(x_d4))
    if lhs(low) <= 1.0:
        high = low
    else:
        high = max(10.0, low * 2.0)
        while high <= max_log_p and lhs(high) > 1.0:
            low = high
            high *= 2.0
        if high > max_log_p and lhs(max_log_p) > 1.0:
            raise SystemExit(f"在 log P <= {max_log_p:g} 内 d4poly 单位化条件未通过。")
        high = min(high, max_log_p)
        for _ in range(100):
            mid = (low + high) / 2.0
            if lhs(mid) <= 1.0:
                high = mid
            else:
                low = mid
    return {
        "condition": "P3(log P)/log(P)^3 + K_d4 * P^(-1/4)/log(P)^3 <= 1",
        "P3_coeffs_low_to_high": p3_coeffs,
        "K_d4": k_d4,
        "X_d4": x_d4,
        "log_P_d4poly_unit": high,
        "P_d4poly_unit_upper": safe_exp(high),
        "lhs_at_threshold": lhs(high),
    }





def pb3_gate_report(log_x: float, c4m: float, steps: int = 20000) -> dict[str, float | str]:
    """用 PB3good+PB3red 数值积分检查横边预算。"""
    if log_x <= 0.0 or c4m <= 0.0:
        raise SystemExit("log X 与 C_4M 必须为正。")
    x = math.exp(log_x)
    t0 = math.exp(0.25 * log_x)
    c = 1.0 + 1.0 / log_x
    m_half = 2.0 * c4m * (math.log(2.0 * math.e * t0) ** 4)
    m_c = (c / (c - 1.0)) ** 4
    width = c - 0.5
    total = 0.0
    for i in range(steps + 1):
        sigma = 0.5 + width * i / steps
        theta = (sigma - 0.5) / width
        interp = (m_half ** (1.0 - theta)) * (m_c ** theta)
        value = (x ** sigma) * interp
        total += (0.5 if i in {0, steps} else 1.0) * value
    integral = total * width / steps
    lhs = integral / (math.pi * t0)
    rhs = 1500.0 * (x ** 0.75)
    return {
        "condition": "PB3good+PB3red horizontal budget",
        "log_X": log_x,
        "X_upper": safe_exp(log_x),
        "C_4M": c4m,
        "T0": t0,
        "M_half": m_half,
        "M_c": m_c,
        "PB3_lhs": lhs,
        "PB3_rhs": rhs,
        "PB3_margin": rhs - lhs,
        "PB3_ratio": lhs / rhs,
    }


def pb2_c4m_capacity(log_x: float) -> dict[str, float | str]:
    """计算 PB2gate 在给定 X=e^log_x 处允许的最大四次矩常数 C_4M。"""
    if log_x <= 0.0:
        raise SystemExit("log X 必须为正。")
    log_t = 0.25 * log_x
    denominator = (1.0 + log_t) * (1.0 + log_t) ** 4
    c4m_max = 1500.0 * math.exp(0.25 * log_x) * math.pi / denominator
    return {
        "condition": "(C_4M/pi)*(1+log T)*log(eT)^4 <= 1500*X^(1/4), T=X^(1/4)",
        "log_X": log_x,
        "X_upper": safe_exp(log_x),
        "T": math.exp(log_t),
        "C_4M_max_allowed": c4m_max,
    }


def d4poly_k_capacity(p3_coeffs: list[float], log_p: float) -> dict[str, object]:
    """计算给定 log P 下 d4poly 单位化可承受的最大 K_d4。"""
    if len(p3_coeffs) != 4:
        raise SystemExit("--d4poly-coeffs 需要 4 个逗号分隔系数：a0,a1,a2,a3。")
    if log_p <= 0.0:
        raise SystemExit("log P 必须为正。")

    p3 = sum(coef * (log_p ** i) for i, coef in enumerate(p3_coeffs))
    main_ratio = p3 / (log_p ** 3)
    k_max = max(0.0, (1.0 - main_ratio) * math.exp(0.25 * log_p) * (log_p ** 3))
    return {
        "log_P": log_p,
        "P_upper": safe_exp(log_p),
        "P3_coeffs_low_to_high": p3_coeffs,
        "main_ratio": main_ratio,
        "remaining_unit_margin": 1.0 - main_ratio,
        "K_d4_max_allowed": k_max,
    }


def final_ledger(c: dict[str, float], d: dict[str, float], max_log_p: float) -> dict[str, object]:
    """汇总当前已脚本化的最终阈值账本。"""
    threshold = bisect_threshold(c, d, max_log_p)
    report = threshold["report"]
    d4_low = d4_threshold(c["C_d4_gate"], max_log_p)
    d4poly_5 = d4poly_unit_threshold(d4poly_stieltjes_coeffs(), 5.0, 149.0, max_log_p)
    d4_active = d4poly_5 if c.get("C_d4_gate") <= 1.0 else d4_low
    d4_active_log = float(d4_active.get("log_P_d4poly_unit", d4_active.get("log_P_D4", 0.0)))
    combined_log_p = max(float(threshold["log_P_tail"]), d4_active_log)
    included = {
        "tail_and_integerization": threshold,
        "optimization_parameters": {
            "tail_mode": c["tail_mode"],
            "chernoff_efficiency": c.get("chernoff_efficiency", None),
            "A_row": c["A_row"],
            "delta_row": c["delta_row"],
            "delta_col": c["delta_col"],
            "mu_col": c["mu_col"],
        },
        "tiny_chebyshev": {
            "C_Cheb": c["C_Cheb"],
            "A1": c["A1"],
            "c0_safety": c["c0_safety"],
            "c0": d["c0"],
        },
        "low_moment_gates": {
            "low_moment_C": c["low_moment_C"],
            "low_moment_uncapped": bool(c.get("low_moment_uncapped", False)),
            "C_d4_gate": c["C_d4_gate"],
            "C_4loc_gate": c["C_4loc_gate"],
            "d4_gate_margin": report["d4_gate_margin"],
            "loc4_gate_margin": report["loc4_gate_margin"],
            "D4_low_threshold": d4_low,
            "D4_poly_K5_threshold": d4poly_5,
            "D4_active_route": "d4poly_K5" if d4_active is d4poly_5 else "sqrtP_log2",
        },
        "row_col_error_gates": {
            "C_row_err": c["C_row_err"],
            "A_row_err": c["A_row_err"],
            "C_col_err": c["C_col_err"],
            "A_col_err": c["A_col_err"],
            "row_error_margin": report["row_error_margin"],
            "col_error_margin": report["col_error_margin"],
        },
        "b04star_parameter_gates": {
            "C_star": d["C_star"],
            "B1": d["B1"],
            "B2": d["B2"],
            "B4": d["B4"],
            "B5": d["B5"],
            "C_L": c["C_L"],
            "C_KS": c["C_KS"],
            "C_poly": c.get("C_poly", 0.0),
            "B1_margin": report["B1_margin"],
            "B2_margin": report["B2_margin"],
            "B4_margin": report["B4_margin"],
            "B5_margin": report["B5_margin"],
            "KS_margin": report["KS_margin"],
        },
    }
    not_included = [
        "Mertens 乘积显式阈值 P_M 的具体引用/数值",
        "行安全间隙中全部 o(1) 项的独立数值阈值 P_G",
        "列容量余量中全部 o(1) 项的独立数值阈值 P_cap",
        "B.0.4* 覆盖矩阵的最终人工审稿确认",
        "D4poly-K5 余项界 sum d4(n) <= X*P3(log X)+5*X^(3/4) 对 X>=149 的严格证明或引用",
        "7 <= P <= 149 的 D4poly 有限桥接证书需归档；P <= 5 的目标命题有限验证已经可直接执行",
        "历史追加段落中的旧状态清理与定稿一致性复核",
    ]
    return {
        "log_P_scripted": combined_log_p,
        "P_scripted_upper": safe_exp(combined_log_p),
        "log_P_tail_only": threshold["log_P_tail"],
        "included_gates": included,
        "not_yet_included_in_script": not_included,
        "status": "这是已脚本化闸门的合并阈值，不是最终全部奇素数有限验证阈值。",
    }

def main() -> None:
    parser = argparse.ArgumentParser(description="显式阈值 P_* 账本计算器")
    parser.add_argument("--show-template", action="store_true", help="输出常数 JSON 模板")
    parser.add_argument("--constants", type=Path, help="原子常数 JSON 文件")
    parser.add_argument("--max-log-p", type=float, default=1000.0, help="搜索的最大 log P")
    parser.add_argument("--bisect", action="store_true", help="使用二分/倍增搜索阈值")
    parser.add_argument("--target-log-p", type=float, help="反推目标 log P 所允许的最大 C_USC")
    parser.add_argument("--scan-tiny", action="store_true", help="扫描若干 C_Cheb,A1 组合的阈值")
    parser.add_argument("--cheb-target-safe", action="store_true", help="使用 Dusart 支撑的 C_Cheb=1+1/36260,A1=8 tiny 目标参数")
    parser.add_argument("--final-ledger", action="store_true", help="输出当前已脚本化最终闸门账本")
    parser.add_argument("--optimization-profile", choices=["conservative", "row2", "sub70", "chernoff52", "chernoff39", "chernoff36", "chernoff17", "chernoff13", "chernoff12", "chernoff5", "chernoff1"], help="应用阈值优化预设：保守、二维行簇、冲击70、Chernoff 诊断档")
    parser.add_argument("--tiny-a1", type=float, help="覆盖 tiny 分界 A1，用于阈值诊断")
    parser.add_argument("--tiny-safety", type=float, help="覆盖 c0_safety/S0，用于阈值诊断")
    parser.add_argument("--low-moment-uncapped", action="store_true", help="诊断模式：允许 m<=low_moment_cutoff 的低阶矩绕过通用 c0 logP 矩阶上界")
    parser.add_argument("--low-moment-c", type=float, help="覆盖低阶矩常数 C_low，用于阈值诊断")
    parser.add_argument("--row-cluster-a", type=float, help="覆盖行簇并合复杂度 A_row，用于阈值诊断")
    parser.add_argument("--delta-row", type=float, help="覆盖行尾界相对缺口 delta_row，用于阈值诊断")
    parser.add_argument("--delta-col", type=float, help="覆盖列尾界相对缺口 delta_col，用于阈值诊断")
    parser.add_argument("--mu-col", type=float, help="覆盖列主量常数 mu_col，用于阈值诊断")
    parser.add_argument("--d4-gate", type=float, help="覆盖二点 d4 平均常数闸门，用于阈值诊断")
    parser.add_argument("--loc4-gate", type=float, help="覆盖四点局部常数闸门，用于阈值诊断")
    parser.add_argument("--row-error-c", type=float, help="覆盖行误差常数 C_row_err，用于阈值诊断")
    parser.add_argument("--row-error-a", type=float, help="覆盖行误差幂 A_row_err，用于阈值诊断")
    parser.add_argument("--col-error-c", type=float, help="覆盖列误差常数 C_col_err，用于阈值诊断")
    parser.add_argument("--col-error-a", type=float, help="覆盖列误差幂 A_col_err，用于阈值诊断")
    parser.add_argument("--ks-c", type=float, help="覆盖 Kloosterman 四点常数 C_KS，用于阈值诊断")
    parser.add_argument("--ks-layer-c", type=float, help="覆盖 Kloosterman 层数常数 C_L，用于阈值诊断")
    parser.add_argument("--poly-c", type=float, help="覆盖 FS8-polymer 常数 C_poly，用于阈值诊断")
    parser.add_argument("--scan-poly", action="store_true", help="扫描 C_poly 对 C_star、KS_margin 与阈值的影响")
    parser.add_argument("--scan-ks", action="store_true", help="扫描 C_KS/C_L 对 KS_margin 与阈值的影响")
    parser.add_argument("--scan-row-col", action="store_true", help="扫描 A_row、delta_col、mu_col 对阈值地板的影响")
    parser.add_argument("--scan-frontier", action="store_true", help="扫描 A_row 与 delta_col 的二维阈值前沿")
    parser.add_argument("--scan-error-gates", action="store_true", help="扫描行列误差闸门对 Chernoff 诊断地板的影响")
    parser.add_argument("--solve-frontier", type=float, help="给定目标 logP，求每个 A_row 所需的最小 delta_col")
    parser.add_argument("--tail-mode", choices=["standard", "optimized", "direct", "chernoff"], help="覆盖尾界模式；chernoff 仅为诊断模型")
    parser.add_argument("--chernoff-efficiency", type=float, help="Chernoff 诊断尾界效率系数")
    parser.add_argument("--solve-d4-threshold", action="store_true", help="求解 D4-low 条件 sqrt(P) >= C_d4 log(P)^2")
    parser.add_argument("--solve-loc4-threshold", action="store_true", help="求解 LOC4-sharp 主量吸收闸门")
    parser.add_argument("--loc4-capacity", type=float, help="给定 logP，计算 LOC4-sharp 可承受的最大 C_4loc")
    parser.add_argument("--solve-d4poly-unit", action="store_true", help="求解 d4 多项式单位化条件")
    parser.add_argument("--d4poly-coeffs", type=str, default="0,0,0,0.16666666666666666", help="P3 系数 a0,a1,a2,a3，按升幂逗号分隔")
    parser.add_argument("--d4poly-k", type=float, default=0.0, help="d4poly 余项常数 K_d4")
    parser.add_argument("--d4poly-x0", type=float, default=3.0, help="d4poly 适用起点 X_d4")
    parser.add_argument("--d4poly-stieltjes-preset", action="store_true", help="使用 zeta(s)^4 留数主项的 Stieltjes 系数预设")
    parser.add_argument("--d4poly-k-capacity", type=float, help="给定 logP，计算 d4poly 单位化可承受的最大 K_d4")
    parser.add_argument("--pb2-c4m-capacity", type=float, help="给定 logX，计算 PB2gate 可承受的最大 C_4M")
    parser.add_argument("--pb3-gate", type=float, help="给定 logX，检查 PB3good+PB3red 横边预算")
    parser.add_argument("--c4m", type=float, default=130.0, help="PB2/PB3 使用的四次矩常数 C_4M")
    parser.add_argument("--target-prime5-audit", action="store_true", help="审查最终阈值压到 P<=5 时的必要闸门余量")
    args = parser.parse_args()

    if args.show_template:
        print(json.dumps(TEMPLATE, ensure_ascii=False, indent=2))
        return
    if args.constants is None:
        constants = dict(TEMPLATE)
    else:
        constants = load_constants(args.constants)
    derived = derived_constants(constants)
    if args.cheb_target_safe:
        constants["C_Cheb"] = 1.0 + 1.0 / 36260.0
        constants["A1"] = 8.0
    if args.optimization_profile is not None:
        apply_optimization_profile(constants, args.optimization_profile)
    if args.tail_mode is not None:
        constants["tail_mode"] = args.tail_mode
    if args.chernoff_efficiency is not None:
        constants["chernoff_efficiency"] = args.chernoff_efficiency
    if args.tiny_a1 is not None:
        constants["A1"] = args.tiny_a1
    if args.tiny_safety is not None:
        constants["c0_safety"] = args.tiny_safety
    if args.low_moment_uncapped:
        constants["low_moment_uncapped"] = True
    if args.low_moment_c is not None:
        constants["low_moment_C"] = args.low_moment_c
    if args.row_cluster_a is not None:
        constants["A_row"] = args.row_cluster_a
    if args.delta_row is not None:
        constants["delta_row"] = args.delta_row
    if args.delta_col is not None:
        constants["delta_col"] = args.delta_col
    if args.mu_col is not None:
        constants["mu_col"] = args.mu_col
    if args.d4_gate is not None:
        constants["C_d4_gate"] = args.d4_gate
    if args.loc4_gate is not None:
        constants["C_4loc_gate"] = args.loc4_gate
    if args.row_error_c is not None:
        constants["C_row_err"] = args.row_error_c
    if args.row_error_a is not None:
        constants["A_row_err"] = args.row_error_a
    if args.col_error_c is not None:
        constants["C_col_err"] = args.col_error_c
    if args.col_error_a is not None:
        constants["A_col_err"] = args.col_error_a
    if args.ks_c is not None:
        constants["C_KS"] = args.ks_c
    if args.ks_layer_c is not None:
        constants["C_L"] = args.ks_layer_c
    if args.poly_c is not None:
        constants["C_poly"] = args.poly_c
    derived = derived_constants(constants)
    if args.solve_d4_threshold:
        print(json.dumps(d4_threshold(constants["C_d4_gate"], args.max_log_p), ensure_ascii=False, indent=2))
        return
    if args.target_prime5_audit:
        print(json.dumps(target_prime5_audit(constants, derived), ensure_ascii=False, indent=2))
        return
    if args.solve_loc4_threshold:
        print(json.dumps(loc4_threshold(constants["C_4loc_gate"], constants["low_moment_C"], constants["mu_row"], constants["a_row"], args.max_log_p), ensure_ascii=False, indent=2))
        return
    if args.loc4_capacity is not None:
        print(json.dumps(loc4_capacity(args.loc4_capacity, constants["low_moment_C"], constants["mu_row"], constants["a_row"]), ensure_ascii=False, indent=2))
        return
    if args.pb3_gate is not None:
        print(json.dumps(pb3_gate_report(args.pb3_gate, args.c4m), ensure_ascii=False, indent=2))
        return
    if args.pb2_c4m_capacity is not None:
        print(json.dumps(pb2_c4m_capacity(args.pb2_c4m_capacity), ensure_ascii=False, indent=2))
        return
    if args.d4poly_k_capacity is not None:
        coeffs = d4poly_stieltjes_coeffs() if args.d4poly_stieltjes_preset else [float(part) for part in args.d4poly_coeffs.split(",")]
        print(json.dumps(d4poly_k_capacity(coeffs, args.d4poly_k_capacity), ensure_ascii=False, indent=2))
        return
    if args.solve_d4poly_unit:
        coeffs = d4poly_stieltjes_coeffs() if args.d4poly_stieltjes_preset else [float(part) for part in args.d4poly_coeffs.split(",")]
        print(json.dumps(d4poly_unit_threshold(coeffs, args.d4poly_k, args.d4poly_x0, args.max_log_p), ensure_ascii=False, indent=2))
        return
    if args.final_ledger:
        print(json.dumps(final_ledger(constants, derived, args.max_log_p), ensure_ascii=False, indent=2))
        return
    if args.target_log_p is not None:
        print(json.dumps({"derived": derived, "target": target_cusc_scan(constants, args.target_log_p)}, ensure_ascii=False, indent=2))
        return
    if args.scan_poly:
        rows = []
        for c_poly in [0, 20, 40, 80, 120, 160, 180, 200, 240, 320]:
            test = dict(constants)
            test["C_poly"] = float(c_poly)
            dtest = derived_constants(test)
            try:
                th = bisect_threshold(test, dtest, args.max_log_p)
                rows.append({
                    "C_poly": c_poly,
                    "C_star": dtest["C_star"],
                    "B1": dtest["B1"],
                    "B2": dtest["B2"],
                    "log_P": th["log_P_tail"],
                    "KS_margin": th["report"]["KS_margin"],
                })
            except SystemExit as exc:
                rows.append({"C_poly": c_poly, "C_star": dtest["C_star"], "error": str(exc)})
        print(json.dumps({"scan_poly": rows}, ensure_ascii=False, indent=2))
        return
    if args.scan_row_col:
        rows = []
        scenarios = []
        for a_row in [4.0, 3.0, 2.0, 1.5, 1.28, 1.0]:
            scenarios.append((a_row, constants["delta_col"], constants["mu_col"], "row-only"))
        for a_row in [2.0, 1.5, 1.28, 1.0]:
            scenarios.append((a_row, 0.2, constants["mu_col"], "delta-col-0.2"))
        for a_row in [2.0, 1.5, 1.28, 1.0]:
            scenarios.append((a_row, constants["delta_col"], 0.25, "mu-col-0.25"))
        for a_row, delta_col, mu_col, label in scenarios:
            test = dict(constants)
            test["A_row"] = float(a_row)
            test["delta_col"] = float(delta_col)
            test["mu_col"] = float(mu_col)
            dtest = derived_constants(test)
            try:
                th = bisect_threshold(test, dtest, args.max_log_p)
                report = th["report"]
                rows.append({
                    "label": label,
                    "A_row": a_row,
                    "delta_col": delta_col,
                    "mu_col": mu_col,
                    "log_P": th["log_P_tail"],
                    "row_tail_margin": report["row_tail_margin"],
                    "col_tail_margin": report["col_tail_margin"],
                    "row_best_m": report["row_best_m"],
                    "col_best_m": report["col_best_m"],
                })
            except SystemExit as exc:
                rows.append({"label": label, "A_row": a_row, "delta_col": delta_col, "mu_col": mu_col, "error": str(exc)})
        print(json.dumps({"scan_row_col": rows}, ensure_ascii=False, indent=2))
        return

    if args.scan_frontier:
        rows = []
        a_values = [2.0, 1.75, 1.5, 1.35, 1.28, 1.2, 1.0, 0.75]
        delta_values = [0.1, 0.15, 0.2, 0.25, 0.3]
        for a_row in a_values:
            best = None
            for delta_col in delta_values:
                test = dict(constants)
                test["A_row"] = float(a_row)
                test["delta_col"] = float(delta_col)
                dtest = derived_constants(test)
                try:
                    th = bisect_threshold(test, dtest, args.max_log_p)
                    item = {
                        "A_row": a_row,
                        "delta_col": delta_col,
                        "log_P": th["log_P_tail"],
                        "row_margin": th["report"]["row_tail_margin"],
                        "col_margin": th["report"]["col_tail_margin"],
                        "row_m": th["report"]["row_best_m"],
                        "col_m": th["report"]["col_best_m"],
                    }
                except SystemExit as exc:
                    item = {"A_row": a_row, "delta_col": delta_col, "error": str(exc)}
                rows.append(item)
                if "log_P" in item and (best is None or item["log_P"] < best["log_P"]):
                    best = item
            if best is not None:
                rows.append({"A_row": a_row, "best_delta_col": best["delta_col"], "best_log_P": best["log_P"], "summary": True})
        below_70 = [r for r in rows if not r.get("summary") and r.get("log_P", 1e9) < 70.0]
        print(json.dumps({"scan_frontier": rows, "below_70_count": len(below_70)}, ensure_ascii=False, indent=2))
        return

    if args.solve_frontier is not None:
        rows = []
        target = float(args.solve_frontier)
        for a_row in [2.0, 1.75, 1.5, 1.35, 1.3, 1.28, 1.25, 1.2, 1.0]:
            lo, hi = 0.01, 0.9
            best = None
            for _ in range(50):
                mid = (lo + hi) / 2.0
                test = dict(constants)
                test["A_row"] = float(a_row)
                test["delta_col"] = mid
                dtest = derived_constants(test)
                try:
                    th = bisect_threshold(test, dtest, args.max_log_p)
                    ok = th["log_P_tail"] <= target
                    if ok:
                        best = (mid, th)
                        hi = mid
                    else:
                        lo = mid
                except SystemExit:
                    lo = mid
            if best is None:
                rows.append({"A_row": a_row, "target_log_P": target, "status": "no delta_col <= 0.9 found"})
            else:
                delta_col, th = best
                rows.append({
                    "A_row": a_row,
                    "target_log_P": target,
                    "required_delta_col": delta_col,
                    "log_P": th["log_P_tail"],
                    "row_margin": th["report"]["row_tail_margin"],
                    "col_margin": th["report"]["col_tail_margin"],
                })
        print(json.dumps({"solve_frontier": rows}, ensure_ascii=False, indent=2))
        return

    if args.scan_error_gates:
        rows = []
        for c_col in [1e12, 3e11, 1e11, 3e10, 1e10, 1e9]:
            for a_col in [8.0, 8.5, 9.0, 10.0]:
                test = dict(constants)
                test["tail_mode"] = "chernoff"
                test["C_col_err"] = float(c_col)
                test["A_col_err"] = float(a_col)
                dtest = derived_constants(test)
                try:
                    th = bisect_threshold(test, dtest, args.max_log_p)
                    rows.append({
                        "C_col_err": c_col,
                        "A_col_err": a_col,
                        "log_P": th["log_P_tail"],
                        "row_error_margin": th["report"]["row_error_margin"],
                        "col_error_margin": th["report"]["col_error_margin"],
                    })
                except SystemExit as exc:
                    rows.append({"C_col_err": c_col, "A_col_err": a_col, "error": str(exc)})
        print(json.dumps({"scan_error_gates": rows}, ensure_ascii=False, indent=2))
        return

    if args.scan_ks:
        rows = []
        for c_l, c_ks in [
            (80,80),(90,90),(95,95),(99,99),(100,100),
            (100,80),(120,80),(160,80),(200,80),
            (80,100),(80,120),(80,160),(80,200),
            (120,120),(160,160),(200,200),
        ]:
            test = dict(constants)
            test["C_L"] = float(c_l)
            test["C_KS"] = float(c_ks)
            dtest = derived_constants(test)
            try:
                th = bisect_threshold(test, dtest, args.max_log_p)
                rows.append({
                    "C_L": c_l,
                    "C_KS": c_ks,
                    "C_star": dtest["C_star"],
                    "B1": dtest["B1"],
                    "B2": dtest["B2"],
                    "log_P": th["log_P_tail"],
                    "KS_margin": th["report"]["KS_margin"],
                })
            except SystemExit as exc:
                rows.append({"C_L": c_l, "C_KS": c_ks, "error": str(exc)})
        print(json.dumps({"scan_ks": rows}, ensure_ascii=False, indent=2))
        return
    if args.scan_tiny:
        rows = []
        for c_cheb, a1 in [(2,50),(1.5,40),(1.2,30),(1.1,20),(1.04,16),(1 + 1/36260,16),(1,16),(1,12)]:
            test = dict(constants)
            test["C_Cheb"] = c_cheb
            test["A1"] = a1
            dtest = derived_constants(test)
            try:
                th = bisect_threshold(test, dtest, args.max_log_p)
                rows.append({"C_Cheb": c_cheb, "A1": a1, "c0": dtest["c0"], "log_P": th["log_P_tail"], "report": th["report"]})
            except SystemExit as exc:
                rows.append({"C_Cheb": c_cheb, "A1": a1, "error": str(exc)})
        print(json.dumps({"scan_tiny": rows}, ensure_ascii=False, indent=2))
        return
    threshold = bisect_threshold(constants, derived, args.max_log_p) if args.bisect else search_threshold(constants, derived, args.max_log_p)
    print(json.dumps({"derived": derived, "threshold": threshold}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
