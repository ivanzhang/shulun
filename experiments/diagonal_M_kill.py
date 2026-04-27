#!/usr/bin/env python3
"""§208 对角线方向 M_kill 解析公式实施。

把 §201 列方向 M_kill 公式直接推广到对角线方向：

设 holes_diag = {t ∈ [0, P-1] : gcd(1 + t(P+1), 2310) = 1}
对每个 q ∤ (P+1) 计算 H_holes_diag(q, r)。

对一个反例 prefix 与候选 t_witness ∈ holes_diag (1 + t·M 是素数):
    r_unkill_q(prefix, t_witness) = (-A_old · t_witness^{-1}) mod q   (待推导)

由于对角线模型与列模型的 CRT 结构同构（只是 P → M = P+1，c → 1），
列方向的 r_unkill 公式应该用 t_witness 替代列方向的素数 P_witness。

但精确意义上，对角线 anchor 应该映射回 t-空间，这与列方向略有不同。

本节先实施数据收集：对若干 P，找对角线反例 prefix 与 witness t，
然后用类比公式计算 M_kill_diag，验证 (⋆) 不等式。

用法：
    python3 experiments/diagonal_M_kill.py --P 47 --S 9 --kLow 4
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict
from typing import List, Tuple

sys.path.append('experiments')
from diagonal_certificate import holes_for_diagonal, q_residue_options_diag, is_prime
from fixed_anchor_sieve_remainder import primes_upto


def prefix_phase_diag(prefix):
    """对角线 prefix CRT 合并：与列方向同。"""
    residue = 0
    modulus = 1
    for q, r, *_ in prefix:
        # CRT
        from prime_weighted_block_sample import crt_pair
        residue, modulus = crt_pair(residue, modulus, r % q, q)
    return residue, modulus


def diag_anchor(residue: int, modulus: int, t_w: int, M: int) -> int:
    """对角线版 anchor：在 t 空间。

    在列方向，anchor = -residue · P mod modulus 对应 t-坐标。
    对角线方向 t 与 P (列参数) 的对应关系不直接，但 anchor 在 t-空间的解释一致。
    一个简化版：anchor = (residue) mod modulus（即 prefix 的 t-代表）；
    检查 anchor ≤ t_w 给出 t_w 为 prefix witness。

    更精确版本（待推导）：anchor = (-residue · S) mod modulus 其中 S 是某常数。
    本节先用 anchor = residue mod modulus，与 t_w 比较。
    """
    return residue % modulus


def survivor_t_diag(prefix, P: int, X_t: int) -> List[Tuple[int, int]]:
    """对角线版 survivor：找让 prefix anchor ≤ t_w 且 1+t_w·M 是素数的 t_w ∈ [0, P-1]。

    这里取所有 t_w ∈ [0, P-1]，对每个 t_w 检查 anchor 一致性 + 素性。
    """
    residue, modulus = prefix_phase_diag(prefix)
    M = P + 1
    out = []
    for t_w in range(P):
        # prefix t_w 在 prefix 的 CRT 类内即 t_w ≡ residue (mod modulus)
        if t_w % modulus != residue % modulus:
            continue
        A = 1 + t_w * M
        if is_prime(A):
            out.append((t_w, A))
    return out


def find_diag_nonzero_prefix(P: int, S_target: int, k_low: int, Y: int = 11) -> List:
    """对单个 P 找对角线方向反例 prefix（saving≥S，prefix 在 holes_diag 上 cover）。

    用束搜索套用 q_residue_options_diag。
    """
    holes = holes_for_diagonal(P, Y=Y)
    if not holes:
        return []
    opts = q_residue_options_diag(holes, P, Y=Y)

    # 简单束搜索：按 cap 降序贪婪
    rows = []
    for q, residue_rows in opts:
        residue_rows.sort(key=lambda x: -x[2])
        rows.append((q, residue_rows[:5]))  # 每 q 取前 5 个 cap 大的 r
    rows.sort(key=lambda item: (-max(row[2] for row in item[1]), item[0]))

    states = [(0, [])]  # (saving, chosen)
    finished = []
    for q, choices in rows:
        new_states = states[:]
        for saving, chosen in states:
            for triple in choices:
                ns = saving + triple[2]
                nchosen = chosen + [(triple[0], triple[1], triple[2])]
                if ns >= S_target and len(nchosen) >= k_low:
                    finished.append((ns, nchosen[:k_low]))
                else:
                    new_states.append((ns, nchosen))
        new_states.sort(key=lambda x: -x[0])
        states = new_states[:200]

    finished.sort(key=lambda x: -x[0])
    return finished[:20]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--P', type=int, default=47)
    parser.add_argument('--S', type=int, default=9)
    parser.add_argument('--kLow', type=int, default=4)
    parser.add_argument('--Y', type=int, default=11)
    parser.add_argument('--maxP', type=int, default=None)
    args = parser.parse_args()

    if args.maxP:
        # 跨 P 扫描
        print(f'maxP 扫描 P ∈ (5, {args.maxP}], S={args.S}, k_low={args.kLow}')
        for P in primes_upto(args.maxP):
            if P <= 5: continue
            holes = holes_for_diagonal(P, Y=args.Y)
            opts = q_residue_options_diag(holes, P, Y=args.Y)
            max_saving = sum(max(row[2] for row in residue_rows) for q, residue_rows in opts)
            n_q = len(opts)
            print(f'  P={P:>4} P+1={P+1:>4} holes={len(holes):>3} q_count={n_q:>3} max_total_cap={max_saving:>3}')
        return

    P = args.P
    print(f'对角线方向 §208: P={P}, P+1={P+1}, S={args.S}, k_low={args.kLow}')
    holes = holes_for_diagonal(P, Y=args.Y)
    print(f'holes_diag size = {len(holes)}')

    opts = q_residue_options_diag(holes, P, Y=args.Y)
    print(f'q_residue_options 数: {len(opts)}')
    for q, rows in opts[:5]:
        max_cap = max(r[2] for r in rows)
        print(f'  q={q} max_cap={max_cap} #r_with_cap>=1={len(rows)}')

    # 找反例 prefix
    candidates = find_diag_nonzero_prefix(P, args.S, args.kLow, Y=args.Y)
    print(f'\n反例 prefix 候选数: {len(candidates)}')
    for saving, prefix in candidates[:5]:
        print(f'  saving={saving} prefix={prefix}')

    # 对每个 prefix 找 witness 并验证 anchor 关系
    for saving, prefix in candidates[:3]:
        witness_list = survivor_t_diag(prefix, P, P)
        print(f'\nprefix {prefix}:')
        print(f'  witness t (prime A_t): {witness_list[:5]}')


if __name__ == '__main__':
    main()
