#!/usr/bin/env python3
"""§211 反例 prefix 的"最坏 r_unkill 序列"几何可达性分析。

§210 显示实测 hot rate 略低于随机。本节问更深问题：
对固定 prefix，令 r_unkill_q* = argmax_r H_holes(q, r) (c-级最坏 r)。
这给出 c-级最坏 M_kill（一般 ≫ need）。

问：是否存在素数 P 使 r_unkill_q(prefix, P) = r_unkill_q* 对所有 q 同时成立？
即"最坏 P_witness"是否真存在？

如果"最坏 P"几何上不存在（(residue, modulus) 约束让对应 CRT 不一致），则
真实 max M_kill < 最坏 c-级上界，给出 (⋆) 的解析下界证明路径。

本脚本：
1. 对 c=2309 反例 prefix_10，列每 q ∉ used 的 hot 余数集 Hot(q)
2. 枚举若干"最坏 r 选择"，CRT 合成对应 P 类
3. 检查每个 P 类是否有素数满足 A_old ≤ P

用法：
    python3 experiments/worst_case_p_witness.py --c 2309
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_phase, prefix_anchor_from_phase


def hot_residues(holes, q, threshold=2):
    """q 上 H_holes(q, r) ≥ threshold 的 r 集合，按 H 降序。"""
    counts = defaultdict(int)
    for h in holes:
        counts[h % q] += 1
    return sorted([(r, c) for r, c in counts.items() if c >= threshold],
                  key=lambda x: -x[1])


def crt_two(a1, m1, a2, m2):
    """CRT 合并 (a1, m1) and (a2, m2)；要求 gcd(m1, m2) = 1."""
    inv = pow(m1, -1, m2)
    k = ((a2 - a1) * inv) % m2
    return (a1 + m1 * k) % (m1 * m2), m1 * m2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--lastCap', type=int, default=3)
    parser.add_argument('--maxQs', type=int, default=15,
                        help='只对前 N 个最高 hot 的 q 做最坏组合')
    parser.add_argument('--need', type=int, default=9)
    args = parser.parse_args()

    # c=2309 反例 prefix_10
    prefix = [(13,5,9),(17,2,6),(19,2,6),(23,0,4),(29,22,4),
              (31,15,4),(37,18,4),(41,27,3),(43,9,3),(53,42,3)]

    holes = holes_for_c(args.c, args.W)
    used = {t[0] for t in prefix}
    residue, modulus = prefix_phase(prefix)
    print(f'prefix: {prefix}')
    print(f'residue={residue}, modulus={modulus}')
    print(f'used q: {sorted(used)}')

    # 列出每个未用 q 的 hot 残数与最大 cap
    D = max(holes) - min(holes)
    Y = 11
    primes_q = [p for p in primes_upto(D) if p > Y and p not in used]
    print(f'未用 q ∈ (11, {D}]: {len(primes_q)} 个')

    # 收集每 q 的 hot 残数
    q_hot = []
    for q in primes_q:
        hot = hot_residues(holes, q)
        if hot:
            max_cap = min(args.lastCap, hot[0][1] - 1)
            q_hot.append((q, hot[0][0], max_cap, hot))

    # 按 max_cap 降序排序
    q_hot.sort(key=lambda x: -x[2])
    print(f'\n前 {args.maxQs} 个最高 cap 的未用 q:')
    print(f'{"q":>6} {"r_max":>6} {"H_max":>6} {"cap":>4}')
    cum_M = 0
    for q, r_max, cap, hot_list in q_hot[:args.maxQs]:
        H_max = hot_list[0][1]
        cum_M += cap
        print(f'  {q:>4} {r_max:>6} {H_max:>6} {cap:>4}  cum_M_kill={cum_M}')

    # 现在 CRT 合并：要 r_unkill_q ≡ r_max (mod q) 对前 maxQs 个 q
    # r_unkill_q = -A_old · P^{-1} (mod q)
    # 即 -A_old · P^{-1} ≡ r_max (mod q)
    # 即 A_old · P^{-1} ≡ -r_max (mod q)
    # 即 A_old ≡ -r_max · P (mod q)
    # 对每 P，A_old 由 prefix 决定 = (-residue · P) mod modulus
    # 所以 (-residue · P) mod modulus mod q = -r_max · P mod q
    # 转化为 P 的同余: (residue · P + r_max · P) ≡ 0 (mod q) ?? 不对
    # 让我重新推导

    # 实际上 r_unkill_q = (-A_old · P^{-1}) mod q 是 P 的函数
    # 要 r_unkill_q = r_max 等价于：
    # P 满足 -A_old(P) · P^{-1} ≡ r_max (mod q)
    # 即 -((-residue · P) mod modulus) · P^{-1} ≡ r_max (mod q)
    # 由 modulus 主导（mod q ≠ 0 这边 used q 是已选，未选 q 与 modulus 互素）：
    # (-residue · P) mod modulus mod q ≠ -residue · P mod q in general
    # 这是因为 modulus mod q ≠ 0
    # 所以 r_unkill_q 对 P 的依赖很复杂

    # 为简化，我对每个 P 计算实际 r_unkill 序列，看哪些 P 让前 maxQs 个 q 都命中 hot
    print(f'\n搜索"最坏 P_witness"（前 {args.maxQs} 个 q 都命中 hot）:')
    print(f'参数: 最坏 cap 总和 = {cum_M}')
    print()

    # 在合理 P 范围 (e.g. 模 modulus 内的素数) 中搜索
    # modulus ≈ 3e14 太大，直接采样 P ∈ [1, 10^7] 内素数
    print(f'在 P ∈ [1, 10^7] 内素数枚举 hot landings 分布:')
    primes_p = primes_upto(10_000_000)
    target_qs = [q_hot[i][0] for i in range(min(args.maxQs, len(q_hot)))]
    target_rs = [q_hot[i][1] for i in range(min(args.maxQs, len(q_hot)))]

    # 对每个 P 检查 anchor 是否 ≤ P
    n_anchor_le_P = 0
    n_partial_hot = defaultdict(int)
    max_hot_count = 0
    best_P_record = None
    for P in primes_p:
        A_old = prefix_anchor_from_phase(residue, modulus, P)
        if A_old > P:
            continue  # 不是 witness
        n_anchor_le_P += 1
        # 计算 r_unkill 序列
        hot_count = 0
        for q, r_max in zip(target_qs, target_rs):
            try:
                P_inv = pow(P % q, -1, q)
            except ValueError:
                continue
            r_uk = (-A_old * P_inv) % q
            if r_uk == r_max:
                hot_count += 1
        n_partial_hot[hot_count] += 1
        if hot_count > max_hot_count:
            max_hot_count = hot_count
            best_P_record = (P, A_old, hot_count)

    print(f'P ∈ [1, 10^7] 内 anchor ≤ P 的素数: {n_anchor_le_P}')
    print(f'hot_count 分布 (前 {args.maxQs} 个 q 中命中 hot 数):')
    for hc in sorted(n_partial_hot.keys()):
        print(f'  hot_count={hc}: {n_partial_hot[hc]} 个 P')
    if best_P_record:
        P, A, hc = best_P_record
        print(f'\n最坏 P: P={P}, A_old={A}, hot_count={hc}/{args.maxQs}')


if __name__ == '__main__':
    main()
