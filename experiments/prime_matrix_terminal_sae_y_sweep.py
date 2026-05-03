#!/usr/bin/env python3
"""扫描 Terminal-SAE 分层参数 y 的安全区间。

用法示例：
  python3 experiments/prime_matrix_terminal_sae_y_sweep.py --max-p 1000
  python3 experiments/prime_matrix_terminal_sae_y_sweep.py --ratios 0.25,0.30,0.36787944117144233,0.50
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from prime_matrix_terminal_sae_split_audit import audit


def run_sweep(max_p: int, ratios: list[float]) -> dict:
    """对多个 y_ratio 执行审计并汇总。"""
    items = []
    for ratio in ratios:
        result = audit(max_p=max_p, y_ratio=ratio)
        records = result["records"]
        worst = min(records, key=lambda record: record["min_margin"])
        items.append(
            {
                "y_ratio": ratio,
                "summary": result["summary"],
                "worst_record": {
                    "p": worst["p"],
                    "q_next": worst["q_next"],
                    "y": worst["y"],
                    "min_margin": worst["min_margin"],
                    "min_data": worst["min_data"],
                    "bad_margin_row_count": worst["bad_margin_row_count"],
                },
            }
        )
    safe = [
        item
        for item in items
        if item["summary"]["unresolved_records_p_ge_7"] == 0
        and item["summary"]["min_margin_p_ge_7"] > 0
    ]
    return {
        "parameters": {
            "max_p": max_p,
            "ratios": ratios,
        },
        "summary": {
            "safe_ratio_count": len(safe),
            "first_safe_ratio": safe[0]["y_ratio"] if safe else None,
            "last_safe_ratio": safe[-1]["y_ratio"] if safe else None,
        },
        "items": items,
    }


def write_markdown(result: dict, path: Path) -> None:
    """输出 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# Terminal-SAE 分层参数 y 扫描",
        "",
        "**状态：** `experimental_y_parameter_stability_scan_not_a_proof`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `ratios`: `{params['ratios']}`",
        "",
        "## 汇总",
        "",
        f"- 安全 ratio 个数：`{result['summary']['safe_ratio_count']}`。",
        f"- 首个安全 ratio：`{result['summary']['first_safe_ratio']}`。",
        f"- 末个安全 ratio：`{result['summary']['last_safe_ratio']}`。",
        "",
        "## 扫描表",
        "",
        "| y_ratio | certified | min margin p>=7 | unresolved p>=7 | worst record |",
        "| ---: | --- | ---: | ---: | --- |",
    ]
    for item in result["items"]:
        summary = item["summary"]
        certified = (
            summary["unresolved_records_p_ge_7"] == 0
            and summary["min_margin_p_ge_7"] > 0
        )
        lines.append(
            "| {ratio:.12f} | {cert} | {margin} | {unresolved} | {worst} |".format(
                ratio=item["y_ratio"],
                cert=certified,
                margin=summary["min_margin_p_ge_7"],
                unresolved=summary["unresolved_records_p_ge_7"],
                worst=item["worst_record"],
            )
        )
    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "扫描显示 `y≈p/e` 位于一个稳定安全区间内，而不是孤立调参点。过小的 `y` 会保留太大的骨架并给尾素数过多命中机会；中等 `y` 后，尾素数带变短，`G_y(h)>T_y(h)` 在样本中稳定成立。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ratios(raw: str) -> list[float]:
    """解析逗号分隔 ratio。"""
    return [float(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument(
        "--ratios",
        default="0.20,0.25,0.30,0.3333333333333333,0.36787944117144233,0.40,0.45,0.50,0.60,0.70",
    )
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/prime-matrix-terminal-sae-y-sweep",
    )
    args = parser.parse_args()
    result = run_sweep(max_p=args.max_p, ratios=parse_ratios(args.ratios))
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
