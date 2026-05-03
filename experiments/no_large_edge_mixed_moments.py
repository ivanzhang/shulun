#!/usr/bin/env python3
"""隔离无粗共享边窗口后的 H,R,U,T 混合矩。

若 E-large 已排除粗因子连通图，则剩余 E-small 应只由小模数筛条件产生。
本脚本比较所有窗口与无粗共享边窗口的相关/混合矩。

用法示例：
  python3 experiments/no_large_edge_mixed_moments.py --Ps 503,1009,2003 --C 4
"""
import argparse
import math
from statistics import mean
from collections import defaultdict

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct
from local_cross_cumulant_scan import corr, standardized_mixed, cov


def row_data(P, row, flags, plist, small, B, L):
    vals = []
    for c in range(1, P + 1):
        n = (row - 1) * P + c
        item = {'H': 0, 'R': 0, 'U': 0, 'T': 0, 'fac': ()}
        if all(n % q for q in small):
            item['H'] = 1
            if not flags[n]:
                fac = tuple(q for q in factor_distinct(n, plist) if q > B)
                item['fac'] = fac
                if len(fac) == 2:
                    item['R' if min(fac) <= L else 'U'] = 1
                elif len(fac) == 3:
                    item['T'] = 1
        vals.append(item)
    return vals


def has_large_edge(items):
    seen = {}
    for item in items:
        for q in item['fac']:
            if q in seen:
                return True
            seen[q] = True
    return False


def summarize(label, samples):
    names = ('H', 'R', 'U', 'T')
    if not samples['H']:
        return f'{label} empty'
    mixed = standardized_mixed(samples, names)
    max_abs_m3 = max(abs(v) for k, v in mixed.items() if k.startswith('m3_'))
    return ' '.join([
        label,
        f'n={len(samples["H"])}',
        'means=' + ','.join(f'{mean(samples[x]):.3f}' for x in names),
        'vars=' + ','.join(f'{cov(samples[x], samples[x]):.3f}' for x in names),
        f'corrHR={corr(samples["H"], samples["R"]):.3f}',
        f'corrHU={corr(samples["H"], samples["U"]):.3f}',
        f'corrRU={corr(samples["R"], samples["U"]):.3f}',
        f'm4HHRR={mixed["m4_HHRR"]:.3f}',
        f'm4HHUU={mixed["m4_HHUU"]:.3f}',
        f'm4RRUU={mixed["m4_RRUU"]:.3f}',
        f'maxAbsM3={max_abs_m3:.3f}',
    ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        B = math.isqrt(P)
        L = max(1, int(args.C * math.sqrt(P)))
        flags = sieve(P * P + P)
        plist = primes(flags, P * P + P)
        small = primes(sieve(B), B)
        step = max(1, L // 8)
        all_samples = {name: [] for name in ('H', 'R', 'U', 'T')}
        noedge_samples = {name: [] for name in ('H', 'R', 'U', 'T')}
        edge_windows = 0
        total_windows = 0
        for row in range(1, P + 1):
            data = row_data(P, row, flags, plist, small, B, L)
            pref = {name: [0] * (P + 1) for name in all_samples}
            for idx, item in enumerate(data, start=1):
                for name in all_samples:
                    pref[name][idx] = pref[name][idx - 1] + item[name]
            for start in range(1, P - L + 2, step):
                end = start + L - 1
                total_windows += 1
                window_items = data[start - 1:end]
                edge = has_large_edge(window_items)
                if edge:
                    edge_windows += 1
                for name in all_samples:
                    val = pref[name][end] - pref[name][start - 1]
                    all_samples[name].append(val)
                    if not edge:
                        noedge_samples[name].append(val)
        print(f'P={P} C={args.C} L={L} edgeWindows={edge_windows}/{total_windows} edgeRate={edge_windows/total_windows:.5f}')
        print(summarize('all', all_samples))
        print(summarize('noEdge', noedge_samples))


if __name__ == '__main__':
    main()
