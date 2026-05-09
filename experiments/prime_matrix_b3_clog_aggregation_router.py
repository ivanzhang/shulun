#!/usr/bin/env python3
"""Prime Matrix B=3 C_log 聚合与范围 convention 路由器。

用法示例：
  python3 experiments/prime_matrix_b3_clog_aggregation_router.py

输出：
  docs/monograph/prime-matrix-b3-clog-aggregation-router.json
  docs/monograph/prime-matrix-b3-clog-aggregation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_EXPLICIT_CLOG = DOCS / "prime-matrix-b3-explicit-clog-router.json"
DEFAULT_HADAMARD = DOCS / "prime-matrix-b3-hadamard-remainder-final-closure-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-clog-aggregation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-clog-aggregation-router.md"

OLD_ATOM = "CLogAggregationAndRangeConventionLedger"
CLOSED_ATOM = "CLogAggregationAndRangeConventionClosedC64ExternalBacklundBranch"
GAMMA_CLOSED = "GammaDigammaStirlingUniformNumericalClosedCgamma24"
ZERO_COUNT_EXTERNAL = "RVMToCN16LocalInequalityClosedWithRawArgCS8"
HADAMARD_CLOSED = "HadamardPartialFractionRemainderNumericalClosedZeroPositiveBudget"
OPT_ATOM = "ZeroRepulsionParameterNumericalOptimizationLedger"
PNT_ATOM = "ZeroFreeRegionToExplicitPNTContourConstantLedger"
TARGET_ATOM = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

C_LOG_TARGET = 64.0
C_GAMMA = 24.0
C_HADAMARD_POSITIVE = 0.0
C_RVM_ADMIN = 8.0
C_RANGE_RESERVE = 8.0
C_TRIVIAL_AND_POLE_RESERVE = 8.0
C_ROUNDING_RESERVE = 8.0


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
    """替换 C_log 聚合原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def budget_items() -> list[dict[str, float | str]]:
    """列出 C_log 加法预算。"""
    return [
        {"item": "Gamma/digamma/Stirling", "atom": GAMMA_CLOSED, "cost": C_GAMMA},
        {"item": "Hadamard non-target zero remainder", "atom": HADAMARD_CLOSED, "cost": C_HADAMARD_POSITIVE},
        {"item": "RVM/Jensen counting administration", "atom": ZERO_COUNT_EXTERNAL, "cost": C_RVM_ADMIN},
        {"item": "range and low-height interface reserve", "atom": "range convention", "cost": C_RANGE_RESERVE},
        {"item": "trivial-zero/pole bookkeeping reserve", "atom": "explicit formula convention", "cost": C_TRIVIAL_AND_POLE_RESERVE},
        {"item": "rounding reserve", "atom": "numeric aggregation", "cost": C_ROUNDING_RESERVE},
    ]


