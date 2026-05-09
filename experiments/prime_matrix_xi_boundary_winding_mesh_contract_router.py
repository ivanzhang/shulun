#!/usr/bin/env python3
"""Prime Matrix xi 边界 winding 网格合同压缩路由器。

用法示例：
  python3 experiments/prime_matrix_xi_boundary_winding_mesh_contract_router.py

输出：
  docs/monograph/prime-matrix-xi-boundary-winding-mesh-contract-router.json
  docs/monograph/prime-matrix-xi-boundary-winding-mesh-contract-router.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-xi-boundary-winding-trace-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-boundary-winding-mesh-contract-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-boundary-winding-mesh-contract-router.md"

TRACE_HELPER = ROOT / "experiments" / "prime_matrix_xi_boundary_winding_trace_router.py"

OLD_ATOM = "XiBoundaryArgumentVariationDyadicTraceLedger0To14Mesh8192"
NODE_LOWER_ATOM = "XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000"
DERIVATIVE_TUBE_ATOM = "XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12"
POLYGON_WINDING_ATOM = "XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

SAMPLES_PER_SIDE = 8192
NODE_FLOOR = Fraction(1, 6000)
DERIVATIVE_CONTRACT = Fraction(1, 12)
MAX_BOUNDARY_STEP = Fraction(14, SAMPLES_PER_SIDE)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def load_trace_helper() -> Any:
    """载入上一层 winding 侦察函数。"""
    spec = importlib.util.spec_from_file_location("winding_trace_helper", TRACE_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load winding trace helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def mesh_audit(samples_per_side: int) -> dict[str, Any]:
    """生成细网格 winding 侦察摘要和 root hash。"""
    helper = load_trace_helper()
    points = helper.boundary_points(samples_per_side)
    values = [helper.xi_value(point) for point in points]
    total_angle = 0.0
    max_step_angle = 0.0
    min_abs = float("inf")
    min_abs_index = 0
    max_adjacent_ratio = 0.0
    quantized_nodes: list[str] = []
    for index, (point, value) in enumerate(zip(points, values)):
        abs_value = abs(value)
        if abs_value < min_abs:
            min_abs = abs_value
            min_abs_index = index
        quantized_nodes.append(
            f"{index}:{point.real:.18e}:{point.imag:.18e}:{value.real:.18e}:{value.imag:.18e}"
        )
    for left_value, right_value, left_point, right_point in zip(values, values[1:] + values[:1], points, points[1:] + points[:1]):
        total_angle += cmath.phase(right_value / left_value)
        max_step_angle = max(max_step_angle, abs(cmath.phase(right_value / left_value)))
        step_length = abs(right_point - left_point)
        if step_length:
            max_adjacent_ratio = max(max_adjacent_ratio, abs(right_value - left_value) / step_length)
    root_hash = hashlib.sha256("\n".join(quantized_nodes).encode("utf-8")).hexdigest()
    winding = total_angle / (2 * 3.1415926535897932384626433832795028841971693993751)
    tube_loss = float(DERIVATIVE_CONTRACT * MAX_BOUNDARY_STEP)
    return {
        "samples_per_side": samples_per_side,
        "edge_count": 4 * samples_per_side,
        "node_count": len(points),
        "trace_root_hash": root_hash,
        "winding_float": winding,
        "winding_rounded": round(winding),
        "rounding_error": abs(winding - round(winding)),
        "total_angle": total_angle,
        "max_step_angle": max_step_angle,
        "min_abs_value": min_abs,
        "min_abs_index": min_abs_index,
        "min_abs_point_re": points[min_abs_index].real,
        "min_abs_point_im": points[min_abs_index].imag,
        "max_adjacent_displacement_ratio": max_adjacent_ratio,
        "node_floor": str(NODE_FLOOR),
        "node_floor_float": float(NODE_FLOOR),
        "node_floor_audit_margin": min_abs - float(NODE_FLOOR),
        "derivative_contract": str(DERIVATIVE_CONTRACT),
        "derivative_contract_float": float(DERIVATIVE_CONTRACT),
        "derivative_contract_audit_margin": float(DERIVATIVE_CONTRACT) - max_adjacent_ratio,
        "max_boundary_step": str(MAX_BOUNDARY_STEP),
        "max_boundary_step_float": float(MAX_BOUNDARY_STEP),
        "tube_loss_under_contract": tube_loss,
        "tube_margin_after_node_floor": float(NODE_FLOOR) - tube_loss,
        "audit_supports_node_floor": min_abs > float(NODE_FLOOR),
        "audit_supports_derivative_contract": max_adjacent_ratio < float(DERIVATIVE_CONTRACT),
        "audit_supports_polygon_winding_zero": round(winding) == 0 and abs(winding) < 1e-8,
    }


def proof_contract() -> list[str]:
    """写出网格合同证明链。"""
    return [
        "在 32768 条 dyadic 边界小段上登记 xi 节点区间值，并证明每个节点 |xi|>=1/6000。",
        "在每条小段上登记 xi' 区间包络，并证明 |xi'|<=1/12。",
        "最大边界小段长度为 14/8192，因此任意段内偏移至多 (1/12)*(14/8192)。",
        "有理余量 1/6000-(1/12)*(14/8192)>0，所以整段像不穿过 0。",
        "离散多边形的每步辐角增量由点积/叉积有理区间确定，总和落在 (-pi,pi) 且整数绕数为 0。",
        "节点下界、导数管道和多边形绕数三项齐备时，XiBoundaryWindingNumberZeroIntervalCertificate0To14 闭合。",
    ]


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成网格合同判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    contract_positive = audit["tube_margin_after_node_floor"] > 0
    return [
        row(
            "WindingTraceMeshGateActive",
            active,
            True,
            "上一层已把 winding 压成有限 dyadic argument-variation trace。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只压缩假设链条中的有限 trace 证书。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "FloatAuditSupportsMeshContracts",
            audit["audit_supports_node_floor"]
            and audit["audit_supports_derivative_contract"]
            and audit["audit_supports_polygon_winding_zero"],
            False,
            (
                f"侦察 min|xi|={audit['min_abs_value']:.6e}>1/6000，"
                f"max adjacent ratio={audit['max_adjacent_displacement_ratio']:.6f}<1/12，polygon winding=0。"
            ),
            "不能作为自足证明，只用于确定合同常数。",
        ),
        row(
            "TubeMarginArithmeticClosed",
            contract_positive,
            True,
            "1/6000-(1/12)*(14/8192)>0，节点下界加导数管道足以排除段内穿零。",
            "integer arithmetic closed.",
        ),
        row(
            "NodeLowerBoundStillMissing",
            False,
            False,
            "需 interval trace/hash 逐节点证明 |xi|>=1/6000。",
            NODE_LOWER_ATOM,
        ),
        row(
            "DerivativeTubeStillMissing",
            False,
            False,
            "需 interval trace/hash 逐段证明 |xi'|<=1/12。",
            DERIVATIVE_TUBE_ATOM,
        ),
        row(
            "PolygonWindingIntegerStillMissing",
            False,
            False,
            "需有理点积/叉积区间累加证明离散多边形绕数整数为 0。",
            POLYGON_WINDING_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "winding trace 已压成节点下界、导数管道和多边形整数绕数三包。",
            f"{NODE_LOWER_ATOM} AND {DERIVATIVE_TUBE_ATOM} AND {POLYGON_WINDING_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 winding 网格合同压缩路由。"""
    previous = load_json(paths["previous"])
    audit = mesh_audit(SAMPLES_PER_SIDE)
    rows = build_rows(previous, audit)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}] + [TRACE_HELPER]
    return {
        "certificate_type": "prime_matrix_xi_boundary_winding_mesh_contract_router",
        "status": "winding_trace_reduced_to_node_tube_polygon_contracts_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "winding_trace_mesh_contracts_selected": True,
        "winding_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            OLD_ATOM: f"{NODE_LOWER_ATOM} AND {DERIVATIVE_TUBE_ATOM} AND {POLYGON_WINDING_ATOM}",
        },
        "audit": audit,
        "proof_contract": proof_contract(),
        "rows": rows,
        "next_priority": NODE_LOWER_ATOM,
        "secondary_priority": DERIVATIVE_TUBE_ATOM,
        "tertiary_priority": POLYGON_WINDING_ATOM,
        "downstream_priority": WINDING_ATOM,
        "plain_conclusion": (
            "winding trace 已进一步压缩为三项有限合同：节点 |xi|>=1/6000、边段 |xi'|<=1/12、"
            "离散多边形绕数为 0。有理管道余量为正；浮点侦察支持这些常数。严格自足仍需把三包实际 interval trace/hash 物化。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix xi 边界 winding 网格合同压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"winding_trace_mesh_contracts_selected={fmt_bool(result['winding_trace_mesh_contracts_selected'])}",
        f"winding_self_contained_closed={fmt_bool(result['winding_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 网格侦察与合同",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| edge count | `{audit['edge_count']}` |",
        f"| node count | `{audit['node_count']}` |",
        f"| trace root hash | `{audit['trace_root_hash']}` |",
        f"| winding float | `{audit['winding_float']:.12e}` |",
        f"| max step angle | `{audit['max_step_angle']:.12f}` |",
        f"| min abs value | `{audit['min_abs_value']:.12e}` |",
        f"| node floor | `{audit['node_floor']}` |",
        f"| node floor audit margin | `{audit['node_floor_audit_margin']:.12e}` |",
        f"| max adjacent displacement ratio | `{audit['max_adjacent_displacement_ratio']:.12f}` |",
        f"| derivative contract | `{audit['derivative_contract']}` |",
        f"| derivative contract audit margin | `{audit['derivative_contract_audit_margin']:.12f}` |",
        f"| tube loss under contract | `{audit['tube_loss_under_contract']:.12e}` |",
        f"| tube margin after node floor | `{audit['tube_margin_after_node_floor']:.12e}` |",
        "",
        "## 2. 证明合同",
        "",
    ]
    for index, item in enumerate(result["proof_contract"], start=1):
        lines.append(f"{index}. {item}")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            f"优先攻：`{result['next_priority']}`。",
            f"随后攻：`{result['secondary_priority']}`。",
            f"最后聚合：`{result['tertiary_priority']}`。",
            "",
            "判定：最后剩余已经从 winding 泛命题压成三个有限 trace 子证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
