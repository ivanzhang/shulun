#!/usr/bin/env python3
"""审计 QSurv 与 q 网格素数间隙结构。

用法示例：
  python3 experiments/prime_matrix_qsurv_gap_structure_audit.py --max-p 2000
  python3 experiments/prime_matrix_qsurv_gap_structure_audit.py --max-p 5000 --out-prefix docs/monograph/prime-matrix-qsurv-gap-structure-audit

该脚本利用平方壳层引理对应的事实：对相邻素数 p<q，q^2 以内旧 p-筛
幸存者除 q^2 外正好是素数。因此 QSurv 可直接转化为每个 q 行含素数。
"""

from __future__ import annotations

import argparse
import bisect
import json
from pathlib import Path


def sieve_bool(n: int) -> bytearray:
    """返回素数布尔表。"""
    is_prime = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        is_prime[0] = 0
    if n >= 1:
        is_prime[1] = 0
    for d in range(2, int(n**0.5) + 1):
        if is_prime[d]:
            start = d * d
            is_prime[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return is_prime


def next_prime_from_table(p: int, is_prime: bytearray) -> int:
    """用素数表返回大于 p 的最小素数。"""
    q = p + 1
    while q < len(is_prime) and not is_prime[q]:
        q += 1
    if q >= len(is_prime):
        raise ValueError("素数表范围不足")
    return q


def prefix_counts(is_prime: bytearray) -> list[int]:
    """素数计数前缀。"""
    pref = [0] * len(is_prime)
    total = 0
    for idx, flag in enumerate(is_prime):
        total += int(flag)
        pref[idx] = total
    return pref


def primes_from_table(is_prime: bytearray) -> list[int]:
    """从布尔表提取素数列表。"""
    return [idx for idx, flag in enumerate(is_prime) if flag]


def row_prime_count(pref: list[int], left: int, right: int) -> int:
    """闭区间素数个数。"""
    return pref[right] - (pref[left - 1] if left > 0 else 0)


def audit(max_p: int) -> dict:
    """主审计。"""
    coarse = sieve_bool(max_p + 1000)
    target_primes = [p for p in range(3, max_p + 1) if coarse[p]]
    max_q = next_prime_from_table(max_p, coarse)
    limit = max_q * max_q

    is_prime = sieve_bool(limit)
    pref = prefix_counts(is_prime)
    primes = primes_from_table(is_prime)

    records = []
    global_min_count = None
    thin_records = []
    zero_records = []

    for p in target_primes:
        q = next_prime_from_table(p, is_prime)
        min_count = None
        min_rows = []
        first_zero = None
        singleton_rows = []

        for row in range(1, q + 1):
            left = (row - 1) * q + 1
            right = row * q
            count = row_prime_count(pref, left, right)
            if min_count is None or count < min_count:
                min_count = count
                min_rows = [row]
            elif count == min_count:
                min_rows.append(row)
            if count == 0 and first_zero is None:
                first_zero = row
            if count == 1:
                prime_idx = bisect.bisect_left(primes, left)
                singleton_rows.append(
                    {
                        "row": row,
                        "interval": [left, right],
                        "prime": primes[prime_idx] if prime_idx < len(primes) and primes[prime_idx] <= right else None,
                    }
                )

        # q^2 前最大素数间隙。
        upto = bisect.bisect_right(primes, q * q)
        max_gap = 0
        max_gap_pair = None
        for a, b in zip(primes[: upto - 1], primes[1:upto]):
            gap = b - a
            if gap > max_gap:
                max_gap = gap
                max_gap_pair = [a, b]

        record = {
            "p": p,
            "q_next": q,
            "min_q_row_prime_count": min_count,
            "min_rows": min_rows[:10],
            "min_row_count": len(min_rows),
            "singleton_row_count": len(singleton_rows),
            "singleton_rows_sample": singleton_rows[:5],
            "first_zero_q_row": first_zero,
            "max_prime_gap_up_to_q_square": max_gap,
            "max_gap_pair": max_gap_pair,
            "max_gap_over_q": max_gap / q if q else None,
        }
        records.append(record)
        if first_zero is not None:
            zero_records.append(record)
        if min_count == 1:
            thin_records.append(record)
        if global_min_count is None or min_count < global_min_count:
            global_min_count = min_count

    return {
        "parameters": {
            "max_p": max_p,
            "max_q": max_q,
            "sieve_limit": limit,
        },
        "summary": {
            "prime_count": len(records),
            "global_min_q_row_prime_count": global_min_count,
            "zero_q_row_records": len(zero_records),
            "singleton_min_records": len(thin_records),
            "max_gap_over_q": max((r["max_gap_over_q"] for r in records), default=None),
            "max_singleton_rows_in_one_q": max((r["singleton_row_count"] for r in records), default=0),
        },
        "threshold_summary": threshold_summary(records),
        "thin_records_sample": thin_records[:20],
        "zero_records": zero_records,
        "records": records,
    }


def threshold_summary(records: list[dict]) -> list[dict]:
    """按 p 阈值汇总最薄行和最大间隙比例。"""
    output = []
    for threshold in [19, 101, 1000]:
        subset = [record for record in records if record["p"] >= threshold]
        if not subset:
            continue
        min_count = min(record["min_q_row_prime_count"] for record in subset)
        worst = [
            {
                "p": record["p"],
                "q_next": record["q_next"],
                "min_rows": record["min_rows"][:5],
            }
            for record in subset
            if record["min_q_row_prime_count"] == min_count
        ][:5]
        output.append(
            {
                "p_threshold": threshold,
                "record_count": len(subset),
                "min_q_row_prime_count": min_count,
                "max_gap_over_q": max(record["max_gap_over_q"] for record in subset),
                "worst_samples": worst,
            }
        )
    return output


def write_markdown(result: dict, path: Path) -> None:
    """输出 Markdown 报告。"""
    summary = result["summary"]
    params = result["parameters"]
    thin = result["thin_records_sample"]

    lines = [
        "# QSurv 与 q 网格素数间隙结构审计",
        "",
        "**状态：** `experimental_qsurv_gap_structure_audit_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `max_q`: `{params['max_q']}`",
        f"- `sieve_limit`: `{params['sieve_limit']}`",
        "",
        "## 总结",
        "",
        f"- 检查奇素数个数：`{summary['prime_count']}`。",
        f"- 全局最小 `q` 行素数数：`{summary['global_min_q_row_prime_count']}`。",
        f"- 零 `q` 行记录数：`{summary['zero_q_row_records']}`。",
        f"- 最薄为单素数行的记录数：`{summary['singleton_min_records']}`。",
        f"- 最大 `prime_gap/q`：`{summary['max_gap_over_q']}`。",
        f"- 单个 `q` 中 singleton 行最多数：`{summary['max_singleton_rows_in_one_q']}`。",
        "",
        "## 阈值分层摘要",
        "",
        "| p threshold | records | min q-row prime count | max gap/q | worst samples |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for item in result["threshold_summary"]:
        lines.append(
            "| {threshold} | {count} | {minc} | {ratio:.6f} | {samples} |".format(
                threshold=item["p_threshold"],
                count=item["record_count"],
                minc=item["min_q_row_prime_count"],
                ratio=item["max_gap_over_q"],
                samples=item["worst_samples"],
            )
        )

    lines.extend(
        [
        "",
        "## 单素数最薄样本",
        "",
        "| p | q | min count | singleton rows | max gap/q | first singleton sample |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in thin:
        sample = item["singleton_rows_sample"][0] if item["singleton_rows_sample"] else None
        lines.append(
            "| {p} | {q} | {minc} | {singletons} | {ratio:.6f} | {sample} |".format(
                p=item["p"],
                q=item["q_next"],
                minc=item["min_q_row_prime_count"],
                singletons=item["singleton_row_count"],
                ratio=item["max_gap_over_q"],
                sample=sample,
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "`QSurv(p,q)` 等价于每个 `q` 网格行 `[(s-1)q+1,sq]` 至少含一个素数。若某行为空，则存在覆盖整行的相邻素数间隙，因而给出长度至少 `q` 量级的网格素数间隙异常。",
            "",
            "本审计没有发现零行，但大量最薄行为单素数行。这说明递推闭合余量很薄：任何证明都必须利用端点、缝合和 CRT 刚性排除整行空洞，不能依赖粗平均。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=2000)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-qsurv-gap-structure-audit",
    )
    args = parser.parse_args()

    result = audit(args.max_p)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
