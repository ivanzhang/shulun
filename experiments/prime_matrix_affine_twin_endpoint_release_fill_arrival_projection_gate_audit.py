#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release fill-arrival projection gate 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_fill_arrival_projection_gate_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-audit.md
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

MOVING_FAMILY_PRESSURE_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json"
)
THRESHOLD_ROUTE_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-threshold-route-classifier-ledger.json"
)
FILL_CATCHUP_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-fill-catchup-mass-budget-ledger.json"
)
SOURCE_GATE_LEDGER = DATA / "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
UNUSED_TARGET_LEDGER = DATA / "prime-matrix-affine-twin-unused-target-arrival-ledger.json"
PROJECTION_DEFICIT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-carrier-arrival-projection-deficit-ledger.json"
)
SUPPORT_GRAPH_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-fill-arrival-projection-gate-audit.md"
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


def index_by_q(rows: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    """按 q 建立索引。"""
    return {int(row["q"]): row for row in rows}


def q_row(
    q: int,
    pressure_row: dict[str, Any],
    threshold_row: dict[str, Any],
    fill_row: dict[str, Any],
    source_row: dict[str, Any],
    projection: dict[str, Any],
    support_graph: dict[str, Any],
) -> dict[str, Any]:
    """构造单个 q 的 fill-arrival 投影门控行。"""
    realized = bool(pressure_row["realized_current_sweep"])
    source_passed = bool(source_row["source_gate_passed_current"])
    fill_only = bool(threshold_row["minimal_route_can_be_fill_only"])
    min_generator = int(threshold_row["min_extra_generator_in_minimal_routes"])
    min_fill = int(threshold_row["min_extra_fill_in_minimal_routes"])

    if realized:
        route = "RealizedNoFillOnlyGraphProjection"
        actual_gate = (
            source_passed
            and not fill_only
            and min_generator > 0
            and bool(projection["aggregate"]["all_minimal_crossings_project_below_sqrt_gate"])
            and bool(support_graph["aggregate"]["support_graph_cap_closed_current_sweep"])
        )
        obstruction = (
            f"fill arrival alone cannot cross; needs at least {min_generator} "
            "generator residues and then projects below sqrt gate"
        )
    elif not source_passed:
        route = f"SourceGateBlockedBeforeFillProjection:{source_row['route']}"
        actual_gate = True
        obstruction = (
            "formal fill-only threshold is source-unmaterialized; actual packet "
            f"blocked by {source_row['route']}"
        )
    else:
        route = "UnclassifiedFillArrival"
        actual_gate = False
        obstruction = "unexpected source-materialized non-realized fill arrival"

    return {
        "q": q,
        "realized_current_sweep": realized,
        "source_route": source_row["route"],
        "source_gate_passed_current": source_passed,
        "formal_pairs_blocked_by_source_gate": int(
            source_row["formal_pairs_blocked_by_source_gate"]
        ),
        "route_class": threshold_row["route_class"],
        "minimal_route_can_be_fill_only": fill_only,
        "minimal_route_can_be_generator_only": bool(
            threshold_row["minimal_route_can_be_generator_only"]
        ),
        "minimal_route_requires_fill_increment": bool(
            threshold_row["minimal_route_requires_fill_increment"]
        ),
        "min_extra_fill_in_minimal_routes": min_fill,
        "min_extra_generator_in_minimal_routes": min_generator,
        "min_total_extra_residues_to_cross": int(
            threshold_row["min_total_extra_residues_to_cross"]
        ),
        "min_new_fill_rankin_mass_required": fill_row[
            "min_new_fill_rankin_mass_required"
        ],
        "fill_duplicate_would_trigger_reset_pdec": bool(
            fill_row["fill_duplicate_would_trigger_reset_pdec"]
        ),
        "fill_arrival_projection_route": route,
        "fill_arrival_actual_overload_closed_current": actual_gate,
        "obstruction": obstruction,
    }


def build_result(
    moving_family_pressure_path: Path,
    threshold_route_path: Path,
    fill_catchup_path: Path,
    source_gate_path: Path,
    unused_target_path: Path,
    projection_deficit_path: Path,
    support_graph_path: Path,
) -> dict[str, Any]:
    """构造 fill-arrival projection gate 审计结果。"""
    moving_family_pressure = load_json(moving_family_pressure_path)
    threshold = load_json(threshold_route_path)
    fill = load_json(fill_catchup_path)
    source = load_json(source_gate_path)
    unused = load_json(unused_target_path)
    projection = load_json(projection_deficit_path)
    support_graph = load_json(support_graph_path)

    pressure_by_q = index_by_q(moving_family_pressure["moving_family_persistence_rows"])
    threshold_by_q = index_by_q(threshold["threshold_route_rows"])
    fill_by_q = index_by_q(fill["fill_catchup_mass_budget_rows"])
    source_by_q = index_by_q(source["source_gate_rows"])
    q_values = [int(q) for q in moving_family_pressure["aggregate"]["candidate_q_values"]]
    rows = [
        q_row(
            q,
            pressure_by_q[q],
            threshold_by_q[q],
            fill_by_q[q],
            source_by_q[q],
            projection,
            support_graph,
        )
        for q in q_values
    ]

    realized_rows = [row for row in rows if row["realized_current_sweep"]]
    source_blocked_rows = [row for row in rows if not row["source_gate_passed_current"]]
    route_histogram: dict[str, int] = {}
    for row in rows:
        route = str(row["fill_arrival_projection_route"])
        route_histogram[route] = route_histogram.get(route, 0) + 1

    aggregate = {
        "moving_family_pressure_ledger": str(
            moving_family_pressure_path.relative_to(ROOT)
        ),
        "threshold_route_ledger": str(threshold_route_path.relative_to(ROOT)),
        "fill_catchup_ledger": str(fill_catchup_path.relative_to(ROOT)),
        "source_gate_ledger": str(source_gate_path.relative_to(ROOT)),
        "unused_target_arrival_ledger": str(unused_target_path.relative_to(ROOT)),
        "projection_deficit_ledger": str(projection_deficit_path.relative_to(ROOT)),
        "support_graph_cap_ledger": str(support_graph_path.relative_to(ROOT)),
        "candidate_q_values": q_values,
        "realized_q_values": [int(row["q"]) for row in realized_rows],
        "source_blocked_q_values": [int(row["q"]) for row in source_blocked_rows],
        "source_blocked_formal_pairs": sum(
            int(row["formal_pairs_blocked_by_source_gate"]) for row in source_blocked_rows
        ),
        "realized_fill_only_route_count": sum(
            1 for row in realized_rows if row["minimal_route_can_be_fill_only"]
        ),
        "realized_min_extra_generator_required": min(
            int(row["min_extra_generator_in_minimal_routes"]) for row in realized_rows
        )
        if realized_rows
        else None,
        "all_realized_fill_arrivals_require_generator_coarrival": all(
            not bool(row["minimal_route_can_be_fill_only"])
            and int(row["min_extra_generator_in_minimal_routes"]) > 0
            for row in realized_rows
        ),
        "unused_target_required_new_fill_residues": unused["aggregate"][
            "required_new_fill_residues"
        ],
        "unused_target_required_new_generator_residues": unused["aggregate"][
            "required_new_generator_residues"
        ],
        "all_unused_targets_need_new_generator_residue": bool(
            unused["aggregate"]["all_unused_targets_need_new_generator_residue"]
        ),
        "all_unused_target_crt_jumps_exceed_support_width": bool(
            unused["aggregate"][
                "all_unused_target_crt_jumps_exceed_support_width_current_sweep"
            ]
        ),
        "minimal_crossing_formal_product_count": int(
            projection["aggregate"]["minimal_crossing_formal_product_count"]
        ),
        "minimal_crossing_projection_hit_count": int(
            projection["aggregate"]["minimal_crossing_projection_hit_count"]
        ),
        "minimal_crossing_projection_deficit_count": int(
            projection["aggregate"]["minimal_crossing_projection_deficit_count"]
        ),
        "minimal_crossing_actual_sqrt_slack": int(
            projection["aggregate"]["minimal_crossing_actual_sqrt_slack"]
        ),
        "all_minimal_crossings_project_below_sqrt_gate": bool(
            projection["aggregate"]["all_minimal_crossings_project_below_sqrt_gate"]
        ),
        "support_graph_cap": int(support_graph["aggregate"]["support_graph_cap"]),
        "sqrt_floor": int(support_graph["aggregate"]["sqrt_floor"]),
        "support_graph_cap_slack_to_sqrt_floor": int(
            support_graph["aggregate"]["support_graph_cap_slack_to_sqrt_floor"]
        ),
        "fill_arrival_projection_route_histogram": dict(sorted(route_histogram.items())),
        "anonymous_fill_arrival_actual_overload_closed_current_sweep": all(
            bool(row["fill_arrival_actual_overload_closed_current"]) for row in rows
        )
        and bool(projection["aggregate"]["all_minimal_crossings_project_below_sqrt_gate"])
        and bool(unused["aggregate"]["all_unused_targets_need_new_generator_residue"]),
        "global_fill_residue_arrival_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_fill_arrival_projection_gate_audit"
        ),
        "status": "current_sweep_fill_arrival_projection_routed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "fill_arrival_projection_rows": rows,
        "contract": {
            "fill_arrival_projection_gate": [
                "realized q cannot use fill-only crossing",
                "realized fill arrival must co-arrive with generator residues",
                "co-arriving unused targets are outside the current formal/support packet",
                "when co-arrival is counted formally, actual projection remains graph-bounded",
                "non-realized fill-only candidates are blocked before projection by source gate",
            ],
            "closed_current_sweep": aggregate[
                "anonymous_fill_arrival_actual_overload_closed_current_sweep"
            ],
            "global_remaining": [
                "FillResidueArrivalBound",
                "GeneratorCoarrivalBound",
                "ProductAccountingTighteningGlobal",
                "SourceRematerialization-PDEC/SAE",
                "ColumnCRT/PDEC",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                moving_family_pressure_path,
                threshold_route_path,
                fill_catchup_path,
                source_gate_path,
                unused_target_path,
                projection_deficit_path,
                support_graph_path,
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
        "# Prime Matrix AffineTwin endpoint-release fill-arrival projection gate audit",
        "",
        "**状态：** `current_sweep_fill_arrival_projection_routed_global_open`",
        "",
        "本审计继续压缩 `FillResidueArrivalBound`：fill 到达本身不是 actual overload。已物化 `q=31` 不能走 fill-only 路线，必须 generator 共到达；未物化 `q=43,103` 虽形式上可 fill-only，但先被 source gate 阻断。",
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"realized_q_values={agg['realized_q_values']}",
        f"source_blocked_q_values={agg['source_blocked_q_values']}",
        f"source_blocked_formal_pairs={agg['source_blocked_formal_pairs']}",
        f"all_realized_fill_arrivals_require_generator_coarrival={fmt_bool(agg['all_realized_fill_arrivals_require_generator_coarrival'])}",
        f"minimal_crossing_formal_product_count={agg['minimal_crossing_formal_product_count']}",
        f"minimal_crossing_projection_hit_count={agg['minimal_crossing_projection_hit_count']}",
        f"minimal_crossing_actual_sqrt_slack={agg['minimal_crossing_actual_sqrt_slack']}",
        f"anonymous_fill_arrival_actual_overload_closed_current_sweep={fmt_bool(agg['anonymous_fill_arrival_actual_overload_closed_current_sweep'])}",
        "```",
        "",
        "## 1. fill arrival projection rows",
        "",
        "| q | route | source | fill-only | min fill | min generator | blocked pairs | obstruction |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in result["fill_arrival_projection_rows"]:
        lines.append(
            "| {q} | `{route}` | `{source}` | {fill_only} | {min_fill} | {min_gen} | {blocked} | {obs} |".format(
                q=row["q"],
                route=table_cell(row["fill_arrival_projection_route"]),
                source=table_cell(row["source_route"]),
                fill_only=fmt_bool(row["minimal_route_can_be_fill_only"]),
                min_fill=row["min_extra_fill_in_minimal_routes"],
                min_gen=row["min_extra_generator_in_minimal_routes"],
                blocked=row["formal_pairs_blocked_by_source_gate"],
                obs=table_cell(row["obstruction"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 显式矛盾读数",
            "",
            "- `q=31` 是唯一已物化候选，但 `minimal_route_can_be_fill_only=false`；任何阈值穿越至少还要新增 2 个 generator residue。",
            f"- unused-target 账本给出的新 fill residues 为 `{agg['unused_target_required_new_fill_residues']}`，但全部 target 同时需要新 generator residue，并且 CRT jump 都超过 support width。",
            f"- 即使把共到达形式乘积推到最小 crossing `{agg['minimal_crossing_formal_product_count']}`，actual projection 也只有 `{agg['minimal_crossing_projection_hit_count']}` 个 hit，仍有 sqrt slack `{agg['minimal_crossing_actual_sqrt_slack']}`。",
            "- `q=43,103` 的 fill-only 形式路线不能进入真实链，因为 source gate 已先阻断：一个 wrong-source，一个 no-source。",
            "",
            "## 3. 结论边界",
            "",
            "当前 sweep 内不存在匿名 fill-arrival actual overload：realized 分支必须 generator 共到达并回到 graph projection；non-realized 分支先败于 source materialization。",
            "",
            "这仍不是全局无条件证明。下一层剩余被压成 `GeneratorCoarrivalBound`、`ProductAccountingTighteningGlobal`、`SourceRematerialization-PDEC/SAE` 与 `ColumnCRT/PDEC` 的族级排斥或控制。",
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
        description="生成 AffineTwin endpoint-release fill-arrival projection gate 审计证书。"
    )
    parser.add_argument(
        "--moving-family-pressure-ledger",
        type=Path,
        default=MOVING_FAMILY_PRESSURE_LEDGER,
    )
    parser.add_argument("--threshold-route-ledger", type=Path, default=THRESHOLD_ROUTE_LEDGER)
    parser.add_argument("--fill-catchup-ledger", type=Path, default=FILL_CATCHUP_LEDGER)
    parser.add_argument("--source-gate-ledger", type=Path, default=SOURCE_GATE_LEDGER)
    parser.add_argument("--unused-target-ledger", type=Path, default=UNUSED_TARGET_LEDGER)
    parser.add_argument(
        "--projection-deficit-ledger", type=Path, default=PROJECTION_DEFICIT_LEDGER
    )
    parser.add_argument("--support-graph-ledger", type=Path, default=SUPPORT_GRAPH_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.moving_family_pressure_ledger,
        args.threshold_route_ledger,
        args.fill_catchup_ledger,
        args.source_gate_ledger,
        args.unused_target_ledger,
        args.projection_deficit_ledger,
        args.support_graph_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
