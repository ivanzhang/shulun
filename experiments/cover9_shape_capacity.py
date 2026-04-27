#!/usr/bin/env python3
"""cover<=9 的共享形状容量筛。

目标不是证明真实可实现性，而是给出一个必要的组合门槛：
15 个洞若能被 <=target 个补丁素数覆盖，则至少需要 W-target 个覆盖节省。
这里把 q=13 三点簇固定为主三点簇，再枚举其余补丁素数在 B11 前洞中的可能多点共享。

用法示例：
    python3 experiments/cover9_shape_capacity.py --W 15 --limit-q 200 --show 20
    python3 experiments/cover9_shape_capacity.py --W 15 --limit-q 1000 --max-clusters 8 --show 30
"""
import argparse
import math
from collections import defaultdict, Counter

M = 2310
Y = 11


def sieve(n):
    """返回 n 以内素数布尔表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0:1] = b"\x00"
    if n >= 1:
        flags[1:2] = b"\x00"
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            flags[p * p:n + 1:p] = b"\x00" * (((n - p * p) // p) + 1)
    return flags


def primes_upto(n):
    """列出 n 以内素数。"""
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def holes_for_c(c, W):
    """给定 B11 平移 c，取前 W 个 B11 前洞高度。"""
    holes = []
    r = 1
    while len(holes) < W:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return holes


def triples_for_13(W):
    """枚举 q=13 三点及以上模板。"""
    out = []
    for c in range(M):
        holes = holes_for_c(c, W)
        by = defaultdict(list)
        for r in holes:
            by[r % 13].append(r)
        for residue, rows in by.items():
            if len(rows) >= 3:
                out.append((c, tuple(holes), residue, tuple(rows)))
    return out


def shared_clusters(holes, limit_q):
    """枚举每个 q 在该窗口内可共享的同余类簇。"""
    clusters = []
    for q in primes_upto(limit_q):
        if q <= Y or q == 13:
            continue
        by = defaultdict(list)
        for idx, r in enumerate(holes):
            by[r % q].append(idx)
        for residue, idxs in by.items():
            if len(idxs) >= 2:
                mask = sum(1 << i for i in idxs)
                clusters.append((q, residue, tuple(idxs), mask, len(idxs) - 1))
    clusters.sort(key=lambda x: (-x[4], x[0], x[1]))
    return clusters


def min_cover_with_q_mutex(base_mask, clusters, W):
    """在同一个 q 只能选择一个余数簇的约束下求理论最小 cover。

    未被共享簇覆盖的洞允许用专属补丁素数单点覆盖，因此目标函数是：
        已选共享簇数 + 未覆盖洞数。
    这给出 cover<=9 是否在组合形状层面可能的必要条件。
    """
    by_q = defaultdict(list)
    for q, residue, idxs, mask, gain in clusters:
        by_q[q].append((q, residue, idxs, mask, gain))
    groups = sorted(by_q.items(), key=lambda item: item[0])
    full = (1 << W) - 1
    best = {'cover': 1 + (full ^ base_mask).bit_count(), 'chosen': [13], 'mask': base_mask}

    # 后缀可覆盖掩码用于剪枝。
    suffix = [0] * (len(groups) + 1)
    for i in range(len(groups) - 1, -1, -1):
        suffix[i] = suffix[i + 1]
        for item in groups[i][1]:
            suffix[i] |= item[3]

    def dfs(i, covered, chosen):
        current_cover = len(chosen) + (full ^ covered).bit_count()
        if current_cover < best['cover']:
            best['cover'] = current_cover
            best['chosen'] = chosen[:]
            best['mask'] = covered
        if i == len(groups):
            return
        # 即使未来全覆盖，已选数量也不能优于当前最好时剪枝。
        if len(chosen) >= best['cover']:
            return
        # 剩余 q 全选也只能覆盖 suffix；由此得一个乐观下界。
        optimistic_mask = covered | suffix[i]
        optimistic_cover = len(chosen) + (full ^ optimistic_mask).bit_count()
        if optimistic_cover >= best['cover']:
            return
        q, options = groups[i]
        # 不选该 q。
        dfs(i + 1, covered, chosen)
        # 选该 q 的一个余数簇；只有新增至少 2 个洞才可能降低 cover。
        for item in sorted(options, key=lambda x: -((x[3] & ~covered).bit_count())):
            new_gain = (item[3] & ~covered).bit_count()
            if new_gain >= 2:
                dfs(i + 1, covered | item[3], chosen + [item])

    dfs(0, base_mask, [13])
    return best


def search(args):
    need_saving = args.W - args.target
    rows = []
    hist = Counter()
    for c, holes, residue13, triple_rows in triples_for_13(args.W):
        base_idxs = tuple(i for i, r in enumerate(holes) if r % 13 == residue13)
        base_mask = sum(1 << i for i in base_idxs)
        clusters = shared_clusters(holes, args.limit_q)

        # 只保留与 q=13 三点不完全重复且能贡献新增共享的簇。
        useful = []
        for item in clusters:
            q, residue, idxs, mask, gain = item
            new_count = (mask & ~base_mask).bit_count()
            if new_count >= 1 and mask != base_mask:
                useful.append(item)

        best = min_cover_with_q_mutex(base_mask, useful, args.W)
        if best['cover'] <= args.target:
            status = 'candidate'
        else:
            status = 'blocked_by_capacity'
        hist[status] += 1

        # 记录最危险：理论 cover 最低、低 q 簇最多。
        top = useful[:args.max_clusters]
        pair_count = sum(1 for x in useful if x[4] == 1)
        high_count = sum(1 for x in useful if x[4] >= 2)
        rows.append({
            'status': status,
            'c': c,
            'holes': holes,
            'residue13': residue13,
            'triple_rows': triple_rows,
            'base_size': len(base_idxs),
            'best_cover': best['cover'],
            'best_mask_count': best['mask'].bit_count(),
            'best_chosen': tuple(best['chosen']),
            'pair_count': pair_count,
            'high_count': high_count,
            'top': top,
        })
    rows.sort(key=lambda r: (r['status'] != 'candidate', r['best_cover'], -r['best_mask_count'], -r['high_count'], r['c']))
    print('W', args.W, 'target', args.target, 'limit_q', args.limit_q, 'templates', len(rows), 'need_saving', need_saving, 'hist', sorted(hist.items()))
    print('rank status c residue13 base_size best_cover best_mask_count chosen_clusters pair_count high_count holes triple_rows top_clusters')
    for rank, row in enumerate(rows[:args.show], 1):
        top_clusters = [(q, residue, tuple(row['holes'][i] for i in idxs), gain) for q, residue, idxs, mask, gain in row['top']]
        chosen_clusters = []
        for item in row['best_chosen']:
            if item == 13:
                chosen_clusters.append(13)
            else:
                q, residue, idxs, mask, gain = item
                chosen_clusters.append((q, residue, tuple(row['holes'][i] for i in idxs)))
        print(rank, row['status'], row['c'], row['residue13'], row['base_size'], row['best_cover'], row['best_mask_count'], chosen_clusters, row['pair_count'], row['high_count'], row['holes'], row['triple_rows'], top_clusters)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--W', type=int, default=15)
    parser.add_argument('--limit-q', type=int, default=200)
    parser.add_argument('--max-clusters', type=int, default=10)
    parser.add_argument('--show', type=int, default=20)
    parser.add_argument('--target', type=int, default=9)
    args = parser.parse_args()
    search(args)


if __name__ == '__main__':
    main()
