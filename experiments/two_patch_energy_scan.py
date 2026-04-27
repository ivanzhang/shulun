#!/usr/bin/env python3
"""二补丁洞的二阶能量扫描。

对长尾样本统计：
  E2 = sum_i C(|Q_i|,2)
其中 Q_i 是第 i 个合数洞的全部有效补丁集合。E2 计数所有二阶斜线交会事件。
若 E2/T 稳定小，则多补丁洞自然稀疏，因为 #{|Q_i|>=2} <= E2。

用法示例：
  python3 experiments/two_patch_energy_scan.py --Ps 32003,64007,128021,256019 --K 35 --y 11 --top 5
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from hole_index_prime_rate import factor
from template_cover_sieve import template_groups


def patch_set(n, y, P):
    """返回 n 的有效补丁素数集合。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > y and q <= root and q != P)


def collect_records(P, A, y, K):
    """按死亡时间降序收集路径记录。"""
    records = []
    for group in template_groups(P, A, y, K):
        states = [(a, ()) for a in group['anchors']]
        for idx, r in enumerate(group['holes'], start=1):
            nxt = []
            for a, path in states:
                qs = patch_set(a + r * P, y, P)
                if qs:
                    nxt.append((a, path + (min(qs),)))
                elif path:
                    records.append((idx, a, path, group['holes'][:idx], group['pattern']))
            states = nxt
        for a, path in states:
            if path:
                records.append((K + 1, a, path, group['holes'], group['pattern']))
    return sorted(records, reverse=True)


def analyze(P, y, death, a, holes):
    """计算二阶能量与相关分布。"""
    prefix = holes[:death - 1] if death <= len(holes) else holes
    sizes = []
    pairs = []
    pair_to_positions = defaultdict(list)
    for idx, r in enumerate(prefix, start=1):
        qs = patch_set(a + r * P, y, P)
        sizes.append(len(qs))
        sorted_qs = sorted(qs)
        for i, q in enumerate(sorted_qs):
            for s in sorted_qs[i + 1:]:
                pairs.append((q, s, idx, r, q * s))
                pair_to_positions[(q, s)].append((idx, r))
    T = len(prefix)
    E2 = sum(k * (k - 1) // 2 for k in sizes)
    multi = sum(1 for k in sizes if k >= 2)
    unique = sum(1 for k in sizes if k == 1)
    E3 = sum(k * (k - 1) * (k - 2) // 6 for k in sizes)
    option_hist = Counter(sizes)
    repeated_pairs = {pair: pos for pair, pos in pair_to_positions.items() if len(pos) > 1}
    pair_products = [x[4] for x in pairs]
    return {
        'T': T,
        'unique': unique,
        'multi': multi,
        'E2': E2,
        'E3': E3,
        'option_hist': option_hist,
        'repeated_pair_count': len(repeated_pairs),
        'pair_product_min': min(pair_products) if pair_products else 0,
        'pair_product_max': max(pair_products) if pair_products else 0,
        'pair_product_avg': sum(pair_products) / len(pair_products) if pair_products else 0.0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='32003,64007,128021,256019')
    parser.add_argument('--A', type=int, default=83)
    parser.add_argument('--y', type=int, default=11)
    parser.add_argument('--K', type=int, default=35)
    parser.add_argument('--top', type=int, default=5)
    args = parser.parse_args()

    print('P rank death a T unique multi multi_ratio E2 E2_ratio E3 option_hist pairprod_min pairprod_avg pairprod_max repeated_pair_types pattern')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        for rank, rec in enumerate(collect_records(P, args.A, args.y, args.K)[:args.top], start=1):
            death, a, path, holes, pattern = rec
            st = analyze(P, args.y, death, a, holes)
            T = st['T']
            print(
                P, rank, death, a, T,
                st['unique'], st['multi'], f'{st["multi"]/T if T else 0:.3f}',
                st['E2'], f'{st["E2"]/T if T else 0:.3f}', st['E3'],
                sorted(st['option_hist'].items()),
                st['pair_product_min'], f'{st["pair_product_avg"]:.1f}', st['pair_product_max'],
                st['repeated_pair_count'], pattern,
            )


if __name__ == '__main__':
    main()
