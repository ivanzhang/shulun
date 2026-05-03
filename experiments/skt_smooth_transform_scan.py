#!/usr/bin/env python3
"""SKT 平滑 Selberg 变换扫描。

用法示例：
  python3 experiments/skt_smooth_transform_scan.py --P-list 2003,5003
  python3 experiments/skt_smooth_transform_scan.py --P-list 10007 --quad-n 800
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


def selberg_model_weights(P: int, R_exp: float) -> tuple[int, dict[int, float], list[int]]:
    """构造模型 Selberg/Brun 上界权。"""
    z = math.isqrt(P)
    R = max(2, int(P**R_exp))
    primes = primes_upto(z)
    weights: dict[int, float] = {}
    logR = math.log(R)
    for d, mu in squarefree_products(primes, R):
        weights[d] = mu * max(0.0, math.log(R / d) / logR)
    return R, weights, primes


def compose_omega(weights: dict[int, float]) -> dict[int, float]:
    """由 lambda_d 合成 omega_l=sum_{[d1,d2]=l} lambda_d1 lambda_d2。"""
    omega: dict[int, float] = defaultdict(float)
    items = list(weights.items())
    for d1, w1 in items:
        for d2, w2 in items:
            omega[lcm(d1, d2)] += w1 * w2
    return dict(omega)


def expi(x: float) -> complex:
    return complex(math.cos(TAU * x), math.sin(TAU * x))


def kernel_integrals(theta: float, eps: float, quad_n: int) -> tuple[complex, complex]:
    """计算 F(theta) 与线性化核 G(theta)=int e(theta/t)/t dt。"""
    F = 0j
    G = 0j
    step = 1.0 / quad_n
    for i in range(quad_n):
        t = 1.0 + (i + 0.5) * step
        phase = expi(theta / t)
        F += phase * (1.0 - expi(theta * eps / t)) * step
        G += phase * (1.0 / t) * step
    return F, G


def analyze_case(P: int, beta: float, m_exp: float, R_exp: float, K: int, L_power: float, quad_n: int) -> dict:
    X = int(beta * P * P)
    H = P
    M = max(1, int(P**m_exp))
    Pm = X / M
    eps = H / X
    L = max(2.0, math.log(P) ** L_power)
    R, weights, _ = selberg_model_weights(P, R_exp)
    omega = compose_omega(weights)

    exact = 0j
    linear = 0j
    exact_env = 0.0
    linear_env = 0.0
    h_contrib: dict[int, complex] = defaultdict(complex)
    ell_scale_mass: dict[str, float] = defaultdict(float)
    theta_bins: dict[str, dict[str, float]] = defaultdict(lambda: {"mass": 0.0, "signed_real": 0.0, "signed_imag": 0.0})
    term_count = 0
    for h in range(1, K + 1):
        low = h * Pm / L
        high = h * Pm * L
        for ell, weight in omega.items():
            if not (low < ell < high):
                continue
            theta = h * Pm / ell
            F, G = kernel_integrals(theta, eps, quad_n)
            exact_term = (weight / h) * M * F
            linear_term = weight * H / ell * (-1j * TAU) * G
            exact += exact_term
            linear += linear_term
            exact_env += abs(weight / h) * M * abs(F)
            linear_env += abs(weight) * H / ell * TAU * abs(G)
            h_contrib[h] += exact_term
            if ell <= R:
                ell_scale_mass["ell<=R"] += abs(weight) / ell
            elif ell <= R * R:
                ell_scale_mass["R<ell<=R2"] += abs(weight) / ell
            else:
                ell_scale_mass["ell>R2"] += abs(weight) / ell
            if theta < 2:
                bucket = "theta<2"
            elif theta < 10:
                bucket = "2<=theta<10"
            elif theta < 50:
                bucket = "10<=theta<50"
            else:
                bucket = "theta>=50"
            theta_bins[bucket]["mass"] += abs(weight) / ell
            theta_bins[bucket]["signed_real"] += linear_term.real
            theta_bins[bucket]["signed_imag"] += linear_term.imag
            term_count += 1

    h_rows = sorted(
        [
            {"h": h, "abs_contrib": abs(value), "real": value.real, "imag": value.imag}
            for h, value in h_contrib.items()
        ],
        key=lambda r: r["abs_contrib"],
        reverse=True,
    )[:8]
    theta_rows = [
        {
            "bucket": bucket,
            "mass": data["mass"],
            "signed_abs": abs(complex(data["signed_real"], data["signed_imag"])),
        }
        for bucket, data in sorted(theta_bins.items())
    ]
    return {
        "P": P,
        "beta": beta,
        "X": X,
        "H": H,
        "M_exp": m_exp,
        "M": M,
        "P_m": Pm,
        "R_exp": R_exp,
        "R": R,
        "K": K,
        "L": L,
        "quad_n": quad_n,
        "term_count": term_count,
        "exact_abs": abs(exact),
        "linear_abs": abs(linear),
        "exact_env": exact_env,
        "linear_env": linear_env,
        "exact_ratio": abs(exact) / exact_env if exact_env else 0.0,
        "linear_ratio": abs(linear) / linear_env if linear_env else 0.0,
        "linear_error_ratio": abs(exact - linear) / exact_env if exact_env else 0.0,
        "h_top": h_rows,
        "ell_scale_mass": dict(ell_scale_mass),
        "theta_bins": theta_rows,
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# SKT 平滑 Selberg 变换扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本实验只检查 `SKT` 的平滑部分。核心比较为",
        "",
        "\\[",
        "M\\sum_{h,\\ell}\\frac{\\omega_\\ell}{h}F(hP_m/\\ell)",
        "\\quad\\text{与}\\quad",
        "-2\\pi iH\\sum_{h,\\ell}\\frac{\\omega_\\ell}{\\ell}G(hP_m/\\ell).",
        "\\]",
        "",
        "若 `linear_error_ratio` 小，则可以把 `SKT` 严格化为一维核 `G` 的 Selberg 合成权相消问题。",
        "",
        "## 摘要",
    ]
    for case in audit["cases"]:
        lines.append(
            f"- P={case['P']} M=P^{case['M_exp']} R=P^{case['R_exp']} terms={case['term_count']} "
            f"exact/env={case['exact_ratio']:.3f} linear/env={case['linear_ratio']:.3f} "
            f"linearErr/env={case['linear_error_ratio']:.3g} topH="
            + ",".join(f"h{row['h']}:{row['abs_contrib']:.2g}" for row in case["h_top"][:3])
        )
    lines += [
        "",
        "## 证明含义",
        "",
        "- 线性化误差小：临界带振幅因子的一阶展开可作为正式证明入口。",
        "- `linear/env` 小：主要相消已经发生在 Selberg 合成权与一维核 `G` 的卷积中。",
        "- 若某些 `h` 独大，应进一步对固定 `h` 的 `ell`-和证明相消；若多个 `h` 抵消，则需要保留 `h`-平均。",
        "",
        "## 下一步接口",
        "",
        "将 `SKT` 拆为：",
        "",
        "```text",
        "SKT-LIN: 振幅一阶展开误差可吸收；",
        "SKT-TRANS: sum omega_l/l * G(hP_m/l) 的临界变换相消。",
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
    parser.add_argument("--quad-n", type=int, default=500)
    args = parser.parse_args()

    cases = [
        analyze_case(P, args.beta, m_exp, R_exp, args.K, args.L_power, args.quad_n)
        for P, m_exp, R_exp in itertools.product(
            parse_ints(args.P_list),
            parse_floats(args.m_exponents),
            parse_floats(args.R_exponents),
        )
    ]
    audit = {
        "certificate_type": "skt_smooth_transform_scan",
        "status": "smooth_transform_scan_not_a_proof",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "beta": args.beta,
            "m_exponents": parse_floats(args.m_exponents),
            "R_exponents": parse_floats(args.R_exponents),
            "K": args.K,
            "L_power": args.L_power,
            "quad_n": args.quad_n,
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "skt-smooth-transform-scan.json"
    md_path = OUT / "skt-smooth-transform-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
