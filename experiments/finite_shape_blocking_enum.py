#!/usr/bin/env python3
"""枚举 T⊂[0,C] 的小素数完全阻断形状。

若 T mod p 覆盖所有 p 个剩余类，则小筛权重为 0。
列出未被 primes<=Y 阻断的高阶形状，作为 E-interaction 的有限检查清单。

用法示例：
  python3 experiments/finite_shape_blocking_enum.py --Cs 4,5,6,8 --Y 13
"""
import argparse
import itertools


def primes_upto(n):
    out = []
    for x in range(2, n + 1):
        for p in out:
            if p * p > x:
                break
            if x % p == 0:
                break
        else:
            out.append(x)
            continue
        if any(x % p == 0 for p in out if p * p <= x):
            continue
        if x not in out:
            out.append(x)
    return out


def blocker(T, primes):
    for p in primes:
        if len({t % p for t in T}) == p:
            return p
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Cs', default='4,5,6,8')
    ap.add_argument('--Y', type=int, default=13)
    args = ap.parse_args()
    primes = primes_upto(args.Y)
    print('C r total blocked unblocked examples')
    for C in [int(x) for x in args.Cs.split(',') if x.strip()]:
        nums = list(range(1, C + 1))
        for r in range(2, C + 2):
            total = blocked = 0
            examples = []
            for rest in itertools.combinations(nums, r - 1):
                T = (0,) + rest
                total += 1
                if blocker(T, primes) is not None:
                    blocked += 1
                elif len(examples) < 12:
                    examples.append(T)
            print(C, r, total, blocked, total - blocked, examples)


if __name__ == '__main__':
    main()
