#!/usr/bin/env python3
"""三洞首次全补事件分析。

枚举 a 从 A_{R-1} 外首次进入 A_R，且 |B_y(a,R)|>=3 的事件。
输出洞位置、每洞补丁因子、共享、上一窗口未补洞，分析同余兼容条件。

用法示例：
    python3 experiments/three_hole_gain_analysis.py --P 461 --y 7 --Rmax 90 --detail
    python3 experiments/three_hole_gain_analysis.py --scan --maxP 1000 --y 7 --Rmax 100
"""
import argparse
from collections import Counter

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from a_space_candidate_decay import candidate_as
from positive_negative_congruence import stats_for_a
from hole_factor_constraints import record as factor_record


def events_for(P, y, Rmax):
    prev = set()
    events = []
    for R in range(1, Rmax + 1):
        cur_data = {a: (holes, patched, hits) for a, holes, patched, hits in candidate_as(P, R, y)}
        cur = set(cur_data)
        for a in sorted(cur - prev):
            holes = cur_data[a][0]
            if holes >= 3:
                prev_st = stats_for_a(P, a, R - 1, y) if R > 1 else None
                fr = factor_record(P, a, R, y)
                events.append({'P': P, 'y': y, 'R': R, 'a': a, 'holes': holes, 'hits': cur_data[a][2], 'prev': prev_st, 'fr': fr})
        prev = cur
    return events


def print_event(ev, detail=False):
    fr = ev['fr']
    print(f"P={ev['P']},y={ev['y']},R={ev['R']},a={ev['a']},holes={ev['holes']},hits={ev['hits']},Q={fr['Q']},prev_unpatched={ev['prev']['unpatched_list'] if ev['prev'] else []}")
    print('holes=', fr['holes'])
    print('patch_degree=', sorted(fr['patch_degree'].items()), 'shared=', [(q, rs) for q, rs, gaps, ok in fr['shared']])
    if detail:
        for row in fr['rows']:
            print(' r=', row['r'], 'n=', row['n'], 'patch=', row['patch'], 'fac=', row['fac'])
        print('gcd_edges=', fr['gcd_rows'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--y', type=int, default=7)
    ap.add_argument('--Rmax', type=int, default=90)
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--maxP', type=int, default=1000)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()

    if args.scan:
        flags = sieve(args.maxP * args.maxP)
        all_events = []
        for P in primes_upto(args.maxP):
            if P <= args.y:
                continue
            worst_R = -1
            for a in range(1, P + 1):
                r0 = first_prime_r(P, a, flags)
                if r0 is not None and r0 > worst_R:
                    worst_R = r0
            all_events.extend(events_for(P, args.y, min(args.Rmax, worst_R + 5)))
        print(f"total_events={len(all_events)}")
        cnt = Counter((ev['holes'], ev['R']) for ev in all_events)
        print('hole_count_counter=', Counter(ev['holes'] for ev in all_events).most_common())
        for ev in sorted(all_events, key=lambda e: (-e['R'], e['P'], e['a']))[:50]:
            print_event(ev, detail=False)
        return

    evs = events_for(args.P, args.y, args.Rmax)
    print(f"P={args.P},y={args.y},events={len(evs)}")
    for ev in evs:
        print_event(ev, detail=args.detail)

if __name__ == '__main__':
    main()
