#!/usr/bin/env python3
"""分析相邻 L-粗合数点的双锚定方程。

用法示例：
  python3 experiments/adjacent_rough_pair_equation.py --P 3000017 --c 458685 --r 8 --C 8
  python3 experiments/adjacent_rough_pair_equation.py --scan --primes 1000003,3000017 --cols 80 --C 8

若 N_i=q_i h_i, N_j=q_j h_j，则：
  q_j h_j - q_i h_i = 30P(j-i)。
该脚本统计相邻粗点的 gap、q/h 尺度与归一化差分。
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
    """构建素数表。"""
    max_P = max(Ps)
    max_L = int(C * math.log(max_P) ** 2 / delta) + 10
    max_N = max_P + delta * max_P * max_L + delta * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))


def min_factor_pair(n, primes):
    """返回最小因子分解。"""
    for p in primes:
        if p * p > n:
            return n, 1
        if n % p == 0:
            return p, n // p
    return n, 1


def rough_items(P, c, r, delta, L, primes):
    """返回 L-粗合数点及其最小因子分解。"""
    A = c + r * P
    step = delta * P
    items = []
    primes_n = []
    for n in range(L + 1):
        N = A + step * n
        q, h = min_factor_pair(N, primes)
        if h == 1:
            primes_n.append(n)
        elif q > L:
            items.append((n, q, h, N))
    return A, step, items, primes_n


def record_for(P, c, r, delta, L, primes):
    """计算相邻粗点方程统计。"""
    A, step, items, primes_n = rough_items(P, c, r, delta, L, primes)
    pair_records = []
    gap_counter = Counter()
    q_order_counter = Counter()
    normalized_errors = []
    for left, right in zip(items, items[1:]):
        n1, q1, h1, N1 = left
        n2, q2, h2, N2 = right
        gap_n = n2 - n1
        lhs = q2 * h2 - q1 * h1
        rhs = step * gap_n
        if lhs != rhs:
            raise AssertionError("双锚定方程失败")
        gap_counter[gap_n] += 1
        q_order_counter["q_up" if q2 > q1 else "q_down_or_equal"] += 1
        # 衡量 q/h 两端变化对巨大差分的贡献方向。
        dq_h = (q2 - q1) * h1
        q_dh = q2 * (h2 - h1)
        normalized_errors.append((abs(dq_h) + abs(q_dh)) / max(1, rhs))
        pair_records.append((n1, n2, gap_n, q1, q2, h1, h2, dq_h, q_dh))
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "rough_comp": len(items),
        "prime": len(primes_n),
        "first_prime": primes_n[0] if primes_n else None,
        "pair_count": len(pair_records),
        "gap_counter": dict(sorted(gap_counter.items())),
        "q_order": dict(q_order_counter),
        "norm_min": min(normalized_errors) if normalized_errors else None,
        "norm_max": max(normalized_errors) if normalized_errors else None,
        "norm_avg": sum(normalized_errors) / len(normalized_errors) if normalized_errors else None,
        "sample_pairs": pair_records[:14],
    }


def print_record(record, detail=False):
    """打印记录。"""
    keys = ["P", "c", "r", "L", "rough_comp", "prime", "first_prime", "pair_count", "norm_min", "norm_avg", "norm_max"]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        print(f"gap_counter={record['gap_counter']}")
        print(f"q_order={record['q_order']}")
        print("sample_pairs=n1,n2,gap,q1,q2,h1,h2,(q2-q1)h1,q2(h2-h1)")
        for item in record["sample_pairs"]:
            print(item)


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
            rows.append(record_for(args.P, args.c, args.r, args.delta, L, primes))

    if args.scan:
        rows.sort(key=lambda rec: (-rec["rough_comp"], rec["prime"], rec["first_prime"] if rec["first_prime"] is not None else 10**9))
        print("worst adjacent rough pair records")
        for record in rows[:30]:
            print_record(record)
        all_gaps = Counter()
        for record in rows:
            all_gaps.update(record["gap_counter"])
        print(f"summary total={len(rows)} top_gaps={all_gaps.most_common(12)}")
    else:
        print_record(rows[0], detail=True)


if __name__ == "__main__":
    main()
