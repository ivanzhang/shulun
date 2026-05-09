#!/usr/bin/env python3
"""Prime Matrix Backlund 最终分叉状态路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_final_branch_status_router.py

输出：
  docs/monograph/prime-matrix-backlund-final-branch-status-router.json
  docs/monograph/prime-matrix-backlund-final-branch-status-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_BACKLUND = MONO / "prime-matrix-backlund-odd-correction-terminal-router.json"
DEFAULT_DSTRUCTURE = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-final-branch-status-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-final-branch-status-router.md"

INDENT_COST_ATOM = "BacklundZeroProximityIndentationCostLedger"
EXTERNAL_ATOM = "ClassicalBacklundZeroIndentationCostExternalAccepted"
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


def branch_rows(backlund: dict[str, Any], dstructure: dict[str, Any]) -> list[dict[str, Any]]:
    """生成最终分叉状态表。"""
    backlund_terminal = backlund.get("odd_correction_terminal_equivalence_closed") is True
    external_backlund_ready = backlund.get("external_backlund_bridge_ready") is True
    dstructure_boundary = dstructure.get("promotion_package_boundary_closed") is True
    dstructure_accepted = dstructure.get("promotion_package_independently_accepted") is True
    return [
        row(
            "SelfContainedBacklundIndentStillOpen",
            True,
            True,
            "零成本、半镜像平均、奇部为零路线均已阻断；自足剩余终端归并回 Backlund 凹口成本。",
            INDENT_COST_ATOM,
        ),
        row(
            "BacklundTerminalEquivalenceClosed",
            backlund_terminal,
            True,
            "奇部修正成本与近零缩进成本是同一个剩余，不再产生新的内部逃逸口。",
            INDENT_COST_ATOM,
        ),
        row(
            "ExternalBacklundAnalyticBridgeReady",
            external_backlund_ready,
            False,
            "接受外部经典 Backlund 缩进引理后，CS8、端点、RVM->CN16 均已可接上。",
            DSTRUCTURE,
        ),
        row(
            "DStructureRankinBoundaryClosed",
            dstructure_boundary,
            True,
            "DStructure/Tail-log4/finite Rankin 晋级包边界已列清，Rankin 子账本 pass-or-return 已闭合。",
            "independent acceptance",
        ),
        row(
            "DStructureRankinIndependentlyAccepted",
            dstructure_accepted,
            False,
            "该门明确要求独立审稿/复现接受，作者侧证书不能自审关闭。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnSelfContainedClosed",
            False,
            False,
            "严格自足闭合仍缺 Backlund 凹口成本内部替代。",
            INDENT_COST_ATOM,
        ),
        row(
            "RowColumnExternalBacklundClosed",
            False,
            False,
            "即使接受外部 Backlund 缩进引理，仍缺 DStructure/Rankin 独立接受。",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行最终分叉状态路由。"""
    backlund = load_json(paths["backlund"])
    dstructure = load_json(paths["dstructure"])
    rows = branch_rows(backlund, dstructure)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_backlund_final_branch_status_router",
        "status": "row_theorem_self_contained_open_external_backlund_referee_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "self_contained_remaining": INDENT_COST_ATOM,
        "external_backlund_acceptance_atom": EXTERNAL_ATOM,
        "external_branch_remaining": DSTRUCTURE,
        "row_column_self_contained_closed": False,
        "row_column_external_backlund_closed": False,
        "no_author_side_overclaim": True,
        "plain_conclusion": (
            "最终分叉状态已固定：严格自足路线没有闭合，唯一剩余是 "
            f"`{INDENT_COST_ATOM}` 的内部替代；此前所有零成本镜像路线均已审查并阻断。"
            f"若接受 `{EXTERNAL_ATOM}`，解析 Backlund 包可接到 `{DSTRUCTURE}`，"
            "但该晋级门仍需独立接受，作者侧不能声明完整无条件闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 最终分叉状态路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        f"row_column_external_backlund_closed={fmt_bool(result['row_column_external_backlund_closed'])}",
        f"no_author_side_overclaim={fmt_bool(result['no_author_side_overclaim'])}",
        "```",
        "",
        "## 1. 当前分叉",
        "",
        "| branch | remaining |",
        "| --- | --- |",
        f"| strict self-contained | `{result['self_contained_remaining']}` |",
        f"| external Backlund accepted | `{result['external_branch_remaining']}` |",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 结论",
            "",
            "不能声明行/列命题已经严格自足闭合。可声明的是：",
            "",
            "- 自足路线的零成本替代已被审查排除，剩余精确归并为 Backlund 凹口成本。",
            "- 外部 Backlund 路线已可接到 DStructure/Rankin 独立验收门。",
            "- 完整无条件闭合仍要求外部缩进引理被接受，并且 DStructure/Rankin 晋级门独立验收通过。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backlund-json", type=Path, default=DEFAULT_BACKLUND)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "backlund": args.backlund_json,
        "dstructure": args.dstructure_json,
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
