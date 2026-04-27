#!/usr/bin/env python3
"""第200节杀死配额上界证书：对 (c, P_10, P) 三元组验证 k+1 强制条件。

定义：给定一个非零前缀 prefix（包含 k 个 (q,r,cap) 三元组）与其证人素数 P
（即 A_R(P)≤P），M_kill(prefix, P) 是"加入第 k+1 项后仍不杀死 P"的候选最大可补
saving；其中限制 cap ≤ last_cap(prefix)，每个 q ∉ used(prefix) 最多选一个 cap 最大
的"不杀死 P 候选"。

若 M_kill(prefix, P) < S − prefix_saving，则不存在能让"prefix 扩展到 saving≥S 且
保持 P 幸存"的 k+1 前缀，故 k+1 强制定理在 (prefix, P) 上成立。

用法：
    python3 experiments/kill_quota_certificate.py --c 2309 --W 100 --S 55 --X 1000000
"""
from __future__ import annotations

import argparse
import sys
from typing import Iterable

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_phase, prefix_anchor_from_phase, survivor_count
from prefix_completion_bound import full_scan, residue_rows_ranked
from skeleton_union_bound import q_residue_options


def kill_quota(prefix: list, witness_P: int, rows, residue_limit: int = 30) -> dict:
    """计算 M_kill(prefix, P)：不杀死 P 的兼容候选最大可补 saving。

    实现采用 §200.12 解析公式：当 modulus_old > P - A_old 时，
    每个 q∉used 的不杀 r 由 r_unkill ≡ -A_old · P^{-1} (mod q) 唯一确定。
    若该 (q, r_unkill, cap) 出现在 flat 中（cap≥1, cap≤last_cap），则贡献 cap。
    """
    used_qs = {t[0] for t in prefix}
    last_cap = prefix[-1][2] if prefix else 10**9
    base_residue, base_modulus = prefix_phase(prefix)
    base_A = prefix_anchor_from_phase(base_residue, base_modulus, witness_P)

    modulus_dominant = base_modulus > witness_P - base_A
    non_killing_by_q: dict[int, list[tuple[int, int, int]]] = {}

    if modulus_dominant:
        # 解析路径：每 q 单点查询
        for q, choices in rows:
            if q in used_qs:
                continue
            P_inv = pow(witness_P % q, -1, q)
            r_unkill = (-base_A * P_inv) % q
            best = None
            for triple in choices[:residue_limit]:
                if triple[1] != r_unkill:
                    continue
                cap = triple[2]
                if cap < 1 or cap > last_cap:
                    continue
                if best is None or cap > best[2]:
                    best = triple
            if best is not None:
                non_killing_by_q[q] = [(best[0], best[1], best[2])]
        m_kill = sum(t[0][2] for t in non_killing_by_q.values())
        # 上述公式仅对 modulus 主导情形精确；total/kill 计数留空避免误导
        return {
            'witness_P': witness_P,
            'base_A': base_A,
            'last_cap': last_cap,
            'used_qs_count': len(used_qs),
            'modulus_dominant': True,
            'modulus_old': base_modulus,
            'P_minus_A': witness_P - base_A,
            'non_killing_q_count': len(non_killing_by_q),
            'non_killing_total': sum(len(v) for v in non_killing_by_q.values()),
            'M_kill': m_kill,
        }

    # fallback：modulus 不主导时退回到逐项验证
    killing_count = 0
    total_count = 0
    for q, choices in rows:
        if q in used_qs:
            continue
        for triple in choices[:residue_limit]:
            cap = triple[2]
            if cap < 1 or cap > last_cap:
                continue
            total_count += 1
            new_prefix = prefix + [triple]
            nresidue, nmodulus = prefix_phase(new_prefix)
            nA = prefix_anchor_from_phase(nresidue, nmodulus, witness_P)
            if nA > witness_P:
                killing_count += 1
            else:
                non_killing_by_q.setdefault(q, []).append((triple[0], triple[1], cap))
    m_kill = sum(max(t[2] for t in triples) for triples in non_killing_by_q.values())

    return {
        'witness_P': witness_P,
        'base_A': base_A,
        'last_cap': last_cap,
        'used_qs_count': len(used_qs),
        'modulus_dominant': False,
        'modulus_old': base_modulus,
        'P_minus_A': witness_P - base_A,
        'total_candidates': total_count,
        'killing_candidates': killing_count,
        'kill_rate': killing_count / max(1, total_count),
        'non_killing_q_count': len(non_killing_by_q),
        'non_killing_total': sum(len(v) for v in non_killing_by_q.values()),
        'M_kill': m_kill,
    }


