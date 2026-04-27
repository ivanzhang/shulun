#!/usr/bin/env python3
"""a 空间候选递减分析。

固定 P,y，逐步增加 R。称 a 是 R-满补洞候选，如果小骨架洞集中每个洞都被中等补丁命中。
观察候选集合 A_R 如何随 R 收缩，以及最终只剩最坏 a 的机制。

用法示例：
    python3 experiments/a_space_candidate_decay.py --P 461 --y 13 --Rmax 100
    python3 experiments/a_space_candidate_decay.py --P 461 --y 13 --Rmax 100 --detail
"""
import argparse
from positive_negative_congruence import stats_for_a


def candidate_as(P, R, y):
    out = []
    for a in range(1, P + 1):
        st = stats_for_a(P, a, R, y)
        if st['holes'] > 0 and st['unpatched'] == 0:
            out.append((a, st['holes'], st['patched'], st['patch_hits']))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--P', type=int, default=461)
    ap.add_argument('--y', type=int, default=13)
    ap.add_argument('--Rmax', type=int, default=100)
    ap.add_argument('--detail', action='store_true')
    args = ap.parse_args()

    prev = None
    for R in range(1, args.Rmax + 1):
        cand = candidate_as(args.P, R, args.y)
        aset = {a for a, _, _, _ in cand}
        lost = sorted(prev - aset) if prev is not None else []
        gained = sorted(aset - prev) if prev is not None else sorted(aset)
        if args.detail or R <= 10 or lost or gained or R == args.Rmax:
            sample = cand[:20]
            print(f"R={R},count={len(cand)},lost={lost[:20]},gained={gained[:20]},sample={sample}")
        prev = aset

if __name__ == '__main__':
    main()
