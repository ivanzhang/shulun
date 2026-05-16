#!/usr/bin/env python3
"""把 AffineTwin 压力乘积门压成整数阈值缺口证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_integer_threshold_deficit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRESSURE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json"
MOVING_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json"
EPOCH_CAPACITY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-router.md"

NEXT_TARGET = "AffineTwinThresholdDeficitBoundOrThresholdCrossingPDECExclusion"


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


def capacity_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], dict[str, Any]]:
    """按 side/ell 建立 epoch 容量索引。"""
    return {(str(row["side"]), int(row["ell"])): row for row in rows}


def moving_index(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立 AffineTwin moving 行索引。"""
    return {int(row["q"]): row for row in rows}


def min_joint_extra_to_cross(
    generator_used: int,
    fill_used: int,
    generator_capacity: int,
    fill_capacity: int,
    threshold_product: int,
) -> dict[str, Any]:
    """求最小总增量，使 (A_g+dg)(A_f+df) 穿越整数阈值。"""
    best_total: int | None = None
    witnesses: list[dict[str, int]] = []
    for d_generator in range(generator_capacity - generator_used + 1):
        new_generator = generator_used + d_generator
        if new_generator <= 0:
            continue
        fail_fill = threshold_product // new_generator + 1
        d_fill = max(0, fail_fill - fill_used)
        if fill_used + d_fill > fill_capacity:
            continue
        total = d_generator + d_fill
        if best_total is None or total < best_total:
            best_total = total
            witnesses = []
        if total == best_total and len(witnesses) < 6:
            witnesses.append(
                {
                    "extra_generator_residues": d_generator,
                    "extra_fill_residues": d_fill,
                    "new_generator_used": new_generator,
                    "new_fill_used": fill_used + d_fill,
                    "new_product": new_generator * (fill_used + d_fill),
                }
            )
    return {
        "min_total_extra_residues_to_cross": best_total,
        "min_crossing_witnesses": witnesses,
    }


