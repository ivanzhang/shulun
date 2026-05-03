#!/usr/bin/env python3
"""扫描 C=4 窗口内多粗因子链图 n1~q n2~r n3 (q!=r)。

顶点为 R/T 粗合数证书；边为共享 >sqrt(P) 粗因子。
因 E7 已排除同一粗因子三点簇，本脚本统计不同粗因子形成的长度二链/更大连通图。

用法示例：
  python3 experiments/multifactor_chain_graph_scan.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from collections import Counter, defaultdict
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def certs_in_row(P, row, flags, plist, small, B):
    certs = []
    for c in range(1, P + 1):
        n = (row - 1) * P + c
        if not all(n % p for p in small):
            continue
        if flags[n]:
            continue
        fac = tuple(q for q in factor_distinct(n, plist) if q > B)
        if len(fac) == 2:
            certs.append((c, 'S2', fac))
        elif len(fac) == 3:
            certs.append((c, 'T3', fac))
    return certs


def window_graph(items):
    n = len(items)
    adj = [set() for _ in range(n)]
    edge_factors = {}
    factor_to_vertices = defaultdict(list)
    for i, (_, _, fac) in enumerate(items):
        for q in fac:
            factor_to_vertices[q].append(i)
    for q, verts in factor_to_vertices.items():
        if len(verts) < 2:
            continue
        for a in range(len(verts)):
            for b in range(a + 1, len(verts)):
                i, j = verts[a], verts[b]
                adj[i].add(j)
                adj[j].add(i)
                edge_factors[tuple(sorted((i, j)))] = q
    seen = [False] * n
    comps = []
    for i in range(n):
        if seen[i]:
            continue
        stack = [i]
        seen[i] = True
        comp = []
        while stack:
            v = stack.pop()
            comp.append(v)
            for w in adj[v]:
                if not seen[w]:
                    seen[w] = True
                    stack.append(w)
        if len(comp) >= 2:
            comps.append(comp)
    chain2 = 0
    chain_shapes = Counter()
    for comp in comps:
        degs = [len(adj[v] & set(comp)) for v in comp]
        edge_count = sum(degs) // 2
        types = Counter(items[v][1] for v in comp)
        shape = (len(comp), edge_count, tuple(sorted(degs)), tuple(sorted(types.items())))
        chain_shapes[shape] += 1
        if len(comp) >= 3 and edge_count >= 2:
            # 统计长度二路径数量。
            for v in comp:
                d = len(adj[v] & set(comp))
                chain2 += d * (d - 1) // 2
    return comps, chain2, chain_shapes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L windows meanV meanEdges meanChain2 chainWindowRate maxCompHist topShapes')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        small = primes(sieve(B), B)
        step = max(1, L // 8)
        vertices = []
        edges = []
        chain2s = []
        max_hist = Counter()
        shape_hist = Counter()
        windows = 0
        for row in range(1, P + 1):
            certs = certs_in_row(P, row, flags, plist, small, B)
            for start in range(1, P - L + 2, step):
                end = start + L - 1
                items = [x for x in certs if start <= x[0] <= end]
                comps, chain2, shapes = window_graph(items)
                edge_count = sum(edge_num * cnt for (_, edge_num, _, _), cnt in shapes.items())
                vertices.append(len(items))
                edges.append(edge_count)
                chain2s.append(chain2)
                max_hist[max((len(c) for c in comps), default=(1 if items else 0))] += 1
                shape_hist.update(shapes)
                windows += 1
        print(
            P,
            args.C,
            L,
            windows,
            f'{mean(vertices):.3f}',
            f'{mean(edges):.5f}',
            f'{mean(chain2s):.6f}',
            f'{sum(1 for x in chain2s if x>0)/windows:.6f}',
            dict(sorted(max_hist.items())),
            shape_hist.most_common(8),
        )


if __name__ == '__main__':
    main()
