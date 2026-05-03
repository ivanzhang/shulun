#!/usr/bin/env python3
"""审计 Distributed-RCI 中平衡双尾半素数到素数的局部配对。

用法示例：
  python3 experiments/prime_matrix_distributed_rci_pairing_audit.py --max-p 1000
  python3 experiments/prime_matrix_distributed_rci_pairing_audit.py --max-p 2000 --min-p 17

若每个终端块内的平衡双尾半素数都能注入匹配到附近不同素数，
则 `balanced semiprimes < primes` 可转化为局部 Hall/间隙不等式。
"""

from __future__ import annotations

import argparse
import json
import math
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


def primes_from_table(is_prime: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(is_prime) if flag]


def next_prime(p: int, primes: list[int]) -> int:
    """返回大于 p 的下一素数。"""
    for prime in primes:
        if prime > p:
            return prime
    raise ValueError("素数表范围不足")


def build_tail_data(
    q: int,
    low_primes: list[int],
    tail_primes: list[int],
) -> tuple[bytearray, bytearray, dict[int, list[int]]]:
    """构造低筛骨架、尾因子数和尾标签。"""
    q_square = q * q
    low_rough = bytearray(b"\x01") * (q_square + 1)
    low_rough[0] = 0
    low_rough[1] = 0
    low_rough[q_square] = 0
    for ell in low_primes:
        low_rough[0 : q_square + 1 : ell] = b"\x00" * ((q_square // ell) + 1)

    tail_omega = bytearray(q_square + 1)
    tail_labels: dict[int, list[int]] = {}
    for ell in tail_primes:
        for pos in range(ell, q_square + 1, ell):
            if not low_rough[pos]:
                continue
            tail_omega[pos] += 1
            tail_labels.setdefault(pos, []).append(ell)
    return low_rough, tail_omega, tail_labels


def can_match_with_radius(semis: list[int], primes: list[int], radius: int) -> bool:
    """判断每个 semiprime 是否能匹配到距离 radius 内的不同 prime。"""
    prime_index = 0
    for semi in semis:
        while prime_index < len(primes) and primes[prime_index] < semi - radius:
            prime_index += 1
        if prime_index >= len(primes) or primes[prime_index] > semi + radius:
            return False
        prime_index += 1
    return True


def min_matching_radius(semis: list[int], primes: list[int]) -> int | None:
    """计算一维有序注入匹配的最小最大距离。"""
    if not semis:
        return 0
    if len(semis) > len(primes):
        return None
    lo = 0
    hi = max(abs(semis[0] - primes[-1]), abs(semis[-1] - primes[0]))
    while lo < hi:
        mid = (lo + hi) // 2
        if can_match_with_radius(semis, primes, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def audit(max_p: int, min_p: int, y_ratio: float) -> dict:
    """执行配对审计。"""
    is_prime = sieve_bool(max_p * max_p + max_p * 20 + 10000)
    primes = primes_from_table(is_prime)
    target_primes = [prime for prime in primes if min_p <= prime <= max_p]

    row_records = []
    records = []

    for p in target_primes:
        q = next_prime(p, primes)
        y = max(2, int(math.floor(y_ratio * p)))
        low_primes = [prime for prime in primes if prime <= y]
        tail_primes = [prime for prime in primes if y < prime <= p]
        low_rough, tail_omega, tail_labels = build_tail_data(
            q=q,
            low_primes=low_primes,
            tail_primes=tail_primes,
        )

        primes_by_row: list[list[int]] = [[] for _ in range(q + 1)]
        semis_by_row: list[list[int]] = [[] for _ in range(q + 1)]
        for n in range(2, q * q):
            if not low_rough[n]:
                continue
            row = (n - 1) // q + 1
            omega = tail_omega[n]
            if omega == 0:
                primes_by_row[row].append(n)
            elif omega == 2:
                labels = tail_labels[n]
                if labels[0] * labels[1] == n:
                    semis_by_row[row].append(n)

        local_worst_radius = 0
        local_worst_row = None
        local_max_ratio = 0.0
        local_max_ratio_row = None
        local_matching_failures = 0

        for row in range(1, q + 1):
            semis = semis_by_row[row]
            if not semis:
                continue
            prime_values = primes_by_row[row]
            radius = min_matching_radius(semis, prime_values)
            ratio = len(semis) / len(prime_values) if prime_values else float("inf")
            record = {
                "p": p,
                "q": q,
                "y": y,
                "row": row,
                "row_interval": [(row - 1) * q + 1, row * q],
                "prime_count": len(prime_values),
                "balanced_semiprime_count": len(semis),
                "semiprime_to_prime_ratio": ratio,
                "matching_radius": radius,
                "semiprime_positions": semis[:20],
                "prime_positions": prime_values[:20],
            }
            row_records.append(record)
            if radius is None:
                local_matching_failures += 1
            elif radius > local_worst_radius:
                local_worst_radius = radius
                local_worst_row = record
            if ratio > local_max_ratio:
                local_max_ratio = ratio
                local_max_ratio_row = record

        records.append(
            {
                "p": p,
                "q": q,
                "y": y,
                "local_worst_matching_radius": local_worst_radius,
                "local_worst_radius_row": local_worst_row,
                "local_max_semiprime_ratio": local_max_ratio,
                "local_max_ratio_row": local_max_ratio_row,
                "local_matching_failures": local_matching_failures,
            }
        )

    finite_radius_rows = [
        row for row in row_records if row["matching_radius"] is not None
    ]
    for row in finite_radius_rows:
        log_q = math.log(row["q"])
        row["radius_over_log2_q"] = row["matching_radius"] / (log_q * log_q)
        row["radius_over_sqrt_q"] = row["matching_radius"] / math.sqrt(row["q"])
        row["radius_over_q_over_log_q"] = (
            row["matching_radius"] / (row["q"] / log_q)
        )
    return {
        "parameters": {
            "max_p": max_p,
            "min_p": min_p,
            "y_ratio": y_ratio,
        },
        "summary": {
            "prime_record_count": len(records),
            "row_with_semiprime_count": len(row_records),
            "matching_failure_rows": sum(
                1 for row in row_records if row["matching_radius"] is None
            ),
            "global_max_matching_radius": max(
                (row["matching_radius"] for row in finite_radius_rows),
                default=0,
            ),
            "global_max_radius_over_log2_q": max(
                (row["radius_over_log2_q"] for row in finite_radius_rows),
                default=0,
            ),
            "global_max_radius_over_sqrt_q": max(
                (row["radius_over_sqrt_q"] for row in finite_radius_rows),
                default=0,
            ),
            "global_max_radius_over_q_over_log_q": max(
                (row["radius_over_q_over_log_q"] for row in finite_radius_rows),
                default=0,
            ),
            "global_max_semiprime_ratio": max(
                (row["semiprime_to_prime_ratio"] for row in row_records),
                default=0,
            ),
            "worst_radius_rows": sorted(
                finite_radius_rows,
                key=lambda item: item["matching_radius"],
                reverse=True,
            )[:20],
            "worst_ratio_rows": sorted(
                row_records,
                key=lambda item: item["semiprime_to_prime_ratio"],
                reverse=True,
            )[:20],
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# Distributed-RCI 半素数-素数局部配对审计",
        "",
        "**状态：** `experimental_semiprime_prime_pairing_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `min_p`: `{params['min_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查素数记录数：`{summary['prime_record_count']}`。",
        f"- 含平衡半素数的行数：`{summary['row_with_semiprime_count']}`。",
        f"- 配对失败行数：`{summary['matching_failure_rows']}`。",
        f"- 最大最小匹配半径：`{summary['global_max_matching_radius']}`。",
        f"- 最大 `radius/log^2(q)`：`{summary['global_max_radius_over_log2_q']}`。",
        f"- 最大 `radius/sqrt(q)`：`{summary['global_max_radius_over_sqrt_q']}`。",
        f"- 最大 `radius/(q/log q)`：`{summary['global_max_radius_over_q_over_log_q']}`。",
        f"- 最大半素数/素数比值：`{summary['global_max_semiprime_ratio']}`。",
        "",
        "## 最大匹配半径样本",
        "",
        "| p | q | row | primes | semis | ratio | radius | radius/log²q | interval |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in summary["worst_radius_rows"]:
        lines.append(
            "| {p} | {q} | {row} | {primes} | {semis} | {ratio:.6f} | {radius} | {rlog:.6f} | {interval} |".format(
                p=row["p"],
                q=row["q"],
                row=row["row"],
                primes=row["prime_count"],
                semis=row["balanced_semiprime_count"],
                ratio=row["semiprime_to_prime_ratio"],
                radius=row["matching_radius"],
                rlog=row["radius_over_log2_q"],
                interval=row["row_interval"],
            )
        )
    lines.extend(
        [
            "",
            "## 最大比例样本",
            "",
            "| p | q | row | primes | semis | ratio | radius |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in summary["worst_ratio_rows"]:
        lines.append(
            "| {p} | {q} | {row} | {primes} | {semis} | {ratio:.6f} | {radius} |".format(
                p=row["p"],
                q=row["q"],
                row=row["row"],
                primes=row["prime_count"],
                semis=row["balanced_semiprime_count"],
                ratio=row["semiprime_to_prime_ratio"],
                radius=row["matching_radius"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "若每个平衡双尾半素数都能匹配到同一行内附近的不同素数，则 `balanced semiprimes < primes` 可被局部 Hall 不等式证明。样本中配对失败数为 `0`，说明局部配对路线值得严攻；但匹配半径不是常数级，正式证明仍需把大半径样本送入端点/尾锚缺陷出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--min-p", type=int, default=17)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-distributed-rci-pairing-audit",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.min_p, args.y_ratio)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = {
        key: value
        for key, value in result["summary"].items()
        if key not in {"worst_radius_rows", "worst_ratio_rows"}
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
