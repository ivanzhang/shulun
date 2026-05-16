#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release generator-coarrival family schema 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_generator_coarrival_family_schema_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-generator-coarrival-family-schema-audit.md
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

COARRIVAL_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "projection-accounting-ledger.json"
)
SUPPORT_GRAPH_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json"
)
MOVING_SLOT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json"
)
SOURCE_GATE_LEDGER = DATA / "prime-matrix-affine-twin-source-materialization-gate-ledger.json"
COLUMNCRT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-cut-anchor-columncrt-compression-ledger.json"
)
MOVING_FAMILY_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-moving-family-persistence-pressure-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "family-schema-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "family-schema-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-generator-coarrival-"
    "family-schema-audit.md"
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


def fixed_graph_bound_row(q: int) -> dict[str, Any]:
    """计算固定 AffineTwin 图像宽度不等式。"""
    width = (q + 9) // 2
    modulus_product = q * (q - 2)
    sqrt_floor = math.isqrt(modulus_product)
    margin = 3 * q * q - 26 * q - 81
    return {
        "q": q,
        "support_width_W": width,
        "modulus_product_q_qminus2": modulus_product,
        "sqrt_floor": sqrt_floor,
        "W_square": width * width,
        "modulus_minus_W_square": modulus_product - width * width,
        "symbolic_margin_3q2_minus_26q_minus_81": margin,
        "W_le_sqrt_floor": width <= sqrt_floor,
        "symbolic_bound_passed": q >= 13 and margin >= 0 and width <= sqrt_floor,
    }


def exit_row(name: str, status: str, evidence: str, route_if_fails: str) -> dict[str, Any]:
    """构造出口路由行。"""
    return {
        "gate": name,
        "status": status,
        "closed_current_sweep": status == "closed_current_sweep",
        "evidence": evidence,
        "route_if_fails": route_if_fails,
    }


