#!/usr/bin/env python3
"""从 Jacobsthal 风险扫描抽取 BCB 平台长度阈值。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_platform_length_threshold.py

BCB no-TailAnchor 分支闭合条件是

  G(h) < P + m - 1 - 2T。

因此给定 `(h,P,T)` 后，平台长度必须满足

  m >= G(h) - P + 2 + 2T。

本脚本把 `prime-matrix-rpz-bcb-jacobsthal-risk-scan.json` 中的风险数据
改写为平台长度阈值表。目标是把下一硬点从“Jacobsthal 上界”进一步
压成“formal BCB 平台长度增长或出口触发”。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def required_platform_length(max_covered_run: int, top_prime: int, tail_threshold: int) -> int:
    """返回闭合 `G(h)<P+m-1-2T` 所需的最小整数 `m`。"""
    return max(1, max_covered_run - top_prime + 2 + 2 * tail_threshold)


def build(risk_path: Path, max_tail_threshold: int) -> dict[str, Any]:
    """构造平台长度阈值账本。"""
    risk = json.loads(risk_path.read_text(encoding="utf-8"))
    rows = risk["rows"]
    threshold_rows = []
    for row in rows:
        thresholds = {
            str(tail_threshold): required_platform_length(
                row["max_covered_run_G"],
                row["minimal_top_prime_gt_2h"],
                tail_threshold,
            )
            for tail_threshold in range(max_tail_threshold + 1)
        }
        threshold_rows.append(
            {
                "h": row["h"],
                "G_h": row["max_covered_run_G"],
                "minimal_top_prime_gt_2h": row["minimal_top_prime_gt_2h"],
                "required_m_by_T": thresholds,
                "required_m_T4": thresholds.get("4"),
                "T4_fixed_m5_safe": thresholds.get("4", 1) <= 5,
            }
        )

    unsafe_t4 = [row for row in threshold_rows if not row["T4_fixed_m5_safe"]]
    unsafe_t4_h_ge_5 = [row for row in unsafe_t4 if row["h"] >= 5]
    return {
        "status": "rpz_bcb_platform_length_threshold",
        "source": str(risk_path),
        "summary": {
            "rows": len(threshold_rows),
            "max_tail_threshold": max_tail_threshold,
            "T4_fixed_m5_unsafe_rows": len(unsafe_t4),
            "first_T4_fixed_m5_unsafe": unsafe_t4[0] if unsafe_t4 else None,
            "first_T4_fixed_m5_unsafe_h_ge_5": (
                unsafe_t4_h_ge_5[0] if unsafe_t4_h_ge_5 else None
            ),
            "max_required_m_T4": max(
                row["required_m_T4"] or 0
                for row in threshold_rows
            ),
        },
        "threshold_rows": threshold_rows,
        "review_boundary": [
            "BCB no-TailAnchor 闭合等价于平台长度满足 m >= G(h)-P+2+2T。",
            "固定 m=5,T=4 不能全局闭合。",
            "下一证明目标是 formal BCB 短平台必触发 TailAnchor/endpoint/first-failure，或证明 m 达到该阈值。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    summary = result["summary"]
    first_unsafe = summary["first_T4_fixed_m5_unsafe"]
    first_unsafe_h_ge_5 = summary["first_T4_fixed_m5_unsafe_h_ge_5"]
    lines = [
        "# RPZ-BCB 平台长度阈值账本",
        "",
        "**状态：** `rpz_bcb_platform_length_threshold`",
        "",
        "## 总结",
        "",
        f"- 数据行数：`{summary['rows']}`。",
        f"- T 扫描上界：`{summary['max_tail_threshold']}`。",
        f"- `T=4,m=5` 不安全行数：`{summary['T4_fixed_m5_unsafe_rows']}`。",
        f"- 首个 `T=4,m=5` 不安全层：`{first_unsafe}`。",
        f"- 首个 `h>=5` 的实质不安全层：`{first_unsafe_h_ge_5}`。",
        f"- `T=4` 最大所需平台长度：`{summary['max_required_m_T4']}`。",
        "",
        "## 精确阈值",
        "",
        "BCB no-TailAnchor 分支闭合条件",
        "",
        "```text",
        "G(h) < P+m-1-2T",
        "```",
        "",
        "等价于整数平台长度阈值",
        "",
        "```text",
        "m >= G(h)-P+2+2T。",
        "```",
        "",
        "因此全局闭合不能只说 `m` 非零；必须证明正式平台长度达到该阈值，或证明短平台触发出口。",
        "",
        "## 阈值摘录",
        "",
        "| h | G(h) | minimal top P | required m T=0 | required m T=2 | required m T=4 | T4 m=5 safe |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in result["threshold_rows"][:30]:
        thresholds = row["required_m_by_T"]
        lines.append(
            "| {h} | {G} | {P} | {t0} | {t2} | {t4} | `{safe}` |".format(
                h=row["h"],
                G=row["G_h"],
                P=row["minimal_top_prime_gt_2h"],
                t0=thresholds["0"],
                t2=thresholds["2"],
                t4=thresholds["4"],
                safe=row["T4_fixed_m5_safe"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿结论",
            "",
            "当前最小硬点已经不是 accepted-preimage 枚举，而是平台长度增长定理：formal BCB 平台必须满足 `m >= G(h)-P+2+2T`。",
            "若不能证明该增长，则短平台层不能由 Jacobsthal 长度障碍闭合，必须触发 TailAnchor、endpoint、first-failure、PDEC 或 ColumnCRT 出口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--risk",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-jacobsthal-risk-scan.json"),
    )
    parser.add_argument("--max-tail-threshold", type=int, default=4)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-platform-length-threshold"),
    )
    args = parser.parse_args()

    result = build(args.risk, args.max_tail_threshold)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
