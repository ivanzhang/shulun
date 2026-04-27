#!/usr/bin/env python3
"""数值验证倒数 Buchstab 短带结构。

用法示例：
  python3 experiments/verify_buchstab.py --max-p 200000 --c-mode first --C 8
  python3 experiments/verify_buchstab.py --primes 99991,199999 --c-mode sample --C 8
"""
import argparse, math, random
from collections import Counter


def sieve(n):
    b = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        b[0] = 0
    if n >= 1:
        b[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if b[i]:
            b[i*i:n+1:i] = b"\x00" * (((n - i*i)//i) + 1)
    return b


def is_prime_mr(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_upto_from_sieve(b):
    return [i for i, v in enumerate(b) if v]


def lpf(n, primes):
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def rough_ge(n, y, primes):
    for p in primes:
        if p >= y or p * p > n:
            break
        if n % p == 0:
            return False
    return True


def primorial_upto_k(K, primes, fraction=1.0):
    """取不超过 fraction*K 的最大奇素数 primorial。"""
    bound = max(1, int(K * fraction))
    delta = 1
    used = []
    for p in primes:
        if p == 2:
            continue
        if delta * p > bound:
            break
        delta *= p
        used.append(p)
    return delta, used


def residue_energy(points, delta):
    """计算点集在 mod delta 上的二阶能量。"""
    counts = Counter(a % delta for a in points)
    total = len(points)
    energy = sum(v * v for v in counts.values())
    occupied = len(counts)
    return counts, total, energy, occupied


def centered_correlation(counts_a, total_a, counts_b, total_b, residues):
    """在给定残基集合上计算中心化相关与范数。"""
    if not residues:
        return 0.0, 0.0, 0.0, 0.0
    avg_a = total_a / len(residues)
    avg_b = total_b / len(residues)
    dot = norm_a = norm_b = 0.0
    for r in residues:
        va = counts_a.get(r, 0) - avg_a
        vb = counts_b.get(r, 0) - avg_b
        dot += va * vb
        norm_a += va * va
        norm_b += vb * vb
    corr = dot / math.sqrt(norm_a * norm_b) if norm_a > 0 and norm_b > 0 else 0.0
    return dot, norm_a, norm_b, corr


def analyze(P, c, C, primes, delta_fraction):
    K = max(2, int(C * math.log(P) ** 2))
    max_n = c + K * P
    small = [p for p in primes if p <= K]
    R = []
    prime_points = []
    comp_points = []
    prime_count = 0
    comp_count = 0
    for t in range(0, K + 1):
        n = c + t * P
        if n >= 2 and all(n % p for p in small):
            R.append(t)
            if is_prime_mr(n):
                prime_count += 1
                prime_points.append(t)
            else:
                comp_count += 1
                comp_points.append(t)

    # 倒数 Buchstab 精确计数
    B = 0
    B_points = []
    bad_examples = []
    blocks = Counter()
    max_q = math.isqrt(max_n) + 1
    for q in primes:
        if q <= K:
            continue
        if q > max_q:
            break
        h = (c * pow(q, -1, P)) % P
        if h == 0:
            h = P
        numerator = q * h - c
        if numerator % P != 0:
            bad_examples.append(("nonint", q, h))
            continue
        a = numerator // P
        if 0 <= a <= K and h >= q and rough_ge(h, q, primes):
            B += 1
            B_points.append(a)
            lo = 1
            while lo * 2 < q:
                lo *= 2
            blocks[lo] += 1

    delta, used_primes = primorial_upto_k(K, primes, delta_fraction)
    R_counts, _, R_energy, R_occupied = residue_energy(R, delta)
    B_counts, _, B_energy, B_occupied = residue_energy(B_points, delta)
    allowed_residues = sorted(set(R_counts) | set(B_counts))
    dot, norm_R, norm_B, corr = centered_correlation(
        R_counts, len(R), B_counts, len(B_points), allowed_residues
    )

    return {
        "P": P,
        "c": c,
        "K": K,
        "R": len(R),
        "prime": prime_count,
        "comp": comp_count,
        "B": B,
        "gap": len(R) - B,
        "K_over_logP": K / math.log(P),
        "R_logK_over_K": len(R) * math.log(K) / K if K else 0,
        "blocks": dict(sorted(blocks.items())),
        "delta": delta,
        "delta_primes": used_primes,
        "R_energy": R_energy,
        "B_energy": B_energy,
        "R_occupied": R_occupied,
        "B_occupied": B_occupied,
        "RB_corr": corr,
        "RB_dot": dot,
        "R_norm": norm_R,
        "B_norm": norm_B,
        "first_prime_t": next((t for t in R if is_prime_mr(c + t * P)), None),
        "bad": bad_examples[:3],
    }


def choose_columns(P, mode):
    if mode == "first":
        return [1]
    if mode == "basic":
        return [1, 2, 6, 30, P // 2, P - 1]
    random.seed(P)
    cols = [1, 2, 6, 30, P // 2, P - 1]
    cols.extend(random.sample(range(1, P), min(5, P - 1)))
    return list(dict.fromkeys(cols))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-p", type=int, default=200000)
    ap.add_argument("--primes", type=str, default="")
    ap.add_argument("--C", type=float, default=8.0)
    ap.add_argument("--delta-fraction", type=float, default=1.0, help="primorial <= fraction*K")
    ap.add_argument("--c-mode", choices=["first", "basic", "sample"], default="basic")
    args = ap.parse_args()

    limit = max(args.max_p, 1000)
    if args.primes:
        selected = [int(x) for x in args.primes.split(",") if x.strip()]
        limit = max(limit, max(selected) + 10)
    b = sieve(limit)
    all_primes = primes_upto_from_sieve(b)
    if args.primes:
        Ps = [P for P in selected if P < len(b) and b[P]]
    else:
        targets = [4999, 9973, 19997, 49999, 99991, 199999]
        Ps = [P for P in targets if P < len(b) and b[P]]

    max_needed = 0
    for P in Ps:
        K = int(args.C * math.log(P) ** 2)
        max_needed = max(max_needed, math.isqrt(P + K * P) + 1000)
    if max_needed >= len(b):
        b2 = sieve(max_needed + 10)
        factor_primes = primes_upto_from_sieve(b2)
    else:
        factor_primes = all_primes

    print("P,c,K,R,prime,comp,B,gap,K/logP,RlogK/K,delta,R_E,B_E,R_occ,B_occ,RB_corr,first_prime_t,blocks")
    for P in Ps:
        for c in choose_columns(P, args.c_mode):
            row = analyze(P, c, args.C, factor_primes, args.delta_fraction)
            print(
                f"{row['P']},{row['c']},{row['K']},{row['R']},{row['prime']},"
                f"{row['comp']},{row['B']},{row['gap']},{row['K_over_logP']:.2f},"
                f"{row['R_logK_over_K']:.3f},{row['delta']},{row['R_energy']},{row['B_energy']},"
                f"{row['R_occupied']},{row['B_occupied']},{row['RB_corr']:.3f},"
                f"{row['first_prime_t']},{row['blocks']}"
            )
            if row["bad"]:
                print("bad_examples", row["bad"])


if __name__ == "__main__":
    main()
