#!/usr/bin/env python3
"""分析长合数块的分型判别：高能量型 vs 低能量交替型。

用法示例：
  python3 experiments/type_dichotomy_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/type_dichotomy_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec_energy = importlib.util.spec_from_file_location("bridge_chain_energy", base / "bridge_chain_energy.py")
energy_mod = importlib.util.module_from_spec(spec_energy)
spec_energy.loader.exec_module(energy_mod)

spec_alt = importlib.util.spec_from_file_location("alternating_chain_analysis", base / "alternating_chain_analysis.py")
alt_mod = importlib.util.module_from_spec(spec_alt)
spec_alt.loader.exec_module(alt_mod)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def record_for(P, c, r, delta, C, primes):
    """生成分型判别记录。"""
    en = energy_mod.record_for(P, c, r, delta, C, primes)
    alt = alt_mod.record_for(P, c, r, delta, C, primes)
    # 简单二分指标：段数由内部能量或最长交替链支撑。
    support = en["chain_energy"] + alt["max_alt_len"]
    normalized_support = support / en["R_segments"] if en["R_segments"] else 0.0
    low_energy = en["chain_energy"] <= 2 * en["R_segments"]
    long_alt = alt["max_alt_len"] >= max(3, en["R_segments"] // 2)
    return {
        "P": P,
        "c": c,
        "r": r,
        "L": en["L"],
        "Y": en["Y"],
        "U": en["U"],
        "Prime": en["Prime"],
        "block_len": en["block_len"],
        "R_segments": en["R_segments"],
        "internal_bridges": en["internal_bridges"],
        "chain_energy": en["chain_energy"],
        "energy_per_segment": en["energy_per_segment"],
        "R_internal_energy": en["R_internal_energy"],
        "M_deep_energy": en["M_deep_energy"],
        "distinct_segment_shapes": en["distinct_segment_shapes"],
        "max_alt_len": alt["max_alt_len"],
        "max_alt_R": alt["max_alt_R"],
        "max_alt_M": alt["max_alt_M"],
        "support": support,
        "normalized_support": normalized_support,
        "low_energy": low_energy,
        "long_alt": long_alt,
        "dichotomy_ok": (not low_energy) or long_alt,
        "pattern": en["pattern"],
    }


def print_record(rec, detail=False):
    """打印分型判别。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_segments", "internal_bridges",
        "chain_energy", "energy_per_segment", "R_internal_energy", "M_deep_energy", "distinct_segment_shapes",
        "max_alt_len", "max_alt_R", "max_alt_M", "support", "normalized_support", "low_energy", "long_alt", "dichotomy_ok",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")


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
    primes = energy_mod.segpat.mlong.segmod.build_primes(Ps, args.C, args.delta)
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
        rows.sort(key=lambda rec: (rec["dichotomy_ok"], -rec["R_segments"], rec["chain_energy"], -rec["max_alt_len"], rec["P"], rec["c"], rec["r"]))
        print("dichotomy stress records")
        for rec in rows[:30]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} dichotomy_failures={sum(not rec['dichotomy_ok'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
