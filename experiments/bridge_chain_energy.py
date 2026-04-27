#!/usr/bin/env python3
"""为段级桥链 R^a M^b R^c 建立统一能量函数。

用法示例：
  python3 experiments/bridge_chain_energy.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/bridge_chain_energy.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_seg = importlib.util.spec_from_file_location("segment_level_endpoint_pattern", base / "segment_level_endpoint_pattern.py")
segpat = importlib.util.module_from_spec(spec_seg)
spec_seg.loader.exec_module(segpat)

spec_budget = importlib.util.spec_from_file_location("structural_budget_decomposition", base / "structural_budget_decomposition.py")
budget_mod = importlib.util.module_from_spec(spec_budget)
spec_budget.loader.exec_module(budget_mod)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def record_for(P, c, r, delta, C, primes):
    """生成桥链能量记录。"""
    seg = segpat.record_for(P, c, r, delta, C, primes)
    budget = budget_mod.record_for(P, c, r, delta, C, primes)
    shapes = Counter(tuple(b["shape"]) for b in seg["bridges"])
    repeated_shapes = sum(v - 1 for v in shapes.values())
    shape_entropy_proxy = len(shapes)
    R_internal_energy = budget["R_total"] - budget["R_segments"]
    M_deep_energy = budget["M_deep_triples"]
    long_bridge_energy = sum(max(0, b["M_len"] - 2) for b in seg["bridges"])
    bridge_head_energy = 2 * seg["long_bridges"] + (seg["internal_bridges"] - seg["long_bridges"])
    chain_energy = R_internal_energy + M_deep_energy + shape_entropy_proxy
    saturation_defect = max(0, (seg["R_segments"] - 1) - seg["internal_bridges"])
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": seg["L"],
        "Y": seg["Y"],
        "U": seg["U"],
        "Prime": seg["Prime"],
        "block_len": seg["block_len"],
        "R_segments": seg["R_segments"],
        "R_total": budget["R_total"],
        "M_total": budget["M_total"],
        "internal_bridges": seg["internal_bridges"],
        "saturation_defect": saturation_defect,
        "long_bridges": seg["long_bridges"],
        "bridge_points": seg["bridge_points"],
        "distinct_segment_shapes": seg["distinct_segment_shapes"],
        "segment_shape_repeat": repeated_shapes,
        "R_internal_energy": R_internal_energy,
        "M_deep_energy": M_deep_energy,
        "long_bridge_energy": long_bridge_energy,
        "bridge_head_energy": bridge_head_energy,
        "chain_energy": chain_energy,
        "energy_per_segment": chain_energy / seg["R_segments"] if seg["R_segments"] else 0.0,
        "shape_counter": shapes,
        "pattern": seg["pattern"],
        "bridges": seg["bridges"],
    }


def print_record(rec, detail=False):
    """打印桥链能量。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "internal_bridges",
        "saturation_defect", "long_bridges", "bridge_points", "distinct_segment_shapes", "segment_shape_repeat",
        "R_internal_energy", "M_deep_energy", "long_bridge_energy", "bridge_head_energy", "chain_energy", "energy_per_segment",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"shape_counter={dict(rec['shape_counter'])}")
        print("bridges=shape,left_end,right_start,m_q_seq")
        for b in rec["bridges"]:
            print(f"{b['shape']},{b['left_end_n']},{b['right_start_n']},{b['m_q_seq']}")


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
    primes = segpat.mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda rec: (-rec["R_segments"], -rec["chain_energy"], rec["P"], rec["c"], rec["r"]))
        print("highest bridge-chain energy records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_R_segments={rows[0]['R_segments'] if rows else None} max_chain_energy={max((rec['chain_energy'] for rec in rows), default=None)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
