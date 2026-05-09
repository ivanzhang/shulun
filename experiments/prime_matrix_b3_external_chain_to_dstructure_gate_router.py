#!/usr/bin/env python3
"""Prime Matrix B=3 外部解析链接入 DStructure/Rankin 守门项路由器。

用法示例：
  python3 experiments/prime_matrix_b3_external_chain_to_dstructure_gate_router.py

输出：
  docs/monograph/prime-matrix-b3-external-chain-to-dstructure-gate-router.json
  docs/monograph/prime-matrix-b3-external-chain-to-dstructure-gate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-meissel-mertens-interval-external-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_FINAL_GUARD = DOCS / "prime-matrix-final-guard-gate-completion-verdict-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-external-chain-to-dstructure-gate-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-external-chain-to-dstructure-gate-router.md"

DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SELF_PROMOTION = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
HIGH_SEGMENT = "HighSegmentModelGapAlpha043C3AnalyticLedger"


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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proves_unconditional: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proves_unconditional": proves_unconditional,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], dstructure: dict[str, Any], final_guard: dict[str, Any]) -> list[dict[str, Any]]:
    """生成外部解析链终端判定表。"""
    basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    chain_reaches_gate = previous.get("next_priority") == DSTRUCTURE_GATE and DSTRUCTURE_GATE in basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    b3_chain_ready = (
        previous.get("meissel_mertens_interval_external_closed") is True
        and previous.get("meissel_mertens_interval_self_contained_closed") is False
        and chain_reaches_gate
        and guard
    )
    boundary_closed = dstructure.get("promotion_package_boundary_closed") is True
    independent_accepted = dstructure.get("promotion_package_independently_accepted") is True
    final_guard_row_col = final_guard.get("row_column_unconditional_closed") is True
    return [
        row(
            "B3ExternalAnalyticChainReachesPromotionGate",
            b3_chain_ready,
            False,
            "B3 外部解析主链中的 theta、低高度、包络、有限桥和 Meissel-Mertens 输入均已条件闭合，并接到最终晋级门。",
            DSTRUCTURE_GATE,
        ),
        row(
            "DStructureRankinBoundaryClosed",
            boundary_closed,
            False,
            "DStructure/Tail-log4/finite Rankin 的验收边界已命名，Rankin pass-or-return 子账本已可审查。",
            "independent acceptance required",
        ),
        row(
            "DStructureRankinIndependentAcceptancePresent",
            independent_accepted,
            independent_accepted,
            "只有独立接受事件发生，外部 B3 条件链才能晋级为行/列无条件闭合。",
            "independent acceptance still absent" if not independent_accepted else "none",
        ),
        row(
            "FinalGuardStillBlocksUnconditionalClaim",
            not final_guard_row_col,
            False,
            "最终守门判定仍明确 row_column_unconditional_closed=false。",
            DSTRUCTURE_GATE,
        ),
        row(
            "SelfContainedAlternativeStillOpen",
            False,
            False,
            "若不用独立接受事件，仍需自足高段模型余量和自足 DStructure/Rankin 晋级证明包。",
            f"{HIGH_SEGMENT} AND {SELF_PROMOTION}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行外部解析链终端路由。"""
    previous = load_json(paths["previous"])
    dstructure = load_json(paths["dstructure"])
    final_guard = load_json(paths["final_guard"])
    rows = build_rows(previous, dstructure, final_guard)
    b3_external_chain_to_gate = next(
        item["closed"] for item in rows if item["gate"] == "B3ExternalAnalyticChainReachesPromotionGate"
    )
    independent_accepted = dstructure.get("promotion_package_independently_accepted") is True
    row_column_unconditional_closed = b3_external_chain_to_gate and independent_accepted
    return {
        "certificate_type": "b3_external_chain_to_dstructure_gate_router",
        "status": (
            "b3_external_chain_reaches_dstructure_gate_acceptance_open"
            if b3_external_chain_to_gate and not independent_accepted
            else "b3_external_chain_gate_status_needs_review"
        ),
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "b3_external_analytic_chain_closed_to_dstructure_gate": b3_external_chain_to_gate,
        "promotion_package_boundary_closed": dstructure.get("promotion_package_boundary_closed") is True,
        "promotion_package_independently_accepted": independent_accepted,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "latest_external_titchmarsh_cn16_basis": previous.get("latest_external_titchmarsh_cn16_basis", ""),
        "highest_valid_statement": (
            "B3 外部解析输入链 + DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance "
            "=> 行/列条件闭合；当前不能声明无条件闭合。"
        ),
        "next_priority": DSTRUCTURE_GATE,
        "self_contained_alternative_priorities": [HIGH_SEGMENT, SELF_PROMOTION],
        "plain_conclusion": (
            "B3 外部解析主链已经推进到最终 DStructure/Rankin 守门项：今天关闭的 theta、低高度、"
            "Dusart 全局包络、有限桥和 Meissel-Mertens 区间外部输入均已接入。"
            "但 DStructure/Rankin 独立接受仍未发生，因此行/列无条件命题仍不能闭合；"
            "作者侧最高合法状态仍是条件定理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix B=3 外部解析链接入 DStructure/Rankin 守门项",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        (
            "b3_external_analytic_chain_closed_to_dstructure_gate="
            f"{fmt_bool(result['b3_external_analytic_chain_closed_to_dstructure_gate'])}"
        ),
        f"promotion_package_boundary_closed={fmt_bool(result['promotion_package_boundary_closed'])}",
        f"promotion_package_independently_accepted={fmt_bool(result['promotion_package_independently_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最高合法状态",
        "",
        result["highest_valid_statement"],
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proves unconditional | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proves}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proves=fmt_bool(item["proves_unconditional"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"外部条件路线只剩 `{result['next_priority']}` 的独立接受事件。",
            "完全自足替代路线仍需：",
            "",
            "```text",
            " AND ".join(result["self_contained_alternative_priorities"]),
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--final-guard", type=Path, default=DEFAULT_FINAL_GUARD)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "dstructure": args.dstructure, "final_guard": args.final_guard}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
