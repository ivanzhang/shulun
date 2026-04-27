#!/usr/bin/env python3
"""段级端点极大性模式 notR-R^a-M^b-R^c-notR。

用法示例：
  python3 experiments/segment_level_endpoint_pattern.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/segment_level_endpoint_pattern.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
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


def record_for(P, c, r, delta, C, primes):
    """生成段级端点模式统计。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    bridges = []
    for idx, (label, seg) in enumerate(segs):
        if label != "M":
            continue
        if not (idx > 0 and idx + 1 < len(segs) and segs[idx - 1][0] == "R" and segs[idx + 1][0] == "R"):
            continue
        left_r = segs[idx - 1][1]
        right_r = segs[idx + 1][1]
        left_external = idx - 2 < 0 or segs[idx - 2][0] != "R"
        right_external = idx + 2 >= len(segs) or segs[idx + 2][0] != "R"
        bridges.append({
            "seg_idx": idx,
            "left_R_len": len(left_r),
            "M_len": len(seg),
            "right_R_len": len(right_r),
            "left_external_not_R": left_external,
            "right_external_not_R": right_external,
            "left_end_n": left_r[-1]["n"],
            "right_start_n": right_r[0]["n"],
            "m_n_seq": [x["n"] for x in seg],
            "m_q_seq": [x["q"] for x in seg],
            "shape": (len(left_r), len(seg), len(right_r)),
        })
    shape_counter = Counter(b["shape"] for b in bridges)
    pattern = "".join(label + str(len(seg)) for label, seg in segs)
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
        "internal_bridges": len(bridges),
        "long_bridges": sum(1 for b in bridges if b["M_len"] >= 2),
        "bridge_points": sum(b["M_len"] for b in bridges),
        "distinct_segment_shapes": len(shape_counter),
        "segment_shape_repeat": sum(v - 1 for v in shape_counter.values()),
        "top_shapes": shape_counter.most_common(10),
        "pattern": pattern,
        "bridges": bridges,
    }


def print_record(rec, detail=False):
    """打印段级模式。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "internal_bridges",
        "long_bridges", "bridge_points", "distinct_segment_shapes", "segment_shape_repeat",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"top_shapes={rec['top_shapes']}")
        print("bridges=seg,leftR,M,rightR,left_ext,right_ext,left_end,right_start,m_n_seq,m_q_seq")
        for b in rec["bridges"]:
            print(
                f"{b['seg_idx']},{b['left_R_len']},{b['M_len']},{b['right_R_len']},"
                f"{b['left_external_not_R']},{b['right_external_not_R']},{b['left_end_n']},{b['right_start_n']},{b['m_n_seq']},{b['m_q_seq']}"
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
        rows.sort(key=lambda rec: (-rec["internal_bridges"], -rec["bridge_points"], rec["P"], rec["c"], rec["r"]))
        print("highest segment-level endpoint records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_internal_bridges={rows[0]['internal_bridges'] if rows else None} max_bridge_points={max((rec['bridge_points'] for rec in rows), default=None)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
