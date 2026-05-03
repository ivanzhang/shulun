#!/usr/bin/env python3
"""§208.8 对角线方向完整 (⋆_diag) 严格证书。

对每个素数 P，做完整证书验证：
1. 用 holes_diag(P, Y) 与 q_residue_options_diag 跑反例搜索 (saving≥S, 长度≥k_low)
2. 对每个反例 (prefix, t_witness)，验证：
     M_kill_diag(prefix, t_w) < S − prefix_saving
   其中 r_unkill_diag(q, t_w) = t_w mod q

输出：每 P 的反例数、(⋆_diag) 验证结果、worst margin。

用法：
    python3 experiments/diagonal_full_certificate.py --maxP 200 --S 9 --kLow 4 --Y 11
"""
from __future__ import annotations

import argparse
import math
import sys
import time
from typing import List, Tuple

sys.path.append('experiments')
from diagonal_certificate import holes_for_diagonal, q_residue_options_diag, is_prime
from fixed_anchor_sieve_remainder import primes_upto


def reverse_search_diag(holes: List[int], P: int, opts, S: int, k_low: int,
                        state_limit: int = 2000, residue_limit: int = 8) -> List:
    """对角线方向反例搜索：找 saving≥S 的 k_low 元 prefix 且其上有 t_w 是 prime。"""
    M = P + 1
    if not opts:
        return []

    rows = []
    for q, residue_rows in opts:
        residue_rows.sort(key=lambda x: -x[2])
        rows.append((q, residue_rows[:residue_limit]))
    rows.sort(key=lambda item: (-max(row[2] for row in item[1]), item[0]))

    states = [(0, [])]
    nonzero_prefixes = []
    seen = set()
    for q, choices in rows:
        new_states = states[:]
        for saving, chosen in states:
            for triple in choices:
                ns = saving + triple[2]
                nchosen = chosen + [(triple[0], triple[1], triple[2])]
                if ns >= S and len(nchosen) >= k_low:
                    key = tuple(sorted(nchosen[:k_low], key=lambda t: (-t[2], t[0], t[1])))
                    if key in seen:
                        continue
                    seen.add(key)
                    # 验证 prefix 在 holes 上有 witness（即存在 t ∈ [0, P-1] 满足 prefix CRT 且 1+t·M 素数）
                    witnesses = find_witnesses_diag(list(key), P, M)
                    if witnesses:
                        nonzero_prefixes.append((key, witnesses))
                else:
                    new_states.append((ns, nchosen))
        new_states.sort(key=lambda x: -x[0])
        states = new_states[:state_limit]

    return nonzero_prefixes


def crt_compose(prefix):
    """对角线 prefix CRT 合并：(residue, modulus)"""
    residue = 0
    modulus = 1
    for q, r, _ in prefix:
        # CRT
        gcd = math.gcd(modulus, q)
        if gcd != 1:
            return None  # q 重复
        m_inv = pow(modulus, -1, q)
        diff = ((r - residue) * m_inv) % q
        residue = residue + modulus * diff
        modulus *= q
    return (residue, modulus)


def find_witnesses_diag(prefix, P: int, M: int) -> List[int]:
    """找 t ∈ [0, P-1] 使 t ≡ residue (mod modulus) 且 1+t·M 是素数。"""
    crt = crt_compose(prefix)
    if crt is None:
        return []
    residue, modulus = crt
    out = []
    t = residue
    while t < P:
        if t >= 0 and t < P:
            A = 1 + t * M
            if A > 1 and is_prime(A):
                out.append(t)
        t += modulus
    return out


def analytic_M_kill_diag(holes: List[int], t_w: int, used_qs: set, last_cap: int,
                         q_max: int, M: int) -> int:
    """对角线版 §201 M_kill 公式：
    M_kill = Σ_{q ∉ used, q ∤ M} min(last_cap, max(0, H_holes(q, t_w mod q) − 1))
    """
    from collections import defaultdict
    Y = 11
    primes = [p for p in primes_upto(q_max) if p > Y]
    M_kill = 0
    for q in primes:
        if q in used_qs:
            continue
        if M % q == 0:
            continue
        r_unkill = t_w % q
        H = sum(1 for h in holes if h % q == r_unkill)
        cap = max(0, H - 1)
        M_kill += min(last_cap, cap)
    return M_kill


