#!/usr/bin/env python3
"""扫描每条 residue 链的 R-B 缺口。"""
import argparse, math, random, importlib.util
from pathlib import Path
from collections import Counter

spec = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def collect(P, c, C, delta, primes):
    K = int(C * math.log(P) ** 2)
    small = [p for p in primes if p <= K]
    R = []
    B = []
    for t in range(K + 1):
        n = c + t * P
        if n >= 2 and all(n % p for p in small):
            R.append(t)
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
    Rc = Counter(a % delta for a in R)
    Bc = Counter(a % delta for a in B)
    residues = sorted(set(Rc) | set(Bc))
    gaps = [Rc.get(r, 0) - Bc.get(r, 0) for r in residues]
    return {
        "P": P, "c": c, "K": K, "delta": delta,
        "R": len(R), "B": len(B), "gap": len(R)-len(B),
        "chains": len(residues), "min_chain_gap": min(gaps) if gaps else 0,
        "max_chain_gap": max(gaps) if gaps else 0,
        "zero_or_negative": sum(1 for g in gaps if g <= 0),
        "gaps": gaps,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--primes", default="999983,1999993,2999933")
    ap.add_argument("--cols", type=int, default=80)
    ap.add_argument("--C", type=float, default=8.0)
    ap.add_argument("--deltas", default="15,105")
    args = ap.parse_args()
    Ps = [int(x) for x in args.primes.split(",") if x.strip()]
    deltas = [int(x) for x in args.deltas.split(",") if x.strip()]
    max_p = max(Ps)
    max_k = int(args.C * math.log(max_p) ** 2)
    max_needed = math.isqrt(max_p + max_k * max_p) + 2000
    primes = vb.primes_upto_from_sieve(vb.sieve(max_needed))

    rows = []
    for P in Ps:
        random.seed(P)
        base = [1, 2, 6, 30, P//2, P-1]
        cols = list(dict.fromkeys(base + random.sample(range(1, P), min(args.cols, P-1))))
        for c in cols:
            for delta in deltas:
                rows.append(collect(P, c, args.C, delta, primes))

    rows.sort(key=lambda r: (r["min_chain_gap"], -r["zero_or_negative"], r["gap"]))
    print("worst chains: P,c,delta,R,B,gap,chains,min_gap,max_gap,nonpositive,gaps")
    for r in rows[:30]:
        print(f"{r['P']},{r['c']},{r['delta']},{r['R']},{r['B']},{r['gap']},{r['chains']},{r['min_chain_gap']},{r['max_chain_gap']},{r['zero_or_negative']},{r['gaps']}")

    total = len(rows)
    bad = sum(1 for r in rows if r["zero_or_negative"])
    print(f"\nsummary total={total} rows_with_nonpositive_chain={bad}")


if __name__ == "__main__":
    main()
