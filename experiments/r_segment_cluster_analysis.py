#!/usr/bin/env python3
"""分析最长 U 合数块中的 R 段粗簇结构。

用法示例：
  python3 experiments/r_segment_cluster_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/r_segment_cluster_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import math
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


def factor_cofactor(n, q, primes):
    """返回粗点 N=q*h 的协因子与协因子最小素因子。"""
    h = n // q
    return h, mlong.segmod.lpf(h, primes)


def r_segment_records(P, c, r, delta, C, primes):
    """生成 R 段记录。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    records = []
    for idx, (label, seg) in enumerate(segs):
        if label != "R":
            continue
        qs = [item["q"] for item in seg]
        ns = [item["n"] for item in seg]
        gaps = [b - a for a, b in zip(ns, ns[1:])]
        gcd_bad = []
        rows = []
        for item in seg:
            h, h_lpf = factor_cofactor(item["N"], item["q"], primes)
            rows.append({
                "u_idx": item["u_idx"],
                "n": item["n"],
                "N": item["N"],
                "q": item["q"],
                "h": h,
                "h_lpf": h_lpf,
            })
        for a_pos in range(len(rows)):
            for b_pos in range(a_pos + 1, len(rows)):
                g = math.gcd(rows[a_pos]["N"], rows[b_pos]["N"])
                if g != 1:
                    gcd_bad.append((rows[a_pos]["n"], rows[b_pos]["n"], g))
        records.append({
            "seg_idx": idx,
            "len": len(seg),
            "u_start": seg[0]["u_idx"],
            "u_end": seg[-1]["u_idx"],
            "n_start": ns[0],
            "n_end": ns[-1],
            "n_span": ns[-1] - ns[0],
            "gaps": gaps,
            "max_gap": max(gaps, default=0),
            "q_min": min(qs),
            "q_max": max(qs),
            "distinct_q": len(set(qs)),
            "q_repeat": len(qs) - len(set(qs)),
            "gcd_bad": gcd_bad,
            "rows": rows,
        })
    return L, Y, items, block, segs, records


def record_for(P, c, r, delta, C, primes):
    """生成 R 簇统计。"""
    L, Y, items, block, segs, r_records = r_segment_records(P, c, r, delta, C, primes)
    q_counter = Counter(row["q"] for rec in r_records for row in rec["rows"])
    h_lpf_bad = []
    for rec in r_records:
        for row in rec["rows"]:
            if row["h_lpf"] <= L:
                h_lpf_bad.append((row["n"], row["q"], row["h_lpf"]))
    all_gaps = [gap for rec in r_records for gap in rec["gaps"]]
    long_segments = [rec for rec in r_records if rec["len"] >= 3]
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
        "R_total": sum(rec["len"] for rec in r_records),
        "R_segments": len(r_records),
        "max_R_run": max((rec["len"] for rec in r_records), default=0),
        "R_long_segments": len(long_segments),
        "R_long_total": sum(rec["len"] for rec in long_segments),
        "R_q_distinct": len(q_counter),
        "R_q_repeat_total": sum(count - 1 for count in q_counter.values()),
        "R_gcd_bad": sum(len(rec["gcd_bad"]) for rec in r_records),
        "h_lpf_bad": len(h_lpf_bad),
        "gap_counter": Counter(all_gaps),
        "top_R_q": q_counter.most_common(10),
        "pattern": pattern,
        "r_records": r_records,
        "h_lpf_bad_detail": h_lpf_bad[:20],
    }


def print_record(rec, detail=False):
    """打印 R 簇统计。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "R_segments",
        "max_R_run", "R_long_segments", "R_long_total", "R_q_distinct", "R_q_repeat_total", "R_gcd_bad", "h_lpf_bad",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"gap_counter={dict(rec['gap_counter'])}")
        print(f"top_R_q={rec['top_R_q']}")
        for seg in rec["r_records"]:
            print(
                f"Rseg#{seg['seg_idx']} len={seg['len']} u={seg['u_start']}..{seg['u_end']} "
                f"n={seg['n_start']}..{seg['n_end']} span={seg['n_span']} gaps={seg['gaps']} "
                f"q_range={seg['q_min']}..{seg['q_max']} distinct_q={seg['distinct_q']} q_repeat={seg['q_repeat']}"
            )
            print("  rows=u_idx,n,q,h_lpf")
            for row in seg["rows"]:
                print(f"  {row['u_idx']},{row['n']},{row['q']},{row['h_lpf']}")
        if rec["h_lpf_bad_detail"]:
            print(f"h_lpf_bad_detail={rec['h_lpf_bad_detail']}")


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
        rows.sort(key=lambda rec: (-rec["R_total"], -rec["max_R_run"], rec["P"], rec["c"], rec["r"]))
        print("worst R-segment records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_R_total={rows[0]['R_total'] if rows else 0} max_R_run={max((rec['max_R_run'] for rec in rows), default=0)}")
        print(f"total_R_gcd_bad={sum(rec['R_gcd_bad'] for rec in rows)} total_h_lpf_bad={sum(rec['h_lpf_bad'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
