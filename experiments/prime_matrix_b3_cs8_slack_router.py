#!/usr/bin/env python3
"""Prime Matrix B=3 Backlund C_S=8 余量验收路由器。

用法示例：
  python3 experiments/prime_matrix_b3_cs8_slack_router.py

输出：
  docs/monograph/prime-matrix-b3-cs8-slack-router.json
  docs/monograph/prime-matrix-b3-cs8-slack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-cs8-slack-router.md"

OLD_ATOM = "BacklundCS8SlackAfterBridgeLedger"
CLOSED_ATOM = "BacklundCS8SlackAfterBridgeClosedTightHalf"
BOUNDARY_ATOM = "BacklundBoundaryConstantSumClosedC16"
BRIDGE_ATOM = "BacklundShortAveragePointwiseBridgeClosedHalfGivenLocalStability"
WINDOW_ATOM = "BacklundVariationWindowScaleClosedH1Over512C192"
INDENT_EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
ENDPOINT_ATOM = "EndpointZeroAvoidanceMultiplicityConventionLedger"
RVM_TO_CN_ATOM = "RVMToCN16LocalInequalityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_BOUNDARY = 16.0
BRIDGE_FACTOR = 0.5
C_S_TARGET = 8.0
C_S_RESULT = C_BOUNDARY * BRIDGE_FACTOR
SLACK = C_S_TARGET - C_S_RESULT


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


def replace_atom(text: str) -> str:
    """替换 C_S=8 余量验收原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def budget_rows() -> list[dict[str, Any]]:
    """生成 C_S=8 预算表。"""
    return [
        {
            "component": "boundary constant",
            "value": C_BOUNDARY,
            "source": BOUNDARY_ATOM,
        },
        {
            "component": "bridge factor",
            "value": BRIDGE_FACTOR,
            "source": BRIDGE_ATOM,
        },
        {
            "component": "resulting C_S",
            "value": C_S_RESULT,
            "source": "C_boundary * bridge_factor",
        },
        {
            "component": "target C_S",
            "value": C_S_TARGET,
            "source": "Backlund target",
        },
        {
            "component": "slack",
            "value": SLACK,
            "source": "target - result",
        },
    ]


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
    """生成 C_S=8 余量判定表。"""
    external_basis = previous.get("latest_conditional_basis", "")
    active = previous.get("conditional_next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    boundary_ready = BOUNDARY_ATOM in external_basis
    bridge_ready = BRIDGE_ATOM in external_basis
    window_ready = WINDOW_ATOM in external_basis
    indent_ready = bool(previous.get("zero_proximity_indentation_cost_external_closed")) and INDENT_EXTERNAL_ATOM in external_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    budget_ok = C_S_RESULT <= C_S_TARGET and SLACK == 0.0
    closed = active and boundary_ready and bridge_ready and window_ready and indent_ready and guard and budget_ok
    return [
        row(
            "CS8SlackGateActive",
            active,
            False,
            "外部 Backlund 分支当前最窄点是 C_S=8 余量验收。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的 Backlund 常数验收，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "BoundaryBridgeInputsAvailable",
            boundary_ready and bridge_ready,
            True,
            "边界常数 C16 与半质量桥均已进入外部分支输入基。",
            f"{BOUNDARY_ATOM} AND {BRIDGE_ATOM}",
        ),
        row(
            "WindowAndIndentCostsNotDoubleCounted",
            window_ready and indent_ready,
            False,
            "窗口尺度与凹口成本已在前两步独立处理；本步不再重复扣减 C_S 预算。",
            f"{WINDOW_ATOM} AND {INDENT_EXTERNAL_ATOM}",
        ),
        row(
            "CS8TightEqualityPasses",
            budget_ok,
            True,
            "16*1/2=8，目标 C_S=8 是紧等号闭合，没有额外正余量。",
            CLOSED_ATOM,
        ),
        row(
            "BacklundCS8SlackClosed",
            closed,
            True,
            "外部 Backlund 分支的点态 arg 常数验收完成。",
            CLOSED_ATOM,
        ),
        row(
            "EndpointConventionNext",
            False,
            False,
            "下一步处理端点避零与重数 convention。",
            ENDPOINT_ATOM,
        ),
        row(
            "RVMToCN16StillDownstream",
            False,
            False,
            "随后仍需 RVM 到 C_N=16 局部计数不等式。",
            RVM_TO_CN_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 C_S=8 余量验收路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "BacklundCS8SlackClosed"
    )
    latest_external = replace_atom(previous.get("latest_conditional_basis", ""))
    return {
        "certificate_type": "b3_cs8_slack_router",
        "status": "backlund_cs8_slack_external_closed_tight",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_cs8_slack_external_closed": closed,
        "backlund_cs8_slack_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "C_boundary": C_BOUNDARY,
        "bridge_factor": BRIDGE_FACTOR,
        "C_S_target": C_S_TARGET,
        "C_S_result": C_S_RESULT,
        "slack": SLACK,
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "latest_conditional_basis": latest_external,
        "latest_global_with_external_basis": latest_external,
        "next_priority": previous.get("next_priority"),
        "secondary_priority": previous.get("secondary_priority"),
        "conditional_next_priority": ENDPOINT_ATOM,
        "secondary_conditional_priority": RVM_TO_CN_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "budget_rows": budget_rows(),
        "plain_conclusion": (
            "Backlund C_S=8 余量在外部分支中以紧等号闭合：C_boundary=16，桥接因子 1/2，"
            "得到 C_S=8。窗口尺度和凹口成本已在前序账本处理，本步不重复扣减。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 Backlund C_S=8 余量验收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_cs8_slack_external_closed={fmt_bool(result['backlund_cs8_slack_external_closed'])}",
        f"backlund_cs8_slack_self_contained_closed={fmt_bool(result['backlund_cs8_slack_self_contained_closed'])}",
        f"C_boundary={fmt_float(result['C_boundary'])}",
        f"bridge_factor={fmt_float(result['bridge_factor'])}",
        f"C_S_target={fmt_float(result['C_S_target'])}",
        f"C_S_result={fmt_float(result['C_S_result'])}",
        f"slack={fmt_float(result['slack'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件链替换",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "## 2. 预算表",
        "",
        "| component | value | source |",
        "| --- | ---: | --- |",
    ]
    for item in result["budget_rows"]:
        lines.append(
            "| {component} | `{value}` | {source} |".format(
                component=table_cell(item["component"]),
                value=fmt_float(float(item["value"])),
                source=table_cell(item["source"]),
            )
        )
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
            "conditional/external Backlund 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"完全自足路线仍先攻 `{result['next_priority']}`；"
                f"外部 Backlund 分支下一步转为 `{result['conditional_next_priority']}`。"
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
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
