#!/usr/bin/env python3
"""候选集合块收缩统计。

A_R 不是单调集合：增加 R 时，新的高度可能改变 Q，引入新补丁，也可能让某些 a 新出现洞/补洞。
本脚本按高度块统计：
- A_R 大小；
- 与前一步相比 lost/gained/stayed；
- 块内最大反弹；
- 是否存在从某个 R0 后单调下降或准单调下降。

用法示例：
    python3 experiments/candidate_block_contraction.py --P 461 --y 13 --Rmax 100 --block 5
    python3 experiments/candidate_block_contraction.py --scan --maxP 1000 --y 13 --block 5
"""
import argparse
from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from a_space_candidate_decay import candidate_as


def sizes_for(P, y, Rmax):
    prev = set()
    rows = []
    sets = {}
    for R in range(1, Rmax + 1):
        aset = {a for a, *_ in candidate_as(P, R, y)}
        lost = prev - aset
        gained = aset - prev
        stayed = prev & aset
        rows.append({'R': R, 'size': len(aset), 'lost': len(lost), 'gained': len(gained), 'stayed': len(stayed), 'aset': aset})
        sets[R] = aset
        prev = aset
    return rows, sets


def block_summary(rows, block):
    out = []
    for i in range(0, len(rows), block):
        chunk = rows[i:i+block]
        if not chunk:
            continue
        start, end = chunk[0], chunk[-1]
        max_size = max(x['size'] for x in chunk)
        min_size = min(x['size'] for x in chunk)
        total_lost = sum(x['lost'] for x in chunk)
        total_gained = sum(x['gained'] for x in chunk)
        out.append({
            'R0': start['R'], 'R1': end['R'], 'start_size': start['size'], 'end_size': end['size'],
            'max_size': max_size, 'min_size': min_size,
            'total_lost': total_lost, 'total_gained': total_gained,
            'net': end['size'] - start['size'],
        })
    return out


def first_event(rows, predicate):
    for row in rows:
        if predicate(row):
            return row['R']
    return None


def analyze(P, y, Rmax, block):
    rows, sets = sizes_for(P, y, Rmax)
    blocks = block_summary(rows, block)
    zero_R = first_event(rows, lambda x: x['size'] == 0)
    one_R = first_event(rows, lambda x: x['size'] <= 1)
    # 找最后一次增长后的位置
    last_gain_R = max((x['R'] for x in rows if x['gained'] > 0), default=None)
    last_increase_R = max((rows[i]['R'] for i in range(1, len(rows)) if rows[i]['size'] > rows[i-1]['size']), default=None)
    return {'P': P, 'y': y, 'Rmax': Rmax, 'rows': rows, 'blocks': blocks, 'zero_R': zero_R, 'one_R': one_R, 'last_gain_R': last_gain_R, 'last_increase_R': last_increase_R}


def print_analysis(an, detail=False):
    print(f"P={an['P']},y={an['y']},Rmax={an['Rmax']},one_R={an['one_R']},zero_R={an['zero_R']},last_gain_R={an['last_gain_R']},last_increase_R={an['last_increase_R']}")
    print('blocks: R0-R1 start end min max lost gained net')
    for b in an['blocks']:
        print(f"{b['R0']}-{b['R1']} {b['start_size']} {b['end_size']} {b['min_size']} {b['max_size']} {b['total_lost']} {b['total_gained']} {b['net']}")
    if detail:
        print('steps: R size lost gained stayed')
        for x in an['rows']:
            print(x['R'], x['size'], x['lost'], x['gained'], x['stayed'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--y', type=int, default=13)
    ap.add_argument('--Rmax', type=int, default=100)
    ap.add_argument('--block', type=int, default=5)
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--maxP', type=int, default=1000)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()
    if args.scan:
        flags = sieve(args.maxP * args.maxP)
        for P in primes_upto(args.maxP):
            if P < 47:
                continue
            worst_R = -1
            for a in range(1, P + 1):
                r0 = first_prime_r(P, a, flags)
                if r0 is not None and r0 > worst_R:
                    worst_R = r0
            an = analyze(P, args.y, min(args.Rmax, worst_R + 5), args.block)
            print(f"P={P},worst_R={worst_R},one_R={an['one_R']},zero_R={an['zero_R']},last_increase={an['last_increase_R']},last_gain={an['last_gain_R']}")
    else:
        print_analysis(analyze(args.P, args.y, args.Rmax, args.block), detail=args.detail)

if __name__ == '__main__':
    main()
