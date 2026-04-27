#!/usr/bin/env python3
"""洞集补丁因子的互质刚性分析。

对小骨架洞集 B_y(a,R)，逐个分析 n_r=a+rP 的素因子，尤其是：
- 可用补丁因子 q: y<q<=sqrt(a+(R-1)P), q|n_r；
- 洞之间 gcd(n_r,n_s) 与 |r-s| 的关系；
- 同一个补丁 q 同时命中多个洞时，必有 q | P(r-s)，因 q!=P，故 q | r-s。

这给出严格事实：大补丁 q 只能连接相差为 q 倍数的洞；若洞集直径 < q，则 q 只能单点命中。

用法示例：
    python3 experiments/hole_factor_constraints.py --P 461 --a 22 --R 81 --y 13 --detail
    python3 experiments/hole_factor_constraints.py --scan --maxP 2000 --y 13 --top 20
"""
import argparse
import math
from collections import defaultdict, Counter

from fixed_anchor_sieve_remainder import sieve, primes_upto, first_prime_r
from skeleton_patch_analysis import analyze as skeleton_analyze


def factor(n, primes):
    out = []
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out.append((p, e))
    if x > 1:
        out.append((x, 1))
    return out


def record(P, a, R, y):
    sk = skeleton_analyze(P, a, R, y)
    holes = sk['holes']
    Q = sk['Q']
    primes = primes_upto(math.isqrt(a + (R - 1) * P) + 10)
    rows = []
    q_to_holes = defaultdict(list)
    for r in holes:
        n = a + r * P
        fac = factor(n, primes)
        patch = [p for p, e in fac if y < p <= Q and p != P]
        large_rest = [p for p, e in fac if p > Q]
        rows.append({'r': r, 'n': n, 'fac': fac, 'patch': patch, 'large_rest': large_rest})
        for q in patch:
            q_to_holes[q].append(r)

    # 共享补丁 q 必整除洞距；统计是否存在违反。
    shared = []
    violations = []
    for q, rs in q_to_holes.items():
        if len(rs) >= 2:
            gaps = [abs(s - r) for i, r in enumerate(rs) for s in rs[i+1:]]
            ok = all(g % q == 0 for g in gaps)
            shared.append((q, rs, gaps, ok))
            if not ok:
                violations.append((q, rs, gaps))

    # 两两 gcd；严格有 gcd(n_r,n_s) | |r-s|，因为 gcd 同时整除 P(r-s) 且与 P 互素。
    gcd_rows = []
    gcd_viol = []
    for i, row1 in enumerate(rows):
        for row2 in rows[i+1:]:
            g = math.gcd(row1['n'], row2['n'])
            d = abs(row2['r'] - row1['r'])
            if g > 1:
                gcd_rows.append((row1['r'], row2['r'], d, g, d % g == 0))
                if d % g != 0:
                    gcd_viol.append((row1['r'], row2['r'], d, g))

    patch_degree = Counter(len(row['patch']) for row in rows)
    single_patch_rows = [row for row in rows if len(row['patch']) == 1]
    no_patch_rows = [row for row in rows if len(row['patch']) == 0]
    product_lower = 1
    for row in rows:
        if row['patch']:
            product_lower *= min(row['patch'])

    return {
        'P': P, 'a': a, 'R': R, 'y': y, 'Q': Q,
        'holes': holes, 'hole_count': len(holes), 'rows': rows,
        'q_to_holes': dict(q_to_holes), 'shared': shared, 'violations': violations,
        'gcd_rows': gcd_rows, 'gcd_viol': gcd_viol,
        'patch_degree': patch_degree,
        'single_patch_count': len(single_patch_rows), 'no_patch_count': len(no_patch_rows),
        'product_lower_digits': len(str(product_lower)) if product_lower else 1,
        'max_shared_size': max((len(rs) for rs in q_to_holes.values()), default=0),
        'multi_shared_count': sum(1 for rs in q_to_holes.values() if len(rs) >= 2),
    }


def print_record(rec, detail=False):
    print(
        f"P={rec['P']},a={rec['a']},R={rec['R']},y={rec['y']},Q={rec['Q']},"
        f"holes={rec['hole_count']},patch_degree={sorted(rec['patch_degree'].items())},"
        f"single_patch={rec['single_patch_count']},no_patch={rec['no_patch_count']},"
        f"multi_shared_q={rec['multi_shared_count']},max_shared={rec['max_shared_size']},"
        f"gcd_edges={len(rec['gcd_rows'])},viol={len(rec['violations'])+len(rec['gcd_viol'])},"
        f"prod_min_patch_digits={rec['product_lower_digits']}"
    )
    print('shared_q=', [(q, rs) for q, rs, gaps, ok in rec['shared'][:30]])
    if detail:
        print('holes=', rec['holes'])
        print('rows: r n factors patch large_rest')
        for row in rec['rows']:
            print(row['r'], row['n'], row['fac'], 'patch=', row['patch'], 'large=', row['large_rest'])
        print('gcd_edges=', rec['gcd_rows'])


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
        out.sort(key=lambda x: (-x['R'], -x['hole_count']))
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
