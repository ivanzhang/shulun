#!/usr/bin/env python3
"""刚性补洞共享剖面。

统计列 a 的大补丁 q 命中多个小筛洞时，q 的区间分布和命中数分布。

用法示例：
  python3 experiments/rigid_patch_share_profile.py --P 1009 --a 720 --ys 11,17,31,47,71
"""
import argparse
from collections import Counter
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def bucket_q(P, q):
    if q <= P // 16:
        return "<=P/16"
    if q <= P // 8:
        return "P/16..P/8"
    if q <= P // 4:
        return "P/8..P/4"
    if q <= P // 2:
        return "P/4..P/2"
    return ">P/2"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--a", type=int, default=720)
    parser.add_argument("--ys", default="11,17,31,47,71")
    args = parser.parse_args()
    flags = sieve(args.P * args.P)
    root_primes = primes_from_flags(flags, args.P)
    print("P a y H prime comp shared_q shared_edges hit_hist q_bucket_edges q_bucket_qs")
    for y in [int(x) for x in args.ys.split(",") if x.strip()]:
        rec = record_for(args.P, args.a, y, flags, root_primes)
        hit_hist = Counter(len(rows) for rows in rec["shared_qs"].values())
        bucket_edges = Counter()
        bucket_qs = Counter()
        for q, rows in rec["shared_qs"].items():
            bucket_qs[bucket_q(args.P, q)] += 1
            bucket_edges[bucket_q(args.P, q)] += len(rows) * (len(rows) - 1) // 2
        print(
            args.P, args.a, y, rec["holes"], rec["prime_holes"], rec["composite_holes"],
            rec["shared_q"], rec["shared_edges"], sorted(hit_hist.items()),
            dict(bucket_edges), dict(bucket_qs)
        )


if __name__ == "__main__":
    main()
