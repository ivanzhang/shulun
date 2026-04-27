#!/usr/bin/env python3
"""验证 L-粗合数点的互质刚性与因子需求。

用法示例：
  python3 experiments/rough_coprime_demand.py --P 3000017 --c 458685 --r 8 --C 8
  python3 experiments/rough_coprime_demand.py --scan --primes 1000003,3000017 --cols 80 --C 8

核心事实：
  若 N_i=A+30Pi, N_j=A+30Pj 且 |i-j|<L，任何公共因子 d 都整除 30P(i-j)。
  在允许链中 gcd(N_i,30P)=1，所以 d | (i-j)。
  若两个数都是 L-粗，则公共因子 d 要么 1，要么 >L；但 d | |i-j| < L，故 d=1。
"""
import argparse
import importlib.util
import math
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec_vb = importlib.util.spec_from_file_location("verify_buchstab", base / "verify_buchstab.py")
vb = importlib.util.module_from_spec(spec_vb)
spec_vb.loader.exec_module(vb)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def build_primes(Ps, C, delta):
    """生成素数表。"""
    max_P = max(Ps)
    max_L = int(C * math.log(max_P) ** 2 / delta) + 10
    max_N = max_P + delta * max_P * max_L + delta * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))


def lpf(n, primes):
    """返回最小素因子。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def factor_distinct(n, primes):
    """返回 n 的不同素因子集合。"""
    factors = set()
    rest = n
    for p in primes:
        if p * p > rest:
            break
        if rest % p == 0:
            factors.add(p)
            while rest % p == 0:
                rest //= p
    if rest > 1:
        factors.add(rest)
    return factors


def record_for(P, c, r, delta, L, primes):
    """计算 L-粗合数互质与因子需求记录。"""
    A = c + r * P
    step = delta * P
    rough_comps = []
    prime_points = []
    all_factors = set()
    min_factor_product_log = 0.0
    max_pair_gcd = 1
    bad_pairs = []

    for n in range(L + 1):
        N = A + step * n
        if N < 2:
            continue
        if vb.is_prime_mr(N):
            prime_points.append(n)
            continue
        least = lpf(N, primes)
        if least > L:
            rough_comps.append((n, N, least))
            factors = factor_distinct(N, primes)
            all_factors.update(factors)
            min_factor_product_log += math.log(least)

    for idx, (n1, N1, _) in enumerate(rough_comps):
        for n2, N2, _ in rough_comps[idx + 1:]:
            gcd_value = math.gcd(N1, N2)
            if gcd_value > max_pair_gcd:
                max_pair_gcd = gcd_value
            if gcd_value != 1:
                bad_pairs.append((n1, n2, gcd_value))
                if len(bad_pairs) >= 5:
                    break
        if bad_pairs:
            break

    # 每个 L-粗合数至少需要一个 >L 的素因子；两两互质时这些素因子不可共享。
    demand_distinct_large = len(rough_comps)
    actual_distinct_factors = len(all_factors)
    interval_log_size = math.log(A + step * L) if A + step * L > 1 else 0
    product_pressure = min_factor_product_log / interval_log_size if interval_log_size else 0
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "rough_comp": len(rough_comps),
        "prime": len(prime_points),
        "first_prime": prime_points[0] if prime_points else None,
        "demand_distinct_large": demand_distinct_large,
        "actual_distinct_factors": actual_distinct_factors,
        "max_pair_gcd": max_pair_gcd,
        "bad_pairs": bad_pairs,
        "product_pressure": product_pressure,
        "sample_rough": [(n, least) for n, _, least in rough_comps[:12]],
    }


def print_record(record, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "rough_comp", "prime", "first_prime",
        "demand_distinct_large", "actual_distinct_factors", "max_pair_gcd", "product_pressure",
    ]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        print(f"bad_pairs={record['bad_pairs']}")
        print(f"sample_rough={record['sample_rough']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--P", type=int, default=0)
    parser.add_argument("--c", type=int, default=0)
    parser.add_argument("--r", type=int, default=0)
    parser.add_argument("--primes", default="1000003,3000017,10000019")
    parser.add_argument("--cols", type=int, default=80)
    parser.add_argument("--C", type=float, default=8.0)
    parser.add_argument("--delta", type=int, default=30)
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c")
    primes = build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        L = int(args.C * math.log(P) ** 2 / args.delta)
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for r in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, r, args.delta, L, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, L, primes))

    if args.scan:
        rows.sort(key=lambda rec: (-rec["rough_comp"], rec["prime"], rec["first_prime"] if rec["first_prime"] is not None else 10**9))
        print("worst rough coprime demand records")
        for record in rows[:30]:
            print_record(record)
        if rows:
            bad = sum(1 for rec in rows if rec["bad_pairs"])
            pressures = sorted(rec["product_pressure"] for rec in rows)
            print(
                "summary "
                f"total={len(rows)} bad_pair_records={bad} "
                f"max_rough={max(rec['rough_comp'] for rec in rows)} "
                f"pressure_q50={pressures[len(pressures)//2]:.3f} pressure_max={pressures[-1]:.3f}"
            )
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
