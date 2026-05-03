#!/usr/bin/env python3
"""QLOW-MID-COMP：固定紧区间网格证书脚手架。

用法示例：
  python3 experiments/qlow_mid_comp_grid_certificate.py
  python3 experiments/qlow_mid_comp_grid_certificate.py --step 0.01 --target 0.35
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

from sqf_qlow_mid_weighted_absorption_scan import (
    H_value,
    Q_value,
    compose_omega,
    optimal_q0_weights,
    parse_floats,
    parse_ints,
    phi_hat,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "monograph"


def log_factorial(n: int) -> float:
    """返回 log(n!)。"""
    return sum(math.log(i) for i in range(1, n + 1))


def omega_variation(omega: dict[int, float]) -> float:
    """返回 Selberg 合成权的绝对变差 sum |omega_l|/l。"""
    return sum(abs(weight) / ell for ell, weight in omega.items())


def omega_log_moment(omega: dict[int, float]) -> float:
    """返回导数账本 sum |omega_l| log(l)/l。"""
    return sum(abs(weight) * math.log(ell) / ell for ell, weight in omega.items() if ell > 1)


def analyze_case(
    P: int,
    R_exp: float,
    K: int,
    L_power: float,
    u_min: float,
    u_max: float,
    step: float,
    target: float,
    y_count: int,
    quad_n: int,
) -> dict:
    """在固定紧区间上计算带权比值与 Lipschitz 余量。"""
    R, weights = optimal_q0_weights(P, R_exp)
    omega = compose_omega(weights)
    logR = math.log(R)
    L = max(2.0, math.log(P) ** L_power)
    variation = omega_variation(omega)
    q_log_moment = omega_log_moment(omega)

    # 对 rho(u)=|H|/K * |Q|/V 使用保守 Lipschitz 账本。
    h_lipschitz = log_factorial(K) / (K * logR)
    q_lipschitz = q_log_moment / (variation * logR) if variation else 0.0
    rho_lipschitz = h_lipschitz + q_lipschitz

    n_cells = math.ceil((u_max - u_min) / step)
    max_width = 0.0
    phi_mass = 0.0
    weighted_rho_mass = 0.0
    max_rho = 0.0
    max_q_ratio = 0.0
    max_h_ratio = 0.0
    worst_midpoint = u_min
    top_cells = []

    for cell in range(n_cells):
        left = u_min + cell * step
        right = min(u_max, left + step)
        width = right - left
        midpoint = 0.5 * (left + right)
        max_width = max(max_width, width)
        t = midpoint / logR
        ph = abs(phi_hat(t, L, y_count, quad_n))
        h_ratio = abs(H_value(K, t)) / K if K else 0.0
        q_ratio = abs(Q_value(omega, t)) / variation if variation else 0.0
        rho = h_ratio * q_ratio
        cell_phi_mass = ph * width / logR
        cell_weighted_mass = cell_phi_mass * rho
        phi_mass += cell_phi_mass
        weighted_rho_mass += cell_weighted_mass
        if rho > max_rho:
            max_rho = rho
            worst_midpoint = midpoint
        max_q_ratio = max(max_q_ratio, q_ratio)
        max_h_ratio = max(max_h_ratio, h_ratio)
        top_cells.append(
            {
                "u": midpoint,
                "rho": rho,
                "q_ratio": q_ratio,
                "h_ratio": h_ratio,
                "phi": ph,
                "weighted_share_raw": cell_weighted_mass,
            }
        )

    grid_ratio = weighted_rho_mass / phi_mass if phi_mass else 0.0
    lipschitz_margin = rho_lipschitz * max_width / 2.0
    certified_ratio = grid_ratio + lipschitz_margin
    top_cells = sorted(top_cells, key=lambda row: row["weighted_share_raw"], reverse=True)[:10]
    total_top = sum(row["weighted_share_raw"] for row in top_cells)
    for row in top_cells:
        row["weighted_share"] = row["weighted_share_raw"] / weighted_rho_mass if weighted_rho_mass else 0.0
        row["top_share"] = row["weighted_share_raw"] / total_top if total_top else 0.0
        del row["weighted_share_raw"]

    return {
        "P": P,
        "R_exp": R_exp,
        "R": R,
        "K": K,
        "L": L,
        "u_min": u_min,
        "u_max": u_max,
        "step": step,
        "cells": n_cells,
        "variation": variation,
        "q_log_moment": q_log_moment,
        "h_lipschitz": h_lipschitz,
        "q_lipschitz": q_lipschitz,
        "rho_lipschitz": rho_lipschitz,
        "grid_ratio": grid_ratio,
        "lipschitz_margin": lipschitz_margin,
        "certified_ratio": certified_ratio,
        "target": target,
        "passes_target": certified_ratio < target,
        "max_rho_grid": max_rho,
        "max_q_ratio_grid": max_q_ratio,
        "max_h_ratio_grid": max_h_ratio,
        "worst_midpoint": worst_midpoint,
        "phi_mass": phi_mass,
        "weighted_rho_mass": weighted_rho_mass,
        "top_cells": top_cells,
    }


def render_markdown(audit: dict) -> str:
    """输出给论文工作台使用的 Markdown 摘要。"""
    lines = [
        "# QLOW-MID-COMP 紧区间网格证书",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本证书把最后单点硬核固定为紧区间",
        "",
        "\\[",
        "2<u\\le U_0,\\qquad U_0=12,",
        "\\]",
        "",
        "并对",
        "",
        "\\[",
        "\\rho_R(u)=\\frac{|H(iu/\\log R)|}{K}\\frac{|Q(iu/\\log R)|}{\\mathcal V_\\omega}",
        "\\]",
        "",
        "做带权平均与导数余量核查。这里的关键不是裸 `Q` 单调性，而是 `Phihat/H/Q` 联合带权吸收。",
        "",
        "## 证书摘要",
        "",
        "| P | R | gridRatio | LipMargin | certified | target | pass | worstU | maxRho |",
        "|---:|---:|---:|---:|---:|---:|:---:|---:|---:|",
    ]
    for case in audit["cases"]:
        lines.append(
            f"| {case['P']} | {case['R']} | {case['grid_ratio']:.6f} | "
            f"{case['lipschitz_margin']:.6f} | {case['certified_ratio']:.6f} | "
            f"{case['target']:.3f} | {'Y' if case['passes_target'] else 'N'} | "
            f"{case['worst_midpoint']:.3f} | {case['max_rho_grid']:.6f} |"
        )
    lines += [
        "",
        "## 导数账本",
        "",
        "对任意一个网格小区间 `I`，若 `m_I` 是中点，则",
        "",
        "\\[",
        "\\rho_R(u)\\le \\rho_R(m_I)+\\frac{|I|}{2}\\left(",
        "\\frac{\\log(K!)}{K\\log R}+",
        "\\frac{\\sum_\\ell |\\omega_\\ell|\\log\\ell/\\ell}{\\mathcal V_\\omega\\log R}",
        "\\right).",
        "\\]",
        "",
        "因此",
        "",
        "\\[",
        "\\frac{\\int_{2}^{12}|\\widehat\\Phi|\\,|H|\\,|Q|\\,du/\\log R}",
        "{K\\mathcal V_\\omega\\int_{2}^{12}|\\widehat\\Phi|\\,du/\\log R}",
        "\\le",
        "\\operatorname{Avg}_{|\\widehat\\Phi|}(\\rho_R)+\\operatorname{LipMargin}.",
        "\\]",
        "",
        "这个处理保留了 `Phihat` 的真实权重，不再使用会丢失余量的逐点 `sup rho`。",
        "",
        "## 审稿口径",
        "",
        "- 当前证书仍是浮点网格证书，作用是定位并压缩最后硬点。",
        "- 要升级为正式无条件证明，需要把 `Phihat`、`H`、`Q` 的网格值改为有理区间外向舍入。",
        "- 由于频带 `2<u<=12` 固定，外向舍入表是固定紧区间解析证书，不是有限模板覆盖无限素数情形。",
        "- 若所有行满足 `certified < target`，则 `QLOW-MID-COMP` 可作为 RSE 临界带的常数输入接入主链。",
        "",
        "## 最大贡献小区间",
    ]
    for case in audit["cases"]:
        lines += ["", f"### P={case['P']} R=P^{case['R_exp']}"]
        for row in case["top_cells"][:5]:
            lines.append(
                f"- u={row['u']:.3f}: rho={row['rho']:.6f}, "
                f"Q={row['q_ratio']:.6f}, H={row['h_ratio']:.6f}, "
                f"weightedShare={row['weighted_share']:.4f}"
            )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003,10007")
    parser.add_argument("--R-exponents", default="0.30,0.35")
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--L-power", type=float, default=2.0)
    parser.add_argument("--u-min", type=float, default=2.0)
    parser.add_argument("--u-max", type=float, default=12.0)
    parser.add_argument("--step", type=float, default=0.02)
    parser.add_argument("--target", type=float, default=0.35)
    parser.add_argument("--y-count", type=int, default=100)
    parser.add_argument("--quad-n", type=int, default=80)
    args = parser.parse_args()

    cases = [
        analyze_case(
            P,
            R_exp,
            args.K,
            args.L_power,
            args.u_min,
            args.u_max,
            args.step,
            args.target,
            args.y_count,
            args.quad_n,
        )
        for P, R_exp in itertools.product(parse_ints(args.P_list), parse_floats(args.R_exponents))
    ]
    audit = {
        "certificate_type": "qlow_mid_comp_grid_certificate",
        "status": "compact_grid_certificate_pending_interval_rounding",
        "parameters": vars(args),
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "qlow-mid-comp-grid-certificate.json"
    md_path = OUT / "qlow-mid-comp-grid-certificate.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
