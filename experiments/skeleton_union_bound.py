#!/usr/bin/env python3
"""低 cover 骨架并集界估算。

目标：估计所有达到 saving S 的骨架 lift 总机会：
    sum_B P/L(B)
骨架选择 q 及其余数类。对每个 q，容量 cap(q)，可选余数类数量 roughly q，
权重约 q / q = 1 会导致粗并集界失效；这里用实际洞集/链容量给出更细估计：
对固定洞段 H，每个 q 的候选余数类中，只有容量>0 的类计入，权重 class_count/q。
用 DP 计算达到 saving>=S 的总权重乘积和。

用法示例：
    python3 experiments/skeleton_union_bound.py --c 1213 --T 30 --S 15 --P 10000000
    python3 experiments/skeleton_union_bound.py --c 1213 --T 100 --S 55 --P 10000000
"""
import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto

Y = 11
M = 2310


def q_options(holes):
    D = max(holes) - min(holes)
    out = []
    for q in [p for p in primes_upto(D) if p > Y]:
        by = defaultdict(int)
        for r in holes:
            by[r % q] += 1
        # 按容量聚合余数类数量；容量=命中数-1。
        cap_counts = defaultdict(int)
        for cnt in by.values():
            cap = cnt - 1
            if cap > 0:
                cap_counts[cap] += 1
        if cap_counts:
            out.append((q, dict(cap_counts)))
    return out


def q_residue_options(holes):
    """返回保留真实余数类的 q 选项。

    每个选项形如：
        (q, residue, cap, hit_indices, hit_values)

    其中 cap=命中洞数-1，表示该斜率类带来的 saving。
    这里的 residue 是洞位置 r 对 q 的余数；若列模型中洞 r 被 q 覆盖，
    则锚点参数 lambda 需要满足 lambda ≡ residue (mod q)。
    """
    D = max(holes) - min(holes)
    indexed_holes = list(enumerate(holes))
    out = []
    for q in [p for p in primes_upto(D) if p > Y]:
        by = defaultdict(list)
        for idx, r in indexed_holes:
            by[r % q].append((idx, r))
        residue_rows = []
        for residue, hits in by.items():
            cap = len(hits) - 1
            if cap > 0:
                residue_rows.append(
                    (
                        q,
                        residue,
                        cap,
                        tuple(idx for idx, _ in hits),
                        tuple(r for _, r in hits),
                    )
                )
        if residue_rows:
            out.append((q, residue_rows))
    return out


def union_weight_dp(options, S):
    """计算达到 saving>=S 的 sum prod(class_count/q)。"""
    dp = [0.0] * (S + 1)
    dp[0] = 1.0
    for q, cap_counts in options:
        ndp = dp[:]
        for s, val in enumerate(dp):
            if val == 0:
                continue
            for cap, count in cap_counts.items():
                ns = min(S, s + cap)
                ndp[ns] += val * (count / q)
        dp = ndp
    return dp[S]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--T', type=int, default=30)
    parser.add_argument('--S', type=int, default=15)
    parser.add_argument('--P', type=int, default=10_000_000)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()
    holes = holes_for_c(args.c, args.T)
    opts = q_options(holes)
    weight = union_weight_dp(opts, args.S)
    # 基础 B11 模数也贡献 1/2310；lift机会约 P/2310 * weight。
    expected = args.P * weight / M
    print('c', args.c, 'T', args.T, 'S', args.S, 'P', args.P, 'D', max(holes)-min(holes), 'q_count', len(opts))
    print('union_weight_without_B11', weight, 'expected_lifts_P_over_2310', expected)
    print('top_options q cap_counts class_weight')
    ranked=[]
    for q, cc in opts:
        ranked.append((sum(count/q for count in cc.values()), q, cc))
    for cw,q,cc in sorted(ranked, reverse=True)[:args.show]:
        print(q, cc, cw)


if __name__ == '__main__':
    main()
