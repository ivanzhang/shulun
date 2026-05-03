#!/usr/bin/env python3
"""R4-NLS 实验：剥离正/反45度小素锁定后分析双粗覆盖相位。"""
from __future__ import annotations
import argparse, json, math
from collections import Counter
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


def analyze(P: int, theta: float) -> dict:
    D = math.isqrt(P)
    small = primes_upto(D)
    spf = spf_sieve(P * P + P)
    pplus = factor_distinct(P + 1, spf)
    pminus = factor_distinct(P - 1, spf)
    small_lock = [p for p in set(pplus + pminus) if p <= D]
    large_lock = [p for p in set(pplus + pminus) if p > D]
    row_records = []
    for k in range(1, P + 1):
        rough_cols = []
        unlocked = []
        double_rough_composite = []
        anchor_phases = []
        m_phases = []
        lock_small_hits = 0
        lock_large_hits = 0
        prime_count_unlocked = 0
        for c in range(1, P + 1):
            n = k * P + c
            if not is_rough(n, small):
                continue
            rough_cols.append(c)
            if any(n % p == 0 for p in small_lock):
                lock_small_hits += 1
                continue
            if any(n % p == 0 for p in large_lock):
                lock_large_hits += 1
                continue
            unlocked.append(c)
            if spf[n] == n:
                prime_count_unlocked += 1
                continue
            factors = factor_distinct(n, spf)
            anchors = [q for q in factors if D < q < P]
            if anchors:
                q = max(anchors)
                m = n // q
                if is_rough(m, small):
                    double_rough_composite.append(c)
                    anchor_phases.append(round(q / P, 3))
                    m_phases.append(round(m / max(k, 1), 3))
        unlocked_count = len(unlocked)
        dr_count = len(double_rough_composite)
        rec = {
            'row': k,
            'rough': len(rough_cols),
            'small_lock_hits': lock_small_hits,
            'large_lock_hits': lock_large_hits,
            'unlocked': unlocked_count,
            'unlocked_primes': prime_count_unlocked,
            'double_rough_composites': dr_count,
            'dr_cover_share_unlocked': dr_count / unlocked_count if unlocked_count else 0,
            'anchor_phase_top': Counter(anchor_phases).most_common(8),
            'm_phase_top': Counter(m_phases).most_common(8),
            'unlocked_sample': unlocked[:20],
        }
        row_records.append(rec)
    worst = max(row_records, key=lambda r: (r['dr_cover_share_unlocked'], r['double_rough_composites'], r['unlocked']))
    min_prime_unlocked = min(row_records, key=lambda r: (r['unlocked_primes'], -r['unlocked']))
    return {
        'P': P,
        'D': D,
        'theta': theta,
        'pplus_factors': pplus,
        'pminus_factors': pminus,
        'small_lock_factors': sorted(small_lock),
        'large_lock_factors': sorted(large_lock),
        'worst_double_rough_cover': worst,
        'min_unlocked_prime_row': min_prime_unlocked,
        'top_rows': sorted(row_records, key=lambda r: (-r['dr_cover_share_unlocked'], -r['double_rough_composites']))[:10],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-p', type=int, default=251)
    ap.add_argument('--theta', type=float, default=0.8)
    args = ap.parse_args()
    Ps = [p for p in primes_upto(args.max_p) if p >= 5]
    results = [analyze(P, args.theta) for P in Ps]
    audit = {
        'certificate_type': 'r4_nls_phase_scan',
        'status': 'r4_nls_unlocked_double_rough_phase_scan',
        'max_p': args.max_p,
        'theta': args.theta,
        'results': results,
        'structural_conclusion': '剥离 P±1 的正/反45度锁定因子后，检测剩余粗候选中由双粗合数解释的比例及 q/P、m/k 相位簇。小锁定因子对粗候选自动无效；大锁定因子只剥离低阶点。重点观察无锁定核心是否仍可能被双粗合数全覆盖。',
    }
    DOCS.mkdir(exist_ok=True)
    (DOCS / 'r4-nls-phase-scan.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    lines = ['# R4-NLS 双粗相位扫描', '', f"**状态：** `{audit['status']}`", '', audit['structural_conclusion'], '', '## 摘要']
    for item in results:
        w = item['worst_double_rough_cover']
        mp = item['min_unlocked_prime_row']
        lines.append(f"- P={item['P']} locks_small={item['small_lock_factors']} locks_large={item['large_lock_factors']} worst_share={w['dr_cover_share_unlocked']:.3f} worst_row={w['row']} unlocked={w['unlocked']} dr={w['double_rough_composites']} primes_unlocked={w['unlocked_primes']} minPrimeRow={mp['row']} minPrime={mp['unlocked_primes']} phase_q={w['anchor_phase_top'][:4]} phase_m={w['m_phase_top'][:4]}")
    (DOCS / 'r4-nls-phase-scan.md').write_text('\n'.join(lines) + '\n')
    print(DOCS / 'r4-nls-phase-scan.json')
    print(DOCS / 'r4-nls-phase-scan.md')


if __name__ == '__main__':
    main()
