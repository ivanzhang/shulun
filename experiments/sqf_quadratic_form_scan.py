#!/usr/bin/env python3
"""SQF Selberg 二次型 Mellin 预算扫描。

用法示例：
  python3 experiments/sqf_quadratic_form_scan.py --P-list 2003,5003
  python3 experiments/sqf_quadratic_form_scan.py --P-list 10007 --t-max 80 --t-count 161
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "monograph"
TAU = 2.0 * math.pi


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数表。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            start = i * i
            sieve[start : n + 1 : i] = [False] * (((n - start) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def parse_ints(raw: str) -> list[int]:
    return [int(x) for x in raw.split(",") if x.strip()]


def parse_floats(raw: str) -> list[float]:
    return [float(x) for x in raw.split(",") if x.strip()]


def squarefree_products(primes: list[int], limit: int) -> list[tuple[int, int]]:
    """枚举 d<=limit 的 squarefree d，并返回 (d, mu(d))。"""
    values = [(1, 1)]
    for p in primes:
        additions = []
        for d, mu in values:
            nd = d * p
            if nd <= limit:
                additions.append((nd, -mu))
        values.extend(additions)
    return sorted(set(values))


def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


def selberg_model_weights(P: int, R_exp: float) -> tuple[int, dict[int, float]]:
    """构造模型 Selberg/Brun 上界权。"""
    R = max(2, int(P**R_exp))
    primes = primes_upto(math.isqrt(P))
    weights: dict[int, float] = {}
    logR = math.log(R)
    for d, mu in squarefree_products(primes, R):
        weights[d] = mu * max(0.0, math.log(R / d) / logR)
    return R, weights


def compose_omega(weights: dict[int, float]) -> dict[int, float]:
    """由 lambda_d 合成 omega_l=sum_[d1,d2]=l lambda_d1 lambda_d2。"""
    omega: dict[int, float] = defaultdict(float)
    items = list(weights.items())
    for d1, w1 in items:
        for d2, w2 in items:
            omega[lcm(d1, d2)] += w1 * w2
    return dict(omega)


def expi(x: float) -> complex:
    return complex(math.cos(TAU * x), math.sin(TAU * x))


def G_kernel(u: float, quad_n: int) -> complex:
    """G(u)=int_1^2 e(u/t) dt/t。"""
    total = 0j
    step = 1.0 / quad_n
    for i in range(quad_n):
        t = 1.0 + (i + 0.5) * step
        total += expi(u / t) * (1.0 / t) * step
    return total


def phi_hat(tau: float, L: float, u_count: int, quad_n: int) -> complex:
    """数值计算 sharp-cutoff Phihat(it)=int G(u) u^(it) du/u。"""
    log_low = -math.log(L)
    log_high = math.log(L)
    step = (log_high - log_low) / u_count
    total = 0j
    for i in range(u_count):
        y = log_low + (i + 0.5) * step
        u = math.exp(y)
        total += G_kernel(u, quad_n) * complex(math.cos(tau * y), math.sin(tau * y)) * step
    return total


def Q_value(omega: dict[int, float], tau: float) -> complex:
    """Q(it)=sum omega_l l^(it-1)。"""
    total = 0j
    for ell, weight in omega.items():
        angle = tau * math.log(ell)
        total += (weight / ell) * complex(math.cos(angle), math.sin(angle))
    return total


def H_value(K: int, tau: float) -> complex:
    """H(it)=sum_{h<=K} h^(-it)。"""
    total = 0j
    for h in range(1, K + 1):
        angle = -tau * math.log(h)
        total += complex(math.cos(angle), math.sin(angle))
    return total


def t_grid(t_max: float, t_count: int) -> list[float]:
    if t_count <= 1:
        return [0.0]
    step = 2 * t_max / (t_count - 1)
    return [-t_max + i * step for i in range(t_count)]


def analyze_case(
    P: int,
    beta: float,
    m_exp: float,
    R_exp: float,
    K: int,
    L_power: float,
    t_max: float,
    t_count: int,
    u_count: int,
    quad_n: int,
) -> dict:
    X = int(beta * P * P)
    M = max(1, int(P**m_exp))
    Pm = X / M
    L = max(2.0, math.log(P) ** L_power)
    R, weights = selberg_model_weights(P, R_exp)
    omega = compose_omega(weights)
    q_abs = sum(abs(w) / ell for ell, w in omega.items())
    q_zero = Q_value(omega, 0.0)
    rows = []
    budget = 0.0
    trivial_budget = 0.0
    q_weighted = 0.0
    h_weighted = 0.0
    ph_weighted = 0.0
    max_row = None
    step = 2 * t_max / max(1, t_count - 1)
    for tau in t_grid(t_max, t_count):
        ph = phi_hat(tau, L, u_count, quad_n)
        hv = H_value(K, tau)
        qv = Q_value(omega, tau)
        integrand = abs(ph) * abs(hv) * abs(qv)
        trivial = abs(ph) * K * q_abs
        budget += integrand * step
        trivial_budget += trivial * step
        q_weighted += abs(ph) * abs(hv) * abs(qv) * step
        h_weighted += abs(ph) * abs(hv) * q_abs * step
        ph_weighted += abs(ph) * K * q_abs * step
        row = {
            "t": tau,
            "abs_phi": abs(ph),
            "abs_H": abs(hv),
            "abs_Q": abs(qv),
            "Q_over_Qabs": abs(qv) / q_abs if q_abs else 0.0,
            "H_over_K": abs(hv) / K if K else 0.0,
            "integrand": integrand,
        }
        rows.append(row)
        if max_row is None or row["integrand"] > max_row["integrand"]:
            max_row = row
    top_rows = sorted(rows, key=lambda r: r["integrand"], reverse=True)[:8]
    q_ratios = [r["Q_over_Qabs"] for r in rows]
    h_ratios = [r["H_over_K"] for r in rows]
    return {
        "P": P,
        "beta": beta,
        "M_exp": m_exp,
        "M": M,
        "P_m": Pm,
        "R_exp": R_exp,
        "R": R,
        "K": K,
        "L": L,
        "omega_count": len(omega),
        "t_max": t_max,
        "t_count": t_count,
        "Q_abs": q_abs,
        "Q_zero_abs": abs(q_zero),
        "Q_zero_ratio": abs(q_zero) / q_abs if q_abs else 0.0,
        "budget": budget,
        "trivial_budget": trivial_budget,
        "budget_ratio": budget / trivial_budget if trivial_budget else 0.0,
        "avg_Q_over_Qabs": sum(q_ratios) / len(q_ratios) if q_ratios else 0.0,
        "max_Q_over_Qabs": max(q_ratios) if q_ratios else 0.0,
        "avg_H_over_K": sum(h_ratios) / len(h_ratios) if h_ratios else 0.0,
        "max_H_over_K": max(h_ratios) if h_ratios else 0.0,
        "top_integrand": top_rows,
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# SQF Selberg 二次型 Mellin 预算扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本实验近似扫描",
        "",
        "\\[",
        "\\int |\\widehat\\Phi(it)|\\,|H(it)|\\,|Q(it)|\\,dt",
        "\\]",
        "",
        "并与平凡预算 `int |Phihat| K sum|omega_l|/l dt` 比较。",
        "",
        "## 摘要",
    ]
    for case in audit["cases"]:
        top = case["top_integrand"][0] if case["top_integrand"] else {
            "t": 0.0,
            "Q_over_Qabs": 0.0,
            "H_over_K": 0.0,
        }
        lines.append(
            f"- P={case['P']} M=P^{case['M_exp']} R=P^{case['R_exp']} "
            f"omega={case['omega_count']} budget/trivial={case['budget_ratio']:.3f} "
            f"Q0/Qabs={case['Q_zero_ratio']:.3f} avgQ/Qabs={case['avg_Q_over_Qabs']:.3f} "
            f"avgH/K={case['avg_H_over_K']:.3f} "
            f"top t={top['t']:.1f} Q/Qabs={top['Q_over_Qabs']:.3f} H/K={top['H_over_K']:.3f}"
        )
    lines += [
        "",
        "## 证明判读",
        "",
        "- `Q0/Qabs` 小：Selberg 二次型在低频已有强符号相消。",
        "- `budget/trivial` 小：`SQF` 主要来自 `Q(it)` 与短 `h` 和的共同相消。",
        "- 若 `top integrand` 集中在小 `t`，应优先证明低频 `Q(it)` 零阶抵消。",
        "- 若大 `t` 主导，则需要依赖 `Phihat` 衰减或平滑截断提升。",
        "",
        "## 下一步接口",
        "",
        "将 `SQF` 拆为：",
        "",
        "```text",
        "SQF-Q0: Q(it) 在低频相对 sum|omega|/ell 有固定节省；",
        "SQF-PHI: 平滑截断使 |Phihat(it)| 快速衰减；",
        "SQF-H: 短 h-sum 在中高频提供平均节省。",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003,10007")
    parser.add_argument("--beta", type=float, default=0.73)
    parser.add_argument("--m-exponents", default="1.2,1.4")
    parser.add_argument("--R-exponents", default="0.30,0.35")
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--L-power", type=float, default=2.0)
    parser.add_argument("--t-max", type=float, default=60.0)
    parser.add_argument("--t-count", type=int, default=121)
    parser.add_argument("--u-count", type=int, default=180)
    parser.add_argument("--quad-n", type=int, default=120)
    args = parser.parse_args()

    cases = [
        analyze_case(
            P,
            args.beta,
            m_exp,
            R_exp,
            args.K,
            args.L_power,
            args.t_max,
            args.t_count,
            args.u_count,
            args.quad_n,
        )
        for P, m_exp, R_exp in itertools.product(
            parse_ints(args.P_list),
            parse_floats(args.m_exponents),
            parse_floats(args.R_exponents),
        )
    ]
    audit = {
        "certificate_type": "sqf_quadratic_form_scan",
        "status": "mellin_budget_scan_not_a_proof",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "beta": args.beta,
            "m_exponents": parse_floats(args.m_exponents),
            "R_exponents": parse_floats(args.R_exponents),
            "K": args.K,
            "L_power": args.L_power,
            "t_max": args.t_max,
            "t_count": args.t_count,
            "u_count": args.u_count,
            "quad_n": args.quad_n,
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "sqf-quadratic-form-scan.json"
    md_path = OUT / "sqf-quadratic-form-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
