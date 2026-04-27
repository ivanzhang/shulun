#!/usr/bin/env python3
"""单点化后尾部灭绝剖面。

思想：对每条证书路径追踪不同补丁模数乘积 M。第一次 M>P 时，路径在列锚点 a∈[1,P)
范围内已经被 CRT 固定为至多一个候选点；随后统计它还继续幸存多少个洞步。

用法示例：
  python3 experiments/post_singleton_extinction_profile.py --P 64007 --K 30 --y 11
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_primes(n, y, P):
    """返回能证明 n 合数的补丁素数。"""
    root = math.isqrt(n)
    return [q for q, _ in factor(n) if q > y and q <= root and q != P]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=64007)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=30)
    parser.add_argument('--top', type=int, default=20)
    args = parser.parse_args()

    records = []
    total_paths = 0
    singleton_paths = 0
    for group in template_groups(args.P, args.A, args.y, args.K):
        states = [(a, (), None) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            new_states = []
            for a, path, singleton_at in states:
                patches = patch_primes(a + r * args.P, args.y, args.P)
                if patches:
                    q = min(patches)
                    new_path = path + (q,)
                    new_singleton_at = singleton_at
                    if new_singleton_at is None:
                        modulus = math.prod(set(new_path))
                        if modulus > args.P:
                            new_singleton_at = idx
                    new_states.append((a, new_path, new_singleton_at))
                else:
                    if path:
                        total_paths += 1
                        if singleton_at is not None:
                            singleton_paths += 1
                            records.append((idx - singleton_at, singleton_at, idx, a, path, group['pattern']))
            states = new_states
        for a, path, singleton_at in states:
            if path:
                total_paths += 1
                if singleton_at is not None:
                    singleton_paths += 1
                    records.append((args.K + 1 - singleton_at, singleton_at, args.K + 1, a, path, group['pattern']))

    tail_hist = Counter(tail for tail, *_ in records)
    by_singleton = Counter(singleton_at for _, singleton_at, *_ in records)
    worst = sorted(records, reverse=True)[:args.top]

    print('P', args.P, 'K', args.K, 'y', args.y, 'total_paths', total_paths, 'singleton_paths', singleton_paths)
    print('tail_after_singleton_hist')
    for tail, count in sorted(tail_hist.items()):
        print(tail, count)
    print('singleton_at_hist')
    for step, count in sorted(by_singleton.items()):
        print(step, count)
    print('worst tail singleton_at death a len distinct repeats pattern path')
    for tail, singleton_at, death, a, path, pattern in worst:
        distinct = len(set(path))
        print(tail, singleton_at, death, a, len(path), distinct, len(path) - distinct, pattern, path)


if __name__ == '__main__':
    main()
