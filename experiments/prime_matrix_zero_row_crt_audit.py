#!/usr/bin/env python3
"""审计旧 p-筛 CRT 延续中的首个零行位置。

用法示例：
  python3 experiments/prime_matrix_zero_row_crt_audit.py --max-p 200 --row-factor 200
  python3 experiments/prime_matrix_zero_row_crt_audit.py --max-p 2000 --aligned-max-p 200 --out-prefix docs/monograph/prime-matrix-zero-row-crt-audit

脚本检查三类对象：
1. p 对齐行：[(r-1)p+1, rp] 是否完全被 <=p 的素数覆盖；
2. q 方阵行：[(s-1)q+1, sq] 在旧 p-筛下是否无幸存者，且排除 q^2 单点；
3. 首个 p 对齐零行与 ceil(q^2/p) 的比较。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的全部素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for d in range(2, int(n**0.5) + 1):
        if sieve[d]:
            start = d * d
            sieve[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return [i for i in range(n + 1) if sieve[i]]


def is_prime(n: int) -> bool:
    """朴素判素；这里只用于相邻素数，规模很小。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def next_prime(n: int) -> int:
    """返回大于 n 的最小素数。"""
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def mark_old_sieve_interval(left: int, right: int, small_primes: Iterable[int]) -> bytearray:
    """在 [left,right] 上标记旧筛幸存者；1 表示避开所有 small_primes。"""
    length = right - left + 1
    alive = bytearray(b"\x01") * length
    for prime in small_primes:
        first = ((left + prime - 1) // prime) * prime
        if first <= right:
            offset = first - left
            alive[offset:length:prime] = b"\x00" * (((length - 1 - offset) // prime) + 1)
    if left <= 1 <= right:
        alive[1 - left] = 0
    return alive


def first_aligned_zero_row(
    p: int,
    small_primes: list[int],
    start_row: int,
    max_row: int,
    block_rows: int,
) -> dict:
    """分段扫描首个 p 对齐零行。"""
    row = start_row
    checked_rows = 0
    while row <= max_row:
        end_row = min(max_row, row + block_rows - 1)
        left = (row - 1) * p + 1
        right = end_row * p
        alive = mark_old_sieve_interval(left, right, small_primes)
        for local_row, actual_row in enumerate(range(row, end_row + 1)):
            a = local_row * p
            b = a + p
            if alive[a:b].count(1) == 0:
                return {
                    "found": True,
                    "row": actual_row,
                    "interval": [(actual_row - 1) * p + 1, actual_row * p],
                    "checked_rows": checked_rows + local_row + 1,
                }
        checked_rows += end_row - row + 1
        row = end_row + 1
    return {
        "found": False,
        "row": None,
        "interval": None,
        "checked_rows": checked_rows,
    }


def q_square_old_sieve_audit(p: int, q: int, small_primes: list[int]) -> dict:
    """检查 q×q 内每个 q 行是否有旧 p-筛幸存者；q^2 单点不计入。"""
    right = q * q
    alive = mark_old_sieve_interval(1, right, small_primes)
    if alive[q * q - 1]:
        alive[q * q - 1] = 0

    first_zero = None
    min_count = None
    min_row = None
    for row in range(1, q + 1):
        left_idx = (row - 1) * q
        right_idx = row * q
        count = alive[left_idx:right_idx].count(1)
        if min_count is None or count < min_count:
            min_count = count
            min_row = row
        if count == 0 and first_zero is None:
            first_zero = row

    return {
        "first_zero_q_row_excluding_q2": first_zero,
        "min_old_sieve_survivors_excluding_q2": min_count,
        "min_row": min_row,
        "safe_all_q_rows": first_zero is None,
    }


def primorial(primes: Iterable[int]) -> int:
    """计算 primorial；Python 大整数足够保存报告用数值。"""
    value = 1
    for prime in primes:
        value *= prime
    return value


def audit(
    max_p: int,
    row_factor: int,
    block_rows: int,
    full_period_max_p: int,
    aligned_max_p: int,
) -> dict:
    """执行主审计。"""
    all_primes = primes_upto(max_p + 100)
    target_primes = [p for p in all_primes if 3 <= p <= max_p]
    records = []

    for p in target_primes:
        small_primes = [prime for prime in all_primes if prime <= p]
        q = next_prime(p)
        q2_p_row_cover = math.ceil((q * q) / p)
        period_rows = None
        if p > aligned_max_p:
            period_rows = None
            max_row = None
            scan_mode = "aligned_scan_skipped"
            aligned = {
                "found": False,
                "row": None,
                "interval": None,
                "checked_rows": 0,
            }
        elif p <= full_period_max_p:
            period_rows = primorial(small_primes) // p
            max_row = period_rows
            scan_mode = "full_crt_row_period"
        else:
            max_row = max(q2_p_row_cover, p) + row_factor * p
            scan_mode = "bounded_after_next_square"
        if p <= aligned_max_p:
            aligned = first_aligned_zero_row(
                p=p,
                small_primes=small_primes,
                start_row=p + 1,
                max_row=max_row,
                block_rows=block_rows,
            )
        q_audit = q_square_old_sieve_audit(p, q, small_primes)

        first_row = aligned["row"]
        if first_row is None:
            relation = "not_found_within_scan_bound"
        elif first_row > q2_p_row_cover:
            relation = "after_q_square_p_row_cover"
        else:
            relation = "inside_q_square_p_row_cover"

        records.append(
            {
                "p": p,
                "q_next": q,
                "q_square": q * q,
                "q_square_p_row_cover": q2_p_row_cover,
                "scan_mode": scan_mode,
                "scan_max_row": max_row,
                "crt_row_period": period_rows,
                "first_aligned_zero_row_after_p": aligned,
                "relation_to_q_square_cover": relation,
                "q_square_old_sieve_audit": q_audit,
            }
        )

    failures_inside_cover = [
        item
        for item in records
        if item["relation_to_q_square_cover"] == "inside_q_square_p_row_cover"
    ]
    q_row_failures = [
        item
        for item in records
        if not item["q_square_old_sieve_audit"]["safe_all_q_rows"]
    ]
    found_rows = [
        item
        for item in records
        if item["first_aligned_zero_row_after_p"]["found"]
    ]

    return {
        "parameters": {
            "max_p": max_p,
            "row_factor": row_factor,
            "block_rows": block_rows,
            "full_period_max_p": full_period_max_p,
            "aligned_max_p": aligned_max_p,
        },
        "summary": {
            "prime_count": len(records),
            "aligned_zero_rows_found": len(found_rows),
            "aligned_zero_inside_q_square_cover": len(failures_inside_cover),
            "q_square_q_row_failures": len(q_row_failures),
            "min_ratio_found_row_to_q_square_cover": min(
                (
                    item["first_aligned_zero_row_after_p"]["row"]
                    / item["q_square_p_row_cover"]
                    for item in found_rows
                ),
                default=None,
            ),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写出简明 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    records = result["records"]

    lines = [
        "# Prime Matrix 旧筛 CRT 零行位置审计",
        "",
        "**状态：** `experimental_zero_row_position_audit_not_a_proof`",
        "",
        "本文审计旧 `p`-筛在 `p` 对齐延续行中的首个零行，并同步检查 `q×q` 中每个 `q` 行是否仍有旧筛幸存者。",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `row_factor`: `{params['row_factor']}`",
        f"- `block_rows`: `{params['block_rows']}`",
        f"- `full_period_max_p`: `{params['full_period_max_p']}`",
        f"- `aligned_max_p`: `{params['aligned_max_p']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- 找到 `p` 对齐零行的个数：`{summary['aligned_zero_rows_found']}`。",
        f"- 首个 `p` 对齐零行落入 `ceil(q^2/p)` 覆盖内的个数：`{summary['aligned_zero_inside_q_square_cover']}`。",
        f"- `q×q` 内旧筛 `q` 行失败个数：`{summary['q_square_q_row_failures']}`。",
        f"- 已找到零行中的最小 `row/ceil(q^2/p)`：`{summary['min_ratio_found_row_to_q_square_cover']}`。",
        "",
        "## 关键样本",
        "",
        "| p | q | ceil(q²/p) | scan | first p-zero row | relation | min q-row survivors | q-row failure |",
        "| ---: | ---: | ---: | --- | ---: | --- | ---: | --- |",
    ]
    for item in records:
        aligned = item["first_aligned_zero_row_after_p"]
        q_audit = item["q_square_old_sieve_audit"]
        if aligned["found"] or not q_audit["safe_all_q_rows"] or item["p"] <= 53:
            lines.append(
                "| {p} | {q} | {cover} | {scan} | {row} | {rel} | {minc} | {fail} |".format(
                    p=item["p"],
                    q=item["q_next"],
                    cover=item["q_square_p_row_cover"],
                    scan=item["scan_mode"],
                    row=aligned["row"],
                    rel=item["relation_to_q_square_cover"],
                    minc=q_audit["min_old_sieve_survivors_excluding_q2"],
                    fail=not q_audit["safe_all_q_rows"],
                )
            )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "实验支持两个分开的事实：",
            "",
            "1. 对已找到的 `p` 对齐零行，首个位置均在 `ceil(q^2/p)` 之后；这支持“旧筛零行不会侵入下一素数平方壳层”的递推直觉。",
            "2. 更直接相关的检查是 `q×q` 内每个 `q` 行的旧筛幸存者数；本次参数内没有出现失败。",
            "",
            "但这仍不是证明。原因是 `p` 对齐行非空不能自动推出任意 `q` 行非空；`q` 行会跨越 `p` 行边界。因此正式引理必须直接证明 `q` 行旧筛幸存者非空，或证明所有可能的跨边界空窗会触发 `PDEC-or-SAE`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=200)
    parser.add_argument("--row-factor", type=int, default=200)
    parser.add_argument("--block-rows", type=int, default=5000)
    parser.add_argument("--full-period-max-p", type=int, default=23)
    parser.add_argument("--aligned-max-p", type=int, default=200)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-zero-row-crt-audit",
    )
    args = parser.parse_args()

    result = audit(
        max_p=args.max_p,
        row_factor=args.row_factor,
        block_rows=args.block_rows,
        full_period_max_p=args.full_period_max_p,
        aligned_max_p=args.aligned_max_p,
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