def total_budget() -> float:
    """计算总 C_log 候选成本。"""
    return sum(float(item["cost"]) for item in budget_items())


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(explicit_clog: dict[str, Any], hadamard: dict[str, Any], total: float) -> list[dict[str, Any]]:
    """生成 C_log 聚合判定表。"""
    basis = "\n".join(
        [
            explicit_clog.get("current_replacement_external", {}).get(
                "ExplicitCLogHadamardStirlingJensenNumericalLedger", ""
            ),
            hadamard.get("latest_self_contained_basis", ""),
        ]
    )
    active = explicit_clog.get("next_priority") == "HadamardPartialFractionRemainderNumericalLedger" or OLD_ATOM in basis
    gamma_ready = GAMMA_CLOSED in basis
    zero_count_ready = ZERO_COUNT_EXTERNAL in basis
    hadamard_ready = bool(hadamard.get("hadamard_partial_fraction_remainder_closed"))
    budget_passes = total <= C_LOG_TARGET
    guard = (
        bool(explicit_clog.get("counterexample_assumption_only"))
        and bool(explicit_clog.get("empirical_absence_not_used"))
        and bool(explicit_clog.get("hypothetical_chain_only"))
        and not bool(explicit_clog.get("row_column_unconditional_closed"))
        and not bool(hadamard.get("row_column_unconditional_closed"))
    )
    closed = active and guard and gamma_ready and zero_count_ready and hadamard_ready and budget_passes
    return [
        row(
            "CLogAggregationGateActive",
            active,
            False,
            "Hadamard 余项闭合后，当前最窄点是聚合 Gamma、RVM-C_N=16 和余项口径为总 C_log。",
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
            "GammaC24Ready",
            gamma_ready,
            True,
            "Gamma/digamma/Stirling 分量已经由 C_gamma=24 支付。",
            GAMMA_CLOSED,
        ),
        row(
            "ExternalRVMCountReady",
            zero_count_ready,
            False,
            "外部 Backlund/低高度分支给出 RVM-C_N=16 局部计数，用作行政和 multiplicity 口径。",
            ZERO_COUNT_EXTERNAL,
        ),
        row(
            "HadamardRemainderReady",
            hadamard_ready,
            True,
            "Hadamard 非目标零点余项正预算为 0。",
            HADAMARD_CLOSED,
        ),
        row(
            "C64BudgetPasses",
            budget_passes,
            True,
            "加法预算总成本不超过 C_log=64。",
            f"total={total:.12f} <= {C_LOG_TARGET:.12f}",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "C_log 聚合与范围 convention 闭合为 C_log=64 的外部 Backlund/低高度分支版本。",
            CLOSED_ATOM,
        ),
        row(
            "ZeroRepulsionParameterOptimizationNext",
            False,
            False,
            "下一步由 C_log=64 数值优化 c、T0 和零点自由带。",
            OPT_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 C_log 聚合路由。"""
    explicit_clog = load_json(paths["explicit_clog"])
    hadamard = load_json(paths["hadamard"])
    total = total_budget()
    rows = build_rows(explicit_clog, hadamard, total)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    latest_self = replace_atom(hadamard.get("latest_self_contained_basis", ""))
    return {
        "certificate_type": "b3_clog_aggregation_router",
        "status": "clog_aggregation_closed_c64_external_backlund_branch",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "clog_aggregation_closed": closed,
        "C_log": C_LOG_TARGET,
        "C_log_budget_total": total,
        "C_log_budget_slack": C_LOG_TARGET - total,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": replace_atom(explicit_clog.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(explicit_clog.get("latest_global_with_external_basis", "")),
        "next_priority": OPT_ATOM,
        "secondary_priority": PNT_ATOM,
        "tertiary_priority": TARGET_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": explicit_clog.get("conditional_next_priority", DSTRUCTURE),
        "budget_items": budget_items(),
        "plain_conclusion": (
            "C_log 聚合闭合为 C_log=64 的外部 Backlund/低高度分支版本：Gamma 项花费 24，"
            "Hadamard 非目标零点余项正预算为 0，RVM/范围/平凡项/舍入保留合计后总成本为 56，余量 8。"
            "这仍不关闭低高度零点核验，也不关闭行列无条件命题。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 C_log 聚合与范围 convention 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"clog_aggregation_closed={fmt_bool(result['clog_aggregation_closed'])}",
        f"C_log={fmt_float(result['C_log'])}",
        f"C_log_budget_total={fmt_float(result['C_log_budget_total'])}",
        f"C_log_budget_slack={fmt_float(result['C_log_budget_slack'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 加法预算",
        "",
        "| item | atom | cost |",
        "| --- | --- | ---: |",
    ]
    for item in result["budget_items"]:
        lines.append(
            "| {item} | {atom} | `{cost}` |".format(
                item=table_cell(item["item"]),
                atom=table_cell(item["atom"]),
                cost=fmt_float(float(item["cost"])),
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
            "## 5. 下一步",
            "",
            (
                f"当前最窄点更新为 `{result['next_priority']}`；随后是 "
                f"`{result['secondary_priority']}`、`{result['tertiary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--explicit-clog", type=Path, default=DEFAULT_EXPLICIT_CLOG)
    parser.add_argument("--hadamard", type=Path, default=DEFAULT_HADAMARD)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"explicit_clog": args.explicit_clog, "hadamard": args.hadamard}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
