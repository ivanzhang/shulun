#!/usr/bin/env python3
"""分析长 M 段内部相邻点的“短程锁相边”。

用法示例：
  python3 experiments/m_locking_edge_analysis.py --P 3000017 --c 458685 --r 8 --C 8 --delta 30 --detail
  python3 experiments/m_locking_edge_analysis.py --scan --primes 1000003,3000017,10000019 --cols 80 --C 8 --delta 30
"""
import argparse
import importlib.util
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


def edge_records(m_records):
    """把每个长 M 段拆成相邻锁相边。"""
    edges = []
    for mrec in m_records:
        if mrec["len"] < 2:
            continue
        rows = mrec["rows"]
        for left, right in zip(rows, rows[1:]):
            q1 = left["q"]
            q2 = right["q"]
            d = right["n"] - left["n"]
            edges.append({
                "seg_idx": mrec["seg_idx"],
                "kind": mrec["kind"],
                "u1": left["u_idx"],
                "u2": right["u_idx"],
                "n1": left["n"],
                "n2": right["n"],
                "d": d,
                "q1": q1,
                "q2": q2,
                "same_q": q1 == q2,
                "short_same_q_forbidden_ok": (q1 != q2) or (d % q1 == 0),
                "product": q1 * q2,
                "ordered_key": (q1, q2, d),
                "pair_key": (q1, q2),
                "unordered_key": tuple(sorted((q1, q2))) + (d,),
            })
    return edges


def record_for(P, c, r, delta, C, primes):
    """生成锁相边记录。"""
    base_rec = mlong.record_for(P, c, r, delta, C, primes)
    edges = edge_records(base_rec["m_records"])
    ordered = Counter(edge["ordered_key"] for edge in edges)
    pair = Counter(edge["pair_key"] for edge in edges)
    unordered = Counter(edge["unordered_key"] for edge in edges)
    d_counter = Counter(edge["d"] for edge in edges)
    q_vertex_counter = Counter()
    for edge in edges:
        q_vertex_counter[edge["q1"]] += 1
        q_vertex_counter[edge["q2"]] += 1
    product_le_L = [edge for edge in edges if edge["product"] <= base_rec["L"]]
    same_q_bad = [edge for edge in edges if not edge["short_same_q_forbidden_ok"]]
    ordered_duplicates = [item for item in ordered.items() if item[1] > 1]
    return {
        **{key: base_rec[key] for key in [
            "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
            "M_long_total", "M_boundary_total", "M_internal_singletons", "max_M_run", "pattern"
        ]},
        "edge_count": len(edges),
        "distinct_ordered_edges": len(ordered),
        "distinct_pairs": len(pair),
        "distinct_unordered_edges": len(unordered),
        "ordered_duplicate_count": sum(count - 1 for count in ordered.values()),
        "pair_repeat_count": sum(count - 1 for count in pair.values()),
        "max_pair_reuse": max(pair.values(), default=0),
        "product_le_L": len(product_le_L),
        "same_q_bad": len(same_q_bad),
        "d_counter": d_counter,
        "top_q_vertices": q_vertex_counter.most_common(10),
        "top_pairs": pair.most_common(10),
        "ordered_duplicates": ordered_duplicates,
        "edges": edges,
    }


def print_record(rec, detail=False):
    """打印记录。"""
    keys = [
        "P", "c", "r", "L", "Y", "U", "Prime", "block_len", "R_total", "M_total",
        "M_long_total", "edge_count", "distinct_ordered_edges", "ordered_duplicate_count",
        "distinct_pairs", "pair_repeat_count", "max_pair_reuse", "product_le_L", "same_q_bad",
    ]
    print(",".join(f"{key}={rec[key]}" for key in keys))
    if detail:
        print(f"pattern={rec['pattern']}")
        print(f"d_counter={dict(rec['d_counter'])}")
        print(f"top_q_vertices={rec['top_q_vertices']}")
        print(f"top_pairs={rec['top_pairs']}")
        print("edges=seg,kind,n1,n2,d,q1,q2,product")
        for edge in rec["edges"]:
            print(f"{edge['seg_idx']},{edge['kind']},{edge['n1']},{edge['n2']},{edge['d']},{edge['q1']},{edge['q2']},{edge['product']}")
        if rec["ordered_duplicates"]:
            print(f"ordered_duplicates={rec['ordered_duplicates']}")


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
        rows.sort(key=lambda rec: (-rec["edge_count"], -rec["pair_repeat_count"], rec["P"], rec["c"], rec["r"]))
        print("worst locking-edge records")
        for rec in rows[:20]:
            print_record(rec, detail=False)
        print(f"checked={len(rows)} max_edge_count={rows[0]['edge_count'] if rows else 0}")
        print(f"total_ordered_duplicates={sum(rec['ordered_duplicate_count'] for rec in rows)}")
        print(f"total_product_le_L={sum(rec['product_le_L'] for rec in rows)}")
        print(f"total_same_q_bad={sum(rec['same_q_bad'] for rec in rows)}")
    else:
        print_record(rows[0], detail=args.detail)


if __name__ == "__main__":
    main()