def threshold_row(
    pressure_row: dict[str, Any],
    moving_by_q: dict[int, dict[str, Any]],
    capacity_by_epoch: dict[tuple[str, int], dict[str, Any]],
) -> dict[str, Any]:
    """构造单个 q 的整数阈值缺口行。"""
    q = int(pressure_row["q"])
    moving = moving_by_q[q]
    generator_side = str(moving["generator_side"])
    fill_side = str(moving["fill_side"])
    generator_ell = int(pressure_row["generator_ell"])
    fill_ell = int(pressure_row["fill_ell"])
    generator_used = int(pressure_row["generator_used_residue_count"])
    fill_used = int(pressure_row["fill_used_residue_count"])
    capacity = generator_ell * fill_ell
    threshold = math.isqrt(capacity)
    current_product = generator_used * fill_used
    required_product_for_failure = threshold + 1
    product_gate_passed = current_product <= threshold
    fixed_generator_fill_fail_at = threshold // generator_used + 1
    fixed_fill_generator_fail_at = threshold // fill_used + 1 if fill_used else None
    joint = min_joint_extra_to_cross(
        generator_used,
        fill_used,
        generator_ell,
        fill_ell,
        threshold,
    )
    generator_epoch = capacity_by_epoch[(generator_side, generator_ell)]
    fill_epoch = capacity_by_epoch[(fill_side, fill_ell)]
    activation_delay = int(fill_epoch["p_min"]) - int(generator_epoch["p_min"])
    return {
        "q": q,
        "generator_side": generator_side,
        "fill_side": fill_side,
        "generator_ell": generator_ell,
        "fill_ell": fill_ell,
        "generator_used_residue_count": generator_used,
        "fill_used_residue_count": fill_used,
        "epoch_pair_capacity": capacity,
        "integer_safe_product_threshold": threshold,
        "required_product_for_failure": required_product_for_failure,
        "current_residue_product": current_product,
        "integer_product_slack": threshold - current_product,
        "integer_threshold_gate_passed_current_sweep": product_gate_passed,
        "threshold_crossing_pdec_trigger_current_sweep": not product_gate_passed,
        "fixed_generator_fill_fail_at": fixed_generator_fill_fail_at,
        "extra_fill_residues_to_fail_with_generator_fixed": max(
            0,
            fixed_generator_fill_fail_at - fill_used,
        ),
        "fixed_fill_generator_fail_at": fixed_fill_generator_fail_at,
        "extra_generator_residues_to_fail_with_fill_fixed": max(
            0,
            fixed_fill_generator_fail_at - generator_used,
        )
        if fixed_fill_generator_fail_at is not None
        else None,
        "min_total_extra_residues_to_cross": joint["min_total_extra_residues_to_cross"],
        "min_crossing_witnesses": joint["min_crossing_witnesses"],
        "generator_epoch_p_min": int(generator_epoch["p_min"]),
        "generator_epoch_p_max": int(generator_epoch["p_max"]),
        "fill_epoch_p_min": int(fill_epoch["p_min"]),
        "fill_epoch_p_max": int(fill_epoch["p_max"]),
        "fill_activation_delay_over_generator": activation_delay,
        "fill_epoch_is_younger_than_generator_epoch": activation_delay > 0,
        "realized_current_sweep": bool(pressure_row["realized_current_sweep"]),
        "realized_pair_count": int(pressure_row["realized_pair_count"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "integer_threshold_form_of_pressure_gate",
            "status": "closed",
            "statement": "The pressure-product gate is equivalent to A_g A_f <= floor(sqrt(q(q-2))).",
        },
        {
            "name": "current_threshold_deficit_materialized",
            "status": "closed_current_sweep",
            "statement": "Every current affine-twin q has positive integer product slack; the smallest multi-side crossing deficit is four additional residues.",
        },
        {
            "name": "activation_delay_diagnosis",
            "status": "closed_current_sweep",
            "statement": "In every current candidate, the fill-side epoch activates later than the generator-side epoch, explaining why one-sided generator pressure has not synchronized with fill pressure.",
        },
        {
            "name": "threshold_crossing_pdec_routing",
            "status": "closed_routing",
            "statement": "If a future row crosses the integer threshold, it is a named ThresholdCrossing-PDEC/ColumnCRT object with explicit extra-residue witnesses.",
        },
        {
            "name": "global_threshold_deficit_bound",
            "status": "open",
            "statement": "A self-contained proof still must show persistent affine-twin rows cannot close the integer threshold deficit, or exclude the crossing PDEC family.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "IntegerThresholdEquivalenceClosed",
            "closed": True,
            "proved": True,
            "meaning": "`PressureProduct` 已无损改写为整数乘积阈值。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentThresholdDeficitPositive",
            "closed": agg["all_current_rows_have_positive_integer_product_slack"],
            "proved": False,
            "meaning": "当前所有候选 q 距离阈值穿越都有正整数缺口。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentFillActivationDelayed",
            "closed": agg["all_current_fill_epochs_younger_than_generators"],
            "proved": False,
            "meaning": "当前所有候选的 fill 侧晚于 generator 侧激活，给出压力不同步的结构诊断。",
            "remaining": "finite structural diagnosis",
        },
        {
            "gate": "ThresholdCrossingPDECRouted",
            "closed": True,
            "proved": True,
            "meaning": "若整数阈值被穿越，失败行有明确的最小 residue 增量见证。",
            "remaining": "exclusion still separate",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只压窄为阈值缺口守门项，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(
    pressure_ledger: Path,
    moving_ledger: Path,
    epoch_capacity_ledger: Path,
) -> dict[str, Any]:
    """构造整数阈值缺口结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    pressure = load_json(pressure_ledger)
    moving = load_json(moving_ledger)
    capacity = load_json(epoch_capacity_ledger)
    moving_by_q = moving_index(moving["candidate_affine_twin_epoch_pair_rows"])
    capacity_by_epoch = capacity_index(capacity["epoch_capacity_rows"])
    rows = [
        threshold_row(row, moving_by_q, capacity_by_epoch)
        for row in pressure["paired_side_pressure_rows"]
    ]
    pdec_rows = [row for row in rows if row["threshold_crossing_pdec_trigger_current_sweep"]]
    aggregate = {
        "pressure_ledger": str(pressure_ledger.relative_to(ROOT)),
        "moving_ledger": str(moving_ledger.relative_to(ROOT)),
        "epoch_capacity_ledger": str(epoch_capacity_ledger.relative_to(ROOT)),
        "candidate_q_values": [row["q"] for row in rows],
        "realized_q_values": [row["q"] for row in rows if row["realized_current_sweep"]],
        "all_current_rows_pass_integer_threshold_gate": len(pdec_rows) == 0,
        "threshold_crossing_pdec_count_current_sweep": len(pdec_rows),
        "all_current_rows_have_positive_integer_product_slack": all(
            row["integer_product_slack"] > 0 for row in rows
        ),
        "min_integer_product_slack": min(
            (row["integer_product_slack"] for row in rows),
            default=None,
        ),
        "min_total_extra_residues_to_cross": min(
            (row["min_total_extra_residues_to_cross"] for row in rows),
            default=None,
        ),
        "all_current_fill_epochs_younger_than_generators": all(
            row["fill_epoch_is_younger_than_generator_epoch"] for row in rows
        ),
        "min_fill_activation_delay_over_generator": min(
            (row["fill_activation_delay_over_generator"] for row in rows),
            default=None,
        ),
        "integer_threshold_deficit_bound_proved_globally": False,
        "threshold_crossing_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "integer_threshold_deficit_rows": rows,
        "threshold_crossing_pdec_rows_current_sweep": pdec_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_integer_threshold_deficit_router"
        ),
        "status": "affine_twin_pressure_product_reduced_to_integer_threshold_deficit_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "integer_threshold_deficit_rows": rows,
        "threshold_crossing_pdec_rows_current_sweep": pdec_rows,
        "integer_threshold_deficit_bound_proved_globally": False,
        "threshold_crossing_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinPairedSidePressureBoundOrPressureProductPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 `PressureProduct` 门压成纯整数阈值：`A_g*A_f <= floor(sqrt(q(q-2)))`。"
            f"当前全部候选通过，最小整数乘积缺口为 {aggregate['min_integer_product_slack']}，"
            f"若允许两侧同时新增 residue，最少还需 {aggregate['min_total_extra_residues_to_cross']} "
            "个额外 residue 才能穿越阈值。所有当前候选的 fill 侧激活都晚于 generator 侧，"
            f"最小延迟为 {aggregate['min_fill_activation_delay_over_generator']}。"
            "因此最新最窄硬点是：证明这种激活延迟/阈值缺口不能被持久补齐；若被补齐，"
            "即得到显式 `ThresholdCrossing-PDEC/ColumnCRT`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_integer_threshold_deficit_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json": sha256(
            pressure_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-moving-family-sae-columncrt-ledger.json": sha256(
            moving_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json": sha256(
            epoch_capacity_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin integer threshold deficit router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"all_current_rows_pass_integer_threshold_gate={fmt_bool(agg['all_current_rows_pass_integer_threshold_gate'])}",
        f"min_integer_product_slack={agg['min_integer_product_slack']}",
        f"min_total_extra_residues_to_cross={agg['min_total_extra_residues_to_cross']}",
        f"all_current_fill_epochs_younger_than_generators={fmt_bool(agg['all_current_fill_epochs_younger_than_generators'])}",
        f"min_fill_activation_delay_over_generator={agg['min_fill_activation_delay_over_generator']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 整数阈值表",
        "",
        "| q | product | threshold | slack | min extra | fill delay | fixed gen fail fill | fixed fill fail gen |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["integer_threshold_deficit_rows"]:
        lines.append(
            f"| {row['q']} | {row['current_residue_product']} | "
            f"{row['integer_safe_product_threshold']} | {row['integer_product_slack']} | "
            f"{row['min_total_extra_residues_to_cross']} | "
            f"{row['fill_activation_delay_over_generator']} | "
            f"{row['fixed_generator_fill_fail_at']} | "
            f"{row['fixed_fill_generator_fail_at']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 等价式",
            "",
            "```text",
            "A_g A_f <= floor(sqrt(q(q-2)))",
            "iff (A_g A_f)^2 <= q(q-2)",
            "iff (A_g^2/(q-2)) * (A_f^2/q) <= 1.",
            "```",
            "",
            "阈值穿越不再是定性事件：每个 q 都有明确的最小新增 residue 见证。",
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
            "- 证明方向：把 fill 侧激活延迟和 residue 到达速率结合，证明阈值缺口不能被持久补齐。",
            "- 失败方向：若缺口被补齐，直接输出带最小新增 residue 见证的 `ThresholdCrossing-PDEC/ColumnCRT`。",
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
    parser.add_argument("--pressure-ledger", type=Path, default=PRESSURE_LEDGER)
    parser.add_argument("--moving-ledger", type=Path, default=MOVING_LEDGER)
    parser.add_argument("--epoch-capacity-ledger", type=Path, default=EPOCH_CAPACITY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    pressure_ledger = args.pressure_ledger if args.pressure_ledger.is_absolute() else ROOT / args.pressure_ledger
    moving_ledger = args.moving_ledger if args.moving_ledger.is_absolute() else ROOT / args.moving_ledger
    epoch_capacity_ledger = (
        args.epoch_capacity_ledger if args.epoch_capacity_ledger.is_absolute() else ROOT / args.epoch_capacity_ledger
    )
    result = build_result(pressure_ledger, moving_ledger, epoch_capacity_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-integer-threshold-deficit-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "candidate_q_values": result["aggregate"]["candidate_q_values"],
                "min_integer_product_slack": result["aggregate"]["min_integer_product_slack"],
                "min_total_extra_residues_to_cross": result["aggregate"]["min_total_extra_residues_to_cross"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
