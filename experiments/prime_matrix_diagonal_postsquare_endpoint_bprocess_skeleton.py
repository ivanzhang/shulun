#!/usr/bin/env python3
"""审计 EndpointReciprocal-OSC 的 B-process 驻相骨架。

用法示例：
  python3 experiments/prime_matrix_diagonal_postsquare_endpoint_bprocess_skeleton.py --freq 64

对相位 f_r(a)=rP^2/a，驻相点满足 n=rP^2/a^2。
在 a in (P/e,P) 上，n 只依赖 r 的范围：r<n<e^2 r。
驻相相位为 e(2P sqrt(rn))，端点因子变为 1-e(sqrt(rn))。
因此 rn 为平方数的无振荡模式会被端点因子精确消掉。
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

TAU = 2.0 * math.pi


def squarefree_kernel(value: int) -> tuple[int, int]:
    """返回 value=d*s^2 的 (d,s)。"""
    rem = value
    d = 1
    s = 1
    factor = 2
    while factor * factor <= rem:
        power = 0
        while rem % factor == 0:
            rem //= factor
            power += 1
        if power % 2:
            d *= factor
        s *= factor ** (power // 2)
        factor += 1 if factor == 2 else 2
    if rem > 1:
        d *= rem
    return d, s


def endpoint_weight_abs(k: int) -> float:
    """计算 |1-e(sqrt(k))|。"""
    return abs(1.0 - complex(math.cos(TAU * math.sqrt(k)), math.sin(TAU * math.sqrt(k))))


def audit(freq: int) -> dict:
    """生成驻相骨架审计。"""
    records = []
    grouped: dict[int, dict] = defaultdict(
        lambda: {"count": 0, "weighted_budget": 0.0, "raw_budget": 0.0}
    )
    square_count = 0
    square_raw_budget = 0.0
    square_weighted_budget = 0.0
    total_raw_budget = 0.0
    total_weighted_budget = 0.0

    for r in range(1, freq + 1):
        start = r + 1
        stop = math.ceil(math.e * math.e * r) - 1
        for n in range(start, stop + 1):
            k = r * n
            raw_coeff = (r ** 0.25) / (math.sqrt(2.0) * (n ** 0.75) * math.pi * r)
            weight_abs = endpoint_weight_abs(k)
            weighted_coeff = raw_coeff * weight_abs
            d, s = squarefree_kernel(k)
            is_square = d == 1
            total_raw_budget += raw_coeff
            total_weighted_budget += weighted_coeff
            grouped[d]["count"] += 1
            grouped[d]["raw_budget"] += raw_coeff
            grouped[d]["weighted_budget"] += weighted_coeff
            if is_square:
                square_count += 1
                square_raw_budget += raw_coeff
                square_weighted_budget += weighted_coeff
            records.append(
                {
                    "r": r,
                    "n": n,
                    "k": k,
                    "squarefree": d,
                    "square_part": s,
                    "is_square": is_square,
                    "raw_coeff": raw_coeff,
                    "endpoint_weight_abs": weight_abs,
                    "weighted_coeff": weighted_coeff,
                }
            )

    top_groups = sorted(
        (
            {"squarefree": d, **data}
            for d, data in grouped.items()
        ),
        key=lambda item: -item["weighted_budget"],
    )[:20]
    top_terms = sorted(records, key=lambda item: -item["weighted_coeff"])[:20]

    return {
        "parameters": {"freq": freq},
        "summary": {
            "stationary_terms": len(records),
            "square_terms": square_count,
            "square_raw_budget": square_raw_budget,
            "square_weighted_budget": square_weighted_budget,
            "total_raw_budget": total_raw_budget,
            "total_weighted_budget": total_weighted_budget,
            "square_removed_fraction": (
                1.0 - square_weighted_budget / square_raw_budget
                if square_raw_budget
                else None
            ),
            "total_abs_budget_ratio": (
                total_weighted_budget / total_raw_budget if total_raw_budget else None
            ),
            "top_squarefree_groups": top_groups,
            "top_weighted_terms": top_terms,
        },
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    summary = result["summary"]
    lines = [
        "# EndpointReciprocal-OSC B-process 驻相骨架审计",
        "",
        "**状态：** `static_bprocess_skeleton_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `freq`: `{params['freq']}`",
        "",
        "## 总结",
        "",
        f"- 驻相项数：`{summary['stationary_terms']}`。",
        f"- 平方驻相项数：`{summary['square_terms']}`。",
        f"- 平方项原始预算：`{summary['square_raw_budget']:.12f}`。",
        f"- 平方项端点加权后预算：`{summary['square_weighted_budget']:.12e}`。",
        f"- 全部原始预算：`{summary['total_raw_budget']:.12f}`。",
        f"- 全部端点加权预算：`{summary['total_weighted_budget']:.12f}`。",
        f"- 平方共振移除比例：`{summary['square_removed_fraction']:.6f}`。",
        f"- 全部绝对预算倍率：`{summary['total_abs_budget_ratio']:.6f}`。",
        "",
        "## 最大平方自由核",
        "",
        "| squarefree d | count | raw budget | weighted budget |",
        "|---:|---:|---:|---:|",
    ]
    for item in summary["top_squarefree_groups"]:
        lines.append(
            f"| {item['squarefree']} | {item['count']} | "
            f"{item['raw_budget']:.6f} | {item['weighted_budget']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 最大驻相项",
            "",
            "| r | n | rn | squarefree | |1-e(sqrt(rn))| | weighted coeff |",
            "|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in summary["top_weighted_terms"]:
        lines.append(
            f"| {item['r']} | {item['n']} | {item['k']} | {item['squarefree']} | "
            f"{item['endpoint_weight_abs']:.6f} | {item['weighted_coeff']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "B-process 的潜在无振荡项满足 `rn=s^2`，此时 `e(2P sqrt(rn))=1`。但同一项的端点因子 `1-e(sqrt(rn))` 精确为零，所以平方共振被自动消去。剩余项均带非平方根频率，可进入有符号有限频率账本或 PDEC 出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--freq", type=int, default=64)
    parser.add_argument(
        "--out-prefix",
        default="docs/diagonal_postsquare_endpoint_bprocess_skeleton_20260505",
    )
    args = parser.parse_args()
    result = audit(args.freq)
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
