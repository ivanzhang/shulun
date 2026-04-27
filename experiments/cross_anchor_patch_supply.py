#!/usr/bin/env python3
"""跨锚点补丁供给与同余唯一化统计。

用法示例：
  python3 experiments/cross_anchor_patch_supply.py --P 997 --K 20 --top 20
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from hole_index_prime_rate import factor, isprimefac
from shared_patch_energy import front_holes
from small_height_failure_rule import status
from zero_repair_boundary_scan import boundary_events


def patch_records(P, y, A, K):
    """收集边界锚点前 K 洞的补丁记录。"""
    rows = [x for x in boundary_events(P, y, P) if A < x['a'] < P]
    records = []
    for row in rows:
        a = row['a']
        holes = front_holes(P, a, y, K)
        for idx, r in enumerate(holes, start=1):
            n = a + r * P
            fac = factor(n)
            prime = isprimefac(fac, n)
            patches = []
            if not prime:
                patches = [q for q, _ in fac if y < q <= math.isqrt(n) and q != P]
            for q in patches:
                records.append({'P': P, 'a': a, 'idx': idx, 'r': r, 'n': n, 'q': q, 'res': a % q})
    return rows, records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=997)
    parser.add_argument('--y', type=int, default=7)
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--K', type=int, default=20)
    parser.add_argument('--top', type=int, default=20)
    args = parser.parse_args()

    rows, records = patch_records(args.P, args.y, args.A, args.K)
    by_q = defaultdict(list)
    by_pair_q = defaultdict(list)
    for rec in records:
        by_q[rec['q']].append(rec)
    for rec in records:
        by_pair_q[(rec['q'], rec['r'])].append(rec)

    total_holes = len(rows) * args.K
    total_records = len(records)
    distinct_q = len(by_q)
    print(f"P={args.P},rows={len(rows)},K={args.K},holes={total_holes},patch_records={total_records},distinct_q={distinct_q}")
    print('top_q q hits anchors distinct_res max_hits_per_res residue_collision_excess')
    for q, recs in sorted(by_q.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:args.top]:
        anchors = {x['a'] for x in recs}
        res_counter = Counter(x['res'] for x in recs)
        excess = sum(v - 1 for v in res_counter.values() if v > 1)
        print('top_q', q, len(recs), len(anchors), len(res_counter), max(res_counter.values()), excess)

    # 对固定 q 与固定高度 r，a mod q 被唯一指定；检查实际是否全部同余。
    violations = []
    pair_sizes = Counter()
    for (q, r), recs in by_pair_q.items():
        residues = {x['res'] for x in recs}
        pair_sizes[len(recs)] += 1
        if len(residues) != 1:
            violations.append((q, r, sorted(residues)[:10]))
    print('fixed_q_r_classes', len(by_pair_q), 'violations', len(violations), 'pair_size_dist', sorted(pair_sizes.items()))

    # 统计同一个 q 在同一 a 内的复用，与跨 a 命中分离。
    reuse_by_anchor = Counter()
    for q, recs in by_q.items():
        anchor_counter = Counter(x['a'] for x in recs)
        for v in anchor_counter.values():
            if v >= 2:
                reuse_by_anchor[v] += 1
    print('same_anchor_q_reuse_degree_dist', sorted(reuse_by_anchor.items()))

    # 按补丁大小分桶，估计供给容量：q 越大，可容纳的 a 个数约 rows/q 级别。
    bucket = Counter()
    for q, recs in by_q.items():
        b = 1 << (q.bit_length() - 1)
        bucket[b] += len(recs)
    print('q_power2_bucket_hits')
    for b, v in sorted(bucket.items()):
        print('bucket', b, v)


if __name__ == '__main__':
    main()
