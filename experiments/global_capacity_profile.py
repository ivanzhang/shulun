#!/usr/bin/env python3
"""全局 B11 洞集容量剖面。

对所有 c mod 2310 与给定 T，计算实际洞集容量 cap_H(q)，并统计：
- 达到给定 saving 所需的最小 m 的最大/最小/分布；
- 最坏模板的 cap 排列；
- 对目标 cover 比例 theta 的 Lmin 下界。

用法示例：
    python3 experiments/global_capacity_profile.py --T 30 --theta 0.5 --X 10000000 --show 10
    python3 experiments/global_capacity_profile.py --Tlist 20,25,30,35 --theta 0.5 --X 10000000
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import M, holes_for_c
from slope_capacity_lift_bound import capacity_profile, min_m_by_actual_capacity, first_available_product, anchor_expectation_bound


def target_cover(T, theta):
    """目标 cover 上限，按 floor(theta*T)。"""
    return math.floor(theta * T)


def scan_T(T, theta, X, show):
    cover = target_cover(T, theta)
    S = T - cover
    rows = []
    hist_m = Counter()
    impossible = 0
    for c in range(M):
        holes = holes_for_c(c, T)
        profile = capacity_profile(holes)
        m, cap, used = min_m_by_actual_capacity(profile, S)
        if m is None:
            impossible += 1
            continue
        Lmin, qs = first_available_product(m)
        expect = anchor_expectation_bound(X, Lmin)
        hist_m[m] += 1
        rows.append({
            'c': c,
            'T': T,
            'cover': cover,
            'saving': S,
            'm': m,
            'cap': cap,
            'Lmin': Lmin,
            'log10L': math.log10(Lmin),
            'expect': expect,
            'used': used,
            'qs': qs,
            'holes': holes,
            'profile_top': sorted(profile, key=lambda x: (-x[1], x[0]))[:show],
        })
    rows.sort(key=lambda r: (r['m'], r['log10L'], r['c']))
    return cover, S, impossible, hist_m, rows


def print_T(T, theta, X, show):
    cover, S, impossible, hist_m, rows = scan_T(T, theta, X, show)
    if not rows:
        print('T', T, 'theta', theta, 'cover<=', cover, 'saving>=', S, 'all_impossible', impossible)
        return
    min_m = min(r['m'] for r in rows)
    max_m = max(r['m'] for r in rows)
    min_log = min(r['log10L'] for r in rows)
    max_expect = max(r['expect'] for r in rows)
    print('T', T, 'theta', theta, 'cover<=', cover, 'saving>=', S, 'impossible', impossible)
    print('m_hist', sorted(hist_m.items()), 'min_m', min_m, 'max_m', max_m, 'min_log10L', f'{min_log:.3f}', 'max_anchor_expect', f'{max_expect:.6g}')
    print('best_cases rank c m cap log10L expect profile_top holes')
    for rank, r in enumerate(rows[:show], 1):
        print(rank, r['c'], r['m'], r['cap'], f'{r["log10L"]:.3f}', f'{r["expect"]:.6g}', r['profile_top'], r['holes'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=30)
    parser.add_argument('--Tlist', default='')
    parser.add_argument('--theta', type=float, default=0.5)
    parser.add_argument('--X', type=int, default=10_000_000)
    parser.add_argument('--show', type=int, default=10)
    args = parser.parse_args()

    if args.Tlist:
        print('T theta cover saving impossible m_hist min_m min_log10L max_anchor_expect')
        for T in [int(x) for x in args.Tlist.split(',') if x.strip()]:
            cover, S, impossible, hist_m, rows = scan_T(T, args.theta, args.X, args.show)
            if rows:
                min_m = min(r['m'] for r in rows)
                min_log = min(r['log10L'] for r in rows)
                max_expect = max(r['expect'] for r in rows)
                print(T, args.theta, cover, S, impossible, sorted(hist_m.items()), min_m, f'{min_log:.3f}', f'{max_expect:.6g}', flush=True)
            else:
                print(T, args.theta, cover, S, impossible, [], 'NA', 'NA', 'NA', flush=True)
        return

    print_T(args.T, args.theta, args.X, args.show)


if __name__ == '__main__':
    main()
