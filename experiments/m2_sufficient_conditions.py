#!/usr/bin/env python3
"""测试 M2 下界的最弱充分条件。

恒等式：U=#{d>=1}, M1=sum d, M2=sum C(d,2)。
因为 d>=1 点中若总额外命中 E=M1-U，则 M2>=E。
更强：M2=(sum d^2-M1)/2。

用法示例：
  python3 experiments/m2_sufficient_conditions.py --Ps 4001,8009,16001 --K 10
"""
import argparse
import math
import sys

sys.path.append('experiments')
from d_distribution_m2_global import scan


def parse_ps(text):
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='4001,8009,16001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=10)
    parser.add_argument('--minN', type=int, default=50)
    args = parser.parse_args()

    print('P step N U/N M1/N excess=(M1-U)/N M2/N M2>=excess ratio M2/excess')
    for P in parse_ps(args.Ps):
        stats = scan(P, args.A, args.y, args.K)
        for idx in range(1, args.K + 1):
            st = stats[idx]
            dist = st['dist']
            N = sum(dist.values())
            if N < args.minN:
                continue
            U = N - dist[0]
            M1 = st['d_sum']
            M2 = sum(math.comb(d, 2) * c for d, c in dist.items() if d >= 2)
            excess = M1 - U
            print(P, idx, N, f'{U/N:.4f}', f'{M1/N:.4f}', f'{excess/N:.4f}', f'{M2/N:.4f}', excess <= M2, f'{M2/excess if excess else 0:.3f}')


if __name__ == '__main__':
    main()
