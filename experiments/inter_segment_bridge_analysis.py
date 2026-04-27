#!/usr/bin/env python3
"""分析 R 段之间的 M 插桥容量。

用法示例：
  python3 experiments/inter_segment_bridge_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/inter_segment_bridge_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
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


def bridge_records(P, c, r, delta, C, primes):
    """生成 R-M-R 插桥记录。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    records = []
    for idx, (label, seg) in enumerate(segs):
        if label != "M":
            continue
        left_is_r = idx > 0 and segs[idx - 1][0] == "R"
        right_is_r = idx + 1 < len(segs) and segs[idx + 1][0] == "R"
        if not (left_is_r and right_is_r):
            continue
        left_r = segs[idx - 1][1]
        right_r = segs[idx + 1][1]
        qs = [item["q"] for item in seg]
        ns = [item["n"] for item in seg]
        records.append({
            "seg_idx": idx,
            "len": len(seg),
            "kind": "singleton" if len(seg) == 1 else "long",
            "left_R_len": len(left_r),
            "right_R_len": len(right_r),
            "left_R_end_n": left_r[-1]["n"],
            "right_R_start_n": right_r[0]["n"],
            "bridge_n_start": ns[0],
            "bridge_n_end": ns[-1],
            "gap_span": right_r[0]["n"] - left_r[-1]["n"],
            "left_gap": ns[0] - left_r[-1]["n"],
            "right_gap": right_r[0]["n"] - ns[-1],
            "q_seq": qs,
            "distinct_q": len(set(qs)),
            "q_min": min(qs),
            "q_max": max(qs),
        })
    pattern = "".join(label + str(len(seg)) for label, seg in segs)
    return L, Y, items, block, segs, records, pattern


def record_for(P, c, r, delta, C, primes):
    """生成插桥容量记录。"""
    L, Y, items, block, segs, records, pattern = bridge_records(P, c, r, delta, C, primes)
    bridge_len_counter = Counter(rec["len"] for rec in records)
    q_counter = Counter(q for rec in records for q in rec["q_seq"])
    gap_counter = Counter((rec["left_gap"], rec["right_gap"]) for rec in records)
    long_records = [rec for rec in records if rec["len"] >= 2]
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
        "internal_bridges": len(records),
        "singleton_bridges": sum(1 for rec in records if rec["len"] == 1),
        "long_bridges": len(long_records),
        "bridge_M_total": sum(rec["len"] for rec in records),
        "long_bridge_M_total": sum(rec["len"] for rec in long_records),
        "bridge_len_counter": bridge_len_counter,
        "distinct_bridge_q": len(q_counter),
        "bridge_q_repeat": sum(count - 1 for count in q_counter.values()),
        "gap_counter": gap_counter,
        "top_bridge_q": q_counter.most_common(10),
        "pattern": pattern,
        "records": records,
    }


def print_record(rec, detail=False):
    """打印插桥容量记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "internal_bridges",
        "singleton_bridges", "long_bridges", "bridge_M_total", "long_bridge_M_total", "distinct_bridge_q", "bridge_q_repeat",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"bridge_len_counter={dict(rec['bridge_len_counter'])}")
        print(f"gap_counter={dict(rec['gap_counter'])}")
        print(f"top_bridge_q={rec['top_bridge_q']}")
        print("bridges=seg,len,kind,leftR,rightR,left_gap,right_gap,gap_span,n_start,n_end,q_seq")
        for row in rec["records"]:
            print(
                f"{row['seg_idx']},{row['len']},{row['kind']},{row['left_R_len']},{row['right_R_len']},"
                f"{row['left_gap']},{row['right_gap']},{row['gap_span']},{row['bridge_n_start']},{row['bridge_n_end']},{row['q_seq']}"
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
        rows.sort(key=lambda rec: (-rec["internal_bridges"], -rec["long_bridges"], -rec["block_len"], rec["P"], rec["c"], rec["r"]))
        print("highest inter-segment bridge records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_internal_bridges={rows[0]['internal_bridges'] if rows else None} max_long_bridges={max((rec['long_bridges'] for rec in rows), default=None)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
