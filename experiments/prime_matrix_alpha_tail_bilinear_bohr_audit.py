#!/usr/bin/env python3
"""AlphaTail 双线性 Fourier 证书的 Bohr-cap 审计。

用法示例：
  python3 experiments/prime_matrix_alpha_tail_bilinear_bohr_audit.py --selected 997:4096:- --scan-h 64 --format table

`p:B:sign` 中 sign 为 `+` 或 `-`，表示审计高块中的 Möbius 正/负平方自由低素除数。
脚本只审计全矩形 `M x D` 的非零频率强度；它不是全局证明输入。
"""

from __future__ import annotations

import argparse
import cmath
import json
from math import ceil, floor, isqrt, pi, sqrt


def primes_upto(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, isqrt(value) + 1)):
            primes.append(value)
    return primes


def low_squarefree_block(cutoff: int, block: int, sign: str) -> list[int]:
    """返回 block<d<=2block 中由低素数生成且 Möbius 符号指定的平方自由数。"""
    allowed = primes_upto(cutoff)
    allowed_set = set(allowed)
    target_parity = 0 if sign == "+" else 1
    records: list[int] = []
    for value in range(block + 1, 2 * block + 1):
        remaining = value
        omega = 0
        ok = True
        for prime in allowed:
            if prime * prime > remaining:
                break
            if remaining % prime != 0:
                continue
            remaining //= prime
            omega += 1
            if remaining % prime == 0:
                ok = False
                break
        if not ok:
            continue
        if remaining > 1:
            if remaining not in allowed_set:
                continue
            omega += 1
        if omega % 2 == target_parity:
            records.append(value)
    return records


def geometric_interval_sum(start: int, stop: int, numerator: int, modulus: int) -> complex:
    """计算 sum_{m=start}^{stop} exp(2πi numerator*m/modulus)。"""
    if stop < start:
        return 0j
    ratio_angle = 2 * pi * (numerator % modulus) / modulus
    if numerator % modulus == 0:
        return complex(stop - start + 1, 0.0)
    ratio = cmath.exp(1j * ratio_angle)
    first = cmath.exp(1j * ratio_angle * start)
    return first * (1 - ratio ** (stop - start + 1)) / (1 - ratio)


def audit_item(prime_bound: int, block: int, sign: str, alpha: float, scan_h: int) -> dict:
    """审计一个 p:B:sign 的全矩形双线性和。"""
    height = prime_bound - 1
    cutoff = int(alpha * prime_bound)
    d_values = low_squarefree_block(cutoff, block, sign)
    m_start = ceil((prime_bound * prime_bound + 1) / (2 * block))
    m_stop = floor((prime_bound * prime_bound + height) / block)
    modulus = 4 * prime_bound * prime_bound + 1
    m_count = max(0, m_stop - m_start + 1)
    baseline = sqrt(max(1, m_count * len(d_values)))
    best = {"h": 0, "abs": 0.0, "normalized": 0.0}
    rows = []
    for frequency in range(1, scan_h + 1):
        total = 0j
        for divisor in d_values:
            total += geometric_interval_sum(m_start, m_stop, frequency * divisor, modulus)
        magnitude = abs(total)
        normalized = magnitude / baseline
        row = {"h": frequency, "abs": magnitude, "normalized": normalized}
        rows.append(row)
        if magnitude > best["abs"]:
            best = row
    return {
        "p": prime_bound,
        "alpha": alpha,
        "block": block,
        "sign": sign,
        "Q": modulus,
        "m_start": m_start,
        "m_stop": m_stop,
        "m_count": m_count,
        "d_count": len(d_values),
        "sqrt_MD": baseline,
        "best": best,
        "rows": rows,
    }


def parse_selected(raw: str) -> list[tuple[int, int, str]]:
    """解析 p:B:sign 逗号列表。"""
    items: list[tuple[int, int, str]] = []
    for part in raw.split(","):
        if not part.strip():
            continue
        prime_raw, block_raw, sign = part.split(":", 2)
        if sign not in {"+", "-"}:
            raise ValueError("sign must be + or -")
        items.append((int(prime_raw), int(block_raw), sign))
    return items


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--selected", type=str, default="997:4096:-,5003:8192:-")
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--scan-h", type=int, default=32)
    parser.add_argument("--format", choices=("json", "table", "repr"), default="repr")
    args = parser.parse_args()

    audits = [
        audit_item(prime_bound, block, sign, args.alpha, args.scan_h)
        for prime_bound, block, sign in parse_selected(args.selected)
    ]
    if args.format == "json":
        print(json.dumps(audits, ensure_ascii=False, indent=2), flush=True)
        return
    if args.format == "table":
        print("p block sign m_count d_count best_h best_abs best_norm", flush=True)
        for audit in audits:
            best = audit["best"]
            print(
                f"{audit['p']} {audit['block']} {audit['sign']} "
                f"{audit['m_count']} {audit['d_count']} "
                f"{best['h']} {best['abs']:.6f} {best['normalized']:.6f}",
                flush=True,
            )
        return
    for audit in audits:
        print(audit, flush=True)


if __name__ == "__main__":
    main()
