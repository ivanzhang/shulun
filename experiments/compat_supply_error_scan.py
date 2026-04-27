#!/usr/bin/env python3
"""扫描高度兼容供给模型误差量级。

用法示例：
  python3 experiments/compat_supply_error_scan.py --Ps 541,997,1999,4001 --K 20
"""
import argparse
import sys

sys.path.append('experiments')
from compat_supply_model import compat_by_q


def parse_ps(text):
    """解析 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='541,997,1321,1999,4001')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=20)
    args = parser.parse_args()

    print('P N Q q_count actual expected ratio abs_err rel_to_N rel_to_qcountK')
    for P in parse_ps(args.Ps):
        anchors, max_r, Q, by_q = compat_by_q(P, args.A, args.y, args.K)
        N = len(anchors)
        expected = N * args.K * sum(1 / q for q in by_q)
        actual = sum(by_q.values())
        err = actual - expected
        print(P, N, Q, len(by_q), actual, f'{expected:.2f}', f'{actual/expected:.4f}', f'{err:.2f}', f'{err/N:.3f}', f'{err/(len(by_q)*args.K):.3f}')


if __name__ == '__main__':
    main()
