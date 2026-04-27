#!/usr/bin/env python3
"""分析粗补洞的“骨架—单点”容量分裂。

用法示例：
  python3 experiments/skeleton_singleton_capacity.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30
  python3 experiments/skeleton_singleton_capacity.py --scan --primes 1000003,3000017 --cols 80 --C 8

思想：
  在短带 [0,L] 中，q 命中次数 >=2 的补洞素因子形成“周期骨架”；
  命中次数 =1 的 q 是“单点补洞”。反例要求二者合力覆盖全部 U。
"""
import argparse
import importlib.util
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec_vb = importlib.util.spec_from_file_location("verify_buchstab", base / "verify_buchstab.py")
vb = importlib.util.module_from_spec(spec_vb)
spec_vb.loader.exec_module(vb)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def collect_holes(P, c, r, delta, L, Y, primes):
    """返回 U、每个 n 的补洞 q 列表、素数逃逸点。"""
    A = c + r * P
    step = delta * P
    max_N = A + step * L
    small = [p for p in primes if p <= Y and math.gcd(p, step) == 1]
    U = set()
    for n in range(L + 1):
        N = A + step * n
        if N >= 2 and all(N % p for p in small):
            U.add(n)

    holes_by_n = defaultdict(list)
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
                holes_by_n[n].append(q)

    B = set(holes_by_n) & U
    escapes = sorted(n for n in U - B if vb.is_prime_mr(A + step * n))
    return A, step, U, B, holes_by_n, escapes


def capacity_record(P, c, r, delta, L, Y, primes):
    """计算骨架与单点容量指标。"""
    A, step, U, B, holes_by_n, escapes = collect_holes(P, c, r, delta, L, Y, primes)
    q_to_ns = defaultdict(list)
    for n in B:
        for q in holes_by_n[n]:
            q_to_ns[q].append(n)

    skeleton_q = {q for q, ns in q_to_ns.items() if len(set(ns)) >= 2}
    singleton_q = set(q_to_ns) - skeleton_q
    skeleton_points = {n for q in skeleton_q for n in q_to_ns[q]}
    singleton_points = {n for q in singleton_q for n in q_to_ns[q]}
    overlap_points = skeleton_points & singleton_points
    skeleton_only = skeleton_points - singleton_points
    singleton_only = singleton_points - skeleton_points

    small_sieve_density = len(U) / (L + 1) if L >= 0 else 0
    skeleton_bound_sum = sum(L // q + 1 for q in skeleton_q)
    q_reuse = Counter(len(set(ns)) for ns in q_to_ns.values())
    q_top = sorted(((len(set(ns)), q, sorted(set(ns))[:8]) for q, ns in q_to_ns.items()), reverse=True)[:10]

    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(U),
        "B": len(B),
        "escapes": len(escapes),
        "first_escape": escapes[0] if escapes else None,
        "skeleton_q": len(skeleton_q),
        "singleton_q": len(singleton_q),
        "skeleton_points": len(skeleton_points & U),
        "singleton_points": len(singleton_points & U),
        "overlap_points": len(overlap_points & U),
        "skeleton_only": len(skeleton_only & U),
        "singleton_only": len(singleton_only & U),
        "small_sieve_density": small_sieve_density,
        "skeleton_bound_sum": skeleton_bound_sum,
        "q_reuse": dict(sorted(q_reuse.items())),
        "q_top": q_top,
    }


def print_record(record, detail=False):
    """打印容量记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "B", "escapes", "first_escape",
        "skeleton_q", "singleton_q", "skeleton_points", "singleton_points",
        "overlap_points", "skeleton_only", "singleton_only", "skeleton_bound_sum",
    ]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        print(f"small_sieve_density={record['small_sieve_density']:.4f}")
        print(f"q_reuse={record['q_reuse']}")
        print("q_top=count,q,first_ns")
        for item in record["q_top"]:
            print(item)


def prime_list_for(Ps, C, delta):
    """按样本范围生成足够的素数表。"""
    max_P = max(Ps)
    max_L = int(C * math.log(max_P) ** 2 / delta) + 10
    max_N = max_P + delta * max_P * max_L + delta * max_P
    return vb.primes_upto_from_sieve(vb.sieve(math.isqrt(max_N) + 5000))


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

    if args.scan:
        Ps = [int(x) for x in args.primes.split(",") if x.strip()]
    else:
        if not args.P or not args.c:
            raise SystemExit("非扫描模式需要 --P 与 --c")
        Ps = [args.P]
    primes = prime_list_for(Ps, args.C, args.delta)

    records = []
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
                    records.append(capacity_record(P, c, r, args.delta, L, Y, primes))
        else:
            records.append(capacity_record(P, args.c, args.r, args.delta, L, Y, primes))

    if args.scan:
        records.sort(key=lambda item: (item["escapes"], -item["first_escape"] if item["first_escape"] is not None else -10**9, item["U"] - item["B"]))
        print("worst capacity records")
        for record in records[:30]:
            print_record(record)
        if records:
            singleton_ratios = sorted(record["singleton_points"] / max(1, record["B"]) for record in records)
            skeleton_ratios = sorted(record["skeleton_points"] / max(1, record["B"]) for record in records)
            print(
                "summary "
                f"total={len(records)} min_escape={min(r['escapes'] for r in records)} "
                f"max_first_escape={max(r['first_escape'] or -1 for r in records)} "
                f"singleton_ratio_q50={singleton_ratios[len(singleton_ratios)//2]:.3f} "
                f"skeleton_ratio_q50={skeleton_ratios[len(skeleton_ratios)//2]:.3f}"
            )
    else:
        print_record(records[0], detail=True)


if __name__ == "__main__":
    main()
