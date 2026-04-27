#!/usr/bin/env python3
"""检验端点约束三元组供需是否足以闭合饱和插桥引理。

用法示例：
  python3 experiments/endpoint_supply_demand.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/endpoint_supply_demand.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import math
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_ep = importlib.util.spec_from_file_location("endpoint_bridge_capacity", base / "endpoint_bridge_capacity.py")
ep = importlib.util.module_from_spec(spec_ep)
spec_ep.loader.exec_module(ep)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def primes_between(primes, lo, hi):
    """返回 (lo,hi] 中素数。"""
    return [p for p in primes if lo < p <= hi]


def record_for(P, c, r, delta, C, primes):
    """生成端点供需记录。"""
    rec = ep.record_for(P, c, r, delta, C, primes)
    mids = primes_between(primes, rec["Y"], rec["L"])
    bridge_q_counter = Counter(p["q"] for p in rec["points"])
    endpoint_shapes = Counter((p["left_dist"], p["right_dist"]) for p in rec["points"])
    # 粗供给：每个中因子 q 在长度 L 内最多 floor(L/q)+1 次。
    q_capacity = {q: rec["L"] // q + 1 for q in mids}
    used_capacity_sum = sum(q_capacity.get(q, 0) for q in bridge_q_counter)
    all_capacity_sum = sum(q_capacity.values())
    demand = rec["bridge_point_count"]
    saturated_need = max(0, rec["R_segments"] - 1)
    distinct_q_used = len(bridge_q_counter)
    return {
        **{key: rec[key] for key in [
            "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "internal_bridges",
            "singleton_bridges", "long_bridges", "bridge_point_count", "distinct_q_endpoint", "q_endpoint_repeat", "pattern"
        ]},
        "mid_prime_count": len(mids),
        "all_mid_capacity": all_capacity_sum,
        "used_q_capacity": used_capacity_sum,
        "bridge_q_distinct": distinct_q_used,
        "bridge_q_repeat": sum(v - 1 for v in bridge_q_counter.values()),
        "saturated_need": saturated_need,
        "demand_minus_distinct_q": demand - distinct_q_used,
        "demand_minus_mid_count": demand - len(mids),
        "demand_minus_all_capacity": demand - all_capacity_sum,
        "saturated_minus_mid_count": saturated_need - len(mids),
        "endpoint_shape_count": len(endpoint_shapes),
        "endpoint_shape_repeat": sum(v - 1 for v in endpoint_shapes.values()),
        "top_bridge_q": bridge_q_counter.most_common(10),
        "mid_primes": mids,
        "points": rec["points"],
    }


def print_record(rec, detail=False):
    """打印端点供需记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "internal_bridges",
        "bridge_point_count", "saturated_need", "mid_prime_count", "all_mid_capacity", "bridge_q_distinct",
        "bridge_q_repeat", "demand_minus_mid_count", "demand_minus_all_capacity", "saturated_minus_mid_count",
        "endpoint_shape_count", "endpoint_shape_repeat",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"mid_primes={rec['mid_primes']}")
        print(f"top_bridge_q={rec['top_bridge_q']}")
        print("points=n,q,left_dist,right_dist")
        for p in rec["points"]:
            print(f"{p['n']},{p['q']},{p['left_dist']},{p['right_dist']}")


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
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()

    Ps = [int(x) for x in args.primes.split(",") if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c):
        raise SystemExit("非扫描模式需要 --P 与 --c，或使用 --scan")
    primes = ep.mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, rr, args.delta, args.C, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))
    if args.scan:
        rows.sort(key=lambda rec: (-rec["demand_minus_mid_count"], -rec["bridge_point_count"], rec["P"], rec["c"], rec["r"]))
        print("tightest endpoint supply-demand records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_demand_minus_mid_count={rows[0]['demand_minus_mid_count'] if rows else None}")
        print(f"positive_demand_over_mid_count={sum(rec['demand_minus_mid_count'] > 0 for rec in rows)} positive_demand_over_all_capacity={sum(rec['demand_minus_all_capacity'] > 0 for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
