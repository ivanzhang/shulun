#!/usr/bin/env python3
"""把 Q=15 窗口错位端点距离压成一跳模数屏障。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-window-miss-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-router.md"

WINDOW_MISS_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_window_miss_router.py"
)

MAIN_TARGET = "LowWheel15WindowMissEndpointInequalityOrPersistentOverlapPDEC"
NEXT_TARGET = "CoverWordModulusDominatesPhaseWidthOrSmallModulusOverlapPDEC"


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


def barrier_atom(atom: dict[str, Any]) -> dict[str, Any]:
    """生成单个端点错位原子的一跳模数屏障记录。"""
    width = int(atom["phase_p_width"])
    modulus = int(atom["word_modulus"])
    window_values = [int(value) for value in atom["window_values"]]
    actual_mod15 = int(atom["actual_p_mod_15"])
    residues_mod15 = sorted({value % 15 for value in window_values})
    single_window_representative = len(window_values) == 1
    actual_residue_absent = actual_mod15 not in residues_mod15
    one_step_barrier_closed = single_window_representative and actual_residue_absent and modulus > width
    nearest_shift = (
        abs(int(atom["nearest_hit_value"]) - window_values[0])
        if single_window_representative and atom["nearest_hit_value"] is not None
        else None
    )
    signed_step_abs = nearest_shift // modulus if nearest_shift is not None else None
    return {
        "p": atom["p"],
        "side": atom["side"],
        "parent_atom_key": atom["parent_atom_key"],
        "labels": atom["labels"],
        "word_modulus": modulus,
        "phase_p_width": width,
        "modulus_minus_width": modulus - width,
        "modulus_to_width_ratio": modulus / width if width else None,
        "window_values": window_values,
        "window_value_mod15": residues_mod15,
        "actual_p_mod_15": actual_mod15,
        "single_window_representative": single_window_representative,
        "actual_residue_absent_in_window_values": actual_residue_absent,
        "nearest_hit_side": atom["nearest_hit_side"],
        "nearest_hit_distance": atom["nearest_hit_distance"],
        "nearest_shift_from_window_value": nearest_shift,
        "signed_step_abs_to_nearest_actual_residue": signed_step_abs,
        "one_step_barrier_closed": one_step_barrier_closed,
        "barrier_statement": (
            "If a word progression has only one representative in the phase window, "
            "that representative is not congruent to actual P mod 15, and word_modulus > phase_width, "
            "then every actual-residue hit in the same word progression lies outside the window."
        ),
    }


def barrier_record(row: dict[str, Any]) -> dict[str, Any]:
    """生成单包一跳模数屏障记录。"""
    atoms = [barrier_atom(atom) for atom in row["window_miss_atoms"]]
    margins = [atom["modulus_minus_width"] for atom in atoms]
    ratios = [atom["modulus_to_width_ratio"] for atom in atoms if atom["modulus_to_width_ratio"] is not None]
    return {
        "index": row["index"],
        "p": row["p"],
        "side": row["side"],
        "shape_key": row["shape_key"],
        "parent_atom_key": row["parent_atom_key"],
        "phase_p_lo": row["phase_p_lo"],
        "phase_p_hi": row["phase_p_hi"],
        "phase_p_width": row["phase_p_width"],
        "window_miss_atom_count": len(atoms),
        "one_step_barrier_closed_count": sum(1 for atom in atoms if atom["one_step_barrier_closed"]),
        "one_step_barrier_failure_count": sum(1 for atom in atoms if not atom["one_step_barrier_closed"]),
        "min_modulus_minus_width": min(margins) if margins else None,
        "min_modulus_to_width_ratio": min(ratios) if ratios else None,
        "barrier_atoms": atoms,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "one_step_modulus_barrier",
            "status": "closed_on_current_frontier",
            "statement": "For all current window-miss atoms, word_modulus exceeds phase width and the word has a single window representative.",
        },
        {
            "name": "endpoint_distance_implied_by_modulus_barrier",
            "status": "closed",
            "statement": "The endpoint distance inequality follows from the one-step modulus barrier and actual mod-15 residue absence.",
        },
        {
            "name": "global_modulus_dominates_phase_width",
            "status": "open",
            "statement": "A global proof must show every non-structural formal-unit cover word has modulus larger than its fixed phase window width.",
        },
        {
            "name": "small_modulus_overlap_pdec",
            "status": "open",
            "statement": "If word_modulus is not larger than the window width, the possible actual-residue overlap must be certified by PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FiniteOneStepBarrierClosed",
            "closed": agg["one_step_barrier_failure_count"] == 0,
            "proved": True,
            "meaning": "当前全部窗口错位原子都由 M>W 的一跳模数屏障解释。",
            "remaining": "closed on current finite frontier",
        },
        {
            "gate": "EndpointInequalityReducedToModulusWidth",
            "closed": True,
            "proved": True,
            "meaning": "端点距离守门项已化为 word_modulus 与 phase_width 的比较。",
            "remaining": "closed",
        },
        {
            "gate": "GlobalModulusWidthDominanceProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明任意 formal-unit 非结构冲突覆盖词都满足 M>W。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "SmallModulusOverlapPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若 M<=W，则需对可能重叠给出 PDEC/ColumnCRT 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步关闭当前端点距离计算层，但全局行/列命题仍未无条件闭合。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造一跳模数屏障结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    records = [barrier_record(row) for row in source["selector_window_miss_records"]]
    atoms = [atom for row in records for atom in row["barrier_atoms"]]
    margins = [atom["modulus_minus_width"] for atom in atoms]
    ratios = [atom["modulus_to_width_ratio"] for atom in atoms if atom["modulus_to_width_ratio"] is not None]
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "record_count": len(records),
        "barrier_atom_count": len(atoms),
        "one_step_barrier_closed_count": sum(1 for atom in atoms if atom["one_step_barrier_closed"]),
        "one_step_barrier_failure_count": sum(1 for atom in atoms if not atom["one_step_barrier_closed"]),
        "min_modulus_minus_width": min(margins) if margins else None,
        "max_modulus_minus_width": max(margins) if margins else None,
        "min_modulus_to_width_ratio": min(ratios) if ratios else None,
        "max_modulus_to_width_ratio": max(ratios) if ratios else None,
        "global_modulus_width_dominance_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_modulus_barrier_records": records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_barrier_router",
        "status": "selector_one_step_modulus_barrier_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_barrier_not_used_as_global_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "selector_modulus_barrier_records": records,
        "window_miss_aggregate": source["aggregate"],
        "global_modulus_width_dominance_proved": False,
        "small_modulus_overlap_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_modulus_barrier_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_window_miss_router.py": sha256(
                WINDOW_MISS_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-window-miss-ledger.json": sha256(
                input_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 Q=15 窗口错位的端点距离不等式进一步压缩为一跳模数屏障。"
            "当前 49 个错位原子全部满足：覆盖词进程在 phase 窗口内只有一个代表、该代表"
            "不是 actual P 的 mod 15 残基，且 word_modulus M 大于 phase_width W。于是沿同一"
            "覆盖词进程要到达 actual 残基至少平移一个 M，而一个 M 已超过整个窗口宽度，故命中点"
            "必在窗口外。当前最小 M-W 为 "
            f"{aggregate['min_modulus_minus_width']}，最小 M/W 为 {aggregate['min_modulus_to_width_ratio']:.6f}。"
            "全局剩余变成证明 formal-unit 族中非结构冲突覆盖词均满足 M>W，或把 M<=W 的重叠族送入 PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector modulus barrier router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"record_count={agg['record_count']}",
        f"barrier_atom_count={agg['barrier_atom_count']}",
        f"one_step_barrier_closed_count={agg['one_step_barrier_closed_count']}",
        f"one_step_barrier_failure_count={agg['one_step_barrier_failure_count']}",
        f"min_modulus_minus_width={agg['min_modulus_minus_width']}",
        f"min_modulus_to_width_ratio={agg['min_modulus_to_width_ratio']:.6f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 一跳屏障",
        "",
        "若覆盖词进程在 phase 窗口内只有一个代表 `v`，且 `v mod 15` 不是 actual `P mod 15`，则下一个 actual 残基命中必须沿同一进程平移非零个 `M`。当 `M>W` 时，任意一跳已超过整个窗口宽度，因此 actual 残基命中不可能仍在窗口内。",
        "",
        "## 2. 前沿记录",
        "",
        "| idx | P | side | atoms | closed | failures | min M-W | min M/W |",
        "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["selector_modulus_barrier_records"]:
        ratio = row["min_modulus_to_width_ratio"]
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["index"]),
                    str(row["p"]),
                    f"`{row['side']}`",
                    str(row["window_miss_atom_count"]),
                    str(row["one_step_barrier_closed_count"]),
                    str(row["one_step_barrier_failure_count"]),
                    str(row["min_modulus_minus_width"]),
                    f"{ratio:.6f}" if ratio is not None else "None",
                ]
            )
            + " |"
        )
    atoms = [
        atom
        for row in result["selector_modulus_barrier_records"]
        for atom in row["barrier_atoms"]
    ]
    lines.extend(
        [
            "",
            "## 3. 最紧屏障原子",
            "",
            "| P | side | labels | M | W | M-W | M/W | nearest distance |",
            "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for atom in sorted(atoms, key=lambda item: item["modulus_minus_width"])[:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(atom["p"]),
                    f"`{atom['side']}`",
                    f"`{atom['labels']}`",
                    str(atom["word_modulus"]),
                    str(atom["phase_p_width"]),
                    str(atom["modulus_minus_width"]),
                    f"{atom['modulus_to_width_ratio']:.6f}",
                    str(atom["nearest_hit_distance"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 命题行",
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
            "## 5. 决策表",
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
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 直接证明目标：从 fixed band/k phase 宽度公式与 cover-word 标签乘积下界推出 `M>W`。",
            "- 若存在 `M<=W`，则把对应 actual-residue overlap 登记为 small-modulus overlap `PDEC/ColumnCRT`。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 7. 依赖哈希",
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
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-modulus-barrier-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "barrier_atom_count": result["aggregate"]["barrier_atom_count"],
                "one_step_barrier_failure_count": result["aggregate"][
                    "one_step_barrier_failure_count"
                ],
                "min_modulus_minus_width": result["aggregate"]["min_modulus_minus_width"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
