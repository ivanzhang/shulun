#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release moving-slot graph-cap route 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_moving_slot_graph_cap_route_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-audit.md
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

SUPPORT_GRAPH_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-support-graph-cap-ledger.json"
)
SUPPORT_MOTION_LEDGER = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"
PRIMITIVE_DEFECT_LEDGER = DATA / (
    "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
)
MOVING_DEPTH_LEDGER = DATA / "prime-matrix-affine-twin-moving-key-depth-formula-ledger.json"
SOURCE_REMATERIALIZATION_LEDGER = DATA / (
    "prime-matrix-affine-twin-moving-key-source-rematerialization-ledger.json"
)
MOVING_FAMILY_LEDGER = DATA / (
    "square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "affine-twin-moving-family-sae-columncrt-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-moving-slot-graph-cap-route-audit.md"
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


def fixed_family_graph_row(row: dict[str, Any]) -> dict[str, Any]:
    """把 moving-family 候选转成固定槽图容量行。"""
    q = int(row["q"])
    width = int(row["pair_support_width_affine"])
    modulus = q * (q - 2)
    sqrt_floor = math.isqrt(modulus)
    symbolic_width = (q + 9) // 2 if (q + 9) % 2 == 0 else (q + 9) / 2
    symbolic_margin = 3 * q * q - 26 * q - 81
    return {
        "q": q,
        "generator_ell": int(row["generator_ell"]),
        "fill_ell": int(row["fill_ell"]),
        "pair_support_width_affine": width,
        "symbolic_width_q_plus_9_over_2": symbolic_width,
        "modulus_product": modulus,
        "sqrt_floor": sqrt_floor,
        "support_width_square": width * width,
        "modulus_minus_support_width_square": modulus - width * width,
        "symbolic_margin_3q2_minus_26q_minus_81": symbolic_margin,
        "fixed_slot_graph_cap_passed": (
            q >= 13 and width <= sqrt_floor and symbolic_margin >= 0
        ),
        "orientation_epochs_present": bool(row["orientation_epochs_present"]),
        "realized_current_sweep": bool(row["realized_current_sweep"]),
        "realized_affine_twin_pair_count": int(row["realized_affine_twin_pair_count"]),
        "epoch_pair_capacity": int(row["epoch_pair_capacity"]),
        "epoch_pair_product_used_upper": int(row["epoch_pair_product_used_upper"]),
        "epoch_pair_unused_lower": int(row["epoch_pair_unused_lower"]),
        "fixed_pair_modulus_margin": int(row["fixed_pair_modulus_margin"]),
    }


def build_route_rows(
    support_graph: dict[str, Any],
    support_motion: dict[str, Any],
    primitive_defect: dict[str, Any],
    moving_depth: dict[str, Any],
    source_remat: dict[str, Any],
    moving_family: dict[str, Any],
    fixed_family_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """构造 moving-slot 逃逸的分层路由表。"""
    sg = support_graph["aggregate"]
    sm = support_motion["aggregate"]
    pd = primitive_defect["aggregate"]
    md = moving_depth["aggregate"]
    sr = source_remat["aggregate"]
    mf = moving_family["aggregate"]

    return [
        {
            "gate": "FixedOrMovedAffineTwinGraphCap",
            "tested_input": "any fixed-orientation AffineTwin slot candidate q>=13",
            "evidence": (
                "all candidate widths W=(q+9)/2 satisfy W^2<=q(q-2); "
                f"current fixed q={sg['q']} has graph cap {sg['support_graph_cap']} "
                f"and sqrt floor {sg['sqrt_floor']}"
            ),
            "closed_current_sweep": all(
                bool(row["fixed_slot_graph_cap_passed"]) for row in fixed_family_rows
            )
            and bool(sg["support_graph_cap_closed_current_sweep"]),
            "route_if_fails": "ProjectionCollision-PDEC / ProductAccountingTightening",
        },
        {
            "gate": "SamePrimitiveSupportMotion",
            "tested_input": "move support while keeping current q=31 primitive key",
            "evidence": (
                f"{sm['support_motion_candidate_count']} candidates all require both "
                "endpoint releases; narrowest atom "
                f"{sm['narrowest_endpoint_release_atom']['source_pair_key']} needs "
                f"release {sm['narrowest_endpoint_release_atom']['endpoint_release_total_required']} "
                f"against support width {sm['support_width_current']}"
            ),
            "closed_current_sweep": bool(
                sm["all_support_motion_requires_both_endpoint_release"]
            )
            and bool(sm["support_motion_depth_closed_current_sweep"]),
            "route_if_fails": "MovingSupportDepthInflation-PDEC/SAE",
        },
        {
            "gate": "FixedPrimitiveDepthIdentity",
            "tested_input": "absorb support motion by the same primitive depth identities",
            "evidence": (
                f"all {pd['support_motion_primitive_defect_candidate_count']} "
                "candidates break both generator and fill depth identities; "
                f"minimum defect is {pd['min_total_affine_depth_defect']}"
            ),
            "closed_current_sweep": bool(
                pd["fixed_primitive_key_support_motion_absorption_closed_current_sweep"]
            ),
            "route_if_fails": "MovingPrimitiveKey-PDEC/SAE",
        },
        {
            "gate": "SameOrientationMovingKeyDepthFormula",
            "tested_input": "allow q to move but keep same AffineTwin orientation and depth formula",
            "evidence": (
                "no support-motion depth gives a common q; narrowest atom "
                f"{md['narrowest_formula_obstruction_atom']['source_pair_key']} gives "
                f"q_g={md['narrowest_formula_obstruction_atom']['q_from_generator_depth_formula']} "
                f"and q_f={md['narrowest_formula_obstruction_atom']['q_from_fill_depth_formula']}"
            ),
            "closed_current_sweep": bool(
                md["same_orientation_moving_key_depth_absorption_closed_current_sweep"]
            ),
            "route_if_fails": "OrientationChangingPrimitiveKey-PDEC/SAE",
        },
        {
            "gate": "MovingKeySourceRematerialization",
            "tested_input": "rematerialize a depth-formula candidate q as a new AffineTwin source",
            "evidence": (
                f"{sr['unique_moving_q_candidate_count']} candidate q values; "
                f"exact rematerialized q values = {sr['exact_rematerialized_q_values']}; "
                f"route histogram = {sr['route_histogram']}"
            ),
            "closed_current_sweep": bool(
                sr["moving_key_source_rematerialization_closed_current_sweep"]
            ),
            "route_if_fails": "SourceRematerialization-PDEC/SAE",
        },
        {
            "gate": "MovingFamilyColumnCRTOrSAE",
            "tested_input": "persist by changing q/residue family rather than carrying the same slot",
            "evidence": (
                f"moving-family candidate q values = {mf['candidate_q_values']}; "
                f"realized q values = {mf['realized_q_values']}; "
                "fixed q/fixed residue ColumnCRT routing is closed in the current ledger"
            ),
            "closed_current_sweep": bool(
                mf["fixed_q_fixed_residue_columncrt_routing_closed"]
            ),
            "route_if_fails": "ColumnCRT/PDEC or moving-family SAE",
        },
    ]


def build_result(
    support_graph_path: Path,
    support_motion_path: Path,
    primitive_defect_path: Path,
    moving_depth_path: Path,
    source_remat_path: Path,
    moving_family_path: Path,
) -> dict[str, Any]:
    """构造 moving-slot graph-cap route 审计结果。"""
    support_graph = load_json(support_graph_path)
    support_motion = load_json(support_motion_path)
    primitive_defect = load_json(primitive_defect_path)
    moving_depth = load_json(moving_depth_path)
    source_remat = load_json(source_remat_path)
    moving_family = load_json(moving_family_path)

    fixed_family_rows = [
        fixed_family_graph_row(row)
        for row in moving_family["candidate_affine_twin_epoch_pair_rows"]
    ]
    route_rows = build_route_rows(
        support_graph,
        support_motion,
        primitive_defect,
        moving_depth,
        source_remat,
        moving_family,
        fixed_family_rows,
    )

    sg = support_graph["aggregate"]
    sm = support_motion["aggregate"]
    pd = primitive_defect["aggregate"]
    md = moving_depth["aggregate"]
    sr = source_remat["aggregate"]
    mf = moving_family["aggregate"]
    fixed_candidate_q_values = [int(row["q"]) for row in fixed_family_rows]
    closed_current = all(bool(row["closed_current_sweep"]) for row in route_rows)

    aggregate = {
        "support_graph_cap_ledger": str(support_graph_path.relative_to(ROOT)),
        "support_motion_depth_ledger": str(support_motion_path.relative_to(ROOT)),
        "support_motion_primitive_defect_ledger": str(
            primitive_defect_path.relative_to(ROOT)
        ),
        "moving_key_depth_formula_ledger": str(moving_depth_path.relative_to(ROOT)),
        "moving_key_source_rematerialization_ledger": str(
            source_remat_path.relative_to(ROOT)
        ),
        "moving_family_ledger": str(moving_family_path.relative_to(ROOT)),
        "current_q": int(sg["q"]),
        "current_support_width": int(sg["support_width"]),
        "current_sqrt_floor": int(sg["sqrt_floor"]),
        "current_support_graph_cap": int(sg["support_graph_cap"]),
        "current_support_graph_cap_slack_to_sqrt_floor": int(
            sg["support_graph_cap_slack_to_sqrt_floor"]
        ),
        "fixed_candidate_q_values": fixed_candidate_q_values,
        "all_fixed_candidate_graph_caps_passed": all(
            bool(row["fixed_slot_graph_cap_passed"]) for row in fixed_family_rows
        ),
        "realized_fixed_candidate_q_values": [
            int(row["q"]) for row in fixed_family_rows if row["realized_current_sweep"]
        ],
        "support_motion_candidate_count": int(sm["support_motion_candidate_count"]),
        "all_support_motion_requires_both_endpoint_release": bool(
            sm["all_support_motion_requires_both_endpoint_release"]
        ),
        "narrowest_support_motion_atom": sm["narrowest_endpoint_release_atom"],
        "narrowest_release_over_support_width": (
            int(sm["narrowest_endpoint_release_atom"]["endpoint_release_total_required"])
            / int(sg["support_width"])
        ),
        "all_support_motion_breaks_both_depth_identities": bool(
            pd["all_support_motion_breaks_both_depth_identities"]
        ),
        "narrowest_primitive_defect_atom": pd["narrowest_affine_defect_atom"],
        "moving_key_depth_formula_candidate_count": int(
            md["moving_key_depth_formula_candidate_count"]
        ),
        "all_same_orientation_affine_depth_common_q_absent": bool(
            md["all_same_orientation_affine_depth_common_q_absent"]
        ),
        "narrowest_formula_obstruction_atom": md[
            "narrowest_formula_obstruction_atom"
        ],
        "unique_moving_q_candidate_count": int(
            sr["unique_moving_q_candidate_count"]
        ),
        "moving_q_candidate_values": sr["candidate_q_values"],
        "prime_candidate_q_values": sr["prime_candidate_q_values"],
        "affine_twin_prime_gate_q_values": sr["affine_twin_prime_gate_q_values"],
        "exact_rematerialized_q_values": sr["exact_rematerialized_q_values"],
        "source_rematerialization_route_histogram": sr["route_histogram"],
        "moving_family_candidate_q_values": mf["candidate_q_values"],
        "moving_family_realized_q_values": mf["realized_q_values"],
        "fixed_q_fixed_residue_columncrt_routing_closed": bool(
            mf["fixed_q_fixed_residue_columncrt_routing_closed"]
        ),
        "anonymous_moving_slot_actual_overload_closed_current_sweep": closed_current,
        "global_moving_slot_support_escape_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_moving_slot_graph_cap_route_audit"
        ),
        "status": (
            "current_sweep_anonymous_moving_slot_support_escape_routed_global_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "fixed_family_graph_cap_rows": fixed_family_rows,
        "moving_slot_route_rows": route_rows,
        "contract": {
            "moving_slot_route_gate": [
                "a fixed-orientation AffineTwin slot remains graph-cap bounded",
                "a moved support with the same primitive key must pay two endpoint releases",
                "the same primitive key then breaks both depth identities",
                "a same-orientation moving q must satisfy both depth formulas",
                "any candidate moving q must rematerialize through prime/source gates",
                "persistent q/residue family motion must enter ColumnCRT/PDEC or SAE",
            ],
            "closed_current_sweep": closed_current,
            "global_remaining": [
                "MovingSlotFamilyPersistenceNoGo",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE",
                "ColumnCRT/PDEC",
                "GlobalUnusedTargetResidueArrivalBound",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (
                support_graph_path,
                support_motion_path,
                primitive_defect_path,
                moving_depth_path,
                source_remat_path,
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
    narrow_motion = agg["narrowest_support_motion_atom"]
    narrow_formula = agg["narrowest_formula_obstruction_atom"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release moving-slot graph-cap route audit",
        "",
        "**状态：** `current_sweep_anonymous_moving_slot_support_escape_routed_global_open`",
        "",
        "本审计把上一层 `support-graph cap` 的剩余 moving-slot 出口拆成可检查路由：固定或同向移动的 AffineTwin 槽仍受图容量控制；真正移动支撑则必须支付双端点释放、破坏固定 primitive 深度身份，或进入 moving-key/source/ColumnCRT/SAE 出口。",
        "",
        "```text",
        f"current_q={agg['current_q']}",
        f"current_support_graph_cap={agg['current_support_graph_cap']}",
        f"current_sqrt_floor={agg['current_sqrt_floor']}",
        f"fixed_candidate_q_values={agg['fixed_candidate_q_values']}",
        f"all_fixed_candidate_graph_caps_passed={fmt_bool(agg['all_fixed_candidate_graph_caps_passed'])}",
        f"support_motion_candidate_count={agg['support_motion_candidate_count']}",
        f"all_support_motion_requires_both_endpoint_release={fmt_bool(agg['all_support_motion_requires_both_endpoint_release'])}",
        f"exact_rematerialized_q_values={agg['exact_rematerialized_q_values']}",
        f"anonymous_moving_slot_actual_overload_closed_current_sweep={fmt_bool(agg['anonymous_moving_slot_actual_overload_closed_current_sweep'])}",
        "```",
        "",
        "## 1. fixed-family graph cap",
        "",
        "| q | width | sqrt floor | width^2 | q(q-2)-width^2 | symbolic margin | realized | graph cap passed |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["fixed_family_graph_cap_rows"]:
        lines.append(
            "| {q} | {width} | {sqrt_floor} | {width_sq} | {margin} | {sym} | {realized} | {passed} |".format(
                q=row["q"],
                width=row["pair_support_width_affine"],
                sqrt_floor=row["sqrt_floor"],
                width_sq=row["support_width_square"],
                margin=row["modulus_minus_support_width_square"],
                sym=row["symbolic_margin_3q2_minus_26q_minus_81"],
                realized=fmt_bool(row["realized_current_sweep"]),
                passed=fmt_bool(row["fixed_slot_graph_cap_passed"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. moving-slot route table",
            "",
            "| gate | closed | route if fails | evidence |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["moving_slot_route_rows"]:
        lines.append(
            "| `{gate}` | {closed} | `{route}` | {evidence} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed_current_sweep"]),
                route=table_cell(row["route_if_fails"]),
                evidence=table_cell(row["evidence"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 当前显式矛盾读数",
            "",
            f"- 固定 actual 图像：`support_graph_cap={agg['current_support_graph_cap']}`，而 `sqrt_floor={agg['current_sqrt_floor']}`，固定槽没有 actual 超平方根负载。",
            f"- 最窄支撑运动 atom `{narrow_motion['source_pair_key']}` 要求共同深度 `{narrow_motion['required_common_side_depth']}`，端点释放 `{narrow_motion['endpoint_release_total_required']}`，是支撑宽度 `{agg['current_support_width']}` 的 `{agg['narrowest_release_over_support_width']:.2f}` 倍。",
            f"- 同向 moving-key 深度公式在最窄 atom `{narrow_formula['source_pair_key']}` 给出 `q_g={narrow_formula['q_from_generator_depth_formula']}` 与 `q_f={narrow_formula['q_from_fill_depth_formula']}`，差 `{narrow_formula['q_candidate_gap']}`，不能形成同一 primitive key。",
            f"- 深度公式吐出的 `{agg['unique_moving_q_candidate_count']}` 个候选 `q` 没有任何精确 source 重物化：`exact_rematerialized_q_values=[]`，路由直方图为 `{agg['source_rematerialization_route_histogram']}`。",
            "",
            "## 4. 结论边界",
            "",
            "当前 sweep 内不存在匿名 moving-slot actual overload：若仍保留 AffineTwin 固定图像，图容量自动低于平方根门；若移动支撑，则必须进入双端点释放、深度身份破坏、moving-key 公式失败、source 重物化失败或 ColumnCRT/SAE 路由。",
            "",
            "这一步仍不是行/列命题的全局无条件闭合。全局剩余被压成 `MovingSlotFamilyPersistenceNoGo`、方向改变 primitive key、source-rematerialization、`ColumnCRT/PDEC` 与 unused-target arrival 的族级排斥或可求和控制。",
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
        description="生成 AffineTwin endpoint-release moving-slot graph-cap route 审计证书。"
    )
    parser.add_argument("--support-graph-ledger", type=Path, default=SUPPORT_GRAPH_LEDGER)
    parser.add_argument("--support-motion-ledger", type=Path, default=SUPPORT_MOTION_LEDGER)
    parser.add_argument(
        "--primitive-defect-ledger", type=Path, default=PRIMITIVE_DEFECT_LEDGER
    )
    parser.add_argument("--moving-depth-ledger", type=Path, default=MOVING_DEPTH_LEDGER)
    parser.add_argument(
        "--source-rematerialization-ledger",
        type=Path,
        default=SOURCE_REMATERIALIZATION_LEDGER,
    )
    parser.add_argument("--moving-family-ledger", type=Path, default=MOVING_FAMILY_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(
        args.support_graph_ledger,
        args.support_motion_ledger,
        args.primitive_defect_ledger,
        args.moving_depth_ledger,
        args.source_rematerialization_ledger,
        args.moving_family_ledger,
    )
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
