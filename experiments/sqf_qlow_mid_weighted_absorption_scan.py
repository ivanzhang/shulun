#!/usr/bin/env python3
"""QLOW-MID：Phihat/H/Q 联合带权吸收扫描。

用法示例：
  python3 experiments/sqf_qlow_mid_weighted_absorption_scan.py --P-list 2003,5003
  python3 experiments/sqf_qlow_mid_weighted_absorption_scan.py --u-max 80 --u-count 401
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
    """高斯消元解线性方程。"""
    n = len(rhs)
    rows = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(rows[r][col]))
        if abs(rows[pivot][col]) < 1e-14:
            raise ValueError("singular matrix")
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        for j in range(col, n + 1):
            rows[col][j] /= divisor
        for r in range(n):
            if r == col:
                continue
            factor = rows[r][col]
            if factor == 0:
                continue
            for j in range(col, n + 1):
                rows[r][j] -= factor * rows[col][j]
    return [rows[i][n] for i in range(n)]


def optimal_q0_weights(P: int, R_exp: float) -> tuple[int, dict[int, float]]:
    """求解 Q(0)=sum lambda_d lambda_e/[d,e] 的 λ1=1 最优权。"""
    R = max(2, int(P**R_exp))
    primes = primes_upto(math.isqrt(P))
    ds = [d for d, _ in squarefree_products(primes, R)]
    matrix = [[1.0 / lcm(d, e) for e in ds] for d in ds]
    e1 = [1.0 if d == 1 else 0.0 for d in ds]
    inv_e1 = solve_linear_system(matrix, e1)
    denom = sum(e1[i] * inv_e1[i] for i in range(len(ds)))
    return R, {d: inv_e1[i] / denom for i, d in enumerate(ds)}


def compose_omega(weights: dict[int, float]) -> dict[int, float]:
    """由 lambda_d 合成 omega_l=sum_[d1,d2]=l lambda_d1 lambda_d2。"""
    omega: dict[int, float] = defaultdict(float)
    items = list(weights.items())
    for d1, w1 in items:
        for d2, w2 in items:
            omega[lcm(d1, d2)] += w1 * w2
    return dict(omega)


def Q_value(omega: dict[int, float], t: float) -> complex:
    """Q(it)=sum omega_l l^(it-1)。"""
    total = 0j
    for ell, weight in omega.items():
        angle = t * math.log(ell)
        total += (weight / ell) * complex(math.cos(angle), math.sin(angle))
    return total


def H_value(K: int, t: float) -> complex:
    """H(it)=sum h^(-it)。"""
    total = 0j
    for h in range(1, K + 1):
        angle = -t * math.log(h)
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


def phi_hat(t: float, L: float, y_count: int, quad_n: int) -> complex:
    """粗略计算 Phihat(it)=int_{1/L}^L G(u)u^(it)du/u。"""
    lo = -math.log(L)
    hi = math.log(L)
    step = (hi - lo) / y_count
    total = 0j
    for i in range(y_count):
        y = lo + (i + 0.5) * step
        u = math.exp(y)
        total += G_kernel(u, quad_n) * complex(math.cos(t * y), math.sin(t * y)) * step
    return total


def band_name(u: float) -> str:
    if u <= 0.5:
        return "ultra_0_0p5"
    if u <= 2:
        return "trans_0p5_2"
    if u <= 6:
        return "mid_2_6"
    if u <= 12:
        return "mid_6_12"
    if u <= 30:
        return "tail_12_30"
    return "tail_30_plus"


def analyze_case(
    P: int,
    R_exp: float,
    K: int,
    L_power: float,
    u_max: float,
    u_count: int,
    y_count: int,
    quad_n: int,
) -> dict:
    R, weights = optimal_q0_weights(P, R_exp)
    omega = compose_omega(weights)
    logR = math.log(R)
    L = max(2.0, math.log(P) ** L_power)
    variation = sum(abs(v) / ell for ell, v in omega.items())
    du = u_max / max(1, u_count - 1)
    bands: dict[str, dict[str, float]] = defaultdict(
        lambda: {
            "budget": 0.0,
            "trivial": 0.0,
            "phi_mass": 0.0,
            "max_Q_ratio": 0.0,
            "max_H_ratio": 0.0,
            "max_integrand_ratio": 0.0,
            "count": 0.0,
        }
    )
    total_budget = 0.0
    total_trivial = 0.0
    mid_budget = 0.0
    mid_trivial = 0.0
    top_rows = []
    for i in range(u_count):
        u = i * du
        t = u / logR if logR else 0.0
        ph = abs(phi_hat(t, L, y_count, quad_n))
        hv = abs(H_value(K, t))
        qv = abs(Q_value(omega, t))
        budget = ph * hv * qv * du / logR
        trivial = ph * K * variation * du / logR
        total_budget += budget
        total_trivial += trivial
        if u > 2:
            mid_budget += budget
            mid_trivial += trivial
        name = band_name(u)
        row = bands[name]
        row["budget"] += budget
        row["trivial"] += trivial
        row["phi_mass"] += ph * du / logR
        row["max_Q_ratio"] = max(row["max_Q_ratio"], qv / variation if variation else 0.0)
        row["max_H_ratio"] = max(row["max_H_ratio"], hv / K if K else 0.0)
        row["max_integrand_ratio"] = max(row["max_integrand_ratio"], budget / trivial if trivial else 0.0)
        row["count"] += 1
        top_rows.append(
            {
                "u": u,
                "t": t,
                "phi": ph,
                "Q_ratio": qv / variation if variation else 0.0,
                "H_ratio": hv / K if K else 0.0,
                "budget": budget,
                "budget_ratio_point": budget / trivial if trivial else 0.0,
                "band": name,
            }
        )
    band_summary = []
    for name in ["ultra_0_0p5", "trans_0p5_2", "mid_2_6", "mid_6_12", "tail_12_30", "tail_30_plus"]:
        row = bands[name]
        band_summary.append(
            {
                "band": name,
                "budget": row["budget"],
                "trivial": row["trivial"],
                "ratio": row["budget"] / row["trivial"] if row["trivial"] else 0.0,
                "share_total_budget": row["budget"] / total_budget if total_budget else 0.0,
                "phi_mass": row["phi_mass"],
                "max_Q_ratio": row["max_Q_ratio"],
                "max_H_ratio": row["max_H_ratio"],
                "max_integrand_ratio": row["max_integrand_ratio"],
            }
        )
    top_rows = sorted(top_rows, key=lambda r: r["budget"], reverse=True)[:12]
    return {
        "P": P,
        "R_exp": R_exp,
        "R": R,
        "K": K,
        "L": L,
        "u_max": u_max,
        "u_count": u_count,
        "variation": variation,
        "total_budget": total_budget,
        "total_trivial": total_trivial,
        "total_ratio": total_budget / total_trivial if total_trivial else 0.0,
        "mid_budget": mid_budget,
        "mid_trivial": mid_trivial,
        "mid_ratio": mid_budget / mid_trivial if mid_trivial else 0.0,
        "mid_share_total": mid_budget / total_budget if total_budget else 0.0,
        "band_summary": band_summary,
        "top_budget_rows": top_rows,
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# QLOW-MID 带权吸收扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本实验直接扫描",
        "",
        "\\[",
        "\\int_{u>2}|\\widehat\\Phi(iu/\\log R)|\\,|H(iu/\\log R)|\\,|Q(iu/\\log R)|\\,\\frac{du}{\\log R}.",
        "\\]",
        "",
        "并按 `u` 段分解预算，检查裸 `Q` 反弹是否被 `Phihat/H` 带权吸收。",
        "",
        "## 摘要",
    ]
    for case in audit["cases"]:
        top = case["top_budget_rows"][0] if case["top_budget_rows"] else {"u": 0.0, "band": "", "budget_ratio_point": 0.0}
        lines.append(
            f"- P={case['P']} R=P^{case['R_exp']} R={case['R']} "
            f"totalRatio={case['total_ratio']:.3f} midRatio={case['mid_ratio']:.3f} "
            f"midShare={case['mid_share_total']:.3f} topU={top['u']:.2f} "
            f"topBand={top['band']} pointRatio={top['budget_ratio_point']:.3f}"
        )
    lines += ["", "## 分段预算"]
    for case in audit["cases"]:
        lines.append("")
        lines.append(f"### P={case['P']} R=P^{case['R_exp']}")
        for row in case["band_summary"]:
            lines.append(
                f"- {row['band']}: ratio={row['ratio']:.3f} shareBudget={row['share_total_budget']:.3f} "
                f"maxQ={row['max_Q_ratio']:.3f} maxH={row['max_H_ratio']:.3f}"
            )
    lines += [
        "",
        "## 判读",
        "",
        "- 若 `midShare` 小，说明中频峰虽高但总预算很小，可由 `Phihat` 衰减吸收。",
        "- 若 `midRatio` 小，说明 `Q/H` 在中频整体仍有固定节省。",
        "- 若主预算集中于 `u<=2`，则 `QLOW-MID` 已不是主障碍，应回到 `QLOW-TRANS` 的有限宽证明。",
        "",
        "## 证明接口",
        "",
        "实验支持把 `QLOW-MID` 写成带权积分命题，而不是裸 `Q` 命题：",
        "",
        "```text",
        "QLOW-MID-W: 中频峰的带权总预算小；",
        "QLOW-MID-PHI: u>U0 的尾部由 Phihat 衰减吸收；",
        "QLOW-MID-COMP: 2<u<=U0 的有限中频由显式常数积分界吸收。",
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
    parser.add_argument("--u-max", type=float, default=80.0)
    parser.add_argument("--u-count", type=int, default=401)
    parser.add_argument("--y-count", type=int, default=100)
    parser.add_argument("--quad-n", type=int, default=80)
    args = parser.parse_args()
    cases = [
        analyze_case(P, R_exp, args.K, args.L_power, args.u_max, args.u_count, args.y_count, args.quad_n)
        for P, R_exp in itertools.product(parse_ints(args.P_list), parse_floats(args.R_exponents))
    ]
    audit = {
        "certificate_type": "sqf_qlow_mid_weighted_absorption_scan",
        "status": "weighted_mid_absorption_scan_not_a_proof",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "R_exponents": parse_floats(args.R_exponents),
            "K": args.K,
            "L_power": args.L_power,
            "u_max": args.u_max,
            "u_count": args.u_count,
            "y_count": args.y_count,
            "quad_n": args.quad_n,
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "sqf-qlow-mid-weighted-absorption-scan.json"
    md_path = OUT / "sqf-qlow-mid-weighted-absorption-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
