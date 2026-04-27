#!/usr/bin/env python3
"""B11 横截面差分链剖面。

不是只看 cover 数量，而是追踪极端覆盖形状中每条共享簇对应的差分 q，
观察这些差分链能否随 T 长程延伸。

用法示例：
    python3 experiments/difference_chain_profile.py --c 1213 --Tmax 80
    python3 experiments/difference_chain_profile.py --c 1182 --Tmax 80
"""
import argparse
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c, min_cover_fast


def profile(c, Tmin, Tmax):
    print('T cover ratio covered saving max_cluster chosen_count chain_signature')
    for T in range(Tmin, Tmax + 1):
        holes = holes_for_c(c, T)
        best = min_cover_fast(holes)
        clusters = []
        max_cluster = 0
        for q, res, idxs, _mask in best['chosen']:
            rs = tuple(holes[i] for i in idxs)
            max_cluster = max(max_cluster, len(rs))
            clusters.append((q, len(rs), rs[0], rs[-1]))
        clusters.sort(key=lambda x: (x[0], x[2]))
        signature = ','.join(f'{q}:{k}:{a}-{b}' for q, k, a, b in clusters)
        print(T, best['cover'], f'{best["cover"]/T:.6f}', best['covered'], best['saving'], max_cluster, len(best['chosen']), signature, flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--Tmin', type=int, default=15)
    parser.add_argument('--Tmax', type=int, default=80)
    args = parser.parse_args()
    profile(args.c, args.Tmin, args.Tmax)


if __name__ == '__main__':
    main()
