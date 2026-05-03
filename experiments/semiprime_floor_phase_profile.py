#!/usr/bin/env python3
"""剖析长命中串中 n=uv 的 floor-sum/分数相位结构。

对每个粗合数命中 n，取最小大因子 u 与 v=floor(n/u)。记录：
  target = (-N mod u)/u，其中 N 是命中串左端整数；
  local = (n-N)/u，衡量短段位移相对 u 的大小；
  命中条件为 offset ≡ -N (mod u)。对真实因子该同余恒成立，故不再把误差相位当作随机信号。

用法示例：
  python3 experiments/semiprime_floor_phase_profile.py --Ps 503,1009 --top 5
"""
from __future__ import annotations

import argparse
import math
from collections import Counter

from high_threshold_margin_fast import primes, sieve
from large_factor_exclusion import factor_distinct
from semiprime_chain_bipartite_energy import low_prime_rows
from semiprime_hit_run_profile import candidate_records, hit_runs


def frac(x: float) -> float:
    return x - math.floor(x)


def circular_gap(values: list[float]) -> tuple[float, float]:
    """返回单位圆排序相位的最大空隙与平均近邻空隙。"""
    if len(values) <= 1:
        return 1.0, 1.0
    xs = sorted(v % 1.0 for v in values)
    gaps = [b - a for a, b in zip(xs, xs[1:])] + [xs[0] + 1.0 - xs[-1]]
    return max(gaps), sum(gaps) / len(gaps)


def rayleigh(values: list[float]) -> float:
    """单位圆相位 Rayleigh 合成长度，越小越相消。"""
    if not values:
        return 0.0
    re = sum(math.cos(2 * math.pi * v) for v in values)
    im = sum(math.sin(2 * math.pi * v) for v in values)
    return math.hypot(re, im) / len(values)


def phase_profile(P: int, records: list[dict], lo: int, hi: int) -> dict:
    """计算一条命中串的 floor 相位指标。"""
    B = math.isqrt(P)
    seg = records[lo : hi + 1]
    if not seg:
        return {}
    base_n = seg[0]["n"]
    targets = []
    locals_ = []
    us = []
    shells = []
    residues = []
    for rec in seg:
        factors = tuple(sorted(rec["factors"]))
        if not factors:
            continue
        u = factors[0]
        us.append(u)
        shells.append(int(math.floor(math.log(max(u, B) / B, 2))) if u >= B else -1)
        target = ((-base_n) % u) / u
        local = (rec["n"] - base_n) / u
        targets.append(target)
        locals_.append(local)
        residues.append(rec["n"] % u)
    max_target_gap, mean_target_gap = circular_gap(targets)
    # 相邻 u 与目标残基的符号变动，粗看是否存在单调/锁相。
    target_steps = [abs(b - a) for a, b in zip(targets, targets[1:])]
    return {
        "run_len": len(seg),
        "target_rayleigh": rayleigh(targets),
        "max_target_gap": max_target_gap,
        "target_step_med": sorted(target_steps)[len(target_steps)//2] if target_steps else 0.0,
        "local_max": max(locals_) if locals_ else 0.0,
        "local_med": sorted(locals_)[len(locals_)//2] if locals_ else 0.0,
        "u_med_over_B": (sorted(us)[len(us)//2] / B) if us else 0.0,
        "shells": dict(Counter(shells)),
        "shell_switches": sum(1 for a, b in zip(shells, shells[1:]) if a != b),
        "zero_residues": sum(1 for r in residues if r == 0),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--Ps", default="503,1009,2003,4001")
    parser.add_argument("--rows", default="")
    parser.add_argument("--top", type=int, default=6)
    parser.add_argument("--window-factor", type=float, default=4.0)
    parser.add_argument("--stride-factor", type=float, default=0.25)
    args = parser.parse_args()

    print("P row start cand prime cover runLen targetRay targetGap targetStep locMed locMax uMed/B switch shells")
    for P in [int(part) for part in args.Ps.split(",") if part.strip()]:
        B = math.isqrt(P)
        limit = P * P + P
        flags = sieve(limit)
        plist = primes(flags, limit)
        small_primes = primes(sieve(B), B)
        rows = [int(x) for x in args.rows.split(",") if x.strip()] if args.rows else low_prime_rows(P, flags, args.top)
        length = max(1, int(args.window_factor * math.sqrt(P)))
        stride = max(1, int(args.stride_factor * math.sqrt(P)))
        profiles = []
        for row in rows:
            max_start = max(1, P - length + 1)
            starts = list(range(1, max_start + 1, stride)) + [max_start]
            for start in sorted(set(starts)):
                records = candidate_records(P, row, start, length, flags, plist, small_primes)
                if not records:
                    continue
                prime_count = sum(1 for rec in records if rec["kind"] == "prime")
                cover = sum(rec["hit"] for rec in records) / len(records)
                for lo, hi in hit_runs(records):
                    prof = phase_profile(P, records, lo, hi)
                    if prof:
                        profiles.append((prof["run_len"], cover, len(records), -prime_count, row, start, prof))
        for _run_len, cover, cand, neg_prime, row, start, prof in sorted(profiles, key=lambda item: (item[0], item[1], item[2], item[3]), reverse=True)[: args.top]:
            shells = ",".join(f"s{k}:{v}" for k, v in sorted(prof["shells"].items()))
            print(
                P, row, start, cand, -neg_prime, f"{cover:.3f}", prof["run_len"],
                f"{prof['target_rayleigh']:.3f}", f"{prof['max_target_gap']:.3f}",
                f"{prof['target_step_med']:.3f}",
                f"{prof['local_med']:.3f}", f"{prof['local_max']:.3f}", f"{prof['u_med_over_B']:.2f}",
                prof["shell_switches"], shells,
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
