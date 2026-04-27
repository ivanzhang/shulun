#!/usr/bin/env python3
"""高度兼容供给的解析模型对比。

模型：对固定 q，前 K 个 B_y 洞约占密度 rho_y=phi(M_y)/M_y，
兼容命中 a+rP≡0 mod q 约给出 1/q 因子。
因此每个 q 的供给预测约 N*K/q，截断 q<=Q。

用法示例：
  python3 experiments/compat_supply_model.py --P 1999 --K 20
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from shared_patch_energy import front_holes


def prime_anchors(P, A):
    """边界锚点短区间。"""
    flags = sieve(P)
    return [a for a in range(A + 1, P) if flags[a]]


def compat_by_q(P, A, y, K):
    """真实高度兼容供给，按 q 分组。"""
    anchors = prime_anchors(P, A)
    anchor_holes = {a: front_holes(P, a, y, K) for a in anchors}
    max_r = max(r for holes in anchor_holes.values() for r in holes)
    Q = math.isqrt((P - 1) + max_r * P)
    primes = [q for q in primes_upto(Q) if q > y and q != P]
    by_q = defaultdict(int)
    for q in primes:
        for a, holes in anchor_holes.items():
            for r in holes:
                if (a + r * P) % q == 0:
                    by_q[q] += 1
    return anchors, max_r, Q, by_q


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=1999)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--K', type=int, default=20)
    parser.add_argument('--top', type=int, default=20)
    args = parser.parse_args()

    anchors, max_r, Q, by_q = compat_by_q(args.P, args.A, args.y, args.K)
    N = len(anchors)
    harmonic = sum(1 / q for q in by_q)
    predicted_total = N * args.K * harmonic
    actual_total = sum(by_q.values())
    print('P', args.P, 'N', N, 'K', args.K, 'max_r', max_r, 'Q', Q, 'q_count', len(by_q))
    print('sum_1q', f'{harmonic:.6f}', 'predicted_NKsum1q', f'{predicted_total:.2f}', 'actual', actual_total, 'ratio', f'{actual_total/predicted_total:.3f}')
    print('q actual expected ratio')
    for q, actual in sorted(by_q.items(), key=lambda kv: (-kv[1], kv[0]))[:args.top]:
        expected = N * args.K / q
        print(q, actual, f'{expected:.2f}', f'{actual/expected:.3f}')


if __name__ == '__main__':
    main()
