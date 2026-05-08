#!/usr/bin/env python3
"""Prime Matrix 全局 PDEC/sparse 终端门到终端家族拆分调和路由器。

用法示例：
  python3 experiments/prime_matrix_global_pdec_sparse_terminal_split_reconciliation_router.py

输出：
  docs/monograph/prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json
  docs/monograph/prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json"
DEFAULT_GLOBAL_BOUNDARY = DOCS / "prime-matrix-global-terminal-family-boundary-router.json"
DEFAULT_GLOBAL_SPLIT = DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.md"

OLD_ATOM = "GlobalPDECorSparseTerminalExclusion"
NEW_ATOM = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
EXACT_COMPAT = "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的终端原子。"""
    return text.replace(old, new)


def build_rows(
    previous: dict[str, Any],
    global_boundary: dict[str, Any],
    global_split: dict[str, Any],
    pdec: dict[str, Any],
    sparse: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 PDEC/sparse 终端门拆分判定表。"""
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in previous.get(
        "latest_self_contained_basis", ""
    )
    branch_guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    current_pdec_empty = (
        bool(pdec.get("pdec_family_explicit_input_boundary_closed"))
        and bool(pdec.get("current_materialized_pdec_frontier_closed"))
        and not bool(pdec.get("global_pdec_family_unconditional_closed"))
    )
    current_sparse_guarded = (
        bool(sparse.get("future_sparse_packet_schema_boundary_closed"))
        and bool(sparse.get("current_materialized_sparse_frontier_closed"))
        and not bool(sparse.get("global_sparse_family_unconditional_closed"))
    )
    materialized_frontier_exhausted = (
        bool(global_boundary.get("materialized_frontier_exhausted"))
        and bool(global_boundary.get("current_terminal_instances_exhausted"))
        and bool(global_boundary.get("terminal_generation_contract_closed"))
        and not bool(global_boundary.get("global_terminal_family_exclusion_closed"))
    )
    terminal_split_imported = (
        bool(global_split.get("closed_nonfinal_reductions"))
        and global_split.get("self_contained_next_hardpoint") == NEW_ATOM
        and not bool(global_split.get("global_terminal_family_exclusion_closed"))
    )
    reconciliation_closed = all(
        [
            active,
            branch_guard,
            current_pdec_empty,
            current_sparse_guarded,
            materialized_frontier_exhausted,
            terminal_split_imported,
        ]
    )
    return [
        row(
            "GlobalPDECorSparseTerminalGateActive",
            active,
            False,
            "上一层最新最窄点是 GlobalPDECorSparseTerminalExclusion。",
            "把它与既有全局终端家族边界对齐。",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            branch_guard,
            True,
            "仍只在假设早期零行反例链条中工作，不从真实样本缺席取证。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "CurrentPDECFrontierBoundaryImported",
            current_pdec_empty,
            True,
            "当前已物化合法非二点 primitive PDEC 候选为零；未来 PDEC 必须提交显式同 formal unit schema。",
            "不是全局 PDEC family 无条件排斥。",
        ),
        row(
            "CurrentSparseFrontierBoundaryImported",
            current_sparse_guarded,
            True,
            "当前 sparse/LocalSurvivor 前沿清零，已知入口 extractor 或合同准入均覆盖。",
            "未来 sparse 路线仍需完整 extractor schema。",
        ),
        row(
            "MaterializedTerminalFrontierExhausted",
            materialized_frontier_exhausted,
            True,
            "当前物化终端前沿没有可继续局部消元对象。",
            "剩余不是样本层对象，而是全局家族证书。",
        ),
        row(
            "GlobalTerminalFamilySplitImported",
            terminal_split_imported,
            True,
            "全局终端家族拆分已把 LocalSurvivor 与 NC-BLK 独立阻塞删除，连续终端二分送入 PDEC-CAP 或 CleanKLS/DLS。",
            NEW_ATOM,
        ),
        row(
            "GlobalPDECorSparseTerminalReconciledToTerminalSplit",
            reconciliation_closed,
            True,
            "GlobalPDECorSparseTerminalExclusion 不再作为宽泛终端黑箱保留。",
            NEW_ATOM,
        ),
        row(
            "PDEC_CAP",
            False,
            False,
            "尚未证明同一坏窗集合上的全局 U_CRT<L_PDEC 容量证书。",
            "PDEC_CAP。",
        ),
        row(
            "INTERNAL_CleanKLS_LargeSieve",
            False,
            False,
            "尚未证明 diffuse clean residual 的内部大筛吸收；外部 KLS/DI/BFI 只能作为条件分支。",
            "INTERNAL_CleanKLS_LargeSieve 或显式外部输入。",
        ),
        row(
            EXACT_COMPAT,
            False,
            False,
            "moving-block 到终端门替换仍需与模型余量/有限 DPRC 账本口径兼容。",
            EXACT_COMPAT,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "最终晋级仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行全局 PDEC/sparse 终端拆分调和。"""
    data = {name: load_json(path) for name, path in paths.items()}
    rows = build_rows(**data)
    split_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "GlobalPDECorSparseTerminalReconciledToTerminalSplit"
    )
    previous = data["previous"]
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "global_pdec_sparse_terminal_split_reconciliation_router",
        "status": "global_pdec_sparse_terminal_reconciled_to_pdec_cap_or_internal_kls_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "global_pdec_sparse_terminal_split_reconciled": split_closed,
        "current_materialized_frontier_exhausted": True,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "exact_model_gap_dprc_compatibility_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": NEW_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 GlobalPDECorSparseTerminalExclusion 与既有全局终端家族边界和拆分路由对齐。"
            "当前已物化 PDEC 与 sparse/LocalSurvivor 前沿已经清零，不能继续靠局部样本消元；"
            "全局终端门被压成完全自足路线的 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。"
            "这仍不是行列无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 全局 PDEC/sparse 终端拆分调和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"global_pdec_sparse_terminal_split_reconciled={fmt_bool(result['global_pdec_sparse_terminal_split_reconciled'])}",
        f"current_materialized_frontier_exhausted={fmt_bool(result['current_materialized_frontier_exhausted'])}",
        f"pdec_cap_or_internal_clean_kls_large_sieve_proved={fmt_bool(result['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}",
        f"exact_model_gap_dprc_compatibility_proved={fmt_bool(result['exact_model_gap_dprc_compatibility_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 拆分律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "这一步只导入已闭合的边界和拆分结果：当前物化前沿耗尽，但全局 PDEC-CAP 与内部 CleanKLS 大筛仍未证明。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 4. 下一步",
            "",
            "下一步最窄目标为 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`：在自足路线中二选一突破全局 PDEC-CAP 容量证书或内部 CleanKLS/DLS 大筛吸收；同时保留 moving-block/DPRC 口径兼容与 DStructure/Rankin 独立验收门。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--global-boundary", type=Path, default=DEFAULT_GLOBAL_BOUNDARY)
    parser.add_argument("--global-split", type=Path, default=DEFAULT_GLOBAL_SPLIT)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "global_boundary": args.global_boundary,
        "global_split": args.global_split,
        "pdec": args.pdec,
        "sparse": args.sparse,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")


if __name__ == "__main__":
    main()
