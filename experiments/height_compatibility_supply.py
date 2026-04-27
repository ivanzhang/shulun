#!/usr/bin/env python3
"""加入“r 必须是锚点前 K 个小骨架洞”的高度兼容供给统计。

用法示例：
  python3 experiments/height_compatibility_supply.py --P 997 --K 20
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from shared_patch_energy import front_holes


def prime_anchors(P, A):
    """边界锚点除 a=P 外即第一行素数短区间。"""
    flags = sieve(P)
    return [a for a in range(A + 1, P) if flags[a]]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=997)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=20)
    parser.add_argument('--top', type=int, default=15)
    args = parser.parse_args()

    anchors = prime_anchors(args.P, args.A)
    anchor_holes = {a: front_holes(args.P, a, args.y, args.K) for a in anchors}
    max_r = max(r for holes in anchor_holes.values() for r in holes)
    Q = math.isqrt((args.P - 1) + max_r * args.P)
    primes = [q for q in primes_upto(Q) if q > args.y and q != args.P]

    compatible_supply = 0
    actual_hits = 0
    by_q_supply = defaultdict(int)
    by_q_hits = defaultdict(int)
    for q in primes:
        for a, holes in anchor_holes.items():
            for r in holes:
                if (a + r * args.P) % q == 0:
                    compatible_supply += 1
                    by_q_supply[q] += 1
                    # 这里只计兼容命中；它是否真为合数补丁取决于 n 是否还有更小因子。
                    actual_hits += 1
                    by_q_hits[q] += 1

    print('P', args.P, 'N', len(anchors), 'K', args.K, 'max_r', max_r, 'Q', Q, 'q_count', len(primes))
    print('compatible_supply', compatible_supply, 'per_hole', f'{compatible_supply/(len(anchors)*args.K):.3f}')
    print('top_q_supply q supply')
    for q, v in sorted(by_q_supply.items(), key=lambda kv: (-kv[1], kv[0]))[:args.top]:
        print('top_q_supply', q, v)


if __name__ == '__main__':
    main()
