#!/usr/bin/env python3
"""把一跳模数屏障拆成长度类模数下界与相位宽度上界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_width_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-router.md"

MODULUS_BARRIER_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_barrier_router.py"
)

MAIN_TARGET = "CoverWordModulusDominatesPhaseWidthOrSmallModulusOverlapPDEC"
NEXT_TARGET = "LengthClassLabelLowerBoundAndPhaseWidthEnvelopeOrSmallModulusPDEC"


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


def all_atoms(source: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取全部屏障原子。"""
    return [
        atom
        for row in source["selector_modulus_barrier_records"]
        for atom in row["barrier_atoms"]
    ]


def length_class_records(atoms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按覆盖词标签长度汇总模数下界与宽度上界。"""
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for atom in atoms:
        grouped[len(atom["labels"])].append(atom)
    records: list[dict[str, Any]] = []
    for length, items in sorted(grouped.items()):
        min_modulus = min(int(atom["word_modulus"]) for atom in items)
        max_width = max(int(atom["phase_p_width"]) for atom in items)
        min_atom_margin = min(int(atom["modulus_minus_width"]) for atom in items)
        records.append(
            {
                "label_word_length": length,
                "atom_count": len(items),
                "min_word_modulus": min_modulus,
                "max_phase_width": max_width,
                "class_margin_minM_minus_maxW": min_modulus - max_width,
                "min_atom_modulus_minus_width": min_atom_margin,
                "dominance_closed_on_frontier": min_modulus > max_width,
                "min_modulus_examples": [
                    {
                        "p": atom["p"],
                        "side": atom["side"],
                        "labels": atom["labels"],
                        "word_modulus": atom["word_modulus"],
                        "phase_p_width": atom["phase_p_width"],
                    }
                    for atom in sorted(items, key=lambda item: item["word_modulus"])[:4]
                ],
                "max_width_examples": [
                    {
                        "p": atom["p"],
                        "side": atom["side"],
                        "labels": atom["labels"],
                        "word_modulus": atom["word_modulus"],
                        "phase_p_width": atom["phase_p_width"],
                    }
                    for atom in sorted(items, key=lambda item: item["phase_p_width"], reverse=True)[:4]
                ],
            }
        )
    return records


def family_class_records(atoms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按父 atom family 汇总局部屏障余量。"""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for atom in atoms:
        grouped[f"{atom['side']}|{atom['parent_atom_key']}|L={len(atom['labels'])}"].append(atom)
    records: list[dict[str, Any]] = []
    for family_key, items in sorted(grouped.items()):
        records.append(
            {
                "family_key": family_key,
                "atom_count": len(items),
                "min_word_modulus": min(int(atom["word_modulus"]) for atom in items),
                "max_phase_width": max(int(atom["phase_p_width"]) for atom in items),
                "min_modulus_minus_width": min(int(atom["modulus_minus_width"]) for atom in items),
                "min_modulus_to_width_ratio": min(float(atom["modulus_to_width_ratio"]) for atom in items),
                "dominance_closed_on_frontier": all(atom["one_step_barrier_closed"] for atom in items),
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_length_class_modulus_width_dominance",
            "status": "closed_on_current_frontier",
            "statement": "For each observed label-word length, the minimum word modulus exceeds the maximum phase width.",
        },
        {
            "name": "modulus_width_source_split",
            "status": "closed",
            "statement": "The M>W barrier splits into a label lower bound and a fixed phase-width envelope.",
        },
        {
            "name": "global_label_lower_bound",
            "status": "open",
            "statement": "A global proof must lower-bound non-structural cover-word moduli by length/family.",
        },
        {
            "name": "global_phase_width_envelope",
            "status": "open",
            "statement": "A global proof must upper-bound fixed small-k phase window widths by the same length/family classes.",
        },
        {
            "name": "small_modulus_overlap_pdec",
            "status": "open",
            "statement": "If either bound fails, the remaining object is a concrete small-modulus overlap PDEC/ColumnCRT certificate.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteLengthClassDominanceClosed",
            "closed": agg["length_class_dominance_failure_count"] == 0,
            "proved": True,
            "meaning": "当前每个长度类都满足 min(M)>max(W)。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "SourceSplitClosed",
            "closed": True,
            "proved": True,
            "meaning": "M>W 已拆为标签乘积下界与 phase 宽度上界两个输入。",
            "remaining": "closed",
        },
        {
            "gate": "GlobalLabelLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 formal-unit 族中的非结构冲突词模数下界。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "GlobalPhaseWidthEnvelopeProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 formal-unit 族中的 fixed phase 宽度上界。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步继续压缩证明义务，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造模数-宽度来源拆分结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    atoms = all_atoms(source)
    length_records = length_class_records(atoms)
    family_records = family_class_records(atoms)
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "barrier_atom_count": len(atoms),
        "length_class_count": len(length_records),
        "family_class_count": len(family_records),
        "length_class_dominance_failure_count": sum(
            1 for row in length_records if not row["dominance_closed_on_frontier"]
        ),
        "min_length_class_margin": min(
            (row["class_margin_minM_minus_maxW"] for row in length_records),
            default=None,
        ),
        "min_atom_modulus_minus_width": source["aggregate"]["min_modulus_minus_width"],
        "global_label_lower_bound_proved": False,
        "global_phase_width_envelope_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "length_class_records": length_records,
        "family_class_records": family_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_width_source_router",
        "status": "selector_modulus_width_source_split_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_length_class_dominance_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "length_class_records": length_records,
        "family_class_records": family_records,
        "modulus_barrier_aggregate": source["aggregate"],
        "global_label_lower_bound_proved": False,
        "global_phase_width_envelope_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_width_source_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_barrier_router.py": sha256(
                MODULUS_BARRIER_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把一跳模数屏障 M>W 的来源拆成两个可攻输入：cover-word 标签乘积/CRT 模数下界，"
            "以及 fixed small-k phase 窗口宽度上界。当前前沿按标签词长度分为 "
            f"{len(length_records)} 类，全部满足 min(M)>max(W)，最小长度类余量为 "
            f"{aggregate['min_length_class_margin']}。这不是全局证明；全局剩余是证明同一 formal-unit "
            "族的标签下界与宽度 envelope，或将 M<=W 的小模数重叠登记为 PDEC/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector modulus-width source router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"barrier_atom_count={agg['barrier_atom_count']}",
        f"length_class_count={agg['length_class_count']}",
        f"family_class_count={agg['family_class_count']}",
        f"length_class_dominance_failure_count={agg['length_class_dominance_failure_count']}",
        f"min_length_class_margin={agg['min_length_class_margin']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 长度类屏障",
        "",
        "| L | atoms | min M | max W | minM-maxW | min atom M-W | closed |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["length_class_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["label_word_length"]),
                    str(row["atom_count"]),
                    str(row["min_word_modulus"]),
                    str(row["max_phase_width"]),
                    str(row["class_margin_minM_minus_maxW"]),
                    str(row["min_atom_modulus_minus_width"]),
                    f"`{fmt_bool(row['dominance_closed_on_frontier'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. Family 屏障",
            "",
            "| family | atoms | min M | max W | min M-W | min M/W | closed |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["family_class_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['family_key'])}`",
                    str(row["atom_count"]),
                    str(row["min_word_modulus"]),
                    str(row["max_phase_width"]),
                    str(row["min_modulus_minus_width"]),
                    f"{row['min_modulus_to_width_ratio']:.6f}",
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
            "- 直接证明目标 A：非结构冲突 cover words 的标签乘积给出长度/族下界。",
            "- 直接证明目标 B：fixed small-k phase 窗口宽度受同一长度/族 envelope 控制。",
            "- 若 A 或 B 失败，则失败对象就是 small-modulus overlap `PDEC/ColumnCRT`。",
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
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-width-source-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "length_class_count": result["aggregate"]["length_class_count"],
                "length_class_dominance_failure_count": result["aggregate"][
                    "length_class_dominance_failure_count"
                ],
                "min_length_class_margin": result["aggregate"]["min_length_class_margin"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
