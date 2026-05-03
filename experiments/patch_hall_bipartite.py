#!/usr/bin/env python3
"""小筛洞-大素数补丁二部图 Hall/匹配分析。

左侧：H_y(a) 中实际合数洞；右侧：能整除这些洞的大素数 q in (y,P)。
边：q | a+rP。
若反例存在且无素数洞，则左侧应覆盖全部 H_y(a)。这里分析合数部分能否完美匹配、Hall 亏损、度分布。

用法示例：
  python3 experiments/patch_hall_bipartite.py --P 1009 --a 720 --ys 101,173,293 --detail
  python3 experiments/patch_hall_bipartite.py --P 2003 --a 1019 --ys 173,293,503 --detail
"""
import argparse
from collections import Counter, deque, defaultdict
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def hopcroft_karp(graph):
    """计算左侧到右侧的最大匹配。graph: left -> iterable(right)。"""
    left_nodes = list(graph)
    pair_u = {u: None for u in left_nodes}
    pair_v = {}
    dist = {}

    def bfs():
        queue = deque()
        found = False
        for u in left_nodes:
            if pair_u[u] is None:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = None
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                pu = pair_v.get(v)
                if pu is None:
                    found = True
                elif dist.get(pu) is None:
                    dist[pu] = dist[u] + 1
                    queue.append(pu)
        return found

    def dfs(u):
        for v in graph[u]:
            pu = pair_v.get(v)
            if pu is None or (dist.get(pu) == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = None
        return False

    matching = 0
    while bfs():
        for u in left_nodes:
            if pair_u[u] is None and dfs(u):
                matching += 1
    return matching, pair_u, pair_v


def reachable_min_vertex_cover(graph, pair_u, pair_v):
    """Kőnig 构造最小点覆盖，并给出未匹配左侧出发的交替可达集。"""
    left = set(graph)
    right = {v for vs in graph.values() for v in vs}
    z_left = set()
    z_right = set()
    queue = deque([u for u in left if pair_u[u] is None])
    z_left.update(queue)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            # 非匹配边 L->R
            if pair_u[u] == v:
                continue
            if v not in z_right:
                z_right.add(v)
                # 匹配边 R->L
                if v in pair_v and pair_v[v] not in z_left:
                    z_left.add(pair_v[v])
                    queue.append(pair_v[v])
    min_cover_left = left - z_left
    min_cover_right = z_right
    return z_left, z_right, min_cover_left, min_cover_right


def analyze(P, a, y, flags, root, detail=False):
    rec = record_for(P, a, y, flags, root)
    graph = {r: tuple(qs) for r, qs in rec["patch_factors_by_r"].items() if qs}
    right = sorted({q for qs in graph.values() for q in qs})
    matching, pair_u, pair_v = hopcroft_karp(graph)
    z_left, z_right, cover_left, cover_right = reachable_min_vertex_cover(graph, pair_u, pair_v)
    left_count = len(graph)
    unmatched = left_count - matching
    left_deg = Counter(len(qs) for qs in graph.values())
    right_deg_counter = Counter()
    q_to_rows = defaultdict(list)
    for r, qs in graph.items():
        for q in qs:
            q_to_rows[q].append(r)
    for q, rows in q_to_rows.items():
        right_deg_counter[len(rows)] += 1
    # Hall 亏损证书：若 unmatched>0，交替可达左集 z_left 给出 |N(S)|<|S| 的候选。
    hall_defect = len(z_left) - len(z_right) if unmatched else 0
    print(
        f"P={P} a={a} y={y} H={rec['holes']} prime={rec['prime_holes']} compL={left_count} rightQ={len(right)} "
        f"match={matching} unmatched={unmatched} hallDef={hall_defect} "
        f"leftDeg={sorted(left_deg.items())} rightDeg={sorted(right_deg_counter.items())} "
        f"minVC=({len(cover_left)}L,{len(cover_right)}R)"
    )
    if detail:
        print("  unmatched_left", [u for u in graph if pair_u[u] is None][:80])
        print("  hall_Z_sizes", len(z_left), len(z_right))
        print("  hall_Z_left", sorted(z_left)[:120])
        print("  hall_Z_right", sorted(z_right)[:120])
        print("  top_right", sorted(((len(rows), q, rows[:20]) for q, rows in q_to_rows.items()), reverse=True)[:20])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--a", type=int, default=720)
    parser.add_argument("--ys", default="101,173,293")
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    flags = sieve(args.P * args.P)
    root = primes_from_flags(flags, args.P)
    for y in [int(x) for x in args.ys.split(",") if x.strip()]:
        analyze(args.P, args.a, y, flags, root, args.detail)


if __name__ == "__main__":
    main()
