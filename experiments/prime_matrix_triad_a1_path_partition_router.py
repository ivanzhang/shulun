#!/usr/bin/env python3
"""硬攻 FiniteSignatureNoCancellationOrCleanReturn 的路径分割硬点。

用法示例：
  python3 experiments/prime_matrix_triad_a1_path_partition_router.py
  python3 experiments/prime_matrix_triad_a1_path_partition_router.py --full-signature-power 0.8

输出：
  docs/monograph/prime-matrix-triad-a1-path-partition-router.json
  docs/monograph/prime-matrix-triad-a1-path-partition-router.md
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
DEFAULT_SELECTOR = DOCS / "prime-matrix-triad-a1-selector-retention-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-path-partition-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-path-partition-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_float(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6g}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def path_row(
    k: int,
    support_power: float,
    buchstab_loss: float,
    full_signature_power: float,
    required_loss: float,
) -> dict[str, Any]:
    """生成完整路径签名数量阈值行。"""
    y = 10**k
    log_y = math.log(y)
    interval_size = log_y**support_power
    raw_support = interval_size / (log_y**buchstab_loss)
    full_signature_count = log_y**full_signature_power
    selected_path_support = raw_support / full_signature_count
    required_support = interval_size / (log_y**required_loss)
    path_budget_suffices = selected_path_support >= required_support
    max_allowed_full_signature_power = required_loss - buchstab_loss
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "support_power_B": support_power,
        "buchstab_loss_power_E": buchstab_loss,
        "full_signature_power_J": full_signature_power,
        "required_loss_power_C": required_loss,
        "max_allowed_full_signature_power_C_minus_E": max_allowed_full_signature_power,
        "model_interval_size": interval_size,
        "raw_support": raw_support,
        "full_signature_count": full_signature_count,
        "selected_path_support": selected_path_support,
        "required_support": required_support,
        "path_budget_suffices": path_budget_suffices,
    }


def build_gate_rows() -> list[dict[str, Any]]:
    """列出路径分割/无抵消的门控。"""
    return [
        {
            "gate": "CompleteDecisionTraceSignature",
            "available": "finite signatures exist as labels in the previous router",
            "needed": "signature records the full RIW/Buchstab branch trace: ordered primes, parity, dyadic bin and truncation",
            "gap": "current label may be coarser than the exact coefficient path",
            "route": "refine the signature until every coefficient contribution has one complete trace",
            "closed": False,
        },
        {
            "gate": "DisjointPathPartition",
            "available": "Buchstab recursion is a deterministic decision tree after a full trace is fixed",
            "needed": "each squarefree product lies in at most one selected complete trace",
            "gap": "none once CompleteDecisionTraceSignature is fixed",
            "route": "use ordered least-new-prime / branch-state uniqueness",
            "closed": True,
        },
        {
            "gate": "SamePathNonzeroCoefficient",
            "available": "a complete trace has a fixed sign/parity and nonzero local factors",
            "needed": "no cancellation inside one complete path support",
            "gap": "none once coefficients are written as path weights with nonzero local factors",
            "route": "coefficient on a path is a nonzero product of local branch factors",
            "closed": True,
        },
        {
            "gate": "FullSignatureCountBudget",
            "available": "K6/tail-label bookkeeping gives a polylog count",
            "needed": "the complete trace count remains <= log^J with E+J<=C",
            "gap": "coarse labels may hide extra trace states; the full count must be recorded",
            "route": "charge extra trace states to K6; if the budget is exceeded, return to tail-label/PDEC",
            "closed": False,
        },
        {
            "gate": "NonDecisionTreeCleanReturn",
            "available": "edge/PDEC/SAE exits exist",
            "needed": "failure of complete disjoint path formula exits clean A1",
            "gap": "the contrapositive clean contract is not yet stated",
            "route": "non-disjoint, cancelling or over-budget traces are named clean failures",
            "closed": False,
        },
        {
            "gate": "PathPartitionImpliesNoCancellation",
            "available": "disjoint partition + nonzero same-path coefficient",
            "needed": "FiniteSignatureNoCancellationOrCleanReturn",
            "gap": "conditional implication is direct; exact formula/budget/return remain",
            "route": "combine complete traces with full signature budget",
            "closed": True,
        },
    ]


def run(
    selector_path: Path,
    min_k: int,
    max_k: int,
    support_power: float,
    buchstab_loss: float,
    full_signature_power: float,
    required_loss: float,
) -> dict[str, Any]:
    """运行路径分割路由。"""
    selector = load_json(selector_path)
    rows = [
        path_row(k, support_power, buchstab_loss, full_signature_power, required_loss)
        for k in range(min_k, max_k + 1)
    ]
    all_path_rows_suffice = all(row["path_budget_suffices"] for row in rows)
    return {
        "certificate_type": "triad_a1_path_partition_router",
        "status": "finite_signature_no_cancellation_reduced_to_exact_decision_tree_or_clean_return",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "selector_retention_json": file_sha256(selector_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "support_power_B": support_power,
            "buchstab_loss_power_E": buchstab_loss,
            "full_signature_power_J": full_signature_power,
            "required_loss_power_C": required_loss,
            "scale": "y=10^k",
        },
        "selector_input_status": selector["status"],
        "selector_input_next_target": selector["next_internal_target"],
        "gate_rows": build_gate_rows(),
        "rows": rows,
        "all_path_rows_suffice": all_path_rows_suffice,
        "complete_decision_trace_signature_closed": False,
        "disjoint_path_partition_closed_conditionally": True,
        "same_path_nonzero_coefficient_closed_conditionally": True,
        "full_signature_count_budget_closed": False,
        "non_decision_tree_clean_return_closed": False,
        "finite_signature_no_cancellation_closed": False,
        "conditional_decision_tree_implies_no_cancellation": True,
        "reduction_law": (
            "No-cancellation is not a new analytic estimate after the full path signature is fixed. "
            "A Buchstab/RIW expansion can be made into a decision tree: the complete trace records "
            "the ordered branch choices, parity and truncation state. Complete traces are disjoint, "
            "and a same-trace coefficient is a nonzero product of local branch factors. Therefore "
            "the remaining obligation is to write the exact canonical coefficient formula as such "
            "a complete decision-tree partition within the polylog signature budget, or to return "
            "over-budget/non-disjoint/cancelling blocks to existing clean exits."
        ),
        "next_internal_target": "ExactRIWDecisionTreeFormulaOrCleanReturn",
        "terminal_gap_after_router": (
            "ExactRIWDecisionTreeFormulaOrCleanReturnOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "FiniteSignatureNoCancellation 已被压缩为 exact RIW/Buchstab 决策树公式问题："
            "若签名细化到完整分支轨迹，则路径天然互斥，同一路径系数非零，无抵消随结构闭合。"
            "真正剩余是把 canonical 筛权逐项写成该完整决策树，并证明完整路径数仍在 K6 "
            "polylog 预算内；失败块必须回到 PDEC/SAE。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Path Partition / No-Cancellation 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 决策树无抵消律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "refine signature to the complete RIW/Buchstab decision trace;",
        "complete traces are disjoint by deterministic branch history;",
        "same-trace coefficient is a nonzero product of local branch factors;",
        "therefore no-cancellation is structural, not spectral;",
        "remaining issue: exact formula + path-count budget, or clean return.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `selector_input_status={result['selector_input_status']}`。",
        f"- `selector_input_next_target={result['selector_input_next_target']}`。",
        f"- `all_path_rows_suffice={result['all_path_rows_suffice']}`。",
        f"- `conditional_decision_tree_implies_no_cancellation={result['conditional_decision_tree_implies_no_cancellation']}`。",
        f"- `finite_signature_no_cancellation_closed={result['finite_signature_no_cancellation_closed']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 门控表",
        "",
        "| gate | available | needed | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=row["closed"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 完整路径预算模型",
            "",
            "| k | log y | raw support | full signatures | selected path support | required support | suffices |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {raw} | {count} | {selected} | {required} | `{suffices}` |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                raw=fmt_float(row["raw_support"]),
                count=fmt_float(row["full_signature_count"]),
                selected=fmt_float(row["selected_path_support"]),
                required=fmt_float(row["required_support"]),
                suffices=row["path_budget_suffices"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 结论",
            "",
            "新最窄内部目标为：",
            "",
            "```text",
            "ExactRIWDecisionTreeFormulaOrCleanReturn:",
            "  write the canonical RIW/Buchstab coefficients as a complete disjoint decision-tree expansion;",
            "  prove the complete trace count stays within the K6/polylog budget;",
            "  otherwise return over-budget/non-disjoint/cancelling blocks to edge/PDEC/SAE.",
            "```",
            "",
            "这仍不是行命题最终闭合；但它把无抵消从解析难题降为 exact 系数公式和 clean 准入合同。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selector-json", type=Path, default=DEFAULT_SELECTOR)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--support-power", type=float, default=7.0)
    parser.add_argument("--buchstab-loss", type=float, default=2.0)
    parser.add_argument("--full-signature-power", type=float, default=1.0)
    parser.add_argument("--required-loss", type=float, default=3.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.selector_json,
        args.min_k,
        args.max_k,
        args.support_power,
        args.buchstab_loss,
        args.full_signature_power,
        args.required_loss,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_internal_target": result["next_internal_target"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
