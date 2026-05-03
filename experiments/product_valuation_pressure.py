#!/usr/bin/env python3
"""小筛洞乘积的大素数 p-adic 贡献压力分析。

研究 V=prod_{r in H_y(a)} (a+rP) 中 q in (y,P) 的贡献。
若 H_y(a) 全部为合数，则每个 r 至少需要一个 q in (y,P) 整除。
本脚本比较：
- demand_count: 需要覆盖的洞数 |H_y| 或实际合数洞数；
- supply_hits: sum_q #{r in H_y: q | a+rP}；
- supply_log: sum_q v_q(V) log q；
- minimal_log_demand: 若每洞至少一个 q>y，至少需要 |H_y| log y；
- distinct/multiplicity 结构与共享上界。

用法示例：
  python3 experiments/product_valuation_pressure.py --P 1009 --a 720 --ys 101,173,293 --detail
  python3 experiments/product_valuation_pressure.py --P 2003 --a 1019 --ys 173,293,503 --detail
"""
import argparse
import math
from collections import Counter, defaultdict
from rigid_patch_lemma_scan import sieve, primes_from_flags, record_for


def valuation(n, q):
    """计算 q-adic 阶。"""
    v = 0
    while n % q == 0:
        v += 1
        n //= q
    return v


def analyze(P, a, y, flags, root, detail=False):
    rec = record_for(P, a, y, flags, root)
    holes = rec["holes_list"]
    q_hits = defaultdict(list)
    q_val_sum = Counter()
    total_log_all = 0.0
    big_log_supply = 0.0
    big_hit_supply = 0
    for r in holes:
        n = a + r * P
        total_log_all += math.log(n)
        for q in root:
            # 根基素数自身 q 不是合数覆盖贡献，只统计 proper multiple。
            if y < q < P and n != q and n % q == 0:
                v = valuation(n, q)
                q_hits[q].append(r)
                q_val_sum[q] += v
                big_hit_supply += 1
                big_log_supply += v * math.log(q)

    covered = {r for rows in q_hits.values() for r in rows}
    prime_like = len(holes) - len(covered)
    hit_hist = Counter(len(rows) for rows in q_hits.values())
    val_hist = Counter(q_val_sum.values())
    demand_all_log_y = len(holes) * math.log(y)
    demand_comp_log_y = len(covered) * math.log(y)
    # 每个 q 最多覆盖 ceil(P/q) 个洞；实际 supply_hits 已是精确覆盖次数。
    max_reuse = max((len(rows) for rows in q_hits.values()), default=0)
    print(
        f"P={P} a={a} y={y} H={len(holes)} covered={len(covered)} primeLike={prime_like} "
        f"qCount={len(q_hits)} hitSupply={big_hit_supply} maxReuse={max_reuse} "
        f"logSupply={big_log_supply:.2f} demandAllLogY={demand_all_log_y:.2f} ratioAll={big_log_supply/demand_all_log_y if demand_all_log_y else 0:.3f} "
        f"demandCoveredLogY={demand_comp_log_y:.2f} ratioCovered={big_log_supply/demand_comp_log_y if demand_comp_log_y else 0:.3f} "
        f"totalLogV={total_log_all:.2f} bigLogFrac={big_log_supply/total_log_all if total_log_all else 0:.3f}"
    )
    print("  hitHist", sorted(hit_hist.items()), "valHist", sorted(val_hist.items()))
    if detail:
        top = sorted(((len(rows), q, q_val_sum[q], rows[:20]) for q, rows in q_hits.items()), reverse=True)[:25]
        zero_rows = [r for r in holes if r not in covered]
        print("  top_q", top)
        print("  zero_rows", zero_rows[:120])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=1009)
    parser.add_argument("--a", type=int, default=720)
    parser.add_argument("--ys", default="101,173,293")
    parser.add_argument("--detail", action="store_true")
    args = parser.parse_args()
    flags = sieve(args.P * args.P)
    root = primes_from_flags(flags, args.P)
    for y in [int(x) for x in args.ys.split(",") if x.strip()]:
        analyze(args.P, args.a, y, flags, root, args.detail)


if __name__ == "__main__":
    main()
