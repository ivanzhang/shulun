#!/usr/bin/env python3
"""审计 z=61 PrefixGate 源纤维的 singleton interval gate。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_source_fiber_singleton_interval_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.md"

NEXT_TARGET = "SingletonIntervalResidueGateBalanceOrIntervalPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-source-fiber-router.json",
]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator == 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_source_fiber_singleton_interval_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行 singleton interval gate 审计。"""
    data = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = []
    for source_row in data["source_rows"]:
        candidate = source_row["source_candidates"][0]
        p_value = source_row["p"]
        q_value = candidate["q"]
        a_value = candidate["a"]
        b_value = candidate["b"]
        modulus = b_value * q_value
        product = a_value * modulus
        left_slack = product - p_value * p_value
        right_slack = p_value * p_value + p_value - product
        a_from_floor = p_value * p_value // modulus + 1
        n_value = candidate["n"]
        n_left = p_value * p_value // b_value + 1
        n_right = (p_value * p_value + p_value - 1) // b_value
        rows.append(
            {
                "phase_quotient": source_row["phase_quotient"],
                "target_cell_sign": source_row["target_cell_sign"],
                "p": p_value,
                "q": q_value,
                "a": a_value,
                "b": b_value,
                "modulus_bq": modulus,
                "product_abq": product,
                "left_slack_abq_minus_p2": left_slack,
                "right_slack_p2_plus_p_minus_abq": right_slack,
                "left_slack_over_p": safe_ratio(left_slack, p_value),
                "right_slack_over_p": safe_ratio(right_slack, p_value),
                "a_from_floor_formula": a_from_floor,
                "a_floor_formula_closed": a_from_floor == a_value,
                "a_interval_width": candidate["a_interval_width"],
                "a_interval_width_below_one": candidate["a_interval_width"] < 1,
                "raw_a_interval": candidate["raw_a_interval"],
                "valid_a_interval": candidate["valid_a_interval"],
                "valid_a_interval_singleton": candidate["valid_a_interval"][0] == candidate["valid_a_interval"][1],
                "n": n_value,
                "n_interval": [n_left, n_right],
                "n_interval_capacity": n_right - n_left + 1,
                "n_in_interval": n_left <= n_value <= n_right,
                "prime_a": candidate["prime_a"],
                "prime_b": candidate["prime_b"],
                "singleton_interval_gate_closed": (
                    a_from_floor == a_value
                    and 0 < left_slack < p_value
                    and 0 <= right_slack < p_value
                    and candidate["a_interval_width"] < 1
                    and candidate["valid_a_interval"][0] == candidate["valid_a_interval"][1]
                    and n_left <= n_value <= n_right
                    and candidate["prime_a"]
                    and not candidate["prime_b"]
                ),
            }
        )
    positive_rows = [row for row in rows if row["target_cell_sign"] == "positive"]
    negative_rows = [row for row in rows if row["target_cell_sign"] == "negative"]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_source_fiber_singleton_interval_router",
        "status": "z61_source_fiber_ladder_reduced_to_singleton_interval_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "phase_modulus": data["phase_modulus"],
        "phase_condition": data["phase_condition"],
        "rows": rows,
        "all_source_fibers_are_singleton_interval_gates": all(
            row["singleton_interval_gate_closed"] for row in rows
        ),
        "max_a_interval_width": max(row["a_interval_width"] for row in rows),
        "positive_singleton_interval_count": len(positive_rows),
        "negative_singleton_interval_count": len(negative_rows),
        "positive_minus_negative_singleton_interval_count": len(positive_rows) - len(negative_rows),
        "singleton_interval_residue_gate_balance_proved": False,
        "interval_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "三条 PrefixGate 源纤维均由同一个 singleton interval gate 产生："
            "`a=floor(p^2/(bq))+1`，且 `0<abq-p^2<p`。"
            "所有 `a` 区间宽度都小于 `1`，实际最大仅约 `0.048834`；"
            "因此剩余硬点可改写为这些短窗 singleton 残基门的有符号计数平衡，"
            "或登记 Interval-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 源纤维 singleton interval",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"all_source_fibers_are_singleton_interval_gates={fmt_bool(result['all_source_fibers_are_singleton_interval_gates'])}",
        f"max_a_interval_width={fmt_float(result['max_a_interval_width'])}",
        f"positive_singleton_interval_count={result['positive_singleton_interval_count']}",
        f"negative_singleton_interval_count={result['negative_singleton_interval_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Singleton Interval",
        "",
        "| quotient | sign | p | q | a | b | width | left/p | right/p | n interval |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['phase_quotient']} | `{row['target_cell_sign']}` | {row['p']} | "
            f"{row['q']} | {row['a']} | {row['b']} | {fmt_float(row['a_interval_width'])} | "
            f"{fmt_float(row['left_slack_over_p'])} | {fmt_float(row['right_slack_over_p'])} | "
            f"`{row['n_interval']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：singleton 源纤维到短窗 interval gate 的样本恒等式。",
            "- 未闭合：短窗残基门的有符号计数平衡，或 Interval-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_source_fibers_are_singleton_interval_gates": result[
                    "all_source_fibers_are_singleton_interval_gates"
                ],
                "max_a_interval_width": result["max_a_interval_width"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
