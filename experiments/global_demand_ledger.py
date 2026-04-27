#!/usr/bin/env python3
"""全局局部需求账本。

合并第74、75节：
- R_total：不可复用 R 粗端点需求；
- distinct_M_q：互异 M 中因子需求；
- period_reuse/span：M 中因子周期复用的额外跨度需求；
- window_count：局部 R-M-R 窗口需求；
- compression terms：同端点压缩与链式共享已由局部引理支付。

本脚本寻找稳定的不等式形态，用于和根基模数库容量比较。

用法示例：
  python3 experiments/global_demand_ledger.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/global_demand_ledger.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
mods = {}
for name in [
    "m_long_segment_analysis",
    "window_family_capacity",
    "local_width_capacity",
    "shared_r_vertex_capacity",
]:
    spec = importlib.util.spec_from_file_location(name, base / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mods[name] = mod

gap = mods["m_long_segment_analysis"].gap


def m_q_period_data(block, L):
    """统计最长块内 M 中因子的互异与周期复用。"""
    by_q = defaultdict(list)
    for item in block:
        if item["label"] == "M":
            by_q[item["q"]].append(item["n"])
    period_reuse = 0
    period_span = 0
    defects = []
    for q, ns in by_q.items():
        ns = sorted(ns)
        period_reuse += max(0, len(ns) - 1)
        period_span += (len(ns) - 1) * q
        for a, b in zip(ns, ns[1:]):
            if (b - a) % q != 0:
                defects.append((q, a, b, b - a))
    return {
        "distinct_M_q": len(by_q),
        "M_q_reuse": period_reuse,
        "period_span": period_span,
        "period_span_units": period_span / L if L else 0,
        "period_defects": defects,
        "top_M_q": Counter({q: len(ns) for q, ns in by_q.items()}).most_common(10),
    }


def record_for(P, c, r, delta, C, primes):
    """生成全局需求账本。"""
    L, Y, items = mods["m_long_segment_analysis"].collect_with_N(P, c, r, delta, C, primes)
    block = mods["m_long_segment_analysis"].longest_block(items)
    segs = mods["m_long_segment_analysis"].segmod.segments(block)
    pattern = "".join(label + str(len(seg)) for label, seg in segs)
    R_total = sum(1 for item in block if item["label"] == "R")
    M_total = sum(1 for item in block if item["label"] == "M")
    R_segments = sum(1 for label, _ in segs if label == "R")
    M_segments = sum(1 for label, _ in segs if label == "M")
    mdata = m_q_period_data(block, L)
    wrec = mods["window_family_capacity"].record_for(P, c, r, delta, C, primes)
    lrec = mods["local_width_capacity"].record_for(P, c, r, delta, C, primes)
    srec = mods["shared_r_vertex_capacity"].record_for(P, c, r, delta, C, primes)

    # 中文注释：已闭合的压缩项，作为需求账本的内部支付项。
    local_pair_extra = lrec["total_extra"]
    local_pair_diversity = lrec["total_diversity_extra"]
    chain_share = srec["shared_count"]
    chain_paid = srec["directly_paid"] + srec["thin_cluster_capacity"]

    # 中文注释：几个候选总需求强度，寻找可与根基模数容量比较的稳定下界。
    independent_factor_demand = R_total + mdata["distinct_M_q"]
    adjusted_demand = independent_factor_demand + mdata["M_q_reuse"]
    span_adjusted_demand = independent_factor_demand + mdata["period_span_units"]
    local_structure_need = wrec["window_count"] + local_pair_extra + chain_share
    local_structure_supply = wrec["distinct_r_endpoints"] + local_pair_diversity + chain_paid

    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "R_total": R_total,
        "M_total": M_total,
        "R_segments": R_segments,
        "M_segments": M_segments,
        "distinct_M_q": mdata["distinct_M_q"],
        "M_q_reuse": mdata["M_q_reuse"],
        "period_span": mdata["period_span"],
        "period_span_units": mdata["period_span_units"],
        "period_defects": len(mdata["period_defects"]),
        "window_count": wrec["window_count"],
        "distinct_r_endpoints": wrec["distinct_r_endpoints"],
        "local_pair_extra": local_pair_extra,
        "local_pair_diversity": local_pair_diversity,
        "local_pair_balance": local_pair_diversity - local_pair_extra,
        "chain_share": chain_share,
        "chain_paid": chain_paid,
        "chain_balance": chain_paid - chain_share,
        "independent_factor_demand": independent_factor_demand,
        "adjusted_demand": adjusted_demand,
        "span_adjusted_demand": span_adjusted_demand,
        "local_structure_need": local_structure_need,
        "local_structure_supply": local_structure_supply,
        "local_structure_balance": local_structure_supply - local_structure_need,
        "factor_density": independent_factor_demand / max(1, len(block)),
        "prime_gap": len(items) - len(block),
        "pattern": pattern,
        "top_M_q": mdata["top_M_q"],
    }


def print_record(rec, detail=False):
    """打印全局需求账本。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
        "distinct_M_q", "M_q_reuse", "period_span", "window_count", "local_pair_balance",
        "chain_balance", "independent_factor_demand", "adjusted_demand", "local_structure_balance",
        "factor_density", "prime_gap",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"top_M_q={rec['top_M_q']}")
        print(
            "ledger=local_need,supply,pair_extra,pair_diversity,chain_share,chain_paid,distinct_r_endpoints"
        )
        print(
            f"{rec['local_structure_need']},{rec['local_structure_supply']},{rec['local_pair_extra']},"
            f"{rec['local_pair_diversity']},{rec['chain_share']},{rec['chain_paid']},{rec['distinct_r_endpoints']}"
        )


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
        raise SystemExit("需要 --P --c 或 --scan")
    primes = mods["m_long_segment_analysis"].segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda row: (row["local_structure_balance"], row["factor_density"], -row["block_len"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_local_structure_balance", min((row["local_structure_balance"] for row in rows), default=None),
            "min_pair_balance", min((row["local_pair_balance"] for row in rows), default=None),
            "min_chain_balance", min((row["chain_balance"] for row in rows), default=None),
            "min_factor_density", min((row["factor_density"] for row in rows), default=None),
            "max_adjusted_demand", max((row["adjusted_demand"] for row in rows), default=None),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
