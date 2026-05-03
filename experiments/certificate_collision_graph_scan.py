#!/usr/bin/env python3
"""扫描局部窗口中粗合数证书的共享因子碰撞图。

用法示例：
  python3 experiments/certificate_collision_graph_scan.py --Ps 503,1009 --C 4

图模型：
  顶点 = 窗口中的粗半素数/粗三因子证书，类型为 R/U/T；
  边 = 两个证书共享同一个 >sqrt(P) 的素因子。
目标：检验混合 cumulant 中真正危险的连通高阶图是否稀疏。
"""
import argparse
import math
from collections import Counter, defaultdict
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def certs_in_row(P, row, flags, plist, small, B, L):
    """返回一行内全部粗合数证书：(列, 类型, 因子元组)。"""
    certs = []
    for c in range(1, P + 1):
        n = (row - 1) * P + c
        if not all(n % q for q in small):
            continue
        if flags[n]:
            continue
        fac = tuple(factor_distinct(n, plist))
        if not fac or not all(q > B for q in fac):
            continue
        if len(fac) == 2:
            typ = 'R' if min(fac) <= L else 'U'
            certs.append((c, typ, fac))
        elif len(fac) == 3:
            certs.append((c, 'T', fac))
    return certs


def graph_stats(items):
    """计算共享因子图的连通分量与边型。"""
    n = len(items)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    factor_to_vertices = defaultdict(list)
    for idx, (_, _, fac) in enumerate(items):
        for q in fac:
            factor_to_vertices[q].append(idx)

    edge_types = Counter()
    shared_factors = 0
    for verts in factor_to_vertices.values():
        if len(verts) < 2:
            continue
        shared_factors += 1
        for i in range(len(verts)):
            for j in range(i + 1, len(verts)):
                a, b = verts[i], verts[j]
                union(a, b)
                ta, tb = items[a][1], items[b][1]
                edge_types[''.join(sorted(ta + tb))] += 1

    comps = defaultdict(list)
    for idx in range(n):
        comps[find(idx)].append(idx)
    comp_shapes = []
    for verts in comps.values():
        if len(verts) < 2:
            continue
        type_count = Counter(items[v][1] for v in verts)
        shape = ''.join(f'{k}{type_count[k]}' for k in sorted(type_count))
        comp_shapes.append((len(verts), shape))
    comp_shapes.sort(reverse=True)
    max_comp = comp_shapes[0][0] if comp_shapes else 1 if n else 0
    return {
        'vertices': n,
        'edges': sum(edge_types.values()),
        'shared_factors': shared_factors,
        'max_comp': max_comp,
        'nontrivial_comps': len(comp_shapes),
        'edge_types': edge_types,
        'comp_shapes': comp_shapes,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    print('P C L windows meanV meanEdges edgePerV sharedFactorRate maxCompHist shapeTop edgeTypes')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        small = primes(sieve(B), B)
        step = max(1, L // 8)
        stats = []
        shape_hist = Counter()
        edge_types = Counter()
        max_hist = Counter()
        for row in range(1, P + 1):
            certs = certs_in_row(P, row, flags, plist, small, B, L)
            for start in range(1, P - L + 2, step):
                end = start + L - 1
                items = [x for x in certs if start <= x[0] <= end]
                st = graph_stats(items)
                stats.append(st)
                max_hist[st['max_comp']] += 1
                edge_types.update(st['edge_types'])
                for shape in st['comp_shapes']:
                    shape_hist[shape] += 1
        mean_v = mean(st['vertices'] for st in stats)
        mean_e = mean(st['edges'] for st in stats)
        mean_shared = mean(st['shared_factors'] for st in stats)
        edge_per_v = mean_e / mean_v if mean_v else 0.0
        shape_top = shape_hist.most_common(8)
        print(
            P,
            args.C,
            L,
            len(stats),
            f'{mean_v:.3f}',
            f'{mean_e:.4f}',
            f'{edge_per_v:.5f}',
            f'{mean_shared:.4f}',
            dict(sorted(max_hist.items())),
            shape_top,
            dict(edge_types),
        )


if __name__ == '__main__':
    main()
