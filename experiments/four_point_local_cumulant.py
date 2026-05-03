#!/usr/bin/env python3
"""分析四点中心化局部因子在不同模 q 碰撞分割下的结构。"""
import argparse
import itertools
from collections import defaultdict


def set_partitions(n):
    parts = []
    def rec(i, blocks):
        if i == n:
            parts.append(tuple(tuple(b) for b in blocks))
            return
        for b in blocks:
            b.append(i); rec(i+1, blocks); b.pop()
        blocks.append([i]); rec(i+1, blocks); blocks.pop()
    rec(0, [])
    return parts


def canon_residues(part):
    res = [None] * 4
    for j, block in enumerate(part):
        for i in block:
            res[i] = j
    return tuple(res)


def nu_for_subset(res, mask):
    vals = {res[i] for i in range(4) if (mask >> i) & 1}
    return len(vals)


def local_centered_factor(q, res):
    p = 1 - 1 / q
    total = 0.0
    for mask in range(16):
        k = mask.bit_count()
        nu = nu_for_subset(res, mask)
        prob = 1 - nu / q
        total += ((-p) ** (4 - k)) * prob
    return total


def local_joint_prob(q, res):
    nu = len(set(res))
    return 1 - nu / q


def block_sizes(part):
    return tuple(sorted([len(b) for b in part], reverse=True))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--qs', default='5,7,11,101')
    args = ap.parse_args()
    qs = [int(x) for x in args.qs.split(',')]
    grouped = defaultdict(list)
    for part in set_partitions(4):
        grouped[block_sizes(part)].append(canon_residues(part))
    print('pattern count q localCumulantScaledBy q^k samples')
    for pat, ress in sorted(grouped.items(), key=lambda kv: (len(kv[0]), kv[0])):
        print(f'pattern={pat} count={len(ress)}')
        for q in qs:
            vals = [local_centered_factor(q, res) for res in ress]
            # 猜测尺度：独立 distinct 为 0；碰撞越强阶越大，统一输出 q^4 缩放。
            scaled = [v * (q ** 4) for v in vals]
            print(' q', q, 'mean', f'{sum(vals)/len(vals):.8g}', 'q4mean', f'{sum(scaled)/len(scaled):.8g}', 'valsQ4', ','.join(f'{x:.4g}' for x in scaled[:6]))


if __name__ == '__main__':
    main()
