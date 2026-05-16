#!/usr/bin/env python3
"""把 AffineTwin fill 追赶路线压成新增 residue/Rankin 质量预算二分。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_fill_catchup_mass_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

ROUTE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json"
EPOCH_CAPACITY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-router.md"

NEXT_TARGET = "AffineTwinFillResidueArrivalBoundOrFillCatchUpMassPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fraction_json(value: Fraction) -> dict[str, Any]:
    """把分数写成 JSON 友好格式。"""
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def capacity_index(rows: list[dict[str, Any]]) -> dict[tuple[str, int], dict[str, Any]]:
    """按 side/ell 建立 epoch 容量索引。"""
    return {(str(row["side"]), int(row["ell"])): row for row in rows}


def budget_row(row: dict[str, Any], capacity_by_epoch: dict[tuple[str, int], dict[str, Any]]) -> dict[str, Any]:
    """构造单个 q 的 fill 追赶质量预算行。"""
    fill_ell = int(row["fill_ell"])
    fill_side = "plus"
    fill_epoch = capacity_by_epoch[(fill_side, fill_ell)]
    current_fill = int(row["current_fill_used"])
    min_extra_fill = int(row["min_extra_fill_in_minimal_routes"])
    max_new_fill = int(row["max_new_fill_in_minimal_routes"])
    fill_capacity = int(fill_epoch["epoch_residue_capacity"])
    fill_unused = int(fill_epoch["unused_residue_count"])
    min_rankin_mass = Fraction(min_extra_fill, fill_ell)
    max_minimal_route_rankin_mass = Fraction(max_new_fill - current_fill, fill_ell)
    return {
        "q": int(row["q"]),
        "route_class": str(row["route_class"]),
        "fill_side": fill_side,
        "fill_ell": fill_ell,
        "current_fill_used": current_fill,
        "fill_epoch_capacity": fill_capacity,
        "fill_epoch_unused_residue_count": fill_unused,
        "fill_epoch_spare_ratio": float(fill_epoch["spare_ratio"]),
        "min_extra_fill_in_minimal_routes": min_extra_fill,
        "max_extra_fill_in_minimal_routes": max_new_fill - current_fill,
        "min_new_fill_rankin_mass_required": fraction_json(min_rankin_mass),
        "max_minimal_route_fill_rankin_mass_required": fraction_json(max_minimal_route_rankin_mass),
        "fill_capacity_can_absorb_minimal_catchup_current_sweep": fill_unused >= min_extra_fill,
        "fill_duplicate_would_trigger_reset_pdec": True,
        "new_fill_or_reset_dichotomy_closed": True,
        "fill_catchup_multiplier_upper": float(row["fill_catchup_multiplier_upper"]),
        "fill_activation_delay_over_generator": int(row["fill_activation_delay_over_generator"]),
        "fill_delay_per_required_fill_increment": float(row["fill_delay_per_required_fill_increment"]),
        "threshold_crossing_pdec_name": row["threshold_crossing_pdec_name"],
        "mass_pdec_name": f"AffineTwinFillCatchUpMass-q{int(row['q'])}-PDEC",
        "realized_current_sweep": bool(row["realized_current_sweep"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fill_catchup_new_residue_or_reset_dichotomy",
            "status": "closed",
            "statement": "Every minimal threshold-crossing route requires fill-side growth; each required fill increment is either a new residue carrying Rankin mass 1/q, or a repeated residue and hence a transport/fixed-residue PDEC.",
        },
        {
            "name": "current_fill_capacity_can_absorb_minimal_catchup",
            "status": "closed_current_sweep",
            "statement": "The current fill epochs have enough unused residue capacity for the minimal catch-up witnesses; this is not an exclusion, only a capacity diagnosis.",
        },
        {
            "name": "fill_catchup_mass_pdec_routing",
            "status": "closed_routing",
            "statement": "If fill catch-up persists, it creates a named fill-side Rankin mass atom; if residue repeats instead, it exits to reset/ColumnCRT PDEC.",
        },
        {
            "name": "global_fill_residue_arrival_bound",
            "status": "open",
            "statement": "A self-contained proof still must bound fill-side residue arrival or exclude the fill-catchup mass PDEC family.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "NewFillOrResetDichotomyClosed",
            "closed": True,
            "proved": True,
            "meaning": "fill 侧追赶必须支付新 residue Rankin 质量，或触发重复 residue/reset PDEC。",
            "remaining": "closed routing",
        },
        {
            "gate": "CurrentFillCapacityAbsorbsMinimalCatchup",
            "closed": agg["all_current_fill_epochs_can_absorb_minimal_catchup"],
            "proved": False,
            "meaning": "当前容量足够容纳最小追赶，因此容量本身不是矛盾。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FillCatchupMassPDECRouted",
            "closed": True,
            "proved": True,
            "meaning": "持久 fill 追赶已变成明确 Rankin 质量原子或 reset PDEC。",
            "remaining": "exclusion still separate",
        },
        {
            "gate": "GlobalFillResidueArrivalBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局控制 fill 侧新增 residue 到达，或排斥质量 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成追赶质量预算二分，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(route_ledger: Path, epoch_capacity_ledger: Path) -> dict[str, Any]:
    """构造 fill 追赶质量预算结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    route = load_json(route_ledger)
    capacity = load_json(epoch_capacity_ledger)
    capacity_by_epoch = capacity_index(capacity["epoch_capacity_rows"])
    rows = [budget_row(row, capacity_by_epoch) for row in route["threshold_route_rows"]]
    total_min_mass = sum(
        Fraction(
            row["min_new_fill_rankin_mass_required"]["numerator"],
            row["min_new_fill_rankin_mass_required"]["denominator"],
        )
        for row in rows
    )
    max_route_mass = max(
        Fraction(
            row["max_minimal_route_fill_rankin_mass_required"]["numerator"],
            row["max_minimal_route_fill_rankin_mass_required"]["denominator"],
        )
        for row in rows
    )
    aggregate = {
        "route_ledger": str(route_ledger.relative_to(ROOT)),
        "epoch_capacity_ledger": str(epoch_capacity_ledger.relative_to(ROOT)),
        "candidate_q_values": [row["q"] for row in rows],
        "all_routes_require_fill_increment": True,
        "all_current_fill_epochs_can_absorb_minimal_catchup": all(
            row["fill_capacity_can_absorb_minimal_catchup_current_sweep"] for row in rows
        ),
        "min_extra_fill_required": min(row["min_extra_fill_in_minimal_routes"] for row in rows),
        "max_extra_fill_required": max(row["max_extra_fill_in_minimal_routes"] for row in rows),
        "total_min_new_fill_rankin_mass_required_if_all_candidates_cross": fraction_json(total_min_mass),
        "max_single_candidate_minimal_route_fill_rankin_mass": fraction_json(max_route_mass),
        "min_fill_epoch_spare_ratio": min(row["fill_epoch_spare_ratio"] for row in rows),
        "new_fill_or_reset_dichotomy_closed": True,
        "fill_catchup_mass_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "fill_catchup_mass_budget_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_fill_catchup_mass_budget_router"
        ),
        "status": "affine_twin_fill_catchup_routed_to_new_residue_mass_or_reset_pdec_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "fill_catchup_mass_budget_rows": rows,
        "new_fill_or_reset_dichotomy_closed": True,
        "fill_catchup_mass_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "AffineTwinFillCatchUpOrMixedCoaccumulationPDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 fill 追赶路线压成二分：每个最小阈值穿越都必须新增 fill residue；"
            "若不是新 residue，则立即是重复 residue/reset/ColumnCRT PDEC。若是新 residue，"
            "它至少支付 `1/q` 的 fill-side Rankin 质量。当前三个候选若同时穿越，最小新增 "
            f"fill Rankin 质量为 {aggregate['total_min_new_fill_rankin_mass_required_if_all_candidates_cross']['decimal']:.12f}；"
            f"当前 fill epoch 最小 spare ratio 为 {aggregate['min_fill_epoch_spare_ratio']:.12f}。"
            "因此容量不产生即时矛盾，最新硬点是全局控制 fill residue 到达率或排斥 fill-catchup mass PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_fill_catchup_mass_budget_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-threshold-route-classifier-ledger.json": sha256(
            route_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json": sha256(
            epoch_capacity_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    total_mass = agg["total_min_new_fill_rankin_mass_required_if_all_candidates_cross"]
    max_mass = agg["max_single_candidate_minimal_route_fill_rankin_mass"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin fill catchup mass budget router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"all_current_fill_epochs_can_absorb_minimal_catchup={fmt_bool(agg['all_current_fill_epochs_can_absorb_minimal_catchup'])}",
        f"min_extra_fill_required={agg['min_extra_fill_required']}",
        f"max_extra_fill_required={agg['max_extra_fill_required']}",
        f"total_min_new_fill_rankin_mass_required_if_all_candidates_cross={total_mass['numerator']}/{total_mass['denominator']} ~= {total_mass['decimal']:.12f}",
        f"max_single_candidate_minimal_route_fill_rankin_mass={max_mass['numerator']}/{max_mass['denominator']} ~= {max_mass['decimal']:.12f}",
        f"min_fill_epoch_spare_ratio={agg['min_fill_epoch_spare_ratio']:.12f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. fill 追赶预算",
        "",
        "| q | route | fill used | min extra fill | fill capacity | unused | min Rankin mass | max route mass | reset dichotomy |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["fill_catchup_mass_budget_rows"]:
        min_mass = row["min_new_fill_rankin_mass_required"]
        max_route = row["max_minimal_route_fill_rankin_mass_required"]
        lines.append(
            f"| {row['q']} | `{row['route_class']}` | {row['current_fill_used']} | "
            f"{row['min_extra_fill_in_minimal_routes']} | {row['fill_epoch_capacity']} | "
            f"{row['fill_epoch_unused_residue_count']} | "
            f"`{min_mass['numerator']}/{min_mass['denominator']}` ~= {min_mass['decimal']:.6f} | "
            f"`{max_route['numerator']}/{max_route['denominator']}` ~= {max_route['decimal']:.6f} | "
            f"`{fmt_bool(row['new_fill_or_reset_dichotomy_closed'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 二分",
            "",
            "```text",
            "minimal threshold crossing",
            "=> fill-side residue increment",
            "=> new residue with Rankin mass 1/q, or repeated residue/reset PDEC.",
            "```",
            "",
            "当前容量足以容纳最小追赶，所以这一步不提供即时矛盾；它把硬点精确转成 fill 侧到达率或 reset PDEC。",
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
            "- 证明方向：给出 fill-side residue arrival 的全局上界，使其不能补齐阈值缺口。",
            "- 失败方向：若 arrival 过密，输出 `FillCatchUpMass-PDEC`；若 residue 重复，输出 reset/ColumnCRT PDEC。",
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
    parser.add_argument("--route-ledger", type=Path, default=ROUTE_LEDGER)
    parser.add_argument("--epoch-capacity-ledger", type=Path, default=EPOCH_CAPACITY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    route_ledger = args.route_ledger if args.route_ledger.is_absolute() else ROOT / args.route_ledger
    epoch_capacity_ledger = (
        args.epoch_capacity_ledger if args.epoch_capacity_ledger.is_absolute() else ROOT / args.epoch_capacity_ledger
    )
    result = build_result(route_ledger, epoch_capacity_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total_mass = result["aggregate"]["total_min_new_fill_rankin_mass_required_if_all_candidates_cross"]
    print(
        json.dumps(
            {
                "status": result["status"],
                "candidate_q_values": result["aggregate"]["candidate_q_values"],
                "total_min_new_fill_rankin_mass_decimal": total_mass["decimal"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
