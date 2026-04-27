#!/usr/bin/env python3
"""极端差分链的 CRT 模数增长剖面。

输出固定 c 下，最优形状链随 T 的 cover 比例、选择簇数、CRT 模数 L、以及 L/P^2 直观阈值。

用法示例：
    python3 experiments/lift_modulus_growth_profile.py --c 1213 --Tmin 15 --Tmax 40
"""
import argparse
import math
import sys

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c, min_cover_fast
from difference_chain_lift_obstruction import skeleton_lambda


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=1213)
    parser.add_argument('--Tmin', type=int, default=15)
    parser.add_argument('--Tmax', type=int, default=40)
    args = parser.parse_args()

    print('T cover ratio chosen_count log10L sqrtL max_q chosen_qs')
    for T in range(args.Tmin, args.Tmax + 1):
        holes = holes_for_c(args.c, T)
        best = min_cover_fast(holes)
        lam, modulus = skeleton_lambda(args.c, best['chosen'])
        qs = [q for q, _res, _idxs, _mask in best['chosen']]
        print(
            T,
            best['cover'],
            f'{best["cover"]/T:.6f}',
            len(qs),
            f'{math.log10(modulus):.3f}',
            int(math.isqrt(modulus)),
            max(qs) if qs else 0,
            ','.join(map(str, qs)),
            flush=True,
        )


if __name__ == '__main__':
    main()
