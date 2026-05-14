#!/usr/bin/env python3
"""审计 z=61 singleton interval gate 的显式残基门。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_singleton_residue_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
INTERVAL_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-singleton-residue-gate-router.md"

NEXT_TARGET = "SingletonResidueGateSignedCountBalanceOrResiduePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-source-fiber-singleton-interval-router.json",
]


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
        "experiments/prime_matrix_square_phase_lowalpha_z61_singleton_residue_gate_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def audit() -> dict[str, Any]:
    """执行显式残基门审计。"""
    data = json.loads(INTERVAL_JSON.read_text(encoding="utf-8"))
    rows = []
    for row in data["rows"]:
        modulus = row["modulus_bq"]
        delta = row["left_slack_abq_minus_p2"]
        residue = row["p"] * row["p"] % modulus
        expected_residue = (modulus - delta) % modulus
        rows.append(
            {
                "phase_quotient": row["phase_quotient"],
                "target_cell_sign": row["target_cell_sign"],
                "p": row["p"],
                "q": row["q"],
                "a": row["a"],
                "b": row["b"],
                "modulus_bq": modulus,
                "delta_abq_minus_p2": delta,
                "residue_p2_mod_bq": residue,
                "expected_negative_delta_residue": expected_residue,
                "residue_identity_closed": residue == expected_residue,
                "short_delta_bound_closed": 0 < delta < row["p"],
                "residue_gate_statement": f"p^2 ≡ {expected_residue} (mod {modulus})",
            }
        )
    positive_rows = [row for row in rows if row["target_cell_sign"] == "positive"]
    negative_rows = [row for row in rows if row["target_cell_sign"] == "negative"]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_singleton_residue_gate_router",
        "status": "z61_singleton_interval_gate_reduced_to_short_residue_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "phase_modulus": data["phase_modulus"],
        "phase_condition": data["phase_condition"],
        "rows": rows,
        "all_residue_gates_closed": all(row["residue_identity_closed"] for row in rows),
        "all_short_delta_bounds_closed": all(row["short_delta_bound_closed"] for row in rows),
        "positive_residue_gate_count": len(positive_rows),
        "negative_residue_gate_count": len(negative_rows),
        "positive_minus_negative_residue_gate_count": len(positive_rows) - len(negative_rows),
        "singleton_residue_gate_signed_count_balance_proved": False,
        "residue_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "singleton interval gate 已等价改写为短残基门：每条源纤维满足 "
            "`p^2 ≡ -delta (mod bq)` 且 `0<delta<p`。"
            "因此剩余问题不再是区间宽度，而是这些短残基门的有符号计数平衡，"
            "或将持续残基偏斜登记为 Residue-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 singleton residue gate",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"all_residue_gates_closed={fmt_bool(result['all_residue_gates_closed'])}",
        f"all_short_delta_bounds_closed={fmt_bool(result['all_short_delta_bounds_closed'])}",
        f"positive_residue_gate_count={result['positive_residue_gate_count']}",
        f"negative_residue_gate_count={result['negative_residue_gate_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 短残基门",
        "",
        "| quotient | sign | p | bq | delta | residue | statement |",
        "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            f"| {row['phase_quotient']} | `{row['target_cell_sign']}` | {row['p']} | "
            f"{row['modulus_bq']} | {row['delta_abq_minus_p2']} | "
            f"{row['residue_p2_mod_bq']} | `{row['residue_gate_statement']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：singleton interval 到短残基门的等价。",
            "- 未闭合：短残基门的有符号计数平衡，或 Residue-PDEC 排斥。",
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
                "all_residue_gates_closed": result["all_residue_gates_closed"],
                "positive_minus_negative_residue_gate_count": result[
                    "positive_minus_negative_residue_gate_count"
                ],
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
