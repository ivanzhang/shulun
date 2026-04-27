#!/usr/bin/env python3
"""模板筛幸存集在补丁模 q 上的桶集中度。

用法示例：
  python3 experiments/survivor_residue_pseudorandom.py --P 4001 --K 10 --qmax 100
"""
import argparse
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from template_cover_sieve import template_groups, covered_by_patch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=4001)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=10)
    parser.add_argument('--qmax', type=int, default=120)
    args = parser.parse_args()

    groups = template_groups(args.P, args.A, args.y, args.K)
    step_sets = defaultdict(list)
    for group in groups:
        survivors = set(group['anchors'])
        step_sets[0].extend(survivors)
        for idx, r in enumerate(group['holes'], start=1):
            survivors = {a for a in survivors if covered_by_patch(args.P, a, r, args.y)}
            step_sets[idx].extend(survivors)

    print('P', args.P, 'K', args.K, 'qmax', args.qmax)
    print('step size worst_q max_bucket expected ratio additive')
    for step in range(0, args.K + 1):
        vals = step_sets[step]
        size = len(vals)
        if size == 0:
            print(step, 0, None, 0, 0, 0, 0)
            continue
        worst = None
        for q in primes_upto(args.qmax):
            if q <= args.y or q == args.P:
                continue
            counts = Counter(a % q for a in vals)
            max_bucket = max(counts.values(), default=0)
            expected = size / q
            ratio = max_bucket / expected if expected else 0
            additive = max_bucket - expected
            rec = (ratio, additive, q, max_bucket, expected)
            if worst is None or rec > worst:
                worst = rec
        ratio, additive, q, max_bucket, expected = worst
        print(step, size, q, max_bucket, f'{expected:.2f}', f'{ratio:.2f}', f'{additive:.2f}')


if __name__ == '__main__':
    main()