def certify_c(c: int, W: int, S: int, k_below: int, X: int,
              state_limit: int = 8000, residue_limit: int = 14,
              verbose: bool = False) -> dict:
    """对 c 做 k_below 完整扫描得到 N_c，再对每个非零前缀计算 M_kill 上界。

    返回每个 (P_below, witness_P) 的杀死配额报告与是否通过 k_below+1 强制判定。
    """
    holes = holes_for_c(c, W)
    opts = q_residue_options(holes)
    rows = residue_rows_ranked(opts, residue_limit)
    primes = primes_upto(X)

    scan = full_scan(c, W, S, k_below, X,
                     state_limit=state_limit, residue_limit=residue_limit,
                     primes=primes, verbose=False)
    nonzero = scan['nonzero_examples']

    if verbose:
        print(f'[c={c}] k={k_below} 扫描完成: {scan["nonzero_prefixes"]} 个非零前缀')

    reports = []
    pass_count = 0
    fail_count = 0
    for prefix_tuple, _, witness_list in nonzero:
        prefix = list(prefix_tuple)
        prefix_saving = sum(t[2] for t in prefix)
        need = S - prefix_saving
        for witness in witness_list:
            P = witness[0] if isinstance(witness, tuple) else witness
            quota = kill_quota(prefix, P, rows, residue_limit=30)
            quota['prefix_saving'] = prefix_saving
            quota['need_saving'] = need
            quota['passes'] = quota['M_kill'] < need
            if quota['passes']:
                pass_count += 1
            else:
                fail_count += 1
            reports.append((prefix, P, quota))

    return {
        'c': c, 'W': W, 'S': S, 'k_below': k_below, 'X': X,
        'k_below_nonzero': scan['nonzero_prefixes'],
        'k_below_zero': scan['zero_prefixes'],
        'k_below_unique': scan['unique_prefixes_checked'],
        'witnesses_total': len(reports),
        'passes': pass_count,
        'fails': fail_count,
        'reports': reports[:20],
        'k_above_force_certified': fail_count == 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kBelow', type=int, default=10,
                        help='待扩展的 k（验证 k+1 强制）')
    parser.add_argument('--X', type=int, default=1_000_000)
    parser.add_argument('--stateLimit', type=int, default=8000)
    parser.add_argument('--residueLimit', type=int, default=14)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    result = certify_c(args.c, args.W, args.S, args.kBelow, args.X,
                       state_limit=args.stateLimit,
                       residue_limit=args.residueLimit,
                       verbose=args.verbose)
    for k, v in result.items():
        if k == 'reports':
            print(f'reports (前 {len(v)} 个 witness):')
            for prefix, P, quota in v[:10]:
                kr = quota.get('kill_rate')
                kr_str = f'{kr:.3f}' if isinstance(kr, float) else 'N/A'
                print(f'  P={P}: prefix_saving={quota["prefix_saving"]} '
                      f'need={quota["need_saving"]} M_kill={quota["M_kill"]} '
                      f'mod_dominant={quota["modulus_dominant"]} '
                      f'kill_rate={kr_str} passes={quota["passes"]}')
        else:
            print(k, v)


if __name__ == '__main__':
    main()
