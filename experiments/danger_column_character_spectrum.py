#!/usr/bin/env python3
"""危险列的模 P 字符谱分析。

对函数 f(a)=列 a 中素数个数，计算乘法群上的离散傅里叶谱。
为避免复数 Dirichlet 字符实现，选取原根 g，把 a=g^t 映射到循环群 Z/(P-1)，对 f(g^t) 做 DFT。

用法示例：
  python3 experiments/danger_column_character_spectrum.py --P 1009 --top 12
  python3 experiments/danger_column_character_spectrum.py --Ps 251,503,1009,2003 --top 8
"""
import argparse
import cmath
import math


def sieve(n: int) -> bytearray:
    """返回 n 以内素数标记。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def factor_distinct(n: int) -> list[int]:
    """分解 n 的不同素因子。"""
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def primitive_root_prime(P: int) -> int:
    """寻找素数模 P 的原根。"""
    factors = factor_distinct(P - 1)
    for g in range(2, P):
        if all(pow(g, (P - 1) // q, P) != 1 for q in factors):
            return g
    raise ValueError("no primitive root found")


def column_prime_counts(P: int) -> list[int]:
    """返回 a=1..P-1 的列素数计数。"""
    flags = sieve(P * P)
    counts = [0] * P
    for a in range(1, P):
        counts[a] = sum(1 for r in range(P) if flags[a + r * P])
    return counts


def dft(values: list[float]) -> list[complex]:
    """朴素 DFT，适合 P 几千以内。"""
    n = len(values)
    out = []
    for m in range(n):
        s = 0j
        for t, val in enumerate(values):
            angle = -2 * math.pi * m * t / n
            s += val * complex(math.cos(angle), math.sin(angle))
        out.append(s)
    return out


def analyze(P: int, top: int, detail: bool = False) -> None:
    counts = column_prime_counts(P)
    mean = sum(counts[1:]) / (P - 1)
    min_a = min(range(1, P), key=lambda a: counts[a])
    max_a = max(range(1, P), key=lambda a: counts[a])
    g = primitive_root_prime(P)
    powers = []
    x = 1
    for _ in range(P - 1):
        powers.append(x)
        x = (x * g) % P
    seq = [counts[a] - mean for a in powers]
    coeffs = dft(seq)
    ranked = sorted(range(1, P - 1), key=lambda m: abs(coeffs[m]), reverse=True)[:top]

    # 用前 k 个谱峰重构危险列偏差，观察是否少数角色主导。
    t_of_a = {a: t for t, a in enumerate(powers)}
    t_min = t_of_a[min_a]
    recon = 0j
    contributions = []
    n = P - 1
    for m in ranked:
        term = coeffs[m] * cmath.exp(2j * math.pi * m * t_min / n) / n
        contributions.append((m, abs(coeffs[m]) / n, term.real))
        recon += term

    print(
        f"P={P} g={g} mean={mean:.4f} min_a={min_a} min={counts[min_a]} "
        f"max_a={max_a} max={counts[max_a]} dev_min={counts[min_a]-mean:.4f} "
        f"top{top}_recon_min={recon.real:.4f}"
    )
    print(" top_spectrum", [(m, round(abs(coeffs[m]) / n, 4), round(contrib, 4)) for m, _, contrib in contributions])
    if detail:
        around = sorted(((counts[a], a) for a in range(1, P)))[:20]
        print(" lowest_columns", around)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--Ps", default="")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    Ps = [int(x) for x in args.Ps.split(",") if x.strip()] if args.Ps else [args.P]
    for P in Ps:
        analyze(P, args.top, args.detail)


if __name__ == "__main__":
    main()
