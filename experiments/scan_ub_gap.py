#!/usr/bin/env python3
"""扫描链级小筛剩余 U 与有效 Buchstab 补洞 B 的供需缺口。

核心参数：delta=30, L=floor(C log^2(P)/delta), Y≈sqrt(L)。
"""
import argparse, math, random, importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("verify_buchstab", Path(__file__).with_name("verify_buchstab.py"))
vb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vb)


def next_prime_ge(x, primes):
    for p in primes:
        if p >= x:
            return p
    return primes[-1]


def compute_ub(P, c, r, delta, L, Y, primes):
    A = c + r * P
    step = delta * P
    max_n = A + step * L
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]

    U = []
    for n in range(L + 1):
        N = A + step * n
        if N < 2:
            continue
        if all(N % p for p in small):
            U.append(n)

    B = []
    max_q = math.isqrt(max_n) + 1
    for q in primes:
        if q <= Y:
            continue
        if q > max_q:
            break
        if math.gcd(q, step) != 1:
            continue
        # 完整补洞：q 在链坐标中覆盖一个模 q 的残基类，
        # 不能只取 h 的最小正代表；必须允许所有平移 n=r_q+kq。
        residue = (-A * pow(step, -1, q)) % q
        for n in range(residue, L + 1, q):
            N = A + step * n
            if N % q:
                continue
            h = N // q
            if h >= q and vb.rough_ge(h, q, primes):
                B.append(n)

    Uset, Bset = set(U), set(B)
    missing_set = Uset - Bset
    prime_missing = sum(1 for n in missing_set if vb.is_prime_mr(A + step * n))
    return len(Uset), len(Bset), len(missing_set), prime_missing, Uset.issubset(Bset)


def allowed_residues(P, c, delta):
    return [r for r in range(delta) if math.gcd(c + r * P, delta) == 1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--primes", default="1000003,3000017,10000019,30000001")
    ap.add_argument("--cols", type=int, default=100)
    ap.add_argument("--C", type=float, default=8.0)
    ap.add_argument("--delta", type=int, default=30)
    ap.add_argument("--Y-mode", choices=["sqrtL", "logP", "fixed"], default="sqrtL")
    ap.add_argument("--Y", type=int, default=0)
    args = ap.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()]
    max_p = max(Ps)
    max_L = int(args.C * math.log(max_p) ** 2 / args.delta) + 5
    max_N = max_p + args.delta * max_p * max_L
    primes = vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))

    rows = []
    for P in Ps:
        random.seed(P)
        cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
        L = int(args.C * math.log(P) ** 2 / args.delta)
        if args.Y_mode == "sqrtL":
            Y = next_prime_ge(math.sqrt(max(2, L)), primes)
        elif args.Y_mode == "logP":
            Y = next_prime_ge(math.log(P), primes)
        else:
            Y = args.Y
        for c in cols:
            for r in allowed_residues(P, c, args.delta):
                u, b, missing, prime_missing, subset = compute_ub(P, c, r, args.delta, L, Y, primes)
                rows.append((u - b, missing, prime_missing, u, b, subset, P, c, r, L, Y))

    rows.sort()
    bad = sum(1 for row in rows if row[0] <= 0)
    subset_true = sum(1 for row in rows if row[5])
    bad_missing = sum(1 for row in rows if row[1] != row[2])
    print(f"total={len(rows)} bad_u_le_b={bad} U_subset_B={subset_true}")
    print(f"missing_not_prime_mismatch={bad_missing}")
    print("worst diff,missing,prime_missing,U,B,subset,P,c,r,L,Y")
    for row in rows[:30]:
        print(row)
    vals = sorted(row[0] for row in rows)
    if vals:
        print("summary min=%d q10=%d q50=%d q90=%d max=%d" % (
            vals[0], vals[int(.1 * len(vals))], vals[len(vals)//2], vals[int(.9 * len(vals))], vals[-1]
        ))


if __name__ == "__main__":
    main()
