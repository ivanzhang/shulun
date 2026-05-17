#!/usr/bin/env python3
"""生成 fifty-unit cross-lock 的载体分离与跨载体同步证书。

用法示例：
  python3 experiments/prime_matrix_fifty_unit_cross_lock_carrier_separation_router.py
  python3 -m json.tool data/prime-matrix-fifty-unit-cross-lock-carrier-separation-ledger.json

输出：
  data/prime-matrix-fifty-unit-cross-lock-carrier-separation-ledger.json
  docs/monograph/prime-matrix-fifty-unit-cross-lock-carrier-separation-router.json
  docs/monograph/prime-matrix-fifty-unit-cross-lock-carrier-separation-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

AMPLIFICATION = DATA / "prime-matrix-terminal-choke-amplification-barrier-ledger.json"
SUPPORT_MOTION = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
PRIMITIVE_DEFECT = DATA / "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
ONE_SLOT_CAPACITY = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-one-slot-residue-epoch-capacity-ledger.json"
)
ACTIVE_ONE_SLOT = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-active-one-slot-epoch-source-ledger.json"
)
SINGLETON_PROFILE = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json"
)
FILL_CATCHUP = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-fill-catchup-mass-budget-ledger.json"
)
TRANSPORT_RESET = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-transport-cell-reset-pdec-ledger.json"
)

OUT_LEDGER = DATA / "prime-matrix-fifty-unit-cross-lock-carrier-separation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-fifty-unit-cross-lock-carrier-separation-router.json"
OUT_MD = DOCS / "prime-matrix-fifty-unit-cross-lock-carrier-separation-router.md"

NEXT_TARGET = "CrossCarrierFiftyUnitSynchronizationPDECOrSAE"


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


def find_row(rows: list[dict[str, Any]], **criteria: Any) -> dict[str, Any]:
    """按精确字段匹配单行。"""
    for row in rows:
        if all(row.get(key) == value for key, value in criteria.items()):
            return row
    raise KeyError(f"missing row for {criteria!r}")


def intervals_overlap(left: tuple[int, int], right: tuple[int, int]) -> bool:
    """判断两个闭区间是否相交。"""
    return max(left[0], right[0]) <= min(left[1], right[1])


def ceiling_div(num: int, den: int) -> int:
    """整数上取整。"""
    return -(-num // den)


def build_result() -> dict[str, Any]:
    """构造载体分离与跨载体同步证书。"""
    amplification = aggregate(AMPLIFICATION)
    support_obj = load_json(SUPPORT_MOTION)
    primitive_obj = load_json(PRIMITIVE_DEFECT)
    capacity_obj = load_json(ONE_SLOT_CAPACITY)
    active_obj = load_json(ACTIVE_ONE_SLOT)
    profile_obj = load_json(SINGLETON_PROFILE)
    fill_obj = load_json(FILL_CATCHUP)
    transport = aggregate(TRANSPORT_RESET)

    # 取上一证书暴露出的最窄 support 原子和最拥挤 one-slot epoch。
    support_atom_key = support_obj["aggregate"]["narrowest_endpoint_release_atom"]["source_pair_key"]
    support_atom = find_row(support_obj["support_motion_rows"], source_pair_key=support_atom_key)
    primitive_atom = find_row(
        primitive_obj["support_motion_primitive_defect_rows"],
        source_pair_key=support_atom_key,
    )
    tight_side, tight_ell_raw = str(amplification["tight_epoch_key"]).split(":")
    tight_ell = int(tight_ell_raw)
    tight_epoch = find_row(capacity_obj["epoch_capacity_rows"], side=tight_side, ell=tight_ell)
    active_ell = find_row(active_obj["active_ell_source_rows"], ell=tight_ell)
    fill_q31 = find_row(fill_obj["fill_catchup_mass_budget_rows"], q=support_atom["q"])
    tight_shape_key = f"size=1|side={tight_side}|ells={tight_ell}"
    tight_shape = find_row(
        profile_obj["top_singleton_shapes_by_count"],
        normal_shape_key=tight_shape_key,
    )

    support_q = int(support_atom["q"])
    support_width = int(support_atom["support_width"])
    support_total_release = int(support_atom["endpoint_release_total_required"])
    support_extra_over_width = support_total_release - support_width
    overflow_new_units = int(tight_epoch["unused_residue_count"]) + 1
    p_delay = int(support_atom["p_delay"])
    combined_modulus = math.lcm(support_q, tight_ell)
    p_delay_gcd_epoch = math.gcd(p_delay, tight_ell)
    residue_increment_mod_epoch = p_delay % tight_ell
    anchor_p = int(support_atom["generator_p"])
    anchor_p_mod_epoch = anchor_p % tight_ell
    fifty_residue_ramp = [
        (anchor_p_mod_epoch + index * residue_increment_mod_epoch) % tight_ell
        for index in range(overflow_new_units)
    ]
    fifty_distinct_residue_count = len(set(fifty_residue_ramp))

    support_p_band = (
        min(int(support_atom["nearest_representative"]), anchor_p),
        max(int(support_atom["nearest_representative"]), anchor_p),
    )
    tight_p_range = (int(tight_epoch["p_min"]), int(tight_epoch["p_max"]))
    support_phase_interval = tuple(int(value) for value in support_atom["support_interval"])
    steps_to_enter_epoch_range = ceiling_div(max(0, tight_p_range[0] - anchor_p), p_delay)
    first_enter_epoch_p = anchor_p + steps_to_enter_epoch_range * p_delay
    last_fifty_block_p = first_enter_epoch_p + (overflow_new_units - 1) * p_delay
    max_fixed_delay_steps_inside_epoch = (tight_p_range[1] - anchor_p) // p_delay

    same_q_or_ell = support_q == tight_ell
    same_side_taxonomy = str(support_atom["window_side"]) == tight_side
    same_p_band = intervals_overlap(support_p_band, tight_p_range)
    same_support_phase_band = intervals_overlap(support_phase_interval, tight_p_range)
    direct_same_carrier_contradiction = (
        same_q_or_ell and same_side_taxonomy and same_p_band and same_support_phase_band
    )
    fifty_step_ramp_is_reset_free = (
        p_delay_gcd_epoch == 1 and fifty_distinct_residue_count == overflow_new_units
    )
    fifty_step_block_can_fit_current_epoch_p_range = (
        first_enter_epoch_p >= tight_p_range[0] and last_fifty_block_p <= tight_p_range[1]
    )
    if_fifty_new_residues_sync_then_one_slot_overflow = (
        int(tight_epoch["used_residue_count"]) + overflow_new_units
        > int(tight_epoch["epoch_residue_capacity"])
    )

    route_rows = [
        {
            "gate": "SameCarrierDirectContradiction",
            "closed_current_sweep": not direct_same_carrier_contradiction,
            "readout": (
                f"support q={support_q}, epoch ell={tight_ell}, "
                f"support_p_band={support_p_band}, epoch_p_range={tight_p_range}"
            ),
            "remaining_if_fails": "DirectSameCarrierCRTContradiction",
        },
        {
            "gate": "FixedDelayResetFreeBeforeFifty",
            "closed_current_sweep": fifty_step_ramp_is_reset_free,
            "readout": (
                f"p_delay={p_delay}, p_delay mod {tight_ell}={residue_increment_mod_epoch}, "
                f"gcd={p_delay_gcd_epoch}, distinct_first_50={fifty_distinct_residue_count}"
            ),
            "remaining_if_fails": "TransportResetPDECOrMovingCarrierColumnCRT",
        },
        {
            "gate": "FiftyBlockRangeAdmission",
            "closed_current_sweep": fifty_step_block_can_fit_current_epoch_p_range,
            "readout": (
                f"first_enter_epoch_p={first_enter_epoch_p}, "
                f"last_fifty_block_p={last_fifty_block_p}, epoch_p_range={tight_p_range}"
            ),
            "remaining_if_fails": "SupportMotionRangeSlipOrUnusedTargetArrivalSAE",
        },
        {
            "gate": "FiftyNewResidueOverflowIfSynchronized",
            "closed_current_sweep": if_fifty_new_residues_sync_then_one_slot_overflow,
            "readout": (
                f"used={tight_epoch['used_residue_count']}, "
                f"new_units={overflow_new_units}, capacity={tight_epoch['epoch_residue_capacity']}"
            ),
            "remaining_if_fails": "OneSlotCapacityNoOverflow",
        },
        {
            "gate": "NewnessAgainstExistingEpochResidues",
            "closed_current_sweep": False,
            "readout": (
                "capacity ledger records used count and sample, but not a full existing-residue set; "
                "global proof must show the 50 arrivals are new or route duplicates to reset/PDEC"
            ),
            "remaining_if_fails": "TransportResetPDECOrSingletonResidueSAE",
        },
    ]

    result = {
        "certificate_type": "prime_matrix_fifty_unit_cross_lock_carrier_separation_router",
        "status": "fifty_unit_cross_lock_carrier_separated_crosscarrier_sync_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": {
            "row_column_unconditional_closed": False,
            "previous_hardpoint": "FiftyUnitCrossLockOrTerminalPDECExclusion",
            "support_atom_key": support_atom_key,
            "support_q": support_q,
            "support_generator_residue": support_atom["generator_residue"],
            "support_fill_residue": support_atom["fill_residue"],
            "support_window_side": support_atom["window_side"],
            "support_nearest_representative": support_atom["nearest_representative"],
            "support_generator_p": support_atom["generator_p"],
            "support_p_band": list(support_p_band),
            "support_width": support_width,
            "support_endpoint_release_total": support_total_release,
            "support_endpoint_release_extra_units": support_extra_over_width,
            "support_p_delay": p_delay,
            "support_source_primitive_key": primitive_atom["source_primitive_key"],
            "support_source_gap_fill_pair_key": primitive_atom["source_gap_fill_pair_key"],
            "tight_epoch_key": f"{tight_side}:{tight_ell}",
            "tight_epoch_side": tight_side,
            "tight_epoch_ell": tight_ell,
            "tight_epoch_used": tight_epoch["used_residue_count"],
            "tight_epoch_capacity": tight_epoch["epoch_residue_capacity"],
            "tight_epoch_unused": tight_epoch["unused_residue_count"],
            "tight_epoch_overflow_new_units": overflow_new_units,
            "tight_epoch_p_range": list(tight_p_range),
            "tight_shape_singleton_count": tight_shape["singleton_count"],
            "tight_shape_min_margin": tight_shape["min_margin"],
            "tight_shape_min_crt_minus_phase_width": tight_shape["min_crt_minus_phase_width"],
            "active_ell_side_count": active_ell["side_count"],
            "active_ell_used_residue_count": active_ell["used_residue_count"],
            "active_ell_capacity": active_ell["capacity"],
            "same_q_or_ell": same_q_or_ell,
            "same_side_taxonomy": same_side_taxonomy,
            "same_p_band": same_p_band,
            "same_support_phase_band": same_support_phase_band,
            "direct_same_carrier_contradiction": direct_same_carrier_contradiction,
            "cross_carrier_sync_required": not direct_same_carrier_contradiction,
            "combined_carrier_modulus": combined_modulus,
            "combined_modulus_over_support_width": combined_modulus / support_width,
            "combined_modulus_over_fifty_units": combined_modulus / overflow_new_units,
            "p_delay_mod_tight_epoch": residue_increment_mod_epoch,
            "p_delay_gcd_tight_epoch": p_delay_gcd_epoch,
            "anchor_p_mod_tight_epoch": anchor_p_mod_epoch,
            "fifty_residue_ramp_sample": fifty_residue_ramp[:16],
            "fifty_distinct_residue_count": fifty_distinct_residue_count,
            "fifty_step_ramp_is_reset_free": fifty_step_ramp_is_reset_free,
            "steps_to_enter_epoch_range": steps_to_enter_epoch_range,
            "first_enter_epoch_p": first_enter_epoch_p,
            "last_fifty_block_p": last_fifty_block_p,
            "max_fixed_delay_steps_inside_epoch": max_fixed_delay_steps_inside_epoch,
            "fifty_step_block_can_fit_current_epoch_p_range": fifty_step_block_can_fit_current_epoch_p_range,
            "if_fifty_new_residues_sync_then_one_slot_overflow": if_fifty_new_residues_sync_then_one_slot_overflow,
            "newness_against_existing_epoch_residues_proved": False,
            "transport_reset_pdec_atom_count": transport["reset_pdec_atom_count"],
            "fill_q31_realized_current_sweep": fill_q31["realized_current_sweep"],
            "fill_q31_min_extra_fill": fill_q31["min_extra_fill_in_minimal_routes"],
            "hardpoint_after_router": NEXT_TARGET,
            "next_direct_attack_target": NEXT_TARGET,
        },
        "route_rows": route_rows,
        "plain_conclusion": (
            "50-unit cross-lock 不是同一载体上的直接矛盾：support 原子在 q=31/source_pair=19:12 "
            "和 P≈2687 的 below 端点释放上，而最拥挤一槽 epoch 是 minus:71 且 P 区间为 "
            "4177..9257。二者要同步必须穿过互素模数 31*71=2201 的跨载体 CRT 门。"
            "固定 p_delay=80 在模 71 上为 9，前 50 步互异且可放入当前 71-epoch P 区间；"
            "所以短路的重复 residue 矛盾不会自动出现。若这 50 个到达都作为新 residue 同步进入 "
            "minus:71，则 22+50>71，立即越过 one-slot 容量；若不是新 residue 或不能同步，"
            "就分别回到 TransportReset-PDEC、SingletonResidue-SAE、SupportMotion/UnusedTarget "
            "或 MovingCarrier-ColumnCRT 出口。"
        ),
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                AMPLIFICATION,
                SUPPORT_MOTION,
                PRIMITIVE_DEFECT,
                ONE_SLOT_CAPACITY,
                ACTIVE_ONE_SLOT,
                SINGLETON_PROFILE,
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
        "# Prime Matrix fifty-unit cross-lock carrier separation router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"support_atom_key={agg['support_atom_key']}",
        f"support_q={agg['support_q']}",
        f"support_generator_residue={agg['support_generator_residue']}",
        f"support_fill_residue={agg['support_fill_residue']}",
        f"support_generator_p={agg['support_generator_p']}",
        f"support_endpoint_release_extra_units={agg['support_endpoint_release_extra_units']}",
        f"tight_epoch_key={agg['tight_epoch_key']}",
        f"tight_epoch_used={agg['tight_epoch_used']}",
        f"tight_epoch_capacity={agg['tight_epoch_capacity']}",
        f"tight_epoch_overflow_new_units={agg['tight_epoch_overflow_new_units']}",
        f"same_q_or_ell={fmt_bool(agg['same_q_or_ell'])}",
        f"same_side_taxonomy={fmt_bool(agg['same_side_taxonomy'])}",
        f"same_p_band={fmt_bool(agg['same_p_band'])}",
        f"direct_same_carrier_contradiction={fmt_bool(agg['direct_same_carrier_contradiction'])}",
        f"cross_carrier_sync_required={fmt_bool(agg['cross_carrier_sync_required'])}",
        f"combined_carrier_modulus={agg['combined_carrier_modulus']}",
        f"combined_modulus_over_fifty_units={agg['combined_modulus_over_fifty_units']:.12f}",
        f"p_delay_mod_tight_epoch={agg['p_delay_mod_tight_epoch']}",
        f"p_delay_gcd_tight_epoch={agg['p_delay_gcd_tight_epoch']}",
        f"fifty_distinct_residue_count={agg['fifty_distinct_residue_count']}",
        f"fifty_step_ramp_is_reset_free={fmt_bool(agg['fifty_step_ramp_is_reset_free'])}",
        f"first_enter_epoch_p={agg['first_enter_epoch_p']}",
        f"last_fifty_block_p={agg['last_fifty_block_p']}",
        f"fifty_step_block_can_fit_current_epoch_p_range={fmt_bool(agg['fifty_step_block_can_fit_current_epoch_p_range'])}",
        f"if_fifty_new_residues_sync_then_one_slot_overflow={fmt_bool(agg['if_fifty_new_residues_sync_then_one_slot_overflow'])}",
        f"newness_against_existing_epoch_residues_proved={fmt_bool(agg['newness_against_existing_epoch_residues_proved'])}",
        f"next_direct_attack_target={agg['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 分流门",
        "",
        "| gate | closed current sweep | readout | remaining if fails |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["route_rows"]:
        lines.append(
            f"| `{row['gate']}` | `{fmt_bool(row['closed_current_sweep'])}` | "
            f"{row['readout']} | `{row['remaining_if_fails']}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 证明边界",
            "",
            "- 本证书关闭的是同载体直接矛盾路线；它没有证明行/列命题。",
            "- 固定 `p_delay=80` 在 `mod 71` 上前 50 步互异，因此重复 residue 的短路 PDEC 不能免费使用。",
            "- 真正剩余是证明这 50 个跨载体到达若持久同步则必须为新 residue 并越界，或把非新/不同步形态登记为 PDEC/SAE/ColumnCRT。",
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
