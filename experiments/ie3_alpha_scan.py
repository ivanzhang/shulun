#!/usr/bin/env python3
"""扫描三阶包含-排除收缩常数 alpha。\n\n用法示例：\n  python3 experiments/ie3_alpha_scan.py --Ps 997,1999,4001,8009,16001 --K 12 --minN 30\n"""
import argparse
import sys

sys.path.append('experiments')
from factorial_moment_scan import scan_P


def parse_ps(text):
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='997,1999,4001,8009,16001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=12)
    parser.add_argument('--minN', type=int, default=30)
    args = parser.parse_args()
    worst = []
    print('P step N U_rate IE3_rate H4_rate')
    for P in parse_ps(args.Ps):
        stats = scan_P(P, args.A, args.y, args.K)
        for idx in range(1, args.K + 1):
            s = stats[idx]
            N = s['N']
            if N < args.minN:
                continue
            ie3 = s['M1'] - s['M2'] + s['M3']
            print(P, idx, N, f'{s["U"]/N:.4f}', f'{ie3/N:.4f}', f'{s["M4"]/N:.5f}')
            worst.append((s['U']/N, ie3/N, s['M4']/N, P, idx, N))
    print('worst_U', max(worst) if worst else None)
    print('worst_IE3', max(worst, key=lambda x: x[1]) if worst else None)

if __name__ == '__main__':
    main()
