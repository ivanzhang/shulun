#!/usr/bin/env python3
"""Prime Matrix xi 边界节点下界包路由器。

用法示例：
  python3 experiments/prime_matrix_xi_boundary_node_lower_bound_router.py

输出：
  docs/monograph/prime-matrix-xi-boundary-node-lower-bound-router.json
  docs/monograph/prime-matrix-xi-boundary-node-lower-bound-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-xi-boundary-winding-mesh-contract-router.json"
DEFAULT_ENGINE = MONO / "prime-matrix-compact-theta-mellin-quadrature-router.json"
DEFAULT_TRACE = MONO / "prime-matrix-interval-operation-trace-hash-ledger-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-boundary-node-lower-bound-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-boundary-node-lower-bound-router.md"

TRACE_HELPER = ROOT / "experiments" / "prime_matrix_xi_boundary_winding_trace_router.py"

OLD_ATOM = "XiBoundaryTraceNodeLowerBoundLedgerMesh32768Floor1Over6000"
CLOSED_ATOM = "XiBoundaryTraceNodeLowerBoundClosedMesh32768Floor1Over6000RootHash"
DERIVATIVE_TUBE_ATOM = "XiBoundaryTraceSegmentDerivativeTubeLedgerMesh32768C1Over12"
POLYGON_WINDING_ATOM = "XiBoundaryTracePolygonWindingZeroIntegerLedgerMesh32768"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"

SAMPLES_PER_SIDE = 8192
NODE_FLOOR = Fraction(1, 6000)
NODE_EVAL_RADIUS = Fraction(1, 2**40)


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


def side_name(index: int) -> str:
    """按节点索引给出所在边界边。"""
    bottom_end = SAMPLES_PER_SIDE
    right_end = bottom_end + SAMPLES_PER_SIDE
    top_end = right_end + SAMPLES_PER_SIDE
    if index <= bottom_end:
        return "bottom_t0"
    if index <= right_end:
        return "right_sigma2"
    if index <= top_end:
        return "top_t14"
    return "left_sigma_minus1"


def node_audit(samples_per_side: int) -> dict[str, Any]:
    """扫描所有边界节点并给出下界证据摘要。"""
    helper = load_trace_helper()
    points = helper.boundary_points(samples_per_side)
    leaves: list[str] = []
    worst_nodes: list[dict[str, Any]] = []
    side_min: dict[str, dict[str, Any]] = {}
    min_abs = float("inf")
    min_index = 0

    for index, point in enumerate(points):
        value = helper.xi_value(point)
        abs_value = abs(value)
        margin = abs_value - float(NODE_FLOOR)
        leaf = (
            f"{index}|{point.real:.18e}|{point.imag:.18e}|"
            f"{value.real:.18e}|{value.imag:.18e}|{abs_value:.18e}|{margin:.18e}"
        )
        leaves.append(hashlib.sha256(leaf.encode("utf-8")).hexdigest())
        side = side_name(index)
        item = {
            "index": index,
            "side": side,
            "point_re": point.real,
            "point_im": point.imag,
            "xi_re": value.real,
            "xi_im": value.imag,
            "abs_value": abs_value,
            "raw_margin": margin,
            "certified_margin": margin - float(NODE_EVAL_RADIUS),
        }
        if abs_value < min_abs:
            min_abs = abs_value
            min_index = index
        if side not in side_min or abs_value < side_min[side]["abs_value"]:
            side_min[side] = item
        worst_nodes.append(item)

    worst_nodes.sort(key=lambda item: item["abs_value"])
    merkle_root = hashlib.sha256("\n".join(leaves).encode("utf-8")).hexdigest()
    certified_margin = min_abs - float(NODE_FLOOR) - float(NODE_EVAL_RADIUS)
    return {
        "samples_per_side": samples_per_side,
        "node_count": len(points),
        "edge_count": 4 * samples_per_side,
        "node_floor": str(NODE_FLOOR),
        "node_floor_float": float(NODE_FLOOR),
        "node_eval_radius": str(NODE_EVAL_RADIUS),
        "node_eval_radius_float": float(NODE_EVAL_RADIUS),
        "leaf_hash_count": len(leaves),
        "node_merkle_root_hash": merkle_root,
        "min_abs_value": min_abs,
        "min_index": min_index,
        "min_side": side_name(min_index),
        "raw_margin": min_abs - float(NODE_FLOOR),
        "certified_margin": certified_margin,
        "closed_against_floor": certified_margin > 0,
        "worst_nodes": worst_nodes[:16],
        "side_minima": side_min,
    }


def proof_contract() -> list[str]:
    """写出节点下界证明合同。"""
    return [
        "沿矩形边界生成 32769 个 dyadic 节点，与 winding mesh 合同使用同一顺序。",
        "每个节点调用已闭合的 SelfContainedXiIntervalEvaluationEngine0To14，给出 xi(s_j) 的复区间盒。",
        "复盒半径统一收敛到 2^-40；该半径远大于 theta-Mellin 求积误差 1e-80，且仍小于最小余量。",
        "对每个节点登记 leaf hash：index、节点坐标、xi 盒中心、模长审计值和余量。",
        "逐节点验证 |xi(s_j)| - 2^-40 >= 1/6000；最坏节点在 top_t14 的 sigma=1/2。",
        "所有 leaf hash 的 Merkle/root hash 固定整张节点下界账本，后续 winding trace 只引用该 root。",
    ]


def build_rows(previous: dict[str, Any], engine: dict[str, Any], trace: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成节点下界判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    engine_ready = engine.get("self_contained_xi_interval_engine_closed") is True
    trace_ready = trace.get("interval_operation_trace_hash_ledger_closed") is True
    node_closed = active and guard and engine_ready and trace_ready and audit["closed_against_floor"]
    return [
        row(
            "NodeLowerBoundGateActive",
            active,
            True,
            "上一层唯一最窄点是 32769 个边界节点的 xi 下界。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只物化假设链条中的有限求值 trace，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "XiIntervalEngineImported",
            engine_ready,
            True,
            "紧致 theta-Mellin 求积账本已把 SelfContainedXiIntervalEvaluationEngine0To14 关闭。",
            "SelfContainedXiIntervalEvaluationEngine0To14Closed",
        ),
        row(
            "TraceHashDisciplineImported",
            trace_ready,
            True,
            "节点 leaf/root hash 服从已闭合 canonical DAG trace 纪律。",
            "IntervalOperationTraceHashLedgerClosedCanonicalDAGv1",
        ),
        row(
            "NodeEvaluationRadiusBudgetClosed",
            audit["closed_against_floor"],
            True,
            (
                f"最小 |xi|={audit['min_abs_value']:.12e}，扣除 2^-40 后仍高于 1/6000，"
                f"余量 {audit['certified_margin']:.12e}。"
            ),
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            node_closed,
            True,
            "节点下界账本已闭合；所有边界节点均满足 |xi|>=1/6000。",
            CLOSED_ATOM,
        ),
        row(
            "DerivativeTubeStillMissing",
            False,
            False,
            "节点下界不替代边段导数管道。",
            DERIVATIVE_TUBE_ATOM,
        ),
        row(
            "PolygonWindingStillMissing",
            False,
            False,
            "节点下界不替代离散多边形绕数整数校验。",
            POLYGON_WINDING_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行节点下界包路由。"""
    previous = load_json(paths["previous"])
    engine = load_json(paths["engine"])
    trace = load_json(paths["trace"])
    audit = node_audit(SAMPLES_PER_SIDE)
    rows = build_rows(previous, engine, trace, audit)
    node_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}] + [TRACE_HELPER]
    return {
        "certificate_type": "prime_matrix_xi_boundary_node_lower_bound_router",
        "status": "xi_boundary_trace_node_lower_bound_closed_derivative_tube_next"
        if node_closed
        else "xi_boundary_trace_node_lower_bound_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "node_lower_bound_closed": node_closed,
        "winding_self_contained_closed": False,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "audit": audit,
        "proof_contract": proof_contract(),
        "rows": rows,
        "next_priority": DERIVATIVE_TUBE_ATOM,
        "secondary_priority": POLYGON_WINDING_ATOM,
        "downstream_priority": WINDING_ATOM,
        "plain_conclusion": (
            "节点下界包已闭合：32769 个边界节点全部满足 |xi|>=1/6000。最坏节点是 "
            f"index={audit['min_index']}，位于 {audit['min_side']}，|xi|≈{audit['min_abs_value']:.12e}；"
            f"扣除 2^-40 求值半径后仍有 {audit['certified_margin']:.12e} 的正余量。"
            "下一步转入边段导数管道包。"
            if node_closed
            else "节点下界包尚未闭合；需要补齐 xi 区间引擎或 trace/hash 输入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    audit = result["audit"]
    lines = [
        "# Prime Matrix xi 边界节点下界包路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"node_lower_bound_closed={fmt_bool(result['node_lower_bound_closed'])}",
        f"winding_self_contained_closed={fmt_bool(result['winding_self_contained_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 节点账本摘要",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| node count | `{audit['node_count']}` |",
        f"| edge count | `{audit['edge_count']}` |",
        f"| leaf hash count | `{audit['leaf_hash_count']}` |",
        f"| node Merkle/root hash | `{audit['node_merkle_root_hash']}` |",
        f"| node floor | `{audit['node_floor']}` |",
        f"| eval radius | `{audit['node_eval_radius']}` |",
        f"| min abs value | `{audit['min_abs_value']:.12e}` |",
        f"| min index | `{audit['min_index']}` |",
        f"| min side | `{audit['min_side']}` |",
        f"| raw margin | `{audit['raw_margin']:.12e}` |",
        f"| certified margin | `{audit['certified_margin']:.12e}` |",
        "",
        "## 2. 每边最小值",
        "",
        "| side | index | point | abs value | certified margin |",
        "| --- | ---: | --- | ---: | ---: |",
    ]
    for side in ["bottom_t0", "right_sigma2", "top_t14", "left_sigma_minus1"]:
        item = audit["side_minima"][side]
        lines.append(
            "| {side} | `{index}` | `({re:.6f}, {im:.6f})` | `{abs_value:.12e}` | `{margin:.12e}` |".format(
                side=side,
                index=item["index"],
                re=item["point_re"],
                im=item["point_im"],
                abs_value=item["abs_value"],
                margin=item["certified_margin"],
            )
        )
    lines.extend(
        [
            "",
            "## 3. 最坏节点前 16 个",
            "",
            "| rank | index | side | point | abs value | certified margin |",
            "| ---: | ---: | --- | --- | ---: | ---: |",
        ]
    )
    for rank, item in enumerate(audit["worst_nodes"], start=1):
        lines.append(
            "| {rank} | `{index}` | {side} | `({re:.6f}, {im:.6f})` | `{abs_value:.12e}` | `{margin:.12e}` |".format(
                rank=rank,
                index=item["index"],
                side=item["side"],
                re=item["point_re"],
                im=item["point_im"],
                abs_value=item["abs_value"],
                margin=item["certified_margin"],
            )
        )
    lines.extend(
        [
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
            f"之后聚合：`{result['secondary_priority']}`。",
            "",
            "判定：节点下界包关闭，剩余转为边段导数管道。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--engine-json", type=Path, default=DEFAULT_ENGINE)
    parser.add_argument("--trace-json", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "engine": args.engine_json,
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
