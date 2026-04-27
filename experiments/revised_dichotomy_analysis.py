#!/usr/bin/env python3
"""用修正能量 E'=sum(a-1)+sum(b-1)+distinct_shapes 检验分型判别。"""
import argparse
import importlib.util
import random
from pathlib import Path

base = Path(__file__).resolve().parent
spec_seg = importlib.util.spec_from_file_location("segment_level_endpoint_pattern", base / "segment_level_endpoint_pattern.py")
segpat = importlib.util.module_from_spec(spec_seg)
spec_seg.loader.exec_module(segpat)

spec_alt = importlib.util.spec_from_file_location("alternating_chain_analysis", base / "alternating_chain_analysis.py")
alt_mod = importlib.util.module_from_spec(spec_alt)
spec_alt.loader.exec_module(alt_mod)

spec_budget = importlib.util.spec_from_file_location("structural_budget_decomposition", base / "structural_budget_decomposition.py")
budget_mod = importlib.util.module_from_spec(spec_budget)
spec_budget.loader.exec_module(budget_mod)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def record_for(P, c, r, delta, C, primes):
    seg = segpat.record_for(P, c, r, delta, C, primes)
    alt = alt_mod.record_for(P, c, r, delta, C, primes)
    budget = budget_mod.record_for(P, c, r, delta, C, primes)
    shapes = set(tuple(b["shape"]) for b in seg["bridges"])
    r_internal = budget["R_total"] - budget["R_segments"]
    m_excess = sum(max(0, b["M_len"] - 1) for b in seg["bridges"])
    revised_energy = r_internal + m_excess + len(shapes)
    s = seg["R_segments"]
    long_alt = alt["max_alt_len"] >= max(3, s // 2)
    high_energy_2 = revised_energy > 2 * s
    high_energy_15 = revised_energy > 1.5 * s
    return {
        "P": P, "c": c, "r": r,
        "L": seg["L"], "Y": seg["Y"], "U": seg["U"], "Prime": seg["Prime"],
        "block_len": seg["block_len"], "R_segments": s, "internal_bridges": seg["internal_bridges"],
        "R_total": budget["R_total"], "M_total": budget["M_total"],
        "r_internal": r_internal, "m_excess": m_excess, "distinct_shapes": len(shapes),
        "revised_energy": revised_energy,
        "energy_per_segment": revised_energy / s if s else 0,
        "max_alt_len": alt["max_alt_len"], "max_alt_R": alt["max_alt_R"], "max_alt_M": alt["max_alt_M"],
        "dichotomy_2_ok": high_energy_2 or long_alt,
        "dichotomy_15_ok": high_energy_15 or long_alt,
        "long_alt": long_alt,
        "pattern": seg["pattern"],
    }


def print_record(rec, detail=False):
    keys = ["P","c","r","L","Y","U","Prime","block_len","R_segments","internal_bridges","r_internal","m_excess","distinct_shapes","revised_energy","energy_per_segment","max_alt_len","long_alt","dichotomy_2_ok","dichotomy_15_ok"]
    print(",".join(f"{k}={rec[k]}" for k in keys))
    if detail:
        print(f"pattern={rec['pattern']}")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--scan',action='store_true')
    ap.add_argument('--P',type=int,default=0); ap.add_argument('--c',type=int,default=0); ap.add_argument('--r',type=int,default=0)
    ap.add_argument('--primes',default='1000003,3000017,10000019'); ap.add_argument('--cols',type=int,default=80)
    ap.add_argument('--C',type=float,default=8.0); ap.add_argument('--delta',type=int,default=30); ap.add_argument('--detail',action='store_true')
    args=ap.parse_args()
    Ps=[int(x) for x in args.primes.split(',') if x.strip()] if args.scan else [args.P]
    if not args.scan and (not args.P or not args.c): raise SystemExit('非扫描模式需要 --P 与 --c，或使用 --scan')
    primes=segpat.mlong.segmod.build_primes(Ps,args.C,args.delta)
    rows=[]
    for P in Ps:
        if args.scan:
            random.seed(P)
            cols=list(dict.fromkeys([1,2,6,30,P//2,P-1]+random.sample(range(1,P),min(args.cols,P-1))))
            for c in cols:
                for rr in gap.allowed_residues(P,c,args.delta):
                    rows.append(record_for(P,c,rr,args.delta,args.C,primes))
        else:
            rows.append(record_for(P,args.c,args.r,args.delta,args.C,primes))
    if args.scan:
        rows.sort(key=lambda x:(x['dichotomy_2_ok'], -x['R_segments'], x['revised_energy'], -x['max_alt_len'], x['P'], x['c'], x['r']))
        print('revised dichotomy stress records')
        for rec in rows[:30]: print_record(rec)
        print(f"checked={len(rows)} failures_2={sum(not x['dichotomy_2_ok'] for x in rows)} failures_15={sum(not x['dichotomy_15_ok'] for x in rows)}")
        for th in range(4,11):
            sub=[x for x in rows if x['R_segments']>=th]
            print(f"threshold={th} count={len(sub)} fail2={sum(not x['dichotomy_2_ok'] for x in sub)} fail15={sum(not x['dichotomy_15_ok'] for x in sub)}")
    else:
        print_record(rows[0], args.detail)
if __name__=='__main__': main()
