#!/usr/bin/env python3
"""SQF-QLOW：标准权与 Q0 最优 Selberg 权比较扫描。

用法示例：
  python3 experiments/sqf_qlow_optimal_weight_scan.py --P-list 2003,5003
  python3 experiments/sqf_qlow_optimal_weight_scan.py --P-list 10007 --R-exponents 0.30,0.35
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


def solve_linear_system(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    """高斯消元解线性方程；仅用于小型实验矩阵。"""
    n = len(rhs)
    a = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-14:
            raise ValueError("singular matrix in Selberg optimizer")
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
        div = a[col][col]
        for j in range(col, n + 1):
            a[col][j] /= div
        for r in range(n):
            if r == col:
                continue
            factor = a[r][col]
            if factor == 0:
                continue
            for j in range(col, n + 1):
                a[r][j] -= factor * a[col][j]
    return [a[i][n] for i in range(n)]


def standard_weights(P: int, R_exp: float) -> tuple[int, dict[int, float], list[int]]:
    """模型 Brun/Selberg 权 lambda_d=mu(d)log(R/d)/log R。"""
    R = max(2, int(P**R_exp))
    primes = primes_upto(math.isqrt(P))
    logR = math.log(R)
    weights: dict[int, float] = {}
    for d, mu in squarefree_products(primes, R):
        weights[d] = mu * max(0.0, math.log(R / d) / logR)
    return R, weights, primes


def optimal_q0_weights(P: int, R_exp: float) -> tuple[int, dict[int, float], list[int]]:
    """求解 Q(0)=sum lambda_d lambda_e/[d,e] 的 λ1=1 最优权。"""
    R = max(2, int(P**R_exp))
    primes = primes_upto(math.isqrt(P))
    ds = [d for d, _mu in squarefree_products(primes, R)]
    matrix = [[1.0 / lcm(d, e) for e in ds] for d in ds]
    e1 = [1.0 if d == 1 else 0.0 for d in ds]
    inv_e1 = solve_linear_system(matrix, e1)
    denom = sum(e1[i] * inv_e1[i] for i in range(len(ds)))
    weights = {d: inv_e1[i] / denom for i, d in enumerate(ds)}
    return R, weights, primes


def compose_omega(weights: dict[int, float]) -> dict[int, float]:
    """由 lambda_d 合成 omega_l=sum_[d1,d2]=l lambda_d1 lambda_d2。"""
    omega: dict[int, float] = defaultdict(float)
    items = list(weights.items())
    for d1, w1 in items:
        for d2, w2 in items:
            omega[lcm(d1, d2)] += w1 * w2
    return dict(omega)


def Q_value(omega: dict[int, float], tau: float) -> complex:
    """Q(it)=sum omega_l l^(it-1)。"""
    total = 0j
    for ell, weight in omega.items():
        angle = tau * math.log(ell)
        total += (weight / ell) * complex(math.cos(angle), math.sin(angle))
    return total


def H_value(K: int, tau: float) -> complex:
    """H(it)=sum h^(-it)。"""
    total = 0j
    for h in range(1, K + 1):
        angle = -tau * math.log(h)
        total += complex(math.cos(angle), math.sin(angle))
    return total


def expi(x: float) -> complex:
    return complex(math.cos(TAU * x), math.sin(TAU * x))


def G_kernel(u: float, quad_n: int) -> complex:
    """G(u)=int_1^2 e(u/t) dt/t。"""
    total = 0j
    step = 1.0 / quad_n
    for i in range(quad_n):
        t = 1.0 + (i + 0.5) * step
        total += expi(u / t) * step / t
    return total


def phi_hat(tau: float, L: float, u_count: int, quad_n: int) -> complex:
    """粗略计算 Phihat(it)=int_{1/L}^L G(u)u^(it)du/u。"""
    lo = -math.log(L)
    hi = math.log(L)
    step = (hi - lo) / u_count
    total = 0j
    for i in range(u_count):
        y = lo + (i + 0.5) * step
        u = math.exp(y)
        total += G_kernel(u, quad_n) * complex(math.cos(tau * y), math.sin(tau * y)) * step
    return total


def scan_weight(
    label: str,
    weights: dict[int, float],
    K: int,
    L: float,
    t_max: float,
    t_count: int,
    u_count: int,
    quad_n: int,
) -> dict:
    omega = compose_omega(weights)
    q_abs = sum(abs(w) / ell for ell, w in omega.items())
    q0 = abs(Q_value(omega, 0.0))
    budget = 0.0
    trivial = 0.0
    max_q_ratio = 0.0
    avg_q_ratio = 0.0
    max_row = None
    step = 2 * t_max / max(1, t_count - 1)
    for i in range(t_count):
        tau = -t_max + i * step
        ph = abs(phi_hat(tau, L, u_count, quad_n))
        hv = abs(H_value(K, tau))
        qv = abs(Q_value(omega, tau))
        ratio = qv / q_abs if q_abs else 0.0
        avg_q_ratio += ratio
        max_q_ratio = max(max_q_ratio, ratio)
        integrand = ph * hv * qv
        budget += integrand * step
        trivial += ph * K * q_abs * step
        row = {"t": tau, "Q_ratio": ratio, "H_ratio": hv / K if K else 0.0, "integrand": integrand}
        if max_row is None or row["integrand"] > max_row["integrand"]:
            max_row = row
    avg_q_ratio /= t_count
    return {
        "label": label,
        "lambda_count": len(weights),
        "omega_count": len(omega),
        "lambda_l1": sum(abs(v) for v in weights.values()),
        "lambda_l2": math.sqrt(sum(v * v for v in weights.values())),
        "Q_abs": q_abs,
        "Q0": q0,
        "Q0_ratio": q0 / q_abs if q_abs else 0.0,
        "budget": budget,
        "trivial": trivial,
        "budget_ratio": budget / trivial if trivial else 0.0,
        "avg_Q_ratio": avg_q_ratio,
        "max_Q_ratio": max_q_ratio,
        "top": max_row,
    }


def analyze_case(P: int, R_exp: float, K: int, L_power: float, t_max: float, t_count: int, u_count: int, quad_n: int) -> dict:
    L = max(2.0, math.log(P) ** L_power)
    R_std, weights_std, _ = standard_weights(P, R_exp)
    R_opt, weights_opt, _ = optimal_q0_weights(P, R_exp)
    return {
        "P": P,
        "R_exp": R_exp,
        "R": R_std,
        "K": K,
        "L": L,
        "standard": scan_weight("standard-log", weights_std, K, L, t_max, t_count, u_count, quad_n),
        "optimal": scan_weight("optimal-Q0", weights_opt, K, L, t_max, t_count, u_count, quad_n),
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# SQF-QLOW 最优 Selberg 权扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本实验比较两类权：标准对数权与精确最小化 `Q(0)` 的 Selberg 权。",
        "目的不是替代证明，而是判断 `SQF-QLOW` 是否应使用核适配/低频优化权。",
        "",
        "## 摘要",
    ]
    for case in audit["cases"]:
        std = case["standard"]
        opt = case["optimal"]
        lines.append(
            f"- P={case['P']} R=P^{case['R_exp']} R={case['R']} "
            f"std Q0/abs={std['Q0_ratio']:.3f} budget={std['budget_ratio']:.3f} "
            f"opt Q0/abs={opt['Q0_ratio']:.3f} budget={opt['budget_ratio']:.3f} "
            f"optL1/stdL1={opt['lambda_l1']/std['lambda_l1']:.2f}"
        )
    lines += [
        "",
        "## 判读",
        "",
        "- 若 `optimal-Q0` 显著降低 `Q0/abs` 且不显著增大 `budget`，则 `SQF-QLOW` 应使用精确 Selberg 极小权。",
        "- 若 `Q0/abs` 降低但 `budget` 不降，瓶颈不是 `t=0`，而是 `|t|≈1` 的低频带。",
        "- 若 `lambda_l1` 暴涨，则权重优化会破坏上界筛误差账本，不能直接采用。",
        "",
        "## 下一步接口",
        "",
        "把 `SQF-QLOW` 拆成：",
        "",
        "```text",
        "QLOW-OPT: 选择 Selberg 权最小化低频二次型；",
        "QLOW-STAB: 优化权在 |t|<=T0 内保持稳定；",
        "QLOW-VAR: 优化权的总变差不破坏 RRD/OSPC 账本。",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003,10007")
    parser.add_argument("--R-exponents", default="0.30,0.35")
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--L-power", type=float, default=2.0)
    parser.add_argument("--t-max", type=float, default=40.0)
    parser.add_argument("--t-count", type=int, default=81)
    parser.add_argument("--u-count", type=int, default=100)
    parser.add_argument("--quad-n", type=int, default=80)
    args = parser.parse_args()
    cases = [
        analyze_case(P, R_exp, args.K, args.L_power, args.t_max, args.t_count, args.u_count, args.quad_n)
        for P, R_exp in itertools.product(parse_ints(args.P_list), parse_floats(args.R_exponents))
    ]
    audit = {
        "certificate_type": "sqf_qlow_optimal_weight_scan",
        "status": "weight_optimization_scan_not_a_proof",
        "parameters": {
            "P_list": parse_ints(args.P_list),
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
    json_path = OUT / "sqf-qlow-optimal-weight-scan.json"
    md_path = OUT / "sqf-qlow-optimal-weight-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
