#!/usr/bin/env python3
"""§207 高预算 N_{c, k_low} 缺口检查。

§204 的全 c 扫描用 stateLimit=1500, residueLimit=7 较小预算。本节：
- 对 §204 报告的 9 个非零 c 用 stateLimit=20000, residueLimit=24 高预算重扫
- 对照 §204 的 1 prefix/c 是否完整覆盖

如果高预算下发现额外 prefix 且都通过 (⋆)，则 §204 证书加强。
若有不通过的 prefix，则更严密的论证需要。

用法：
    python3 experiments/high_budget_n_c_check.py
"""
from __future__ import annotations

import sys
import time

sys.path.append('experiments')
from analytic_kill_quota import analytic_M_kill
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from prefix_barrier_library import prefix_phase, prefix_anchor_from_phase
from prefix_completion_bound import full_scan


# 来自 §204 扫描日志的 9 个非零 c（部分推断 + 已知）
KNOWN_NONZERO_CS = [961, 1343, 2309]  # 已直接日志验证
# 其余 6 个 c 可能在中间，未单独打印


def main():
    W, S, k_low, X = 100, 55, 10, 1_000_000
    print(f'高预算 N_c 缺口检查 W={W} S={S} k_low={k_low} X={X}')
    print(f'参数: stateLimit=20000, residueLimit=24')
    print(f'素数表构建...', flush=True)
    primes = primes_upto(X)
    print(f'素数表大小 {len(primes)}', flush=True)

    summary = {
        'total_witnesses': 0,
        'pass_witnesses': 0,
        'fail_witnesses': 0,
        'worst_M_kill': 0,
        'worst_margin': 999,
    }
    fails = []

    t0 = time.time()
    for c in KNOWN_NONZERO_CS:
        print(f'\n--- c={c} 高预算扫描 ---', flush=True)
        result = full_scan(c, W, S, k_low, X,
                           state_limit=20000, residue_limit=24,
                           primes=primes, verbose=False)
        nz = result['nonzero_examples']
        elapsed = time.time() - t0
        print(f'  unique={result["unique_prefixes_checked"]} nz={len(nz)} t={elapsed:.0f}s')

        holes = holes_for_c(c, W)
        for prefix_tuple, _, witness_list in nz:
            prefix = list(prefix_tuple)
            prefix_saving = sum(t[2] for t in prefix)
            need = S - prefix_saving
            last_cap = prefix[-1][2]
            used_qs = {t[0] for t in prefix}
            base_residue, base_modulus = prefix_phase(prefix)
            for witness in witness_list:
                P = witness[0] if isinstance(witness, tuple) else witness
                A_old = prefix_anchor_from_phase(base_residue, base_modulus, P)
                quota = analytic_M_kill(holes, A_old, P, used_qs, last_cap)
                M = quota['M_kill']
                margin = need - M
                summary['total_witnesses'] += 1
                if M >= need:
                    summary['fail_witnesses'] += 1
                    fails.append((c, P, prefix_saving, M, need, prefix))
                    print(f'  FAIL: P={P} M_kill={M} need={need}')
                else:
                    summary['pass_witnesses'] += 1
                if M > summary['worst_M_kill']:
                    summary['worst_M_kill'] = M
                if margin < summary['worst_margin']:
                    summary['worst_margin'] = margin

        nz_count = len(nz)
        if nz_count > 1:
            print(f'  >>> c={c}: 高预算下发现 {nz_count} 个 nonzero prefix（§204 只报 1 个）')
            print(f'  示例 prefix:')
            for prefix_tuple, _, witness_list in nz[:3]:
                prefix_saving = sum(t[2] for t in prefix_tuple)
                witness = witness_list[0] if witness_list else None
                P = witness[0] if witness else None
                print(f'    saving={prefix_saving} P={P} prefix={prefix_tuple}')

    elapsed = time.time() - t0
    print()
    print('=' * 60)
    print('总结')
    print('=' * 60)
    for k, v in summary.items():
        print(f'  {k}: {v}')
    if fails:
        print(f'\n FAIL 列表（{len(fails)}）:')
        for c, P, ps, M, n, _ in fails[:10]:
            print(f'  c={c} P={P} ps={ps} M={M} need={n}')
    else:
        print('\n 所有高预算下的 (prefix, P) 全部通过 (⋆)')
    print(f'\n总耗时 {elapsed:.0f}s')


if __name__ == '__main__':
    main()
