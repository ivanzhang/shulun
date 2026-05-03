#!/usr/bin/env python3
"""CWM 临界 Selberg 合成权质量扫描。

用法示例：
  python3 experiments/cwm_selberg_critical_mass_scan.py --P-list 5003,20011
  python3 experiments/cwm_selberg_critical_mass_scan.py --R-exponents 0.25,0.30,0.35 --K 16
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


def selberg_model_weights(P: int, R_exp: float) -> tuple[int, dict[int, float]]:
    """构造模型 Selberg/Brun 上界权 lambda_d=mu(d)log(R/d)/log R。"""
    z = math.isqrt(P)
    R = max(2, int(P**R_exp))
    primes = primes_upto(z)
    weights: dict[int, float] = {}
    logR = math.log(R)
    for d, mu in squarefree_products(primes, R):
        if d <= R:
            weights[d] = mu * max(0.0, math.log(R / d) / logR)
    return R, weights


def compose_omega(weights: dict[int, float]) -> dict[int, float]:
    """由 lambda_d 合成 omega_l=sum_{[d1,d2]=l} lambda_d1 lambda_d2。"""
    omega: dict[int, float] = defaultdict(float)
    items = list(weights.items())
    for d1, w1 in items:
        for d2, w2 in items:
            omega[lcm(d1, d2)] += w1 * w2
    return dict(omega)


def analyze_case(P: int, beta: float, m_exp: float, R_exp: float, K: int, L_power: float) -> dict:
    X = int(beta * P * P)
    M = max(1, int(P**m_exp))
    Pm = X / M
    L = max(2.0, math.log(P) ** L_power)
    R, lambdas = selberg_model_weights(P, R_exp)
    omega = compose_omega(lambdas)
    total_abs_per_h = sum(abs(w) / ell for ell, w in omega.items())
    total_signed_per_h = sum(w / ell for ell, w in omega.items())

    crit_abs = 0.0
    crit_signed = 0.0
    crit_pairs = 0
    crit_by_h = []
    for h in range(1, K + 1):
        low = h * Pm / L
        high = h * Pm * L
        h_abs = 0.0
        h_signed = 0.0
        h_count = 0
        for ell, w in omega.items():
            if low < ell < high:
                h_abs += abs(w) / ell
                h_signed += w / ell
                h_count += 1
        crit_abs += h_abs
        crit_signed += h_signed
        crit_pairs += h_count
        crit_by_h.append({"h": h, "abs_mass": h_abs, "signed_mass": h_signed, "ell_count": h_count})

    total_abs = K * total_abs_per_h
    total_signed = K * total_signed_per_h
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
        "lambda_count": len(lambdas),
        "omega_count": len(omega),
        "total_abs_mass": total_abs,
        "total_signed_mass": total_signed,
        "critical_abs_mass": crit_abs,
        "critical_signed_mass": crit_signed,
        "critical_fraction_abs": crit_abs / total_abs if total_abs else 0.0,
        "critical_pairs": crit_pairs,
        "max_h_abs": max(crit_by_h, key=lambda r: r["abs_mass"]) if crit_by_h else None,
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# CWM 临界 Selberg 合成权质量扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本扫描使用模型上界权",
        "",
        "\\[",
        "\\lambda_d=\\mu(d)\\frac{\\log(R/d)}{\\log R},\\qquad d\\le R,",
        "\\]",
        "",
        "并合成",
        "",
        "\\[",
        "\\omega_\\ell=\\sum_{[d_1,d_2]=\\ell}\\lambda_{d_1}\\lambda_{d_2}.",
        "\\]",
        "",
        "它不是正式 Selberg 最优权证明，只用于判断 `CWM` 是否现实。",
        "",
        "## 总体判断",
        "",
        "- 若 `critical_abs_mass` 已明显趋小，则 `CWM` 有希望直接闭合。",
        "- 若 `critical_abs_mass` 不小但 `critical_signed_mass` 很小，则应利用 Selberg 符号相消，转向 signed-CWM。",
        "- 若二者都不小，则应走 `CRD`：临界 lcm 层共振推出 CRTDefect。",
        "",
        "## 样本摘要",
    ]
    for case in audit["cases"]:
        max_h = case["max_h_abs"] or {"h": None, "abs_mass": 0, "ell_count": 0}
        lines.append(
            f"- P={case['P']} M=P^{case['M_exp']} R=P^{case['R_exp']} "
            f"Pm={case['P_m']:.2f} R={case['R']} omega={case['omega_count']} "
            f"critAbs={case['critical_abs_mass']:.4g} "
            f"critSigned={case['critical_signed_mass']:.4g} "
            f"fracAbs={case['critical_fraction_abs']:.3f} "
            f"maxH={max_h['h']} mass={max_h['abs_mass']:.4g} ellCount={max_h['ell_count']}"
        )
    lines += [
        "",
        "## 对硬点的影响",
        "",
        "这一扫描若显示临界绝对质量不随 `P` 下降，就说明不能只靠粗糙绝对值账本闭合 `RSE-CRIT`。",
        "此时应把正式证明目标改为以下二选一：",
        "",
        "1. `signed-CWM`：证明 Selberg 合成权在临界带内有足够符号相消；",
        "2. `CRD`：证明临界绝对质量集中必然导致小模投影或短差值方向 CRTDefect。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="5003,20011,100003")
    parser.add_argument("--beta", type=float, default=0.73)
    parser.add_argument("--m-exponents", default="1.0,1.2,1.4")
    parser.add_argument("--R-exponents", default="0.25,0.30,0.35")
    parser.add_argument("--K", type=int, default=16)
    parser.add_argument("--L-power", type=float, default=2.0)
    args = parser.parse_args()

    cases = [
        analyze_case(P, args.beta, m_exp, R_exp, args.K, args.L_power)
        for P, m_exp, R_exp in itertools.product(
            parse_ints(args.P_list),
            parse_floats(args.m_exponents),
            parse_floats(args.R_exponents),
        )
    ]
    audit = {
        "certificate_type": "cwm_selberg_critical_mass_scan",
        "status": "model_weight_scan_not_a_proof",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "beta": args.beta,
            "m_exponents": parse_floats(args.m_exponents),
            "R_exponents": parse_floats(args.R_exponents),
            "K": args.K,
            "L_power": args.L_power,
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "cwm-selberg-critical-mass-scan.json"
    md_path = OUT / "cwm-selberg-critical-mass-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
