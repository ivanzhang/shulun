#!/usr/bin/env python3
"""大锚逃逸扫描：检查 P×P 方阵行内粗候选由接近 P 的锚解释的比例。"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            step_count = ((n - i * i) // i) + 1
            sieve[i * i:n + 1:i] = [False] * step_count
    return [i for i, ok in enumerate(sieve) if ok]


def spf_sieve(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def distinct_prime_factors(n: int, spf: list[int]) -> list[int]:
    out = []
    while n > 1:
        p = spf[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


def analyze_p(P: int, theta: float) -> dict:
    max_n = P * P + P
    spf = spf_sieve(max_n)
    D = int(math.isqrt(P))
    small = [p for p in primes_upto(D)]
    row_records = []
    zero_prime_rows = []
    worst_large_share = 0.0
    worst_record = None
    for k in range(1, P + 1):
        rough = []
        prime_count = 0
        composite_rough = []
        large_anchor_hits = 0
        anchor_values = []
        m_values = []
        for c in range(1, P + 1):
            n = k * P + c
            if spf[n] == n:
                prime_count += 1
            if all(n % p for p in small):
                rough.append(c)
                if spf[n] != n:
                    factors = distinct_prime_factors(n, spf)
                    anchors = [q for q in factors if D < q < P]
                    if anchors:
                        q = max(anchors)
                        anchor_values.append(q)
                        m_values.append(n // q)
                        composite_rough.append(c)
                        if q >= theta * P:
                            large_anchor_hits += 1
        share = large_anchor_hits / len(composite_rough) if composite_rough else 0.0
        rec = {
            'row': k,
            'prime_count': prime_count,
            'rough_count': len(rough),
            'composite_rough_count': len(composite_rough),
            'large_anchor_share': share,
            'anchor_min': min(anchor_values) if anchor_values else None,
            'anchor_max': max(anchor_values) if anchor_values else None,
            'anchor_avg': sum(anchor_values) / len(anchor_values) if anchor_values else None,
            'm_min': min(m_values) if m_values else None,
            'm_max': max(m_values) if m_values else None,
            'm_distinct': len(set(m_values)),
        }
        row_records.append(rec)
        if prime_count == 0:
            zero_prime_rows.append(rec)
        if share > worst_large_share:
            worst_large_share = share
            worst_record = rec
    return {
        'P': P,
        'D': D,
        'theta': theta,
        'zero_prime_rows': zero_prime_rows,
        'worst_large_anchor_row': worst_record,
        'top_large_anchor_rows': sorted(row_records, key=lambda r: (-r['large_anchor_share'], -r['composite_rough_count']))[:10],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-p', type=int, default=251)
    parser.add_argument('--theta', type=float, default=0.8)
    args = parser.parse_args()
    Ps = [p for p in primes_upto(args.max_p) if p >= 5]
    results = [analyze_p(P, args.theta) for P in Ps]
    audit = {
        'certificate_type': 'large_anchor_escape_scan',
        'status': 'large_anchor_escape_measured_in_first_P_rows',
        'theta': args.theta,
        'max_p': args.max_p,
        'results': results,
        'structural_conclusion': '在 P×P 目标窗口内直接测量大锚逃逸形态：记录每行粗合数由 q>=theta P 解释的比例、互补因子 m 的范围和复用情况。若零素数行不存在，则用最高大锚占比行作为潜在逃逸近似模型。',
    }
    DOCS.mkdir(exist_ok=True)
    (DOCS / 'large-anchor-escape-scan.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    lines = ['# 大锚逃逸扫描', '', f"**状态：** `{audit['status']}`", '', audit['structural_conclusion'], '', '## 摘要']
    for item in results:
        w = item['worst_large_anchor_row']
        zeros = item['zero_prime_rows']
        lines.append(f"- P={item['P']} D={item['D']} zero_rows={len(zeros)} worst_row={w}")
    (DOCS / 'large-anchor-escape-scan.md').write_text('\n'.join(lines) + '\n')
    print(DOCS / 'large-anchor-escape-scan.json')
    print(DOCS / 'large-anchor-escape-scan.md')


if __name__ == '__main__':
    main()
