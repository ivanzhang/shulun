#!/usr/bin/env python3
"""分析边界预算 boundary=R_segments+M_boundary+M_singletons+M_long_heads 的来源。

用法示例：
  python3 experiments/boundary_budget_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/boundary_budget_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_energy = importlib.util.spec_from_file_location("unified_energy_analysis", base / "unified_energy_analysis.py")
energy_mod = importlib.util.module_from_spec(spec_energy)
spec_energy.loader.exec_module(energy_mod)

spec_m = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec_m)
spec_m.loader.exec_module(mlong)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def classify_segments(P, c, r, delta, C, primes):
    """提取块分段并标注边界贡献。"""
    base_rec = mlong.record_for(P, c, r, delta, C, primes)
    L, Y, items = mlong.collect_with_N(P, c, r, delta, C, primes)
    block = mlong.longest_block(items)
    segs = mlong.segmod.segments(block)
    rows = []
    for idx, (label, seg) in enumerate(segs):
        left = segs[idx - 1][0] if idx > 0 else None
        right = segs[idx + 1][0] if idx + 1 < len(segs) else None
        contribution = 0
        component = "energy_or_none"
        if label == "R":
            contribution = 1
            component = "R_segment_head"
        else:
            if left == "R" and right == "R":
                if len(seg) == 1:
                    contribution = 1
                    component = "M_internal_singleton"
                else:
                    contribution = 2
                    component = "M_long_head"
            elif left == "R" or right == "R":
                contribution = len(seg)
                component = "M_boundary"
            else:
                # 无 R 邻居的纯 M 块按长 M 规则拆：前两点属边界预算，其余属深内部能量。
                contribution = min(2, len(seg))
                component = "M_isolated_head"
        rows.append({
            "idx": idx,
            "label": label,
            "len": len(seg),
            "left": left,
            "right": right,
            "component": component,
            "contribution": contribution,
            "u_start": seg[0]["u_idx"],
            "u_end": seg[-1]["u_idx"],
            "n_start": seg[0]["n"],
            "n_end": seg[-1]["n"],
        })
    return base_rec, rows


def record_for(P, c, r, delta, C, primes):
    """生成边界预算剖析记录。"""
    energy = energy_mod.record_for(P, c, r, delta, C, primes)
    base_rec, rows = classify_segments(P, c, r, delta, C, primes)
    comp_counter = Counter()
    comp_count = Counter()
    for row in rows:
        comp_counter[row["component"]] += row["contribution"]
        comp_count[row["component"]] += 1
    R_segments = comp_counter["R_segment_head"]
    internal_m_segments = comp_count["M_internal_singleton"] + comp_count["M_long_head"]
    r_head_bound_ok = energy["M_internal_singletons"] <= max(0, R_segments - 1)
    long_head_bound_ok = comp_counter["M_long_head"] <= 2 * comp_count["M_long_head"]
    boundary_rebuild = sum(row["contribution"] for row in rows)
    return {
        **energy,
        "component_budget": dict(comp_counter),
        "component_count": dict(comp_count),
        "internal_m_segments": internal_m_segments,
        "boundary_rebuild": boundary_rebuild,
        "boundary_rebuild_ok": boundary_rebuild == energy["boundary"],
        "singletons_vs_R_ok": r_head_bound_ok,
        "long_head_bound_ok": long_head_bound_ok,
        "rows": rows,
    }


def print_record(rec, detail=False):
    """打印边界预算记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "gap_to_U", "boundary", "energy",
        "R_segments", "M_boundary_total", "M_internal_singletons", "M_long_heads", "internal_m_segments",
        "boundary_rebuild_ok", "singletons_vs_R_ok",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"component_budget={rec['component_budget']}")
        print(f"component_count={rec['component_count']}")
        print("segments=idx,label,len,left,right,component,contribution,u,n")
        for row in rec["rows"]:
            print(
                f"{row['idx']},{row['label']},{row['len']},{row['left']},{row['right']},"
                f"{row['component']},{row['contribution']},{row['u_start']}..{row['u_end']},{row['n_start']}..{row['n_end']}"
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
        rows.sort(key=lambda rec: (-rec["boundary"], rec["gap_to_U"], -rec["block_len"], rec["P"], rec["c"], rec["r"]))
        print("highest boundary-budget records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_boundary={rows[0]['boundary'] if rows else None}")
        print(f"boundary_rebuild_failures={sum(not rec['boundary_rebuild_ok'] for rec in rows)} singleton_bound_failures={sum(not rec['singletons_vs_R_ok'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
