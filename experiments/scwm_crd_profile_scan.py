#!/usr/bin/env python3
"""signed-CWM/CRD 临界带剖面扫描。

用法示例：
  python3 experiments/scwm_crd_profile_scan.py --P-list 2003,5003
  python3 experiments/scwm_crd_profile_scan.py --P-list 10007 --sample-ms 50000
"""
from __future__ import annotations

import argparse
import cmath
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


def rough_values(M: int, small_primes: list[int], sample_cap: int) -> tuple[list[int], int, int]:
    """枚举或抽样 dyadic 块 [M,2M) 中的 Y-rough m。"""
    rough: list[int] = []
    for m in range(max(1, M), max(1, 2 * M)):
        ok = True
        for q in small_primes:
            if m % q == 0:
                ok = False
                break
        if ok:
            rough.append(m)
    full_count = len(rough)
    if sample_cap > 0 and full_count > sample_cap:
        step = full_count / sample_cap
        rough = [rough[int(i * step)] for i in range(sample_cap)]
    return rough, full_count, len(rough)


def expi(x: float) -> complex:
    return complex(math.cos(TAU * x), math.sin(TAU * x))


def rse_sum(X: int, H: int, h: int, ell: int, ms: list[int]) -> complex:
    """计算实际 RSE 核。"""
    total = 0j
    for m in ms:
        total += expi(h * X / (ell * m)) * (1.0 - expi(h * H / (ell * m)))
    return total


def factor_distinct(n: int, primes: list[int]) -> list[int]:
    """用给定素数表分解 n 的不同素因子。"""
    out: list[int] = []
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
    if x > 1:
        out.append(x)
    return out


def analyze_case(
    P: int,
    alpha: float,
    beta: float,
    m_exp: float,
    R_exp: float,
    K: int,
    L_power: float,
    sample_ms: int,
) -> dict:
    Y = max(2, int(P**alpha))
    X = int(beta * P * P)
    H = P
    M = max(1, int(P**m_exp))
    Pm = X / M
    L = max(2.0, math.log(P) ** L_power)
    rough_primes = primes_upto(Y)
    ms, full_rough_count, sample_count = rough_values(M, rough_primes, sample_ms)
    sample_scale = full_rough_count / sample_count if sample_count else 0.0
    R, lambdas, selberg_primes = selberg_model_weights(P, R_exp)
    omega = compose_omega(lambdas)

    weighted_complex = 0j
    abs_envelope = 0.0
    signed_mass = 0.0
    abs_mass = 0.0
    positive_mass = 0.0
    negative_mass = 0.0
    term_count = 0
    top_terms: list[dict] = []
    prime_abs_share: dict[int, float] = defaultdict(float)
    support_size_mass: dict[int, float] = defaultdict(float)

    for h in range(1, K + 1):
        low = h * Pm / L
        high = h * Pm * L
        for ell, weight in omega.items():
            if not (low < ell < high):
                continue
            mass = weight / ell
            abs_mass_term = abs(weight) / ell
            signed_mass += mass
            abs_mass += abs_mass_term
            if weight >= 0:
                positive_mass += abs_mass_term
            else:
                negative_mass += abs_mass_term
            factors = factor_distinct(ell, selberg_primes)
            support_size_mass[len(factors)] += abs_mass_term
            for p in factors:
                prime_abs_share[p] += abs_mass_term

            kernel = rse_sum(X, H, h, ell, ms)
            if sample_scale:
                kernel *= sample_scale
            contribution = weight * kernel / h
            weighted_complex += contribution
            abs_envelope += abs(weight) * abs(kernel) / h
            term_count += 1
            top_terms.append(
                {
                    "h": h,
                    "ell": ell,
                    "weight": weight,
                    "mass": mass,
                    "theta": h * Pm / ell,
                    "kernel_abs": abs(kernel),
                    "contribution_abs": abs(contribution),
                    "support_size": len(factors),
                    "factors": factors[:8],
                }
            )

    top_terms = sorted(top_terms, key=lambda r: r["contribution_abs"], reverse=True)[:12]
    top_prime_share = sorted(
        [{"prime": p, "abs_mass": v, "share": v / abs_mass if abs_mass else 0.0} for p, v in prime_abs_share.items()],
        key=lambda r: r["abs_mass"],
        reverse=True,
    )[:12]
    support_profile = [
        {"support_size": k, "abs_mass": v, "share": v / abs_mass if abs_mass else 0.0}
        for k, v in sorted(support_size_mass.items())
    ]
    return {
        "P": P,
        "alpha": alpha,
        "Y": Y,
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
        "lambda_count": len(lambdas),
        "omega_count": len(omega),
        "rough_count_full": full_rough_count,
        "rough_count_sample": sample_count,
        "sample_scale": sample_scale,
        "term_count": term_count,
        "critical_abs_mass": abs_mass,
        "critical_signed_mass": signed_mass,
        "signed_mass_ratio": abs(signed_mass) / abs_mass if abs_mass else 0.0,
        "positive_mass": positive_mass,
        "negative_mass": negative_mass,
        "pos_neg_balance_ratio": abs(positive_mass - negative_mass) / abs_mass if abs_mass else 0.0,
        "weighted_kernel_abs": abs(weighted_complex),
        "abs_kernel_envelope": abs_envelope,
        "signed_kernel_ratio": abs(weighted_complex) / abs_envelope if abs_envelope else 0.0,
        "weighted_kernel_real": weighted_complex.real,
        "weighted_kernel_imag": weighted_complex.imag,
        "top_terms": top_terms,
        "top_prime_share": top_prime_share,
        "support_profile": support_profile,
    }


