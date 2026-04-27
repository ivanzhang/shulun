#!/usr/bin/env python3
"""统计端点极大性对应的五点模式 notR-R-M-R-notR。

在 U 幸存序列索引上统计，而不是原始 n 连续索引。

用法示例：
  python3 experiments/five_point_endpoint_pattern.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/five_point_endpoint_pattern.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_m = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec_m)
spec_m.loader.exec_module(mlong)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def collect_u(P, c, r, delta, C, primes):
    """收集 U 序列标签。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    return L, Y, items


def record_for(P, c, r, delta, C, primes):
    """生成五点端点模式统计。"""
    L, Y, items = collect_u(P, c, r, delta, C, primes)
    labels = [item["label"] for item in items]
    rmr_windows = []
    endpoint_windows = []
    endpoint_by_core = Counter()
    rmr_by_core = Counter()
    for i in range(len(labels) - 2):
        if labels[i:i + 3] == ["R", "M", "R"]:
            left_boundary = i == 0 or labels[i - 1] != "R"
            right_boundary = i + 3 == len(labels) or labels[i + 3] != "R"
            core = (items[i + 1]["q"], items[i + 1]["n"] - items[i]["n"], items[i + 2]["n"] - items[i + 1]["n"])
            row = {
                "u_idx": i,
                "n_tuple": (items[i]["n"], items[i + 1]["n"], items[i + 2]["n"]),
                "q_tuple": (items[i]["q"], items[i + 1]["q"], items[i + 2]["q"]),
                "left_boundary": left_boundary,
                "right_boundary": right_boundary,
                "core": core,
            }
            rmr_windows.append(row)
            rmr_by_core[core] += 1
            if left_boundary and right_boundary:
                endpoint_windows.append(row)
                endpoint_by_core[core] += 1
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for x in labels if x == "P"),
        "rmr_adjacent_windows": len(rmr_windows),
        "endpoint_five_windows": len(endpoint_windows),
        "filtered_out": len(rmr_windows) - len(endpoint_windows),
        "endpoint_ratio": len(endpoint_windows) / len(rmr_windows) if rmr_windows else 0.0,
        "distinct_rmr_core": len(rmr_by_core),
        "distinct_endpoint_core": len(endpoint_by_core),
        "rmr_core_repeat": sum(v - 1 for v in rmr_by_core.values()),
        "endpoint_core_repeat": sum(v - 1 for v in endpoint_by_core.values()),
        "top_rmr_core": rmr_by_core.most_common(10),
        "top_endpoint_core": endpoint_by_core.most_common(10),
        "rmr_windows": rmr_windows,
        "endpoint_windows": endpoint_windows,
    }


def print_record(rec, detail=False):
    """打印五点模式统计。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "rmr_adjacent_windows", "endpoint_five_windows",
        "filtered_out", "endpoint_ratio", "distinct_rmr_core", "distinct_endpoint_core", "rmr_core_repeat", "endpoint_core_repeat",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"top_rmr_core={rec['top_rmr_core']}")
        print(f"top_endpoint_core={rec['top_endpoint_core']}")
        print("endpoint_windows=u_idx,n_tuple,q_tuple,core")
        for row in rec["endpoint_windows"]:
            print(f"{row['u_idx']},{row['n_tuple']},{row['q_tuple']},{row['core']}")


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
    primes = mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda rec: (-rec["endpoint_five_windows"], rec["endpoint_ratio"], -rec["rmr_adjacent_windows"], rec["P"], rec["c"], rec["r"]))
        print("highest five-point endpoint records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        ratios = [rec["endpoint_ratio"] for rec in rows if rec["rmr_adjacent_windows"]]
        print(f"checked={len(rows)} max_endpoint_five={rows[0]['endpoint_five_windows'] if rows else None} max_ratio={max(ratios) if ratios else 0:.6f} min_ratio={min(ratios) if ratios else 0:.6f}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
