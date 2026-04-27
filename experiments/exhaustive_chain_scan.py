#!/usr/bin/env python3
"""完整枚举 P<=X 的所有列 c 与 mod delta 允许链，扫描首个链内素数。"""
import argparse, math, importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def allowed_residues(P, c, delta):
    return [r for r in range(delta) if math.gcd(c + r * P, delta) == 1]


def first_prime(P, c, r, max_n, delta):
    A = c + r * P
    step = delta * P
    for n in range(max_n + 1):
        if vb.is_prime_mr(A + step * n):
            return n
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-p", type=int, default=5000)
    ap.add_argument("--Cmax", type=float, default=32.0)
    ap.add_argument("--min-p", type=int, default=5)
    ap.add_argument("--exclude-c-eq-p", action="store_true", help="排除平凡边界列 c=P")
    ap.add_argument("--delta", type=int, default=15)
    args = ap.parse_args()

    sieve = vb.sieve(args.max_p)
    Ps = [p for p in range(args.min_p, args.max_p + 1) if sieve[p]]
    records = []
    missing = []
    total = 0
    for P in Ps:
        max_n = int(args.Cmax * math.log(P) ** 2 / args.delta) + 10
        for c in range(1, P + 1):
            if args.exclude_c_eq_p and c == P:
                continue
            for r in allowed_residues(P, c, args.delta):
                total += 1
                n = first_prime(P, c, r, max_n, args.delta)
                if n is None:
                    missing.append((P, c, r, max_n))
                    continue
                ratio = args.delta * n / (math.log(P) ** 2)
                records.append((ratio, n, P, c, r))
    records.sort(reverse=True)
    print(f"scanned_primes={len(Ps)} total_chains={total} found={len(records)} missing={len(missing)}")
    print("top C_chain,n,P,c,r")
    for rec in records[:40]:
        print("%.3f,%d,%d,%d,%d" % rec)
    if records:
        vals = sorted(x[0] for x in records)
        def q(prob):
            return vals[min(len(vals)-1, int(prob * len(vals)))]
        print("summary q50=%.3f q90=%.3f q99=%.3f q999=%.3f max=%.3f" % (q(.5), q(.9), q(.99), q(.999), vals[-1]))
    if missing:
        print("missing first", missing[:20])


if __name__ == "__main__":
    main()
