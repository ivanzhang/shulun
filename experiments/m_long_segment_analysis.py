#!/usr/bin/env python3
"""分析 U 合数块中的长 M 段稀疏结构。

用法示例：
  python3 experiments/m_long_segment_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/m_long_segment_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec_seg = importlib.util.spec_from_file_location("segment_boundary_identities", base / "segment_boundary_identities.py")
segmod = importlib.util.module_from_spec(spec_seg)
spec_seg.loader.exec_module(segmod)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def factor_with_lpf(n, q, primes):
    """给出 N=q*h 的协因子粗略信息。"""
    h = n // q
    h_lpf = segmod.lpf(h, primes)
    return h, h_lpf


def segment_positions(segs):
    """给每段标注边界类型。"""
    out = []
    for idx, (label, items) in enumerate(segs):
        left_label = segs[idx - 1][0] if idx > 0 else None
        right_label = segs[idx + 1][0] if idx + 1 < len(segs) else None
        if label == "M":
            if left_label == "R" and right_label == "R":
                kind = "internal"
            elif left_label == "R" or right_label == "R":
                kind = "boundary"
            else:
                kind = "isolated"
        else:
            kind = "R"
        out.append((idx, label, kind, items))
    return out


def m_segment_record(P, delta, primes, idx, kind, items):
    """生成单个 M 段记录。"""
    qs = [item["q"] for item in items]
    ns = [item["n"] for item in items]
    Ns = [item.get("N") for item in items]
    rows = []
    for item in items:
        N = item.get("N")
        if N is None:
            N = None
            h = None
            h_lpf = None
        else:
            h, h_lpf = factor_with_lpf(N, item["q"], primes)
        rows.append({
            "u_idx": item["u_idx"],
            "n": item["n"],
            "q": item["q"],
            "h": h,
            "h_lpf": h_lpf,
        })
    return {
        "seg_idx": idx,
        "kind": kind,
        "len": len(items),
        "u_start": items[0]["u_idx"],
        "u_end": items[-1]["u_idx"],
        "n_start": ns[0],
        "n_end": ns[-1],
        "n_span": ns[-1] - ns[0],
        "distinct_q": len(set(qs)),
        "q_repeat": len(qs) - len(set(qs)),
        "q_min": min(qs),
        "q_max": max(qs),
        "q_seq": qs,
        "n_seq": ns,
        "rows": rows,
    }


def collect_with_N(P, c, r, delta, C, primes):
    """复用原收集逻辑，并补充 N 字段。"""
    L, Y, items = segmod.collect(P, c, r, delta, C, primes)
    A = c + r * P
    step = delta * P
    for item in items:
        item["N"] = A + step * item["n"]
    return L, Y, items


def longest_block(items):
    """最长 U 合数块。"""
    return segmod.longest_block(items)


def record_for(P, c, r, delta, C, primes):
    """生成长 M 段分析记录。"""
    L, Y, items = collect_with_N(P, c, r, delta, C, primes)
    block = longest_block(items)
    segs = segmod.segments(block)
    positioned = segment_positions(segs)
    m_records = [m_segment_record(P, delta, primes, idx, kind, seg) for idx, label, kind, seg in positioned if label == "M"]
    long_m = [rec for rec in m_records if rec["len"] >= 2]
    boundary_m = [rec for rec in m_records if rec["kind"] == "boundary"]
    internal_single = [rec for rec in m_records if rec["kind"] == "internal" and rec["len"] == 1]
    internal_long = [rec for rec in m_records if rec["kind"] == "internal" and rec["len"] >= 2]
    q_counter = Counter(q for rec in m_records for q in rec["q_seq"])
    q_to_m_positions = defaultdict(list)
    for rec in m_records:
        for n, q in zip(rec["n_seq"], rec["q_seq"]):
            q_to_m_positions[q].append(n)
    repeat_q_gaps = []
    for q, ns in q_to_m_positions.items():
        ns = sorted(ns)
        for a, b in zip(ns, ns[1:]):
            repeat_q_gaps.append((q, b - a))
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
        "R_total": sum(1 for item in block if item["label"] == "R"),
        "M_total": sum(1 for item in block if item["label"] == "M"),
        "M_segments": len(m_records),
        "M_long_segments": len(long_m),
        "M_long_total": sum(rec["len"] for rec in long_m),
        "M_internal_singletons": len(internal_single),
        "M_internal_long_segments": len(internal_long),
        "M_internal_long_total": sum(rec["len"] for rec in internal_long),
        "M_boundary_segments": len(boundary_m),
        "M_boundary_total": sum(rec["len"] for rec in boundary_m),
        "max_M_run": max((rec["len"] for rec in m_records), default=0),
        "distinct_M_q": len(q_counter),
        "M_q_repeat_total": sum(count - 1 for count in q_counter.values()),
        "repeat_q_gaps_bad": [(q, gap) for q, gap in repeat_q_gaps if gap < q],
        "top_M_q": q_counter.most_common(10),
        "pattern": pattern,
        "m_records": m_records,
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
        "M_segments", "M_long_segments", "M_long_total", "M_internal_singletons",
        "M_internal_long_total", "M_boundary_total", "max_M_run", "distinct_M_q", "M_q_repeat_total",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys) + f",repeat_gap_violation={len(rec['repeat_q_gaps_bad'])}")
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"top_M_q={rec['top_M_q']}")
        for mrec in rec["m_records"]:
            mark = "LONG" if mrec["len"] >= 2 else "single"
            print(
                f"Mseg#{mrec['seg_idx']} {mark} kind={mrec['kind']} len={mrec['len']} "
                f"u={mrec['u_start']}..{mrec['u_end']} n={mrec['n_start']}..{mrec['n_end']} "
                f"distinct_q={mrec['distinct_q']} q_seq={mrec['q_seq']} n_seq={mrec['n_seq']}"
            )
            if mrec["len"] >= 2:
                print("  rows=u_idx,n,q,h,h_lpf")
                for row in mrec["rows"]:
                    print(f"  {row['u_idx']},{row['n']},{row['q']},{row['h']},{row['h_lpf']}")


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
    primes = segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for r in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, r, args.delta, args.C, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))
    if args.scan:
        rows.sort(key=lambda rec: (-rec["M_long_total"], -rec["block_len"], rec["P"], rec["c"], rec["r"]))
        print("worst long-M records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_M_long_total={rows[0]['M_long_total'] if rows else 0}")
        print(f"repeat_gap_violations={sum(len(rec['repeat_q_gaps_bad']) for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
