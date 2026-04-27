#!/usr/bin/env python3
"""专属补丁乘积账本。

对小骨架洞集 B_y，若每个洞 r 都要由中等素因子 q_r 补丁覆盖，
且共享受洞距限制，则多数 q_r 必须近似专属。
本脚本计算：
- 洞到补丁素因子的二分图；
- 最大匹配/最小可用不同补丁数；
- 选择最小补丁乘积与洞数列乘积的关系；
- 是否存在 Hall 缺口或乘积容量矛盾。

用法示例：
    python3 experiments/exclusive_patch_product.py --P 461 --a 22 --R 81 --y 13 --detail
    python3 experiments/exclusive_patch_product.py --scan --maxP 2000 --y 13 --top 20
"""
import argparse
import math
from itertools import combinations

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from hole_factor_constraints import record as factor_record


def max_bipartite_matching(left_to_right):
    match_r = {}
    def dfs(u, seen):
        for v in left_to_right[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in match_r or dfs(match_r[v], seen):
                match_r[v] = u
                return True
        return False
    m = 0
    for u in left_to_right:
        if dfs(u, set()):
            m += 1
    return m, {u: v for v, u in match_r.items()}


def hall_deficit(left_to_right):
    # 洞数很小，直接枚举所有子集找最小 Hall 余量。
    left = list(left_to_right)
    best = None
    n = len(left)
    for mask in range(1, 1 << n):
        subset = [left[i] for i in range(n) if (mask >> i) & 1]
        neigh = set()
        for u in subset:
            neigh.update(left_to_right[u])
        margin = len(neigh) - len(subset)
        if best is None or margin < best[0]:
            best = (margin, subset, sorted(neigh))
    return best


def min_product_assignment(left_to_right):
    # 动态规划：为每个洞选不同补丁，最小化 log 乘积。
    left = list(left_to_right)
    rights = sorted(set(q for qs in left_to_right.values() for q in qs))
    idx = {q: i for i, q in enumerate(rights)}
    dp = {0: (0.0, [])}
    for u in left:
        ndp = {}
        for mask, (cost, pairs) in dp.items():
            for q in left_to_right[u]:
                bit = 1 << idx[q]
                if mask & bit:
                    continue
                val = cost + math.log(q)
                nm = mask | bit
                if nm not in ndp or val < ndp[nm][0]:
                    ndp[nm] = (val, pairs + [(u, q)])
        dp = ndp
        if not dp:
            return None, None
    best = min(dp.values(), key=lambda x: x[0])
    return best[0], best[1]


def record(P, a, R, y):
    fr = factor_record(P, a, R, y)
    left_to_right = {row['r']: sorted(set(row['patch'])) for row in fr['rows']}
    matching_size, matching = max_bipartite_matching(left_to_right)
    hall = hall_deficit(left_to_right)
    min_log_prod, assignment = min_product_assignment(left_to_right)

    log_n_product = sum(math.log(row['n']) for row in fr['rows'])
    log_min_patch_product = min_log_prod if min_log_prod is not None else float('inf')
    log_ratio = log_n_product - log_min_patch_product if min_log_prod is not None else float('-inf')

    # 每个 q<=Q 在洞数列乘积中出现的总指数；实际容量。
    q_exp = {}
    for row in fr['rows']:
        for p, e in row['fac']:
            if y < p <= fr['Q']:
                q_exp[p] = q_exp.get(p, 0) + e

    return {
        **fr,
        'left_to_right': left_to_right,
        'matching_size': matching_size,
        'matching': matching,
        'hall_margin': hall[0] if hall else None,
        'hall_subset': hall[1] if hall else [],
        'hall_neigh': hall[2] if hall else [],
        'min_log_patch_product': log_min_patch_product,
        'min_patch_product_digits': int(log_min_patch_product / math.log(10)) + 1 if min_log_prod is not None else None,
        'assignment': assignment,
        'log_n_product': log_n_product,
        'n_product_digits': int(log_n_product / math.log(10)) + 1,
        'log_ratio': log_ratio,
        'q_exp': q_exp,
        'distinct_patch_count': len(q_exp),
        'total_patch_exp': sum(q_exp.values()),
    }


def print_record(rec, detail=False):
    print(
        f"P={rec['P']},a={rec['a']},R={rec['R']},y={rec['y']},holes={rec['hole_count']},"
        f"distinct_q={rec['distinct_patch_count']},total_exp={rec['total_patch_exp']},"
        f"matching={rec['matching_size']}/{rec['hole_count']},hall_margin={rec['hall_margin']},"
        f"min_patch_digits={rec['min_patch_product_digits']},nprod_digits={rec['n_product_digits']},"
        f"log_ratio={rec['log_ratio']:.2f}"
    )
    if detail:
        print('left_to_right=', rec['left_to_right'])
        print('hall_subset=', rec['hall_subset'], 'hall_neigh=', rec['hall_neigh'])
        print('assignment=', rec['assignment'])
        print('q_exp=', sorted(rec['q_exp'].items()))
        print('rows=', [(row['r'], row['n'], row['patch'], row['fac']) for row in rec['rows']])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--a', type=int, default=22)
    ap.add_argument('--R', type=int, default=0)
    ap.add_argument('--y', type=int, default=13)
    ap.add_argument('--scan', action='store_true')
    ap.add_argument('--maxP', type=int, default=2000)
    ap.add_argument('--top', type=int, default=20)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()

    if args.scan:
        flags = sieve(args.maxP * args.maxP)
        out = []
        for P in primes_upto(args.maxP):
            if P < 3:
                continue
            worst_a, worst_R = 1, -1
            for a in range(1, P + 1):
                r0 = first_prime_r(P, a, flags)
                if r0 is not None and r0 > worst_R:
                    worst_a, worst_R = a, r0
            if worst_R > 0:
                out.append(record(P, worst_a, worst_R, args.y))
        out.sort(key=lambda x: (-x['R'], 999 if x['hall_margin'] is None else x['hall_margin']))
        for rec in out[:args.top]:
            print_record(rec, detail=False)
    else:
        R = args.R
        if not R:
            flags = sieve(args.P * args.P)
            R = first_prime_r(args.P, args.a, flags)
        print_record(record(args.P, args.a, R, args.y), detail=args.detail)


if __name__ == '__main__':
    main()
