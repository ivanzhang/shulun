#!/usr/bin/env python3
"""扫描 mod delta 允许链中的首个素数高度 n。"""
import argparse, math, random, importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def allowed_residues(P, c, delta):
    out = []
    for r in range(delta):
        if math.gcd(c + r * P, delta) == 1:
            out.append(r)
    return out


def first_prime_in_chain(P, c, r, max_n, delta):
    A = c + r * P
    step = delta * P
    for n in range(max_n + 1):
        if vb.is_prime_mr(A + step * n):
            return n
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--primes", default="1000003,3000017,10000019,30000001")
    ap.add_argument("--cols", type=int, default=50)
    ap.add_argument("--Cmax", type=float, default=64.0)
    ap.add_argument("--delta", type=int, default=15)
    args = ap.parse_args()
    Ps = [int(x) for x in args.primes.split(",") if x.strip()]

    records = []
    missing = []
    for P in Ps:
        random.seed(P)
        cols = list(dict.fromkeys([1, 2, 6, 30, P//2, P-1] + random.sample(range(1, P), min(args.cols, P-1))))
        max_n = int(args.Cmax * math.log(P) ** 2 / args.delta) + 5
        for c in cols:
            for r in allowed_residues(P, c, args.delta):
                n = first_prime_in_chain(P, c, r, max_n, args.delta)
                if n is None:
                    missing.append((P, c, r, max_n))
                    continue
                ratio = (args.delta * n) / (math.log(P) ** 2)  # 对应 K=C log^2P 的 C
                records.append((ratio, n, P, c, r))

    records.sort(reverse=True)
    print(f"top first-chain-prime constants: C_chain={args.delta}n/log^2P,n,P,c,r")
    for rec in records[:30]:
        print("%.3f,%d,%d,%d,%d" % rec)
    if records:
        vals = sorted(x[0] for x in records)
        print("\nsummary count=%d missing=%d q50=%.3f q90=%.3f q99=%.3f max=%.3f" % (
            len(records), len(missing), vals[len(vals)//2], vals[int(.9*len(vals))], vals[int(.99*len(vals))-1], vals[-1]
        ))
    if missing:
        print("missing", missing[:10])


if __name__ == "__main__":
    main()
