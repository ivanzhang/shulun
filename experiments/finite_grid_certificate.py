#!/usr/bin/env python3
"""生成/校验 P×P 方阵行列素数有限验证证书。

证书记录每个已验证奇素数 P 的每行一个素数见证、每个非末列一个素数见证，
用于把小范围直接验证从一次性输出变成可复核 JSON 证书。

用法示例：
  python3 experiments/finite_grid_certificate.py generate --max-p 1000 --output /tmp/grid-cert.json
  python3 experiments/finite_grid_certificate.py check --input /tmp/grid-cert.json
"""
from __future__ import annotations

import argparse
import json
from math import isqrt
from pathlib import Path
from typing import Any


def sieve(n: int) -> list[bool]:
    """返回 0..n 的素性表。"""
    if n < 2:
        return [False] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : n + 1 : p] = [False] * (((n - start) // p) + 1)
    return is_prime


def primes_up_to(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    table = sieve(n)
    return [i for i, ok in enumerate(table) if ok]


def first_prime_in_row(P: int, row: int, prime_table: list[bool]) -> int | None:
    """返回第 row 行中的第一个素数见证。"""
    start = (row - 1) * P + 1
    for value in range(start, start + P):
        if prime_table[value]:
            return value
    return None


def first_prime_in_col(P: int, col: int, prime_table: list[bool]) -> int | None:
    """返回第 col 列中的第一个素数见证；col 为 1..P-1。"""
    for row in range(1, P + 1):
        value = (row - 1) * P + col
        if prime_table[value]:
            return value
    return None


def generate_certificate(max_p: int) -> dict[str, Any]:
    """生成 P<=max_p 的见证证书。"""
    odd_primes = [p for p in primes_up_to(max_p) if p % 2 == 1]
    max_n = odd_primes[-1] ** 2 if odd_primes else 1
    prime_table = sieve(max_n)
    records: list[dict[str, Any]] = []

    for P in odd_primes:
        row_witnesses: list[int] = []
        col_witnesses: list[int] = []
        for row in range(1, P + 1):
            witness = first_prime_in_row(P, row, prime_table)
            if witness is None:
                raise RuntimeError(f"P={P} 第 {row} 行无素数")
            row_witnesses.append(witness)
        for col in range(1, P):
            witness = first_prime_in_col(P, col, prime_table)
            if witness is None:
                raise RuntimeError(f"P={P} 第 {col} 列无素数")
            col_witnesses.append(witness)
        records.append({"P": P, "row_witnesses": row_witnesses, "col_witnesses": col_witnesses})

    return {
        "type": "finite_grid_prime_witness_certificate",
        "max_p": max_p,
        "prime_count": len(odd_primes),
        "records": records,
    }


def is_prime_trial(n: int) -> bool:
    """用试除校验证书中的单个见证是否为素数。"""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n)
    divisor = 3
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def check_certificate(cert: dict[str, Any]) -> tuple[bool, str]:
    """校验证书格式、行列位置和素性。"""
    if cert.get("type") != "finite_grid_prime_witness_certificate":
        return False, "证书 type 不正确"
    for record in cert.get("records", []):
        P = int(record["P"])
        rows = record.get("row_witnesses", [])
        cols = record.get("col_witnesses", [])
        if len(rows) != P:
            return False, f"P={P} 行见证数量错误"
        if len(cols) != P - 1:
            return False, f"P={P} 列见证数量错误"
        for row, value in enumerate(rows, start=1):
            if not ((row - 1) * P + 1 <= value <= row * P):
                return False, f"P={P} 第 {row} 行见证越界: {value}"
            if not is_prime_trial(value):
                return False, f"P={P} 第 {row} 行见证非素数: {value}"
        for col, value in enumerate(cols, start=1):
            if value % P != col % P or not (1 <= value <= P * P):
                return False, f"P={P} 第 {col} 列见证越界: {value}"
            if not is_prime_trial(value):
                return False, f"P={P} 第 {col} 列见证非素数: {value}"
    return True, f"证书通过：{len(cert.get('records', []))} 个奇素数 P"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    gen = sub.add_parser("generate")
    gen.add_argument("--max-p", type=int, required=True)
    gen.add_argument("--output", type=Path, required=True)
    chk = sub.add_parser("check")
    chk.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()

    if args.cmd == "generate":
        cert = generate_certificate(args.max_p)
        args.output.write_text(json.dumps(cert, ensure_ascii=False, separators=(",", ":")))
        print(f"生成证书: {args.output}，P 数量={cert['prime_count']}，max_p={args.max_p}")
        return 0

    cert = json.loads(args.input.read_text())
    ok, message = check_certificate(cert)
    print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
