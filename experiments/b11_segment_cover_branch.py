#!/usr/bin/env python3
"""B11 长段形状 cover 的快速分支定界。

目标函数 cover = 已选共享簇数 + 未覆盖点数。
等价最大化 saving = 覆盖点数 - 已选共享簇数。
每个素数 q 最多选择一个余数簇。

用法示例：
    python3 experiments/b11_segment_cover_branch.py --T 25 --show 10
    python3 experiments/b11_segment_cover_branch.py --Tmin 15 --Tmax 35 --summary
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
    if n < 2:
        return []
    flags = sieve(n)
    return [i for i in range(2, n + 1) if flags[i]]


def holes_for_c(c, T):
    """给定 B11 平移 c，取前 T 个 B11 前洞高度。"""
    holes = []
    r = 1
    while len(holes) < T:
        if math.gcd((r - c) % M, M) == 1:
            holes.append(r)
        r += 1
    return tuple(holes)


def groups_for_holes(holes):
    """按 q 构造所有多点余数簇。"""
    span = max(holes) - min(holes)
    groups = []
    for q in primes_upto(span):
        if q <= Y:
            continue
        by = defaultdict(list)
        for idx, r in enumerate(holes):
            by[r % q].append(idx)
        options = []
        for residue, idxs in by.items():
            if len(idxs) >= 2:
                mask = sum(1 << i for i in idxs)
                options.append((q, residue, tuple(idxs), mask))
        if options:
            options.sort(key=lambda x: (-x[3].bit_count(), x[1]))
            groups.append((q, options))
    # 大簇优先、再按 q 小优先。
    groups.sort(key=lambda item: (-max(opt[3].bit_count() - 1 for opt in item[1]), item[0]))
    return groups


def greedy_initial(T, groups):
    """给出一个快速可行 saving 下界。"""
    covered = 0
    saving = 0
    chosen = []
    for q, options in groups:
        best = None
        best_gain = 0
        for opt in options:
            gain = (opt[3] & ~covered).bit_count()
            if gain > best_gain:
                best_gain = gain
                best = opt
        if best_gain >= 2:
            covered |= best[3]
            saving += best_gain - 1
            chosen.append(best)
    return saving, covered, chosen


def min_cover_fast(holes):
    """返回长段理论最小 cover。"""
    T = len(holes)
    groups = groups_for_holes(holes)
    greedy_saving, greedy_mask, greedy_chosen = greedy_initial(T, groups)
    best = {'saving': greedy_saving, 'mask': greedy_mask, 'chosen': greedy_chosen, 'nodes': 0}

    # 后缀可覆盖掩码与后缀最大乐观节省。
    suffix_mask = [0] * (len(groups) + 1)
    suffix_raw_saving = [0] * (len(groups) + 1)
    for i in range(len(groups) - 1, -1, -1):
        suffix_mask[i] = suffix_mask[i + 1]
        max_raw = 0
        for opt in groups[i][1]:
            suffix_mask[i] |= opt[3]
            max_raw = max(max_raw, opt[3].bit_count() - 1)
        suffix_raw_saving[i] = suffix_raw_saving[i + 1] + max_raw

    def dfs(i, covered, saving, chosen):
        best['nodes'] += 1
        if saving > best['saving']:
            best['saving'] = saving
            best['mask'] = covered
            best['chosen'] = chosen[:]
        if i == len(groups):
            return
        # 乐观上界1：未来每个 q 取其原始最大节省。
        if saving + suffix_raw_saving[i] <= best['saving']:
            return
        # 乐观上界2：未来最多新增 suffix_mask 中尚未覆盖的点，每选一簇至少花1，先用宽松上界。
        if saving + (suffix_mask[i] & ~covered).bit_count() <= best['saving']:
            return

        q, options = groups[i]
        # 先尝试能产生最大新增的选项。
        ordered = []
        for opt in options:
            gain = (opt[3] & ~covered).bit_count()
            if gain >= 2:
                ordered.append((gain, opt))
        ordered.sort(key=lambda x: (-x[0], x[1][1]))
        for gain, opt in ordered:
            dfs(i + 1, covered | opt[3], saving + gain - 1, chosen + [opt])
        # 不选该 q。
        dfs(i + 1, covered, saving, chosen)

    dfs(0, 0, 0, [])
    cover = T - best['saving']
    return {
        'cover': cover,
        'saving': best['saving'],
        'covered': best['mask'].bit_count(),
        'chosen': best['chosen'],
        'nodes': best['nodes'],
        'groups': len(groups),
    }


def scan_T(T, show):
    hist = Counter()
    rows = []
    for c in range(M):
        holes = holes_for_c(c, T)
        best = min_cover_fast(holes)
        hist[best['cover']] += 1
        chosen = [(q, res, tuple(holes[i] for i in idxs)) for q, res, idxs, _mask in best['chosen']]
        rows.append((best['cover'], -best['covered'], c, holes, chosen, best['nodes'], best['groups']))
    rows.sort()
    return hist, rows[:show]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--T', type=int, default=25)
    parser.add_argument('--Tmin', type=int, default=15)
    parser.add_argument('--Tmax', type=int, default=30)
    parser.add_argument('--show', type=int, default=10)
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args()

    if args.summary:
        print('T min_cover ratio hist', flush=True)
        for T in range(args.Tmin, args.Tmax + 1):
            hist, _ = scan_T(T, 0)
            m = min(hist)
            compact = ','.join(f'{k}:{v}' for k, v in sorted(hist.items()))
            print(T, m, f'{m/T:.6f}', compact, flush=True)
        return

    hist, rows = scan_T(args.T, args.show)
    m = min(hist)
    print('T', args.T, 'min_cover', m, 'ratio', f'{m/args.T:.6f}', 'hist', sorted(hist.items()))
    print('rank cover covered c nodes groups holes chosen')
    for rank, (cover, neg_cov, c, holes, chosen, nodes, groups) in enumerate(rows, 1):
        print(rank, cover, -neg_cov, c, nodes, groups, holes, chosen)


if __name__ == '__main__':
    main()
