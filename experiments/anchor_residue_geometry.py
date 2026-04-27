#!/usr/bin/env python3
"""分析 L-粗合数最小因子的倒数锚定几何。

用法示例：
  python3 experiments/anchor_residue_geometry.py --P 3000017 --c 458685 --r 8 --C 8
  python3 experiments/anchor_residue_geometry.py --scan --primes 1000003,3000017 --cols 80 --C 8

对 L-粗合数 N_n=q*h，记录最小因子 q 的锚定：
  n = (q*h-A)/(30P), q>L, h>=q, P^-(h)>=q。
并统计 q、h、h/q、相邻锚点间距、倒数残基分布。
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


def factor_min_and_cofactor(n, primes):
    """返回 n 的最小素因子及对应协因子；n 为素数时返回 (n,1)。"""
    for p in primes:
        if p * p > n:
            return n, 1
        if n % p == 0:
            return p, n // p
    return n, 1


def collect_anchor_record(P, c, r, delta, L, primes):
    """收集单条链的倒数锚定数据。"""
    A = c + r * P
    step = delta * P
    anchors = []
    prime_points = []
    for n in range(L + 1):
        N = A + step * n
        if N < 2:
            continue
        q, h = factor_min_and_cofactor(N, primes)
        if h == 1:
            prime_points.append(n)
            continue
        if q > L:
            # q 是最小因子，所以 h 自动 q-粗；记录真实锚定点。
            inv_residue = (-A * pow(step, -1, q)) % q
            anchors.append({
                "n": n,
                "N": N,
                "q": q,
                "h": h,
                "inv_residue": inv_residue,
                "anchor_error": inv_residue - n,
                "h_over_q": h / q,
            })

    ns = [item["n"] for item in anchors]
    q_values = [item["q"] for item in anchors]
    h_ratios = [item["h_over_q"] for item in anchors]
    gaps = [b - a for a, b in zip(ns, ns[1:])]
    q_blocks = Counter(int(math.log2(q)) for q in q_values)
    ratio_blocks = Counter(int(math.log2(max(1.0, ratio))) for ratio in h_ratios)
    residue_blocks = Counter(min(9, int(10 * item["n"] / max(1, L + 1))) for item in anchors)
    anchor_error_nonzero = sum(1 for item in anchors if item["anchor_error"] != 0)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "rough_comp": len(anchors),
        "prime": len(prime_points),
        "first_prime": prime_points[0] if prime_points else None,
        "min_gap": min(gaps) if gaps else None,
        "max_gap": max(gaps) if gaps else None,
        "q_min": min(q_values) if q_values else None,
        "q_max": max(q_values) if q_values else None,
        "ratio_min": min(h_ratios) if h_ratios else None,
        "ratio_max": max(h_ratios) if h_ratios else None,
        "anchor_error_nonzero": anchor_error_nonzero,
        "q_blocks": dict(sorted(q_blocks.items())),
        "ratio_blocks": dict(sorted(ratio_blocks.items())),
        "residue_blocks": dict(sorted(residue_blocks.items())),
        "sample": [(item["n"], item["q"], item["h"], item["inv_residue"], item["anchor_error"]) for item in anchors[:16]],
    }


def print_record(record, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "rough_comp", "prime", "first_prime", "min_gap", "max_gap",
        "q_min", "q_max", "ratio_min", "ratio_max", "anchor_error_nonzero",
    ]
    print(",".join(f"{key}={record[key]}" for key in keys))
    if detail:
        print(f"q_log2_blocks={record['q_blocks']}")
        print(f"ratio_log2_blocks={record['ratio_blocks']}")
        print(f"position_deciles={record['residue_blocks']}")
        print("sample=n,q,h,inv_residue,anchor_error")
        for item in record["sample"]:
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
    records = []
    for P in Ps:
        L = int(args.C * math.log(P) ** 2 / args.delta)
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for r in gap.allowed_residues(P, c, args.delta):
                    records.append(collect_anchor_record(P, c, r, args.delta, L, primes))
        else:
            records.append(collect_anchor_record(args.P, args.c, args.r, args.delta, L, primes))

    if args.scan:
        records.sort(key=lambda rec: (-rec["rough_comp"], rec["prime"], rec["first_prime"] if rec["first_prime"] is not None else 10**9))
        print("worst anchor geometry records")
        for record in records[:30]:
            print_record(record)
        if records:
            nonzero = sum(rec["anchor_error_nonzero"] for rec in records)
            max_rough = max(rec["rough_comp"] for rec in records)
            print(f"summary total={len(records)} max_rough={max_rough} total_anchor_error_nonzero={nonzero}")
    else:
        print_record(records[0], detail=True)


if __name__ == "__main__":
    main()
