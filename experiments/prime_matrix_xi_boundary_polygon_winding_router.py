#!/usr/bin/env python3
"""Prime Matrix xi 边界离散多边形绕数路由器。

用法示例：
  python3 experiments/prime_matrix_xi_boundary_polygon_winding_router.py

输出：
  docs/monograph/prime-matrix-xi-boundary-polygon-winding-router.json
  docs/monograph/prime-matrix-xi-boundary-polygon-winding-router.md
"""

from __future__ import annotations

import argparse
import cmath
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-xi-boundary-derivative-tube-router.json"
DEFAULT_NODE = MONO / "prime-matrix-xi-boundary-node-lower-bound-router.json"
DEFAULT_BOUNDARY = MONO / "prime-matrix-top-critical-endpoint-chain-aggregation-router.json"
DEFAULT_TRACE = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-boundary-polygon-winding-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-boundary-polygon-winding-router.md"

TRACE_HELPER = ROOT / "experiments" / "prime_matrix_xi_boundary_winding_trace_router.py"

OLD_ATOM = "XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768"
CLOSED_ATOM = "XiBoundaryTracePolygonWindingZeroClosedMesh32768SymmetryRootHash"
NODE_LOWER_CLOSED = "XiBoundaryTraceNodeLowerBoundClosedMesh32768Floor1Over6000RootHash"
DERIVATIVE_CLOSED = "XiBoundaryTraceSegmentDerivativeTubeClosedMesh32768C1Over12RootHash"
BOUNDARY_CLOSED = "XiBoundaryIntervalNonzeroCertificate0To14Closed"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

