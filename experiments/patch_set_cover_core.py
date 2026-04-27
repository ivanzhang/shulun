#!/usr/bin/env python3
"""补丁集合覆盖核心。

既然专属匹配不总是有缺口，就计算覆盖小骨架洞集所需的最少补丁素数数量。
这是真正的补丁需求下界：若要满覆盖，至少需要 tau(B) 个中等素数补丁。

用法示例：
    python3 experiments/patch_set_cover_core.py --P 461 --a 22 --R 81 --y 13 --detail
    python3 experiments/patch_set_cover_core.py --scan --maxP 2000 --y 13 --top 20
"""
import argparse
import math

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from hole_factor_constraints import record as factor_record


def min_set_cover(left_to_right):
    holes = sorted(left_to_right)
    hidx = {r: i for i, r in enumerate(holes)}
    qmask = {}
    for r, qs in left_to_right.items():
        for q in qs:
            qmask[q] = qmask.get(q, 0) | (1 << hidx[r])
    full = (1 << len(holes)) - 1
    qs = sorted(qmask, key=lambda q: (-qmask[q].bit_count(), q))
    best = {'size': len(holes) + 1, 'chosen': [], 'nodes': 0}

    # 后缀可覆盖剪枝
    suffix = [0] * (len(qs) + 1)
    for i in range(len(qs) - 1, -1, -1):
        suffix[i] = suffix[i + 1] | qmask[qs[i]]

    def dfs(i, covered, chosen):
        best['nodes'] += 1
        if covered == full:
            if len(chosen) < best['size']:
                best['size'] = len(chosen)
                best['chosen'] = chosen[:]
            return
        if i == len(qs) or len(chosen) >= best['size']:
            return
        if (covered | suffix[i]) != full:
            return
        # 简单下界：剩余点 / 最大新增覆盖
        remaining = (full ^ (covered & full)).bit_count()
        max_gain = max(((qmask[qs[j]] & ~covered).bit_count() for j in range(i, len(qs))), default=1)
        if len(chosen) + math.ceil(remaining / max(1, max_gain)) >= best['size']:
            return
        q = qs[i]
        # 先选有新增的 q
        if qmask[q] & ~covered:
            dfs(i + 1, covered | qmask[q], chosen + [q])
        dfs(i + 1, covered, chosen)

    dfs(0, 0, [])
    return best['size'], best['chosen'], best['nodes'], {q: qmask[q] for q in qmask}, holes


def record(P, a, R, y):
    fr = factor_record(P, a, R, y)
    left_to_right = {row['r']: sorted(set(row['patch'])) for row in fr['rows']}
    size, chosen, nodes, qmask, holes = min_set_cover(left_to_right)
    chosen_hits = sum(qmask[q].bit_count() for q in chosen)
    return {
        **fr,
        'left_to_right': left_to_right,
        'cover_size': size,
        'chosen': chosen,
        'nodes': nodes,
        'chosen_hits': chosen_hits,
        'cover_excess': chosen_hits - len(holes),
        'holes': holes,
        'qmask': qmask,
    }


def print_record(rec, detail=False):
    print(
        f"P={rec['P']},a={rec['a']},R={rec['R']},y={rec['y']},holes={rec['hole_count']},"
        f"cover_core={rec['cover_size']},chosen_hits={rec['chosen_hits']},excess={rec['cover_excess']},"
        f"chosen={rec['chosen']}"
    )
    if detail:
        print('left_to_right=', rec['left_to_right'])
        for q in rec['chosen']:
            hit = [r for r in rec['holes'] if (rec['qmask'][q] >> rec['holes'].index(r)) & 1]
            print('q', q, 'hits', hit)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--a', type=int, default=22)
    ap.add_argument('--R', type=int, default=0)
    ap.add_argument('--y', type=int, default=13)
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
                out.append(record(P, worst_a, worst_R, args.y))
        out.sort(key=lambda x: (-x['R'], -x['cover_size']))
        for rec in out[:args.top]:
            print_record(rec, detail=False)
    else:
        R = args.R
        if not R:
            flags = sieve(args.P * args.P)
            R = first_prime_r(args.P, args.a, flags)
        print_record(record(args.P, args.a, R, args.y), detail=args.detail)


if __name__ == '__main__':
    main()
