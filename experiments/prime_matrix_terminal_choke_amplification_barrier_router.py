#!/usr/bin/env python3
"""生成终端 choke 的放大门槛证书。

用法示例：
  python3 experiments/prime_matrix_terminal_choke_amplification_barrier_router.py
  python3 -m json.tool data/prime-matrix-terminal-choke-amplification-barrier-ledger.json

输出：
  data/prime-matrix-terminal-choke-amplification-barrier-ledger.json
  docs/monograph/prime-matrix-terminal-choke-amplification-barrier-router.json
  docs/monograph/prime-matrix-terminal-choke-amplification-barrier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

TERMINAL_CHOKE = DATA / "prime-matrix-global-named-exit-terminal-choke-ledger.json"
FORMAL_CUTSET = DATA / "prime-matrix-formal-to-actual-global-cutset-ledger.json"
WINDOW_EDGE = DATA / "prime-matrix-affine-twin-window-edge-collision-ledger.json"
SUPPORT_MOTION = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
PRIMITIVE_DEFECT = DATA / "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
MOVING_SLOT = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-moving-slot-crt-phase-barrier-ledger.json"
ONE_SLOT_CAPACITY = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
PAIRED_PRESSURE = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-paired-side-pressure-ledger.json"
FILL_CATCHUP = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json"
TRANSPORT_RESET = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-terminal-choke-amplification-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-terminal-choke-amplification-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-terminal-choke-amplification-barrier-router.md"

NEXT_TARGET = "FiftyUnitCrossLockOrTerminalPDECExclusion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def aggregate(path: Path) -> dict[str, Any]:
    """读取账本 aggregate；没有 aggregate 时返回原对象。"""
    obj = load_json(path)
    return obj.get("aggregate", obj)


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def decimal(value: Any) -> float:
    """读取普通数或分数对象的十进制值。"""
    if isinstance(value, dict) and "decimal" in value:
        return float(value["decimal"])
    return float(value)


def build_result() -> dict[str, Any]:
    """构造放大门槛证书。"""
    terminal = aggregate(TERMINAL_CHOKE)
    cutset = aggregate(FORMAL_CUTSET)
    edge = aggregate(WINDOW_EDGE)
    support = aggregate(SUPPORT_MOTION)
    primitive = aggregate(PRIMITIVE_DEFECT)
    moving = aggregate(MOVING_SLOT)
    one_slot = aggregate(ONE_SLOT_CAPACITY)
    pressure = aggregate(PAIRED_PRESSURE)
    fill = aggregate(FILL_CATCHUP)
    transport = aggregate(TRANSPORT_RESET)
    one_slot_rows = load_json(ONE_SLOT_CAPACITY)["epoch_capacity_rows"]

    # 最拥挤的一槽 epoch 给出 singleton/transport 方向最窄容量门槛。
    tight_epoch = min(one_slot_rows, key=lambda row: float(row["spare_ratio"]))
    tight_epoch_overflow_new_units = int(tight_epoch["unused_residue_count"]) + 1
    tight_epoch_capacity_factor = float(tight_epoch["epoch_residue_capacity"]) / float(
        tight_epoch["used_residue_count"]
    )

    support_width = int(support["support_width_current"])
    endpoint_release_required = int(support["min_endpoint_release_total_required"])
    support_release_factor = endpoint_release_required / support_width
    support_extra_over_width = endpoint_release_required - support_width

    phase_jump_factor = int(cutset["min_empty_window_distance"]) / support_width
    crt_modulus_factor = int(cutset["combined_modulus_current"]) / support_width
    moving_slot_crt_factor = float(moving["min_highfactor_crt_modulus_at_p0"]) / float(
        moving["max_phase_width_at_p0"]
    )
    pressure_product = decimal(pressure["max_paired_side_pressure_product"])
    pressure_amplification_to_failure = 1.0 / pressure_product

    barrier_rows = [
        {
            "barrier": "CRTWindowPhaseJump",
            "terminal_choke": "SourceAndCRTMaterialization",
            "multiplicative_gap_to_failure": phase_jump_factor,
            "additive_gap_units": int(cutset["min_empty_window_distance"]),
            "current_readout": (
                f"min_empty_window_distance={cutset['min_empty_window_distance']}, "
                f"support_width={support_width}, modulus_factor={crt_modulus_factor:.6f}, "
                f"edge_candidates={edge['edge_collision_candidate_count_current']}"
            ),
            "route_if_persistent": "UnusedTargetArrival or WindowEdgeCollision-PDEC/SAE",
            "global_closed": False,
        },
        {
            "barrier": "OneSlotTransportOverflow",
            "terminal_choke": "TransportSingletonActiveEll",
            "multiplicative_gap_to_failure": tight_epoch_capacity_factor,
            "additive_gap_units": tight_epoch_overflow_new_units,
            "current_readout": (
                f"tight_epoch={tight_epoch['side']}:{tight_epoch['ell']}, "
                f"used={tight_epoch['used_residue_count']}, capacity={tight_epoch['epoch_residue_capacity']}, "
                f"unused={tight_epoch['unused_residue_count']}, "
                f"transport_reset_atoms={transport['reset_pdec_atom_count']}"
            ),
            "route_if_persistent": "TransportReset-PDEC or SingletonResidueSAE/Rankin",
            "global_closed": False,
        },
        {
            "barrier": "SupportEndpointRelease",
            "terminal_choke": "SupportMotionPrimitiveIdentity",
            "multiplicative_gap_to_failure": support_release_factor,
            "additive_gap_units": support_extra_over_width,
            "current_readout": (
                f"min_endpoint_release={endpoint_release_required}, support_width={support_width}, "
                f"min_depth_defect={primitive['min_total_affine_depth_defect']}, "
                f"breaks_both_identities={fmt_bool(primitive['all_support_motion_breaks_both_depth_identities'])}"
            ),
            "route_if_persistent": "PrimitiveIdentityShift-PDEC/SAE or MovingSlot-ColumnCRT",
            "global_closed": False,
        },
        {
            "barrier": "EpochPairPairedPressure",
            "terminal_choke": "EpochPairPairedPressure",
            "multiplicative_gap_to_failure": pressure_amplification_to_failure,
            "additive_gap_units": int(fill["min_extra_fill_required"]),
            "current_readout": (
                f"max_pressure_product={pressure_product:.12f}, "
                f"pressure_slack={decimal(pressure['min_pressure_product_slack']):.12f}, "
                f"fill_extra_range={fill['min_extra_fill_required']}..{fill['max_extra_fill_required']}, "
                f"min_fill_spare={fill['min_fill_epoch_spare_ratio']:.12f}"
            ),
            "route_if_persistent": "PressureProduct-PDEC/ColumnCRT or FillCatchUpMass-PDEC",
            "global_closed": False,
        },
        {
            "barrier": "FixedMovingSlotCRT",
            "terminal_choke": "SupportMotionPrimitiveIdentity",
            "multiplicative_gap_to_failure": moving_slot_crt_factor,
            "additive_gap_units": int(moving["min_crt_minus_phase_width_at_p0"]),
            "current_readout": (
                f"min_highfactor_crt_modulus={moving['min_highfactor_crt_modulus_at_p0']}, "
                f"max_phase_width={moving['max_phase_width_at_p0']}, "
                f"fixed_pattern_failures={moving['fixed_highfactor_slot_pattern_isolation_failure_count_at_p0']}"
            ),
            "route_if_persistent": "MovingSlotFamily-PDEC/ColumnCRT",
            "global_closed": False,
        },
    ]

    ranked = sorted(barrier_rows, key=lambda row: float(row["multiplicative_gap_to_failure"]))
    terminal_ranked = [row for row in ranked if row["barrier"] != "CRTWindowPhaseJump"]
    narrowest_terminal = terminal_ranked[0]
    fifty_unit_cross_lock = (
        tight_epoch_overflow_new_units == support_extra_over_width
        and support_extra_over_width == 50
    )

    result = {
        "certificate_type": "prime_matrix_terminal_choke_amplification_barrier_router",
        "status": "terminal_choke_amplification_barriers_current_sweep_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "barrier_count": len(barrier_rows),
            "row_column_unconditional_closed": False,
            "terminal_chokes_closed_current_sweep": bool(terminal["all_terminal_chokes_closed_current_sweep"]),
            "narrowest_barrier": ranked[0]["barrier"],
            "narrowest_barrier_factor": ranked[0]["multiplicative_gap_to_failure"],
            "narrowest_terminal_barrier": narrowest_terminal["barrier"],
            "narrowest_terminal_factor": narrowest_terminal["multiplicative_gap_to_failure"],
            "tight_epoch_key": f"{tight_epoch['side']}:{tight_epoch['ell']}",
            "tight_epoch_used": tight_epoch["used_residue_count"],
            "tight_epoch_capacity": tight_epoch["epoch_residue_capacity"],
            "tight_epoch_unused": tight_epoch["unused_residue_count"],
            "tight_epoch_overflow_new_units": tight_epoch_overflow_new_units,
            "support_endpoint_release_extra_units": support_extra_over_width,
            "fifty_unit_cross_lock": fifty_unit_cross_lock,
            "support_release_factor": support_release_factor,
            "crt_window_phase_jump_factor": phase_jump_factor,
            "crt_modulus_factor": crt_modulus_factor,
            "moving_slot_crt_factor": moving_slot_crt_factor,
            "pressure_amplification_to_failure": pressure_amplification_to_failure,
            "fill_min_extra_required": fill["min_extra_fill_required"],
            "fill_max_extra_required": fill["max_extra_fill_required"],
            "fill_total_min_rankin_mass_if_all_cross": fill[
                "total_min_new_fill_rankin_mass_required_if_all_candidates_cross"
            ]["decimal"],
            "transport_reset_pdec_atom_count": transport["reset_pdec_atom_count"],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "barrier_rows": barrier_rows,
        "ranked_barriers": [row["barrier"] for row in ranked],
        "plain_conclusion": (
            "五个终端 choke 的当前复现门槛可以量化为放大屏障。"
            "最窄 raw phase jump 是 CRT 空窗到支撑窗的 2 倍距离，但它不是独立终端，"
            "会立即进入 unused-target/window-edge 路由。真正终端侧最窄门槛是 "
            "one-slot transport overflow：最拥挤 epoch 为 minus:71，已用 22/71，"
            "还需 50 个新增 residue 才能越界；support motion 的最小端点释放额外量也正好是 50。"
            "因此最新显式交叉点是 fifty-unit cross-lock：反例链若继续复现，必须支付同一个 50-unit "
            "release/residue 包，或进入 reset/PDEC/SAE。"
        ),
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                TERMINAL_CHOKE,
                FORMAL_CUTSET,
                WINDOW_EDGE,
                SUPPORT_MOTION,
                PRIMITIVE_DEFECT,
                MOVING_SLOT,
                ONE_SLOT_CAPACITY,
                PAIRED_PRESSURE,
                FILL_CATCHUP,
                TRANSPORT_RESET,
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
        "# Prime Matrix terminal choke amplification barrier router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"barrier_count={agg['barrier_count']}",
        f"terminal_chokes_closed_current_sweep={fmt_bool(agg['terminal_chokes_closed_current_sweep'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"narrowest_barrier={agg['narrowest_barrier']}",
        f"narrowest_barrier_factor={agg['narrowest_barrier_factor']:.12f}",
        f"narrowest_terminal_barrier={agg['narrowest_terminal_barrier']}",
        f"narrowest_terminal_factor={agg['narrowest_terminal_factor']:.12f}",
        f"tight_epoch_key={agg['tight_epoch_key']}",
        f"tight_epoch_used={agg['tight_epoch_used']}",
        f"tight_epoch_capacity={agg['tight_epoch_capacity']}",
        f"tight_epoch_unused={agg['tight_epoch_unused']}",
        f"tight_epoch_overflow_new_units={agg['tight_epoch_overflow_new_units']}",
        f"support_endpoint_release_extra_units={agg['support_endpoint_release_extra_units']}",
        f"fifty_unit_cross_lock={fmt_bool(agg['fifty_unit_cross_lock'])}",
        f"support_release_factor={agg['support_release_factor']:.12f}",
        f"crt_window_phase_jump_factor={agg['crt_window_phase_jump_factor']:.12f}",
        f"moving_slot_crt_factor={agg['moving_slot_crt_factor']:.12f}",
        f"pressure_amplification_to_failure={agg['pressure_amplification_to_failure']:.12f}",
        f"fill_total_min_rankin_mass_if_all_cross={agg['fill_total_min_rankin_mass_if_all_cross']:.12f}",
        f"transport_reset_pdec_atom_count={agg['transport_reset_pdec_atom_count']}",
        "```",
        "",
        "## 1. 放大屏障表",
        "",
        "| barrier | terminal choke | factor | additive units | current readout | route if persistent |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]
    for row in result["barrier_rows"]:
        lines.append(
            f"| `{row['barrier']}` | `{row['terminal_choke']}` | "
            f"{row['multiplicative_gap_to_failure']:.12f} | {row['additive_gap_units']} | "
            f"{row['current_readout']} | `{row['route_if_persistent']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 排序",
            "",
            "```text",
            " -> ".join(result["ranked_barriers"]),
            "```",
            "",
            "## 3. 证明边界",
            "",
            "- 本证书只量化 terminal choke 的当前放大门槛，不证明全局行/列命题。",
            "- 最窄终端接口是 one-slot transport overflow；它与 support endpoint release 共享 50-unit 门槛。",
            f"- 下一主攻点：`{agg['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
