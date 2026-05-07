#!/usr/bin/env python3
"""审计平方后端点面积的基线-进位分解。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_area_carry_audit.py --max-p 10000

对 y=floor(P/e)，a in (y,P) 时 floor(P/a) 只能是 1 或 2。
因此双曲窄带面积
  X(P)=sum_a (floor((P^2+P-1)/a)-floor(P^2/a))
可精确写为 base(P)+carry(P)。
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return flags


def primes_from_table(flags: bytearray) -> list[int]:
    """提取素数列表。"""
    return [idx for idx, flag in enumerate(flags) if flag]


def audit_p(p: int, y_ratio: float) -> dict:
    """审计单个 p 的基线和进位项。"""
    y = max(2, int(math.floor(y_ratio * p)))
    p_square = p * p
    base = p + p // 2 - 1 - 2 * y
    area = 0
    carry = 0
    carry_q1 = 0
    carry_q2 = 0
    carry_samples = []
    max_slice = 0

    for a in range(y + 1, p):
        quotient = p // a
        residue_p = p - quotient * a
        residue_square = p_square % a
        slice_len = (p_square + p - 1) // a - p_square // a
        area += slice_len
        if slice_len > max_slice:
            max_slice = slice_len
        carry_bit = slice_len - quotient
        if carry_bit not in (0, 1):
            raise AssertionError("进位项应为 0 或 1")
        if carry_bit:
            carry += 1
            if quotient == 1:
                carry_q1 += 1
            elif quotient == 2:
                carry_q2 += 1
            if len(carry_samples) < 5:
                carry_samples.append(
                    {
                        "a": a,
                        "quotient": quotient,
                        "p_mod_a": residue_p,
                        "p_square_mod_a": residue_square,
                        "slice_len": slice_len,
                    }
                )

    if area != base + carry:
        raise AssertionError("base+carry 分解失败")
    area_target = 1.02 * p
    carry_allowance = area_target - base
    return {
        "p": p,
        "y": y,
        "area": area,
        "base": base,
        "carry": carry,
        "carry_q1": carry_q1,
        "carry_q2": carry_q2,
        "area_ratio": area / p,
        "base_ratio": base / p,
        "carry_ratio": carry / p,
        "carry_allowance": carry_allowance,
        "carry_allowance_ratio": carry_allowance / p,
        "carry_slack": carry_allowance - carry,
        "max_slice_length": max_slice,
        "certifies_area_102": area <= area_target,
        "carry_samples": carry_samples,
    }


def audit(max_p: int, y_ratio: float) -> dict:
    """执行审计。"""
    primes = [prime for prime in primes_from_table(sieve_bool(max_p)) if prime >= 23]
    records = [audit_p(p, y_ratio) for p in primes]
    failures_102 = [record for record in records if not record["certifies_area_102"]]
    tail_records = [record for record in records if record["p"] >= 2003]
    tail_failures = [
        record for record in tail_records if not record["certifies_area_102"]
    ]
    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "area_102_failure_count": len(failures_102),
            "last_area_102_failure_p": failures_102[-1]["p"]
            if failures_102
            else None,
            "tail_p_ge_2003_count": len(tail_records),
            "tail_area_102_failure_count": len(tail_failures),
            "min_tail_carry_slack": min(
                (record["carry_slack"] for record in tail_records), default=None
            ),
            "max_tail_carry_ratio_record": max(
                tail_records, key=lambda item: item["carry_ratio"], default=None
            ),
            "max_area_ratio_record": max(
                records, key=lambda item: item["area_ratio"], default=None
            ),
            "worst_tail_slack_records": sorted(
                tail_records, key=lambda item: item["carry_slack"]
            )[:20],
        },
        "area_102_failures": failures_102,
        "tail_area_102_failures": tail_failures,
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平方后端点面积进位审计",
        "",
        "**状态：** `experimental_area_carry_decomposition_support_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        "",
        "## 总结",
        "",
        f"- 检查 `p>=23` 奇素数个数：`{summary['prime_count']}`。",
        f"- `X(P)<=1.02P` 失败数：`{summary['area_102_failure_count']}`。",
        f"- 最后失败 p：`{summary['last_area_102_failure_p']}`。",
        f"- `p>=2003` 记录数：`{summary['tail_p_ge_2003_count']}`。",
        f"- `p>=2003` 失败数：`{summary['tail_area_102_failure_count']}`。",
        f"- `p>=2003` 最小进位余量：`{summary['min_tail_carry_slack']}`。",
        f"- 尾段最大进位比例记录：`{summary['max_tail_carry_ratio_record']}`。",
        f"- 全局最大面积比例记录：`{summary['max_area_ratio_record']}`。",
        "",
        "## 尾段最小进位余量样本",
        "",
        "| p | y | base | carry | allow | slack | area/P | carry/P | q1 | q2 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for record in summary["worst_tail_slack_records"]:
        lines.append(
            f"| {record['p']} | {record['y']} | {record['base']} | "
            f"{record['carry']} | {record['carry_allowance']:.2f} | "
            f"{record['carry_slack']:.2f} | {record['area_ratio']:.6f} | "
            f"{record['carry_ratio']:.6f} | {record['carry_q1']} | {record['carry_q2']} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "对 `a in (y,P)`，`floor(P/a)` 只能取 `1` 或 `2`，故面积可精确分解为 `X(P)=base(P)+carry(P)`。`RFP-Area` 的尾段目标等价于进位计数低于 `1.02P-base(P)`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_area_carry_audit_20260505",
    )
    args = parser.parse_args()
    result = audit(args.max_p, args.y_ratio)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    compact = {
        key: value
        for key, value in result["summary"].items()
        if key != "worst_tail_slack_records"
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
