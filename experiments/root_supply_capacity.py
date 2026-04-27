#!/usr/bin/env python3
"""根基模数库供给容量分析。

根基模数库：第一行中的所有素数。对短带 N_n=A+δPn 的最长合数块，统计每个根基素数 q 的命中容量。
这里按前面框架分三层：
- small q<=Y：已被小筛移除，不进入 U 块；
- medium Y<q<=L：可命中 M 点，命中间距至少 q；
- rough q>L：命中 R 点，在长度 L 内不可复用。

用法示例：
  python3 experiments/root_supply_capacity.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/root_supply_capacity.py --scan --primes 1000003,3000017,10000019 --cols 120 --C 8 --delta 30
"""
import argparse
import importlib.util
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

base = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mlong)
gap = mlong.gap
vb = mlong.segmod.vb


def first_row_primes(P, primes):
    """第一行根基素数：2..P 中的素数。"""
    return [p for p in primes if p <= P]


def capacity_for_block(P, c, r, delta, C, primes):
    """计算最长合数块的根基供给容量。"""
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    A = c + r * P
    step = delta * P
    root = first_row_primes(P, primes)
    block_ns = [item["n"] for item in block]
    block_set = set(block_ns)
    hits_by_q = defaultdict(list)
    for q in root:
        if math.gcd(q, step) != 1:
            continue
        residue = (-A * pow(step, -1, q)) % q
        # 中文注释：只统计落在最长合数块内部的命中点。
        for n in range(residue, L + 1, q):
            if n in block_set:
                hits_by_q[q].append(n)
    covered = set(n for ns in hits_by_q.values() for n in ns)
    actual_qs = sorted(hits_by_q)
    medium_qs = [q for q in actual_qs if Y < q <= L]
    rough_qs = [q for q in actual_qs if q > L]
    small_qs = [q for q in actual_qs if q <= Y]
    medium_hits = sum(len(hits_by_q[q]) for q in medium_qs)
    rough_hits = sum(len(hits_by_q[q]) for q in rough_qs)
    small_hits = sum(len(hits_by_q[q]) for q in small_qs)
    # 中文注释：有效容量：medium 按实际命中计；rough 在短带内每 q 最多 1 次。
    effective_supply = medium_hits + len(rough_qs)
    raw_supply = sum(len(ns) for ns in hits_by_q.values())
    overlap_excess = raw_supply - len(covered)
    labels = Counter(item["label"] for item in block)
    lpf_counter = Counter(item["q"] for item in block)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": L,
        "Y": Y,
        "U": len(items),
        "Prime": sum(1 for item in items if item["label"] == "P"),
        "block_len": len(block),
        "R_total": labels["R"],
        "M_total": labels["M"],
        "root_count": len(root),
        "actual_q_count": len(actual_qs),
        "small_q_count": len(small_qs),
        "medium_q_count": len(medium_qs),
        "rough_q_count": len(rough_qs),
        "small_hits": small_hits,
        "medium_hits": medium_hits,
        "rough_hits": rough_hits,
        "raw_supply": raw_supply,
        "effective_supply": effective_supply,
        "covered_points": len(covered),
        "overlap_excess": overlap_excess,
        "supply_minus_block": effective_supply - len(block),
        "covered_minus_block": len(covered) - len(block),
        "pattern": "".join(label + str(len(seg)) for label, seg in mlong.segmod.segments(block)),
        "hits_by_q": hits_by_q,
        "lpf_counter": lpf_counter,
        "block": block,
    }


def print_record(rec, detail=False):
    """打印根基供给容量记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
        "actual_q_count", "medium_q_count", "rough_q_count", "medium_hits", "rough_hits",
        "raw_supply", "effective_supply", "covered_points", "overlap_excess", "supply_minus_block",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"lpf_counter={rec['lpf_counter'].most_common(20)}")
        print("hits=q,count,n_seq")
        for q, ns in sorted(rec["hits_by_q"].items(), key=lambda item: (-len(item[1]), item[0]))[:40]:
            print(f"{q},{len(ns)},{ns}")


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
    primes = mlong.segmod.build_primes(Ps, args.C, args.delta)
    rows = []
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols = list(dict.fromkeys([1, 2, 6, 30, P // 2, P - 1] + random.sample(range(1, P), min(args.cols, P - 1))))
            for c in cols:
                for rr in gap.allowed_residues(P, c, args.delta):
                    rows.append(capacity_for_block(P, c, rr, args.delta, args.C, primes))
        else:
            rows.append(capacity_for_block(P, args.c, args.r, args.delta, args.C, primes))

    if args.scan:
        rows.sort(key=lambda row: (row["supply_minus_block"], -row["block_len"], row["P"], row["c"], row["r"]))
        for rec in rows[:30]:
            print_record(rec)
        print(
            "checked", len(rows),
            "min_supply_minus_block", min((row["supply_minus_block"] for row in rows), default=None),
            "max_supply_minus_block", max((row["supply_minus_block"] for row in rows), default=None),
            "cover_failures", sum(row["covered_points"] != row["block_len"] for row in rows),
        )
    else:
        print_record(rows[0], args.detail)


if __name__ == "__main__":
    main()