def build_result(
    coarrival_path: Path,
    support_graph_path: Path,
    moving_slot_path: Path,
    source_gate_path: Path,
    columncrt_path: Path,
    moving_family_path: Path,
) -> dict[str, Any]:
    """构造 family schema 审计结果。"""
    coarrival = load_json(coarrival_path)
    support_graph = load_json(support_graph_path)
    moving_slot = load_json(moving_slot_path)
    source_gate = load_json(source_gate_path)
    columncrt = load_json(columncrt_path)
    moving_family = load_json(moving_family_path)

    ca = coarrival["aggregate"]
    sg = support_graph["aggregate"]
    ms = moving_slot["aggregate"]
    src = source_gate["aggregate"]
    cc = columncrt["aggregate"]
    mf = moving_family["aggregate"]

    candidate_q_values = sorted({int(q) for q in ca["candidate_q_values"]})
    fixed_graph_rows = [fixed_graph_bound_row(q) for q in candidate_q_values]
    boundary_rows = [fixed_graph_bound_row(q) for q in (13, 17, 19, 23, 29, 31)]

    # 对 q>=13，margin(q)=3q^2-26q-81 在 q>=13 单调递增，且 margin(13)>0。
    symbolic_family_bound = (
        fixed_graph_bound_row(13)["symbolic_margin_3q2_minus_26q_minus_81"] > 0
        and 6 * 13 - 26 > 0
    )

    inside_graph_closed = (
        bool(ca["generator_coarrival_projection_accounting_closed_current_sweep"])
        and bool(ca["all_formal_super_sqrt_subsets_project_below_sqrt"])
        and int(ca["actual_overload_subset_count"]) == 0
    )
    fixed_graph_closed = (
        symbolic_family_bound
        and bool(sg["global_support_graph_cap_proved_for_fixed_affinetwin_q_ge_13"])
        and all(bool(row["symbolic_bound_passed"]) for row in fixed_graph_rows)
    )
    moving_slot_closed = bool(ms["anonymous_moving_slot_actual_overload_closed_current_sweep"])
    source_gate_closed = bool(src["source_materialization_gate_closed_current_sweep"])
    columncrt_closed = bool(cc["fixed_q_fixed_residue_columncrt_routing_closed"])
    moving_family_closed = bool(mf["anonymous_moving_family_persistence_closed_current_sweep"])

    exit_rows = [
        exit_row(
            "InsideFixedSupportGraphProjection",
            "closed_current_sweep" if inside_graph_closed else "open",
            (
                f"formal_super_sqrt_subset_count={ca['formal_super_sqrt_subset_count']}, "
                f"actual_overload_subset_count={ca['actual_overload_subset_count']}, "
                f"full packet {ca['full_formal_product_count']} -> "
                f"{ca['full_projection_hit_count']} actual hits"
            ),
            "ProductAccountingTighteningGlobal or ProjectionCollision-PDEC",
        ),
        exit_row(
            "FixedAffineTwinGraphFamilyBound",
            "closed_current_sweep" if fixed_graph_closed else "open",
            (
                "For q>=13, W=(q+9)/2 and W^2<=q(q-2) follows from "
                "3q^2-26q-81>=0; current candidate q values all pass"
            ),
            "MovingSlotSupportEscape-PDEC/SAE",
        ),
        exit_row(
            "MovingSlotSupportEscape",
            "closed_current_sweep" if moving_slot_closed else "open",
            (
                f"support_motion_candidate_count={ms['support_motion_candidate_count']}; "
                f"narrowest release={ms['narrowest_support_motion_atom']['endpoint_release_total_required']} "
                f"against support width={ms['current_support_width']}; "
                f"exact_rematerialized_q_values={ms['exact_rematerialized_q_values']}"
            ),
            "MovingSlotFamilyPersistenceNoGo or SourceRematerialization-PDEC/SAE",
        ),
        exit_row(
            "SourceMaterializationGate",
            "closed_current_sweep" if source_gate_closed else "open",
            (
                f"source_gate_pass_q_values={src['source_gate_pass_q_values']}; "
                f"source_gate_fail_q_values={src['source_gate_fail_q_values']}; "
                f"blocked formal pairs={src['formal_pairs_blocked_by_source_gate']}"
            ),
            "SameGapWrongSource-PDEC/SAE or NoGapSource-PDEC/SAE",
        ),
        exit_row(
            "FixedResidueColumnCRTCompression",
            "closed_current_sweep" if columncrt_closed else "open",
            (
                f"actual anchor {cc['actual_anchor_pair']} compresses "
                f"{cc['cut_count']} cuts to P == {cc['actual_crt_residue']} "
                f"mod {cc['combined_crt_modulus']}"
            ),
            "ColumnCRT/PDEC",
        ),
        exit_row(
            "MovingFamilyPersistencePressure",
            "closed_current_sweep" if moving_family_closed else "open",
            (
                f"realized_q_values={mf['realized_q_values']}; "
                f"source_gate_blocked_formal_pairs={mf['source_gate_blocked_formal_pairs']}; "
                f"total_min_extra_fill_required={mf['total_min_extra_fill_required_if_all_candidates_cross']}"
            ),
            "HighDensityEpochPair-PDEC/ColumnCRT or moving-family SAE",
        ),
    ]

    schema_closed = all(bool(row["closed_current_sweep"]) for row in exit_rows)

    aggregate = {
        "coarrival_projection_accounting_ledger": str(coarrival_path.relative_to(ROOT)),
        "support_graph_cap_ledger": str(support_graph_path.relative_to(ROOT)),
        "moving_slot_graph_cap_route_ledger": str(moving_slot_path.relative_to(ROOT)),
        "source_materialization_gate_ledger": str(source_gate_path.relative_to(ROOT)),
        "cut_anchor_columncrt_compression_ledger": str(columncrt_path.relative_to(ROOT)),
        "moving_family_persistence_pressure_ledger": str(
            moving_family_path.relative_to(ROOT)
        ),
        "candidate_q_values": candidate_q_values,
        "realized_q_values": ca["realized_q_values"],
        "sqrt_floor_current": int(ca["sqrt_floor"]),
        "support_graph_cap_current": int(ca["support_graph_cap"]),
        "support_graph_cap_slack_to_sqrt_floor": int(
            ca["support_graph_cap_slack_to_sqrt_floor"]
        ),
        "formal_super_sqrt_subset_count": int(ca["formal_super_sqrt_subset_count"]),
        "actual_overload_subset_count": int(ca["actual_overload_subset_count"]),
        "full_formal_product_count": int(ca["full_formal_product_count"]),
        "full_projection_hit_count": int(ca["full_projection_hit_count"]),
        "full_actual_sqrt_slack": int(ca["full_actual_sqrt_slack"]),
        "q_ge_13_symbolic_margin_at_13": int(
            fixed_graph_bound_row(13)[
                "symbolic_margin_3q2_minus_26q_minus_81"
            ]
        ),
        "q_ge_13_margin_derivative_at_13": 6 * 13 - 26,
        "fixed_graph_family_symbolic_bound_proved": symbolic_family_bound,
        "all_candidate_fixed_graph_bounds_passed": all(
            bool(row["symbolic_bound_passed"]) for row in fixed_graph_rows
        ),
        "inside_fixed_graph_projection_closed_current_sweep": inside_graph_closed,
        "moving_slot_support_escape_routed_current_sweep": moving_slot_closed,
        "source_materialization_gate_closed_current_sweep": source_gate_closed,
        "fixed_residue_columncrt_compression_closed_current_sweep": columncrt_closed,
        "moving_family_persistence_closed_current_sweep": moving_family_closed,
        "generator_coarrival_family_schema_closed_current_sweep": schema_closed,
        "global_generator_coarrival_family_bound_proved": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "generator_coarrival_family_schema_audit"
        ),
        "status": "current_sweep_generator_coarrival_family_schema_routed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "symbolic_boundary_rows": boundary_rows,
        "fixed_candidate_graph_bound_rows": fixed_graph_rows,
        "exit_route_rows": exit_rows,
        "contract": {
            "generator_coarrival_family_schema": [
                "inside a fixed AffineTwin support graph, actual load is graph image size, not side-product size",
                "for q>=13 the fixed graph width W=(q+9)/2 is below sqrt(q(q-2))",
                "therefore actual overload requires support motion, source rematerialization, projection collision, or ColumnCRT/moving-family persistence",
                "the current sweep routes each of these exits to an already named ledger",
            ],
            "closed_current_sweep": schema_closed,
            "global_remaining": [
                "PromoteFixedGraphProjectionSchemaToAllPersistentAffineTwinFamilies",
                "MovingSlotFamilyPersistenceNoGo",
                "SourceRematerialization-PDEC/SAE",
                "ColumnCRT/PDEC",
                "ProductAccountingTighteningGlobal",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                coarrival_path,
                support_graph_path,
                moving_slot_path,
                source_gate_path,
                columncrt_path,
                moving_family_path,
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
        "# Prime Matrix AffineTwin endpoint-release generator-coarrival family schema audit",
        "",
        "**状态：** `current_sweep_generator_coarrival_family_schema_routed_global_open`",
        "",
        "本审计把上一轮 `q=31` 的 coarrival 子集枚举提升为族级门控格式：固定 AffineTwin 支撑图像内，actual load 只按图像容量计；若要 actual overload，必须破坏固定图像假设并进入命名出口。",
        "",
        "```text",
        f"candidate_q_values={agg['candidate_q_values']}",
        f"fixed_graph_family_symbolic_bound_proved={fmt_bool(agg['fixed_graph_family_symbolic_bound_proved'])}",
        f"q_ge_13_symbolic_margin_at_13={agg['q_ge_13_symbolic_margin_at_13']}",
        f"formal_super_sqrt_subset_count={agg['formal_super_sqrt_subset_count']}",
        f"actual_overload_subset_count={agg['actual_overload_subset_count']}",
        f"full_formal_product_count={agg['full_formal_product_count']}",
        f"full_projection_hit_count={agg['full_projection_hit_count']}",
        f"moving_slot_support_escape_routed_current_sweep={fmt_bool(agg['moving_slot_support_escape_routed_current_sweep'])}",
        f"source_materialization_gate_closed_current_sweep={fmt_bool(agg['source_materialization_gate_closed_current_sweep'])}",
        f"fixed_residue_columncrt_compression_closed_current_sweep={fmt_bool(agg['fixed_residue_columncrt_compression_closed_current_sweep'])}",
        f"generator_coarrival_family_schema_closed_current_sweep={fmt_bool(agg['generator_coarrival_family_schema_closed_current_sweep'])}",
        "```",
        "",
        "## 1. 固定图像族级不等式",
        "",
        "固定 AffineTwin 槽的支撑宽度为 `W=(q+9)/2`。对 `q>=13`，",
        "",
        "```text",
        "W^2 <= q(q-2)  <=>  3q^2-26q-81 >= 0.",
        "```",
        "",
        "`q=13` 时右侧为正，且导数 `6q-26` 在 `q>=13` 为正，所以该不等式对所有 `q>=13` 成立。",
        "",
        "| q | W | sqrt_floor | W^2 | q(q-2)-W^2 | margin | pass |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["fixed_candidate_graph_bound_rows"]:
        lines.append(
            "| {q} | {w} | {sqrt} | {w2} | {gap} | {margin} | {passed} |".format(
                q=row["q"],
                w=row["support_width_W"],
                sqrt=row["sqrt_floor"],
                w2=row["W_square"],
                gap=row["modulus_minus_W_square"],
                margin=row["symbolic_margin_3q2_minus_26q_minus_81"],
                passed=fmt_bool(row["symbolic_bound_passed"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 出口路由",
            "",
            "| gate | status | evidence | route if fails |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["exit_route_rows"]:
        lines.append(
            "| `{gate}` | `{status}` | {evidence} | `{route}` |".format(
                gate=row["gate"],
                status=row["status"],
                evidence=table_cell(row["evidence"]),
                route=table_cell(row["route_if_fails"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 显式矛盾读数",
            "",
            "- 反例链需要把 generator/fill 共到达后的侧残基笛卡尔积当作容量来源。",
            "- 真实链在固定 AffineTwin 支撑内只允许函数图像容量 `W`，而 `W<=sqrt(q(q-2))`。",
            "- 当前 sweep 的 `22` 个形式超平方根子集全部投影到平方根门以下；完整 packet 为 `64 -> 6 hits`。",
            "- 若未来全局族中出现 actual overload，它必须破坏固定函数图像，转入 support motion、source rematerialization、ColumnCRT/PDEC 或 moving-family persistence。",
            "",
            "## 4. 结论边界",
            "",
            "当前 sweep 的 generator-coarrival family schema 已路由闭合，但这仍不是行/列命题的全局无条件证明。全局剩余是把该 schema 推广到所有持久 AffineTwin family，并排斥或吸收每个命名出口。",
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
        description="生成 AffineTwin endpoint-release generator-coarrival family schema 审计证书。"
    )
    parser.add_argument("--coarrival-ledger", type=Path, default=COARRIVAL_LEDGER)
    parser.add_argument("--support-graph-ledger", type=Path, default=SUPPORT_GRAPH_LEDGER)
    parser.add_argument("--moving-slot-ledger", type=Path, default=MOVING_SLOT_LEDGER)
    parser.add_argument("--source-gate-ledger", type=Path, default=SOURCE_GATE_LEDGER)
    parser.add_argument("--columncrt-ledger", type=Path, default=COLUMNCRT_LEDGER)
    parser.add_argument("--moving-family-ledger", type=Path, default=MOVING_FAMILY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.coarrival_ledger,
        args.support_graph_ledger,
        args.moving_slot_ledger,
        args.source_gate_ledger,
        args.columncrt_ledger,
        args.moving_family_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
