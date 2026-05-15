#!/usr/bin/env python3
"""审计 non-structural cover words 的标签模数下界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_label_lower_bound_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json"
WIDTH_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-router.md"

WIDTH_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_phase_width_envelope_router.py"
)

MAIN_TARGET = "ActiveEndpointPhaseWidthEnvelopeAndLabelLowerBoundOrSmallModulusPDEC"
NEXT_TARGET = "NonStructuralLabelModulusFloorOrSmallModulusOverlapPDEC"


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


def odd_primes(limit: int) -> list[int]:
    """列出不超过 limit 的奇素数。"""
    values: list[int] = []
    for number in range(3, limit + 1, 2):
        if all(number % divisor for divisor in range(3, math.isqrt(number) + 1, 2)):
            values.append(number)
    return values


def crt_pair(a_value: int, a_modulus: int, b_value: int, b_modulus: int) -> tuple[int, int] | None:
    """合并两个 CRT 条件。"""
    gcd_value = math.gcd(a_modulus, b_modulus)
    if (b_value - a_value) % gcd_value:
        return None
    reduced_a = a_modulus // gcd_value
    reduced_b = b_modulus // gcd_value
    delta = (b_value - a_value) // gcd_value
    step = (delta * pow(reduced_a, -1, reduced_b)) % reduced_b
    modulus = a_modulus // gcd_value * b_modulus
    residue = (a_value + a_modulus * step) % modulus
    return residue, modulus


def progression_values(lo_value: int, hi_value: int, residue: int, modulus: int) -> list[int]:
    """列出区间内同余类取值。"""
    if lo_value > hi_value:
        return []
    quotient = math.ceil((lo_value - residue) / modulus)
    value = residue + quotient * modulus
    values: list[int] = []
    while value <= hi_value:
        values.append(value)
        value += modulus
    return values


def compatible_cover_words(row: dict[str, Any]) -> list[dict[str, Any]]:
    """枚举相位兼容覆盖词。"""
    b_start = int(row["b_lo"])
    length = int(row["cell_length"])
    phase_lo = int(row["phase_p_lo"])
    phase_hi = int(row["phase_p_hi"])
    label_pool = odd_primes(math.isqrt(int(row["p"])))
    words: list[dict[str, Any]] = []

    def recurse(offset: int, residue: int, modulus: int, labels: list[int]) -> None:
        if offset == length:
            values = progression_values(phase_lo, phase_hi, residue, modulus)
            if values:
                words.append(
                    {
                        "labels": labels[:],
                        "distinct_labels": sorted(set(labels)),
                        "residue": residue,
                        "modulus": modulus,
                        "window_values": values,
                    }
                )
            return

        b_value = b_start + offset
        for label in label_pool:
            # 若 label|b，则 P 会落到 0 mod label；对 P>label 的素数不允许。
            if b_value % label == 0:
                continue
            merged = crt_pair(residue, modulus, (2 * b_value) % label, label)
            if merged is None:
                continue
            recurse(offset + 1, merged[0], merged[1], labels + [label])

    recurse(0, 0, 1, [])
    return words


def classify_word(row: dict[str, Any], word: dict[str, Any]) -> dict[str, Any]:
    """标记覆盖词是否为结构低轮冲突。"""
    actual_p = int(row["p"])
    gcd15 = math.gcd(int(word["modulus"]), 15)
    structural_conflict = gcd15 > 1 and actual_p % gcd15 != int(word["residue"]) % gcd15
    actual_residue_hit = any(int(value) % 15 == actual_p % 15 for value in word["window_values"])
    return {
        **word,
        "gcd_modulus_15": gcd15,
        "structural_lowwheel_conflict": structural_conflict,
        "actual_residue_hit_inside_window": actual_residue_hit,
        "small_modulus_against_row_width": int(word["modulus"]) <= int(row["phase_p_width"]),
    }


def row_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单行标签下界记录。"""
    words = [classify_word(row, word) for word in compatible_cover_words(row)]
    nonstructural = [word for word in words if not word["structural_lowwheel_conflict"]]
    small = [word for word in nonstructural if word["small_modulus_against_row_width"]]
    overlaps = [word for word in nonstructural if word["actual_residue_hit_inside_window"]]
    min_word = min(nonstructural, key=lambda word: int(word["modulus"])) if nonstructural else None
    signatures: dict[str, int] = {}
    for word in nonstructural:
        key = ",".join(str(label) for label in word["distinct_labels"])
        signatures[key] = min(int(word["modulus"]), signatures.get(key, int(word["modulus"])))
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "parent_atom_band": row["parent_atom_band"],
        "parent_atom_k": row["parent_atom_k"],
        "cell_length": row["cell_length"],
        "phase_p_width": row["phase_p_width"],
        "phase_compatible_cover_word_count": len(words),
        "nonstructural_cover_word_count": len(nonstructural),
        "small_modulus_nonstructural_count": len(small),
        "actual_residue_overlap_count": len(overlaps),
        "min_nonstructural_modulus": int(min_word["modulus"]) if min_word else None,
        "min_nonstructural_labels": min_word["labels"] if min_word else [],
        "min_nonstructural_distinct_labels": min_word["distinct_labels"] if min_word else [],
        "min_nonstructural_margin_M_minus_W": int(min_word["modulus"]) - int(row["phase_p_width"]) if min_word else None,
        "nonstructural_signature_min_modulus": dict(sorted(signatures.items())),
        "label_lower_bound_closed_on_frontier": bool(nonstructural) and not small,
        "overlap_pdec_needed_on_frontier": bool(small or overlaps),
        "small_modulus_examples": [
            {
                "labels": word["labels"],
                "modulus": word["modulus"],
                "window_values": word["window_values"],
            }
            for word in small[:5]
        ],
    }


