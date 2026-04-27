#!/usr/bin/env python3
"""扫描短链中的 L-粗合数、素数与低层骨架容量平衡。

用法示例：
  python3 experiments/rough_composite_balance.py --P 3000017 --c 458685 --r 8 --C 8
  python3 experiments/rough_composite_balance.py --scan --primes 1000003,3000017 --cols 80 --C 8

目标：
  验证最终局部硬核：L-粗合数是否可能在扣除低层周期骨架后占满小筛幸存点。
"""
import argparse
import importlib.util
import math
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_vb = importlib.util.spec_from_file_location("verify_buchstab", base / "verify_buchstab.py")
vb = importlib.util.module_from_spec(spec_vb)
spec_vb.loader.exec_module(vb)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def build_primes(Ps, C, delta):
    """生成足够用于试除和 Miller-Rabin 前置筛的素数表。"""
    max_P = max(Ps)
    max_L = int(C * math.log(max_P) ** 2 / delta) + 10
    max_N = max_P + delta * max_P * max_L + delta * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))


def is_rough_above(n, bound, primes):
    """判断 n 是否没有 <=bound 的素因子。"""
    for p in primes:
        if p > bound or p * p > n:
            return True
        if n % p == 0:
            return False
    return True


def least_prime_factor(n, primes):
    """返回最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def record_for(P, c, r, delta, L, Y, primes):
    """计算单条链的粗合数平衡指标。"""
    A = c + r * P
    step = delta * P
    low_primes = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    U = []
    prime_points = []
    rough_comp_points = []
    mid_factor_points = []
    lpf_blocks = Counter()

    for n in range(L + 1):
        N = A + step * n
        if N < 2 or any(N % p == 0 for p in low_primes):
            continue
        U.append(n)
        if vb.is_prime_mr(N):
            prime_points.append(n)
            continue
        lpf = least_prime_factor(N, primes)
        if lpf > L:
            rough_comp_points.append(n)
            lpf_blocks["lpf>L"] += 1
        else:
            mid_factor_points.append(n)
            if lpf <= Y:
                lpf_blocks["lpf<=Y"] += 1
            else:
                lpf_blocks["Y<lpf<=L"] += 1

    low_capacity = sum(L // q + 1 for q in primes if Y < q <= L and math.gcd(q, step) == 1)
    need_after_low = max(0, len(U) - low_capacity)
    rough_margin = len(rough_comp_points) - need_after_low
    prime_margin = len(prime_points)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(U),
        "prime": len(prime_points),
        "rough_comp": len(rough_comp_points),
        "mid_factor": len(mid_factor_points),
        "low_capacity": low_capacity,
        "need_after_low": need_after_low,
        "rough_margin": rough_margin,
        "first_prime": prime_points[0] if prime_points else None,
        "first_rough_comp": rough_comp_points[0] if rough_comp_points else None,
        "lpf_blocks": dict(lpf_blocks),
        "prime_points": prime_points[:12],
        "rough_comp_points": rough_comp_points[:12],
        "mid_factor_points": mid_factor_points[:12],
    }


def print_record(record, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "prime", "rough_comp", "mid_factor",
        "low_capacity", "need_after_low", "rough_margin", "first_prime", "first_rough_comp",
    ]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        print(f"lpf_blocks={record['lpf_blocks']}")
        print(f"prime_points={record['prime_points']}")
        print(f"rough_comp_points={record['rough_comp_points']}")
        print(f"mid_factor_points={record['mid_factor_points']}")


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
    parser.add_argument("--Y-mode", choices=["sqrtL", "logP", "fixed"], default="sqrtL")
    parser.add_argument("--Y", type=int, default=0)
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c")
    primes = build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        L = int(args.C * math.log(P) ** 2 / args.delta)
        if args.Y_mode == "sqrtL":
            Y = gap.next_prime_ge(math.sqrt(max(2, L)), primes)
        elif args.Y_mode == "logP":
            Y = gap.next_prime_ge(math.log(P), primes)
        else:
            Y = args.Y
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for r in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, r, args.delta, L, Y, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, L, Y, primes))

    if args.scan:
        rows.sort(key=lambda rec: (rec["prime"], -rec["rough_margin"], rec["first_prime"] if rec["first_prime"] is not None else 10**9))
        print("worst rough-composite balance records")
        for record in rows[:30]:
            print_record(record)
        if rows:
            rough_margins = sorted(rec["rough_margin"] for rec in rows)
            prime_counts = sorted(rec["prime"] for rec in rows)
            print(
                "summary "
                f"total={len(rows)} min_prime={prime_counts[0]} q50_prime={prime_counts[len(prime_counts)//2]} "
                f"max_rough_margin={rough_margins[-1]} q50_rough_margin={rough_margins[len(rough_margins)//2]} "
                f"bad_rough_margin_nonneg={sum(1 for rec in rows if rec['rough_margin'] >= 0)}"
            )
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
