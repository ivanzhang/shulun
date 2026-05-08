#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund 点态辐角桥路由器。

用法示例：
  python3 experiments/prime_matrix_b3_backlund_pointwise_bridge_router.py

输出：
  docs/monograph/prime-matrix-b3-backlund-pointwise-bridge-router.json
  docs/monograph/prime-matrix-b3-backlund-pointwise-bridge-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-backlund-constant-aggregation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-backlund-pointwise-bridge-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-backlund-pointwise-bridge-router.md"

OLD_ATOM = "BacklundPointwiseArgumentFromLittlewoodBridgeLedger"
BRANCH_CLOSED = "BacklundArgumentBranchNormalizationClosed"
SHORT_AVG_ATOM = "BacklundShortAveragePointwiseBridgeLedger"
SPIKE_ATOM = "BacklundArgumentSpikeExclusionLogDerivativeLedger"
SLACK_ATOM = "BacklundCS8SlackAfterBridgeLedger"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_BOUNDARY = 16.0
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
    """写出点态桥替换包。"""
    return f"({BRANCH_CLOSED} AND {SHORT_AVG_ATOM} AND {SPIKE_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧点态桥原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def bridge_factor_rows() -> list[dict[str, float]]:
    """生成点态桥因子压力表。"""
    rows: list[dict[str, float]] = []
    for bridge_factor in [1.0, 0.75, 0.5, 1.0 / math.pi, 1.0 / (2.0 * math.pi)]:
        cs = bridge_factor * C_BOUNDARY
        rows.append(
            {
                "bridge_factor": bridge_factor,
                "resulting_CS": cs,
                "slack": C_S_TARGET - cs,
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
    """生成 Backlund 点态桥判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    boundary_ready = "BacklundBoundaryConstantSumClosedC16" in basis
    rectangle_ready = "BacklundLittlewoodRectangleArgumentClosed" in basis
    indent_ready = "HorizontalZeroIndentationConventionClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    reduced = active and boundary_ready and rectangle_ready and indent_ready and guard
    return [
        row(
            "BacklundPointwiseBridgeGateActive",
            active,
            False,
            "上一层唯一内部最窄点是从 Littlewood 平均/积分控制到点态 arg zeta 的桥。",
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
            "BoundaryAndRectangleInputsAvailable",
            boundary_ready and rectangle_ready,
            True,
            "边界常数合计和 Littlewood 矩形形式层均已可用。",
            "无边界输入剩余。",
        ),
        row(
            "ArgumentBranchNormalizationClosed",
            reduced,
            True,
            "右边界 sigma>1 上由 Euler product 固定 arg 分支；穿零边界由缩进 convention 统一处理。",
            BRANCH_CLOSED,
        ),
        row(
            "ShortAveragePointwiseBridgeMissing",
            False,
            False,
            "仍需证明若点态 arg 在 T 处大，则在一个短高度平均或短 sigma 平均中保留固定比例质量。",
            SHORT_AVG_ATOM,
        ),
        row(
            "ArgumentSpikeExclusionMissing",
            False,
            False,
            "仍需排除极窄辐角尖峰；可用 log-derivative/Jensen/RVM 局部零点计数来支付。",
            SPIKE_ATOM,
        ),
        row(
            "BacklundPointwiseBridgeReduced",
            reduced,
            False,
            "旧点态桥原子已压成分支归一化、短平均桥和尖峰排斥三包。",
            replacement_pair(),
        ),
        row(
            "CS8SlackStillDownstream",
            False,
            False,
            "桥接损失因子确定后才能验收 C_S=8。",
            SLACK_ATOM,
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
    """执行 Backlund 点态桥路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "BacklundPointwiseBridgeReduced")
    return {
        "certificate_type": "b3_backlund_pointwise_bridge_router",
        "status": "backlund_pointwise_bridge_reduced_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_pointwise_bridge_reduced": reduced,
        "backlund_pointwise_bridge_self_contained_proved": False,
        "C_boundary": C_BOUNDARY,
        "C_S_target": C_S_TARGET,
        "required_bridge_factor": C_S_TARGET / C_BOUNDARY,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": SHORT_AVG_ATOM,
        "secondary_priority": SPIKE_ATOM,
        "tertiary_priority": SLACK_ATOM,
        "post_backlund_priority": ENDPOINT_ATOM,
        "post_endpoint_priority": RVM_CN_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "bridge_factor_rows": bridge_factor_rows(),
        "plain_conclusion": (
            "Backlund 点态桥尚未自足闭合。"
            "本步闭合的是 arg 分支归一化；真正剩余是短平均点态桥和尖峰排斥。"
            "这正是平均型 Littlewood 矩形预算与点态 S(T) 之间的缺口。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund 点态辐角桥路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_pointwise_bridge_reduced={fmt_bool(result['backlund_pointwise_bridge_reduced'])}",
        (
            "backlund_pointwise_bridge_self_contained_proved="
            f"{fmt_bool(result['backlund_pointwise_bridge_self_contained_proved'])}"
        ),
        f"C_boundary={fmt_float(result['C_boundary'])}",
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
        "## 2. 桥接因子压力",
        "",
        "| bridge factor | resulting C_S | slack to C_S=8 |",
        "| ---: | ---: | ---: |",
    ]
    for item in result["bridge_factor_rows"]:
        lines.append(
            "| `{factor}` | `{cs}` | `{slack}` |".format(
                factor=fmt_float(item["bridge_factor"]),
                cs=fmt_float(item["resulting_CS"]),
                slack=fmt_float(item["slack"]),
            )
        )
    lines.extend(
        [
            "",
            "这张表说明目标并不是任意强：只要点态桥损失不超过 `1/2`，`C_S=8` 就能通过。",
            "",
            "## 3. 判定表",
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`。"
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
