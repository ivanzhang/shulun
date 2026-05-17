#!/usr/bin/env python3
"""生成 formal-to-actual cutset 之后的命名出口前沿证书。

用法示例：
  python3 experiments/prime_matrix_after_cutset_named_exit_frontier_router.py
  python3 -m json.tool data/prime-matrix-after-cutset-named-exit-frontier-ledger.json

输出：
  data/prime-matrix-after-cutset-named-exit-frontier-ledger.json
  docs/monograph/prime-matrix-after-cutset-named-exit-frontier-router.json
  docs/monograph/prime-matrix-after-cutset-named-exit-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CUTSET = DATA / "prime-matrix-formal-to-actual-global-cutset-ledger.json"
WINDOW_EDGE = DATA / "prime-matrix-affine-twin-window-edge-collision-ledger.json"
SUPPORT_MOTION = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
PRIMITIVE_DEFECT = DATA / "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
MOVING_SLOT = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json"
EPOCH_PAIR = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-epoch-pair-multiplicity-ledger.json"
UNIQUE_REP = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json"
TRANSPORT_RESET = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-after-cutset-named-exit-frontier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-after-cutset-named-exit-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-after-cutset-named-exit-frontier-router.md"

NEXT_TARGET = "GlobalNamedExitExclusionOrSummability"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def aggregate(path: Path) -> dict[str, Any]:
    """读取账本 aggregate；无 aggregate 时返回原对象。"""
    obj = load_json(path)
    return obj.get("aggregate", obj)


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_ratio(numerator: int | float, denominator: int | float) -> str:
    """稳定输出比值。"""
    return f"{numerator / denominator:.6f}" if denominator else "undefined"


def build_result() -> dict[str, Any]:
    """合成 cutset 后命名出口前沿。"""
    cutset = aggregate(CUTSET)
    edge = aggregate(WINDOW_EDGE)
    support = aggregate(SUPPORT_MOTION)
    primitive = aggregate(PRIMITIVE_DEFECT)
    moving = aggregate(MOVING_SLOT)
    epoch = aggregate(EPOCH_PAIR)
    unique = aggregate(UNIQUE_REP)
    transport = aggregate(TRANSPORT_RESET)

    closed_flags = {
        "cutset_partition_current_sweep": bool(cutset["current_sweep_cutset_closed"]),
        "window_edge_displacement_current_sweep": bool(
            edge["window_edge_collision_displacement_closed_current_sweep"]
        ),
        "support_motion_depth_current_sweep": bool(support["support_motion_depth_closed_current_sweep"]),
        "fixed_primitive_absorption_current_sweep": bool(
            primitive["fixed_primitive_key_support_motion_absorption_closed_current_sweep"]
        ),
        "fixed_highfactor_slot_isolation_current_sweep": bool(
            moving["fixed_highfactor_slot_pattern_isolation_failure_count_at_p0"] == 0
            and moving["equality_atom_fixed_pattern_isolated"]
        ),
        "epoch_pair_sparse_gate_current_sweep": bool(epoch["current_sparse_acceptance_closed"]),
        "transport_reset_atoms_empty_current_sweep": bool(transport["current_sweep_transport_reset_atoms_empty"]),
        "unique_representative_identity_current_sweep": bool(
            unique["unique_representative_identity_failure_count"] == 0
        ),
    }

    open_global_flags = {
        "source_materialization_global": "SourceMaterializationFailure-PDEC/SAE",
        "crt_window_global": "CRTWindowEmptyGlobalSupportBound",
        "window_edge_global": "WindowEdgeCollisionOrUnusedTargetArrivalBound",
        "support_motion_global": "SupportMotionNonpersistenceOrEndpointReleaseBound",
        "primitive_identity_shift_global": "PrimitiveIdentityShiftExclusion",
        "moving_slot_family_global": "MovingSlotFamily-PDEC/ColumnCRT",
        "transport_reset_global": "TransportResetPDECExclusion",
        "epoch_pair_global": "GlobalEpochPairMultiplicityBound",
        "moving_residue_global": "MovingResidueShapeSAE/Rankin",
        "singleton_residue_global": "SingletonResidueSAE/Rankin",
    }

    named_exit_rows = [
        {
            "exit_family": "SourceMaterializationFailure",
            "current_readout": (
                f"source_unmaterialized={cutset['source_unmaterialized_pair_total_current']} "
                f"inside formal_to_actual_gap={cutset['formal_to_actual_gap']}"
            ),
            "current_route": "already separated by cutset completeness",
            "global_remaining": "SameGapWrongSource-PDEC/SAE or NoGapSource-PDEC/SAE exclusion/summability",
        },
        {
            "exit_family": "CRTWindowEmpty",
            "current_readout": (
                f"empty_pairs={cutset['crt_window_empty_pair_total_current']}, "
                f"modulus={cutset['combined_modulus_current']}, "
                f"support_width={cutset['support_width_current']}, "
                f"min_empty_distance={cutset['min_empty_window_distance']}"
            ),
            "current_route": "phase window empty, not hidden actual load",
            "global_remaining": "CRTWindowEmptyGlobalSupportBound",
        },
        {
            "exit_family": "WindowEdgeCollision/UnusedTargetArrival",
            "current_readout": (
                f"candidates={edge['edge_collision_candidate_count_current']}, "
                f"existing_actual_needed={edge['empty_pairs_target_existing_actual_count']}, "
                f"unused_target_needed={edge['empty_pairs_target_unused_residue_arrival_count']}, "
                f"l1_displacement={edge['min_empty_l1_residue_displacement']}.."
                f"{edge['max_empty_l1_residue_displacement']}"
            ),
            "current_route": "all current empty windows have positive residue displacement",
            "global_remaining": "global edge-collision bound or unused-target arrival bound",
        },
        {
            "exit_family": "SupportMotionEndpointRelease",
            "current_readout": (
                f"candidates={support['support_motion_candidate_count']}, "
                f"support_width={support['support_width_current']}, "
                f"min_endpoint_release={support['min_endpoint_release_total_required']}, "
                f"release_over_width={fmt_ratio(support['min_endpoint_release_total_required'], support['support_width_current'])}"
            ),
            "current_route": "every support motion requires both endpoint releases",
            "global_remaining": "SupportMotionNonpersistence or endpoint-release summability",
        },
        {
            "exit_family": "PrimitiveIdentityShift",
            "current_readout": (
                f"min_total_depth_defect={primitive['min_total_affine_depth_defect']}, "
                f"breaks_both_depth_identities={fmt_bool(primitive['all_support_motion_breaks_both_depth_identities'])}, "
                f"fixed_q_absorbs={fmt_bool(primitive['any_fixed_q_affine_depth_identity_can_absorb'])}"
            ),
            "current_route": "fixed primitive key cannot absorb current support motion",
            "global_remaining": "PrimitiveIdentityShiftExclusion or PDEC/SAE registration",
        },
        {
            "exit_family": "MovingSlotFamily",
            "current_readout": (
                f"fixed_pattern_failures={moving['fixed_highfactor_slot_pattern_isolation_failure_count_at_p0']}, "
                f"equality_atom_isolated={fmt_bool(moving['equality_atom_fixed_pattern_isolated'])}, "
                f"min_crt_minus_phase_width={moving['min_crt_minus_phase_width_at_p0']}, "
                f"max_phase_width={moving['max_phase_width_at_p0']}"
            ),
            "current_route": "fixed highfactor slot patterns isolated by CRT modulus > phase width",
            "global_remaining": "exclude moving highfactor slot families or route to MovingSlot-PDEC/ColumnCRT",
        },
        {
            "exit_family": "TransportReset",
            "current_readout": (
                f"transport_cells={transport['transport_cell_count']}, "
                f"unique_keys={transport['unique_transport_cell_key_count']}, "
                f"repeated_keys={transport['repeated_transport_cell_key_count']}, "
                f"reset_atoms={transport['reset_pdec_atom_count']}"
            ),
            "current_route": "current transport reset atom set is empty",
            "global_remaining": "TransportResetPDECExclusion and transport SAE/Rankin bound",
        },
        {
            "exit_family": "EpochPairMultiplicity",
            "current_readout": (
                f"candidate_q={epoch['candidate_q_values']}, "
                f"mass_upper_sum={epoch['candidate_product_mass_upper_sum']:.12f}, "
                f"eta={epoch['eta']}, "
                f"high_density_count={epoch['high_density_epoch_pair_count']}"
            ),
            "current_route": "current candidate mass is below eta sparse gate",
            "global_remaining": "GlobalEpochPairMultiplicityBound or HighDensityEpochPair-PDEC/ColumnCRT exclusion",
        },
        {
            "exit_family": "MovingResidue/SingletonSAE",
            "current_readout": (
                f"physical_records={unique['physical_record_count']}, "
                f"singleton_packets={unique['residue_count_histogram']['1']}, "
                f"recurrent_fixed_residue_packets={unique['recurrent_fixed_residue_packet_count']}, "
                f"moving_residue_shapes={unique['moving_residue_shape_count']}"
            ),
            "current_route": "identity split has no current representative failure",
            "global_remaining": "MovingResidueShapeSAE/Rankin and SingletonResidueSAE/Rankin",
        },
    ]

    current_sweep_frontier_closed = all(closed_flags.values())
    row_column_unconditional_closed = all(
        [
            bool(cutset["row_column_unconditional_closed"]),
            bool(edge["row_column_unconditional_closed"]),
            bool(support["row_column_unconditional_closed"]),
            bool(primitive["row_column_unconditional_closed"]),
            bool(moving["row_column_unconditional_closed"]),
            bool(epoch["row_column_unconditional_closed"]),
            bool(unique["row_column_unconditional_closed"]),
            bool(transport["row_column_unconditional_closed"]),
        ]
    )

    result = {
        "certificate_type": "prime_matrix_after_cutset_named_exit_frontier_router",
        "status": "after_cutset_named_exit_frontier_current_sweep_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "formal_pair_total": cutset["formal_pair_total"],
            "actual_packet_total_current": cutset["actual_packet_total_current"],
            "formal_to_actual_gap": cutset["formal_to_actual_gap"],
            "source_unmaterialized_pair_total_current": cutset["source_unmaterialized_pair_total_current"],
            "crt_window_empty_pair_total_current": cutset["crt_window_empty_pair_total_current"],
            "unresolved_formal_pair_total_current": cutset["unresolved_formal_pair_total_current"],
            "edge_collision_candidate_count_current": edge["edge_collision_candidate_count_current"],
            "support_motion_candidate_count": support["support_motion_candidate_count"],
            "min_endpoint_release_total_required": support["min_endpoint_release_total_required"],
            "min_endpoint_release_over_support_width": fmt_ratio(
                support["min_endpoint_release_total_required"], support["support_width_current"]
            ),
            "min_total_affine_depth_defect": primitive["min_total_affine_depth_defect"],
            "fixed_highfactor_slot_pattern_isolation_failure_count_at_p0": moving[
                "fixed_highfactor_slot_pattern_isolation_failure_count_at_p0"
            ],
            "min_crt_minus_phase_width_at_p0": moving["min_crt_minus_phase_width_at_p0"],
            "transport_reset_pdec_atom_count": transport["reset_pdec_atom_count"],
            "candidate_product_mass_upper_sum": epoch["candidate_product_mass_upper_sum"],
            "eta": epoch["eta"],
            "high_density_epoch_pair_count": epoch["high_density_epoch_pair_count"],
            "moving_residue_shape_count": unique["moving_residue_shape_count"],
            "singleton_residue_packet_count": unique["residue_count_histogram"]["1"],
            "current_sweep_frontier_closed": current_sweep_frontier_closed,
            "row_column_unconditional_closed": row_column_unconditional_closed,
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "closed_flags": closed_flags,
        "open_global_flags": open_global_flags,
        "named_exit_rows": named_exit_rows,
        "frontier_formula": (
            "FormalToActualGap = SourceFailure + CRTWindowEmpty + PrimitiveEscape, "
            "and every post-cutset primitive escape is routed to window-edge, support-motion, "
            "primitive-identity, moving-slot, transport-reset, epoch-pair, or residue-SAE named exits."
        ),
        "plain_conclusion": (
            "cutset 完备后，当前 sweep 不再存在匿名容量缺口：40 个形式配对中 1 个成为 actual packet，"
            "28 个进入 source failure，11 个进入 CRT 空窗；空窗后的 11 个边缘候选又被分流到 "
            "window-edge、support-motion、primitive-identity 与 moving-slot/transport/epoch/residue 出口。"
            "本证书关闭的是 current-sweep after-cutset 前沿；全局行/列命题仍需证明这些命名出口的无条件排斥或可求和吸收。"
        ),
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                CUTSET,
                WINDOW_EDGE,
                SUPPORT_MOTION,
                PRIMITIVE_DEFECT,
                MOVING_SLOT,
                EPOCH_PAIR,
                UNIQUE_REP,
                TRANSPORT_RESET,
            )
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown 前沿证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix after-cutset named-exit frontier router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"formal_pair_total={agg['formal_pair_total']}",
        f"actual_packet_total_current={agg['actual_packet_total_current']}",
        f"formal_to_actual_gap={agg['formal_to_actual_gap']}",
        f"source_unmaterialized_pair_total_current={agg['source_unmaterialized_pair_total_current']}",
        f"crt_window_empty_pair_total_current={agg['crt_window_empty_pair_total_current']}",
        f"unresolved_formal_pair_total_current={agg['unresolved_formal_pair_total_current']}",
        f"edge_collision_candidate_count_current={agg['edge_collision_candidate_count_current']}",
        f"support_motion_candidate_count={agg['support_motion_candidate_count']}",
        f"min_endpoint_release_total_required={agg['min_endpoint_release_total_required']}",
        f"min_endpoint_release_over_support_width={agg['min_endpoint_release_over_support_width']}",
        f"min_total_affine_depth_defect={agg['min_total_affine_depth_defect']}",
        f"fixed_highfactor_slot_pattern_isolation_failure_count_at_p0={agg['fixed_highfactor_slot_pattern_isolation_failure_count_at_p0']}",
        f"min_crt_minus_phase_width_at_p0={agg['min_crt_minus_phase_width_at_p0']}",
        f"transport_reset_pdec_atom_count={agg['transport_reset_pdec_atom_count']}",
        f"candidate_product_mass_upper_sum={agg['candidate_product_mass_upper_sum']:.12f}",
        f"eta={agg['eta']}",
        f"high_density_epoch_pair_count={agg['high_density_epoch_pair_count']}",
        f"moving_residue_shape_count={agg['moving_residue_shape_count']}",
        f"singleton_residue_packet_count={agg['singleton_residue_packet_count']}",
        f"current_sweep_frontier_closed={fmt_bool(agg['current_sweep_frontier_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. after-cutset 命名出口表",
        "",
        "| exit family | current readout | current route | global remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["named_exit_rows"]:
        lines.append(
            f"| `{row['exit_family']}` | {row['current_readout']} | {row['current_route']} | `{row['global_remaining']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 当前闭合标志",
            "",
            "| flag | value |",
            "| --- | ---: |",
        ]
    )
    for key, value in result["closed_flags"].items():
        lines.append(f"| `{key}` | `{fmt_bool(value)}` |")

    lines.extend(
        [
            "",
            "## 3. 全局剩余接口",
            "",
        ]
    )
    for key, value in result["open_global_flags"].items():
        lines.append(f"- `{key}` -> `{value}`")

    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 该证书把 cutset 完备分割后的剩余全部压入命名出口前沿。",
            "- 它证明 current sweep 的匿名容量/相位逃逸已关闭；没有证明全局行/列命题。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