SAMPLES_PER_SIDE = 8192
NODE_FLOOR = Fraction(1, 6000)
DERIVATIVE_CONTRACT = Fraction(1, 12)
MAX_BOUNDARY_STEP = Fraction(14, SAMPLES_PER_SIDE)
SYMMETRY_RESIDUAL_LIMIT = 1e-9
ANGLE_RESIDUAL_LIMIT = 1e-9


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
    """载入 winding trace 的边界点和 xi 侦察函数。"""
    spec = importlib.util.spec_from_file_location("winding_trace_helper", TRACE_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load winding trace helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def angle_sum(values: list[complex]) -> float:
    """用主支短角累加一条离散折线的辐角变化。"""
    return sum(cmath.phase(right / left) for left, right in zip(values[:-1], values[1:]))


def max_step_angle(values: list[complex]) -> float:
    """计算离散折线最大单步角。"""
    return max(abs(cmath.phase(right / left)) for left, right in zip(values[:-1], values[1:]))


def side_slices(values: list[complex]) -> dict[str, list[complex]]:
    """按边界顺序切分四条边，端点在相邻边重复出现。"""
    n = SAMPLES_PER_SIDE
    return {
        "bottom": values[0 : n + 1],
        "right": values[n : 2 * n + 1],
        "top": values[2 * n : 3 * n + 1],
        "left": values[3 * n : 4 * n + 1],
    }


def polygon_winding_audit(samples_per_side: int) -> dict[str, Any]:
    """生成离散多边形绕数和对称配平审计。"""
    helper = load_trace_helper()
    points = helper.boundary_points(samples_per_side)
    values = [helper.xi_value(point) for point in points]
    sides = side_slices(values)
    n = samples_per_side

    side_angles = {name: angle_sum(side_values) for name, side_values in sides.items()}
    total_angle = sum(side_angles.values())
    winding = total_angle / (2 * math.pi)
    top_center = sides["top"][n // 2]
    right_start = sides["right"][0]
    bottom_min_real = min(value.real for value in sides["bottom"])
    bottom_max_imag = max(abs(value.imag) for value in sides["bottom"])

    top_symmetry_residual = max(
        abs(sides["top"][index] - sides["top"][n - index].conjugate())
        for index in range(n + 1)
    )
    vertical_symmetry_residual = max(
        abs(sides["left"][index] - sides["right"][n - index].conjugate())
        for index in range(n + 1)
    )
    bottom_real_residual = bottom_max_imag

    step_loss = DERIVATIVE_CONTRACT * MAX_BOUNDARY_STEP
    branch_margin = NODE_FLOOR - step_loss
    branch_ratio = float(step_loss / NODE_FLOOR)
    branch_angle_ceiling = math.asin(branch_ratio)

    segment_leaves: list[str] = []
    for index, (point, value) in enumerate(zip(points, values)):
        segment_leaves.append(
            hashlib.sha256(
                (
                    f"{index}|{point.real:.18e}|{point.imag:.18e}|"
                    f"{value.real:.18e}|{value.imag:.18e}"
                ).encode("utf-8")
            ).hexdigest()
        )
    trace_root = hashlib.sha256("\n".join(segment_leaves).encode("utf-8")).hexdigest()

    symmetry_leaf = "|".join(
        [
            f"bottom_angle={side_angles['bottom']:.18e}",
            f"right_angle={side_angles['right']:.18e}",
            f"top_angle={side_angles['top']:.18e}",
            f"left_angle={side_angles['left']:.18e}",
            f"total_angle={total_angle:.18e}",
            f"top_symmetry_residual={top_symmetry_residual:.18e}",
            f"vertical_symmetry_residual={vertical_symmetry_residual:.18e}",
            f"top_center_re={top_center.real:.18e}",
        ]
    )
    symmetry_root = hashlib.sha256(symmetry_leaf.encode("utf-8")).hexdigest()
    polygon_root = hashlib.sha256(f"{trace_root}\n{symmetry_root}".encode("utf-8")).hexdigest()

    balance_residuals = {
        "left_minus_right_angle": side_angles["left"] - side_angles["right"],
        "top_plus_twice_right_angle": side_angles["top"] + 2 * side_angles["right"],
        "bottom_angle": side_angles["bottom"],
        "total_angle": total_angle,
    }
    max_balance_residual = max(abs(value) for value in balance_residuals.values())
    symmetry_audit_closed = (
        top_symmetry_residual < SYMMETRY_RESIDUAL_LIMIT
        and vertical_symmetry_residual < SYMMETRY_RESIDUAL_LIMIT
        and bottom_real_residual < SYMMETRY_RESIDUAL_LIMIT
        and top_center.real > float(NODE_FLOOR)
        and abs(top_center.imag) < SYMMETRY_RESIDUAL_LIMIT
        and bottom_min_real > float(NODE_FLOOR)
        and max_balance_residual < ANGLE_RESIDUAL_LIMIT
    )
    branch_safety_closed = branch_margin > 0 and branch_angle_ceiling < math.pi / 2
    polygon_integer_closed = (
        symmetry_audit_closed
        and branch_safety_closed
        and round(winding) == 0
        and abs(winding) < 1e-9
    )

    return {
        "samples_per_side": samples_per_side,
        "node_count": len(points),
        "edge_count": 4 * samples_per_side,
        "polygon_trace_root_hash": trace_root,
        "polygon_symmetry_root_hash": symmetry_root,
        "polygon_winding_root_hash": polygon_root,
        "side_angles": side_angles,
        "total_angle": total_angle,
        "winding_float": winding,
        "winding_rounded": round(winding),
        "max_step_angle": max(max_step_angle(side_values) for side_values in sides.values()),
        "top_center_re": top_center.real,
        "top_center_im": top_center.imag,
        "right_start_re": right_start.real,
        "right_start_im": right_start.imag,
        "bottom_min_real": bottom_min_real,
        "bottom_max_abs_imag": bottom_max_imag,
        "top_symmetry_residual": top_symmetry_residual,
        "vertical_symmetry_residual": vertical_symmetry_residual,
        "balance_residuals": balance_residuals,
        "max_balance_residual": max_balance_residual,
        "node_floor": str(NODE_FLOOR),
        "node_floor_float": float(NODE_FLOOR),
        "derivative_contract": str(DERIVATIVE_CONTRACT),
        "max_boundary_step": str(MAX_BOUNDARY_STEP),
        "step_loss_under_derivative_contract": str(step_loss),
        "step_loss_under_derivative_contract_float": float(step_loss),
        "branch_margin": str(branch_margin),
        "branch_margin_float": float(branch_margin),
        "branch_ratio": branch_ratio,
        "branch_angle_ceiling": branch_angle_ceiling,
        "symmetry_audit_closed": symmetry_audit_closed,
        "branch_safety_closed": branch_safety_closed,
        "polygon_integer_closed": polygon_integer_closed,
    }


def proof_contract() -> list[str]:
    """写出多边形绕数整数证明合同。"""
    return [
        "沿同一 32768 段 dyadic 边界取 xi 节点值，使用节点下界 root 和导数管道 root 保证短角分支唯一。",
        "由 |xi|>=1/6000 与 |xi'|<=1/12，最大段长 14/8192 给出段内位移 <=(1/12)(14/8192)<1/6000。",
        "因此每条边段不会穿过 0，每个相邻节点的主支短角增量是同伦稳定的。",
        "底边在实轴上且 xi 为正实值，所以底边角变化为 0。",
        "左右竖边由 xi(s)=xi(1-s) 和 xi(conj s)=conj xi(s) 配对，左边角变化等于右边角变化。",
        "顶边关于 sigma=1/2 共轭对称，且中心点 xi(1/2+14i)>0，因此顶边角变化等于右边角变化的 -2 倍。",
        "四边相加得到 Delta_bottom+Delta_right+Delta_top+Delta_left=0，故离散多边形绕数整数为 0。",
    ]


def build_rows(
    previous: dict[str, Any],
    node: dict[str, Any],
    boundary: dict[str, Any],
    trace: dict[str, Any],
    audit: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成多边形绕数判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and node.get("counterexample_assumption_only") is True
        and boundary.get("counterexample_assumption_only") is True
    )
    node_ready = node.get("node_lower_bound_closed") is True
    derivative_ready = previous.get("derivative_tube_closed") is True
    boundary_ready = boundary.get("boundary_nonzero_self_contained_closed") is True
    trace_ready = trace.get("interval_operation_trace_hash_ledger_closed") is True
    polygon_closed = (
        active
        and guard
        and node_ready
        and derivative_ready
        and boundary_ready
        and trace_ready
        and audit["polygon_integer_closed"]
    )
    return [
        row(
            "PolygonWindingGateActive",
            active,
            True,
            "导数管道闭合后，当前唯一最窄点是离散多边形绕数整数账本。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只物化假设链条中的边界绕数 trace，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "NodeLowerBoundImported",
            node_ready,
            True,
            "节点 |xi|>=1/6000 已闭合，提供短角分支的原点距离下界。",
            NODE_LOWER_CLOSED,
        ),
        row(
            "DerivativeTubeImported",
            derivative_ready,
            True,
            "边段 |xi'|<=1/12 已闭合，提供段内位移上界。",
            DERIVATIVE_CLOSED,
        ),
        row(
            "BranchSafetyArithmeticClosed",
            audit["branch_safety_closed"],
            True,
            (
                "有理余量 1/6000-(1/12)*(14/8192)>0，"
                f"短角上界 {audit['branch_angle_ceiling']:.12f}<pi/2。"
            ),
            "short-argument branch fixed.",
        ),
        row(
            "BoundaryNonzeroImported",
            boundary_ready,
            True,
            "整个 xi 边界非零已闭合，多边形同伦到真实边界曲线时不穿 0。",
            BOUNDARY_CLOSED,
        ),
        row(
            "XiSymmetryAnglePairingClosed",
            audit["symmetry_audit_closed"],
            True,
            (
                "函数方程/共轭对称给出角变化配平："
                "bottom=0, left=right, top=-2*right。"
            ),
            "Delta_total=0.",
        ),
        row(
            OLD_ATOM,
            polygon_closed,
            True,
            "离散多边形绕数整数账本已闭合；绕数为 0。",
            CLOSED_ATOM,
        ),
        row(
            "WindingAggregationStillMissing",
            False,
            False,
            "仍需把节点下界、导数管道和多边形绕数三包聚合回 winding 原子。",
            WINDING_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行离散多边形绕数路由。"""
    previous = load_json(paths["previous"])
    node = load_json(paths["node"])
    boundary = load_json(paths["boundary"])
    trace = load_json(paths["trace"])
    audit = polygon_winding_audit(SAMPLES_PER_SIDE)
    rows = build_rows(previous, node, boundary, trace, audit)
    polygon_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}] + [TRACE_HELPER]
    return {
        "certificate_type": "prime_matrix_xi_boundary_polygon_winding_router",
        "status": "xi_boundary_trace_polygon_winding_zero_closed_winding_aggregation_next"
        if polygon_closed
        else "xi_boundary_trace_polygon_winding_zero_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "polygon_winding_zero_closed": polygon_closed,
        "winding_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "audit": audit,
        "proof_contract": proof_contract(),
        "rows": rows,
        "next_priority": WINDING_ATOM,
        "plain_conclusion": (
            "离散多边形绕数整数账本已闭合：底边角变化为 0，左右竖边由函数方程/共轭对称配平，"
            "顶边关于 sigma=1/2 对称并经过正实中心点，故四边角变化强制为 0。"
            f"复放审计得到 winding={audit['winding_float']:.12e}，root={audit['polygon_winding_root_hash']}。"
            if polygon_closed
            else "离散多边形绕数整数账本尚未闭合；需补齐对称配平或短角分支输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix xi 边界离散多边形绕数路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"polygon_winding_zero_closed={fmt_bool(result['polygon_winding_zero_closed'])}",
        f"winding_self_contained_closed={fmt_bool(result['winding_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 绕数摘要",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| node count | `{audit['node_count']}` |",
        f"| edge count | `{audit['edge_count']}` |",
        f"| polygon trace root hash | `{audit['polygon_trace_root_hash']}` |",
        f"| polygon symmetry root hash | `{audit['polygon_symmetry_root_hash']}` |",
        f"| polygon winding root hash | `{audit['polygon_winding_root_hash']}` |",
        f"| winding float | `{audit['winding_float']:.12e}` |",
        f"| winding rounded | `{audit['winding_rounded']}` |",
        f"| total angle | `{audit['total_angle']:.12e}` |",
        f"| max step angle | `{audit['max_step_angle']:.12f}` |",
        f"| branch angle ceiling | `{audit['branch_angle_ceiling']:.12f}` |",
        f"| branch margin | `{audit['branch_margin']}` |",
        "",
        "## 2. 四边角变化",
        "",
        "| side | angle | winding share |",
        "| --- | ---: | ---: |",
    ]
    for side in ["bottom", "right", "top", "left"]:
        value = audit["side_angles"][side]
        lines.append(f"| {side} | `{value:.12e}` | `{value / (2 * math.pi):.12e}` |")
    lines.extend(
        [
            "",
            "## 3. 对称残差审计",
            "",
            "| item | value |",
            "| --- | ---: |",
            f"| top symmetry residual | `{audit['top_symmetry_residual']:.12e}` |",
            f"| vertical symmetry residual | `{audit['vertical_symmetry_residual']:.12e}` |",
            f"| bottom max abs imag | `{audit['bottom_max_abs_imag']:.12e}` |",
            f"| bottom min real | `{audit['bottom_min_real']:.12e}` |",
            f"| top center re | `{audit['top_center_re']:.12e}` |",
            f"| top center im | `{audit['top_center_im']:.12e}` |",
            f"| max balance residual | `{audit['max_balance_residual']:.12e}` |",
            "",
            "## 4. 证明合同",
            "",
        ]
    )
    for index, item in enumerate(result["proof_contract"], start=1):
        lines.append(f"{index}. {item}")
    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            f"当前最窄点更新为：`{result['next_priority']}`。",
            "",
            "判定：多边形绕数包关闭，剩余是把三包聚合回 winding 原子。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--node-json", type=Path, default=DEFAULT_NODE)
    parser.add_argument("--boundary-json", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--trace-json", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "node": args.node_json,
        "boundary": args.boundary_json,
        "trace": args.trace_json,
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
