#!/usr/bin/env python3
"""前洞共享补丁能量统计。

用法示例：
  python3 experiments/shared_patch_energy.py --Ps 997,1321 --K 20
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from hole_index_prime_rate import factor, isprimefac
from small_height_failure_rule import status
from zero_repair_boundary_scan import boundary_events


def parse_ps(text):
    """解析逗号分隔的 P 列表。"""
    return [int(x.strip()) for x in text.split(',') if x.strip()]


def front_holes(P, a, y, K):
    """返回前 K 个未被小骨架阻塞的高度。"""
    holes = []
    r = 1
    while len(holes) < K and r <= P:
        st, _ = status(P, a, y, r)
        if st != 'blocked':
            holes.append(r)
        r += 1
    return holes


def omega_gt_y(n, y):
    """统计 n 中大于 y 的不同素因子个数。"""
    if n <= 0:
        return 0
    count = 0
    x = n
    for p in primes_upto(math.isqrt(x) + 1):
        if p * p > x:
            break
        if x % p == 0:
            if p > y:
                count += 1
            while x % p == 0:
                x //= p
    if x > 1 and x > y:
        count += 1
    return count


def row_energy(P, a, y, K):
    """计算单个边界锚点前洞的实际共享能量与差值上界。"""
    holes = front_holes(P, a, y, K)
    q_to_holes = defaultdict(list)
    prime_count = 0
    composite_count = 0
    patch_incidence = 0
    for r in holes:
        n = a + r * P
        fac = factor(n)
        if isprimefac(fac, n):
            prime_count += 1
            continue
        composite_count += 1
        small_factors = [q for q, _ in fac if y < q <= math.isqrt(n) and q != P]
        patch_incidence += len(small_factors)
        for q in small_factors:
            q_to_holes[q].append(r)

    actual_energy = sum(len(rs) * (len(rs) - 1) // 2 for rs in q_to_holes.values())
    bound_energy = 0
    gap_omega_counter = Counter()
    for i, r in enumerate(holes):
        for s in holes[i + 1:]:
            value = omega_gt_y(abs(s - r), y)
            bound_energy += value
            gap_omega_counter[value] += 1

    # Cauchy 给出的覆盖 T 个合数洞所需不同补丁数下界。
    if composite_count:
        distinct_lower = composite_count * composite_count / max(1, composite_count + 2 * bound_energy)
    else:
        distinct_lower = 0.0

    return {
        'holes': holes,
        'prime_count': prime_count,
        'composite_count': composite_count,
        'patch_incidence': patch_incidence,
        'distinct_patch_count': len(q_to_holes),
        'actual_energy': actual_energy,
        'bound_energy': bound_energy,
        'gap_omega_counter': gap_omega_counter,
        'max_share': max((len(rs) for rs in q_to_holes.values()), default=0),
        'distinct_lower': distinct_lower,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', type=str, default='541,997,1321,1439')
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--K', type=int, default=20)
    parser.add_argument('--show-worst', type=int, default=5)
    args = parser.parse_args()

    all_rows = []
    totals = Counter()
    omega_total = Counter()
    for P in parse_ps(args.Ps):
        rows = [x for x in boundary_events(P, args.y, P) if args.A < x['a'] < P]
        per = []
        for row in rows:
            rec = row_energy(P, row['a'], args.y, args.K)
            rec.update({'P': P, 'a': row['a'], 'R': row['R']})
            per.append(rec)
            all_rows.append(rec)
            omega_total.update(rec['gap_omega_counter'])
            for key in ['prime_count', 'composite_count', 'patch_incidence', 'distinct_patch_count', 'actual_energy', 'bound_energy', 'max_share']:
                totals[key] += rec[key]
        avg_actual = sum(x['actual_energy'] for x in per) / len(per) if per else 0.0
        avg_bound = sum(x['bound_energy'] for x in per) / len(per) if per else 0.0
        avg_share = sum(x['max_share'] for x in per) / len(per) if per else 0.0
        print('per_P', P, 'rows', len(rows), 'avg_actual_E', f'{avg_actual:.2f}', 'avg_bound_E', f'{avg_bound:.2f}', 'avg_max_share', f'{avg_share:.2f}')

    row_count = len(all_rows)
    print('summary rows', row_count, 'K', args.K, 'y', args.y)
    for key in ['prime_count', 'composite_count', 'patch_incidence', 'distinct_patch_count', 'actual_energy', 'bound_energy', 'max_share']:
        print(key, totals[key], 'avg', f'{totals[key] / row_count:.3f}' if row_count else '0')
    if totals['bound_energy']:
        print('actual_over_bound_energy', f"{totals['actual_energy'] / totals['bound_energy']:.4f}")
    print('gap_omega_distribution', sorted(omega_total.items()))
    print('worst_by_actual_energy')
    for rec in sorted(all_rows, key=lambda x: (-x['actual_energy'], -x['composite_count']))[:args.show_worst]:
        print('worst', 'P', rec['P'], 'a', rec['a'], 'R', rec['R'], 'pr', rec['prime_count'], 'comp', rec['composite_count'], 'actual_E', rec['actual_energy'], 'bound_E', rec['bound_energy'], 'max_share', rec['max_share'], 'holes', rec['holes'])


if __name__ == '__main__':
    main()
