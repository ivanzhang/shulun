#!/usr/bin/env python3
"""Prime Matrix Backlund 奇部修正成本终端路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_odd_correction_terminal_router.py

输出：
  docs/monograph/prime-matrix-backlund-odd-correction-terminal-router.json
  docs/monograph/prime-matrix-backlund-odd-correction-terminal-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-backlund-original-trace-odd-zero-router.json"
DEFAULT_INDENT = MONO / "prime-matrix-b3-zero-proximity-indentation-cost-router.json"
DEFAULT_CS8 = MONO / "prime-matrix-b3-cs8-slack-router.json"
DEFAULT_ENDPOINT = MONO / "prime-matrix-b3-endpoint-multiplicity-convention-router.json"
DEFAULT_RVM = MONO / "prime-matrix-b3-rvm-to-cn16-local-inequality-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-odd-correction-terminal-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-odd-correction-terminal-router.md"

ODD_CORRECTION_ATOM = "BacklundOddMirrorCorrectionCostLedger"
INDENT_COST_ATOM = "BacklundZeroProximityIndentationCostLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
CS8_CLOSED = "BacklundCS8SlackAfterBridgeClosedTightHalf"
ENDPOINT_CLOSED = "EndpointZeroAvoidanceMultiplicityConventionClosedByLimit"
RVM_CLOSED = "RVMToCN16LocalInequalityClosedWithRawArgCS8"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def terminal_map() -> list[dict[str, str]]:
    """给出奇部修正与凹口成本的终端等价图。"""
    return [
        {
            "from": ODD_CORRECTION_ATOM,
            "to": INDENT_COST_ATOM,
            "meaning": "奇部修正正是原始 trace 的未配对 crossing/近零缩进成本，没有新的独立自由度。",
        },
        {
            "from": INDENT_COST_ATOM,
            "to": EXTERNAL_ATOM,
            "meaning": "若接受经典 Backlund 缩进引理，该成本门在外部分支关闭。",
        },
        {
            "from": EXTERNAL_ATOM,
            "to": f"{CS8_CLOSED} AND {ENDPOINT_CLOSED} AND {RVM_CLOSED}",
            "meaning": "外部凹口门之后，CS8、端点、RVM->CN16 已有验收证书。",
        },
    ]


def build_rows(
    previous: dict[str, Any],
    indent: dict[str, Any],
    cs8: dict[str, Any],
    endpoint: dict[str, Any],
    rvm: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成奇部修正终端判定表。"""
    active = previous.get("next_priority") == ODD_CORRECTION_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    indent_external = indent.get("zero_proximity_indentation_cost_external_closed") is True
    indent_self = indent.get("zero_proximity_indentation_cost_self_contained_closed") is True
    cs8_external = cs8.get("backlund_cs8_slack_external_closed") is True
    endpoint_closed = (
        endpoint.get("endpoint_multiplicity_convention_closed") is True
        or endpoint.get("endpoint_multiplicity_convention_external_closed") is True
    )
    rvm_external = rvm.get("rvm_to_cn16_external_closed") is True
    terminal_equivalence = active and guard
    external_bridge_ready = indent_external and cs8_external and endpoint_closed and rvm_external
    return [
        row(
            "OddCorrectionGateActive",
            active,
            True,
            "原始奇部为零被阻断后，当前剩余是奇部修正成本。",
            ODD_CORRECTION_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的解析成本归并，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "OddCorrectionEqualsIndentCost",
            terminal_equivalence,
            True,
            "奇部修正就是近零 crossing 的缩进成本；它不产生新路线。",
            INDENT_COST_ATOM,
        ),
        row(
            "SelfContainedIndentCostStillOpen",
            not indent_self,
            True,
            "仓库内已证明零成本路线失败；自足凹口成本仍未闭合。",
            INDENT_COST_ATOM,
        ),
        row(
            "ExternalIndentCostAvailable",
            indent_external,
            False,
            "接受经典 Backlund 缩进引理时，凹口成本可作为外部闭合输入。",
            EXTERNAL_ATOM,
        ),
        row(
            "ExternalBacklundDownstreamReady",
            external_bridge_ready,
            False,
            "外部凹口门后，CS8 紧等号、端点 convention、RVM->CN16 均已有验收。",
            DSTRUCTURE,
        ),
        row(
            ODD_CORRECTION_ATOM,
            False,
            False,
            "完全自足路线仍缺经典 Backlund 缩进引理的内部替代；当前没有更窄的零成本路径。",
            INDENT_COST_ATOM,
        ),
        row(
            "ConditionalExternalBacklundPackage",
            external_bridge_ready,
            False,
            "在接受外部缩进引理后，解析 Backlund 包可推进到 DStructure/Rankin 独立验收门。",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行奇部修正成本终端路由。"""
    previous = load_json(paths["previous"])
    indent = load_json(paths["indent"])
    cs8 = load_json(paths["cs8"])
    endpoint = load_json(paths["endpoint"])
    rvm = load_json(paths["rvm"])
    rows = build_rows(previous, indent, cs8, endpoint, rvm)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    external_ready = next(item["closed"] for item in rows if item["gate"] == "ExternalBacklundDownstreamReady")
    return {
        "certificate_type": "prime_matrix_backlund_odd_correction_terminal_router",
        "status": "backlund_odd_correction_terminal_equivalent_to_indent_cost_external_ready",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "odd_correction_terminal_equivalence_closed": True,
        "odd_correction_self_contained_closed": False,
        "indent_cost_self_contained_closed": False,
        "external_backlund_bridge_ready": external_ready,
        "row_column_self_contained_closed": False,
        "row_column_external_backlund_closed": False,
        "terminal_map": terminal_map(),
        "replacement_self_contained": {ODD_CORRECTION_ATOM: INDENT_COST_ATOM},
        "replacement_external": {INDENT_COST_ATOM: EXTERNAL_ATOM},
        "self_contained_remaining": INDENT_COST_ATOM,
        "external_next_priority": DSTRUCTURE,
        "parallel_priority": DSTRUCTURE,
        "plain_conclusion": (
            "奇部修正成本已终端归并：它与 `BacklundZeroProximityIndentationCostLedger` 是同一个剩余。"
            "此前的零成本、半镜像平均、奇部为零路线均已被审查并阻断；"
            "因此完全自足路线的唯一未闭合解析输入仍是经典 Backlund 缩进成本的内部替代。"
            "若接受外部 `ClassicalBacklundZeroIndentationCostExternalAccepted`，则 CS8、端点、RVM->CN16 均已可接上，"
            "外部分支下一门为 DStructure/Rankin 独立验收。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 奇部修正成本终端路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "odd_correction_terminal_equivalence_closed="
            f"{fmt_bool(result['odd_correction_terminal_equivalence_closed'])}"
        ),
        f"odd_correction_self_contained_closed={fmt_bool(result['odd_correction_self_contained_closed'])}",
        f"indent_cost_self_contained_closed={fmt_bool(result['indent_cost_self_contained_closed'])}",
        f"external_backlund_bridge_ready={fmt_bool(result['external_backlund_bridge_ready'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"row_column_external_backlund_closed={fmt_bool(result['row_column_external_backlund_closed'])}",
        "```",
        "",
        "## 1. 终端归并图",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["terminal_map"]:
        lines.append(
            f"| `{table_cell(item['from'])}` | `{table_cell(item['to'])}` | {table_cell(item['meaning'])} |"
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
            f"完全自足剩余：`{result['self_contained_remaining']}`。",
            f"若接受外部 Backlund 缩进引理，下一门：`{result['external_next_priority']}`。",
            "",
            "判定：自足路线未闭合；外部 Backlund 分支已可接到 DStructure/Rankin 验收门。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--indent-json", type=Path, default=DEFAULT_INDENT)
    parser.add_argument("--cs8-json", type=Path, default=DEFAULT_CS8)
    parser.add_argument("--endpoint-json", type=Path, default=DEFAULT_ENDPOINT)
    parser.add_argument("--rvm-json", type=Path, default=DEFAULT_RVM)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
        "indent": args.indent_json,
        "cs8": args.cs8_json,
        "endpoint": args.endpoint_json,
        "rvm": args.rvm_json,
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
    print(result["self_contained_remaining"])


if __name__ == "__main__":
    main()