def verdict(case: dict) -> str:
    """给出面向证明路线的实验判读。"""
    if case["critical_abs_mass"] == 0:
        return "no-critical-mass"
    if case["signed_kernel_ratio"] < 0.15 and case["signed_mass_ratio"] < 0.20:
        return "signed-CWM-promising"
    if case["top_prime_share"] and case["top_prime_share"][0]["share"] > 0.35:
        return "CRD-prime-concentration"
    return "mixed-needs-signed-CWM-or-CRD"


def render_markdown(audit: dict) -> str:
    lines = [
        "# signed-CWM / CRD 临界带剖面扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本实验同时扫描三件事：",
        "",
        "1. 临界带 Selberg 合成权的 signed/absolute 比例；",
        "2. 真实粗数倒数核加权后的 signed-kernel/absolute-envelope 比例；",
        "3. 临界质量在 `ell` 的小素支撑上的集中程度，用于判断是否转向 CRD。",
        "",
        "实验仍不是证明；它只决定下一步应严攻 `signed-CWM` 还是 `CRD`。",
        "",
        "## 摘要",
    ]
    for case in audit["cases"]:
        top = case["top_prime_share"][0] if case["top_prime_share"] else {"prime": None, "share": 0.0}
        lines.append(
            f"- P={case['P']} M=P^{case['M_exp']} R=P^{case['R_exp']} "
            f"terms={case['term_count']} rough={case['rough_count_full']} sample={case['rough_count_sample']} "
            f"absMass={case['critical_abs_mass']:.4g} signedMassRatio={case['signed_mass_ratio']:.3f} "
            f"signedKernelRatio={case['signed_kernel_ratio']:.3f} "
            f"posNegBal={case['pos_neg_balance_ratio']:.3f} "
            f"topPrime={top['prime']} share={top['share']:.3f} verdict={verdict(case)}"
        )
    lines += [
        "",
        "## 证明路线判读",
        "",
        "- `signedKernelRatio` 小：真实 RSE 核已经在 Selberg 符号权下相消，优先严写 signed-CWM。",
        "- `signedMassRatio` 小但 `signedKernelRatio` 不小：权重本身有相消，但相位核与符号相关，需要 kernel-signed-CWM。",
        "- `topPrime share` 大：临界 lcm 质量集中到少数小素支撑，应转向 CRD 辅助模缺陷。",
        "- 三者混合：需要二分定理，不应单独假设绝对 CWM。",
        "",
        "## 最坏贡献项",
    ]
    for case in audit["cases"]:
        lines.append("")
        lines.append(f"### P={case['P']} M=P^{case['M_exp']} R=P^{case['R_exp']}")
        for term in case["top_terms"][:5]:
            lines.append(
                f"- h={term['h']} ell={term['ell']} theta={term['theta']:.3f} "
                f"w={term['weight']:.3g} |K|={term['kernel_abs']:.3g} "
                f"|contrib|={term['contribution_abs']:.3g} supp={term['support_size']} factors={term['factors']}"
            )
    lines += [
        "",
        "## 当前硬攻结论",
        "",
        "实验支持把 `RSE-CRIT` 写成更精确的核版本二分：",
        "",
        "```text",
        "kernel-signed-CWM 成立",
        "=> 临界 RSE 加权和直接可吸收；",
        "",
        "kernel-signed-CWM 失败",
        "=> 权重符号与倒数相位核同向相关",
        "=> 临界 lcm 支撑在小素/短差值方向集中",
        "=> CRD。",
        "```",
        "",
        "下一步正式证明应避免只估计 `sum |omega_l|/l`，而应保留 Selberg 符号与实际 RSE 核。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003")
    parser.add_argument("--alpha", type=float, default=0.45)
    parser.add_argument("--beta", type=float, default=0.73)
    parser.add_argument("--m-exponents", default="1.0,1.2,1.4")
    parser.add_argument("--R-exponents", default="0.25,0.30,0.35")
    parser.add_argument("--K", type=int, default=12)
    parser.add_argument("--L-power", type=float, default=2.0)
    parser.add_argument("--sample-ms", type=int, default=50000)
    args = parser.parse_args()

    cases = [
        analyze_case(P, args.alpha, args.beta, m_exp, R_exp, args.K, args.L_power, args.sample_ms)
        for P, m_exp, R_exp in itertools.product(
            parse_ints(args.P_list),
            parse_floats(args.m_exponents),
            parse_floats(args.R_exponents),
        )
    ]
    audit = {
        "certificate_type": "scwm_crd_profile_scan",
        "status": "experimental_route_selection_not_a_proof",
        "parameters": {
            "P_list": parse_ints(args.P_list),
            "alpha": args.alpha,
            "beta": args.beta,
            "m_exponents": parse_floats(args.m_exponents),
            "R_exponents": parse_floats(args.R_exponents),
            "K": args.K,
            "L_power": args.L_power,
            "sample_ms": args.sample_ms,
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "scwm-crd-profile-scan.json"
    md_path = OUT / "scwm-crd-profile-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
