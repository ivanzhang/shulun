#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 总常数聚合路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_constant_aggregation_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-constant-aggregation-router.json
  docs/monograph/prime-matrix-b3-backlund-constant-aggregation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-horizontal-aggregation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-constant-aggregation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-constant-aggregation-router.md"

OLD_ATOM = "BacklundArgumentConstantAggregationLedger"
BOUNDARY_CLOSED = "BacklundBoundaryConstantSumClosedC16"
BRIDGE_ATOM = "BacklundPointwiseArgumentFromLittlewoodBridgeLedger"
SLACK_ATOM = "BacklundCS8SlackAfterBridgeLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_RIGHT = 2.0
C_LEFT = 4.0
C_HORIZONTAL = 8.0
C_ELEMENTARY = 2.0
C_BOUNDARY_SUM = C_RIGHT + C_LEFT + C_HORIZONTAL + C_ELEMENTARY
C_S_TARGET = 8.0


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replacement_pair() -> str:
    """写出 Backlund 总常数替换包。"""
    return f"({BOUNDARY_CLOSED} AND {BRIDGE_ATOM} AND {SLACK_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧总常数原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def constants_table() -> list[dict[str, Any]]:
    """生成边界常数表。"""
    return [
        {
            "component": "right_edge",
            "atom": "ZetaRightEdgeEulerProductArgumentClosedCright2",
            "constant": C_RIGHT,
            "meaning": "右边界 sigma>1 的点态 log/arg 预算。",
        },
        {
            "component": "left_edge",
            "atom": "FunctionalEquationLeftEdgeArgumentClosedCleft4",
            "constant": C_LEFT,
            "meaning": "函数方程左边界保守预算。",
        },
        {
            "component": "horizontal_edges",
            "atom": "HorizontalVariationConstantClosedC8",
            "constant": C_HORIZONTAL,
            "meaning": "上下水平边合计预算。",
        },
        {
            "component": "elementary_indent",
            "atom": "HorizontalZeroIndentationConventionClosed",
            "constant": C_ELEMENTARY,
            "meaning": "凹口、去极点和端点保留的安全常数。",
        },
    ]


def bridge_budget_rows() -> list[dict[str, float]]:
    """生成桥接损失候选表。"""
    rows: list[dict[str, float]] = []
    for factor in [1.0, 1.0 / math.pi, 1.0 / (2.0 * math.pi), 0.25, 0.5]:
        rows.append(
            {
                "bridge_factor": factor,
                "resulting_CS": factor * C_BOUNDARY_SUM,
                "slack_to_CS8": C_S_TARGET - factor * C_BOUNDARY_SUM,
            }
        )
    return rows


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Backlund 总常数聚合判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    required_atoms = [
        "BacklundLittlewoodRectangleArgumentClosed",
        "ZetaRightEdgeEulerProductArgumentClosedCright2",
        "HorizontalVariationConstantClosedC8",
        "FunctionalEquationLeftEdgeArgumentClosedCleft4",
        "CriticalStripConvexityClosedC2",
    ]
    boundary_ready = all(atom in basis for atom in required_atoms)
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and boundary_ready and guard
    bridge_needed_factor = C_S_TARGET / C_BOUNDARY_SUM
    return [
        row(
            "BacklundConstantAggregationGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Backlund/arg zeta 总常数聚合。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "BoundaryInputsAvailable",
            boundary_ready,
            True,
            "Littlewood 矩形、右边界、水平边、左边界和 C=2 凸性输入均已可用。",
            "无边界输入剩余。",
        ),
        row(
            "BoundaryConstantSumClosed",
            reduced,
            True,
            "边界常数可保守合计为 C_boundary=16。",
            BOUNDARY_CLOSED,
        ),
        row(
            "PointwiseArgumentBridgeMissing",
            False,
            False,
            "仍需严格证明 Backlund 桥：如何从 Littlewood 矩形的积分/平均控制推出点态 |S(T)| 上界，并记录桥接损失。",
            BRIDGE_ATOM,
        ),
        row(
            "CS8SlackVerificationMissing",
            False,
            False,
            f"C_boundary=16 要推出 C_S=8，桥接损失因子必须 <= {bridge_needed_factor:.6f}；该因子尚未证明。",
            SLACK_ATOM,
        ),
        row(
            "BacklundConstantAggregationReduced",
            reduced,
            False,
            "旧总常数原子已压成边界常数合计、点态桥和 C_S=8 余量验收三包。",
            replacement_pair(),
        ),
        row(
            "EndpointAndCN16StillDownstream",
            False,
            False,
            "Backlund 完成后仍需端点 convention 与 RVM->CN16 合并。",
            f"{ENDPOINT_ATOM} AND {RVM_CN_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Backlund 总常数聚合路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "BacklundConstantAggregationReduced")
    return {
        "certificate_type": "b3_backlund_constant_aggregation_router",
        "status": "backlund_constant_aggregation_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_constant_aggregation_reduced": reduced,
        "backlund_argument_bound_self_contained_proved": False,
        "C_boundary_sum": C_BOUNDARY_SUM,
        "C_S_target": C_S_TARGET,
        "required_bridge_factor": C_S_TARGET / C_BOUNDARY_SUM,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": BRIDGE_ATOM,
        "secondary_priority": SLACK_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "constants_table": constants_table(),
        "bridge_budget_rows": bridge_budget_rows(),
        "plain_conclusion": (
            "Backlund 总常数尚未自足闭合。边界常数已经可合计为 C_boundary=16，"
            "但还缺一个把 Littlewood 平均/积分控制变成点态 arg zeta 上界的 Backlund 桥；"
            "只有桥接损失因子不超过 1/2 时，才能验收 C_S=8。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 总常数聚合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_constant_aggregation_reduced={fmt_bool(result['backlund_constant_aggregation_reduced'])}",
        (
            "backlund_argument_bound_self_contained_proved="
            f"{fmt_bool(result['backlund_argument_bound_self_contained_proved'])}"
        ),
        f"C_boundary_sum={fmt_float(result['C_boundary_sum'])}",
        f"C_S_target={fmt_float(result['C_S_target'])}",
        f"required_bridge_factor={fmt_float(result['required_bridge_factor'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 边界常数合计",
        "",
        "| component | atom | constant | meaning |",
        "| --- | --- | ---: | --- |",
    ]
    for item in result["constants_table"]:
        lines.append(
            "| {component} | `{atom}` | `{constant}` | {meaning} |".format(
                component=table_cell(item["component"]),
                atom=table_cell(item["atom"]),
                constant=fmt_float(item["constant"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 桥接损失压力",
            "",
            "| bridge factor | resulting C_S | slack to C_S=8 |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in result["bridge_budget_rows"]:
        lines.append(
            "| `{factor}` | `{cs}` | `{slack}` |".format(
                factor=fmt_float(item["bridge_factor"]),
                cs=fmt_float(item["resulting_CS"]),
                slack=fmt_float(item["slack_to_CS8"]),
            )
        )
    lines.extend(
        [
            "",
            "结论：`1/(2*pi)`、`1/pi` 或 `1/4` 级桥接因子都有充足余量；纯三角不等式因子 `1` 不够。",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 5. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
