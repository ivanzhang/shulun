#!/usr/bin/env python3
"""长段累计 cover 贪心/局部搜索模型。

精确求大 T 的 set cover 较难。本脚本在 B11 形状模型中构造 q->洞掩码，
用贪心给出上界，并输出覆盖规模、q数量、覆盖效率。
用于观察全列累计 cover 是否可能低于/高于局部比例。

用法示例：
    python3 experiments/cumulative_cover_greedy.py --c 1213 --T 200
    python3 experiments/cumulative_cover_greedy.py --Tlist 50,100,200,400 --c 1213
"""
import argparse
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto

Y = 11


def build_masks(holes):
    D = max(holes) - min(holes)
    q_masks = {}
    for q in [p for p in primes_upto(D) if p > Y]:
        by = defaultdict(list)
        for i, r in enumerate(holes):
            by[r % q].append(i)
        # 形状模型中每个 q 只能选一个余数类，取每个余数类作为一个选项。
        options = []
        for residue, idxs in by.items():
            if len(idxs) >= 2:
                mask = 0
                for i in idxs:
                    mask |= 1 << i
                options.append((residue, mask, len(idxs)))
        if options:
            q_masks[q] = options
    return q_masks


def greedy_cover(T, q_masks):
    full = (1 << T) - 1
    covered = 0
    chosen = []
    used_q = set()
    while covered != full:
        best = None
        best_gain = 0
        for q, options in q_masks.items():
            if q in used_q:
                continue
            for residue, mask, size in options:
                gain = (mask & ~covered).bit_count()
                if gain > best_gain:
                    best_gain = gain
                    best = (q, residue, mask, size)
        if best is None or best_gain < 2:
            break
        q, residue, mask, size = best
        chosen.append((q, residue, best_gain, size))
        used_q.add(q)
        covered |= mask
    singles = T - covered.bit_count()
    return chosen, singles, covered.bit_count()


def run(c, T):
    holes = holes_for_c(c, T)
    q_masks = build_masks(holes)
    chosen, singles, shared_covered = greedy_cover(T, q_masks)
    cover = len(chosen) + singles
    q_product_count = len(chosen)
    return {
        'c': c,
        'T': T,
        'D': max(holes) - min(holes),
        'cover': cover,
        'ratio': cover / T,
        'shared_q': q_product_count,
        'singles': singles,
        'shared_covered': shared_covered,
        'chosen': chosen,
        'holes_first_last': (holes[0], holes[-1]),
    }


def print_rec(rec, detail=False):
    print('c', rec['c'], 'T', rec['T'], 'D', rec['D'], 'cover_greedy', rec['cover'], 'ratio', f'{rec["ratio"]:.6f}', 'shared_q', rec['shared_q'], 'singles', rec['singles'], 'shared_covered', rec['shared_covered'], 'holes', rec['holes_first_last'])
    if detail:
        print('chosen', rec['chosen'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--T', type=int, default=200)
    parser.add_argument('--Tlist', default='')
    parser.add_argument('--detail', action='store_true')
    args = parser.parse_args()
    Ts = [int(x) for x in args.Tlist.split(',') if x.strip()] if args.Tlist else [args.T]
    for T in Ts:
        print_rec(run(args.c, T), detail=args.detail)


if __name__ == '__main__':
    main()
