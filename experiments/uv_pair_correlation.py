#!/usr/bin/env python3
"""比较小筛剩余 U 与大模倒数命中 V 的二点相关。"""
import argparse, math, importlib.util
from pathlib import Path
from collections import Counter

spec = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def pair_counts(points, max_delta):
    s = set(points)
    return {d: sum(1 for x in points if x + d in s) for d in range(1, max_delta + 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--P", type=int, default=1321)
    ap.add_argument("--c", type=int, default=416)
    ap.add_argument("--r", type=int, default=17)
    ap.add_argument("--delta", type=int, default=30)
    ap.add_argument("--L", type=int, default=45)
    ap.add_argument("--Y", type=int, default=45)
    ap.add_argument("--max-delta", type=int, default=30)
    args = ap.parse_args()

    A = args.c + args.r * args.P
    step = args.delta * args.P
    maxN = A + step * args.L
    primes = vb.primes_upto_from_sieve(vb.sieve(math.isqrt(maxN) + 5000))
    small = [p for p in primes if p <= args.Y and math.gcd(p, step) == 1]

    U = []
    for n in range(args.L + 1):
        N = A + step * n
        if all(N % p for p in small):
            U.append(n)

    V = []
    B = []
    maxq = math.isqrt(maxN) + 1
    modulus = step
    for q in primes:
        if q <= args.Y or q > maxq or math.gcd(q, modulus) != 1:
            continue
        h = (A * pow(q, -1, modulus)) % modulus
        if h == 0:
            h = modulus
        num = q * h - A
        if num % modulus:
            continue
        n = num // modulus
        if 0 <= n <= args.L:
            V.append(n)
            if h >= q and vb.rough_ge(h, q, primes):
                B.append(n)
    U = sorted(set(U)); V = sorted(set(V)); B = sorted(set(B))
    DU = pair_counts(U, args.max_delta)
    DV = pair_counts(V, args.max_delta)
    DB = pair_counts(B, args.max_delta)
    print(f"P={args.P} c={args.c} r={args.r} step={step} L={args.L} Y={args.Y}")
    print(f"|U|={len(U)} |V|={len(V)} |B|={len(B)} U_subset_V={set(U).issubset(set(V))} U_subset_B={set(U).issubset(set(B))}")
    print("U", U)
    print("V", V)
    print("B", B)
    print("delta,DU,DV,DB,DU-DV,DU-DB")
    best=[]
    for d in range(1, args.max_delta + 1):
        diff=DU[d]-DV[d]
        diffb=DU[d]-DB[d]
        best.append((diffb,d,DU[d],DB[d]))
        print(f"{d},{DU[d]},{DV[d]},{DB[d]},{diff},{diffb}")
    print("best_DU_minus_DB", sorted(best, reverse=True)[:10])


if __name__ == "__main__":
    main()
