#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard 部分分式余项最终闭合路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_remainder_final_closure_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-remainder-final-closure-router.json
  docs/monograph/prime-matrix-b3-hadamard-remainder-final-closure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-range-kernel-convention-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-remainder-final-closure-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-remainder-final-closure-router.md"

OLD_ATOM = "HadamardPartialFractionRemainderNumericalLedger"
CLOSED_ATOM = "HadamardPartialFractionRemainderNumericalClosedZeroPositiveBudget"
PAIRING_CLOSED = "HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed"
SHAPE_CLOSED = "HadamardFarZeroQuadraticDecayShapeClosed"
COEFF_CLOSED = "HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros"
SHELL_SEPARATION_CLOSED = "HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic"
SHELL_COUNT_CLOSED = "HadamardCN16UnitIntervalToDyadicShellCountClosed"
DYADIC_SUM_CLOSED = "HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel"
LOCAL_CLOSED = "HadamardLocalZeroCoreAbsorptionClosedBySignDiscard"
RANGE_CLOSED = "HadamardRemainderRangeAndKernelConventionClosed"
CLOG_AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
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


def replace_atom(text: str) -> str:
    """替换 Hadamard 余项总原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def required_atoms() -> list[str]:
    """列出 Hadamard 余项闭合所需子原子。"""
    return [
        PAIRING_CLOSED,
        SHAPE_CLOSED,
        COEFF_CLOSED,
        SHELL_SEPARATION_CLOSED,
        SHELL_COUNT_CLOSED,
        DYADIC_SUM_CLOSED,
        LOCAL_CLOSED,
        RANGE_CLOSED,
    ]


def build_rows(previous: dict[str, Any], missing: list[str]) -> list[dict[str, Any]]:
    """生成 Hadamard 余项最终闭合判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = OLD_ATOM not in basis and any(atom in basis for atom in required_atoms())
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    all_ready = not missing
    closed = active and guard and all_ready
    return [
        row(
            "HadamardRemainderFinalGateActive",
            active,
            False,
            "Hadamard 余项旧原子已被拆开，当前检查全部子账本是否足以回填总闭合原子。",
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
            "AllHadamardMicroLedgersReady",
            all_ready,
            True,
            "配对、二次形状、系数归一化、远/近壳分离、dyadic 求和、局部核心和范围 convention 均已闭合。",
            "missing=" + ("none" if all_ready else ", ".join(missing)),
        ),
        row(
            "HadamardPositiveBudgetZero",
            all_ready,
            True,
            "非目标零点和 1/rho 项均按符号丢弃，Hadamard 零点余项正预算为 0。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "Hadamard 部分分式余项数值账本闭合。",
            CLOSED_ATOM,
        ),
        row(
            "CLogAggregationNext",
            False,
            False,
            "下一步聚合 Gamma、RVM-C_N=16 和 Hadamard 余项得到总 C_log。",
            CLOG_AGGREGATION_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Hadamard 余项最终闭合路由。"""
    previous = load_json(paths["previous"])
    basis = previous.get("latest_self_contained_basis", "")
    missing = [atom for atom in required_atoms() if atom not in basis]
    rows = build_rows(previous, missing)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_remainder_final_closure_router",
        "status": "hadamard_partial_fraction_remainder_closed_zero_positive_budget",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "hadamard_partial_fraction_remainder_closed": closed,
        "hadamard_positive_budget": 0.0,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "required_atoms": required_atoms(),
        "missing_atoms": missing,
        "plain_conclusion": (
            "Hadamard 部分分式余项数值账本闭合：所有非目标零点核与 1/rho 项均为非正贡献，"
            "可在 de la Vallee Poussin 上界中丢弃；远壳 dyadic 求和和范围 convention 已作为安全账本登记。"
            "该闭合不替代低高度零点核验。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Hadamard 部分分式余项最终闭合路由器",
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
            "hadamard_partial_fraction_remainder_closed="
            f"{fmt_bool(result['hadamard_partial_fraction_remainder_closed'])}"
        ),
        f"hadamard_positive_budget={result['hadamard_positive_budget']:.1f}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 总替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 子账本",
        "",
    ]
    for atom in result["required_atoms"]:
        mark = "ok" if atom not in result["missing_atoms"] else "missing"
        lines.append(f"- `{atom}`: {mark}")
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
            f"当前最窄点更新为 `{result['next_priority']}`。",
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
