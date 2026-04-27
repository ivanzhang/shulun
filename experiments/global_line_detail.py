#!/usr/bin/env python3
"""整行/整列危险线细节分析。"""
import argparse
import importlib.util
import math
from collections import Counter, defaultdict
from pathlib import Path

spec = importlib.util.spec_from_file_location("global_grid_scan", Path(__file__).with_name("global_grid_scan.py"))
grid = importlib.util.module_from_spec(spec)
spec.loader.exec_module(grid)


def factor_roots(N, root):
    """列出整除 N 的根基素数。"""
    return [q for q in root if N % q == 0]


def line_record(P, kind, index):
    """分析一行或一列。"""
    flags = grid.sieve(P * P)
    root = grid.primes_upto(P)
    items = []
    q_counter = Counter()
    for t in range(P):
        r, c = (index, t) if kind == "row" else (t, index)
        N = r * P + c + 1
        roots = factor_roots(N, root) if not flags[N] and N > 1 else []
        for q in roots:
            q_counter[q] += 1
        items.append({"t": t, "N": N, "prime": bool(flags[N]), "roots": roots})
    prime_positions = [item["t"] for item in items if item["prime"]]
    return {
        "P": P,
        "kind": kind,
        "index": index,
        "prime_count": len(prime_positions),
        "prime_positions": prime_positions,
        "root_count_used": len(q_counter),
        "total_hits": sum(q_counter.values()),
        "overlap": sum(q_counter.values()) - (P - len(prime_positions)),
        "q_counter": q_counter,
        "items": items,
    }


def print_record(rec, detail=False):
    print(
        f"P={rec['P']},kind={rec['kind']},index={rec['index']},prime_count={rec['prime_count']},"
        f"root_count_used={rec['root_count_used']},total_hits={rec['total_hits']},overlap={rec['overlap']},"
        f"prime_positions={rec['prime_positions']}"
    )
    print(f"top_q={rec['q_counter'].most_common(30)}")
    if detail:
        print("t,N,prime,roots")
        for item in rec["items"]:
            print(f"{item['t']},{item['N']},{item['prime']},{item['roots']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, required=True)
    parser.add_argument("--kind", choices=["row", "col"], required=True)
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    print_record(line_record(args.P, args.kind, args.index), args.detail)


if __name__ == "__main__":
    main()
