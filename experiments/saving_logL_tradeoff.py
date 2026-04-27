#!/usr/bin/env python3
"""saving -> min logL(S,D) 权衡函数。

每个斜率 q 有容量 cap(q) 与成本 log(q)。要达到 saving S，
最小化 sum log(q)。由于每个 q 只能选一次，且容量为整数，用 DP 求解。
容量上界使用 analytic_closure_bound 的精确短区间单位函数。

用法示例：
    python3 experiments/saving_logL_tradeoff.py --D 150 --Smax 40
    python3 experiments/saving_logL_tradeoff.py --cases 150:15,198:20,480:55,960:135
"""
import argparse
import math
import sys

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto
from analytic_closure_bound import cap_bound

Y = 11
BASE_LOG10 = math.log10(2310)


def options_for_D(D):
    opts = []
    for q in [p for p in primes_upto(max(13, D)) if p > Y]:
        cap = cap_bound(D, q)
        if cap > 0:
            opts.append((q, cap, math.log10(q)))
    return opts


def min_log_for_savings(D, Smax):
    opts = options_for_D(D)
    inf = 10**100
    dp = [inf] * (Smax + 1)
    parent = [None] * (Smax + 1)
    dp[0] = 0.0
    for q, cap, cost in opts:
        old = dp[:]
        old_parent = parent[:]
        for s in range(Smax + 1):
            if old[s] >= inf:
                continue
            ns = min(Smax, s + cap)
            val = old[s] + cost
            if val < dp[ns]:
                dp[ns] = val
                parent[ns] = (s, q, cap, cost, old_parent[s])
    return dp, parent, opts


def reconstruct(parent, S):
    out = []
    node = parent[S]
    while node:
        prev, q, cap, cost, prev_parent = node
        out.append((q, cap, cost))
        node = prev_parent
    return list(reversed(out))


def run_case(D, S):
    dp, parent, opts = min_log_for_savings(D, S)
    if dp[S] >= 10**99:
        return None, opts
    chosen = reconstruct(parent, S)
    return {
        'D': D,
        'S': S,
        'log10_product': dp[S],
        'log10L': BASE_LOG10 + dp[S],
        'chosen': chosen,
        'capacity': sum(x[1] for x in chosen),
        'q_count': len(chosen),
    }, opts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--D', type=int, default=150)
    parser.add_argument('--Smax', type=int, default=40)
    parser.add_argument('--cases', default='')
    args = parser.parse_args()

    if args.cases:
        print('D S q_count capacity log10L chosen')
        for item in args.cases.split(','):
            if not item.strip():
                continue
            D, S = [int(x) for x in item.split(':')]
            rec, _opts = run_case(D, S)
            if rec is None:
                print(D, S, 'impossible')
            else:
                print(D, S, rec['q_count'], rec['capacity'], f'{rec["log10L"]:.3f}', rec['chosen'], flush=True)
        return

    dp, parent, opts = min_log_for_savings(args.D, args.Smax)
    print('D', args.D, 'options', opts[:30])
    print('S q_count capacity log10L chosen')
    for S in range(1, args.Smax + 1):
        if dp[S] >= 10**99:
            print(S, 'impossible')
            continue
        chosen = reconstruct(parent, S)
        print(S, len(chosen), sum(x[1] for x in chosen), f'{BASE_LOG10 + dp[S]:.3f}', chosen)


if __name__ == '__main__':
    main()
