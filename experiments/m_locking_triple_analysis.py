#!/usr/bin/env python3
"""分析长 M 段内部连续三点的链式 CRT 锁相。

用法示例：
  python3 experiments/m_locking_triple_analysis.py --P 10000019 --c 1838683 --r 2 --C 8 --delta 30 --detail
  python3 experiments/m_locking_triple_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
import random
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parent
spec_e = importlib.util.spec_from_file_location("m_locking_edge_analysis", base / "m_locking_edge_analysis.py")
edge_mod = importlib.util.module_from_spec(spec_e)
spec_e.loader.exec_module(edge_mod)

spec_m = importlib.util.spec_from_file_location("m_long_segment_analysis", base / "m_long_segment_analysis.py")
mlong = importlib.util.module_from_spec(spec_m)
spec_m.loader.exec_module(mlong)

spec_gap = importlib.util.spec_from_file_location("scan_ub_gap", base / "scan_ub_gap.py")
gap = importlib.util.module_from_spec(spec_gap)
spec_gap.loader.exec_module(gap)


def triple_records(m_records):
    """把每个长 M 段拆成连续三点记录。"""
    triples = []
    for mrec in m_records:
        if mrec["len"] < 3:
            continue
        rows = mrec["rows"]
        for a, b, c in zip(rows, rows[1:], rows[2:]):
            d1 = b["n"] - a["n"]
            d2 = c["n"] - b["n"]
            qs = (a["q"], b["q"], c["q"])
            modulus = 1
            for q in set(qs):
                modulus *= q
            triples.append({
                "seg_idx": mrec["seg_idx"],
                "kind": mrec["kind"],
                "n1": a["n"],
                "n2": b["n"],
                "n3": c["n"],
                "d1": d1,
                "d2": d2,
                "q1": qs[0],
                "q2": qs[1],
                "q3": qs[2],
                "all_distinct": len(set(qs)) == 3,
                "modulus": modulus,
                "type_key": (qs[0], qs[1], qs[2], d1, d2),
                "q_key": qs,
                "d_key": (d1, d2),
            })
    return triples


def record_for(P, c, r, delta, C, primes):
    """生成三点锁相记录。"""
    base_rec = mlong.record_for(P, c, r, delta, C, primes)
    edge_rec = edge_mod.record_for(P, c, r, delta, C, primes)
    triples = triple_records(base_rec["m_records"])
    type_counter = Counter(t["type_key"] for t in triples)
    q_counter = Counter(t["q_key"] for t in triples)
    d_counter = Counter(t["d_key"] for t in triples)
    non_distinct = [t for t in triples if not t["all_distinct"]]
    modulus_le_L = [t for t in triples if t["modulus"] <= base_rec["L"]]
    duplicate_types = [item for item in type_counter.items() if item[1] > 1]
    return {
        **{key: base_rec[key] for key in [
            "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
            "M_long_total", "M_boundary_total", "M_internal_singletons", "max_M_run", "pattern"
        ]},
        "edge_count": edge_rec["edge_count"],
        "triple_count": len(triples),
        "distinct_triple_types": len(type_counter),
        "triple_duplicate_count": sum(count - 1 for count in type_counter.values()),
        "distinct_q_triples": len(q_counter),
        "distinct_d_patterns": len(d_counter),
        "non_distinct_q_triples": len(non_distinct),
        "modulus_le_L": len(modulus_le_L),
        "max_type_reuse": max(type_counter.values(), default=0),
        "top_q_triples": q_counter.most_common(10),
        "top_d_patterns": d_counter.most_common(10),
        "duplicate_types": duplicate_types,
        "triples": triples,
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
        "M_long_total", "edge_count", "triple_count", "distinct_triple_types", "triple_duplicate_count",
        "distinct_q_triples", "distinct_d_patterns", "non_distinct_q_triples", "modulus_le_L", "max_type_reuse",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"top_q_triples={rec['top_q_triples']}")
        print(f"top_d_patterns={rec['top_d_patterns']}")
        print("triples=seg,kind,n1,n2,n3,d1,d2,q1,q2,q3,modulus")
        for t in rec["triples"]:
            print(f"{t['seg_idx']},{t['kind']},{t['n1']},{t['n2']},{t['n3']},{t['d1']},{t['d2']},{t['q1']},{t['q2']},{t['q3']},{t['modulus']}")
        if rec["duplicate_types"]:
            print(f"duplicate_types={rec['duplicate_types']}")


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
        rows.sort(key=lambda rec: (-rec["triple_count"], -rec["edge_count"], rec["P"], rec["c"], rec["r"]))
        print("worst locking-triple records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_triple_count={rows[0]['triple_count'] if rows else 0}")
        print(f"total_triple_duplicates={sum(rec['triple_duplicate_count'] for rec in rows)}")
        print(f"total_non_distinct_q_triples={sum(rec['non_distinct_q_triples'] for rec in rows)}")
        print(f"total_modulus_le_L={sum(rec['modulus_le_L'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
