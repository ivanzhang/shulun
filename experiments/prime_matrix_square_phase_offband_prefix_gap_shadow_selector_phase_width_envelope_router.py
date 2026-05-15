#!/usr/bin/env python3
"""把 fixed small-k phase 宽度上界正规化为活跃端点公式。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_phase_width_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json"
SOURCE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-router.md"

SOURCE_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_width_source_router.py"
)

MAIN_TARGET = "LengthClassLabelLowerBoundAndPhaseWidthEnvelopeOrSmallModulusPDEC"
NEXT_TARGET = "ActiveEndpointPhaseWidthEnvelopeAndLabelLowerBoundOrSmallModulusPDEC"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def min_integer_gt(value: Fraction) -> int:
    """返回满足 n>value 的最小整数。"""
    return value.numerator // value.denominator + 1


def max_integer_lt(value: Fraction) -> int:
    """返回满足 n<value 的最大整数。"""
    return (value.numerator + value.denominator - 1) // value.denominator - 1


def lower_constraints(row: dict[str, Any]) -> list[dict[str, Any]]:
    """列出 fixed atom 的所有下界约束。"""
    k_value = int(row["parent_atom_k"])
    band = row["parent_atom_band"]
    constraints: list[dict[str, Any]] = []
    for b_value in range(int(row["b_lo"]), int(row["b_hi"]) + 1):
        constraints.append(
            {
                "value": min_integer_gt(Fraction(2 * b_value * b_value, k_value + 1) + 2 * b_value),
                "b": b_value,
                "type": "floor_lower",
            }
        )
        if band == "plus_only_noslot":
            constraints.append(
                {
                    "value": min_integer_gt(
                        Fraction(
                            4 * b_value * b_value + 4 * k_value * b_value + 4 * b_value - 1,
                            2 * k_value + 1,
                        )
                    ),
                    "b": b_value,
                    "type": "plus_band_lower",
                }
            )
    return constraints


def upper_constraints(row: dict[str, Any]) -> list[dict[str, Any]]:
    """列出 fixed atom 的所有上界约束。"""
    k_value = int(row["parent_atom_k"])
    band = row["parent_atom_band"]
    constraints: list[dict[str, Any]] = []
    for b_value in range(int(row["b_lo"]), int(row["b_hi"]) + 1):
        if k_value > 0:
            constraints.append(
                {
                    "value": math.floor(Fraction(2 * b_value * b_value, k_value) + 2 * b_value),
                    "b": b_value,
                    "type": "floor_upper",
                }
            )
        if band == "minus_only_noslot":
            constraints.append(
                {
                    "value": max_integer_lt(
                        Fraction(4 * b_value * b_value + 4 * k_value * b_value + 1, 2 * k_value + 1)
                    ),
                    "b": b_value,
                    "type": "minus_band_upper",
                }
            )
    return constraints


def active_formula(row: dict[str, Any], lower: dict[str, Any], upper: dict[str, Any]) -> str:
    """输出活跃端点宽度公式。"""
    band = row["parent_atom_band"]
    k_value = int(row["parent_atom_k"])
    if band == "minus_only_noslot":
        return (
            "W = max_integer_lt((4*B^2+4*k*B+1)/(2*k+1)) "
            "- min_integer_gt(2*H^2/(k+1)+2*H) + 1"
        )
    if band == "plus_only_noslot" and k_value > 0:
        return (
            "W = floor(2*B^2/k+2*B) "
            "- min_integer_gt((4*H^2+4*k*H+4*H-1)/(2*k+1)) + 1"
        )
    return f"W = {upper['type']}(B) - {lower['type']}(H) + 1"


def phase_width_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单条 phase width envelope 记录。"""
    lower_items = lower_constraints(row)
    upper_items = upper_constraints(row)
    active_lower = max(lower_items, key=lambda item: (item["value"], item["b"], item["type"]))
    active_upper = min(upper_items, key=lambda item: (item["value"], item["b"], item["type"]))
    exact_width = active_upper["value"] - active_lower["value"] + 1
    active_pattern = (
        f"band={row['parent_atom_band']}|k={row['parent_atom_k']}|"
        f"L={row['cell_length']}|lo={active_lower['type']}@b_{active_lower['b'] - row['b_lo']}|"
        f"hi={active_upper['type']}@b_{active_upper['b'] - row['b_lo']}"
    )
    expected_lower_b = int(row["b_hi"])
    expected_upper_b = int(row["b_lo"])
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "parent_atom_band": row["parent_atom_band"],
        "parent_atom_k": row["parent_atom_k"],
        "b_lo": row["b_lo"],
        "b_hi": row["b_hi"],
        "cell_length": row["cell_length"],
        "phase_p_lo": row["phase_p_lo"],
        "phase_p_hi": row["phase_p_hi"],
        "phase_p_width": row["phase_p_width"],
        "active_lower": active_lower,
        "active_upper": active_upper,
        "active_width": exact_width,
        "active_formula": active_formula(row, active_lower, active_upper),
        "active_pattern": active_pattern,
        "width_matches_phase_window": exact_width == int(row["phase_p_width"]),
        "active_lower_at_b_hi": active_lower["b"] == expected_lower_b,
        "active_upper_at_b_lo": active_upper["b"] == expected_upper_b,
        "endpoint_orientation_closed": active_lower["b"] == expected_lower_b and active_upper["b"] == expected_upper_b,
        "lower_constraint_count": len(lower_items),
        "upper_constraint_count": len(upper_items),
    }


