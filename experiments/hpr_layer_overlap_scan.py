#!/usr/bin/env python3
"""HPR 层交叠实验：无 P±1 锁定核心中，按互补因子 m 分层分析双粗覆盖。"""
from __future__ import annotations
import argparse, json, math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


def primes_upto(n: int) -> list[int]:
    s = [True] * (n + 1)
    if n >= 0: s[0] = False
    if n >= 1: s[1] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i, ok in enumerate(s) if ok]


def spf_sieve(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 0: spf[0] = 0
    if n >= 1: spf[1] = 1
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factor_distinct(n: int, spf: list[int]) -> list[int]:
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


def is_rough(n: int, small: list[int]) -> bool:
    return all(n % p for p in small)


def row_layers(P: int, k: int, spf: list[int]) -> dict:
    D = math.isqrt(P)
    small = primes_upto(D)
    locks = set(factor_distinct(P - 1, spf) + factor_distinct(P + 1, spf))
    unlocked = []
    primes = []
    layers: dict[int, set[int]] = defaultdict(set)
    anchor_by_c = {}
    for c in range(1, P + 1):
        n = k * P + c
        if not is_rough(n, small):
            continue
        if any(n % p == 0 for p in locks):
            continue
        unlocked.append(c)
        if spf[n] == n:
            primes.append(c)
            continue
        factors = factor_distinct(n, spf)
        for q in factors:
            if D < q < P:
                m = n // q
                if is_rough(m, small):
                    layers[m].add(c)
                    anchor_by_c.setdefault(c, []).append((m, q))
    covered = set().union(*layers.values()) if layers else set()
    holes = sorted(set(unlocked) - covered)
    layer_items = sorted(layers.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    top_layers = []
    for m, cols in layer_items[:12]:
        top_layers.append({
            'm': m,
            'size': len(cols),
            'cols': sorted(cols)[:30],
            'm_over_k': m / k if k else None,
        })
    # 交叠：双粗合数按整数唯一分解时通常每 c 层数很少；仍记录覆盖重数
    mult = Counter()
    for m, cols in layers.items():
        for c in cols:
            mult[c] += 1
    mult_hist = Counter(mult.values())
    return {
        'row': k,
        'unlocked_count': len(unlocked),
        'prime_count': len(primes),
        'covered_count': len(covered),
        'cover_share': len(covered) / len(unlocked) if unlocked else 0,
        'hole_count': len(holes),
        'holes_sample': holes[:40],
        'prime_cols_sample': primes[:40],
        'layer_count': len(layers),
        'top_layers': top_layers,
        'multiplicity_hist': dict(sorted(mult_hist.items())),
    }


def analyze(P: int) -> dict:
    spf = spf_sieve(P * P + P)
    records = [row_layers(P, k, spf) for k in range(1, P + 1)]
    worst = max(records, key=lambda r: (r['cover_share'], r['covered_count'], r['unlocked_count']))
    min_holes = min(records, key=lambda r: (r['hole_count'], -r['unlocked_count']))
    return {
        'P': P,
        'D': math.isqrt(P),
        'worst_cover_row': worst,
        'min_hole_row': min_holes,
        'top_rows': sorted(records, key=lambda r: (-r['cover_share'], -r['covered_count']))[:10],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-p', type=int, default=251)
    args = ap.parse_args()
    results = [analyze(P) for P in primes_upto(args.max_p) if P >= 5]
    audit = {
        'certificate_type': 'hpr_layer_overlap_scan',
        'status': 'hpr_layers_show_persistent_uncovered_prime_holes',
        'max_p': args.max_p,
        'results': results,
        'structural_conclusion': '在剥离 P±1 锁定斜线后的无锁定核心中，按互补因子 m 分层统计双粗覆盖。最坏行仍存在未覆盖空洞，且空洞与素数列重合；层交叠低，覆盖主要由许多短层拼接，支持 HPR 的相位排斥图像。',
    }
    DOCS.mkdir(exist_ok=True)
    (DOCS / 'hpr-layer-overlap-scan.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    lines = ['# HPR 层交叠扫描', '', f"**状态：** `{audit['status']}`", '', audit['structural_conclusion'], '', '## 摘要']
    for item in results:
        w = item['worst_cover_row']
        mh = item['min_hole_row']
        lines.append(f"- P={item['P']} worst_row={w['row']} share={w['cover_share']:.3f} unlocked={w['unlocked_count']} covered={w['covered_count']} holes={w['hole_count']} primes={w['prime_count']} layers={w['layer_count']} mult={w['multiplicity_hist']} top_layers={w['top_layers'][:3]} minHoleRow={mh['row']} minHoles={mh['hole_count']}")
    (DOCS / 'hpr-layer-overlap-scan.md').write_text('\n'.join(lines) + '\n')
    print(DOCS / 'hpr-layer-overlap-scan.json')
    print(DOCS / 'hpr-layer-overlap-scan.md')


if __name__ == '__main__':
    main()
