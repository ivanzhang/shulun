#!/usr/bin/env python3
"""枚举小 r 的超图，检查 connected 骨架外的 rank 节省。"""
from itertools import combinations, chain
from collections import defaultdict, deque


def subsets(vertices):
    """生成所有大小至少 2 的超边。"""
    verts = list(vertices)
    for k in range(2, len(verts) + 1):
        for comb in combinations(verts, k):
            yield tuple(comb)


def rank(edge):
    return len(edge) - 1


def connected(vertices, edges):
    """用超边诱导的普通连接性判断。"""
    adj = defaultdict(set)
    for edge in edges:
        for a, b in combinations(edge, 2):
            adj[a].add(b)
            adj[b].add(a)
    start = next(iter(vertices))
    seen = {start}
    q = deque([start])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    return len(seen) == len(vertices)


def ordinary_edges(edge):
    """一个超边可贡献的二点投影。"""
    return list(combinations(edge, 2))


def has_tree_skeleton(vertices, hyperedges):
    """暴力判断能否从超边中选 r-1 个二点投影组成生成树。"""
    candidates = []
    for idx, edge in enumerate(hyperedges):
        for a, b in ordinary_edges(edge):
            candidates.append((idx, tuple(sorted((a, b)))))
    n = len(vertices)
    for chosen in combinations(range(len(candidates)), n - 1):
        used_edges = [candidates[i][1] for i in chosen]
        if connected(vertices, used_edges):
            used_hyper = {candidates[i][0] for i in chosen}
            return True, used_hyper, used_edges
    return False, set(), []


def scan(r, max_edges=None):
    vertices = tuple(range(r))
    all_edges = list(subsets(vertices))
    stats = defaultdict(int)
    bad = []
    # 限制枚举规模：检查所有边数到 max_edges 的超图
    if max_edges is None:
        max_edges = min(len(all_edges), r + 1)
    for m in range(1, max_edges + 1):
        for edge_idxs in combinations(range(len(all_edges)), m):
            hedges = [all_edges[i] for i in edge_idxs]
            if not connected(vertices, hedges):
                continue
            ok, used_hyper, tree_edges = has_tree_skeleton(vertices, hedges)
            total_rank = sum(rank(e) for e in hedges)
            extra_rank = total_rank - (r - 1)
            stats[(m, extra_rank, ok)] += 1
            if not ok:
                bad.append(hedges)
    return stats, bad


def main():
    for r in [3, 4, 5]:
        stats, bad = scan(r, max_edges=min(r + 1, 5))
        print(f"r={r}: bad={len(bad)}")
        by_extra = defaultdict(int)
        for (_m, extra, ok), count in stats.items():
            by_extra[(extra, ok)] += count
        for key in sorted(by_extra):
            print(f"  extra_rank={key[0]}, tree_ok={key[1]}: {by_extra[key]}")
        if bad[:3]:
            print("  sample bad:", bad[:3])

if __name__ == "__main__":
    main()
