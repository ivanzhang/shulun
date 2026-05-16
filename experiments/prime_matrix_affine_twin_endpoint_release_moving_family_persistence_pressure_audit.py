#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release moving-family persistence pressure 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_moving_family_persistence_pressure_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-audit.md
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

MOVING_SLOT_ROUTE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json"
)
SOURCE_GATE_LEDGER = DATA / "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
EPOCH_MULTIPLICITY_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-epoch-pair-multiplicity-ledger.json"
)
PAIRED_PRESSURE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-paired-side-pressure-ledger.json"
)
THRESHOLD_ROUTE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-threshold-route-classifier-ledger.json"
)
FILL_CATCHUP_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-fill-catchup-mass-budget-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-audit.md"
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


def frac_from_obj(value: dict[str, Any]) -> Fraction:
    """从含 numerator/denominator 的对象读取分数。"""
    return Fraction(int(value["numerator"]), int(value["denominator"]))


def index_by_q(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立索引。"""
    return {int(row["q"]): row for row in rows}


def source_phase_defect(row: dict[str, Any]) -> dict[str, Any]:
    """抽取 source gate 的相位缺陷。"""
    if bool(row["source_gate_passed_current"]):
        return {
            "source_phase_defect_type": "exact_source_materialized",
            "p_delay_delta": 0,
            "failed_invariants": [],
        }
    vector = row.get("best_source_match_vector")
    if vector is None:
        return {
            "source_phase_defect_type": "gap_source_absent",
            "p_delay_delta": None,
            "failed_invariants": row["failed_invariants"],
        }
    return {
        "source_phase_defect_type": "wrong_source_signature",
        "p_delay_delta": vector["p_delay_delta"],
        "actual_p_delay": vector["actual_p_delay"],
        "expected_p_delay": vector["expected_p_delay"],
        "failed_invariants": row["failed_invariants"],
    }


def persistence_route(
    source_row: dict[str, Any],
    pressure_row: dict[str, Any],
    threshold_row: dict[str, Any],
) -> str:
    """给出单个 q 的 moving-family 持久复现路由。"""
    if not bool(source_row["source_gate_passed_current"]):
        return f"{source_row['route']}+FillArrivalOrReset"
    if bool(pressure_row["pressure_product_pdec_trigger_current_sweep"]):
        return "PressureProduct-PDEC"
    if bool(threshold_row["minimal_route_requires_fill_increment"]):
        return "RealizedGraphCap+FillArrivalOrReset"
    return "SparseSAEOrColumnCRT"


def family_row(
    q: int,
    source_row: dict[str, Any],
    epoch_row: dict[str, Any],
    pressure_row: dict[str, Any],
    threshold_row: dict[str, Any],
    fill_row: dict[str, Any],
) -> dict[str, Any]:
    """合并一个 q 的 source/pressure/threshold/fill 读数。"""
    min_fill_mass = frac_from_obj(fill_row["min_new_fill_rankin_mass_required"])
    pressure_product = frac_from_obj(pressure_row["paired_side_pressure_product"])
    pressure_slack = Fraction(1, 1) - pressure_product
    route = persistence_route(source_row, pressure_row, threshold_row)
    return {
        "q": q,
        "realized_current_sweep": bool(epoch_row["realized_current_sweep"]),
        "source_route": source_row["route"],
        "source_gate_passed_current": bool(source_row["source_gate_passed_current"]),
        "formal_pair_count": int(source_row["formal_pair_count"]),
        "formal_pairs_blocked_by_source_gate": int(
            source_row["formal_pairs_blocked_by_source_gate"]
        ),
        "source_phase_defect": source_phase_defect(source_row),
        "occupancy_upper_ratio": epoch_row["occupancy_upper_ratio"],
        "eta_slack_numerator": int(epoch_row["eta_slack_numerator"]),
        "high_density_epoch_pair_pdec_trigger": bool(
            epoch_row["high_density_epoch_pair_pdec_trigger"]
        ),
        "generator_side_pressure": pressure_row["generator_side_pressure"],
        "fill_side_pressure": pressure_row["fill_side_pressure"],
        "paired_side_pressure_product": pressure_row["paired_side_pressure_product"],
        "paired_pressure_product_slack": {
            "numerator": pressure_slack.numerator,
            "denominator": pressure_slack.denominator,
            "decimal": float(pressure_slack),
        },
        "one_sided_pressure_without_pair_collision": bool(
            pressure_row["one_sided_pressure_without_pair_collision"]
        ),
        "paired_pressure_bottleneck": pressure_row["paired_pressure_bottleneck"],
        "route_class": threshold_row["route_class"],
        "min_total_extra_residues_to_cross": int(
            threshold_row["min_total_extra_residues_to_cross"]
        ),
        "min_extra_fill_in_minimal_routes": int(
            threshold_row["min_extra_fill_in_minimal_routes"]
        ),
        "minimal_route_requires_fill_increment": bool(
            threshold_row["minimal_route_requires_fill_increment"]
        ),
        "fill_delay_per_required_fill_increment": threshold_row[
            "fill_delay_per_required_fill_increment"
        ],
        "min_new_fill_rankin_mass_required": fill_row[
            "min_new_fill_rankin_mass_required"
        ],
        "fill_epoch_spare_ratio": fill_row["fill_epoch_spare_ratio"],
        "fill_duplicate_would_trigger_reset_pdec": bool(
            fill_row["fill_duplicate_would_trigger_reset_pdec"]
        ),
        "family_persistence_route": route,
        "anonymous_persistence_closed_current": (
            (
                not bool(source_row["source_gate_passed_current"])
                or bool(threshold_row["minimal_route_requires_fill_increment"])
            )
            and bool(epoch_row["occupancy_below_eta"])
            and bool(pressure_row["paired_pressure_gate_passed_current_sweep"])
            and bool(fill_row["new_fill_or_reset_dichotomy_closed"])
        ),
    }


def build_result(
    moving_slot_route_path: Path,
    source_gate_path: Path,
    epoch_multiplicity_path: Path,
    paired_pressure_path: Path,
    threshold_route_path: Path,
    fill_catchup_path: Path,
) -> dict[str, Any]:
    """构造 moving-family persistence pressure 审计结果。"""
    moving_slot_route = load_json(moving_slot_route_path)
    source_gate = load_json(source_gate_path)
    epoch = load_json(epoch_multiplicity_path)
    pressure = load_json(paired_pressure_path)
    threshold = load_json(threshold_route_path)
    fill = load_json(fill_catchup_path)

    source_by_q = index_by_q(source_gate["source_gate_rows"])
    epoch_by_q = index_by_q(epoch["affine_twin_epoch_pair_multiplicity_rows"])
    pressure_by_q = index_by_q(pressure["paired_side_pressure_rows"])
    threshold_by_q = index_by_q(threshold["threshold_route_rows"])
    fill_by_q = index_by_q(fill["fill_catchup_mass_budget_rows"])
    q_values = [int(q) for q in source_gate["aggregate"]["candidate_q_values"]]
    rows = [
        family_row(
            q,
            source_by_q[q],
            epoch_by_q[q],
            pressure_by_q[q],
            threshold_by_q[q],
            fill_by_q[q],
        )
        for q in q_values
    ]

    total_min_fill_mass = sum(
        (frac_from_obj(row["min_new_fill_rankin_mass_required"]) for row in rows),
        Fraction(0, 1),
    )
    blocked_formal_pairs = sum(
        int(row["formal_pairs_blocked_by_source_gate"]) for row in rows
    )
    total_formal_pairs = sum(int(row["formal_pair_count"]) for row in rows)
    route_histogram: dict[str, int] = {}
    for row in rows:
        route = str(row["family_persistence_route"])
        route_histogram[route] = route_histogram.get(route, 0) + 1

    current_closed = (
        bool(
            moving_slot_route["aggregate"][
                "anonymous_moving_slot_actual_overload_closed_current_sweep"
            ]
        )
        and bool(source_gate["aggregate"]["source_materialization_gate_closed_current_sweep"])
        and bool(epoch["aggregate"]["current_sparse_acceptance_closed"])
        and bool(pressure["aggregate"]["all_current_rows_pass_paired_pressure_gate"])
        and bool(threshold["aggregate"]["route_classifier_closed_current_sweep"])
        and bool(fill["aggregate"]["new_fill_or_reset_dichotomy_closed"])
        and all(bool(row["anonymous_persistence_closed_current"]) for row in rows)
    )

    aggregate = {
        "moving_slot_route_ledger": str(moving_slot_route_path.relative_to(ROOT)),
        "source_gate_ledger": str(source_gate_path.relative_to(ROOT)),
        "epoch_multiplicity_ledger": str(epoch_multiplicity_path.relative_to(ROOT)),
        "paired_pressure_ledger": str(paired_pressure_path.relative_to(ROOT)),
        "threshold_route_ledger": str(threshold_route_path.relative_to(ROOT)),
        "fill_catchup_ledger": str(fill_catchup_path.relative_to(ROOT)),
        "candidate_q_values": q_values,
        "realized_q_values": epoch["aggregate"]["realized_q_values"],
        "source_gate_pass_q_values": source_gate["aggregate"]["source_gate_pass_q_values"],
        "source_gate_fail_q_values": source_gate["aggregate"]["source_gate_fail_q_values"],
        "source_gate_blocked_formal_pairs": blocked_formal_pairs,
        "source_gate_blocked_formal_pair_ratio": blocked_formal_pairs / total_formal_pairs,
        "candidate_product_mass_upper_sum": epoch["aggregate"][
            "candidate_product_mass_upper_sum"
        ],
        "candidate_product_mass_upper_sum_below_eta": bool(
            epoch["aggregate"]["candidate_product_mass_upper_sum_below_eta"]
        ),
        "high_density_epoch_pair_count": int(
            epoch["aggregate"]["high_density_epoch_pair_count"]
        ),
        "one_sided_pressure_q_values": pressure["aggregate"][
            "one_sided_pressure_q_values"
        ],
        "pressure_product_pdec_count_current_sweep": int(
            pressure["aggregate"]["pressure_product_pdec_count_current_sweep"]
        ),
        "min_pressure_product_slack": pressure["aggregate"]["min_pressure_product_slack"],
        "all_minimal_routes_require_fill_increment": bool(
            threshold["aggregate"]["all_minimal_routes_require_fill_increment"]
        ),
        "total_min_extra_fill_required_if_all_candidates_cross": sum(
            int(row["min_extra_fill_in_minimal_routes"]) for row in rows
        ),
        "total_min_new_fill_rankin_mass_required_if_all_candidates_cross": {
            "numerator": total_min_fill_mass.numerator,
            "denominator": total_min_fill_mass.denominator,
            "decimal": float(total_min_fill_mass),
        },
        "max_single_candidate_minimal_route_fill_rankin_mass": fill["aggregate"][
            "max_single_candidate_minimal_route_fill_rankin_mass"
        ],
        "family_persistence_route_histogram": dict(sorted(route_histogram.items())),
        "anonymous_moving_family_persistence_closed_current_sweep": current_closed,
        "global_moving_family_persistence_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_moving_family_persistence_pressure_audit"
        ),
        "status": (
            "current_sweep_moving_family_persistence_routed_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "moving_family_persistence_rows": rows,
        "contract": {
            "moving_family_persistence_gate": [
                "a persistent moving family must pass source materialization",
                "its paired side-pressure product must cross the square-root gate",
                "threshold crossing requires fill-side residue arrival",
                "duplicate fill arrival is routed to reset/ColumnCRT-PDEC",
                "sparse epoch-pair mass is SAE unless a high-density PDEC row appears",
            ],
            "closed_current_sweep": current_closed,
            "global_remaining": [
                "MovingSlotFamilyPersistenceNoGo",
                "FillResidueArrivalBound",
                "HighDensityEpochPair-PDEC/ColumnCRT",
                "PressureProduct-PDEC",
                "SourceRematerialization-PDEC/SAE",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                moving_slot_route_path,
                source_gate_path,
                epoch_multiplicity_path,
                paired_pressure_path,
                threshold_route_path,
                fill_catchup_path,
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
        "# Prime Matrix AffineTwin endpoint-release moving-family persistence pressure audit",
        "",
        "**状态：** `current_sweep_moving_family_persistence_routed_global_open`",
        "",
        "本审计继续下钻 moving-slot 的族级持久复现出口：若反例链不靠单个槽位，而靠 moving family 反复续命，则每个候选 `q` 必须同时通过 source 物化、双侧压力乘积、阈值穿越和 fill 到达/重置二分。",
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"source_gate_pass_q_values={agg['source_gate_pass_q_values']}",
        f"source_gate_fail_q_values={agg['source_gate_fail_q_values']}",
        f"source_gate_blocked_formal_pairs={agg['source_gate_blocked_formal_pairs']}",
        f"candidate_product_mass_upper_sum={agg['candidate_product_mass_upper_sum']}",
        f"one_sided_pressure_q_values={agg['one_sided_pressure_q_values']}",
        f"all_minimal_routes_require_fill_increment={fmt_bool(agg['all_minimal_routes_require_fill_increment'])}",
        f"total_min_extra_fill_required_if_all_candidates_cross={agg['total_min_extra_fill_required_if_all_candidates_cross']}",
        f"anonymous_moving_family_persistence_closed_current_sweep={fmt_bool(agg['anonymous_moving_family_persistence_closed_current_sweep'])}",
        "```",
        "",
        "## 1. family persistence rows",
        "",
        "| q | route | source | blocked | one-sided pressure | paired slack | min fill | fill mass | phase defect |",
        "| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["moving_family_persistence_rows"]:
        defect = row["source_phase_defect"]
        if defect["p_delay_delta"] is None:
            defect_text = defect["source_phase_defect_type"]
        else:
            defect_text = f"{defect['source_phase_defect_type']}, dp_delta={defect['p_delay_delta']}"
        lines.append(
            "| {q} | `{route}` | `{source}` | {blocked} | {one_side} | {slack:.6f} | {min_fill} | {fill_mass:.6f} | `{defect}` |".format(
                q=row["q"],
                route=table_cell(row["family_persistence_route"]),
                source=table_cell(row["source_route"]),
                blocked=row["formal_pairs_blocked_by_source_gate"],
                one_side=fmt_bool(row["one_sided_pressure_without_pair_collision"]),
                slack=row["paired_pressure_product_slack"]["decimal"],
                min_fill=row["min_extra_fill_in_minimal_routes"],
                fill_mass=row["min_new_fill_rankin_mass_required"]["decimal"],
                defect=table_cell(defect_text),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾读数",
            "",
            "- `q=31` 是唯一已物化 source，但已被固定 graph cap 管住；若要从安全阈值穿越，仍需新增 fill residue 或进入 reset/ColumnCRT。",
            "- `q=43` 有同 gap source，但实际签名是 `plus->minus` 且 `p_delay=74`，而 AffineTwin 期望 `minus->plus` 且 `p_delay=113`；相位差 `-39`，16 个 formal pairs 全部被 source gate 阻断。",
            "- `q=103` 没有 gap source，12 个 formal pairs 全部被 source gate 阻断。",
            "- `q=43,103` 虽有 generator 单侧压力，但 paired pressure product 仍低于 1；缺口由 fill 侧瓶颈控制。若要越过阈值，所有最小路线都要求 fill 增量。",
            f"- 若三个候选全都尝试阈值穿越，至少需要新增 fill residue 总数 `{agg['total_min_extra_fill_required_if_all_candidates_cross']}`，对应 Rankin 质量 `{agg['total_min_new_fill_rankin_mass_required_if_all_candidates_cross']['decimal']:.12f}`；重复则触发 reset/ColumnCRT-PDEC。",
            "",
            "## 3. 结论边界",
            "",
            "当前 sweep 的 moving-family 持久复现不能作为匿名容量来源：未物化候选先被 source gate 阻断；已物化候选受 graph cap 和 fill-arrival 二分约束；单侧 generator 压力没有与 fill 侧同步形成 paired overload。",
            "",
            "这仍不是全局无条件证明。下一层全局剩余是证明 fill-side residue arrival 不能持久补齐这些阈值缺口，或把失败登记为 `FillResidueArrivalBound`、`HighDensityEpochPair-PDEC/ColumnCRT`、`PressureProduct-PDEC`、`SourceRematerialization-PDEC/SAE`。",
            "",
            "## 4. 依赖哈希",
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
        description=(
            "生成 AffineTwin endpoint-release moving-family persistence pressure 审计证书。"
        )
    )
    parser.add_argument("--moving-slot-route-ledger", type=Path, default=MOVING_SLOT_ROUTE_LEDGER)
    parser.add_argument("--source-gate-ledger", type=Path, default=SOURCE_GATE_LEDGER)
    parser.add_argument(
        "--epoch-multiplicity-ledger", type=Path, default=EPOCH_MULTIPLICITY_LEDGER
    )
    parser.add_argument("--paired-pressure-ledger", type=Path, default=PAIRED_PRESSURE_LEDGER)
    parser.add_argument("--threshold-route-ledger", type=Path, default=THRESHOLD_ROUTE_LEDGER)
    parser.add_argument("--fill-catchup-ledger", type=Path, default=FILL_CATCHUP_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.moving_slot_route_ledger,
        args.source_gate_ledger,
        args.epoch_multiplicity_ledger,
        args.paired_pressure_ledger,
        args.threshold_route_ledger,
        args.fill_catchup_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
