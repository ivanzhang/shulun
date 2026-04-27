#!/usr/bin/env python3
"""五线骨架 lift 扫描。

第165节把 cover<=9 的必要形状压缩为 12 个模板族：
B11 模板 + q=13 三点簇 + 四个二点共享簇。
本脚本把这些共享簇转成 CRT 约束：
    a + rP == 0 (mod q)
并扫描素数 P 与第一行素数锚点 a，检查是否能形成真实 15 洞全合数窗口，
以及真实集合覆盖数是否达到 9。

用法示例：
    python3 experiments/five_line_lift_scan.py --maxP 200000 --show 20
    python3 experiments/five_line_lift_scan.py --maxP 500000 --show 20
"""
import argparse
import math
import sys
from collections import Counter, defaultdict

sys.path.append('experiments')
from cover9_shape_capacity import M, Y, triples_for_13, shared_clusters, min_cover_with_q_mutex
from fixed_anchor_sieve_remainder import primes_upto
from local_cover_min_scan import exact_cover_size

SKELETON_Q_LIMIT = 1000
SKELETON_MODS = (13, 17, 19, 23, 31)


def crt_pair(a1, m1, a2, m2):
    """合并两个互素同余。"""
    inv = pow(m1, -1, m2)
    k = ((a2 - a1) * inv) % m2
    return (a1 + m1 * k) % (m1 * m2), m1 * m2


def lambda_for_constraints(c, chosen):
    """求 lambda，使 a == -lambda*P (mod L)。"""
    residue, modulus = c % M, M
    for item in chosen:
        if item == 13:
            continue
        q, qresidue, _idxs, _mask, _gain = item
        residue, modulus = crt_pair(residue, modulus, qresidue % q, q)
    # q=13 的 residue 从 chosen 外部补入；调用方会先替换成具体三点 residue。
    return residue, modulus


def factor_small(n, primes, limit, P):
    """返回 n 的有效补丁素因子集合。"""
    out = []
    x = n
    for p in primes:
        if p > limit or p * p > x:
            break
        if x % p == 0:
            if p > Y and p != P:
                out.append(p)
            while x % p == 0:
                x //= p
    if x > 1 and x <= limit and x > Y and x != P:
        out.append(x)
    return tuple(out)


def patch_sets(P, a, holes, primes):
    """计算窗口补丁集合；若某洞为素数/无补丁则返回 None。"""
    sets = []
    for r in holes:
        n = a + r * P
        qs = factor_small(n, primes, math.isqrt(n), P)
        if not qs:
            return None
        sets.append(qs)
    return sets


def candidate_skeletons():
    """生成第165节 cover=9 组合候选骨架。"""
    rows = []
    for c, holes, residue13, triple_rows in triples_for_13(15):
        base_idxs = tuple(i for i, r in enumerate(holes) if r % 13 == residue13)
        base_mask = sum(1 << i for i in base_idxs)
        useful = []
        for item in shared_clusters(holes, SKELETON_Q_LIMIT):
            _q, _residue, _idxs, mask, _gain = item
            if (mask & ~base_mask).bit_count() >= 1 and mask != base_mask:
                useful.append(item)
        best = min_cover_with_q_mutex(base_mask, useful, 15)
        if best['cover'] <= 9:
            chosen = []
            for item in best['chosen']:
                if item == 13:
                    chosen.append((13, residue13, base_idxs, base_mask, len(base_idxs) - 1))
                else:
                    chosen.append(item)
            rows.append((c, tuple(holes), residue13, tuple(triple_rows), tuple(chosen), best['cover']))
    return rows


def residue_lambda(c, chosen):
    """把 B11 与五线骨架统一成 lambda。"""
    residue, modulus = c % M, M
    for q, qresidue, _idxs, _mask, _gain in chosen:
        residue, modulus = crt_pair(residue, modulus, qresidue % q, q)
    return residue, modulus


def mask_for_q(holes, qs):
    """真实补丁集合中每个 q 覆盖的洞掩码。"""
    qmask = defaultdict(int)
    for idx, patch in enumerate(qs):
        for q in patch:
            qmask[q] |= 1 << idx
    return qmask


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--maxP', type=int, default=200000)
    parser.add_argument('--show', type=int, default=20)
    parser.add_argument('--require-a-prime', action='store_true', default=True)
    args = parser.parse_args()

    prime_list = primes_upto(args.maxP)
    prime_set = set(prime_list)
    factor_primes = primes_upto(math.isqrt(args.maxP * (100 + args.maxP)) + 1000)
    skeletons = candidate_skeletons()

    tested = 0
    prime_anchor = 0
    full = 0
    cover_hist = Counter()
    residue_hit_hist = Counter()
    records = []

    for sk_id, (c, holes, residue13, triple_rows, chosen, model_cover) in enumerate(skeletons, 1):
        lam, modulus = residue_lambda(c, chosen)
        for P in prime_list:
            if P in (2, 3, 5, 7, 11, 13, 17, 19, 23, 31):
                continue
            a0 = (-lam * (P % modulus)) % modulus
            if a0 == 0:
                a0 = modulus
            # a 必须在第一行 1..P，且是第一行根基素数。P 小于骨架模数时最多只有一个 lift。
            a = a0
            while a < P:
                tested += 1
                if args.require_a_prime and a not in prime_set:
                    a += modulus
                    continue
                prime_anchor += 1
                sets = patch_sets(P, a, holes, factor_primes)
                if sets is None:
                    a += modulus
                    continue
                full += 1
                cover = exact_cover_size(sets)
                cover_hist[cover] += 1
                qmask = mask_for_q(holes, sets)
                skeleton_hits = []
                for q, _res, idxs, mask, _gain in chosen:
                    skeleton_hits.append((q, tuple(holes[i] for i in idxs), (qmask.get(q, 0) & mask) == mask))
                residue_hit_hist[sum(1 for _q, _rs, ok in skeleton_hits if ok)] += 1
                shared = {q: [holes[i] for i in range(len(holes)) if (mask >> i) & 1]
                          for q, mask in qmask.items() if mask.bit_count() >= 2}
                records.append((cover, -len(shared), P, a, sk_id, c, residue13, model_cover, holes, skeleton_hits, shared, sets))
                a += modulus

    records.sort(key=lambda row: (row[0], row[1], row[2]))
    print('skeletons', len(skeletons), 'maxP', args.maxP, 'tested', tested, 'prime_anchor', prime_anchor, 'full', full)
    print('cover_hist', sorted(cover_hist.items()), 'skeleton_line_hits_hist', sorted(residue_hit_hist.items()))
    for rank, row in enumerate(records[:args.show], 1):
        cover, neg_shared, P, a, sk_id, c, residue13, model_cover, holes, skeleton_hits, shared, sets = row
        print(rank, 'cover', cover, 'P', P, 'a', a, 'sk', sk_id, 'c', c, 'res13', residue13, 'model', model_cover)
        print('  holes', holes)
        print('  skeleton_hits', skeleton_hits)
        print('  shared', shared)
        print('  sets', sets)


if __name__ == '__main__':
    main()
