#!/usr/bin/env python3
"""输出指定 P,c 的 residue 链明细。"""
import argparse, math, importlib.util
from pathlib import Path
from collections import Counter

spec = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def collect_points(P, c, C, primes):
    K = int(C * math.log(P) ** 2)
    small = [p for p in primes if p <= K]
    R = []
    B = []
    Pi = []
    for t in range(K + 1):
        n = c + t * P
        if n >= 2 and all(n % p for p in small):
            R.append(t)
            if vb.is_prime_mr(n):
                Pi.append(t)
    max_q = math.isqrt(c + K * P) + 1
    for q in primes:
        if q <= K:
            continue
        if q > max_q:
            break
        h = (c * pow(q, -1, P)) % P or P
        num = q * h - c
        if num % P:
            continue
        a = num // P
        if 0 <= a <= K and h >= q and vb.rough_ge(h, q, primes):
            B.append(a)
    return K, R, B, Pi


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--P", type=int, required=True)
    ap.add_argument("--c", type=int, required=True)
    ap.add_argument("--C", type=float, default=8.0)
    ap.add_argument("--delta", type=int, default=15)
    args = ap.parse_args()

    K_est = int(args.C * math.log(args.P) ** 2)
    max_needed = math.isqrt(args.c + K_est * args.P) + 2000
    primes = vb.primes_upto_from_sieve(vb.sieve(max_needed))
    K, R, B, Pi = collect_points(args.P, args.c, args.C, primes)
    Rc = Counter(a % args.delta for a in R)
    Bc = Counter(a % args.delta for a in B)
    Pc = Counter(a % args.delta for a in Pi)
    residues = sorted(set(Rc) | set(Bc) | set(Pc))
    print(f"P={args.P} c={args.c} K={K} delta={args.delta} R={len(R)} B={len(B)} Pi={len(Pi)}")
    print("r,R,B,Pi,R-B")
    for r in residues:
        print(f"{r},{Rc.get(r,0)},{Bc.get(r,0)},{Pc.get(r,0)},{Rc.get(r,0)-Bc.get(r,0)}")


if __name__ == "__main__":
    main()