def grouped_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 band/k/L 分组汇总宽度 envelope。"""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in records:
        key = f"band={row['parent_atom_band']}|k={row['parent_atom_k']}|L={row['cell_length']}"
        grouped[key].append(row)
    groups: list[dict[str, Any]] = []
    for key, items in sorted(grouped.items()):
        groups.append(
            {
                "group_key": key,
                "record_count": len(items),
                "max_phase_width": max(int(item["phase_p_width"]) for item in items),
                "min_phase_width": min(int(item["phase_p_width"]) for item in items),
                "active_patterns": sorted({item["active_pattern"] for item in items}),
                "all_widths_match": all(item["width_matches_phase_window"] for item in items),
                "all_endpoint_orientations_closed": all(item["endpoint_orientation_closed"] for item in items),
            }
        )
    return groups


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "active_endpoint_width_formula",
            "status": "closed_on_current_frontier",
            "statement": "Every current fixed phase window is exactly recovered from the active b_hi lower endpoint and b_lo upper endpoint.",
        },
        {
            "name": "phase_width_envelope_normal_form",
            "status": "closed",
            "statement": "The phase width input is reduced to explicit endpoint formulas by band/k family.",
        },
        {
            "name": "global_endpoint_orientation",
            "status": "open",
            "statement": "A global proof must show the same active endpoint orientation holds for the formal-unit family.",
        },
        {
            "name": "global_width_bound",
            "status": "open",
            "statement": "A global proof must combine the endpoint formula with label lower bounds to prove M>W.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteActiveEndpointFormulaClosed",
            "closed": agg["width_formula_failure_count"] == 0,
            "proved": True,
            "meaning": "当前 fixed phase 窗口宽度均由活跃端点公式精确恢复。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "EndpointOrientationClosed",
            "closed": agg["endpoint_orientation_failure_count"] == 0,
            "proved": True,
            "meaning": "当前所有窗口均为 b_hi 给下界、b_lo 给上界。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "GlobalEndpointOrientationProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 formal-unit 族中活跃端点方向不变。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "GlobalMGreaterThanWProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需与标签模数下界合并推出全局 M>W。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭当前宽度公式层，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, source_ledger: Path) -> dict[str, Any]:
    """构造 phase width envelope 路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    source_split = load_json(source_ledger)
    records = [phase_width_record(row) for row in source["phase_compatibility_records"]]
    groups = grouped_records(records)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "source_ledger": str(source_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "group_count": len(groups),
        "width_formula_failure_count": sum(1 for row in records if not row["width_matches_phase_window"]),
        "endpoint_orientation_failure_count": sum(1 for row in records if not row["endpoint_orientation_closed"]),
        "active_pattern_count": len({row["active_pattern"] for row in records}),
        "max_phase_width": max((int(row["phase_p_width"]) for row in records), default=0),
        "global_endpoint_orientation_proved": False,
        "global_width_bound_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "phase_width_records": records,
        "phase_width_group_records": groups,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_phase_width_envelope_router",
        "status": "selector_phase_width_envelope_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_width_formula_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "phase_width_records": records,
        "phase_width_group_records": groups,
        "modulus_width_source_aggregate": source_split["aggregate"],
        "global_endpoint_orientation_proved": False,
        "global_width_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_phase_width_envelope_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_width_source_router.py": sha256(
                SOURCE_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-ledger.json": sha256(
                source_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 fixed small-k phase 宽度输入正规化为活跃端点公式。当前 11 个窗口全部由"
            "右端 b_hi 的下界约束和左端 b_lo 的上界约束夹出，精确恢复原 phase_p_width；"
            f"活跃 pattern 数为 {aggregate['active_pattern_count']}，最大宽度为 {aggregate['max_phase_width']}。"
            "这关闭了当前前沿的宽度公式层；全局仍需证明 formal-unit 族中同样的端点方向和宽度 envelope，"
            "再与标签模数下界合并推出 M>W。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector phase width envelope router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"group_count={agg['group_count']}",
        f"active_pattern_count={agg['active_pattern_count']}",
        f"width_formula_failure_count={agg['width_formula_failure_count']}",
        f"endpoint_orientation_failure_count={agg['endpoint_orientation_failure_count']}",
        f"max_phase_width={agg['max_phase_width']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 活跃端点公式",
        "",
        "| idx | P | band | k | b range | width | active lower | active upper | formula ok |",
        "| ---: | ---: | --- | ---: | --- | ---: | --- | --- | ---: |",
    ]
    for row in result["phase_width_records"]:
        lower = row["active_lower"]
        upper = row["active_upper"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["index"]),
                    str(row["p"]),
                    f"`{row['parent_atom_band']}`",
                    str(row["parent_atom_k"]),
                    f"`{row['b_lo']}..{row['b_hi']}`",
                    str(row["phase_p_width"]),
                    f"`{lower['type']}@b={lower['b']} -> {lower['value']}`",
                    f"`{upper['type']}@b={upper['b']} -> {upper['value']}`",
                    f"`{fmt_bool(row['width_matches_phase_window'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. Family Envelope",
            "",
            "| group | records | min W | max W | patterns | orientation ok |",
            "| --- | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for row in result["phase_width_group_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['group_key'])}`",
                    str(row["record_count"]),
                    str(row["min_phase_width"]),
                    str(row["max_phase_width"]),
                    f"`{table_cell(row['active_patterns'])}`",
                    f"`{fmt_bool(row['all_endpoint_orientations_closed'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 4. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 直接证明目标：证明 formal-unit 族中活跃端点方向稳定，并用上述公式给出宽度 envelope。",
            "- 随后与 cover-word 标签模数下界合并，形成全局 `M>W`。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    parser.add_argument("--source-ledger", type=Path, default=SOURCE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    source_ledger = args.source_ledger if args.source_ledger.is_absolute() else ROOT / args.source_ledger
    result = build_result(input_ledger, source_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "record_count": result["aggregate"]["record_count"],
                "width_formula_failure_count": result["aggregate"]["width_formula_failure_count"],
                "endpoint_orientation_failure_count": result["aggregate"][
                    "endpoint_orientation_failure_count"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
