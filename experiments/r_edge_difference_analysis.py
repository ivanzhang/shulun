#!/usr/bin/env python3
"""分析 R 段内部相邻粗点差方程 q2*h2-q1*h1=delta*P*d。

用法示例：
  python3 experiments/r_edge_difference_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/r_edge_difference_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import math
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_r = importlib.util.spec_from_file_location("r_segment_cluster_analysis", base / "r_segment_cluster_analysis.py")
rseg = importlib.util.module_from_spec(spec_r)
spec_r.loader.exec_module(rseg)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def edge_records(P, delta, r_records):
    """把 R 段拆成相邻 R 边。"""
    edges = []
    for rec in r_records:
        rows = rec["rows"]
        for left, right in zip(rows, rows[1:]):
            d = right["n"] - left["n"]
            diff = right["N"] - left["N"]
            rhs = delta * P * d
            g_q_cross_1 = math.gcd(left["q"], right["h"])
            g_q_cross_2 = math.gcd(right["q"], left["h"])
            edges.append({
                "seg_idx": rec["seg_idx"],
                "n1": left["n"],
                "n2": right["n"],
                "d": d,
                "q1": left["q"],
                "q2": right["q"],
                "h1": left["h"],
                "h2": right["h"],
                "h1_lpf": left["h_lpf"],
                "h2_lpf": right["h_lpf"],
                "rhs": rhs,
                "diff_ok": diff == rhs,
                "q_pair": (left["q"], right["q"]),
                "d_key": d,
                "cross_gcd_bad": g_q_cross_1 != 1 or g_q_cross_2 != 1,
                "g_q_cross_1": g_q_cross_1,
                "g_q_cross_2": g_q_cross_2,
                "min_big_factor": min(left["q"], right["q"], left["h_lpf"], right["h_lpf"]),
            })
    return edges


def record_for(P, c, r, delta, C, primes):
    """生成 R 边差方程统计。"""
    base_rec = rseg.record_for(P, c, r, delta, C, primes)
    edges = edge_records(P, delta, base_rec["r_records"])
    q_pair_counter = Counter(edge["q_pair"] for edge in edges)
    d_counter = Counter(edge["d_key"] for edge in edges)
    same_d_q_min = Counter((edge["d"], min(edge["q1"], edge["q2"])) for edge in edges)
    min_big_le_L = [edge for edge in edges if edge["min_big_factor"] <= base_rec["L"]]
    return {
        **{key: base_rec[key] for key in [
            "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "R_segments", "max_R_run", "R_long_total", "pattern"
        ]},
        "R_edge_count": len(edges),
        "distinct_q_pairs": len(q_pair_counter),
        "q_pair_repeat_total": sum(count - 1 for count in q_pair_counter.values()),
        "max_q_pair_reuse": max(q_pair_counter.values(), default=0),
        "d_counter": d_counter,
        "distinct_d": len(d_counter),
        "diff_failures": sum(not edge["diff_ok"] for edge in edges),
        "cross_gcd_bad": sum(edge["cross_gcd_bad"] for edge in edges),
        "min_big_le_L": len(min_big_le_L),
        "top_q_pairs": q_pair_counter.most_common(10),
        "edges": edges,
    }


def print_record(rec, detail=False):
    """打印 R 边差方程统计。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "R_segments", "max_R_run",
        "R_edge_count", "distinct_q_pairs", "q_pair_repeat_total", "max_q_pair_reuse", "distinct_d",
        "diff_failures", "cross_gcd_bad", "min_big_le_L",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"d_counter={dict(rec['d_counter'])}")
        print(f"top_q_pairs={rec['top_q_pairs']}")
        print("edges=seg,n1,n2,d,q1,q2,h1_lpf,h2_lpf,min_big_factor,rhs")
        for edge in rec["edges"]:
            print(
                f"{edge['seg_idx']},{edge['n1']},{edge['n2']},{edge['d']},{edge['q1']},{edge['q2']},"
                f"{edge['h1_lpf']},{edge['h2_lpf']},{edge['min_big_factor']},{edge['rhs']}"
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
        raise SystemExit("非扫描模式需要 --P 与 --c，或使用 --scan")
    primes = rseg.mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda rec: (-rec["R_edge_count"], -rec["max_R_run"], rec["P"], rec["c"], rec["r"]))
        print("worst R-edge records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_R_edge_count={rows[0]['R_edge_count'] if rows else 0}")
        print(f"total_diff_failures={sum(rec['diff_failures'] for rec in rows)} total_cross_gcd_bad={sum(rec['cross_gcd_bad'] for rec in rows)} total_min_big_le_L={sum(rec['min_big_le_L'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
