#!/usr/bin/env python3
"""同一个 a 的正负同余兼容性实验。

固定 P,R,y，枚举 a：
- 负同余定义小骨架洞：对 p<=y，a != -rP mod p；
- 正同余定义补丁命中：存在 q>y, q<=sqrt(a+(R-1)P), a == -rP mod q。
统计洞数、被补洞数、未补洞数、补丁核心大小。

目标：寻找容量不等式，说明同一个 a 很难让所有洞都被正同余补上。

用法示例：
    python3 experiments/positive_negative_congruence.py --P 461 --R 81 --y 13 --detail-a 22
    python3 experiments/positive_negative_congruence.py --P 461 --R 81 --y 13 --top 20
    python3 experiments/positive_negative_congruence.py --scanP --maxP 1000 --y 13
"""
import argparse
import math
from collections import Counter

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from skeleton_patch_analysis import analyze as skeleton_analyze
from patch_set_cover_core import record as cover_record


def stats_for_a(P, a, R, y):
    sk = skeleton_analyze(P, a, R, y)
    holes = sk['holes']
    patched = [r for r in holes if sk['patch_by_hole'].get(r)]
    unpatched = [r for r in holes if not sk['patch_by_hole'].get(r)]
    patch_hits = sk['patch_hits']
    patch_q = sk['patch_q_count']
    cover_core = None
    if holes and not unpatched:
        cover_core = cover_record(P, a, R, y)['cover_size']
    return {
        'P': P, 'a': a, 'R': R, 'y': y, 'Q': sk['Q'],
        'holes': len(holes), 'patched': len(patched), 'unpatched': len(unpatched),
        'patch_hits': patch_hits, 'patch_q': patch_q, 'cover_core': cover_core,
        'hole_list': holes, 'unpatched_list': unpatched,
        'ratio': len(patched) / len(holes) if holes else 1.0,
    }


def enumerate_a(P, R, y):
    rows = [stats_for_a(P, a, R, y) for a in range(1, P + 1)]
    return rows


def summarize(rows):
    full = [x for x in rows if x['holes'] > 0 and x['unpatched'] == 0]
    nontrivial = [x for x in rows if x['holes'] > 0]
    hole_counter = Counter(x['holes'] for x in nontrivial)
    unpatched_counter = Counter(x['unpatched'] for x in nontrivial)
    max_ratio = max((x['ratio'] for x in nontrivial), default=0)
    max_patched = max((x['patched'] for x in nontrivial), default=0)
    return {
        'count': len(rows), 'nontrivial': len(nontrivial), 'full_count': len(full),
        'full': full, 'hole_counter': hole_counter, 'unpatched_counter': unpatched_counter,
        'max_ratio': max_ratio, 'max_patched': max_patched,
    }


def print_row(x):
    print(
        f"a={x['a']},R={x['R']},Q={x['Q']},holes={x['holes']},patched={x['patched']},"
        f"unpatched={x['unpatched']},ratio={x['ratio']:.3f},patch_hits={x['patch_hits']},"
        f"patch_q={x['patch_q']},cover_core={x['cover_core']}"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--R', type=int, default=81)
    ap.add_argument('--y', type=int, default=13)
    ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--detail-a', type=int, default=0)
    ap.add_argument('--scanP', action='store_true')
    ap.add_argument('--maxP', type=int, default=1000)
    args = ap.parse_args()

    if args.detail_a:
        x = stats_for_a(args.P, args.detail_a, args.R, args.y)
        print_row(x)
        print('holes=', x['hole_list'])
        print('unpatched=', x['unpatched_list'])
        return

    if args.scanP:
        flags = sieve(args.maxP * args.maxP)
        for P in primes_upto(args.maxP):
            if P < 3:
                continue
            worst_a, worst_R = 1, -1
            for a in range(1, P + 1):
                r0 = first_prime_r(P, a, flags)
                if r0 is not None and r0 > worst_R:
                    worst_a, worst_R = a, r0
            rows = enumerate_a(P, worst_R, args.y)
            sm = summarize(rows)
            print(
                f"P={P},R={worst_R},worst_a={worst_a},full_count={sm['full_count']},"
                f"max_patched={sm['max_patched']},max_ratio={sm['max_ratio']:.3f},"
                f"unpatched0={sm['unpatched_counter'].get(0,0)},unpatched1={sm['unpatched_counter'].get(1,0)}"
            )
        return

    rows = enumerate_a(args.P, args.R, args.y)
    sm = summarize(rows)
    print(
        f"P={args.P},R={args.R},y={args.y},a_count={sm['count']},nontrivial={sm['nontrivial']},"
        f"full_count={sm['full_count']},max_patched={sm['max_patched']},max_ratio={sm['max_ratio']:.3f}"
    )
    print('hole_counter_top=', sm['hole_counter'].most_common(12))
    print('unpatched_counter_top=', sm['unpatched_counter'].most_common(12))
    rows.sort(key=lambda x: (x['unpatched'], -x['holes'], -x['patched']))
    for x in rows[:args.top]:
        print_row(x)


if __name__ == '__main__':
    main()
