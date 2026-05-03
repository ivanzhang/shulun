#!/usr/bin/env python3
"""扫描四重除数求和相对主项的余项常数需求。"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def d4poly_stieltjes_coeffs() -> list[float]:
    """返回 d_4 主项 P3 的系数 a0,a1,a2,a3（升幂）。"""
    gamma = 0.5772156649015328606
    gamma1 = -0.0728158454836767249
    gamma2 = -0.00969036319287231848
    return [
        -1.0 + 4.0 * gamma - 6.0 * gamma * gamma + 4.0 * gamma1 + 4.0 * gamma**3 - 12.0 * gamma * gamma1 + 2.0 * gamma2,
        1.0 - 4.0 * gamma + 6.0 * gamma * gamma - 4.0 * gamma1,
        -0.5 + 2.0 * gamma,
        1.0 / 6.0,
    ]


def p3_value(log_x: float) -> float:
    """计算主项多项式 P3(log x)。"""
    coeffs = d4poly_stieltjes_coeffs()
    return sum(coef * log_x**i for i, coef in enumerate(coeffs))


def d4_prefix(max_n: int) -> list[int]:
    """用四重卷积筛计算 D4(N)=sum_{n<=N} d4(n)。"""
    d2 = [0] * (max_n + 1)
    for d in range(1, max_n + 1):
        for m in range(d, max_n + 1, d):
            d2[m] += 1

    d4 = [0] * (max_n + 1)
    for d in range(1, max_n + 1):
        value = d2[d]
        if value == 0:
            continue
        for m in range(d, max_n + 1, d):
            d4[m] += value * d2[m // d]

    prefix = [0] * (max_n + 1)
    running = 0
    for n in range(1, max_n + 1):
        running += d4[n]
        prefix[n] = running
    return prefix


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=5504, help="扫描到的最大 X")
    parser.add_argument("--start", type=int, default=3, help="扫描起点")
    parser.add_argument("--top", type=int, default=10, help="输出最大 K 需求的前若干项")
    parser.add_argument("--assert-k", type=float, help="断言所有扫描点的 K 需求不超过该值")
    parser.add_argument("--json", type=Path, help="把摘要证书写入 JSON 文件")
    args = parser.parse_args()

    prefix = d4_prefix(args.max_n)
    rows = []
    for x in range(max(3, args.start), args.max_n + 1):
        log_x = math.log(x)
        main_term = x * p3_value(log_x)
        remainder = max(0.0, prefix[x] - main_term)
        k_needed = remainder / (x ** 0.75)
        rows.append((k_needed, x, prefix[x], main_term, remainder))

    rows.sort(reverse=True)
    print(f"SCAN max_n={args.max_n} start={args.start} top={args.top}")
    for k_needed, x, actual, main_term, remainder in rows[: args.top]:
        print(
            "x={x} k_needed={k:.6f} actual={actual} main={main:.3f} rem={rem:.3f}".format(
                x=x,
                k=k_needed,
                actual=actual,
                main=main_term,
                rem=remainder,
            )
        )
    if rows:
        print(f"MAX_K_NEEDED={rows[0][0]:.6f} at X={rows[0][1]}")
        if args.assert_k is not None and rows[0][0] > args.assert_k:
            print(f"FAIL: max K {rows[0][0]:.9f} exceeds asserted {args.assert_k:.9f}")
            return 1
        if args.json is not None:
            args.json.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "max_n": args.max_n,
                "start": max(3, args.start),
                "assert_k": args.assert_k,
                "max_k_needed": rows[0][0],
                "max_witness_x": rows[0][1],
                "top": [
                    {
                        "k_needed": row[0],
                        "x": row[1],
                        "actual": row[2],
                        "main_term": row[3],
                        "remainder": row[4],
                    }
                    for row in rows[: args.top]
                ],
            }
            args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
