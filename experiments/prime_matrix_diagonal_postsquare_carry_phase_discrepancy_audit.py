#!/usr/bin/env python3
"""审计面积进位的二次相位偏差。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_carry_phase_discrepancy_audit.py --max-p 10000

进位条件可写为 {h^2/a} > 1-h/a，其中 h=P-floor(P/a)*a。
自然连续主量是 W(P)=sum h/a；D(P)=C(P)-W(P) 是二次分数部分偏差。
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
    """审计单个 p 的相位偏差。"""
    y = max(2, int(math.floor(y_ratio * p)))
    base = p + p // 2 - 1 - 2 * y
    carry = 0
    weight = 0.0
    carry_q1 = 0
    carry_q2 = 0
    weight_q1 = 0.0
    weight_q2 = 0.0
    samples = []

    for a in range(y + 1, p):
        q = p // a
        h = p - q * a
        threshold_weight = h / a
        weight += threshold_weight
        residue = (h * h) % a
        carry_bit = 1 if residue + h > a else 0
        carry += carry_bit
        if q == 1:
            weight_q1 += threshold_weight
            carry_q1 += carry_bit
        elif q == 2:
            weight_q2 += threshold_weight
            carry_q2 += carry_bit
        if carry_bit and len(samples) < 5:
            samples.append(
                {
                    "a": a,
                    "q": q,
                    "h": h,
                    "h_over_a": threshold_weight,
                    "h2_mod_a": residue,
                }
            )

    discrepancy = carry - weight
    allowance = 1.02 * p - base
    return {
        "p": p,
        "y": y,
        "base": base,
        "carry": carry,
        "weight": weight,
        "discrepancy": discrepancy,
        "discrepancy_abs": abs(discrepancy),
        "discrepancy_over_sqrt_p": discrepancy / math.sqrt(p),
        "abs_discrepancy_over_sqrt_p": abs(discrepancy) / math.sqrt(p),
        "allowance": allowance,
        "allowance_minus_weight": allowance - weight,
        "allowance_minus_carry": allowance - carry,
        "weight_ratio": weight / p,
        "carry_ratio": carry / p,
        "carry_q1": carry_q1,
        "carry_q2": carry_q2,
        "weight_q1": weight_q1,
        "weight_q2": weight_q2,
        "certifies_area_102": carry <= allowance,
        "samples": samples,
    }


def audit(max_p: int, y_ratio: float) -> dict:
    """执行审计。"""
    primes = [prime for prime in primes_from_table(sieve_bool(max_p)) if prime >= 23]
    records = [audit_p(p, y_ratio) for p in primes]
    tail_records = [record for record in records if record["p"] >= 2003]
    failures = [record for record in records if not record["certifies_area_102"]]
    tail_failures = [
        record for record in tail_records if not record["certifies_area_102"]
    ]
    return {
        "parameters": {"max_p": max_p, "y_ratio": y_ratio},
        "summary": {
            "prime_count": len(records),
            "area_102_failure_count": len(failures),
            "last_area_102_failure_p": failures[-1]["p"] if failures else None,
            "tail_p_ge_2003_count": len(tail_records),
            "tail_area_102_failure_count": len(tail_failures),
            "max_positive_discrepancy_over_sqrt_p_record": max(
                records, key=lambda item: item["discrepancy_over_sqrt_p"], default=None
            ),
            "max_abs_discrepancy_over_sqrt_p_record": max(
                records,
                key=lambda item: item["abs_discrepancy_over_sqrt_p"],
                default=None,
            ),
            "min_tail_allowance_minus_weight_record": min(
                tail_records,
                key=lambda item: item["allowance_minus_weight"],
                default=None,
            ),
            "min_tail_allowance_minus_carry_record": min(
                tail_records,
                key=lambda item: item["allowance_minus_carry"],
                default=None,
            ),
            "worst_tail_records": sorted(
                tail_records, key=lambda item: item["allowance_minus_carry"]
            )[:20],
        },
        "failures": failures,
        "tail_failures": tail_failures,
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# 平方后端点进位相位偏差审计",
        "",
        "**状态：** `experimental_carry_phase_discrepancy_support_not_a_proof`",
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
        f"- 最大正偏差/根号 p 记录：`{summary['max_positive_discrepancy_over_sqrt_p_record']}`。",
        f"- 最大绝对偏差/根号 p 记录：`{summary['max_abs_discrepancy_over_sqrt_p_record']}`。",
        f"- 尾段最小 `allowance-W` 记录：`{summary['min_tail_allowance_minus_weight_record']}`。",
        f"- 尾段最小 `allowance-C` 记录：`{summary['min_tail_allowance_minus_carry_record']}`。",
        "",
        "## 尾段最紧样本",
        "",
        "| p | carry | W | D | D/sqrt(p) | allow-W | allow-C | q1 | q2 |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for record in summary["worst_tail_records"]:
        lines.append(
            f"| {record['p']} | {record['carry']} | {record['weight']:.6f} | "
            f"{record['discrepancy']:.6f} | {record['discrepancy_over_sqrt_p']:.6f} | "
            f"{record['allowance_minus_weight']:.6f} | "
            f"{record['allowance_minus_carry']:.6f} | "
            f"{record['carry_q1']} | {record['carry_q2']} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "进位条件等价于 `{h^2/a}>1-h/a`。因此 `C(P)=W(P)+D(P)`，其中 `W(P)=sum h/a` 是连续主量，`D(P)` 是二次分数部分偏差。若 `D(P)` 在尾段异常为正，则这是双曲地板二次相位集中，正好路由到 `HyperbolicDiscFailure/PDEC`。",
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
        default="docs/diagonal_postsquare_carry_phase_discrepancy_audit_20260505",
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
        if key != "worst_tail_records"
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
