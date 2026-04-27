#!/usr/bin/env python3
"""§203 c-级 M_kill 解析上界。

对固定 c, W，定义不依赖具体 (prefix, P) 的"c-级最坏 M_kill 上界"：

    M_kill_c_upper(c, W, used, last_cap) = Σ_{q ∉ used} min(last_cap, max_r H_holes(q,r) - 1)

它是 §201 解析公式在最坏 r_unkill_q 选择下的上界，仅依赖 c 与 used、last_cap，
完全不依赖 prefix 的具体 (q,r) 选择或 P_witness 的具体值。

进一步，对 (used, last_cap) 取若干典型组合（由 N_{c, k_low} 的结构给出），
取最大 M_kill_c_upper，比较是否 < min(need)。

用法：
    python3 experiments/c_level_kill_quota_bound.py --c 2309 --W 100 --S 55 \
        --kRange 7,8,9,10
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto

Y = 11


def holes_caps_per_q(holes: tuple[int, ...]) -> dict[int, list[tuple[int, int]]]:
    """对每个 q 返回 [(r, H_holes(q, r))] 列表，仅保留 H≥2 项。"""
    D = max(holes) - min(holes)
    out: dict[int, list[tuple[int, int]]] = {}
    for q in [p for p in primes_upto(D) if p > Y]:
        counts = defaultdict(int)
        for h in holes:
            counts[h % q] += 1
        hot = [(r, h) for r, h in counts.items() if h >= 2]
        if hot:
            out[q] = sorted(hot, key=lambda x: -x[1])
    return out


def c_level_M_kill_upper(per_q_caps: dict[int, list[tuple[int, int]]],
                         used_qs: set[int], last_cap: int) -> tuple[int, list]:
    """对固定 (used, last_cap) 计算 M_kill 的 c-级最坏 r 上界。"""
    total = 0
    contrib = []
    for q, hot_list in per_q_caps.items():
        if q in used_qs:
            continue
        # 取最大 H 的 r 作为最坏 r_unkill_q
        max_h = hot_list[0][1]
        cap = min(last_cap, max_h - 1)
        if cap > 0:
            contrib.append((q, hot_list[0][0], max_h, cap))
            total += cap
    return total, contrib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--kRange', default='7,8,9,10',
                        help='验证 k_low 列表')
    parser.add_argument('--show', type=int, default=20)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.W)
    per_q = holes_caps_per_q(holes)

    print(f'c={args.c} W={args.W} |holes|={len(holes)} D={max(holes)-min(holes)}')
    print(f'q 数量（含 hot 命中）: {len(per_q)}')
    print()

    # 全 c-级上界（used=∅）
    print('--- 不含 used 限制的 c-级上界 ---')
    for last_cap in [2, 3, 4, 5, 8]:
        total, _ = c_level_M_kill_upper(per_q, set(), last_cap)
        print(f'  last_cap={last_cap}: M_kill ≤ {total}')

    print()
    print('--- 假定典型 used_qs（前 k 素数 + 选定）---')
    # 假设 k 层 prefix 用前 k 个素数（>Y）
    primes_above_Y = sorted(per_q.keys())
    for k_low in [int(x) for x in args.kRange.split(',')]:
        used = set(primes_above_Y[:k_low])
        for last_cap in [2, 3, 4]:
            total, contrib = c_level_M_kill_upper(per_q, used, last_cap)
            print(f'  k_low={k_low} (used=top-{k_low}) last_cap={last_cap}: '
                  f'M_kill ≤ {total} (contrib_q={len(contrib)})')

    # 给出"need 下界"：用最高 cap 排序前 k_low 项的 saving 上界
    # k_low 层最大 prefix_saving = sum top k_low cap = ?
    print()
    print('--- 各 k_low 层 prefix_saving 与 need 的代表值（用 top-cap-q 估计） ---')
    # 取每 q 的 max cap，按降序求前 k_low 的和
    max_cap_per_q = sorted([h[0][1] - 1 for h in per_q.values()], reverse=True)
    print(f'all q max cap (降序前 20): {max_cap_per_q[:20]}')
    print(f'k_low | sum_top_caps | need=S-sum')
    for k_low in [int(x) for x in args.kRange.split(',')]:
        s = sum(max_cap_per_q[:k_low])
        print(f'  {k_low:3d}  |  {s:3d}  |  {args.S - s:3d}')


if __name__ == '__main__':
    main()
