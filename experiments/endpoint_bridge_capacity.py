#!/usr/bin/env python3
"""分析给定左右 R 端点时，内部 M 桥的端点约束容量。

用法示例：
  python3 experiments/endpoint_bridge_capacity.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/endpoint_bridge_capacity.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec_bridge = importlib.util.spec_from_file_location("inter_segment_bridge_analysis", base / "inter_segment_bridge_analysis.py")
bridge_mod = importlib.util.module_from_spec(spec_bridge)
spec_bridge.loader.exec_module(bridge_mod)

spec_m = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec_m)
spec_m.loader.exec_module(mlong)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def endpoint_records(P, c, r, delta, C, primes):
    """生成端点约束桥记录。"""
    rec = bridge_mod.record_for(P, c, r, delta, C, primes)
    point_records = []
    for bridge in rec["records"]:
        left_end = bridge["left_R_end_n"]
        right_start = bridge["right_R_start_n"]
        q_seq = bridge["q_seq"]
        if bridge["len"] == 1:
            n_seq = [bridge["bridge_n_start"]]
        else:
            # 桥内 M 点在 n 上不一定连续，用原 collect 重取精确 n 序列。
            n_seq = None
        point_records.append((bridge, n_seq, q_seq))
    # 重建精确桥内 n 序列。
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    out = []
    for idx, (label, seg) in enumerate(segs):
        if label != "M":
            continue
        if not (idx > 0 and idx + 1 < len(segs) and segs[idx - 1][0] == "R" and segs[idx + 1][0] == "R"):
            continue
        left_r = segs[idx - 1][1]
        right_r = segs[idx + 1][1]
        left_end = left_r[-1]["n"]
        right_start = right_r[0]["n"]
        for pos, item in enumerate(seg):
            out.append({
                "seg_idx": idx,
                "bridge_len": len(seg),
                "pos": pos,
                "n": item["n"],
                "q": item["q"],
                "left_end": left_end,
                "right_start": right_start,
                "left_dist": item["n"] - left_end,
                "right_dist": right_start - item["n"],
                "gap_span": right_start - left_end,
                "endpoint_key": (item["n"] - left_end, right_start - item["n"], len(seg)),
                "q_endpoint_key": (item["q"], item["n"] - left_end, right_start - item["n"]),
            })
    return rec, out


def record_for(P, c, r, delta, C, primes):
    """生成端点容量统计。"""
    bridge_rec, points = endpoint_records(P, c, r, delta, C, primes)
    endpoint_counter = Counter(p["endpoint_key"] for p in points)
    q_endpoint_counter = Counter(p["q_endpoint_key"] for p in points)
    q_to_points = defaultdict(list)
    for p in points:
        q_to_points[p["q"]].append(p)
    q_short_reuse_bad = []
    for q, ps in q_to_points.items():
        ns = sorted(p["n"] for p in ps)
        for a, b in zip(ns, ns[1:]):
            if (b - a) % q != 0:
                q_short_reuse_bad.append((q, a, b, b - a))
    return {
        **{key: bridge_rec[key] for key in [
            "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments",
            "internal_bridges", "singleton_bridges", "long_bridges", "bridge_M_total", "long_bridge_M_total", "pattern"
        ]},
        "bridge_point_count": len(points),
        "distinct_endpoint_shapes": len(endpoint_counter),
        "endpoint_shape_repeat": sum(count - 1 for count in endpoint_counter.values()),
        "distinct_q_endpoint": len(q_endpoint_counter),
        "q_endpoint_repeat": sum(count - 1 for count in q_endpoint_counter.values()),
        "q_short_reuse_bad": len(q_short_reuse_bad),
        "endpoint_counter": endpoint_counter,
        "top_q_endpoint": q_endpoint_counter.most_common(10),
        "q_short_reuse_bad_detail": q_short_reuse_bad[:20],
        "points": points,
    }


def print_record(rec, detail=False):
    """打印端点容量统计。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "internal_bridges",
        "singleton_bridges", "long_bridges", "bridge_point_count", "distinct_endpoint_shapes", "endpoint_shape_repeat",
        "distinct_q_endpoint", "q_endpoint_repeat", "q_short_reuse_bad",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"endpoint_counter={dict(rec['endpoint_counter'])}")
        print(f"top_q_endpoint={rec['top_q_endpoint']}")
        print("points=seg,len,pos,n,q,left_dist,right_dist,gap_span")
        for p in rec["points"]:
            print(f"{p['seg_idx']},{p['bridge_len']},{p['pos']},{p['n']},{p['q']},{p['left_dist']},{p['right_dist']},{p['gap_span']}")
        if rec["q_short_reuse_bad_detail"]:
            print(f"q_short_reuse_bad_detail={rec['q_short_reuse_bad_detail']}")


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
        rows.sort(key=lambda rec: (-rec["bridge_point_count"], -rec["internal_bridges"], rec["P"], rec["c"], rec["r"]))
        print("highest endpoint-bridge-capacity records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_bridge_point_count={rows[0]['bridge_point_count'] if rows else None}")
        print(f"total_q_short_reuse_bad={sum(rec['q_short_reuse_bad'] for rec in rows)} total_q_endpoint_repeat={sum(rec['q_endpoint_repeat'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
