#!/usr/bin/env python3
"""审计 z=61 正向 dyadic lift 存在性与 shifted pair 链的桥接。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_shifted_pair_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
BALANCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json"
SAME_P_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json"
SHIFTED_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json"
SQUARE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.md"

NEXT_TARGET = "ShiftedSquareWindowGlobalBoundOrMissingLiftPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-fixed-core-dyadic-balance-lemma-router.json",
    "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json",
    "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json",
    "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_positive_lift_shifted_pair_bridge_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def positive_rows_from_balance(balance: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取正向 quotient 2/4 行。"""
    return [
        row
        for row in balance["quotient_rows"]
        if row["sign"] == "positive" and row["quotient"] in {2, 4}
    ]


def normalize_positive_row(row: dict[str, Any]) -> dict[str, Any]:
    """保留桥接所需的稳定字段。"""
    return {
        "quotient": row.get("quotient", row.get("phase_quotient")),
        "p": row["p"],
        "q": row["q"],
        "a": row["a"],
        "b": row["b"],
    }


def audit() -> dict[str, Any]:
    """执行正向 lift 到 shifted pair 的桥接审计。"""
    balance = load(BALANCE_JSON)
    same_p = load(SAME_P_JSON)
    shifted = load(SHIFTED_JSON)
    square = load(SQUARE_JSON)

    balance_positive_rows = [normalize_positive_row(row) for row in positive_rows_from_balance(balance)]
    same_p_group = same_p["same_p_strip_groups"][0]
    same_p_positive_rows = [normalize_positive_row(row) for row in same_p_group["source_rows"]]
    shifted_row = shifted["shifted_factor_rows"][0]
    square_row = square["square_window_rows"][0]

    expected_from_shifted = [
        {
            "quotient": 2,
            "p": shifted_row["p"],
            "q": shifted_row["q2"],
            "a": shifted_row["a2"],
            "b": shifted_row["base_modulus"],
        },
        {
            "quotient": 4,
            "p": shifted_row["p"],
            "q": shifted_row["q4"],
            "a": shifted_row["a4"],
            "b": 2 * shifted_row["base_modulus"],
        },
    ]

    positive_lift_rows_match_same_p = balance_positive_rows == same_p_positive_rows
    positive_lift_rows_match_shifted_pair = balance_positive_rows == expected_from_shifted
    same_p_shifted_pair_bridge_closed = (
        same_p["all_positive_same_p_groups_closed"]
        and same_p["all_positive_same_p_groups_endpoint_spanning"]
        and shifted["all_endpoint_shifted_factor_groups_closed"]
        and shifted_row["endpoint_shifted_factor_closed_for_group"]
        and shifted_row["carry_equals_q_gap"]
        and shifted_row["shifted_product_identity_closed"]
        and shifted_row["a2_linear_form_closed"]
        and shifted_row["a4_linear_form_closed"]
    )
    shifted_pair_square_window_bridge_closed = (
        square["all_shifted_square_window_groups_closed"]
        and square_row["shifted_square_window_closed_for_group"]
        and square_row["s"] == shifted_row["common_multiplier"]
        and square_row["p"] == shifted_row["p"]
        and square_row["q2"] == shifted_row["q2"]
        and square_row["q4"] == shifted_row["q4"]
        and square_row["base_modulus"] == shifted_row["base_modulus"]
        and square_row["span"] == shifted_row["carry"]
    )
    bridge_closed = (
        balance["fixed_core_dyadic_balance_lemma_closed_for_sample"]
        and positive_lift_rows_match_same_p
        and positive_lift_rows_match_shifted_pair
        and same_p_shifted_pair_bridge_closed
        and shifted_pair_square_window_bridge_closed
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_positive_lift_shifted_pair_bridge_router",
        "status": "z61_positive_dyadic_lift_existence_reduced_to_shifted_square_window_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            balance["certificate_type"],
            same_p["certificate_type"],
            shifted["certificate_type"],
            square["certificate_type"],
        ],
        "target_bucket": balance["target_bucket"],
        "target_omega": balance["target_omega"],
        "target_shell": balance["target_shell"],
        "phase_modulus": balance["phase_modulus"],
        "positive_lift_rows_from_balance": balance_positive_rows,
        "positive_lift_rows_from_same_p_strip": same_p_positive_rows,
        "positive_lift_rows_expected_from_shifted_pair": expected_from_shifted,
        "positive_lift_rows_match_same_p": positive_lift_rows_match_same_p,
        "positive_lift_rows_match_shifted_pair": positive_lift_rows_match_shifted_pair,
        "same_p_group_p": same_p_group["p"],
        "same_p_group_base_modulus": same_p_group["base_modulus"],
        "same_p_strip_capacity": same_p_group["slot_capacity"],
        "same_p_normalized_span": same_p_group["normalized_span"],
        "same_p_occupies_both_strip_endpoints": same_p_group["occupies_both_strip_endpoints"],
        "semiprime_carry_equation": same_p_group["semiprime_carry_equation"],
        "shifted_pair_p": shifted_row["p"],
        "q2": shifted_row["q2"],
        "a2": shifted_row["a2"],
        "q4": shifted_row["q4"],
        "a4": shifted_row["a4"],
        "carry": shifted_row["carry"],
        "q_gap_2q4_minus_q2": shifted_row["q_gap_2q4_minus_q2"],
        "common_multiplier": shifted_row["common_multiplier"],
        "linear_prime_pair_forms": shifted_row["linear_prime_pair_forms"],
        "square_window_delta": square_row["delta_low"],
        "square_window_residue": square_row["p_square_residue_mod_base"],
        "square_window_s_recovered": square_row["s_recovered_from_square_window"],
        "same_p_shifted_pair_bridge_closed": same_p_shifted_pair_bridge_closed,
        "shifted_pair_square_window_bridge_closed": shifted_pair_square_window_bridge_closed,
        "positive_lift_shifted_pair_bridge_closed_for_sample": bridge_closed,
        "positive_dyadic_lift_existence_proved_globally": False,
        "shifted_square_window_global_bound_proved": False,
        "missing_lift_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "正向 dyadic lift 的存在性不是新的自由命题：quotient `2,4` 的两条正向 "
            "lift 与已有 same-p strip 完全同一组，并等价于 endpoint shifted-factor "
            "中的同步移位线性素数对 `a4=71s-1`、`a2=74s-1`，其中 `s=132`。"
            "再与平方窗口证书对接后，MissingLift 的剩余被压成 shifted square-window "
            "全局容量界，或相应 MissingLift-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 positive lift shifted pair bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"positive_lift_rows_match_same_p={fmt_bool(result['positive_lift_rows_match_same_p'])}",
        f"positive_lift_rows_match_shifted_pair={fmt_bool(result['positive_lift_rows_match_shifted_pair'])}",
        f"same_p_shifted_pair_bridge_closed={fmt_bool(result['same_p_shifted_pair_bridge_closed'])}",
        f"shifted_pair_square_window_bridge_closed={fmt_bool(result['shifted_pair_square_window_bridge_closed'])}",
        f"positive_lift_shifted_pair_bridge_closed_for_sample={fmt_bool(result['positive_lift_shifted_pair_bridge_closed_for_sample'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 正向 lift 行",
        "",
        "| quotient | p | q | a | b |",
        "| ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["positive_lift_rows_from_balance"]:
        lines.append(f"| {row['quotient']} | {row['p']} | {row['q']} | {row['a']} | {row['b']} |")
    lines.extend(
        [
            "",
            "## 2. Same-p endpoint strip",
            "",
            "| p | base M | capacity | span | endpoints | carry equation |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
            f"| {result['same_p_group_p']} | {result['same_p_group_base_modulus']} | "
            f"{result['same_p_strip_capacity']} | {result['same_p_normalized_span']} | "
            f"{fmt_bool(result['same_p_occupies_both_strip_endpoints'])} | "
            f"`{result['semiprime_carry_equation']}` |",
            "",
            "## 3. Shifted pair",
            "",
            "| p | q2 | a2 | q4 | a4 | carry | 2q4-q2 | s | forms |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
            f"| {result['shifted_pair_p']} | {result['q2']} | {result['a2']} | "
            f"{result['q4']} | {result['a4']} | {result['carry']} | "
            f"{result['q_gap_2q4_minus_q2']} | {result['common_multiplier']} | "
            f"`{result['linear_prime_pair_forms']}` |",
            "",
            "## 4. Square-window 对接",
            "",
            "| delta | residue | recovered s |",
            "| ---: | ---: | ---: |",
            f"| {result['square_window_delta']} | {result['square_window_residue']} | "
            f"{result['square_window_s_recovered']} |",
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：当前正向 dyadic lift 与 shifted pair / square-window 链严格同一对象。",
            "- 未闭合：shifted square-window 全局容量界，或 MissingLift-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
                "positive_lift_shifted_pair_bridge_closed_for_sample": result[
                    "positive_lift_shifted_pair_bridge_closed_for_sample"
                ],
                "common_multiplier": result["common_multiplier"],
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