def certify_P(P: int, S: int, k_low: int, Y: int = 11) -> dict:
    holes = holes_for_diagonal(P, Y=Y)
    opts = q_residue_options_diag(holes, P, Y=Y)
    M = P + 1
    nonzero = reverse_search_diag(holes, P, opts, S, k_low)

    if not nonzero:
        return {
            'P': P,
            'holes_size': len(holes),
            'nonzero_count': 0,
            'witnesses_total': 0,
            'fail_count': 0,
            'worst_margin': None,
        }

    witnesses_total = 0
    fail_count = 0
    worst_margin = None
    fail_records = []
    q_max = max(holes) - min(holes) if holes else 0
    for prefix_tuple, witnesses in nonzero:
        prefix = list(prefix_tuple)
        prefix_saving = sum(t[2] for t in prefix)
        need = S - prefix_saving
        last_cap = prefix[-1][2]
        used_qs = {t[0] for t in prefix}
        for t_w in witnesses:
            witnesses_total += 1
            M_kill = analytic_M_kill_diag(holes, t_w, used_qs, last_cap, q_max, M)
            margin = need - M_kill
            if M_kill >= need:
                fail_count += 1
                fail_records.append((P, t_w, prefix_saving, M_kill, need))
            if worst_margin is None or margin < worst_margin:
                worst_margin = margin

    return {
        'P': P,
        'holes_size': len(holes),
        'nonzero_count': len(nonzero),
        'witnesses_total': witnesses_total,
        'fail_count': fail_count,
        'worst_margin': worst_margin,
        'fail_records': fail_records,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=200)
    parser.add_argument('--S', type=int, default=None,
                        help='固定 S；若 None 则自适应 S = |holes_diag| - kLow')
    parser.add_argument('--kLow', type=int, default=4)
    parser.add_argument('--Y', type=int, default=11)
    parser.add_argument('--minP', type=int, default=23)
    parser.add_argument('--Sratio', type=float, default=None,
                        help='S = ratio · |holes_diag|；与 --S 互斥')
    args = parser.parse_args()

    print(f'对角线方向 (⋆_diag) 证书 P ∈ [{args.minP}, {args.maxP}], k_low={args.kLow}, Y={args.Y}')
    print(f'S 模式: {"固定 S=" + str(args.S) if args.S else ("Sratio=" + str(args.Sratio) if args.Sratio else "自适应 S = |holes| - kLow")}')
    print()

    summary = {
        'total_P': 0,
        'no_nonzero': 0,
        'has_nonzero': 0,
        'P_with_fail': 0,
        'total_witnesses': 0,
        'total_fails': 0,
        'worst_margin': None,
        'worst_record': None,
    }
    fail_list = []
    t0 = time.time()
    for P in primes_upto(args.maxP):
        if P < args.minP:
            continue
        summary['total_P'] += 1
        # 决定该 P 的 S
        if args.S is not None:
            S_p = args.S
        elif args.Sratio is not None:
            holes_p = holes_for_diagonal(P, Y=args.Y)
            S_p = max(1, int(args.Sratio * len(holes_p)))
        else:
            holes_p = holes_for_diagonal(P, Y=args.Y)
            S_p = max(1, len(holes_p) - args.kLow)
        rec = certify_P(P, S_p, args.kLow, Y=args.Y)
        rec['S_used'] = S_p
        if rec['nonzero_count'] == 0:
            summary['no_nonzero'] += 1
            continue
        summary['has_nonzero'] += 1
        summary['total_witnesses'] += rec['witnesses_total']
        if rec['fail_count'] > 0:
            summary['P_with_fail'] += 1
            summary['total_fails'] += rec['fail_count']
            fail_list.extend(rec.get('fail_records', []))
        if rec['worst_margin'] is not None:
            if summary['worst_margin'] is None or rec['worst_margin'] < summary['worst_margin']:
                summary['worst_margin'] = rec['worst_margin']
                summary['worst_record'] = (P, rec)
        if rec['nonzero_count'] > 0:
            print(f'  P={P:>4} holes={rec["holes_size"]} S={S_p} nz={rec["nonzero_count"]} '
                  f'witnesses={rec["witnesses_total"]} fails={rec["fail_count"]} '
                  f'worst_margin={rec["worst_margin"]}', flush=True)

    elapsed = time.time() - t0
    print()
    print('=' * 60)
    print(f'总结 ({elapsed:.0f}s)')
    print('=' * 60)
    for k, v in summary.items():
        if k != 'worst_record':
            print(f'  {k}: {v}')
    if summary['worst_record']:
        P, rec = summary['worst_record']
        print(f'  worst_record: P={P} margin={rec["worst_margin"]}')
    if fail_list:
        print(f'\nFAIL 列表 ({len(fail_list)}):')
        for P, t_w, ps, M, n in fail_list[:10]:
            print(f'  P={P} t_w={t_w} ps={ps} M_kill={M} need={n}')


if __name__ == '__main__':
    main()
