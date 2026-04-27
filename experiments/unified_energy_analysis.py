#!/usr/bin/env python3
"""统一统计 R 内部边能量 E_R 与 M 深内部三点能量 T_M。

用法示例：
  python3 experiments/unified_energy_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/unified_energy_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec_budget = importlib.util.spec_from_file_location("structural_budget_decomposition", base / "structural_budget_decomposition.py")
budget_mod = importlib.util.module_from_spec(spec_budget)
spec_budget.loader.exec_module(budget_mod)

spec_redge = importlib.util.spec_from_file_location("r_edge_difference_analysis", base / "r_edge_difference_analysis.py")
redge_mod = importlib.util.module_from_spec(spec_redge)
spec_redge.loader.exec_module(redge_mod)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def record_for(P, c, r, delta, C, primes):
    """生成统一能量记录。"""
    budget = budget_mod.record_for(P, c, r, delta, C, primes)
    redge = redge_mod.record_for(P, c, r, delta, C, primes)
    E_R = redge["R_edge_count"]
    T_M = budget["M_deep_triples"]
    energy = E_R + T_M
    boundary = budget["R_segments"] + budget["M_boundary_total"] + budget["M_internal_singletons"] + budget["M_long_heads"]
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": budget["L"],
        "Y": budget["Y"],
        "U": budget["U"],
        "Prime": budget["Prime"],
        "block_len": budget["block_len"],
        "gap_to_U": budget["gap_to_U"],
        "R_total": budget["R_total"],
        "R_segments": budget["R_segments"],
        "M_total": budget["M_total"],
        "M_segments": budget["M_segments"],
        "M_boundary_total": budget["M_boundary_total"],
        "M_internal_singletons": budget["M_internal_singletons"],
        "M_long_heads": budget["M_long_heads"],
        "E_R": E_R,
        "T_M": T_M,
        "energy": energy,
        "boundary": boundary,
        "energy_ratio_U": energy / budget["U"] if budget["U"] else 0.0,
        "energy_gap": budget["U"] - energy,
        "boundary_gap": budget["U"] - boundary,
        "identity_ok": boundary + energy == budget["block_len"],
        "pattern": budget["pattern"],
    }


def print_record(rec, detail=False):
    """打印统一能量记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "gap_to_U",
        "R_segments", "M_boundary_total", "M_internal_singletons", "M_long_heads",
        "E_R", "T_M", "energy", "energy_gap", "boundary", "boundary_gap", "identity_ok",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"energy_ratio_U={rec['energy_ratio_U']:.4f}")


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
    primes = budget_mod.mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda rec: (-rec["energy"], rec["energy_gap"], -rec["block_len"], rec["P"], rec["c"], rec["r"]))
        print("highest unified-energy records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_energy={rows[0]['energy'] if rows else None} min_energy_gap={min((rec['energy_gap'] for rec in rows), default=None)}")
        print(f"identity_failures={sum(not rec['identity_ok'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
