#!/usr/bin/env python3
"""审计 z=61 dyadic 正 lift 的同 p 短条带 carry 结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_same_p_strip_carry_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-same-p-strip-carry-router.md"

BASE_QUOTIENT = 2
NEXT_TARGET = "EndpointSpanningSemiprimePairGlobalBoundOrEndpointPairPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_same_p_strip_carry_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def floor_div(numerator: int, denominator: int) -> int:
    """整数下取整。"""
    return numerator // denominator


def normalized_source(row: dict[str, Any]) -> dict[str, Any]:
    """把 quotient 2、4 的源纤维归一到 quotient 2 条带。"""
    quotient = row["phase_quotient"]
    factor = quotient // BASE_QUOTIENT
    n_value = row["q"] * row["a"]
    normalized_n = factor * n_value
    return {
        **row,
        "n_value": n_value,
        "normalization_factor": factor,
        "normalized_n": normalized_n,
    }


def positive_same_p_groups(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """构造同 p 的正 dyadic pair 短条带记录。"""
    positives = [
        normalized_source(row)
        for row in rows
        if row["target_cell_sign"] == "positive"
        and row["phase_quotient"] % BASE_QUOTIENT == 0
    ]
    by_p: dict[int, list[dict[str, Any]]] = {}
    for row in positives:
        by_p.setdefault(row["p"], []).append(row)

    groups = []
    for p_value, group_rows in sorted(by_p.items()):
        group_rows.sort(key=lambda row: row["phase_quotient"])
        if len(group_rows) < 2:
            continue
        phase_modulus = group_rows[0]["b"] // group_rows[0]["phase_quotient"]
        base_modulus = phase_modulus * BASE_QUOTIENT
        slot_min = floor_div(p_value * p_value, base_modulus) + 1
        slot_max = floor_div(p_value * p_value + p_value - 1, base_modulus)
        slot_capacity = max(0, slot_max - slot_min + 1)
        normalized_values = [row["normalized_n"] for row in group_rows]
        min_normalized = min(normalized_values)
        max_normalized = max(normalized_values)
        normalized_span = max_normalized - min_normalized
        delta_by_quotient = {
            row["phase_quotient"]: base_modulus * row["normalized_n"] - p_value * p_value
            for row in group_rows
        }
        quotient_to_row = {row["phase_quotient"]: row for row in group_rows}
        q2 = quotient_to_row.get(2)
        q4 = quotient_to_row.get(4)
        carry_equation = None
        if q2 is not None and q4 is not None:
            carry_equation = q2["q"] * q2["a"] - 2 * q4["q"] * q4["a"]
        groups.append(
            {
                "p": p_value,
                "phase_modulus": phase_modulus,
                "base_quotient": BASE_QUOTIENT,
                "base_modulus": base_modulus,
                "slot_min": slot_min,
                "slot_max": slot_max,
                "slot_capacity": slot_capacity,
                "source_rows": group_rows,
                "normalized_values": normalized_values,
                "min_normalized": min_normalized,
                "max_normalized": max_normalized,
                "normalized_span": normalized_span,
                "span_equals_capacity_minus_one": normalized_span == slot_capacity - 1,
                "occupies_both_strip_endpoints": (
                    min_normalized == slot_min and max_normalized == slot_max
                ),
                "delta_by_quotient": delta_by_quotient,
                "delta_relation_closed": (
                    q2 is not None
                    and q4 is not None
                    and delta_by_quotient[2] - delta_by_quotient[4]
                    == base_modulus * carry_equation
                ),
                "semiprime_carry_equation_value": carry_equation,
                "semiprime_carry_equation": (
                    None
                    if q2 is None or q4 is None
                    else f"{q2['q']}*{q2['a']} - 2*{q4['q']}*{q4['a']} = {carry_equation}"
                ),
                "strip_membership_closed": all(
                    slot_min <= row["normalized_n"] <= slot_max for row in group_rows
                ),
                "all_source_rows_prime_a": all(row["prime_a"] for row in group_rows),
                "same_p_strip_carry_closed_for_group": (
                    slot_capacity > 0
                    and all(slot_min <= row["normalized_n"] <= slot_max for row in group_rows)
                    and min_normalized == slot_min
                    and max_normalized == slot_max
                    and normalized_span == slot_capacity - 1
                    and carry_equation == normalized_span
                ),
            }
        )
    return groups


def audit() -> dict[str, Any]:
    """执行同 p 短条带 carry 审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    groups = positive_same_p_groups(source["source_rows"])
    all_groups_closed = bool(groups) and all(
        group["same_p_strip_carry_closed_for_group"] for group in groups
    )
    all_endpoint_spanning = bool(groups) and all(
        group["occupies_both_strip_endpoints"] for group in groups
    )
    max_slot_capacity = max((group["slot_capacity"] for group in groups), default=0)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_dyadic_same_p_strip_carry_router",
        "status": "z61_positive_dyadic_lifts_reduced_to_endpoint_spanning_same_p_strip_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "positive_same_p_group_count": len(groups),
        "max_slot_capacity": max_slot_capacity,
        "all_positive_same_p_groups_closed": all_groups_closed,
        "all_positive_same_p_groups_endpoint_spanning": all_endpoint_spanning,
        "same_p_strip_groups": groups,
        "endpoint_spanning_semiprime_pair_bound_proved": False,
        "endpoint_pair_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "两个正 dyadic lift 共用同一个 `p` 后，可归一到同一个 quotient-2 短条带。"
            "在样本中该条带只有 `4` 个整数槽，`2q_4a_4` 占最低槽，"
            "`q_2a_2` 占最高槽；等价半素数 carry 方程为 "
            "`71*9767 - 2*37*9371 = 3`。"
            "因此 dyadic 正吸收器进一步压成端点跨越的短条带半素数对问题，"
            "下一步证明这种 endpoint-spanning pair 的全局容量界，"
            "或登记 EndpointPair-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 dyadic same-p strip carry",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"positive_same_p_group_count={result['positive_same_p_group_count']}",
        f"max_slot_capacity={result['max_slot_capacity']}",
        f"all_positive_same_p_groups_closed={fmt_bool(result['all_positive_same_p_groups_closed'])}",
        f"all_positive_same_p_groups_endpoint_spanning={fmt_bool(result['all_positive_same_p_groups_endpoint_spanning'])}",
        f"endpoint_spanning_semiprime_pair_bound_proved={fmt_bool(result['endpoint_spanning_semiprime_pair_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同 p 短条带",
        "",
        "| p | B | base modulus | slots | capacity | normalized values | span | carry equation | endpoints |",
        "| ---: | ---: | ---: | --- | ---: | --- | ---: | --- | --- |",
    ]
    for group in result["same_p_strip_groups"]:
        lines.append(
            f"| {group['p']} | {group['phase_modulus']} | {group['base_modulus']} | "
            f"`[{group['slot_min']},{group['slot_max']}]` | {group['slot_capacity']} | "
            f"`{group['normalized_values']}` | {group['normalized_span']} | "
            f"`{group['semiprime_carry_equation']}` | "
            f"{fmt_bool(group['occupies_both_strip_endpoints'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 源纤维归一化",
            "",
            "| quotient | q | a | n=qa | normalized n | delta |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for group in result["same_p_strip_groups"]:
        for row in group["source_rows"]:
            lines.append(
                f"| {row['phase_quotient']} | {row['q']} | {row['a']} | "
                f"{row['n_value']} | {row['normalized_n']} | "
                f"{group['delta_by_quotient'][row['phase_quotient']]} |"
            )
    lines.extend(
        [
            "",
            "## 3. 自足小引理",
            "",
            "设同一 `p,B` 下有 quotient `2` 与 `4` 两条短残基源纤维。"
            "令 `n_2=q_2a_2`，`n_4=q_4a_4`。二者归一到同一条带：",
            "",
            "```text",
            "p^2 < 2B*n_2 <= p^2+p-1,",
            "p^2 < 2B*(2n_4) <= p^2+p-1.",
            "```",
            "",
            "因此 `n_2` 与 `2n_4` 必须落在同一个长度约 `p/(2B)` 的整数槽集合中。"
            "样本里该集合只有 4 个槽，二者占据两端，所以正吸收器的存在等价于一个端点跨越半素数对。",
            "",
            "## 4. 证明边界",
            "",
            "- 已闭合：样本内正 dyadic lift 对被压成同 p 短条带端点跨越半素数 carry 方程。",
            "- 未闭合：全局端点跨越半素数对容量界，或 EndpointPair-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
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
                "all_positive_same_p_groups_closed": result["all_positive_same_p_groups_closed"],
                "max_slot_capacity": result["max_slot_capacity"],
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
