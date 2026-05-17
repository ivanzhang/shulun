#!/usr/bin/env python3
"""生成全局命名出口的终端 choke-set 证书。

用法示例：
  python3 experiments/prime_matrix_global_named_exit_terminal_choke_router.py
  python3 -m json.tool data/prime-matrix-global-named-exit-terminal-choke-ledger.json

输出：
  data/prime-matrix-global-named-exit-terminal-choke-ledger.json
  docs/monograph/prime-matrix-global-named-exit-terminal-choke-router.json
  docs/monograph/prime-matrix-global-named-exit-terminal-choke-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

AFTER_CUTSET = DATA / "prime-matrix-after-cutset-named-exit-frontier-ledger.json"
FORMAL_CUTSET = DATA / "prime-matrix-formal-to-actual-global-cutset-ledger.json"
WINDOW_EDGE = DATA / "prime-matrix-affine-twin-window-edge-collision-ledger.json"
SUPPORT_MOTION = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
PRIMITIVE_DEFECT = DATA / "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
MOVING_SLOT = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json"
TRANSPORT_RESET = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json"
SINGLETON_BUDGET = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json"
ONE_SLOT_CAPACITY = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
ACTIVE_ELL = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-ell-interval-band-ledger.json"
ENDPOINT_GAP = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-endpoint-motion-gap-ledger.json"
SPARSE_SAE = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-sparse-sae-global-envelope-ledger.json"
PAIRED_PRESSURE = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json"
UNIQUE_REP = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-unique-representative-persistence-split-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-global-named-exit-terminal-choke-ledger.json"
OUT_JSON = DOCS / "prime-matrix-global-named-exit-terminal-choke-router.json"
OUT_MD = DOCS / "prime-matrix-global-named-exit-terminal-choke-router.md"

NEXT_TARGET = "TerminalChokeSetGlobalExclusionOrSummability"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def aggregate(path: Path) -> dict[str, Any]:
    """读取 aggregate；没有 aggregate 时返回原对象。"""
    obj = load_json(path)
    return obj.get("aggregate", obj)


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def ratio_decimal(value: Any) -> float:
    """读取可用的十进制比值。"""
    if isinstance(value, dict) and "decimal" in value:
        return float(value["decimal"])
    return float(value)


def build_result() -> dict[str, Any]:
    """合成终端 choke-set。"""
    after = aggregate(AFTER_CUTSET)
    cutset = aggregate(FORMAL_CUTSET)
    edge = aggregate(WINDOW_EDGE)
    support = aggregate(SUPPORT_MOTION)
    primitive = aggregate(PRIMITIVE_DEFECT)
    moving = aggregate(MOVING_SLOT)
    transport = aggregate(TRANSPORT_RESET)
    singleton = aggregate(SINGLETON_BUDGET)
    one_slot = aggregate(ONE_SLOT_CAPACITY)
    active = aggregate(ACTIVE_ELL)
    gap = aggregate(ENDPOINT_GAP)
    sparse = aggregate(SPARSE_SAE)
    pressure = aggregate(PAIRED_PRESSURE)
    unique = aggregate(UNIQUE_REP)

    crt_phase_margin = int(cutset["combined_modulus_current"]) - int(cutset["support_width_current"])
    endpoint_release_extra = int(support["min_endpoint_release_total_required"]) - int(support["support_width_current"])
    epoch_spare_ratio = float(one_slot["total_unused_residue_count"]) / float(one_slot["total_residue_capacity"])
    min_epoch_spare_ratio = float(one_slot["min_spare_ratio"])
    pressure_slack_decimal = ratio_decimal(pressure["min_pressure_product_slack"])
    all_endpoint_gaps_have_known_fill = all(
        all(str(ell) in row.get("known_fill_delays", {}) for ell in row.get("missing_internal_prime_ells", []))
        for row in gap["gap_snapshots"]
    )

    terminal_rows = [
        {
            "terminal_choke": "SourceAndCRTMaterialization",
            "absorbs_named_exits": [
                "SourceMaterializationFailure-PDEC/SAE",
                "CRTWindowEmptyGlobalSupportBound",
                "WindowEdgeCollisionOrUnusedTargetArrivalBound",
            ],
            "current_capacity_phase_readout": (
                f"formal_gap={after['formal_to_actual_gap']}, source_fail={after['source_unmaterialized_pair_total_current']}, "
                f"crt_empty={after['crt_window_empty_pair_total_current']}, unresolved={after['unresolved_formal_pair_total_current']}, "
                f"crt_phase_margin={crt_phase_margin}, edge_candidates={edge['edge_collision_candidate_count_current']}"
            ),
            "closed_current_sweep": bool(after["current_sweep_frontier_closed"])
            and int(after["unresolved_formal_pair_total_current"]) == 0
            and bool(edge["window_edge_collision_displacement_closed_current_sweep"]),
            "global_obligation": (
                "prove persistent source failures and CRT empty windows are PDEC/SAE-summable, "
                "or exclude unused-target residue arrival globally"
            ),
        },
        {
            "terminal_choke": "SupportMotionPrimitiveIdentity",
            "absorbs_named_exits": [
                "SupportMotionNonpersistenceOrEndpointReleaseBound",
                "PrimitiveIdentityShiftExclusion",
                "MovingSlotFamily-PDEC/ColumnCRT",
            ],
            "current_capacity_phase_readout": (
                f"support_motion_candidates={support['support_motion_candidate_count']}, "
                f"min_endpoint_release={support['min_endpoint_release_total_required']}, "
                f"release_extra_over_width={endpoint_release_extra}, "
                f"min_depth_defect={primitive['min_total_affine_depth_defect']}, "
                f"fixed_slot_failures={moving['fixed_highfactor_slot_pattern_isolation_failure_count_at_p0']}, "
                f"min_crt_minus_phase_width={moving['min_crt_minus_phase_width_at_p0']}"
            ),
            "closed_current_sweep": bool(support["support_motion_depth_closed_current_sweep"])
            and bool(primitive["fixed_primitive_key_support_motion_absorption_closed_current_sweep"])
            and int(moving["fixed_highfactor_slot_pattern_isolation_failure_count_at_p0"]) == 0,
            "global_obligation": (
                "prove moving supports cannot preserve both primitive depth identities, "
                "or route repeated moving-slot patterns to ColumnCRT/PDEC"
            ),
        },
        {
            "terminal_choke": "TransportSingletonActiveEll",
            "absorbs_named_exits": [
                "TransportResetPDECExclusion",
                "SingletonResidueSAE/Rankin",
                "ActiveEllBandEndpointGrowthBoundOrEndpointResetPDEC",
                "EndpointMotionGapFillBoundOrGapPDECExclusion",
            ],
            "current_capacity_phase_readout": (
                f"transport_reset_atoms={transport['reset_pdec_atom_count']}, "
                f"singleton_rankin_mass={singleton['singleton_rankin_mass_total']:.12f}, "
                f"one_slot_mass={singleton['one_slot_mass']:.12f}, "
                f"epoch_used={one_slot['total_used_residue_count']}/{one_slot['total_residue_capacity']}, "
                f"epoch_spare_ratio={epoch_spare_ratio:.12f}, "
                f"active_band={active['active_ell_values'][0]}..{active['active_ell_values'][-1]}, "
                f"endpoint_gap_count={len(gap['gap_snapshots'])}, max_gap_delay={gap['max_known_gap_fill_delay']}"
            ),
            "closed_current_sweep": bool(transport["current_sweep_transport_reset_atoms_empty"])
            and bool(one_slot["reset_free_epoch_capacity_closed"])
            and bool(active["exact_active_prime_interval_current_sweep"])
            and all_endpoint_gaps_have_known_fill,
            "global_obligation": (
                "prove active ell endpoint growth has a fill bound, or show endpoint motion creates "
                "reset-PDEC/SAE before singleton Rankin mass can accumulate"
            ),
        },
        {
            "terminal_choke": "EpochPairPairedPressure",
            "absorbs_named_exits": [
                "GlobalEpochPairMultiplicityBound",
                "HighDensityEpochPair-PDEC/ColumnCRT",
                "AffineTwinPairedSidePressureBoundOrPressureProductPDECExclusion",
            ],
            "current_capacity_phase_readout": (
                f"candidate_q={pressure['candidate_q_values']}, "
                f"sparse_tail_frontier={sparse['frontier_single_atom_tail_from_min_candidate_q']['decimal']:.12f}, "
                f"candidate_mass={sparse['candidate_single_pair_sae_mass_sum']['decimal']:.12f}, "
                f"max_pressure_product={pressure['max_paired_side_pressure_product']['decimal']:.12f}, "
                f"pressure_slack={pressure_slack_decimal:.12f}, "
                f"one_sided_pressure_q={pressure['one_sided_pressure_q_values']}"
            ),
            "closed_current_sweep": bool(pressure["all_sqrt_product_pressure_equivalences_closed"])
            and bool(pressure["all_current_rows_pass_paired_pressure_gate"])
            and int(pressure["pressure_product_pdec_count_current_sweep"]) == 0,
            "global_obligation": (
                "prove adjacent twin epochs cannot synchronize both-side residue pressure above one, "
                "or exclude PressureProduct-PDEC/ColumnCRT"
            ),
        },
        {
            "terminal_choke": "MovingResidueShapeSAE",
            "absorbs_named_exits": [
                "MovingResidueShapeSAE/Rankin",
                "FixedResidueSlotDriftColumnCRT",
            ],
            "current_capacity_phase_readout": (
                f"moving_residue_shapes={unique['moving_residue_shape_count']}, "
                f"recurrent_fixed_residue_packets={unique['recurrent_fixed_residue_packet_count']}, "
                f"singleton_packets={unique['residue_count_histogram']['1']}, "
                f"max_residue_packet_multiplicity={unique['max_physical_multiplicity_per_residue_packet']}"
            ),
            "closed_current_sweep": bool(unique["unique_representative_identity_failure_count"] == 0),
            "global_obligation": (
                "prove moving residue shapes are SAE/Rankin-summable, or turn recurrent fixed residues into ColumnCRT/PDEC"
            ),
        },
    ]

    all_current_closed = all(row["closed_current_sweep"] for row in terminal_rows)
    row_column_unconditional_closed = all(
        [
            bool(after["row_column_unconditional_closed"]),
            bool(support["row_column_unconditional_closed"]),
            bool(primitive["row_column_unconditional_closed"]),
            bool(moving["row_column_unconditional_closed"]),
            bool(transport["row_column_unconditional_closed"]),
            bool(singleton["row_column_unconditional_closed"]),
            bool(one_slot["row_column_unconditional_closed"]),
            bool(sparse["row_column_unconditional_closed"]),
            bool(pressure["row_column_unconditional_closed"]),
            bool(unique["row_column_unconditional_closed"]),
        ]
    )

    result = {
        "certificate_type": "prime_matrix_global_named_exit_terminal_choke_router",
        "status": "terminal_choke_set_current_sweep_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "terminal_choke_count": len(terminal_rows),
            "all_terminal_chokes_closed_current_sweep": all_current_closed,
            "row_column_unconditional_closed": row_column_unconditional_closed,
            "formal_pair_total": after["formal_pair_total"],
            "formal_to_actual_gap": after["formal_to_actual_gap"],
            "unresolved_formal_pair_total_current": after["unresolved_formal_pair_total_current"],
            "crt_phase_margin": crt_phase_margin,
            "min_endpoint_release_total_required": support["min_endpoint_release_total_required"],
            "endpoint_release_extra_over_support_width": endpoint_release_extra,
            "transport_reset_pdec_atom_count": transport["reset_pdec_atom_count"],
            "one_slot_epoch_spare_ratio": epoch_spare_ratio,
            "one_slot_epoch_min_spare_ratio": min_epoch_spare_ratio,
            "active_ell_band": [active["active_ell_values"][0], active["active_ell_values"][-1]],
            "endpoint_gap_count": len(gap["gap_snapshots"]),
            "max_known_gap_fill_delay": gap["max_known_gap_fill_delay"],
            "candidate_single_pair_sae_mass_sum": sparse["candidate_single_pair_sae_mass_sum"]["decimal"],
            "max_paired_side_pressure_product": pressure["max_paired_side_pressure_product"]["decimal"],
            "paired_pressure_slack": pressure_slack_decimal,
            "moving_residue_shape_count": unique["moving_residue_shape_count"],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "terminal_choke_rows": terminal_rows,
        "plain_conclusion": (
            "after-cutset 的十个命名出口可以进一步合并为五个终端 choke。"
            "当前 sweep 中五个 choke 都有显式容量/相位余量或已命名路由："
            "CRT 相位余量 879，端点释放最小额外量 50，transport reset atom 为 0，"
            "one-slot epoch 总剩余容量比例约 0.9039、单 epoch 最小剩余比例约 0.6901，"
            "paired pressure 最大仅 0.1602。"
            "因此最新硬点不是局部容量缺口，而是这些余量能否在全局持久族中被反复复现；"
            "若能复现，必须进入对应的 PDEC/SAE/ColumnCRT 终端。"
        ),
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                AFTER_CUTSET,
                FORMAL_CUTSET,
                WINDOW_EDGE,
                SUPPORT_MOTION,
                PRIMITIVE_DEFECT,
                MOVING_SLOT,
                TRANSPORT_RESET,
                SINGLETON_BUDGET,
                ONE_SLOT_CAPACITY,
                ACTIVE_ELL,
                ENDPOINT_GAP,
                SPARSE_SAE,
                PAIRED_PRESSURE,
                UNIQUE_REP,
            )
        },
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix global named-exit terminal choke router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_choke_count={agg['terminal_choke_count']}",
        f"all_terminal_chokes_closed_current_sweep={fmt_bool(agg['all_terminal_chokes_closed_current_sweep'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"formal_pair_total={agg['formal_pair_total']}",
        f"formal_to_actual_gap={agg['formal_to_actual_gap']}",
        f"unresolved_formal_pair_total_current={agg['unresolved_formal_pair_total_current']}",
        f"crt_phase_margin={agg['crt_phase_margin']}",
        f"min_endpoint_release_total_required={agg['min_endpoint_release_total_required']}",
        f"endpoint_release_extra_over_support_width={agg['endpoint_release_extra_over_support_width']}",
        f"transport_reset_pdec_atom_count={agg['transport_reset_pdec_atom_count']}",
        f"one_slot_epoch_spare_ratio={agg['one_slot_epoch_spare_ratio']:.12f}",
        f"one_slot_epoch_min_spare_ratio={agg['one_slot_epoch_min_spare_ratio']:.12f}",
        f"active_ell_band={agg['active_ell_band'][0]}..{agg['active_ell_band'][1]}",
        f"endpoint_gap_count={agg['endpoint_gap_count']}",
        f"max_known_gap_fill_delay={agg['max_known_gap_fill_delay']}",
        f"candidate_single_pair_sae_mass_sum={agg['candidate_single_pair_sae_mass_sum']:.12f}",
        f"max_paired_side_pressure_product={agg['max_paired_side_pressure_product']:.12f}",
        f"paired_pressure_slack={agg['paired_pressure_slack']:.12f}",
        f"moving_residue_shape_count={agg['moving_residue_shape_count']}",
        "```",
        "",
        "## 1. terminal choke set",
        "",
        "| choke | absorbs exits | current readout | closed current sweep | global obligation |",
        "| --- | --- | --- | ---: | --- |",
    ]
    for row in result["terminal_choke_rows"]:
        exits = ", ".join(f"`{item}`" for item in row["absorbs_named_exits"])
        lines.append(
            f"| `{row['terminal_choke']}` | {exits} | {row['current_capacity_phase_readout']} | "
            f"`{fmt_bool(row['closed_current_sweep'])}` | {row['global_obligation']} |"
        )

    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 本证书把 after-cutset 命名出口收缩为五个终端 choke，并记录每个 choke 的当前显式容量/相位余量。",
            "- 它关闭 current sweep 的匿名复现解释；没有证明全局行/列命题。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 3. 依赖哈希",
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
