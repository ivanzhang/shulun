#!/usr/bin/env python3
"""§208 主对角线方向局部非空刚性证书。

按 §206 元层面框架，把列方向 §200-§205 推广到主对角线 R = {(i, i)}。

核心数据：A_t = 1 + t(P+1), t ∈ [0, P-1]。
设 M = P+1（一般合数）。q | A_t ⇔ t ≡ -M^{-1} (mod q)，需 (q, M) = 1。

工具：
- holes_for_diagonal(P, Y_primes): 小筛幸存的 t ∈ [0, P-1]
- q_residue_options_diag: H_holes(q, r) for diagonal
- r_unkill_diag, M_kill_diag: 类比 §201 解析公式

实证：对所有素数 P ≤ X_lim，验证主对角线含素数。

用法：
    python3 experiments/diagonal_certificate.py --maxP 10000
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict
from typing import List, Tuple

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    for d in range(3, math.isqrt(n) + 1, 2):
        if n % d == 0: return False
    return True


def holes_for_diagonal(P: int, Y: int = 11) -> List[int]:
    """对角线 holes：t ∈ [0, P-1] 使得 gcd(A_t, ∏_{q≤Y} q) = 1.
    其中 A_t = 1 + t·(P+1)。"""
    M = P + 1
    small_primes = primes_upto(Y)
    out = []
    for t in range(P):
        A = 1 + t * M
        if A < 2:
            continue
        if all(A % q != 0 for q in small_primes):
            out.append(t)
    return out


def q_residue_options_diag(holes: List[int], P: int, Y: int = 11):
    """对角线版 q_residue_options：返回 [(q, [(q, r, cap, ...)] for q ∤ M.

    每个 q ∤ M = P+1 给出单一同余斜线。对每个 r mod q，统计 H_holes(q, r)。
    """
    if not holes:
        return []
    M = P + 1
    D = max(holes) - min(holes)
    out = []
    for q in [p for p in primes_upto(D) if p > Y]:
        if M % q == 0:
            continue  # 这种 q 永远不覆盖对角线，跳过
        by_r = defaultdict(list)
        for idx, t in enumerate(holes):
            by_r[t % q].append((idx, t))
        residue_rows = []
        for r, hits in by_r.items():
            cap = len(hits) - 1
            if cap > 0:
                residue_rows.append(
                    (q, r, cap, tuple(idx for idx, _ in hits), tuple(t for _, t in hits))
                )
        if residue_rows:
            out.append((q, residue_rows))
    return out


def diag_anchor_check(P: int, Y: int = 11) -> dict:
    """对单个 P 验证对角线含素数。

    注意：小素数 q ≤ Y 本身也是合法素数。检验时同时保留：
    - 全 P 个 t 的对角线值 A_t（整体直接验证素性）
    - holes 筛中保留的"大素数候选"
    """
    M = P + 1
    holes = holes_for_diagonal(P, Y)
    primes_full = []  # 全对角线上的所有素数
    primes_in_holes = []
    for t in range(P):
        A = 1 + t * M
        if is_prime(A):
            primes_full.append((t, A))
            if t in holes:
                primes_in_holes.append((t, A))
    return {
        'P': P,
        'P+1': M,
        'P+1_factors': sorted(set(p for p in primes_upto(min(M, 10000)) if M % p == 0)),
        'diag_size': P,
        'holes_size': len(holes),
        'primes_full': len(primes_full),     # 全对角线上的素数
        'primes_in_holes': len(primes_in_holes),
        'first_prime': primes_full[0] if primes_full else None,
        'q_residue_options_count': len(q_residue_options_diag(holes, P, Y)),
    }


def H_holes_diag(holes: List[int], q: int, r: int) -> int:
    return sum(1 for t in holes if t % q == r)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=2000)
    parser.add_argument('--Y', type=int, default=11)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    print(f'对角线方向局部非空刚性证书')
    print(f'参数: maxP={args.maxP}, Y={args.Y}')
    print()

    fail = []
    margin_records = []
    for P in primes_upto(args.maxP):
        if P == 2:
            continue  # 边界情形 (1, 4) 自动跳过
        rec = diag_anchor_check(P, Y=args.Y)
        if rec['primes_full'] == 0:
            fail.append(rec)
        margin_records.append((P, rec['primes_full'], rec['primes_in_holes'], rec['holes_size']))

    print(f'验证 P ∈ (2, {args.maxP}] 素数总数: {len(margin_records)}')
    print(f'反例数 (主对角线无素数): {len(fail)}')
    print()

    if fail:
        print('反例:')
        for r in fail[:args.show]:
            print(f'  P={r["P"]}, P+1={r["P+1"]}, holes={r["holes_size"]}, primes_full={r["primes_full"]}')
    else:
        # 看最坏样本（最少素数对角线）
        margin_records.sort(key=lambda x: x[1])
        print(f'素数最少 {args.show} 个对角线:')
        print(f'  {"P":>6} {"primes_full":>11} {"in_holes":>9} {"holes":>6} {"ratio":>6}')
        for P, primes_full, primes_holes, holes in margin_records[:args.show]:
            ratio = primes_full / max(1, P)
            print(f'  {P:>6} {primes_full:>11} {primes_holes:>9} {holes:>6} {ratio:>6.3f}')

        # 平均统计
        avg_primes = sum(r[1] for r in margin_records) / len(margin_records)
        avg_holes = sum(r[3] for r in margin_records) / len(margin_records)
        print(f'\n平均: holes={avg_holes:.1f}, primes_full={avg_primes:.1f}')


if __name__ == '__main__':
    main()
