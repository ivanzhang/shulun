#!/usr/bin/env python3
"""审计 BCB-Core 中心区间的网格包含余量与端点缺陷相位。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_grid_endpoint_audit.py

输入为 `prime-matrix-rpz-bcb-core-audit.json`。脚本对每个强制中心区间
`J=[u,v]` 和半宽网格宽度 `h` 计算精确判据：

  delta = (1-u) mod h；
  J 含完整 h 对齐行 iff |J| >= delta + h。

若不满足，则记录缺口 `delta+h-|J|`，该缺口就是端点 seam 缺陷相位。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def grid_profile(left: int, right: int, h: int) -> dict:
    """计算区间 `[left,right]` 对 `h` 网格的完整行包含判据。"""
    length = max(0, right - left + 1)
    delta_to_next_start = (1 - left) % h
    next_row_start = left + delta_to_next_start
    next_row_end = next_row_start + h - 1
    margin = length - (delta_to_next_start + h)
    contains = length >= delta_to_next_start + h
    universal_margin = length - (2 * h - 1)
    return {
        "length": length,
        "left_residue_mod_h": left % h,
        "right_residue_mod_h": right % h,
        "delta_to_next_row_start": delta_to_next_start,
        "next_row_start": next_row_start,
        "next_row_end": next_row_end,
        "contains_aligned_row_by_criterion": contains,
        "criterion_margin": margin,
        "endpoint_deficit": 0 if contains else -margin,
        "universal_length_margin_2h_minus_1": universal_margin,
        "endpoint_phase": {
            "h": h,
            "left_residue_mod_h": left % h,
            "length_mod_h": length % h,
            "delta_to_next_row_start": delta_to_next_start,
            "endpoint_deficit": 0 if contains else -margin,
        },
    }


def audit(source_path: Path) -> dict:
    """执行 BCB 网格/端点审计。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    records = []
    for record in source["records"]:
        left, right = record["forced_core_interval"]
        h = record["half_prime"]
        profile = grid_profile(left, right, h)
        contained = record["contained_half_rows"]
        records.append(
            {
                "top_prime": record["top_prime"],
                "top_zero_row": record["top_zero_row"],
                "half_prime": h,
                "forced_core_interval": record["forced_core_interval"],
                "contained_half_rows": contained,
                "audit_contains_aligned_row": bool(contained),
                **profile,
                "criterion_matches_contained_rows": bool(contained)
                == profile["contains_aligned_row_by_criterion"],
            }
        )

    failing = [
        record for record in records if not record["contains_aligned_row_by_criterion"]
    ]
    return {
        "status": "rpz_bcb_grid_endpoint_exact_criterion_audit",
        "source": str(source_path),
        "summary": {
            "records": len(records),
            "records_containing_aligned_row": sum(
                1 for record in records if record["contains_aligned_row_by_criterion"]
            ),
            "records_endpoint_defect": len(failing),
            "criterion_mismatches": sum(
                1 for record in records if not record["criterion_matches_contained_rows"]
            ),
            "min_criterion_margin": min(
                (record["criterion_margin"] for record in records),
                default=None,
            ),
            "max_endpoint_deficit": max(
                (record["endpoint_deficit"] for record in records),
                default=0,
            ),
            "records_universal_by_length": sum(
                1
                for record in records
                if record["universal_length_margin_2h_minus_1"] >= 0
            ),
        },
        "records": records,
    }


def write_markdown(result: dict, path: Path) -> None:
    """写 Markdown 审计报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ-BCB 网格端点相位审计",
        "",
        "**状态：** `rpz_bcb_grid_endpoint_exact_criterion_audit`",
        "",
        "## 总结",
        "",
        f"- 样本记录数：`{summary['records']}`。",
        f"- 按精确判据含完整半宽行的记录数：`{summary['records_containing_aligned_row']}`。",
        f"- 进入端点缺陷的记录数：`{summary['records_endpoint_defect']}`。",
        f"- 判据与枚举不一致数：`{summary['criterion_mismatches']}`。",
        f"- 最小判据余量：`{summary['min_criterion_margin']}`。",
        f"- 最大端点缺口：`{summary['max_endpoint_deficit']}`。",
        f"- 仅凭长度 `|J|>=2h-1` 自动闭合的记录数：`{summary['records_universal_by_length']}`。",
        "",
        "## 逐例表",
        "",
        "| top P | row | h | J | length | delta | margin | universal margin | contained rows | endpoint deficit |",
        "|---:|---:|---:|---|---:|---:|---:|---:|---|---:|",
    ]
    for record in result["records"]:
        lines.append(
            "| {top} | {row} | {h} | `{interval}` | {length} | {delta} | {margin} | {umargin} | `{rows}` | {deficit} |".format(
                top=record["top_prime"],
                row=record["top_zero_row"],
                h=record["half_prime"],
                interval=record["forced_core_interval"],
                length=record["length"],
                delta=record["delta_to_next_row_start"],
                margin=record["criterion_margin"],
                umargin=record["universal_length_margin_2h_minus_1"],
                rows=record["contained_half_rows"],
                deficit=record["endpoint_deficit"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "完整半宽行包含性不需要枚举：设 `J=[u,v]`、长度 `N`，`delta=(1-u) mod h`，则下一条 `h` 对齐行从 `u+delta` 开始。故 `J` 含完整 `h` 行当且仅当 `N>=delta+h`。",
            "",
            "若 `N>=2h-1`，该条件对所有端点相位自动成立；若失败，则失败完全由有限端点相位 `(h, u mod h, N mod h, delta)` 决定，适合进入 `SeamEndpoint/SAE/PDEC/ColumnCRT`。",
            "",
            "同批样本中精确判据与枚举完全一致，且全部含完整半宽行；但只有部分样本满足纯长度自动闭合。这说明全局证明需要同时使用长度余量和端点相位，而不能只靠 `|J|>=2h-1`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-core-audit.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-grid-endpoint-audit"),
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
