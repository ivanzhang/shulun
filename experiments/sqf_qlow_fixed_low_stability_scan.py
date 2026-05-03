#!/usr/bin/env python3
"""QLOW-STAB fixed-low 归一化频率稳定扫描。

用法示例：
  python3 experiments/sqf_qlow_fixed_low_stability_scan.py --P-list 2003,5003
  python3 experiments/sqf_qlow_fixed_low_stability_scan.py --u-max 12 --u-count 121
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


def local_phase_dispersion(P: int, R: int, u: float) -> float:
    """粗略欧拉相位离散量 sum_{p<=R}(1-cos(u log p/logR))/p。"""
    if R < 2:
        return 0.0
    logR = math.log(R)
    total = 0.0
    for p in primes_upto(min(R, math.isqrt(P))):
        total += (1.0 - math.cos(u * math.log(p) / logR)) / p
    return total


def analyze_case(P: int, R_exp: float, u_max: float, u_count: int) -> dict:
    R, weights = optimal_q0_weights(P, R_exp)
    omega = compose_omega(weights)
    logR = math.log(R)
    variation = sum(abs(v) / ell for ell, v in omega.items())
    rows = []
    bands = {
        "ultra": [],
        "fixed_0p5_2": [],
        "fixed_2_6": [],
        "fixed_6_plus": [],
    }
    for i in range(u_count):
        u = u_max * i / max(1, u_count - 1)
        t = u / logR if logR else 0.0
        q_ratio = abs(Q_value(omega, t)) / variation if variation else 0.0
        disp = local_phase_dispersion(P, R, u)
        row = {"u": u, "t": t, "Q_ratio": q_ratio, "dispersion": disp}
        rows.append(row)
        if u <= 0.5:
            bands["ultra"].append(row)
        elif u <= 2:
            bands["fixed_0p5_2"].append(row)
        elif u <= 6:
            bands["fixed_2_6"].append(row)
        else:
            bands["fixed_6_plus"].append(row)
    band_summary = {}
    for name, items in bands.items():
        band_summary[name] = {
            "count": len(items),
            "max_Q_ratio": max((r["Q_ratio"] for r in items), default=0.0),
            "avg_Q_ratio": sum(r["Q_ratio"] for r in items) / len(items) if items else 0.0,
            "min_dispersion": min((r["dispersion"] for r in items), default=0.0),
            "avg_dispersion": sum(r["dispersion"] for r in items) / len(items) if items else 0.0,
        }
    top_rows = sorted(rows, key=lambda r: r["Q_ratio"], reverse=True)[:10]
    return {
        "P": P,
        "R_exp": R_exp,
        "R": R,
        "lambda_count": len(weights),
        "omega_count": len(omega),
        "lambda_l1": sum(abs(v) for v in weights.values()),
        "variation": variation,
        "Q0_ratio": abs(Q_value(omega, 0.0)) / variation if variation else 0.0,
        "u_max": u_max,
        "u_count": u_count,
        "band_summary": band_summary,
        "top_Q_rows": top_rows,
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# QLOW-STAB fixed-low 稳定性扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "扫描归一化频率",
        "",
        "\\[",
        "u=t\\log R,\\qquad Q(iu/\\log R)/\\mathcal V_\\omega.",
        "\\]",
        "",
        "目标是判断 fixed-low 段是否有统一固定节省，并定位最后需要证明的频带。",
        "",
        "## 摘要",
    ]
    for case in audit["cases"]:
        b0 = case["band_summary"]["ultra"]
        b1 = case["band_summary"]["fixed_0p5_2"]
        b2 = case["band_summary"]["fixed_2_6"]
        b3 = case["band_summary"]["fixed_6_plus"]
        top = case["top_Q_rows"][0] if case["top_Q_rows"] else {"u": 0.0, "Q_ratio": 0.0}
        lines.append(
            f"- P={case['P']} R=P^{case['R_exp']} R={case['R']} Q0={case['Q0_ratio']:.3f} "
            f"maxUltra={b0['max_Q_ratio']:.3f} max0.5-2={b1['max_Q_ratio']:.3f} "
            f"max2-6={b2['max_Q_ratio']:.3f} max6+={b3['max_Q_ratio']:.3f} "
            f"top u={top['u']:.2f} ratio={top['Q_ratio']:.3f}"
        )
    lines += [
        "",
        "## 判读",
        "",
        "- 若最大值始终出现在 `u≈0`，则 fixed-low 段由零频极小化和连续性共同控制。",
        "- 若 `u≈1` 附近反弹，则需要证明优化权的低频稳定，而不是只证明 `Q(0)`。",
        "- 若 `u>=2` 后持续下降，可用欧拉局部相位离散量给出振荡节省。",
        "",
        "## 最窄证明接口",
        "",
        "实验把 `QLOW-STAB fixed-low` 进一步拆为：",
        "",
        "```text",
        "QLOW-ULTRA: 0 <= u <= 1/2，矩阵扰动/Lipschitz；",
        "QLOW-TRANS: 1/2 < u <= 2，有限宽过渡稳定；",
        "QLOW-OSC: u > 2，Euler 局部相位振荡。",
        "```",
        "",
        "其中 `QLOW-TRANS` 是新的最后最窄接口。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003,10007")
    parser.add_argument("--R-exponents", default="0.30,0.35")
    parser.add_argument("--u-max", type=float, default=12.0)
    parser.add_argument("--u-count", type=int, default=121)
    args = parser.parse_args()
    cases = [
        analyze_case(P, R_exp, args.u_max, args.u_count)
        for P, R_exp in itertools.product(parse_ints(args.P_list), parse_floats(args.R_exponents))
    ]
    audit = {
        "certificate_type": "sqf_qlow_fixed_low_stability_scan",
        "status": "fixed_low_stability_scan_not_a_proof",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "R_exponents": parse_floats(args.R_exponents),
            "u_max": args.u_max,
            "u_count": args.u_count,
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "sqf-qlow-fixed-low-stability-scan.json"
    md_path = OUT / "sqf-qlow-fixed-low-stability-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
