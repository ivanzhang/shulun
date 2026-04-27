#!/usr/bin/env python3
"""扫描链中粗补洞的前缀饱和与尾端逃逸结构。

用法示例：
  python3 experiments/scan_escape_profile.py --primes 1000003,3000017 --cols 100 --C 8 --delta 30

核心量：
  first_escape：第一个 U-B 点，即第一个素数幸存点。
  prefix_saturation：从 0 开始，U 中所有点都被 B 补住的最长前缀终点。
  escape_count：U-B 的点数。
"""
import argparse
import importlib.util
import math
import random
from pathlib import Path

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", Path(__file__).with_name("scan_ub_gap.py"))
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)

spec_vb = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec_vb)
spec_vb.loader.exec_module(vb)


def collect_sets(P, c, r, delta, L, Y, primes):
    """返回 U、B、Prime 三个集合。"""
    A = c + r * P
    step = delta * P
    max_N = A + step * L
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    U = set()
    for n in range(L + 1):
        N = A + step * n
        if N >= 2 and all(N % p for p in small):
            U.add(n)
    B = set()
    for q in primes:
        if q <= Y:
            continue
        if q > math.isqrt(max_N) + 1:
            break
        if math.gcd(q, step) != 1:
            continue
        residue = (-A * pow(step, -1, q)) % q
        for n in range(residue, L + 1, q):
            N = A + step * n
            h = N // q
            if N % q == 0 and h >= q and vb.rough_ge(h, q, primes):
                B.add(n)
    prime = {n for n in U - B if vb.is_prime_mr(A + step * n)}
    return U, B, prime


def prefix_saturation(U, B, L):
    """计算 U 点被 B 连续补住到哪里。"""
    last = -1
    for n in range(L + 1):
        if n in U:
            if n not in B:
                return last
            last = n
    return L


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", default="1000003,3000017,10000019")
    parser.add_argument("--cols", type=int, default=80)
    parser.add_argument("--C", type=float, default=8.0)
    parser.add_argument("--delta", type=int, default=30)
    parser.add_argument("--Y-mode", choices=["sqrtL", "logP", "fixed"], default="sqrtL")
    parser.add_argument("--Y", type=int, default=0)
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()]
    max_P = max(Ps)
    max_L = int(args.C * math.log(max_P) ** 2 / args.delta) + 10
    max_N = max_P + args.delta * max_P * max_L
    primes = vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))
    rows = []
    for P in Ps:
        random.seed(P)
        cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
        L = int(args.C * math.log(P) ** 2 / args.delta)
        if args.Y_mode == "sqrtL":
            Y = gap.next_prime_ge(math.sqrt(max(2, L)), primes)
        elif args.Y_mode == "logP":
            Y = gap.next_prime_ge(math.log(P), primes)
        else:
            Y = args.Y
        for c in cols:
            for r in gap.allowed_residues(P, c, args.delta):
                U, B, prime = collect_sets(P, c, r, args.delta, L, Y, primes)
                escapes = sorted(U - B)
                first_escape = escapes[0] if escapes else None
                prefix = prefix_saturation(U, B, L)
                rows.append((first_escape if first_escape is not None else L + 1, len(escapes), len(U), len(B), prefix, P, c, r, L, Y, escapes[:10]))

    rows.sort(reverse=True)
    print("worst by first_escape: first_escape,escape_count,U,B,prefix_sat,P,c,r,L,Y,escapes")
    for row in rows[:30]:
        print(row)
    first_values = sorted(row[0] for row in rows)
    escape_counts = sorted(row[1] for row in rows)
    prefix_values = sorted(row[4] for row in rows)
    if rows:
        def q(values, prob):
            return values[min(len(values) - 1, int(prob * len(values)))]
        print(
            "summary "
            f"total={len(rows)} first_q50={q(first_values,.5)} first_q90={q(first_values,.9)} first_max={first_values[-1]} "
            f"esc_min={escape_counts[0]} esc_q50={q(escape_counts,.5)} esc_max={escape_counts[-1]} "
            f"prefix_q90={q(prefix_values,.9)} prefix_max={prefix_values[-1]}"
        )


if __name__ == "__main__":
    main()
