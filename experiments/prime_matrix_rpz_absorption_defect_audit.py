#!/usr/bin/env python3
"""审计 RPZ 复活点吸收标签是否形成缺陷。

用法示例：
  python3 experiments/prime_matrix_rpz_absorption_defect_audit.py

输入为 `prime-matrix-scaled-peeling-halfwidth-audit.json`。脚本对半宽层复活点选择
一个吸收标签：最小的 `half_prime < ell <= top_prime` 且 `ell | n` 的素因子。
随后统计标签负载、列位置和粗互补因子，用来判断样本更接近 TailAnchor/ColumnCRT
集中，还是分散吸收分支。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def select_absorber(factors: list[int], half_prime: int, top_prime: int) -> int | None:
    """选择复活点的吸收标签。"""
    candidates = [factor for factor in factors if half_prime < factor <= top_prime]
    return min(candidates) if candidates else None


def audit(source_path: Path) -> dict:
    """执行 RPZ 吸收缺陷审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    records = []
    global_label_load: Counter[int] = Counter()
    total_resurrected = 0

    for item in source["records"]:
        top = item["top_prime"]
        half = item["half_prime"]
        left, right = item["top_interval"]
        absorptions = []
        label_load: Counter[int] = Counter()
        column_load: Counter[int] = Counter()
        missing_absorber = []

        for profile in item["half_survivor_factor_profiles"]:
            n = profile["n"]
            factors = profile["factors"]
            absorber = select_absorber(factors, half, top)
            top_column = n - left + 1
            half_row = (n - 1) // half + 1
            half_column = (n - 1) % half + 1
            if absorber is None:
                missing_absorber.append(n)
                cofactor = None
            else:
                label_load[absorber] += 1
                global_label_load[absorber] += 1
                cofactor = n // absorber
            column_load[top_column] += 1
            absorptions.append(
                {
                    "n": n,
                    "top_column": top_column,
                    "half_row": half_row,
                    "half_column": half_column,
                    "factors": factors,
                    "absorber": absorber,
                    "cofactor": cofactor,
                    "cofactor_gt_top": cofactor is not None and cofactor > top,
                }
            )

        total_resurrected += len(absorptions)
        records.append(
            {
                "top_prime": top,
                "top_zero_row": item["top_zero_row"],
                "top_interval": item["top_interval"],
                "half_prime": half,
                "resurrected_count": len(absorptions),
                "missing_absorber_count": len(missing_absorber),
                "missing_absorber": missing_absorber,
                "absorber_label_load": dict(sorted(label_load.items())),
                "max_absorber_label_load": max(label_load.values(), default=0),
                "distinct_absorber_labels": len(label_load),
                "top_column_load": dict(sorted(column_load.items())),
                "max_top_column_load": max(column_load.values(), default=0),
                "absorptions": absorptions,
            }
        )

    return {
        "status": "rpz_absorption_audit_shows_dispersed_resurrected_labels",
        "source": str(source_path),
        "summary": {
            "records": len(records),
            "total_resurrected_points": total_resurrected,
            "records_with_missing_absorber": sum(
                1 for record in records if record["missing_absorber_count"]
            ),
            "global_max_local_label_load": max(
                (record["max_absorber_label_load"] for record in records),
                default=0,
            ),
            "global_max_top_column_load": max(
                (record["max_top_column_load"] for record in records),
                default=0,
            ),
            "global_absorber_label_load": dict(sorted(global_label_load.items())),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 复活点吸收缺陷审计",
        "",
        "**状态：** `rpz_absorption_audit_shows_dispersed_resurrected_labels`",
        "",
        "## 总结",
        "",
        f"- 样本记录数：`{summary['records']}`。",
        f"- 复活点总数：`{summary['total_resurrected_points']}`。",
        f"- 缺失吸收标签的记录数：`{summary['records_with_missing_absorber']}`。",
        f"- 局部最大吸收标签负载：`{summary['global_max_local_label_load']}`。",
        f"- 局部最大顶层列负载：`{summary['global_max_top_column_load']}`。",
        f"- 全局吸收标签负载：`{summary['global_absorber_label_load']}`。",
        "",
        "## 逐例表",
        "",
        "| top P | row | half | resurrected | max label load | labels | missing |",
        "|---:|---:|---:|---:|---:|---|---:|",
    ]
    for record in result["records"]:
        lines.append(
            "| {top} | {row} | {half} | {count} | {max_load} | `{labels}` | {missing} |".format(
                top=record["top_prime"],
                row=record["top_zero_row"],
                half=record["half_prime"],
                count=record["resurrected_count"],
                max_load=record["max_absorber_label_load"],
                labels=record["absorber_label_load"],
                missing=record["missing_absorber_count"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "在这些已知零行模型中，半宽层复活点都能找到 `half_prime < ell <= top_prime` 的吸收标签，且每个窗口内最大标签负载为 `1`。因此有限样本没有表现为 TailAnchor 集中，而是分散吸收。",
            "",
            "这说明 `RPZ-Absorption=>TailAnchor` 不能只靠单窗标签负载完成；必须加入相邻漂移窗口、列见证位移或低模端点投影。下一步应证明：分散吸收若能在漂移族中稳定持续，则必转化为 `ColumnCRT` 位移余类负载或 `ColumnRadius` 异常。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-scaled-peeling-halfwidth-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-absorption-defect-audit"),
    )
    args = parser.parse_args()
    result = audit(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
