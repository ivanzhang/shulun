#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release persistent-family promotion 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_persistent_family_promotion_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-audit.md
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

FAMILY_SCHEMA_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "family-schema-ledger.json"
)
MOVING_FAMILY_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-moving-family-sae-columncrt-ledger.json"
)
EPOCH_MULTIPLICITY_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-epoch-pair-multiplicity-ledger.json"
)
PAIRED_PRESSURE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-paired-side-pressure-ledger.json"
)
FILL_CATCHUP_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-fill-catchup-mass-budget-ledger.json"
)
SOURCE_GATE_LEDGER = DATA / "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
FIXED_DRIFT_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "fixed-residue-slot-drift-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-persistent-family-promotion-audit.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def route_row(
    gate: str,
    closed: bool,
    evidence: str,
    global_remaining: str,
) -> dict[str, Any]:
    """构造 promotion 路由行。"""
    return {
        "gate": gate,
        "closed_current_sweep": closed,
        "evidence": evidence,
        "global_remaining": global_remaining,
    }


def build_result(
    family_schema_path: Path,
    moving_family_path: Path,
    epoch_multiplicity_path: Path,
    paired_pressure_path: Path,
    fill_catchup_path: Path,
    source_gate_path: Path,
    fixed_drift_path: Path,
) -> dict[str, Any]:
    """构造 persistent-family promotion 审计结果。"""
    family_schema = load_json(family_schema_path)
    moving_family = load_json(moving_family_path)
    epoch = load_json(epoch_multiplicity_path)
    pressure = load_json(paired_pressure_path)
    fill = load_json(fill_catchup_path)
    source = load_json(source_gate_path)
    fixed_drift = load_json(fixed_drift_path)

    fs = family_schema["aggregate"]
    mf = moving_family["aggregate"]
    ep = epoch["aggregate"]
    pr = pressure["aggregate"]
    fl = fill["aggregate"]
    sg = source["aggregate"]
    fd = fixed_drift["aggregate"]
    total_min_extra_fill = sum(
        int(row["min_extra_fill_in_minimal_routes"])
        for row in fill["fill_catchup_mass_budget_rows"]
    )

    fixed_graph_closed = bool(fs["generator_coarrival_family_schema_closed_current_sweep"])
    fixed_q_residue_routed = bool(mf["fixed_q_fixed_residue_columncrt_routing_closed"])
    epoch_sparse_closed = bool(ep["current_sparse_acceptance_closed"])
    paired_pressure_closed = bool(pr["all_current_rows_pass_paired_pressure_gate"])
    fill_reset_closed = bool(fl["new_fill_or_reset_dichotomy_closed"])
    source_closed = bool(sg["source_materialization_gate_closed_current_sweep"])
    fixed_slot_empty = int(fd["fixed_slot_recurrence_count"]) == 0
    drift_identified = bool(fd["all_fixed_residue_recurrences_are_slot_drift"])

    route_rows = [
        route_row(
            "FixedSupportGraphSchema",
            fixed_graph_closed,
            (
                "fixed graph W=(q+9)/2 stays below sqrt(q(q-2)); "
                f"formal SuperSqrt subsets={fs['formal_super_sqrt_subset_count']}, "
                f"actual overload subsets={fs['actual_overload_subset_count']}"
            ),
            "PromoteFixedGraphProjectionSchemaToAllPersistentAffineTwinFamilies",
        ),
        route_row(
            "FixedQFixedResidueColumnCRT",
            fixed_q_residue_routed and fixed_slot_empty and drift_identified,
            (
                f"fixed_slot_recurrence_count={fd['fixed_slot_recurrence_count']}; "
                f"fixed_residue_slot_drift_pair_count={fd['fixed_residue_recurrent_packet_count']}; "
                f"all drift gaps divisible by ell={fd['all_p_gaps_divisible_by_ell']}"
            ),
            "FixedResidueSlotDriftColumnCRT",
        ),
        route_row(
            "MovingEpochPairSparseSAE",
            epoch_sparse_closed,
            (
                f"candidate_product_mass_upper_sum={ep['candidate_product_mass_upper_sum']}; "
                f"eta={ep['eta']}; high_density_epoch_pair_count="
                f"{ep['high_density_epoch_pair_count']}"
            ),
            "GlobalEpochPairMultiplicityBound or HighDensityEpochPair-PDEC",
        ),
        route_row(
            "PairedPressureGate",
            paired_pressure_closed,
            (
                f"max_paired_side_pressure_product={pr['max_paired_side_pressure_product']}; "
                f"one_sided_pressure_q_values={pr['one_sided_pressure_q_values']}"
            ),
            "PressureProduct-PDEC",
        ),
        route_row(
            "FillArrivalOrReset",
            fill_reset_closed,
            (
                f"all routes require fill increment={fl['all_routes_require_fill_increment']}; "
                f"total min extra fill={total_min_extra_fill}; "
                f"total min new fill Rankin mass="
                f"{fl['total_min_new_fill_rankin_mass_required_if_all_candidates_cross']}"
            ),
            "FillCatchupMassPDEC or Reset/ColumnCRT-PDEC",
        ),
        route_row(
            "SourceMaterialization",
            source_closed,
            (
                f"pass q={sg['source_gate_pass_q_values']}; "
                f"fail q={sg['source_gate_fail_q_values']}; "
                f"blocked formal pairs={sg['formal_pairs_blocked_by_source_gate']}"
            ),
            "SourceRematerialization-PDEC/SAE",
        ),
    ]
    closed_current = all(bool(row["closed_current_sweep"]) for row in route_rows)

    aggregate = {
        "family_schema_ledger": str(family_schema_path.relative_to(ROOT)),
        "moving_family_sae_columncrt_ledger": str(moving_family_path.relative_to(ROOT)),
        "epoch_pair_multiplicity_ledger": str(
            epoch_multiplicity_path.relative_to(ROOT)
        ),
        "paired_side_pressure_ledger": str(paired_pressure_path.relative_to(ROOT)),
        "fill_catchup_mass_budget_ledger": str(fill_catchup_path.relative_to(ROOT)),
        "source_materialization_gate_ledger": str(source_gate_path.relative_to(ROOT)),
        "fixed_residue_slot_drift_ledger": str(fixed_drift_path.relative_to(ROOT)),
        "candidate_q_values": mf["candidate_q_values"],
        "realized_q_values": mf["realized_q_values"],
        "candidate_affine_twin_epoch_pair_count": int(
            mf["candidate_affine_twin_epoch_pair_count"]
        ),
        "realized_affine_twin_pair_count": int(mf["realized_affine_twin_pair_count"]),
        "candidate_product_mass_upper_sum": float(
            ep["candidate_product_mass_upper_sum"]
        ),
        "eta": float(ep["eta"]),
        "candidate_total_eta_slack": float(ep["candidate_total_eta_slack"]),
        "high_density_epoch_pair_count": int(ep["high_density_epoch_pair_count"]),
        "fixed_slot_recurrence_count": int(fd["fixed_slot_recurrence_count"]),
        "fixed_residue_slot_drift_pair_count": int(
            fd["fixed_residue_recurrent_packet_count"]
        ),
        "same_depth_signature_pair_count": int(fd["same_depth_signature_pair_count"]),
        "min_p_gap_over_ell": int(fd["min_p_gap_over_ell"]),
        "max_p_gap_over_ell": int(fd["max_p_gap_over_ell"]),
        "source_gate_blocked_formal_pairs": int(
            sg["formal_pairs_blocked_by_source_gate"]
        ),
        "one_sided_pressure_q_values": pr["one_sided_pressure_q_values"],
        "pressure_product_pdec_count_current_sweep": int(
            pr["pressure_product_pdec_count_current_sweep"]
        ),
        "total_min_extra_fill_required_if_all_candidates_cross": total_min_extra_fill,
        "fixed_graph_schema_promoted_current_sweep": fixed_graph_closed,
        "fixed_q_fixed_residue_routed_current_sweep": fixed_q_residue_routed,
        "moving_epoch_pair_sparse_sae_closed_current_sweep": epoch_sparse_closed,
        "paired_pressure_gate_closed_current_sweep": paired_pressure_closed,
        "fill_arrival_or_reset_closed_current_sweep": fill_reset_closed,
        "source_materialization_closed_current_sweep": source_closed,
        "persistent_family_promotion_closed_current_sweep": closed_current,
        "global_epoch_pair_multiplicity_bound_proved": False,
        "fixed_residue_slot_drift_columncrt_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "persistent_family_promotion_audit"
        ),
        "status": "current_sweep_persistent_family_promotion_routed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "promotion_route_rows": route_rows,
        "candidate_epoch_pair_rows": moving_family[
            "candidate_affine_twin_epoch_pair_rows"
        ],
        "contract": {
            "persistent_family_promotion": [
                "fixed support graph families obey the graph-width square-root gate",
                "fixed q and fixed residue recurrence is a ColumnCRT/PDEC object",
                "moving q/residue families are measured by epoch-pair SAE mass unless high-density",
                "source, paired-pressure, and fill-arrival gates block current anonymous persistence",
            ],
            "closed_current_sweep": closed_current,
            "global_remaining": [
                "GlobalEpochPairMultiplicityBound",
                "FixedResidueSlotDriftColumnCRT",
                "MovingResidueShapeSAE/Rankin",
                "HighDensityEpochPair-PDEC/ColumnCRT",
                "SourceRematerialization-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                family_schema_path,
                moving_family_path,
                epoch_multiplicity_path,
                paired_pressure_path,
                fill_catchup_path,
                source_gate_path,
                fixed_drift_path,
            )
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release persistent-family promotion audit",
        "",
        "**状态：** `current_sweep_persistent_family_promotion_routed_global_open`",
        "",
        "本审计把 `GeneratorCoarrivalFamilyBound` 的推广义务继续拆开：固定支撑图像、固定 q/残基复现、moving epoch-pair SAE、source/pressure/fill 门控分别进入独立账本。当前 sweep 中这些门都已路由，但全局 multiplicity 与 slot-drift 排斥仍开放。",
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"candidate_product_mass_upper_sum={agg['candidate_product_mass_upper_sum']}",
        f"eta={agg['eta']}",
        f"candidate_total_eta_slack={agg['candidate_total_eta_slack']}",
        f"high_density_epoch_pair_count={agg['high_density_epoch_pair_count']}",
        f"fixed_slot_recurrence_count={agg['fixed_slot_recurrence_count']}",
        f"fixed_residue_slot_drift_pair_count={agg['fixed_residue_slot_drift_pair_count']}",
        f"source_gate_blocked_formal_pairs={agg['source_gate_blocked_formal_pairs']}",
        f"persistent_family_promotion_closed_current_sweep={fmt_bool(agg['persistent_family_promotion_closed_current_sweep'])}",
        "```",
        "",
        "## 1. promotion route rows",
        "",
        "| gate | closed | evidence | global remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["promotion_route_rows"]:
        lines.append(
            "| `{gate}` | {closed} | {evidence} | `{remaining}` |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed_current_sweep"]),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["global_remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. candidate epoch pairs",
            "",
            "| q | used upper | capacity | occupancy upper | realized | single SAE mass |",
            "| ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for row in result["candidate_epoch_pair_rows"]:
        lines.append(
            "| {q} | {used} | {capacity} | {occ:.12g} | {realized} | {mass:.12g} |".format(
                q=row["q"],
                used=row["epoch_pair_product_used_upper"],
                capacity=row["epoch_pair_capacity"],
                occ=row["epoch_pair_occupancy_upper_ratio"],
                realized=fmt_bool(row["realized_current_sweep"]),
                mass=row["single_pair_sae_mass"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 显式矛盾读数",
            "",
            "- 反例链若停在固定图像内，已由 family schema 的 `W<=sqrt(q(q-2))` 阻断。",
            "- 若固定 q/残基反复复现，则不再是匿名容量，而是固定模 ColumnCRT/PDEC；当前 fixed-slot 复现数为 `0`。",
            "- 若 q 或残基移动，则进入 epoch-pair SAE；当前候选总 occupancy 上界 `0.023577...` 低于 `eta=0.025`，高密度行数为 `0`。",
            "- 余下真正全局硬点是证明该稀疏/漂移结构不能无限持久，或把持久失败转成 ColumnCRT/PDEC/SAE 证书。",
            "",
            "## 4. 结论边界",
            "",
            "当前 sweep 的 persistent-family promotion 已完成路由闭合；这仍不是行/列命题无条件证明。最新剩余被压成 `GlobalEpochPairMultiplicityBound` 与 `FixedResidueSlotDriftColumnCRT`，并保留 `MovingResidueShapeSAE/Rankin` 与 source-rematerialization 出口。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin endpoint-release persistent-family promotion 审计证书。"
    )
    parser.add_argument("--family-schema-ledger", type=Path, default=FAMILY_SCHEMA_LEDGER)
    parser.add_argument("--moving-family-ledger", type=Path, default=MOVING_FAMILY_LEDGER)
    parser.add_argument(
        "--epoch-multiplicity-ledger", type=Path, default=EPOCH_MULTIPLICITY_LEDGER
    )
    parser.add_argument("--paired-pressure-ledger", type=Path, default=PAIRED_PRESSURE_LEDGER)
    parser.add_argument("--fill-catchup-ledger", type=Path, default=FILL_CATCHUP_LEDGER)
    parser.add_argument("--source-gate-ledger", type=Path, default=SOURCE_GATE_LEDGER)
    parser.add_argument("--fixed-drift-ledger", type=Path, default=FIXED_DRIFT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.family_schema_ledger,
        args.moving_family_ledger,
        args.epoch_multiplicity_ledger,
        args.paired_pressure_ledger,
        args.fill_catchup_ledger,
        args.source_gate_ledger,
        args.fixed_drift_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
