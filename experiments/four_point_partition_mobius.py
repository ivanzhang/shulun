#!/usr/bin/env python3
"""用集合分割公式计算四阶 cumulant 的局部/全局组合系数。

目标：识别哪些碰撞图属于配对主项，哪些属于非配对 cumulant。
"""
import itertools
from collections import defaultdict


def partitions_of_set(items):
    items = list(items)
    if not items:
        yield []
        return
    first = items[0]
    for part in partitions_of_set(items[1:]):
        yield [[first]] + [b[:] for b in part]
        for i in range(len(part)):
            new = [b[:] for b in part]
            new[i].append(first)
            yield new


def cumulant_coeff(num_blocks):
    # κ(X1,...,Xn)=sum_partition (|π|-1)!(-1)^{|π|-1} prod_B E prod_{i in B}X_i
    import math
    return math.factorial(num_blocks - 1) * ((-1) ** (num_blocks - 1))


def canon_pattern(res):
    mapping = {}
    nxt = 0
    out = []
    for x in res:
        if x not in mapping:
            mapping[x] = nxt; nxt += 1
        out.append(mapping[x])
    sizes = sorted([out.count(i) for i in set(out)], reverse=True)
    return tuple(sizes)


def nu(res, block):
    return len({res[i] for i in block})


def joint_prob(q, res, block):
    return 1 - nu(res, block) / q


def cumulant4_joint(q, res):
    total = 0.0
    for part in partitions_of_set(range(4)):
        prod = 1.0
        for block in part:
            prod *= joint_prob(q, res, block)
        total += cumulant_coeff(len(part)) * prod
    return total


def central4_joint(q, res):
    # E prod_i (X_i-p)，不是 cumulant；用于比较。
    p = 1 - 1 / q
    total = 0.0
    for mask in range(16):
        block = [i for i in range(4) if (mask >> i) & 1]
        k = len(block)
        prob = 1.0 if not block else joint_prob(q, res, block)
        total += ((-p) ** (4-k)) * prob
    return total


def representative_patterns():
    return {
        (4,): (0,0,0,0),
        (3,1): (0,0,0,1),
        (2,2): (0,0,1,1),
        (2,1,1): (0,0,1,2),
        (1,1,1,1): (0,1,2,3),
    }


def main():
    qs = [5,7,11,101]
    print('pattern q central*q4 cumulant*q4 cumulant raw')
    for pat, res in representative_patterns().items():
        for q in qs:
            cent = central4_joint(q, res)
            cum = cumulant4_joint(q, res)
            print(pat, q, f'{cent*q**4:.6g}', f'{cum*q**4:.6g}', f'{cum:.6g}')
        print()

if __name__ == '__main__':
    main()
