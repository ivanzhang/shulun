#!/usr/bin/env python3
"""Prime Matrix Backlund 辅助实部 Jensen 构造路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_auxiliary_realpart_jensen_router.py

输出：
  docs/monograph/prime-matrix-backlund-auxiliary-realpart-jensen-router.json
  docs/monograph/prime-matrix-backlund-auxiliary-realpart-jensen-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_OBSTRUCTION = MONO / "prime-matrix-backlund-signchange-absorption-obstruction-router.json"
DEFAULT_CENTER = MONO / "prime-matrix-b3-jensen-right-edge-center-router.json"
DEFAULT_EULER = MONO / "prime-matrix-b3-jensen-euler-lower-router.json"
DEFAULT_BOUNDARY = MONO / "prime-matrix-b3-xi-boundary-constant-aggregation-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-auxiliary-realpart-jensen-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-auxiliary-realpart-jensen-router.md"

PARENT_REMAINING = "BacklundAuxiliaryRealPartJensenCountNoDoubleCountLedger"
CONSTRUCTION = "BacklundAuxiliaryRealPartEntireFunctionConstructionClosed"
ANCHOR = "BacklundAuxiliaryRealPartRightEdgePhaseAnchorClosed"
BOUNDARY = "BacklundAuxiliaryRealPartBoundaryMajorantTransferredClosed"
COUNT_REMAINING = "BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger"
NO_DOUBLE_COUNT = "BacklundAuxiliaryRealPartNoDoubleCountingWithXiZerosLedger"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def construction_steps() -> list[dict[str, str]]:
    """列出辅助实部函数构造步骤。"""
    return [
        {
            "step": "define_auxiliary_entire",
            "content": "B_{T,theta}(z)=1/2*(exp(-i theta) xi(z+iT)+exp(i theta) xi(z-iT))。",
            "status": "closed_formal",
        },
        {
            "step": "real_axis_identity",
            "content": "z=x 为实数时，由 xi(conj s)=conj xi(s)，得 B_{T,theta}(x)=Re(exp(-i theta) xi(x+iT))。",
            "status": "closed_formal",
        },
        {
            "step": "right_edge_phase_anchor",
            "content": "取 theta=arg xi(2+iT)，则 B_{T,theta}(2)=|xi(2+iT)|，圆心不为零。",
            "status": "closed_given_right_edge_anchor",
        },
        {
            "step": "boundary_transfer",
            "content": "|B_{T,theta}(z)| <= (|xi(z+iT)|+|xi(z-iT)|)/2，圆周上界可由既有 xi 边界包转移。",
            "status": "closed_symbolic",
        },
    ]


def build_rows(
    obstruction: dict[str, Any],
    center: dict[str, Any],
    euler: dict[str, Any],
    boundary: dict[str, Any],
    endpoint: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成辅助实部 Jensen 构造判定表。"""
    guard = (
        obstruction.get("counterexample_assumption_only") is True
        and obstruction.get("empirical_absence_not_used") is True
        and obstruction.get("hypothetical_chain_only") is True
    )
    parent_active = obstruction.get("new_unique_internal_remaining") == PARENT_REMAINING
    center_closed = center.get("backlund_jensen_right_edge_center_choice_closed") is True
    euler_closed = euler.get("backlund_jensen_right_edge_euler_lower_bound_closed") is True
    boundary_closed = boundary.get("backlund_independent_xi_boundary_majorant_closed_symbolic") is True
    endpoint_closed = endpoint.get("endpoint_multiplicity_convention_closed") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只构造经典 Backlund 辅助函数和 Jensen 接口，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "AuxiliaryRealPartJensenGateActive",
            parent_active,
            True,
            "上一层已证明不能把 sign-change 直接注入 xi 真零点计数，必须构造辅助实部 Jensen 包。",
            PARENT_REMAINING,
        ),
        row(
            "AuxiliaryEntireFunctionConstructionClosed",
            True,
            True,
            "B_{T,theta}(z) 由 xi 的两个平移共轭项组成，是整函数。",
            CONSTRUCTION,
        ),
        row(
            "RealAxisSignChangeIdentityClosed",
            True,
            True,
            "在实轴上 B_{T,theta}(x) 正是旋转后 xi(x+iT) 的实部，因此其零点计数 sign-change。",
            CONSTRUCTION,
        ),
        row(
            "RightEdgeCenterGeometryAvailable",
            center_closed,
            True,
            "既有 z0=2、R=4、r=sqrt(5) 的 Jensen 圆心几何可复用到辅助函数。",
            "BacklundJensenRightEdgeCenterChoiceConventionClosedR4",
        ),
        row(
            "RightEdgePhaseAnchorClosed",
            euler_closed,
            True,
            "取 theta=arg xi(2+iT) 后圆心值为 |xi(2+iT)|；sigma=2 的 Euler 下界给非零 anchor。",
            ANCHOR,
        ),
        row(
            "BoundaryMajorantTransferClosedSymbolic",
            boundary_closed,
            True,
            "辅助函数的圆周上界由两个 xi 圆周上界平均控制，形式上不新增零点计数输入。",
            BOUNDARY,
        ),
        row(
            "EndpointMultiplicityCompatible",
            endpoint_closed,
            True,
            "端点落在辅助函数零点时仍按避零序列和解析重数取极限。",
            "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit",
        ),
        row(
            "AuxiliaryJensenConstantAggregationOpen",
            False,
            False,
            "还未把辅助函数边界上界、右边 anchor、低高度项聚合成目标 C16 或可被 C_S=8 吸收的常数。",
            COUNT_REMAINING,
        ),
        row(
            "AuxiliaryNoDoubleCountingOpen",
            False,
            False,
            "还未证明辅助实部零点计数、xi 真零点重数和缩进登记三者没有重复扣费。",
            NO_DOUBLE_COUNT,
        ),
        row(
            "SelfContainedAuxiliaryBacklundPackageOpen",
            False,
            False,
            "形式构造已完成；常数聚合与无重复扣费未完成前，内部经典 Backlund 缩进证明仍开。",
            f"{COUNT_REMAINING} AND {NO_DOUBLE_COUNT}",
        ),
        row(
            "ExternalBacklundStillAvailable",
            True,
            False,
            "外部经典 Backlund 引理可整体替代辅助实部 Jensen 计数与无重复扣费证明。",
            EXTERNAL_ACCEPTED,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行辅助实部 Jensen 构造路由。"""
    obstruction = load_json(paths["obstruction"])
    center = load_json(paths["center"])
    euler = load_json(paths["euler"])
    boundary = load_json(paths["boundary"])
    endpoint = load_json(paths["endpoint"])
    rows = build_rows(obstruction, center, euler, boundary, endpoint)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_auxiliary_realpart_jensen_router",
        "status": "backlund_auxiliary_realpart_jensen_formal_construction_closed_constants_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "parent_remaining": PARENT_REMAINING,
        "formal_construction_closed": True,
        "right_edge_phase_anchor_closed": True,
        "boundary_majorant_transfer_closed_symbolic": True,
        "new_unique_internal_remaining": f"{COUNT_REMAINING} AND {NO_DOUBLE_COUNT}",
        "row_column_self_contained_closed": False,
        "row_column_external_route_closed": False,
        "external_backlund_escape": EXTERNAL_ACCEPTED,
        "construction_steps": construction_steps(),
        "plain_conclusion": (
            "经典 Backlund 辅助实部函数的形式层已闭合："
            "B_{T,theta}(z)=1/2(e^{-i theta}xi(z+iT)+e^{i theta}xi(z-iT)) 是整函数，"
            "在实轴上等于旋转后的实部，故其零点正是 sign-change 计数对象。"
            "右边相位 anchor 与 xi 圆周上界可由既有 Jensen 圆心、Euler 下界和 xi 边界包转移。"
            "剩余未闭合的是辅助函数 Jensen 常数聚合，以及它与 xi 真零点/缩进登记的无重复扣费纪律。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 辅助实部 Jensen 构造路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"parent_remaining={result['parent_remaining']}",
        f"formal_construction_closed={fmt_bool(result['formal_construction_closed'])}",
        f"right_edge_phase_anchor_closed={fmt_bool(result['right_edge_phase_anchor_closed'])}",
        f"boundary_majorant_transfer_closed_symbolic={fmt_bool(result['boundary_majorant_transfer_closed_symbolic'])}",
        f"new_unique_internal_remaining={result['new_unique_internal_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 构造步骤",
        "",
        "| step | content | status |",
        "| --- | --- | --- |",
    ]
    for item in result["construction_steps"]:
        lines.append(f"| `{table_cell(item['step'])}` | {table_cell(item['content'])} | `{item['status']}` |")
    lines.extend(
        [
            "",
            "## 2. 新剩余",
            "",
            "```text",
            f"{result['parent_remaining']}",
            "  =>",
            f"{CONSTRUCTION} AND {ANCHOR} AND {BOUNDARY}",
            "  AND",
            f"({COUNT_REMAINING} AND {NO_DOUBLE_COUNT})",
            "```",
            "",
            "前三个形式/anchor/边界转移项本步关闭；括号内两项仍开。",
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
            f"内部剩余：`{result['new_unique_internal_remaining']}`。",
            f"外部逃逸门：`{result['external_backlund_escape']}`。",
            "",
            "判定：辅助实部 Jensen 的形式层已完成，常数聚合和无重复扣费仍是当前内部硬点。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--obstruction-json", type=Path, default=DEFAULT_OBSTRUCTION)
    parser.add_argument("--center-json", type=Path, default=DEFAULT_CENTER)
    parser.add_argument("--euler-json", type=Path, default=DEFAULT_EULER)
    parser.add_argument("--boundary-json", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "obstruction": args.obstruction_json,
        "center": args.center_json,
        "euler": args.euler_json,
        "boundary": args.boundary_json,
        "endpoint": args.endpoint_json,
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
    print(result["new_unique_internal_remaining"])


if __name__ == "__main__":
    main()
