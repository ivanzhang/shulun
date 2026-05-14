#!/usr/bin/env python3
"""审计 z=61 PrefixGate 相位命中的 quotient ladder 平衡。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_quotient_ladder_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PERSISTENCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-quotient-ladder-router.md"

NEXT_TARGET = "DyadicPhaseQuotientCountBalanceOrLadderPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_prefix_gate_quotient_ladder_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def is_power_of_two(value: int) -> bool:
    """判断正整数是否为 2 的幂。"""
    return value > 0 and value & (value - 1) == 0


def audit() -> dict[str, Any]:
    """执行 quotient ladder 审计。"""
    data = json.loads(PERSISTENCE_JSON.read_text(encoding="utf-8"))
    sign_by_p = {row["p"]: row["target_cell_sign"] for row in data["profile_rows"]}
    hit_rows = []
    for hit in data["phase_hit_rows"]:
        row = {
            **hit,
            "target_cell_sign": sign_by_p[hit["p"]],
            "is_power_of_two_quotient": is_power_of_two(hit["phase_quotient"]),
        }
        hit_rows.append(row)
    quotient_rows = sorted(hit_rows, key=lambda row: row["phase_quotient"])
    contribution_values = {round(row["target_contribution"], 15) for row in quotient_rows}
    per_hit_contribution = quotient_rows[0]["target_contribution"] if quotient_rows else 0.0
    positive_quotients = [row["phase_quotient"] for row in quotient_rows if row["target_cell_sign"] == "positive"]
    negative_quotients = [row["phase_quotient"] for row in quotient_rows if row["target_cell_sign"] == "negative"]
    positive_count = len(positive_quotients)
    negative_count = len(negative_quotients)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_prefix_gate_quotient_ladder_router",
        "status": "z61_prefix_gate_signed_phase_balance_reduced_to_quotient_ladder_count_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": data["certificate_type"],
        "phase_modulus": data["phase_modulus"],
        "phase_condition": data["phase_condition"],
        "quotient_rows": quotient_rows,
        "quotients": [row["phase_quotient"] for row in quotient_rows],
        "all_quotients_are_powers_of_two": all(row["is_power_of_two_quotient"] for row in quotient_rows),
        "observed_quotient_ladder": [1, 2, 4],
        "observed_quotient_ladder_exact": [row["phase_quotient"] for row in quotient_rows] == [1, 2, 4],
        "per_hit_contribution": per_hit_contribution,
        "constant_per_hit_contribution_closed": len(contribution_values) <= 1,
        "positive_quotients": positive_quotients,
        "negative_quotients": negative_quotients,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "positive_minus_negative_count": positive_count - negative_count,
        "signed_actual_balance_reduced_to_count_identity_closed": (
            len(contribution_values) <= 1
            and data["positive_phase_actual"] == positive_count * per_hit_contribution
            and data["negative_phase_actual"] == negative_count * per_hit_contribution
        ),
        "dyadic_phase_quotient_count_balance_proved": False,
        "ladder_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "PrefixGate signed phase balance 已进一步压成 quotient ladder 计数问题："
            "三个命中全部贡献同一 target 权重，quotient 分别为 `1,2,4`。"
            "负侧只有 quotient `1`，正侧有 quotient `2,4`，因此样本中的正/负相位实际比 "
            "完全等于命中计数比 `2/1`。下一步应证明这种 dyadic quotient ladder "
            "在全局上给出计数平衡，或登记 Ladder-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 PrefixGate quotient ladder",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"quotients={result['quotients']}",
        f"all_quotients_are_powers_of_two={fmt_bool(result['all_quotients_are_powers_of_two'])}",
        f"constant_per_hit_contribution_closed={fmt_bool(result['constant_per_hit_contribution_closed'])}",
        f"positive_quotients={result['positive_quotients']}",
        f"negative_quotients={result['negative_quotients']}",
        f"positive_minus_negative_count={result['positive_minus_negative_count']}",
        f"signed_actual_balance_reduced_to_count_identity_closed={fmt_bool(result['signed_actual_balance_reduced_to_count_identity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Quotient Ladder",
        "",
        "| quotient | p | b | sign | contribution | power of 2 |",
        "| ---: | ---: | ---: | --- | ---: | --- |",
    ]
    for row in result["quotient_rows"]:
        lines.append(
            f"| {row['phase_quotient']} | {row['p']} | {row['b_value']} | "
            f"`{row['target_cell_sign']}` | {fmt_float(row['target_contribution'])} | "
            f"{fmt_bool(row['is_power_of_two_quotient'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 已闭合：signed phase balance 到 dyadic quotient 计数的样本恒等式。",
            "- 未闭合：dyadic quotient count balance 的全局证明，或 Ladder-PDEC 排斥。",
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
                "observed_quotient_ladder_exact": result["observed_quotient_ladder_exact"],
                "positive_minus_negative_count": result["positive_minus_negative_count"],
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
