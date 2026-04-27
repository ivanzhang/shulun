#!/usr/bin/env python3
"""§201 解析杀死配额：用洞集合 mod q 的命中数直接给出 M_kill。

核心观察（§200.12 + 洞结构化）：
  M_kill(prefix, P) = Σ_{q ∉ used} max(0, H_holes(q, r_unkill_q(prefix, P)) − 1)
其中
  r_unkill_q(prefix, P) = (−A_old · P^{−1}) mod q,
  H_holes(q, r) = #{h ∈ holes_for_c(c, W) : h mod q = r}.

这把 §200.12 的"对 flat 单点查询"再压缩为"对 holes 取模计数"，完全摆脱
prefix_phase + prefix_anchor 的递归。

用法：
    python3 experiments/analytic_kill_quota.py --c 2309 --W 100 \
        --prefixSaving 46 --A 494868 --P 568787 --used 13,17,19,23,29,31,37,41,43,53
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import Counter

sys.path.append('experiments')
from b11_segment_cover_branch import holes_for_c
from fixed_anchor_sieve_remainder import primes_upto


Y = 11


def holes_count_at_residue(holes: tuple[int, ...], q: int, r: int) -> int:
    """计数 holes 中 ≡ r (mod q) 的洞数。"""
    return sum(1 for h in holes if h % q == r)


def analytic_M_kill(holes, A_old: int, witness_P: int, used_qs: set[int],
                    last_cap: int, q_max: int | None = None) -> dict:
    """对一个 (prefix 概要, P) 计算 M_kill 解析上界。

    输入：
      holes：洞集合（来自 holes_for_c(c, W)）
      A_old：当前 anchor
      witness_P：证人素数
      used_qs：已用 q 集合
      last_cap：cap 上界（cap ≤ last_cap）
      q_max：q 扫描上界（默认为 max(holes)−min(holes) 即 q_residue_options 的范围）

    输出：M_kill 与逐 q 贡献。
    """
    if q_max is None:
        q_max = max(holes) - min(holes)
    primes = [p for p in primes_upto(q_max) if p > Y]
    contributions = []
    M_kill = 0
    for q in primes:
        if q in used_qs:
            continue
        try:
            P_inv = pow(witness_P % q, -1, q)
        except ValueError:
            continue  # P 与 q 不互素（罕见）
        r_unkill = (-A_old * P_inv) % q
        H = holes_count_at_residue(holes, q, r_unkill)
        cap = max(0, H - 1)
        cap_used = min(cap, last_cap)
        if cap_used > 0:
            contributions.append((q, r_unkill, H, cap_used))
            M_kill += cap_used
    return {
        'M_kill': M_kill,
        'q_count_scanned': len(primes) - len(used_qs.intersection(primes)),
        'q_count_contributing': len(contributions),
        'contributions': contributions,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--c', type=int, default=2309)
    parser.add_argument('--W', type=int, default=100)
    parser.add_argument('--A', type=int, required=False, default=494868,
                        help='当前 anchor A_old')
    parser.add_argument('--P', type=int, required=False, default=568787,
                        help='证人素数')
    parser.add_argument('--used', default='13,17,19,23,29,31,37,41,43,53',
                        help='已用 q 列表，逗号分隔')
    parser.add_argument('--lastCap', type=int, default=3)
    parser.add_argument('--prefixSaving', type=int, default=46)
    parser.add_argument('--S', type=int, default=55)
    parser.add_argument('--show', type=int, default=15)
    args = parser.parse_args()

    holes = holes_for_c(args.c, args.W)
    used_qs = {int(x) for x in args.used.split(',') if x}
    result = analytic_M_kill(holes, args.A, args.P, used_qs, args.lastCap)

    need = args.S - args.prefixSaving
    print(f'c={args.c} W={args.W} A={args.A} P={args.P}')
    print(f'used_qs={sorted(used_qs)} last_cap={args.lastCap}')
    print(f'prefix_saving={args.prefixSaving} need_saving={need}')
    print()
    print(f'M_kill={result["M_kill"]} need={need} '
          f'passes={result["M_kill"] < need}')
    print(f'q 扫描数={result["q_count_scanned"]} '
          f'有贡献 q 数={result["q_count_contributing"]}')
    print(f'前 {args.show} 个 q 贡献：')
    for q, r_u, H, cap in result['contributions'][:args.show]:
        print(f'  q={q} r_unkill={r_u} H_holes={H} cap_used={cap}')


if __name__ == '__main__':
    main()
