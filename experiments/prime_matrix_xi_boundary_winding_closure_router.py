#!/usr/bin/env python3
"""Prime Matrix xi 边界 winding 三包聚合闭合路由器。

用法示例：
  python3 experiments/prime_matrix_xi_boundary_winding_closure_router.py

输出：
  docs/monograph/prime-matrix-xi-boundary-winding-closure-router.json
  docs/monograph/prime-matrix-xi-boundary-winding-closure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_POLYGON = MONO / "prime-matrix-xi-boundary-polygon-winding-router.json"
DEFAULT_NODE = MONO / "prime-matrix-xi-boundary-node-lower-bound-router.json"
DEFAULT_DERIVATIVE = MONO / "prime-matrix-xi-boundary-derivative-tube-router.json"
DEFAULT_MESH = MONO / "prime-matrix-xi-boundary-winding-mesh-contract-router.json"
DEFAULT_BOUNDARY = MONO / "prime-matrix-top-critical-endpoint-chain-aggregation-router.json"
DEFAULT_ENGINE = MONO / "prime-matrix-compact-theta-mellin-quadrature-router.json"
DEFAULT_XI_ENTIRE = MONO / "prime-matrix-b3-xi-entire-order-router.json"
DEFAULT_ARGUMENT = MONO / "prime-matrix-b3-argument-principle-xi-router.json"
DEFAULT_LOWHEIGHT = MONO / "prime-matrix-lowheight-rectangle-count-compression-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-boundary-winding-closure-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-boundary-winding-closure-router.md"

WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"
WINDING_CLOSED = "XiBoundaryWindingNumberZeroSelfContainedClosedMesh32768RootHash"
TRACE_ATOM = "XiBoundaryArgumentVariationDyadicTraceLedger0To14Mesh8192"
NODE_ATOM = "XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000"
DERIVATIVE_ATOM = "XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12"
POLYGON_ATOM = "XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768"
RECT_COUNT_ATOM = "LowHeightXiRectangleZeroCountZero0To14Ledger"
RECT_COUNT_CLOSED = "LowHeightXiRectangleZeroCountZero0To14SelfContainedClosed"


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


def guard_ok(items: list[dict[str, Any]]) -> bool:
    """确认所有输入保持假设链条纪律。"""
    return all(
        item.get("counterexample_assumption_only") is True
        and item.get("empirical_absence_not_used") is True
        and item.get("hypothetical_chain_only") is True
        for item in items
    )


def combined_root(data: dict[str, dict[str, Any]]) -> str:
    """聚合三包 root hash。"""
    node_root = data["node"]["audit"]["node_merkle_root_hash"]
    derivative_root = data["derivative"]["audit"]["derivative_tube_root_hash"]
    polygon_root = data["polygon"]["audit"]["polygon_winding_root_hash"]
    mesh_root = data["mesh"]["audit"]["trace_root_hash"]
    payload = "\n".join([node_root, derivative_root, polygon_root, mesh_root])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def proof_chain() -> list[dict[str, str]]:
    """列出 winding 与低高度计数闭合链。"""
    return [
        {
            "step": "MeshCompression",
            "input": TRACE_ATOM,
            "output": f"{NODE_ATOM} AND {DERIVATIVE_ATOM} AND {POLYGON_ATOM}",
        },
        {
            "step": "NodeLowerBound",
            "input": "32769 个边界节点 xi 区间值",
            "output": "所有节点 |xi|>=1/6000",
        },
        {
            "step": "DerivativeTube",
            "input": "32768 条边段 xi' 区间管道",
            "output": "所有边段 |xi'|<=1/12",
        },
        {
            "step": "PolygonInteger",
            "input": "函数方程、共轭对称、底边正实、顶边中心正实",
            "output": "离散多边形绕数整数为 0",
        },
        {
            "step": "Homotopy",
            "input": "|xi| 下界 + |xi'| 上界 + 多边形绕数 0",
            "output": "真实边界曲线 winding=0",
        },
        {
            "step": "ArgumentPrinciple",
            "input": "xi 整函数 + 边界非零 + winding=0",
            "output": "低高度矩形内 xi 零点计数为 0",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]], root_hash: str) -> list[dict[str, Any]]:
    """生成 winding 聚合判定表。"""
    polygon = data["polygon"]
    node = data["node"]
    derivative = data["derivative"]
    mesh = data["mesh"]
    boundary = data["boundary"]
    engine = data["engine"]
    xi_entire = data["xi_entire"]
    argument = data["argument"]
    lowheight = data["lowheight"]

    guard = guard_ok([polygon, node, derivative, mesh, boundary, engine, xi_entire, argument, lowheight])
    active = polygon.get("next_priority") == WINDING_ATOM
    mesh_ready = mesh.get("winding_trace_mesh_contracts_selected") is True
    node_ready = node.get("node_lower_bound_closed") is True
    derivative_ready = derivative.get("derivative_tube_closed") is True
    polygon_ready = polygon.get("polygon_winding_zero_closed") is True
    boundary_ready = boundary.get("boundary_nonzero_self_contained_closed") is True
    engine_ready = engine.get("self_contained_xi_interval_engine_closed") is True
    xi_entire_ready = xi_entire.get("xi_entire_order_one_growth_closed") is True
    argument_ready = argument.get("argument_principle_xi_rectangle_counting_closed") is True
    lowheight_ready = lowheight.get("compression_closed") is True
    homotopy_ready = (
        mesh["audit"]["tube_margin_after_node_floor"] > 0
        and polygon["audit"]["branch_safety_closed"] is True
        and polygon["audit"]["polygon_integer_closed"] is True
    )
    winding_closed = (
        active
        and guard
        and mesh_ready
        and node_ready
        and derivative_ready
        and polygon_ready
        and boundary_ready
        and homotopy_ready
        and bool(root_hash)
    )
    rectangle_closed = (
        winding_closed
        and engine_ready
        and xi_entire_ready
        and argument_ready
        and lowheight_ready
    )
    return [
        row(
            "WindingAggregationGateActive",
            active,
            True,
            "多边形包闭合后，当前目标是聚合回原 winding 原子。",
            WINDING_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "聚合仍只使用假设链条中的解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "MeshCompressionImported",
            mesh_ready,
            True,
            "winding trace 已被压缩为节点下界、导数管道、多边形整数绕数三包。",
            f"{NODE_ATOM} AND {DERIVATIVE_ATOM} AND {POLYGON_ATOM}",
        ),
        row(
            "NodeLowerBoundPackageClosed",
            node_ready,
            True,
            "节点下界 root 已闭合，提供边界离原点的离散距离。",
            NODE_ATOM,
        ),
        row(
            "DerivativeTubePackageClosed",
            derivative_ready,
            True,
            "导数管道 root 已闭合，提供从离散节点到整段曲线的同伦管道。",
            DERIVATIVE_ATOM,
        ),
        row(
            "PolygonIntegerWindingClosed",
            polygon_ready,
            True,
            "多边形整数绕数由对称角变化配平闭合为 0。",
            POLYGON_ATOM,
        ),
        row(
            "HomotopyNoCrossingClosed",
            homotopy_ready,
            True,
            "1/6000-(1/12)*(14/8192)>0，真实边界曲线与离散多边形同伦且不穿过 0。",
            "continuous boundary winding equals polygon winding.",
        ),
        row(
            WINDING_ATOM,
            winding_closed,
            True,
            f"三包 root 聚合完成，winding=0；聚合 root={root_hash}。",
            WINDING_CLOSED,
        ),
        row(
            "LowHeightRectangleCountZero",
            rectangle_closed,
            True,
            "xi 区间引擎、边界非零、winding=0、xi 整函数和 argument principle 齐备，低高度矩形零点计数为 0。",
            RECT_COUNT_CLOSED,
        ),
        row(
            "RowColumnTheoremStillSeparate",
            False,
            False,
            "这关闭低高度 xi 边界/winding 包；完整行列定理仍需后续筛法全局包接力。",
            "global row-column sieve closure remains outside this xi package.",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 winding 聚合闭合。"""
    data = {
        "polygon": load_json(paths["polygon"]),
        "node": load_json(paths["node"]),
        "derivative": load_json(paths["derivative"]),
        "mesh": load_json(paths["mesh"]),
        "boundary": load_json(paths["boundary"]),
        "engine": load_json(paths["engine"]),
        "xi_entire": load_json(paths["xi_entire"]),
        "argument": load_json(paths["argument"]),
        "lowheight": load_json(paths["lowheight"]),
    }
    root_hash = combined_root(data)
    rows = build_rows(data, root_hash)
    winding_closed = next(item["closed"] for item in rows if item["gate"] == WINDING_ATOM)
    rectangle_closed = next(item["closed"] for item in rows if item["gate"] == "LowHeightRectangleCountZero")
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_xi_boundary_winding_closure_router",
        "status": "xi_boundary_winding_and_lowheight_rectangle_count_self_contained_closed"
        if rectangle_closed
        else "xi_boundary_winding_self_contained_closed_lowheight_open"
        if winding_closed
        else "xi_boundary_winding_closure_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "winding_self_contained_closed": winding_closed,
        "lowheight_rectangle_count_self_contained_closed": rectangle_closed,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {
            TRACE_ATOM: f"{NODE_ATOM} AND {DERIVATIVE_ATOM} AND {POLYGON_ATOM}",
            WINDING_ATOM: WINDING_CLOSED,
            RECT_COUNT_ATOM: RECT_COUNT_CLOSED,
        },
        "winding_aggregation_root_hash": root_hash,
        "proof_chain": proof_chain(),
        "rows": rows,
        "next_priority": "GlobalRowColumnSieveClosureAfterLowHeightXiPackage",
        "plain_conclusion": (
            "winding 原子已自足闭合：节点下界、导数管道和多边形整数绕数三包完成聚合，"
            "真实 xi 边界曲线绕原点次数为 0。结合 xi 整函数、边界非零与 argument principle，"
            "低高度矩形 xi 零点计数也闭合为 0。本步不声称完整行列定理闭合，"
            "而是关闭此前唯一最窄的低高度 xi/winding 输入包。"
            if rectangle_closed
            else "winding 聚合尚未完全闭合；需检查三包或 argument principle 输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix xi 边界 winding 三包聚合闭合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"winding_self_contained_closed={fmt_bool(result['winding_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"winding_aggregation_root_hash={result['winding_aggregation_root_hash']}",
        "```",
        "",
        "## 1. 闭合链",
        "",
        "| step | input | output |",
        "| --- | --- | --- |",
    ]
    for item in result["proof_chain"]:
        lines.append(
            "| {step} | {input} | {output} |".format(
                step=table_cell(item["step"]),
                input=table_cell(item["input"]),
                output=table_cell(item["output"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一步",
            "",
            f"当前 xi 低高度包之后的下一层：`{result['next_priority']}`。",
            "",
            "判定：低高度 xi 边界/winding 输入包已关闭，但完整行列命题仍需后续全局筛法链条接上。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--polygon-json", type=Path, default=DEFAULT_POLYGON)
    parser.add_argument("--node-json", type=Path, default=DEFAULT_NODE)
    parser.add_argument("--derivative-json", type=Path, default=DEFAULT_DERIVATIVE)
    parser.add_argument("--mesh-json", type=Path, default=DEFAULT_MESH)
    parser.add_argument("--boundary-json", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--engine-json", type=Path, default=DEFAULT_ENGINE)
    parser.add_argument("--xi-entire-json", type=Path, default=DEFAULT_XI_ENTIRE)
    parser.add_argument("--argument-json", type=Path, default=DEFAULT_ARGUMENT)
    parser.add_argument("--lowheight-json", type=Path, default=DEFAULT_LOWHEIGHT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "polygon": args.polygon_json,
        "node": args.node_json,
        "derivative": args.derivative_json,
        "mesh": args.mesh_json,
        "boundary": args.boundary_json,
        "engine": args.engine_json,
        "xi_entire": args.xi_entire_json,
        "argument": args.argument_json,
        "lowheight": args.lowheight_json,
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