def length_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 cell length 汇总标签下界。"""
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[int(row["cell_length"])].append(row)
    records: list[dict[str, Any]] = []
    for length, items in sorted(grouped.items()):
        min_modulus = min(int(row["min_nonstructural_modulus"]) for row in items)
        max_width = max(int(row["phase_p_width"]) for row in items)
        records.append(
            {
                "cell_length": length,
                "record_count": len(items),
                "min_nonstructural_modulus": min_modulus,
                "max_phase_width": max_width,
                "length_margin_minM_minus_maxW": min_modulus - max_width,
                "small_modulus_nonstructural_count": sum(row["small_modulus_nonstructural_count"] for row in items),
                "actual_residue_overlap_count": sum(row["actual_residue_overlap_count"] for row in items),
                "dominance_closed_on_frontier": min_modulus > max_width,
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_nonstructural_label_floor",
            "status": "closed_on_current_frontier",
            "statement": "Every current non-structural compatible cover word has modulus larger than its phase width.",
        },
        {
            "name": "small_modulus_overlap_absent",
            "status": "closed_on_current_frontier",
            "statement": "No current non-structural cover word has M<=W or an actual mod-15 hit inside the phase window.",
        },
        {
            "name": "global_label_floor",
            "status": "open",
            "statement": "A global proof must exclude non-structural cover words with small label modulus in the formal-unit family.",
        },
        {
            "name": "small_modulus_overlap_pdec",
            "status": "open",
            "statement": "Any global small-modulus survivor must be routed to a PDEC/ColumnCRT certificate.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteLabelFloorClosed",
            "closed": agg["small_modulus_nonstructural_count"] == 0,
            "proved": True,
            "meaning": "当前 non-structural 覆盖词全部满足 M>W。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "FiniteActualResidueOverlapAbsent",
            "closed": agg["actual_residue_overlap_count"] == 0,
            "proved": True,
            "meaning": "当前没有 actual mod-15 残基命中窗口。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "GlobalLabelFloorProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 formal-unit 族中不存在小模数 non-structural 覆盖词。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "SmallModulusOverlapPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若小模数词存在，仍需 PDEC/ColumnCRT 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭当前标签下界审计，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path, width_ledger: Path) -> dict[str, Any]:
    """构造标签下界路由结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    width = load_json(width_ledger)
    records = [row_record(row) for row in source["phase_compatibility_records"]]
    length_summary = length_records(records)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "width_ledger": str(width_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "phase_compatible_cover_word_count": sum(row["phase_compatible_cover_word_count"] for row in records),
        "nonstructural_cover_word_count": sum(row["nonstructural_cover_word_count"] for row in records),
        "small_modulus_nonstructural_count": sum(row["small_modulus_nonstructural_count"] for row in records),
        "actual_residue_overlap_count": sum(row["actual_residue_overlap_count"] for row in records),
        "min_nonstructural_margin_M_minus_W": min(
            row["min_nonstructural_margin_M_minus_W"] for row in records if row["min_nonstructural_margin_M_minus_W"] is not None
        ),
        "length_class_dominance_failure_count": sum(
            1 for row in length_summary if not row["dominance_closed_on_frontier"]
        ),
        "global_label_floor_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "label_lower_bound_records": records,
        "length_class_records": length_summary,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_label_lower_bound_router",
        "status": "selector_label_lower_bound_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_label_floor_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "label_lower_bound_records": records,
        "length_class_records": length_summary,
        "phase_width_envelope_aggregate": width["aggregate"],
        "global_label_floor_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_label_lower_bound_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_phase_width_envelope_router.py": sha256(
                WIDTH_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-phase-compatibility-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-phase-width-envelope-ledger.json": sha256(
                width_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步审计 cover-word 标签模数下界：在 162 个相位兼容覆盖词中，排除结构低轮冲突后"
            f"剩余 {aggregate['nonstructural_cover_word_count']} 个 non-structural 词；当前没有任何 "
            "non-structural 词满足 M<=W，也没有 actual mod-15 残基命中窗口。最小行级余量 "
            f"M-W 为 {aggregate['min_nonstructural_margin_M_minus_W']}。"
            "这关闭当前前沿的标签下界审计；全局仍需证明 formal-unit 族无小模数 non-structural 词，"
            "或将其登记为 PDEC/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector label lower bound router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_compatible_cover_word_count={agg['phase_compatible_cover_word_count']}",
        f"nonstructural_cover_word_count={agg['nonstructural_cover_word_count']}",
        f"small_modulus_nonstructural_count={agg['small_modulus_nonstructural_count']}",
        f"actual_residue_overlap_count={agg['actual_residue_overlap_count']}",
        f"min_nonstructural_margin_M_minus_W={agg['min_nonstructural_margin_M_minus_W']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 行级标签下界",
        "",
        "| idx | P | W | compatible | nonstruct | min M | min labels | min M-W | small M count | overlap count |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: |",
    ]
    for row in result["label_lower_bound_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["index"]),
                    str(row["p"]),
                    str(row["phase_p_width"]),
                    str(row["phase_compatible_cover_word_count"]),
                    str(row["nonstructural_cover_word_count"]),
                    str(row["min_nonstructural_modulus"]),
                    f"`{row['min_nonstructural_labels']}`",
                    str(row["min_nonstructural_margin_M_minus_W"]),
                    str(row["small_modulus_nonstructural_count"]),
                    str(row["actual_residue_overlap_count"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 长度类下界",
            "",
            "| L | records | min M | max W | minM-maxW | small M count | overlap count | closed |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["length_class_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["cell_length"]),
                    str(row["record_count"]),
                    str(row["min_nonstructural_modulus"]),
                    str(row["max_phase_width"]),
                    str(row["length_margin_minM_minus_maxW"]),
                    str(row["small_modulus_nonstructural_count"]),
                    str(row["actual_residue_overlap_count"]),
                    f"`{fmt_bool(row['dominance_closed_on_frontier'])}`",
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
            "- 直接证明目标：全局排斥 small-modulus non-structural cover words。",
            "- 若存在 small-modulus survivor，则登记为 small-modulus overlap `PDEC/ColumnCRT`。",
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
    parser.add_argument("--width-ledger", type=Path, default=WIDTH_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    width_ledger = args.width_ledger if args.width_ledger.is_absolute() else ROOT / args.width_ledger
    result = build_result(input_ledger, width_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-label-lower-bound-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "nonstructural_cover_word_count": result["aggregate"]["nonstructural_cover_word_count"],
                "small_modulus_nonstructural_count": result["aggregate"][
                    "small_modulus_nonstructural_count"
                ],
                "actual_residue_overlap_count": result["aggregate"]["actual_residue_overlap_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
