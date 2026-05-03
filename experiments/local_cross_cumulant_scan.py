#!/usr/bin/env python3
"""扫描局部窗口 H,R,U,T 的低阶交叉中心矩。

用法示例：
  python3 experiments/local_cross_cumulant_scan.py --Ps 503,1009,2003 --C 4

说明：
  H 为 sqrt(P)-小筛候选数；R 为可复用半素数证书；U 为单命中半素数证书；T 为粗三因子误差。
  输出二阶相关与若干三/四阶标准化混合中心矩，用于检验交叉 cumulant 是否低阶或有符号抵消。
"""
import argparse
import math
from itertools import combinations
from statistics import mean

from high_threshold_margin_fast import sieve, primes
from large_factor_exclusion import factor_distinct


def cov(xs, ys):
    mx = mean(xs)
    my = mean(ys)
    return mean((x - mx) * (y - my) for x, y in zip(xs, ys))


def corr(xs, ys):
    vx = cov(xs, xs)
    vy = cov(ys, ys)
    if vx <= 0 or vy <= 0:
        return 0.0
    return cov(xs, ys) / math.sqrt(vx * vy)


def centered(vals):
    mu = mean(vals)
    return [v - mu for v in vals]


def standardized_mixed(samples, names):
    centered_map = {name: centered(vals) for name, vals in samples.items()}
    vars_map = {name: mean(x * x for x in centered_map[name]) for name in names}
    out = {}

    # 三阶：E[X^2 Y] / (VarX sqrt(VarY))，观测单分量极端是否拖动另一分量。
    for x, y in combinations(names, 2):
        for a, b in ((x, y), (y, x)):
            denom = vars_map[a] * math.sqrt(vars_map[b]) if vars_map[a] > 0 and vars_map[b] > 0 else 0
            val = mean((u * u) * v for u, v in zip(centered_map[a], centered_map[b])) / denom if denom else 0.0
            out[f'm3_{a}{a}{b}'] = val

    # 四阶交叉：E[X^2 Y^2]/(VarX VarY)-1，越接近 2 表示近高斯相关，越小越安全。
    for x, y in combinations(names, 2):
        denom = vars_map[x] * vars_map[y] if vars_map[x] > 0 and vars_map[y] > 0 else 0
        raw = mean((u * u) * (v * v) for u, v in zip(centered_map[x], centered_map[y])) / denom if denom else 0.0
        out[f'm4_{x}{x}{y}{y}'] = raw
    return out


def collect(P, C):
    B = math.isqrt(P)
    flags = sieve(P * P + P)
    plist = primes(flags, P * P + P)
    small = primes(sieve(B), B)
    L = max(1, int(C * math.sqrt(P)))
    step = max(1, L // 8)
    samples = {name: [] for name in ('H', 'R', 'U', 'T')}

    for row in range(1, P + 1):
        pref = {name: [0] * (P + 1) for name in samples}
        for c in range(1, P + 1):
            n = (row - 1) * P + c
            vals = {name: 0 for name in samples}
            if all(n % q for q in small):
                vals['H'] = 1
                if not flags[n]:
                    fac = factor_distinct(n, plist)
                    if all(q > B for q in fac):
                        if len(fac) == 2:
                            vals['R' if min(fac) <= L else 'U'] = 1
                        elif len(fac) == 3:
                            vals['T'] = 1
            for name in samples:
                pref[name][c] = pref[name][c - 1] + vals[name]
        for start in range(1, P - L + 2, step):
            end = start + L - 1
            for name in samples:
                samples[name].append(pref[name][end] - pref[name][start - 1])
    return L, samples


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--Ps', default='503,1009,2003')
    ap.add_argument('--C', type=float, default=4.0)
    args = ap.parse_args()
    names = ('H', 'R', 'U', 'T')
    print('P C L n means vars corrHR corrHU corrHT corrRU corrRT corrUT m4_HHRR m4_HHUU m4_RRUU maxAbsM3')
    for P in [int(x) for x in args.Ps.split(',') if x.strip()]:
        L, samples = collect(P, args.C)
        means = {name: mean(samples[name]) for name in names}
        vars_map = {name: cov(samples[name], samples[name]) for name in names}
        mixed = standardized_mixed(samples, names)
        max_abs_m3 = max(abs(v) for k, v in mixed.items() if k.startswith('m3_'))
        print(
            P,
            args.C,
            L,
            len(samples['H']),
            ','.join(f'{means[name]:.3f}' for name in names),
            ','.join(f'{vars_map[name]:.3f}' for name in names),
            f'{corr(samples["H"], samples["R"]):.3f}',
            f'{corr(samples["H"], samples["U"]):.3f}',
            f'{corr(samples["H"], samples["T"]):.3f}',
            f'{corr(samples["R"], samples["U"]):.3f}',
            f'{corr(samples["R"], samples["T"]):.3f}',
            f'{corr(samples["U"], samples["T"]):.3f}',
            f'{mixed["m4_HHRR"]:.3f}',
            f'{mixed["m4_HHUU"]:.3f}',
            f'{mixed["m4_RRUU"]:.3f}',
            f'{max_abs_m3:.3f}',
        )


if __name__ == '__main__':
    main()
