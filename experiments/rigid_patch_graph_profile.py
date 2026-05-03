#!/usr/bin/env python3
"""刚性补洞差分共享图分析。

顶点为小筛后仍为合数的洞；若两个洞共享某个大素数补丁 q，则连边。
统计连通分量、树/环复杂度、最大组件、孤立点与贪心覆盖压力。

用法示例：
  python3 experiments/rigid_patch_graph_profile.py --P 1009 --a 720 --ys 31,47,71,101 --detail
  python3 experiments/rigid_patch_graph_profile.py --Ps 251,503,1009 --ys 31,47,71
"""
import argparse
from collections import Counter, defaultdict, deque
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def graph_profile(rec):
    """从补洞记录构造共享图指标。"""
    vertices = set(r for r, qs in rec["patch_factors_by_r"].items() if qs)
    adj = {r: set() for r in vertices}
    edge_labels = defaultdict(set)
    for q, rows in rec["shared_qs"].items():
        rows = [r for r in rows if r in vertices]
        for i, r1 in enumerate(rows):
            for r2 in rows[i + 1:]:
                adj[r1].add(r2)
                adj[r2].add(r1)
                edge_labels[tuple(sorted((r1, r2)))].add(q)

    seen = set()
    comps = []
    for start in vertices:
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        comp = []
        while queue:
            r = queue.popleft()
            comp.append(r)
            for nb in adj[r]:
                if nb not in seen:
                    seen.add(nb)
                    queue.append(nb)
        comp_set = set(comp)
        edge_count = sum(1 for e in edge_labels if e[0] in comp_set and e[1] in comp_set)
        label_count = len({q for e, qs in edge_labels.items() if e[0] in comp_set and e[1] in comp_set for q in qs})
        comps.append((len(comp), edge_count, label_count, sorted(comp)))
    comps.sort(reverse=True, key=lambda x: (x[0], x[1]))

    comp_size_hist = Counter(size for size, _, _, _ in comps)
    edge_count = len(edge_labels)
    label_multiplicity = Counter(len(qs) for qs in edge_labels.values())
    isolated = comp_size_hist.get(1, 0)
    nontrivial = sum(1 for size, _, _, _ in comps if size >= 2)
    cyclomatic = sum(max(0, edges - size + 1) for size, edges, _, _ in comps)

    return {
        "V": len(vertices),
        "E": edge_count,
        "components": len(comps),
        "isolated": isolated,
        "nontrivial_components": nontrivial,
        "max_component": comps[0][0] if comps else 0,
        "max_component_edges": comps[0][1] if comps else 0,
        "cyclomatic": cyclomatic,
        "comp_hist": comp_size_hist,
        "label_multiplicity": label_multiplicity,
        "top_components": comps[:8],
    }


def analyze(P, a, ys, detail):
    flags = sieve(P * P)
    root_primes = primes_from_flags(flags, P)
    rows = []
    for y in ys:
        rec = record_for(P, a, y, flags, root_primes)
        prof = graph_profile(rec)
        rows.append((rec, prof))
        print(
            f"P={P} a={a} y={y} H={rec['holes']} prime={rec['prime_holes']} comp={rec['composite_holes']} "
            f"V={prof['V']} E={prof['E']} comps={prof['components']} iso={prof['isolated']} "
            f"nontriv={prof['nontrivial_components']} maxC={prof['max_component']} cyc={prof['cyclomatic']} "
            f"cover≈{rec['greedy_cover']} maxhit={rec['max_q_hit']}"
        )
        if detail:
            print("  comp_hist", sorted(prof["comp_hist"].items()))
            print("  label_mult", sorted(prof["label_multiplicity"].items()))
            print("  top_components", [(size, edges, labels, verts[:20]) for size, edges, labels, verts in prof["top_components"]])
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--a", type=int, default=720)
    parser.add_argument("--ys", default="31,47,71,101")
    parser.add_argument("--Ps", default="")
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    ys = [int(x) for x in args.ys.split(",") if x.strip()]
    if args.Ps:
        for P in [int(x) for x in args.Ps.split(",") if x.strip()]:
            # 先找 y=min(ys) 下最危险列。
            flags = sieve(P * P)
            root_primes = primes_from_flags(flags, P)
            y0 = ys[0]
            best = None
            for a in range(1, P):
                rec = record_for(P, a, y0, flags, root_primes)
                key = (rec["prime_holes"], rec["holes"], -rec["shared_edges"])
                if best is None or key < best[0]:
                    best = (key, a)
            analyze(P, best[1], ys, args.detail)
        return
    analyze(args.P, args.a, ys, args.detail)


if __name__ == "__main__":
    main()
