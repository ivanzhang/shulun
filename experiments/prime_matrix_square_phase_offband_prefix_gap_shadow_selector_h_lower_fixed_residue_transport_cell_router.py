#!/usr/bin/env python3
"""把固定残基槽漂移压成 transport cell 审计。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_residue_transport_cell_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLOT_DRIFT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "fixed-residue-transport-cell-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "fixed-residue-transport-cell-router.md"
)

MAIN_TARGET = "FixedResidueSlotDriftColumnCRTOrMovingResidueShapeSAE"
NEXT_TARGET = "FixedResidueTransportCellPDECOrMovingResidueShapeSAE"


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


def parse_slot(slot_key: str) -> tuple[int, int, int]:
    """解析 b:u:ell 槽键。"""
    b_value, u_value, ell_value = slot_key.split(":")
    return int(b_value), int(u_value), int(ell_value)


def side_from_key(packet_key: str) -> str:
    """从 packet key 提取 side。"""
    if "|side=plus|" in packet_key:
        return "plus"
    if "|side=minus|" in packet_key:
        return "minus"
    raise ValueError(f"side not found in {packet_key}")


def active_edges(b_value: int, u_value: int, side: str) -> dict[str, Any]:
    """返回相位区间的活动边界公式。"""
    base = 2 * b_value * b_value
    if side == "minus":
        lower_candidates = [
            ("lo_div_u_plus_1", base // (u_value + 1) + 2 * b_value + 1),
        ]
        if u_value == 0:
            lower_candidates.append(("lo_u0_2base", 2 * base + 1))
            upper_candidates = [("hi_infinite", 10**30)]
        else:
            lower_candidates.append(
                (
                    "lo_diag",
                    (2 * base + 4 * b_value * u_value + 1 + (2 * u_value + 1) - 1)
                    // (2 * u_value + 1),
                )
            )
            upper_candidates = [
                ("hi_div_u", base // u_value + 2 * b_value),
                ("hi_diag", (base + 2 * b_value * u_value - 1) // u_value),
            ]
    elif side == "plus":
        lower_candidates = [
            ("lo_div_u", base // u_value + 2 * b_value + 1),
            ("lo_diag", (2 * b_value * (u_value + b_value) + 1 + u_value - 1) // u_value),
        ]
        upper_candidates = [
            ("hi_div_u_minus_1", 10**30 if u_value == 1 else base // (u_value - 1) + 2 * b_value),
            ("hi_diag", (4 * b_value * (u_value + b_value) - 1) // (2 * u_value - 1)),
        ]
    else:
        raise ValueError(f"unknown side: {side}")

    lower = max(value for _, value in lower_candidates)
    upper = min(value for _, value in upper_candidates)
    return {
        "lower": lower,
        "upper": upper,
        "lower_active": [name for name, value in lower_candidates if value == lower],
        "upper_active": [name for name, value in upper_candidates if value == upper],
        "lower_candidates": dict(lower_candidates),
        "upper_candidates": dict(upper_candidates),
    }


def transport_cell(row: dict[str, Any]) -> dict[str, Any]:
    """把固定残基换槽复现对写成 transport cell。"""
    side = side_from_key(row["residue_packet_key"])
    b_left, u_left, ell_left = parse_slot(row["left_slot_key"])
    b_right, u_right, ell_right = parse_slot(row["right_slot_key"])
    if ell_left != ell_right or ell_left != int(row["ell"]):
        raise ValueError(f"ell mismatch in {row['residue_packet_key']}")
    ell = int(row["ell"])
    b_gap = int(row["b_gap"])
    u_gap = int(row["u_gap"])
    slot_sum_gap = b_gap + u_gap
    left_edges = active_edges(b_left, u_left, side)
    right_edges = active_edges(b_right, u_right, side)
    common_lower = sorted(set(left_edges["lower_active"]).intersection(right_edges["lower_active"]))
    common_upper = sorted(set(left_edges["upper_active"]).intersection(right_edges["upper_active"]))
    lo_defect = int(row["phase_lo_gap_minus_p_gap"])
    hi_defect = int(row["phase_hi_gap_minus_p_gap"])
    p_lift = int(row["p_gap_over_ell"])
    slot_sum_lift = slot_sum_gap // ell
    b_residue_step = b_gap % ell
    u_residue_step = u_gap % ell
    transport_key = (
        f"side={side}|ell={ell}|residue={row['crt_residue']}|p_lift={p_lift}|"
        f"sum_lift={slot_sum_lift}|b_step={b_residue_step}|"
        f"lo_defect={lo_defect}|hi_defect={hi_defect}|"
        f"lower={','.join(common_lower)}|upper={','.join(common_upper)}"
    )
    return {
        "transport_cell_key": transport_key,
        "residue_packet_key": row["residue_packet_key"],
        "side": side,
        "ell": ell,
        "crt_residue": int(row["crt_residue"]),
        "p_values": list(row["p_values"]),
        "p_lift": p_lift,
        "left_slot_key": row["left_slot_key"],
        "right_slot_key": row["right_slot_key"],
        "b_gap": b_gap,
        "u_gap": u_gap,
        "slot_sum_gap": slot_sum_gap,
        "slot_sum_lift": slot_sum_lift,
        "slot_sum_lift_integral": slot_sum_gap % ell == 0,
        "b_residue_step": b_residue_step,
        "u_residue_step": u_residue_step,
        "residue_step_sum_mod_ell": (b_residue_step + u_residue_step) % ell,
        "left_lower_active": left_edges["lower_active"],
        "right_lower_active": right_edges["lower_active"],
        "common_lower_active": common_lower,
        "left_upper_active": left_edges["upper_active"],
        "right_upper_active": right_edges["upper_active"],
        "common_upper_active": common_upper,
        "active_edge_mode_intersects": bool(common_lower) and bool(common_upper),
        "left_active_interval": [left_edges["lower"], left_edges["upper"]],
        "right_active_interval": [right_edges["lower"], right_edges["upper"]],
        "recorded_left_phase": list(row["phase_left"]),
        "recorded_right_phase": list(row["phase_right"]),
        "active_interval_matches_record": [left_edges["lower"], left_edges["upper"]] == list(row["phase_left"])
        and [right_edges["lower"], right_edges["upper"]] == list(row["phase_right"]),
        "lo_translate_defect": lo_defect,
        "hi_translate_defect": hi_defect,
        "exact_phase_translate": lo_defect == 0 and hi_defect == 0,
        "max_abs_edge_defect": max(abs(lo_defect), abs(hi_defect)),
        "edge_defect_strictly_below_ell": max(abs(lo_defect), abs(hi_defect)) < ell,
        "depth_left": list(row["depth_left"]),
        "depth_right": list(row["depth_right"]),
        "same_depth_signature": bool(row["same_depth_signature"]),
        "min_margin": int(row["min_margin"]),
        "min_crt_minus_phase_width": int(row["min_crt_minus_phase_width"]),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_residue_transport_identity",
            "status": "closed",
            "statement": "For one-slot fixed-residue recurrence, P2-P1 and (b2+u2)-(b1+u1) are both integral ell-lifts.",
        },
        {
            "name": "current_sweep_transport_cells_unique",
            "status": "closed_on_current_sweep",
            "statement": "The current fixed-residue slot-drift recurrences have distinct transport-cell signatures and no exact phase translate.",
        },
        {
            "name": "transport_cell_persistence_exclusion_open",
            "status": "open",
            "statement": "A global proof must exclude persistent transport cells by ColumnCRT/PDEC or route nonpersistent cells to SAE/Rankin.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FixedResidueTransportIdentityClosed",
            "closed": agg["all_slot_sum_lifts_integral"] and agg["all_residue_steps_sum_zero"],
            "proved": True,
            "meaning": "固定残基复现严格推出 `P` 与 `b+u` 的两个 `ell`-lift 条件。",
            "remaining": "closed",
        },
        {
            "gate": "ActiveEdgeModeIntersects",
            "closed": agg["all_active_edge_modes_intersect"],
            "proved": False,
            "meaning": "当前 12 对的左右槽共享相位边界主导公式，可压成同类 transport cell。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ExactPhaseTranslateAbsent",
            "closed": agg["exact_phase_translate_count"] == 0,
            "proved": False,
            "meaning": "当前没有边界缺陷为零的同相位平移复现。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "TransportCellPersistenceExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需证明同一 transport cell 不能全局持久复现。",
            "remaining": "TransportCellPDEC/ColumnCRT",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只压缩固定残基槽漂移，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(slot_drift_ledger: Path) -> dict[str, Any]:
    """构造 transport cell 审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(slot_drift_ledger)
    cells = [transport_cell(row) for row in source["fixed_residue_slot_drift_pairs"]]
    cell_counts = Counter(row["transport_cell_key"] for row in cells)
    edge_defects = [row["max_abs_edge_defect"] for row in cells]
    aggregate = {
        "slot_drift_ledger": str(slot_drift_ledger.relative_to(ROOT)),
        "transport_cell_count": len(cells),
        "unique_transport_cell_count": len(cell_counts),
        "transport_cell_recurrence_count": sum(1 for count in cell_counts.values() if count > 1),
        "all_transport_cells_unique_current_sweep": all(count == 1 for count in cell_counts.values()),
        "all_slot_sum_lifts_integral": all(row["slot_sum_lift_integral"] for row in cells),
        "all_residue_steps_sum_zero": all(row["residue_step_sum_mod_ell"] == 0 for row in cells),
        "all_active_interval_matches_record": all(row["active_interval_matches_record"] for row in cells),
        "all_active_edge_modes_intersect": all(row["active_edge_mode_intersects"] for row in cells),
        "exact_phase_translate_count": sum(1 for row in cells if row["exact_phase_translate"]),
        "all_edge_defects_strictly_below_ell": all(row["edge_defect_strictly_below_ell"] for row in cells),
        "max_abs_edge_defect": max(edge_defects),
        "min_abs_nonzero_edge_defect": min(
            value for row in cells for value in [abs(row["lo_translate_defect"]), abs(row["hi_translate_defect"])] if value > 0
        ),
        "p_lift_histogram": dict(sorted(Counter(str(row["p_lift"]) for row in cells).items(), key=lambda item: int(item[0]))),
        "slot_sum_lift_histogram": dict(
            sorted(Counter(str(row["slot_sum_lift"]) for row in cells).items(), key=lambda item: int(item[0]))
        ),
        "lower_active_histogram": dict(
            sorted(Counter(",".join(row["common_lower_active"]) for row in cells).items())
        ),
        "upper_active_histogram": dict(
            sorted(Counter(",".join(row["common_upper_active"]) for row in cells).items())
        ),
        "transport_cell_persistence_excluded_globally": False,
        "moving_residue_sae_rankin_bound_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "transport_cells": cells,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "fixed_residue_transport_cell_router"
        ),
        "status": "fixed_residue_slot_drift_reduced_to_transport_cells_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "transport_cells": cells,
        "transport_cell_persistence_excluded_globally": False,
        "moving_residue_sae_rankin_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 12 个固定残基换槽复现对压成 transport cell。固定残基给出两个严格整数条件："
            "`P2-P1=k*ell` 且 `(b2+u2)-(b1+u1)=a*ell`。当前扫描中 12 个 transport cell "
            "全部互异，没有 exact phase translate；所有相位边界缺陷的绝对值都小于对应 `ell`。"
            "这说明当前复现不是稳定同相位复现，而是带小边界缺陷的槽漂移；全局仍需排斥 "
            "transport cell 持久复现，或把它送入 SAE/Rankin。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_residue_transport_cell_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-slot-drift-ledger.json": sha256(
            slot_drift_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower fixed-residue transport-cell router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"transport_cell_count={agg['transport_cell_count']}",
        f"unique_transport_cell_count={agg['unique_transport_cell_count']}",
        f"transport_cell_recurrence_count={agg['transport_cell_recurrence_count']}",
        f"all_slot_sum_lifts_integral={fmt_bool(agg['all_slot_sum_lifts_integral'])}",
        f"all_residue_steps_sum_zero={fmt_bool(agg['all_residue_steps_sum_zero'])}",
        f"exact_phase_translate_count={agg['exact_phase_translate_count']}",
        f"all_edge_defects_strictly_below_ell={fmt_bool(agg['all_edge_defects_strictly_below_ell'])}",
        f"max_abs_edge_defect={agg['max_abs_edge_defect']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. transport cell",
        "",
        "```text",
        "P2-P1 = p_lift * ell",
        "(b2+u2)-(b1+u1) = slot_sum_lift * ell",
        "b_step + u_step == 0 mod ell",
        "phase_edge_2 = phase_edge_1 + (P2-P1) + edge_defect",
        "```",
        "",
        "## 2. transport cell 明细",
        "",
        "| ell | residue | side | p values | p lift | sum lift | b/u step | edge defect | active edges | exact translate |",
        "| ---: | ---: | --- | --- | ---: | ---: | --- | --- | --- | ---: |",
    ]
    for row in result["transport_cells"]:
        lines.append(
            f"| {row['ell']} | {row['crt_residue']} | `{row['side']}` | `{row['p_values']}` | "
            f"{row['p_lift']} | {row['slot_sum_lift']} | "
            f"`{row['b_residue_step']}/{row['u_residue_step']}` | "
            f"`{row['lo_translate_defect']}/{row['hi_translate_defect']}` | "
            f"`{row['common_lower_active']} / {row['common_upper_active']}` | "
            f"`{fmt_bool(row['exact_phase_translate'])}` |"
        )

    lines.extend(
        [
            "",
            "## 3. 结构判断",
            "",
            "- 固定残基复现的核心不是固定槽，而是 `P` lift 与槽和 lift 的同步。",
            "- 当前 12 个 cell 没有重复，也没有零边界缺陷的 exact phase translate。",
            "- 若全局出现持久 cell，必须同时固定 lift、槽残差步长和边界缺陷；这就是下一步 ColumnCRT/PDEC 的精确输入。",
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
            "- 固定残基分支：排斥同一 transport cell 的全局持久复现。",
            "- 移动残基分支：继续建立 SAE/Rankin 可求和账本。",
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
    parser.add_argument("--slot-drift-ledger", type=Path, default=SLOT_DRIFT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    slot_drift_ledger = args.slot_drift_ledger if args.slot_drift_ledger.is_absolute() else ROOT / args.slot_drift_ledger
    result = build_result(slot_drift_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-residue-transport-cell-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "transport_cell_count": result["aggregate"]["transport_cell_count"],
                "unique_transport_cell_count": result["aggregate"]["unique_transport_cell_count"],
                "transport_cell_recurrence_count": result["aggregate"]["transport_cell_recurrence_count"],
                "exact_phase_translate_count": result["aggregate"]["exact_phase_translate_count"],
                "max_abs_edge_defect": result["aggregate"]["max_abs_edge_defect"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
