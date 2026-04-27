#!/usr/bin/env python3
"""按小骨架洞序号统计条件素数率。

用法示例：
  python3 experiments/hole_index_prime_rate.py --P 997 --Kmax 20
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from small_height_failure_rule import status
from zero_repair_boundary_scan import boundary_events


def factor(n):
    """朴素分解；实验规模足够快，避免导入带顶层执行的脚本。"""
    out = []
    x = n
    for p in primes_upto(math.isqrt(n) + 1):
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out.append((p, e))
    if x > 1:
        out.append((x, 1))
    return out


def isprimefac(factors, n):
    """由分解结果判断 n 是否为素数。"""
    return len(factors) == 1 and factors[0][0] == n and factors[0][1] == 1


def collect_stats(P, y, A, Kmax):
    """收集边界锚点前 Kmax 个小骨架洞的素数率。"""
    rows = [x for x in boundary_events(P, y, P) if A < x['a'] < P]
    stats = defaultdict(lambda: [0, 0, 0.0])
    for row in rows:
        idx = 0
        r = 1
        while idx < Kmax and r <= P:
            st, _ = status(P, row['a'], y, r)
            if st != 'blocked':
                idx += 1
                n = row['a'] + r * P
                prime = isprimefac(factor(n), n)
                stats[idx][0] += 1
                stats[idx][1] += 1 if prime else 0
                stats[idx][2] += 1 / max(2.0, math.log(n))
            r += 1
    return rows, stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=997)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--Kmax', type=int, default=20)
    args = parser.parse_args()

    rows, stats = collect_stats(args.P, args.y, args.A, args.Kmax)
    # y=7 时小骨架筛掉 2,3,5,7；条件素数率主因子为 1/幸存密度。
    skeleton_primes = primes_upto(args.y)
    C_y = math.prod(skeleton_primes) / math.prod(q - 1 for q in skeleton_primes)
    print(f"P={args.P},rows={len(rows)},Cy={C_y:.6f}")
    print('idx total primes rate avg_1log expected ratio')
    for i in range(1, args.Kmax + 1):
        total, primes, avg = stats[i]
        if total:
            avg /= total
            rate = primes / total
            expected = C_y * avg
            ratio = rate / expected if expected else 0.0
            print(i, total, primes, f"{rate:.4f}", f"{avg:.4f}", f"{expected:.4f}", f"{ratio:.2f}")


if __name__ == '__main__':
    main()
