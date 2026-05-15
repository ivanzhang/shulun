#!/usr/bin/env python3
"""审计 z=61 positive lift carry-layer 目标纤维到 signed-sum 门的接桥。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_to_signed_sum_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-to-signed-sum-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-to-signed-sum-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-to-signed-sum-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
POSITIVE_CARRY_JSON = (
    DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json"
)
SIGNED_SUM_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json"
OUT_JSON = (
    DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-to-signed-sum-bridge-router.json"
)
OUT_MD = (
    DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-to-signed-sum-bridge-router.md"
)

NEXT_TARGET = "FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-positive-lift-carry-layer-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_to_signed_sum_bridge_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def selected_signed_sum_row(source: dict[str, Any]) -> dict[str, Any]:
    """当前证书只有一个 formal-unit 组；这里显式守住这个边界。"""
    rows = source["signed_sum_rows"]
    if len(rows) != 1:
        raise ValueError(f"expected one signed-sum row, got {len(rows)}")
    return rows[0]


def audit() -> dict[str, Any]:
    """执行 positive-lift carry 到 signed-sum 的接桥审计。"""
    positive = load(POSITIVE_CARRY_JSON)
    signed_sum = load(SIGNED_SUM_JSON)
    row = selected_signed_sum_row(signed_sum)
    selected_layer = next(layer for layer in row["layer_rows"] if layer["carry"] == row["selected_carry"])

    # 这一步只比较同一对象的三种坐标：root residue、carry layer、signed-sum interval。
    carry_identity_closed = (
        positive["positive_lift_carry_layer_bridge_closed_for_sample"]
        and signed_sum["all_signed_sum_residue_gates_closed"]
        and row["signed_sum_residue_gate_closed_for_group"]
        and positive["target_bucket"] == signed_sum["target_bucket"] == "unbalanced<=8"
        and positive["target_omega"] == signed_sum["target_omega"] == 4
        and positive["target_shell"] == signed_sum["target_shell"] == "(8D,16D]"
        and positive["modulus"] == row["modulus"] == 57684
        and positive["q2"] == row["q2"] == 71
        and positive["q4"] == row["q4"] == 37
        and positive["selected_residue"] == row["selected_residue"] == 26951
        and positive["selected_sign_word"] == row["selected_sign_word"] == "--++-"
        and positive["selected_carry"] == row["selected_carry"] == 6
        and positive["carry_values"] == row["carry_values"]
        and positive["combined_target_hit_count"] == row["combined_hit_count"] == 1
        and positive["nonempty_target_layers"][0]["combined_hit_words"] == row["combined_hit_words"]
        and selected_layer["combined_hit_words"] == row["combined_hit_words"] == ["--++-:26951"]
        and selected_layer["q4_hit_count"] == selected_layer["q2_hit_count"] == 1
        and row["selected_signed_sum"] == 373055
        and row["selected_sum_mod_2627"] == 21
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_positive_lift_carry_to_signed_sum_bridge_router",
        "status": "z61_positive_lift_carry_layer_reduced_to_five_term_signed_sum_residue_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            positive["certificate_type"],
            signed_sum["certificate_type"],
        ],
        "target_bucket": positive["target_bucket"],
        "target_omega": positive["target_omega"],
        "target_shell": positive["target_shell"],
        "modulus": positive["modulus"],
        "q2": positive["q2"],
        "q4": positive["q4"],
        "selected_residue": positive["selected_residue"],
        "selected_sign_word": positive["selected_sign_word"],
        "selected_carry": positive["selected_carry"],
        "selected_signed_sum": row["selected_signed_sum"],
        "selected_sum_mod_2627": row["selected_sum_mod_2627"],
        "signed_coefficients": row["signed_coefficients"],
        "carry_values": row["carry_values"],
        "selected_layer_sign_count": positive["selected_layer_sign_count"],
        "positive_lift_target_words": positive["nonempty_target_layers"][0]["combined_hit_words"],
        "signed_sum_target_words": row["combined_hit_words"],
        "selected_layer_q4_hit_count": selected_layer["q4_hit_count"],
        "selected_layer_q2_hit_count": selected_layer["q2_hit_count"],
        "selected_layer_combined_hit_count": selected_layer["combined_hit_count"],
        "positive_lift_carry_to_signed_sum_bridge_closed_for_sample": carry_identity_closed,
        "five_term_signed_sum_interval_residue_global_bound_proved": False,
        "sum_residue_pdec_excluded": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "positive-lift/MissingLift 链上的 carry=6 目标纤维与已有五项 signed-sum "
            "区间同余门是同一对象：唯一目标词都是 `--++-:26951`，对应 "
            "`S=373055`、`S mod 2627=21`。因此当前剩余从 "
            "`CarryLayerTargetFiberGlobalBoundOrMissingLiftPDEC` 正式压到 "
            "`FiveTermSignedSumIntervalResidueGlobalBoundOrSumResiduePDEC`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 positive lift carry to signed-sum bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"selected_carry={result['selected_carry']}",
        f"selected_sign_word={result['selected_sign_word']}",
        f"selected_residue={result['selected_residue']}",
        f"selected_signed_sum={result['selected_signed_sum']}",
        f"selected_sum_mod_2627={result['selected_sum_mod_2627']}",
        f"positive_lift_carry_to_signed_sum_bridge_closed_for_sample={fmt_bool(result['positive_lift_carry_to_signed_sum_bridge_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 对齐摘要",
        "",
        "| M | coefficients | carry | sign | root r | S | S mod 2627 | target words |",
        "| ---: | --- | ---: | --- | ---: | ---: | ---: | --- |",
        f"| {result['modulus']} | `{result['signed_coefficients']}` | "
        f"{result['selected_carry']} | `{result['selected_sign_word']}` | "
        f"{result['selected_residue']} | {result['selected_signed_sum']} | "
        f"{result['selected_sum_mod_2627']} | `{result['signed_sum_target_words']}` |",
        "",
        "## 2. 同一性检查",
        "",
        "| check | value |",
        "| --- | --- |",
        f"| carry values | `{result['carry_values']}` |",
        f"| selected layer sign count | {result['selected_layer_sign_count']} |",
        f"| positive-lift target words | `{result['positive_lift_target_words']}` |",
        f"| signed-sum target words | `{result['signed_sum_target_words']}` |",
        f"| selected layer q4 hits | {result['selected_layer_q4_hit_count']} |",
        f"| selected layer q2 hits | {result['selected_layer_q2_hit_count']} |",
        f"| selected layer combined hits | {result['selected_layer_combined_hit_count']} |",
        "",
        "## 3. 证明边界",
        "",
        "- 已闭合：当前 positive-lift carry 纤维与五项 signed-sum 区间同余门严格接桥。",
        "- 未闭合：五项 signed-sum 区间同余纤维的全局界，或 SumResidue/MissingLift-PDEC 排斥。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
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
                "bridge_closed": result["positive_lift_carry_to_signed_sum_bridge_closed_for_sample"],
                "selected_sign_word": result["selected_sign_word"],
                "selected_carry": result["selected_carry"],
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
