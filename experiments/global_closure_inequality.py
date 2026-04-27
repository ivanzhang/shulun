#!/usr/bin/env python3
"""全局闭合不等式数值测试。

设全列 B11 前洞数量约 T≈P*phi(2310)/2310。
若全覆盖使用 cover > pi(P)，则不同补丁素数数量超过可用素数供给（粗模型）。
否则 cover<=pi(P)，saving S=T-cover 很大，用 saving_logL_tradeoff 计算 F(D,S)，
检查是否 F(D,S)>2log10(P)，从而固定骨架 lift 稀薄。

用法示例：
    python3 experiments/global_closure_inequality.py --Ps 1000,10000,100000,1000000
"""
import argparse
import math
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from saving_logL_tradeoff import run_case

PHI2310 = 480
M = 2310


def pi_count(n):
    return len(primes_upto(n))


def approx_case(P):
    T = math.floor(P * PHI2310 / M)
    # B11前洞在高度轴平均间距 2310/480，跨度约 P。
    D = P
    cover_supply = pi_count(P) - 5  # q>11 可用数量粗略值
    S = max(0, T - cover_supply)
    rec, _ = run_case(D, S) if S > 0 else (None, None)
    return {
        'P': P,
        'T': T,
        'D': D,
        'pi_gt11': cover_supply,
        'saving_if_cover_le_supply': S,
        'F_log10L': rec['log10L'] if rec else 0.0,
        'q_count': rec['q_count'] if rec else 0,
        'threshold_2logP': 2 * math.log10(P),
        'margin': (rec['log10L'] - 2 * math.log10(P)) if rec else 0.0,
        'chosen': rec['chosen'] if rec else [],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--Ps', default='1000,3000,10000,30000,100000,300000,1000000')
    args = parser.parse_args()
    print('P T pi_gt11 S F_log10L 2logP margin q_count')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        rec = approx_case(P)
        print(rec['P'], rec['T'], rec['pi_gt11'], rec['saving_if_cover_le_supply'], f'{rec["F_log10L"]:.3f}', f'{rec["threshold_2logP"]:.3f}', f'{rec["margin"]:.3f}', rec['q_count'], flush=True)


if __name__ == '__main__':
    main()
