#!/usr/bin/env python3
"""纯同余 Hall 图分析。

左侧：全部小筛洞 H_y(a)，包括真实素数洞。
右侧：q in (y,P) 的素数。
边：r ≡ -a P^{-1} (mod q)。

这表示“如果 r 要被大素数 q 补掉，纯同余容量是否允许”。
若此图无法匹配全部 H_y(a)，则刚性补洞引理成立。

用法示例：
  python3 experiments/pure_congruence_hall.py --P 1009 --a 720 --ys 101,173,293 --detail
  python3 experiments/pure_congruence_hall.py --Ps 251,503,1009 --ys 101,173,293
"""
import argparse
from collections import Counter, defaultdict, deque
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for
from patch_hall_bipartite import hopcroft_karp, reachable_min_vertex_cover


def pure_graph(P, a, y, flags, root):
    """构造全部小筛洞到大素数同余补丁的纯容量图。"""
    rec = record_for(P, a, y, flags, root)
    big_primes = [q for q in root if y < q < P]
    graph = {r: [] for r in rec["holes_list"]}
    for q in big_primes:
        residue = (-a * pow(P, -1, q)) % q
        for r in range(residue, P, q):
            # 根基素数自身 q 不是合数覆盖边，只保留 proper multiple。
            if r in graph and a + r * P != q:
                graph[r].append(q)
    graph = {r: tuple(qs) for r, qs in graph.items()}
    return rec, graph


def analyze(P, a, y, flags, root, detail=False):
    rec, graph = pure_graph(P, a, y, flags, root)
    match, pair_u, pair_v = hopcroft_karp(graph)
    z_left, z_right, cover_left, cover_right = reachable_min_vertex_cover(graph, pair_u, pair_v)
    left_count = len(graph)
    right_count = len({q for qs in graph.values() for q in qs})
    unmatched = left_count - match
    left_deg = Counter(len(qs) for qs in graph.values())
    q_to_rows = defaultdict(list)
    for r, qs in graph.items():
        for q in qs:
            q_to_rows[q].append(r)
    right_deg = Counter(len(rows) for rows in q_to_rows.values())
    prime_unmatched = sum(1 for r in graph if pair_u[r] is None and r in set(rec["prime_rows"]))
    comp_unmatched = unmatched - prime_unmatched
    print(
        f"P={P} a={a} y={y} H={rec['holes']} prime={rec['prime_holes']} comp={rec['composite_holes']} "
        f"rightQ={right_count} match={match} unmatched={unmatched} "
        f"unmatchedPrime={prime_unmatched} unmatchedComp={comp_unmatched} "
        f"leftDeg={sorted(left_deg.items())[:8]} rightDeg={sorted(right_deg.items())[:8]} "
        f"minVC=({len(cover_left)}L,{len(cover_right)}R)"
    )
    if detail:
        unmatched_rows = [r for r in graph if pair_u[r] is None]
        print("  unmatched_rows", unmatched_rows[:120])
        print("  hall_Z_sizes", len(z_left), len(z_right), "defect", len(z_left) - len(z_right) if unmatched else 0)
        print("  hall_Z_left", sorted(z_left)[:160])
        print("  hall_Z_right", sorted(z_right)[:160])
        print("  top_right", sorted(((len(rows), q, rows[:20]) for q, rows in q_to_rows.items()), reverse=True)[:20])


def scan_P(P, ys, detail=False):
    flags = sieve(P * P)
    root = primes_from_flags(flags, P)
    for y in ys:
        # 使用该 y 下真实最危险列：素数洞最少。
        best = None
        for a in range(1, P):
            rec = record_for(P, a, y, flags, root)
            key = (rec["prime_holes"], rec["holes"], -rec["shared_edges"])
            if best is None or key < best[0]:
                best = (key, a)
        analyze(P, best[1], y, flags, root, detail)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--a", type=int, default=720)
    parser.add_argument("--ys", default="101,173,293")
    parser.add_argument("--Ps", default="")
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    ys = [int(x) for x in args.ys.split(",") if x.strip()]
    if args.Ps:
        for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
            scan_P(P, [y for y in ys if y < P], args.detail)
        return
    flags = sieve(args.P * args.P)
    root = primes_from_flags(flags, args.P)
    for y in [y for y in ys if y < args.P]:
        analyze(args.P, args.a, y, flags, root, args.detail)


if __name__ == "__main__":
    main()
