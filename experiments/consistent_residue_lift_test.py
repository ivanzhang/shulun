#!/usr/bin/env python3
"""H>=4 一致残基见证的整数 lift 测试。

先枚举模 2310 一致模型中 H>=threshold 的 (Pmod, amod, c) 见证；
再在实际素数 P<=maxP、第一行素数锚点 a<P 中搜索同残基类，检查对应 15 洞是否全合数、
实际 anchor_hits/cover/raw_repeats 如何。

用法示例：
  python3 experiments/consistent_residue_lift_test.py --maxP 300000 --threshold 4 --limit-classes 30 --max-a-per-class 200
"""
import argparse
import math
import sys
from collections import defaultdict, Counter

sys.path.append('experiments')
from fixed_anchor_sieve_remainder import primes_upto, sieve
from hole_index_prime_rate import factor, isprimefac

Y = 11
M = 2310


def holes_for_c(c, count):
    """生成 B11 模板 c 的前 count 个洞高。"""
    holes = []
    r = 1
    while len(holes) < count:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def gt_y_prime_factors(n, y=Y):
    """返回 n 的大于 y 的不同素因子。"""
    out = []
    x = n
    for p in primes_upto(math.isqrt(x) + 1):
        if p * p > x:
            break
        if x % p == 0:
            if p > y:
                out.append(p)
            while x % p == 0:
                x //= p
    if x > 1 and x > y:
        out.append(x)
    return out


def candidate_hits(Pmod, amod, holes):
    """一致残基模型的 H 命中。"""
    hits = []
    for i, r in enumerate(holes):
        for j in range(i + 1, len(holes)):
            diff = holes[j] - r
            for q in gt_y_prime_factors(diff):
                required = (-r * (Pmod % q)) % q
                if required and (amod - required) % q == 0:
                    hits.append((i, j, diff, q, required))
    return hits


def residue_classes(threshold, W, limit):
    """枚举 H>=threshold 的一致残基类。"""
    units = [x for x in range(M) if math.gcd(x, M) == 1]
    recs = []
    for Pmod in units:
        invP = pow(Pmod, -1, M)
        for amod in units:
            c = (-amod * invP) % M
            holes = holes_for_c(c, W)
            hits = candidate_hits(Pmod, amod, holes)
            if len(hits) >= threshold:
                recs.append((len(hits), Pmod, amod, c, holes, hits))
    recs.sort(reverse=True, key=lambda x: x[0])
    return recs[:limit]


def patch_set(n, P):
    """返回 n 的有效补丁素数集合。"""
    root = math.isqrt(n)
    return tuple(q for q, _ in factor(n) if q > Y and q <= root and q != P)


def exact_cover_size(sets):
    """小窗口精确覆盖数。"""
    q_to_idx = defaultdict(set)
    for idx, qs in enumerate(sets):
        for q in qs:
            q_to_idx[q].add(idx)
    uncovered = set(range(len(sets)))
    greedy = []
    while uncovered:
        q, hits = max(q_to_idx.items(), key=lambda item: len(item[1] & uncovered))
        greedy.append(q)
        uncovered -= hits
    best = {'size': len(greedy)}
    def lb(uncovered_set):
        max_gain = max((len(v & uncovered_set) for v in q_to_idx.values()), default=1)
        return math.ceil(len(uncovered_set) / max(1, max_gain))
    def search(uncovered_set, size):
        if not uncovered_set:
            best['size'] = min(best['size'], size); return
        if size + lb(uncovered_set) >= best['size']:
            return
        idx = min(uncovered_set, key=lambda i: len(tuple(sets[i])))
        for q in sorted(sets[idx], key=lambda x: -len(q_to_idx[x] & uncovered_set)):
            search(uncovered_set - q_to_idx[q], size + 1)
    search(set(range(len(sets))), 0)
    return best['size']


def actual_window_stats(P, a, holes):
    """实际 P,a 下窗口统计。"""
    sets = []
    prime_positions = []
    for idx, r in enumerate(holes, start=1):
        n = a + r * P
        fac = factor(n)
        if isprimefac(fac, n):
            prime_positions.append(idx)
            sets.append(())
        else:
            sets.append(patch_set(n, P))
    all_composite = not prime_positions and all(sets)
    if not all_composite:
        return {'all_composite': False, 'prime_positions': prime_positions, 'cover': None, 'raw_repeats': None, 'anchor_hits': None, 'sets': sets}
    incidence = sum(len(s) for s in sets)
    distinct = len({q for s in sets for q in s})
    # 实际共享边数由共同补丁决定。
    anchor_hits = 0
    for i in range(len(holes)):
        for j in range(i + 1, len(holes)):
            anchor_hits += len(set(sets[i]) & set(sets[j]))
    return {'all_composite': True, 'prime_positions': [], 'cover': exact_cover_size(sets), 'raw_repeats': incidence - distinct, 'anchor_hits': anchor_hits, 'sets': sets}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=300000)
    parser.add_argument('--threshold', type=int, default=4)
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--limit-classes', type=int, default=30)
    parser.add_argument('--max-a-per-class', type=int, default=200)
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    flags = sieve(args.maxP * (args.W * 8 + 100) + args.maxP)
    primes = [p for p in primes_upto(args.maxP) if p > M]
    primes_by_mod = defaultdict(list)
    for p in primes:
        primes_by_mod[p % M].append(p)

    classes = residue_classes(args.threshold, args.W, args.limit_classes)
    print('classes', len(classes), 'maxP', args.maxP)
    results = []
    for H, Pmod, amod, c, holes, hits in classes:
        Ps = primes_by_mod.get(Pmod, [])
        tested = 0
        full = 0
        best_cover = None
        best = None
        prime_fail_counter = Counter()
        for P in Ps:
            # 只取该残基类下前若干素数锚点，控制时间。
            a_count = 0
            for a in primes_by_mod.get(amod, []):
                if a >= P:
                    break
                a_count += 1
                if a_count > args.max_a_per_class:
                    break
                tested += 1
                st = actual_window_stats(P, a, holes)
                if st['all_composite']:
                    full += 1
                    if best_cover is None or st['cover'] < best_cover:
                        best_cover = st['cover']
                        best = (P, a, st)
                else:
                    for pos in st['prime_positions'][:1]:
                        prime_fail_counter[pos] += 1
        results.append((H, Pmod, amod, c, len(Ps), tested, full, best_cover, best, holes, hits, prime_fail_counter))

    print('H Pmod amod c Ps tested full_all_composite best_cover best_P_a first_prime_fail hits holes')
    for row in results[:args.show]:
        H, Pmod, amod, c, pcount, tested, full, best_cover, best, holes, hits, fail_counter = row
        best_pa = None if best is None else (best[0], best[1], best[2]['raw_repeats'], best[2]['anchor_hits'])
        print(H, Pmod, amod, c, pcount, tested, full, best_cover, best_pa, fail_counter.most_common(5), hits, holes)


if __name__ == '__main__':
    main()
