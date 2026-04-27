#!/usr/bin/env python3
"""刚性补洞聚合摘要。

对若干 P,y 扫描所有非零列，输出最危险列的聚合统计。

用法示例：
  python3 experiments/rigid_patch_summary.py --Ps 251,503,1009,2003 --ys 11,17,31,47
"""
import argparse
import math
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def summarize(P, y):
    flags = sieve(P * P)
    root_primes = primes_from_flags(flags, P)
    best_prime = None
    min_holes = None
    max_shared = None
    max_maxhit = None
    total_prime = total_holes = total_shared_edges = 0
    zero_prime = 0
    for a in range(1, P):
        rec = record_for(P, a, y, flags, root_primes)
        total_prime += rec["prime_holes"]
        total_holes += rec["holes"]
        total_shared_edges += rec["shared_edges"]
        zero_prime += rec["prime_holes"] == 0
        if best_prime is None or (rec["prime_holes"], rec["holes"], -rec["shared_edges"]) < (best_prime["prime_holes"], best_prime["holes"], -best_prime["shared_edges"]):
            best_prime = rec
        if min_holes is None or rec["holes"] < min_holes["holes"]:
            min_holes = rec
        if max_shared is None or rec["shared_edges"] > max_shared["shared_edges"]:
            max_shared = rec
        if max_maxhit is None or rec["max_q_hit"] > max_maxhit["max_q_hit"]:
            max_maxhit = rec
    ncols = P - 1
    return {
        "P": P,
        "y": y,
        "avgH": total_holes / ncols,
        "avgPrime": total_prime / ncols,
        "avgSharedEdges": total_shared_edges / ncols,
        "zeroPrimeCols": zero_prime,
        "bestPrime": best_prime,
        "minHoles": min_holes,
        "maxShared": max_shared,
        "maxMaxHit": max_maxhit,
    }


def brief(rec):
    return f"a={rec['a']},H={rec['holes']},prime={rec['prime_holes']},comp={rec['composite_holes']},single={rec['singleton_holes']},sharedEdges={rec['shared_edges']},maxhit={rec['max_q_hit']},cover≈{rec['greedy_cover']}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Ps", default="251,503,1009,2003")
    parser.add_argument("--ys", default="11,17,31,47")
    args = parser.parse_args()
    Ps = [int(x) for x in args.Ps.split(",") if x.strip()]
    ys = [int(x) for x in args.ys.split(",") if x.strip()]
    print("P y avgH avgPrime avgShared zeroPrime bestPrime minHoles maxShared maxMaxHit")
    for P in Ps:
        for y in ys:
            s = summarize(P, y)
            print(
                P, y,
                f"{s['avgH']:.2f}", f"{s['avgPrime']:.2f}", f"{s['avgSharedEdges']:.2f}", s["zeroPrimeCols"],
                "|", brief(s["bestPrime"]),
                "|", brief(s["minHoles"]),
                "|", brief(s["maxShared"]),
                "|", brief(s["maxMaxHit"]),
            )


if __name__ == "__main__":
    main()
