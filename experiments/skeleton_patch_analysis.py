#!/usr/bin/env python3
"""小素数骨架 + 大素数补丁分析。

首段满覆盖通常由 2,3,5,7,... 的小素数形成骨架，剩余空洞由较大 q 单点或少点补丁覆盖。
本脚本按阈值 y 拆分：
- skeleton: q<=y 覆盖的点；
- holes: 未被骨架覆盖的点；
- patch q: q>y 对 holes 的覆盖贡献。
寻找“补丁需求”与“可用大模数锚点命中”的精确关系。

用法示例：
    python3 experiments/skeleton_patch_analysis.py --P 461 --a 22 --R 81 --ys 7,11,13,17,23,29 --detail
    python3 experiments/skeleton_patch_analysis.py --scan --maxP 2000 --y 13 --top 20
"""
import argparse
import math
from collections import defaultdict, Counter

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r


def cover_rows(P, a, R):
    Q = math.isqrt(a + (R - 1) * P)
    rows = []
    for q in primes_upto(min(P, Q)):
        if q == P:
            continue
        b = (-a * pow(P, -1, q)) % q
        points = list(range(b, R, q))
        if points:
            rows.append((q, b, points))
    return Q, rows


def analyze(P, a, R, y):
    Q, rows = cover_rows(P, a, R)
    skeleton = set()
    for q, b, points in rows:
        if q <= y:
            skeleton.update(points)
    holes = sorted(set(range(R)) - skeleton)
    hole_set = set(holes)
    patch_by_q = []
    patch_by_hole = defaultdict(list)
    for q, b, points in rows:
        if q <= y:
            continue
        hit = [r for r in points if r in hole_set]
        if hit:
            patch_by_q.append((q, b, hit))
            for r in hit:
                patch_by_hole[r].append(q)
    deg = Counter(len(patch_by_hole[r]) for r in holes)
    single_patch_holes = [r for r in holes if len(patch_by_hole[r]) == 1]
    # 每个大 q 在短前缀里通常只命中 1 个洞；multi_patch 是真实共享补丁。
    multi_patch_q = [(q, hit) for q, b, hit in patch_by_q if len(hit) >= 2]
    return {
        'P': P, 'a': a, 'R': R, 'Q': Q, 'y': y,
        'skeleton_covered': len(skeleton), 'hole_count': len(holes), 'holes': holes,
        'patch_q_count': len(patch_by_q), 'patch_hits': sum(len(hit) for _, _, hit in patch_by_q),
        'degree_counter': deg, 'single_patch_holes': single_patch_holes,
        'single_patch_count': len(single_patch_holes), 'multi_patch_q': multi_patch_q,
        'patch_by_q': patch_by_q, 'patch_by_hole': patch_by_hole,
    }


def print_rec(rec, detail=False):
    print(
        f"P={rec['P']},a={rec['a']},R={rec['R']},Q={rec['Q']},y={rec['y']},"
        f"skeleton={rec['skeleton_covered']},holes={rec['hole_count']},"
        f"patch_q={rec['patch_q_count']},patch_hits={rec['patch_hits']},"
        f"single_holes={rec['single_patch_count']},deg={sorted(rec['degree_counter'].items())},"
        f"multi_q={len(rec['multi_patch_q'])}"
    )
    print('holes_first=', rec['holes'][:80])
    if detail:
        print('single_patch_holes=', rec['single_patch_holes'])
        print('multi_patch_q=', rec['multi_patch_q'][:50])
        print('patch_by_q=', [(q, hit) for q, b, hit in rec['patch_by_q'][:100]])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--a', type=int, default=22)
    ap.add_argument('--R', type=int, default=0)
    ap.add_argument('--y', type=int, default=13)
    ap.add_argument('--ys', type=str, default='')
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--maxP', type=int, default=2000)
    ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()

    if args.scan:
        flags = sieve(args.maxP * args.maxP)
        rows = []
        for P in primes_upto(args.maxP):
            if P < 3:
                continue
            worst_a, worst_R = 1, -1
            for a in range(1, P + 1):
                r0 = first_prime_r(P, a, flags)
                if r0 is not None and r0 > worst_R:
                    worst_a, worst_R = a, r0
            if worst_R > 0:
                rows.append(analyze(P, worst_a, worst_R, args.y))
        rows.sort(key=lambda x: (-x['R'], -x['hole_count']))
        for rec in rows[:args.top]:
            print_rec(rec, detail=False)
    else:
        R = args.R
        if not R:
            flags = sieve(args.P * args.P)
            R = first_prime_r(args.P, args.a, flags)
        ys = [int(x) for x in args.ys.split(',') if x] or [args.y]
        for y in ys:
            print_rec(analyze(args.P, args.a, R, y), detail=args.detail)


if __name__ == '__main__':
    main()
