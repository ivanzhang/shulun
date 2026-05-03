#!/usr/bin/env python3
"""KSCWM/CRD-SPC 双出口压力扫描。

用法示例：
  python3 experiments/kscwm_crd_dual_obstruction_scan.py --P-list 2003,5003
  python3 experiments/kscwm_crd_dual_obstruction_scan.py --P-list 10007 --sample-ms 4000
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


def rough_values(M: int, small_primes: list[int], sample_cap: int) -> tuple[list[int], int]:
    """枚举或抽样 dyadic 块 [M,2M) 中的 Y-rough m。"""
    values: list[int] = []
    for m in range(max(1, M), max(1, 2 * M)):
        ok = True
        for q in small_primes:
            if m % q == 0:
                ok = False
                break
        if ok:
            values.append(m)
    full_count = len(values)
    if sample_cap > 0 and full_count > sample_cap:
        step = full_count / sample_cap
        values = [values[int(i * step)] for i in range(sample_cap)]
    return values, full_count


def smooth_values(M: int, count: int) -> list[int]:
    """构造均匀 dyadic 网格，用于平滑粗数密度模型。"""
    if count <= 0:
        return []
    step = M / count
    return [max(1, int(M + (i + 0.5) * step)) for i in range(count)]


def expi(x: float) -> complex:
    return complex(math.cos(TAU * x), math.sin(TAU * x))


def term_value(X: int, H: int, h: int, ell: int, m: int) -> complex:
    """单个 m 的 RSE 核。"""
    return expi(h * X / (ell * m)) * (1.0 - expi(h * H / (ell * m)))


def build_critical_terms(Pm: float, L: float, K: int, omega: dict[int, float], primes: list[int]) -> list[dict]:
    """列出临界带项及其支撑。"""
    terms: list[dict] = []
    for h in range(1, K + 1):
        low = h * Pm / L
        high = h * Pm * L
        for ell, weight in omega.items():
            if low < ell < high and weight != 0:
                terms.append(
                    {
                        "h": h,
                        "ell": ell,
                        "weight": weight,
                        "factors": factor_distinct(ell, primes),
                        "theta": h * Pm / ell,
                    }
                )
    return terms


def residue_energy(
    X: int,
    H: int,
    terms: list[dict],
    ms: list[int],
    sample_scale: float,
    support_prime: int,
    aux_prime: int,
) -> dict:
    """计算给定支撑素数和辅助模的有向残基能量。"""
    complex_by_res: dict[int, complex] = defaultdict(complex)
    abs_by_res: dict[int, float] = defaultdict(float)
    total_abs = 0.0
    for term in terms:
        if support_prime not in term["factors"]:
            continue
        h = int(term["h"])
        ell = int(term["ell"])
        weight = float(term["weight"])
        coef = weight / h
        for m in ms:
            c = coef * term_value(X, H, h, ell, m) * sample_scale
            res = m % aux_prime
            complex_by_res[res] += c
            abs_by_res[res] += abs(c)
            total_abs += abs(c)
    nonzero_res = [a for a in range(1, aux_prime)]
    if total_abs == 0:
        return {
            "support_prime": support_prime,
            "aux_prime": aux_prime,
            "total_abs": 0.0,
            "max_abs_over_uniform": 0.0,
            "complex_energy": 0.0,
            "zero_abs_share": 0.0,
        }
    expected = total_abs / max(1, aux_prime - 1)
    max_abs = max((abs_by_res[a] for a in nonzero_res), default=0.0)
    complex_energy = (aux_prime - 1) * sum(abs(complex_by_res[a]) ** 2 for a in nonzero_res) / (total_abs**2)
    return {
        "support_prime": support_prime,
        "aux_prime": aux_prime,
        "total_abs": total_abs,
        "max_abs_over_uniform": max_abs / expected if expected else 0.0,
        "complex_energy": complex_energy,
        "zero_abs_share": abs_by_res[0] / total_abs,
    }


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
    small_primes = primes_upto(Y)
    ms, rough_count = rough_values(M, small_primes, sample_ms)
    sample_scale = rough_count / len(ms) if ms else 0.0
    smooth_ms = smooth_values(M, len(ms))

    R, weights, selberg_primes = selberg_model_weights(P, R_exp)
    omega = compose_omega(weights)
    terms = build_critical_terms(Pm, L, K, omega, selberg_primes)

    actual = 0j
    smooth = 0j
    envelope = 0.0
    prime_abs_share: dict[int, float] = defaultdict(float)
    for term in terms:
        h = int(term["h"])
        ell = int(term["ell"])
        weight = float(term["weight"])
        coef = weight / h
        actual_kernel = sum(term_value(X, H, h, ell, m) for m in ms) * sample_scale
        smooth_kernel = sum(term_value(X, H, h, ell, m) for m in smooth_ms) * sample_scale
        actual += coef * actual_kernel
        smooth += coef * smooth_kernel
        envelope += abs(coef) * abs(actual_kernel)
        abs_mass = abs(weight) / ell
        for p in term["factors"]:
            prime_abs_share[p] += abs_mass

    top_prime_rows = sorted(
        [{"prime": p, "share": v / sum(prime_abs_share.values()) if prime_abs_share else 0.0, "mass": v} for p, v in prime_abs_share.items()],
        key=lambda r: r["mass"],
        reverse=True,
    )[:6]
    top_support_prime = int(top_prime_rows[0]["prime"]) if top_prime_rows else 0
    aux_candidates = [p for p in primes_upto(31) if p != top_support_prime and p <= Y]
    aux_rows = [
        residue_energy(X, H, terms, ms, sample_scale, top_support_prime, r)
        for r in aux_candidates
        if top_support_prime
    ]
    aux_rows = sorted(aux_rows, key=lambda r: r["complex_energy"], reverse=True)[:6]

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
        "term_count": len(terms),
        "rough_count": rough_count,
        "sample_count": len(ms),
        "envelope": envelope,
        "actual_abs": abs(actual),
        "smooth_abs": abs(smooth),
        "rough_discrepancy_abs": abs(actual - smooth),
        "actual_ratio": abs(actual) / envelope if envelope else 0.0,
        "smooth_ratio": abs(smooth) / envelope if envelope else 0.0,
        "rough_discrepancy_ratio": abs(actual - smooth) / envelope if envelope else 0.0,
        "top_prime_share": top_prime_rows,
        "auxiliary_energy": aux_rows,
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# KSCWM / CRD-SPC 双出口压力扫描",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本实验把当前两个硬点拆成两个可审查问题：",
        "",
        "1. `KSCWM` 是否主要来自平滑 dyadic 核上的 Selberg 符号相消；",
        "2. `SPC` 是否能在辅助模上产生可检测的有向能量缺陷。",
        "",
        "## 摘要",
    ]
    for case in audit["cases"]:
        top = case["top_prime_share"][0] if case["top_prime_share"] else {"prime": None, "share": 0.0}
        aux = case["auxiliary_energy"][0] if case["auxiliary_energy"] else {
            "aux_prime": None,
            "complex_energy": 0.0,
            "max_abs_over_uniform": 0.0,
            "zero_abs_share": 0.0,
        }
        lines.append(
            f"- P={case['P']} M=P^{case['M_exp']} R=P^{case['R_exp']} terms={case['term_count']} "
            f"actual/env={case['actual_ratio']:.3f} smooth/env={case['smooth_ratio']:.3f} "
            f"roughDiff/env={case['rough_discrepancy_ratio']:.3f} "
            f"topPrime={top['prime']} share={top['share']:.3f} "
            f"bestAux={aux['aux_prime']} energy={aux['complex_energy']:.3f} "
            f"maxAbs/unif={aux['max_abs_over_uniform']:.2f} zeroShare={aux['zero_abs_share']:.3f}"
        )
    lines += [
        "",
        "## 判读",
        "",
        "- `smooth/env` 小且 `roughDiff/env` 小：`KSCWM` 可先化为平滑 Selberg 变换相消。",
        "- `smooth/env` 小但 `roughDiff/env` 不小：需加入粗数分布误差，即 Buchstab/CRT 均衡输入。",
        "- `topPrime share` 大但辅助能量不大：仅有 lcm 支撑集中还不足以推出 `CRD-SPC`，必须增加“有向相位集中”条件。",
        "- 辅助能量大：可把 `SPC` 转化为辅助模 CRTDefect 或短差值能量超标。",
        "",
        "## 当前严谨修正",
        "",
        "`SPC` 不能单独作为 `CRD-SPC` 的充分条件；它必须升级为 oriented-SPC：临界质量不仅集中在 `q|ell`，还要在某个辅助模或短差值方向上保持同向相位。否则小素支撑集中可能只是 Selberg 权结构，而不一定给出真实 CRT 缺陷。",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="2003,5003,10007")
    parser.add_argument("--alpha", type=float, default=0.45)
    parser.add_argument("--beta", type=float, default=0.73)
    parser.add_argument("--m-exponents", default="1.0,1.2,1.4")
    parser.add_argument("--R-exponents", default="0.30,0.35")
    parser.add_argument("--K", type=int, default=8)
    parser.add_argument("--L-power", type=float, default=2.0)
    parser.add_argument("--sample-ms", type=int, default=6000)
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
        "certificate_type": "kscwm_crd_dual_obstruction_scan",
        "status": "experimental_obstruction_split_not_a_proof",
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
    json_path = OUT / "kscwm-crd-dual-obstruction-scan.json"
    md_path = OUT / "kscwm-crd-dual-obstruction-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
