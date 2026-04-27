#!/usr/bin/env python3
"""把最长 U 合数块分解成 R、M边界、M段头尾、M三点深内部的结构预算。

用法示例：
  python3 experiments/structural_budget_decomposition.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/structural_budget_decomposition.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec_m = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec_m)
spec_m.loader.exec_module(mlong)

spec_tri = importlib.util.spec_from_file_location("m_locking_triple_analysis", base / "m_locking_triple_analysis.py")
triple_mod = importlib.util.module_from_spec(spec_tri)
spec_tri.loader.exec_module(triple_mod)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def m_segment_budget(m_records):
    """计算 M 段预算分解。"""
    boundary_total = 0
    internal_singletons = 0
    long_heads = 0
    deep_triples = 0
    exact_rebuild = 0
    details = []
    for rec in m_records:
        length = rec["len"]
        if rec["kind"] == "boundary":
            boundary_total += length
            component = "boundary"
            rebuild = length
        elif length == 1:
            internal_singletons += 1
            component = "internal_single"
            rebuild = 1
        else:
            head = min(2, length)
            deep = max(0, length - 2)
            long_heads += head
            deep_triples += deep
            component = "internal_long"
            rebuild = head + deep
        exact_rebuild += rebuild
        details.append({
            "seg_idx": rec["seg_idx"],
            "kind": rec["kind"],
            "len": length,
            "component": component,
            "rebuild": rebuild,
            "q_seq": rec["q_seq"],
            "n_seq": rec["n_seq"],
        })
    return {
        "M_boundary_total": boundary_total,
        "M_internal_singletons": internal_singletons,
        "M_long_heads": long_heads,
        "M_deep_triples": deep_triples,
        "M_exact_rebuild": exact_rebuild,
        "details": details,
    }


def record_for(P, c, r, delta, C, primes):
    """生成结构预算记录。"""
    base_rec = mlong.record_for(P, c, r, delta, C, primes)
    tri_rec = triple_mod.record_for(P, c, r, delta, C, primes)
    budget = m_segment_budget(base_rec["m_records"])
    R_segments = base_rec["pattern"].count("R")
    M_segments = base_rec["M_segments"]
    controlled_by_boundary = budget["M_internal_singletons"] + budget["M_long_heads"]
    structural_core = base_rec["R_total"] + budget["M_boundary_total"] + controlled_by_boundary + budget["M_deep_triples"]
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": base_rec["L"],
        "Y": base_rec["Y"],
        "U": base_rec["U"],
        "Prime": base_rec["Prime"],
        "block_len": base_rec["block_len"],
        "R_total": base_rec["R_total"],
        "M_total": base_rec["M_total"],
        "R_segments": R_segments,
        "M_segments": M_segments,
        "M_boundary_total": budget["M_boundary_total"],
        "M_internal_singletons": budget["M_internal_singletons"],
        "M_long_heads": budget["M_long_heads"],
        "M_deep_triples": budget["M_deep_triples"],
        "M_exact_rebuild": budget["M_exact_rebuild"],
        "triple_count": tri_rec["triple_count"],
        "structural_core": structural_core,
        "rebuild_ok": budget["M_exact_rebuild"] == base_rec["M_total"],
        "core_ok": structural_core == base_rec["block_len"],
        "gap_to_U": base_rec["U"] - base_rec["block_len"],
        "prime_gap": base_rec["Prime"],
        "pattern": base_rec["pattern"],
        "details": budget["details"],
    }


def print_record(rec, detail=False):
    """打印预算记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "gap_to_U", "R_total", "R_segments",
        "M_total", "M_segments", "M_boundary_total", "M_internal_singletons", "M_long_heads",
        "M_deep_triples", "triple_count", "rebuild_ok", "core_ok",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print("M_budget=seg,kind,len,component,n_seq,q_seq")
        for row in rec["details"]:
            print(f"{row['seg_idx']},{row['kind']},{row['len']},{row['component']},{row['n_seq']},{row['q_seq']}")


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
                for r in gap.allowed_residues(P, c, args.delta):
                    rows.append(record_for(P, c, r, args.delta, args.C, primes))
        else:
            rows.append(record_for(P, args.c, args.r, args.delta, args.C, primes))
    if args.scan:
        rows.sort(key=lambda rec: (rec["gap_to_U"], -rec["block_len"], -rec["M_deep_triples"], rec["P"], rec["c"], rec["r"]))
        print("tightest structural-budget records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} min_gap_to_U={rows[0]['gap_to_U'] if rows else None}")
        print(f"rebuild_failures={sum(not rec['rebuild_ok'] for rec in rows)} core_failures={sum(not rec['core_ok'] for rec in rows)}")
        print(f"max_M_deep_triples={max((rec['M_deep_triples'] for rec in rows), default=0)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
