#!/usr/bin/env python3
"""分析 R-M-R 整体局部构型：左右粗端点 + 中间 M 桥点。

用法示例：
  python3 experiments/rmr_local_configuration.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/rmr_local_configuration.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
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


def rmr_records(P, c, r, delta, C, primes):
    """生成 R-M-R 局部构型记录。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    records = []
    for idx, (label, seg) in enumerate(segs):
        if label != "M":
            continue
        if not (idx > 0 and idx + 1 < len(segs) and segs[idx - 1][0] == "R" and segs[idx + 1][0] == "R"):
            continue
        left = segs[idx - 1][1][-1]
        right = segs[idx + 1][1][0]
        for item in seg:
            records.append({
                "seg_idx": idx,
                "bridge_len": len(seg),
                "left_n": left["n"],
                "mid_n": item["n"],
                "right_n": right["n"],
                "left_q": left["q"],
                "mid_q": item["q"],
                "right_q": right["q"],
                "d_left": item["n"] - left["n"],
                "d_right": right["n"] - item["n"],
                "span": right["n"] - left["n"],
                "shape": (item["n"] - left["n"], right["n"] - item["n"], len(seg)),
                "q_shape": (left["q"], item["q"], right["q"], item["n"] - left["n"], right["n"] - item["n"]),
                "middle_shape": (item["q"], item["n"] - left["n"], right["n"] - item["n"]),
                "coarse_pair": (left["q"], right["q"]),
            })
    pattern = "".join(label + str(len(seg)) for label, seg in segs)
    return L, Y, items, block, segs, records, pattern


def record_for(P, c, r, delta, C, primes):
    """生成 RMR 构型统计。"""
    L, Y, items, block, segs, records, pattern = rmr_records(P, c, r, delta, C, primes)
    q_shape_counter = Counter(rec["q_shape"] for rec in records)
    middle_shape_counter = Counter(rec["middle_shape"] for rec in records)
    coarse_pair_counter = Counter(rec["coarse_pair"] for rec in records)
    shape_counter = Counter(rec["shape"] for rec in records)
    nonunique_middle = sum(v - 1 for v in middle_shape_counter.values())
    nonunique_full = sum(v - 1 for v in q_shape_counter.values())
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "R_segments": sum(1 for label, _ in segs if label == "R"),
        "rmr_count": len(records),
        "distinct_full_q_shapes": len(q_shape_counter),
        "full_q_shape_repeat": nonunique_full,
        "distinct_middle_shapes": len(middle_shape_counter),
        "middle_shape_repeat": nonunique_middle,
        "distinct_coarse_pairs": len(coarse_pair_counter),
        "coarse_pair_repeat": sum(v - 1 for v in coarse_pair_counter.values()),
        "distinct_geometric_shapes": len(shape_counter),
        "geometric_shape_repeat": sum(v - 1 for v in shape_counter.values()),
        "top_middle_shapes": middle_shape_counter.most_common(10),
        "top_shapes": shape_counter.most_common(10),
        "pattern": pattern,
        "records": records,
    }


def print_record(rec, detail=False):
    """打印 RMR 构型统计。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "rmr_count",
        "distinct_full_q_shapes", "full_q_shape_repeat", "distinct_middle_shapes", "middle_shape_repeat",
        "distinct_coarse_pairs", "coarse_pair_repeat", "distinct_geometric_shapes", "geometric_shape_repeat",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"top_middle_shapes={rec['top_middle_shapes']}")
        print(f"top_shapes={rec['top_shapes']}")
        print("rmr=seg,len,left_n,mid_n,right_n,left_q,mid_q,right_q,d_left,d_right,span")
        for row in rec["records"]:
            print(
                f"{row['seg_idx']},{row['bridge_len']},{row['left_n']},{row['mid_n']},{row['right_n']},"
                f"{row['left_q']},{row['mid_q']},{row['right_q']},{row['d_left']},{row['d_right']},{row['span']}"
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
        rows.sort(key=lambda rec: (-rec["rmr_count"], -rec["R_segments"], rec["P"], rec["c"], rec["r"]))
        print("highest RMR local-configuration records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_rmr_count={rows[0]['rmr_count'] if rows else None}")
        print(f"total_full_q_shape_repeat={sum(rec['full_q_shape_repeat'] for rec in rows)} total_middle_shape_repeat={sum(rec['middle_shape_repeat'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
