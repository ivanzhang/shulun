#!/usr/bin/env python3
"""跨 P 扫描单点化尾部长度。

统计每个素数 P 下：证书路径何时满足不同补丁模数乘积 M>P，并记录单点化后还能继续
幸存多少个 B11 前洞。输出用于观察尾部长度是否按 log P 缓慢增长。

用法示例：
  python3 experiments/post_singleton_multiP_scan.py --Ps 8009,16001,32003,64007 --K 30 --y 11
"""
import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_primes(n, y, P):
    """返回能作为合数证书的补丁素数。"""
    root = math.isqrt(n)
    return [q for q, _ in factor(n) if q > y and q <= root and q != P]


def scan_one(P, A, y, K):
    """扫描单个 P，返回单点化尾部统计。"""
    total_paths = 0
    singleton_paths = 0
    max_tail = 0
    max_death = 0
    max_len = 0
    tail_hist = Counter()
    singleton_hist = Counter()
    worst = None

    for group in template_groups(P, A, y, K):
        states = [(a, (), None) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            next_states = []
            for a, path, singleton_at in states:
                patches = patch_primes(a + r * P, y, P)
                if not patches:
                    if path:
                        total_paths += 1
                        if singleton_at is not None:
                            singleton_paths += 1
                            tail = idx - singleton_at
                            tail_hist[tail] += 1
                            singleton_hist[singleton_at] += 1
                            record = (tail, singleton_at, idx, a, path, group['pattern'])
                            if worst is None or record > worst:
                                worst = record
                            max_tail = max(max_tail, tail)
                            max_death = max(max_death, idx)
                            max_len = max(max_len, len(path))
                    continue

                q = min(patches)
                new_path = path + (q,)
                new_singleton_at = singleton_at
                if new_singleton_at is None and math.prod(set(new_path)) > P:
                    new_singleton_at = idx
                next_states.append((a, new_path, new_singleton_at))
            states = next_states

        for a, path, singleton_at in states:
            if path:
                total_paths += 1
                if singleton_at is not None:
                    singleton_paths += 1
                    tail = K + 1 - singleton_at
                    tail_hist[tail] += 1
                    singleton_hist[singleton_at] += 1
                    record = (tail, singleton_at, K + 1, a, path, group['pattern'])
                    if worst is None or record > worst:
                        worst = record
                    max_tail = max(max_tail, tail)
                    max_death = max(max_death, K + 1)
                    max_len = max(max_len, len(path))

    return {
        'P': P,
        'total_paths': total_paths,
        'singleton_paths': singleton_paths,
        'max_tail': max_tail,
        'max_death': max_death,
        'max_len': max_len,
        'tail_hist': tail_hist,
        'singleton_hist': singleton_hist,
        'worst': worst,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='8009,16001,32003,64007')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=30)
    parser.add_argument('--detail', action='store_true')
    args = parser.parse_args()

    Ps = [int(x) for x in args.Ps.split(',') if x.strip()]
    print('P total singleton ratio max_tail max_death max_len logP tail/logP singleton_steps worst')
    for P in Ps:
        rec = scan_one(P, args.A, args.y, args.K)
        ratio = rec['singleton_paths'] / rec['total_paths'] if rec['total_paths'] else 0.0
        logP = math.log(P)
        worst = rec['worst']
        if worst:
            tail, singleton_at, death, a, path, pattern = worst
            worst_text = f'a={a},single={singleton_at},death={death},distinct={len(set(path))},repeats={len(path)-len(set(path))},pattern={pattern}'
        else:
            worst_text = '-'
        steps = ','.join(f'{k}:{v}' for k, v in sorted(rec['singleton_hist'].items()))
        print(P, rec['total_paths'], rec['singleton_paths'], f'{ratio:.3f}', rec['max_tail'], rec['max_death'], rec['max_len'], f'{logP:.3f}', f'{rec["max_tail"]/logP if logP else 0:.3f}', steps, worst_text)
        if args.detail:
            print('  tail_hist', sorted(rec['tail_hist'].items()))


if __name__ == '__main__':
    main()
