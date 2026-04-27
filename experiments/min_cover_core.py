#!/usr/bin/env python3
"""首段满覆盖的最小覆盖核心分析。

目标：给定素数 P、剩余类 a、前缀长度 R，研究固定锚点同余族
    r ≡ -a P^{-1} (mod q), q<=sqrt(a+(R-1)P)
覆盖 [0,R) 时，真正需要多少个 q。

如果满覆盖必须依赖很多互相独立的 q，则可作为后续“供需/刚性矛盾”的精确对象。

用法示例：
    python3 experiments/min_cover_core.py --P 461 --a 22 --R 81 --detail
    python3 experiments/min_cover_core.py --scan --maxP 2000 --top 20
"""
import argparse
import math
from functools import lru_cache

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r


def masks_for(P, a, R):
    Q = math.isqrt(a + (R - 1) * P)
    rows = []
    full = (1 << R) - 1
    point_to_q = [[] for _ in range(R)]
    for q in primes_upto(min(P, Q)):
        if q == P:
            continue
        b = (-a * pow(P, -1, q)) % q
        mask = 0
        count = 0
        for r in range(b, R, q):
            mask |= 1 << r
            count += 1
            point_to_q[r].append(q)
        if mask:
            rows.append({'q': q, 'b': b, 'mask': mask, 'count': count})
    covered = 0
    for row in rows:
        covered |= row['mask']
    return Q, rows, point_to_q, full, covered


def greedy_upper(rows, full):
    uncovered = full
    chosen = []
    while uncovered:
        best = max(rows, key=lambda row: (row['mask'] & uncovered).bit_count())
        gain = (best['mask'] & uncovered).bit_count()
        if gain == 0:
            return None
        chosen.append(best['q'])
        uncovered &= ~best['mask']
    return chosen


def exact_min_cover(rows, point_to_q, full, time_node_limit=500000):
    q_to_row = {row['q']: row for row in rows}
    upper = greedy_upper(rows, full)
    if upper is None:
        return None, None, 0, False
    best = {'size': len(upper), 'chosen': upper[:], 'nodes': 0, 'complete': True}

    # 每个点按候选 q 的覆盖规模从大到小排序，优先强覆盖。
    cand_by_point = []
    for qs in point_to_q:
        cand_by_point.append(sorted(qs, key=lambda q: -q_to_row[q]['count']))

    suffix_max_gain = max((row['count'] for row in rows), default=1)

    def lower_bound(uncovered):
        # 粗下界：剩余点数 / 当前最大单模覆盖点数。
        return math.ceil(uncovered.bit_count() / max(1, suffix_max_gain))

    def choose_point(uncovered):
        # 选候选数最少的未覆盖点；这是满覆盖刚性的瓶颈点。
        best_r = None
        best_len = 10**9
        tmp = uncovered
        while tmp:
            low = tmp & -tmp
            r = low.bit_length() - 1
            ln = len(cand_by_point[r])
            if ln < best_len:
                best_r, best_len = r, ln
                if ln == 1:
                    break
            tmp ^= low
        return best_r

    def dfs(uncovered, chosen):
        best['nodes'] += 1
        if best['nodes'] > time_node_limit:
            best['complete'] = False
            return
        if not uncovered:
            if len(chosen) < best['size']:
                best['size'] = len(chosen)
                best['chosen'] = chosen[:]
            return
        if len(chosen) + lower_bound(uncovered) >= best['size']:
            return
        r = choose_point(uncovered)
        for q in cand_by_point[r]:
            row = q_to_row[q]
            new_uncovered = uncovered & ~row['mask']
            if new_uncovered == uncovered:
                continue
            dfs(new_uncovered, chosen + [q])

    dfs(full, [])
    return best['size'], best['chosen'], best['nodes'], best['complete']


def record(P, a, R=None):
    if R is None:
        flags = sieve(P * P)
        R = first_prime_r(P, a, flags)
    Q, rows, point_to_q, full, covered = masks_for(P, a, R)
    if covered != full:
        return {'P': P, 'a': a, 'R': R, 'Q': Q, 'covered': False}
    min_size, chosen, nodes, complete = exact_min_cover(rows, point_to_q, full)
    forced_points = [r for r, qs in enumerate(point_to_q) if len(qs) == 1]
    chosen_set = set(chosen or [])
    core_rows = [row for row in rows if row['q'] in chosen_set]
    core_hits = sum(row['count'] for row in core_rows)
    return {
        'P': P, 'a': a, 'R': R, 'Q': Q, 'covered': True,
        'q_count': len(rows), 'min_size': min_size, 'chosen': chosen or [],
        'nodes': nodes, 'complete': complete,
        'forced_points': forced_points,
        'forced_count': len(forced_points),
        'core_hits': core_hits,
        'core_excess': core_hits - R,
        'rows': rows,
        'point_degree_min': min(len(qs) for qs in point_to_q),
        'point_degree_max': max(len(qs) for qs in point_to_q),
    }


def print_record(rec, detail=False):
    if not rec['covered']:
        print(f"P={rec['P']},a={rec['a']},R={rec['R']},Q={rec['Q']},not_covered")
        return
    print(
        f"P={rec['P']},a={rec['a']},R={rec['R']},Q={rec['Q']},q_count={rec['q_count']},"
        f"min_core={rec['min_size']},core_hits={rec['core_hits']},core_excess={rec['core_excess']},"
        f"forced_points={rec['forced_count']},degree=[{rec['point_degree_min']},{rec['point_degree_max']}],"
        f"nodes={rec['nodes']},complete={rec['complete']}"
    )
    print('chosen_core=', rec['chosen'])
    if detail:
        chosen = set(rec['chosen'])
        print('core_rows(q,b,count)=', [(row['q'], row['b'], row['count']) for row in rec['rows'] if row['q'] in chosen])
        print('forced_points=', rec['forced_points'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--a', type=int, default=22)
    ap.add_argument('--R', type=int, default=0)
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--maxP', type=int, default=2000)
    ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()

    if args.scan:
        flags = sieve(args.maxP * args.maxP)
        out = []
        for P in primes_upto(args.maxP):
            if P < 3:
                continue
            worst_a, worst_R = 1, -1
            for a in range(1, P + 1):
                r0 = first_prime_r(P, a, flags)
                if r0 is not None and r0 > worst_R:
                    worst_a, worst_R = a, r0
            if worst_R > 0:
                out.append(record(P, worst_a, worst_R))
        out.sort(key=lambda x: (-x.get('R', 0), -x.get('min_size', 0)))
        for rec in out[:args.top]:
            print_record(rec, detail=False)
    else:
        R = args.R or None
        print_record(record(args.P, args.a, R), detail=args.detail)


if __name__ == '__main__':
    main()
