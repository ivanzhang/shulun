#!/usr/bin/env python3
"""单点合数洞的专属大因子剖析。

当共享图匹配化/无边时，合数洞通常由一个专属大素数补掉。
本脚本统计这些专属大因子的大小、互异性、cofactor、乘积对数压力等。

用法示例：
  python3 experiments/singleton_patch_factor_profile.py --P 1009 --a 720 --ys 101,173,293 --detail
  python3 experiments/singleton_patch_factor_profile.py --P 2003 --a 1019 --ys 173,293,503 --detail
"""
import argparse
import math
from collections import Counter
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for, factor_by_primes


def bucket_ratio(P, q):
    ratio = q / P
    if ratio < 0.1:
        return "<0.1P"
    if ratio < 0.2:
        return "0.1-0.2P"
    if ratio < 0.3:
        return "0.2-0.3P"
    if ratio < 0.5:
        return "0.3-0.5P"
    return ">=0.5P"


def analyze(P, a, y, flags, root_primes, detail=False):
    rec = record_for(P, a, y, flags, root_primes)
    singleton = []
    multi = []
    all_comp = []
    for r, qs in rec["patch_factors_by_r"].items():
        if not qs:
            continue
        n = a + r * P
        fac = factor_by_primes(n, root_primes)
        big_qs = [q for q in fac if y < q < P]
        item = (r, n, big_qs, fac)
        all_comp.append(item)
        if len(big_qs) == 1:
            singleton.append(item)
        else:
            multi.append(item)

    qs = [item[2][0] for item in singleton]
    distinct_qs = len(set(qs))
    q_hist = Counter(bucket_ratio(P, q) for q in qs)
    cofactor_hist = Counter()
    log_product_q = sum(math.log(q) for q in qs) if qs else 0.0
    log_product_n = sum(math.log(item[1]) for item in singleton) if singleton else 0.0
    min_q = min(qs) if qs else None
    max_q = max(qs) if qs else None
    avg_q = sum(qs) / len(qs) if qs else 0

    # cofactor = n / q，记录是否仍含小筛已排除之外的大结构。
    for r, n, big_qs, fac in singleton:
        q = big_qs[0]
        cofactor = n // q
        if cofactor == 1:
            cofactor_hist["prime_n"] += 1
        elif cofactor < P:
            cofactor_hist["cofactor<P"] += 1
        elif cofactor < P * P // q:
            cofactor_hist["cofactor_mid"] += 1
        else:
            cofactor_hist["cofactor_large"] += 1

    print(
        f"P={P} a={a} y={y} H={rec['holes']} prime={rec['prime_holes']} comp={rec['composite_holes']} "
        f"singleton={len(singleton)} multi={len(multi)} distinct_q={distinct_qs} "
        f"q_reuse={len(qs)-distinct_qs} minq={min_q} avgq={avg_q:.1f} maxq={max_q} "
        f"sumlogq={log_product_q:.2f} sumlogn={log_product_n:.2f} ratio={log_product_q/log_product_n if log_product_n else 0:.3f}"
    )
    print("  q_bucket", dict(q_hist), "cofactor", dict(cofactor_hist))
    if detail:
        print("  first_singletons", [(r, q, n // q, n) for r, n, (q,), _ in singleton[:60]])
        print("  multi_examples", [(r, n, big_qs) for r, n, big_qs, _ in multi[:30]])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--a", type=int, default=720)
    parser.add_argument("--ys", default="101,173,293")
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    flags = sieve(args.P * args.P)
    root_primes = primes_from_flags(flags, args.P)
    for y in [int(x) for x in args.ys.split(",") if x.strip()]:
        analyze(args.P, args.a, y, flags, root_primes, args.detail)


if __name__ == "__main__":
    main()
