#!/usr/bin/env python3
"""低 cover 块骨架的素性加权与锚点可达性抽样。

本版使用真实余数类，而不是 residue=0 代理：
对每个 q，枚举真实的 r mod q 命中洞集；组合达到 saving S 后，
用 CRT 合并得到 lambda 模 L，再扫描素数 P，检查 a=(-lambda P mod L)<P
以及 a 是否为素数。

用法示例：
    python3 experiments/prime_weighted_block_sample.py --c 1213 --W 100 --S 55 --maxP 1000000 --limit 200
    python3 experiments/prime_weighted_block_sample.py --c 1213 --W 180 --S 120 --maxP 10000000 --limit 50
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto
from skeleton_union_bound import M, q_residue_options


def crt_pair(a1, m1, a2, m2):
    """合并两个互素模同余。"""
    inv = pow(m1, -1, m2)
    k = ((a2 - a1) * inv) % m2
    return (a1 + m1 * k) % (m1 * m2), m1 * m2


def enumerate_weighted_skeletons(opts, target_saving, limit, beam):
    """用束搜索枚举较有贡献的真实余数类骨架。"""
    rows = []
    for q, residue_rows in opts:
        choices = sorted(residue_rows, key=lambda x: (-x[2], x[1]))
        # 同一个 q 的不同余数类互斥，只保留最高容量层附近，控制组合爆炸。
        best_cap = choices[0][2]
        choices = [row for row in choices if row[2] >= max(1, best_cap - 1)]
        rows.append((q, choices[:beam]))
    rows.sort(key=lambda item: (-max(row[2] for row in item[1]), item[0]))

    states = [(0, 1.0, [])]  # saving, 负log权重代理, chosen
    finished = []
    for q, choices in rows:
        new_states = states[:]
        for saving, score, chosen in states:
            for row in choices:
                _, residue, cap, hit_indices, hit_values = row
                ns = saving + cap
                nscore = score * q
                nchosen = chosen + [(q, residue, cap, hit_indices, hit_values)]
                if ns >= target_saving:
                    finished.append((nscore, ns, nchosen))
                else:
                    new_states.append((ns, nscore, nchosen))
        # 保留较大 saving、较小模数乘积的候选。
        new_states.sort(key=lambda x: (-x[0], x[1]))
        states = new_states[:limit]
        finished.sort(key=lambda x: (x[0], -x[1]))
        finished = finished[:limit]
    return [chosen for _, _, chosen in finished[:limit]]


def anchor_counts_for_skeleton(skeleton, c, primes, prime_set):
    """统计一个骨架在 P 范围内的整数锚点和素锚点数量。"""
    lam = c % M
    mod = M
    q_set = {q for q, *_ in skeleton}
    for q, residue, *_ in skeleton:
        if math.gcd(mod, q) != 1:
            return None
        lam, mod = crt_pair(lam, mod, residue % q, q)
    integer_hits = 0
    prime_hits = 0
    for P in primes:
        if P in q_set:
            continue
        a = (-lam * (P % mod)) % mod
        if a == 0:
            a = mod
        if a < P:
            integer_hits += 1
            if a in prime_set:
                prime_hits += 1
    return integer_hits, prime_hits, mod, lam


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--maxP', type=int, default=1_000_000)
    parser.add_argument('--limit', type=int, default=200)
    parser.add_argument('--beam', type=int, default=8)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.W)
    opts = q_residue_options(holes)
    skeletons = enumerate_weighted_skeletons(opts, args.S, args.limit, args.beam)
    primes = primes_upto(args.maxP)
    prime_set = set(primes)

    total_int = 0
    total_prime = 0
    rows = []
    for skeleton in skeletons:
        counted = anchor_counts_for_skeleton(skeleton, args.c, primes, prime_set)
        if counted is None:
            continue
        integer_hits, prime_hits, mod, lam = counted
        total_int += integer_hits
        total_prime += prime_hits
        rows.append((integer_hits, prime_hits, mod, lam, skeleton))

    ratio = total_prime / total_int if total_int else None
    print('c W S maxP skeletons', args.c, args.W, args.S, args.maxP, len(rows))
    print('total_int', total_int, 'total_prime', total_prime, 'ratio', ratio, '1/log', 1 / math.log(args.maxP))
    for integer_hits, prime_hits, mod, lam, skeleton in rows[:args.show]:
        compact = [(q, residue, cap, hits) for q, residue, cap, hits, _ in skeleton]
        print('row', 'int', integer_hits, 'prime', prime_hits, 'log10L', math.log10(mod), 'lambda', lam, 'skel', compact)


if __name__ == '__main__':
    main()
