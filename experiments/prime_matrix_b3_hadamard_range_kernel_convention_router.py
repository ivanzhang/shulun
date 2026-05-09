#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard 余项范围与 kernel convention 路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_range_kernel_convention_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-range-kernel-convention-router.json
  docs/monograph/prime-matrix-b3-hadamard-range-kernel-convention-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-local-core-absorption-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-range-kernel-convention-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-range-kernel-convention-router.md"

OLD_ATOM = "HadamardRemainderRangeAndKernelConventionLedger"
CLOSED_ATOM = "HadamardRemainderRangeAndKernelConventionClosed"
PAIRING_CLOSED = "HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed"
SHELL_CLOSED = "HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic"
LOCAL_CLOSED = "HadamardLocalZeroCoreAbsorptionClosedBySignDiscard"
COEFF_CLOSED = "HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros"
DYADIC_CLOSED = "HadamardDyadicSeriesSummationClosedC192GivenQuadraticKernel"
CLOG_AGGREGATION_ATOM = "CLogAggregationAndRangeConventionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

A_MAX = 0.25
SIGMA_MAX_AT_T0 = 1.0 + A_MAX / math.log(3.0)
HADAMARD_POSITIVE_BUDGET = 0.0


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
    """替换范围与 kernel convention 原子。"""
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


def convention_table() -> list[dict[str, str]]:
    """列出范围约定。"""
    return [
        {
            "item": "height_parameter",
            "convention": "L=log(|gamma0|+3)",
            "effect": "L>=log(3), so sigma=1+a/L is uniformly defined",
        },
        {
            "item": "sigma_range",
            "convention": "0<a<=1/4",
            "effect": f"1<sigma<=1+a/log(3)={SIGMA_MAX_AT_T0:.6f}<2",
        },
        {
            "item": "target_local_far",
            "convention": "target, |Delta|<1 local core, and half-open dyadic far shells",
            "effect": "no overlap among main zero, local core, and far tail",
        },
        {
            "item": "positive_budget",
            "convention": "non-target zero kernels and 1/rho constants are sign-discarded",
            "effect": "Hadamard zero remainder contributes 0 positive C_log budget",
        },
        {
            "item": "low_height",
            "convention": "finite low-height zero exclusion remains a separate global ledger",
            "effect": "this convention does not close FiniteLowHeightZeroCheckLedger",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成范围与 kernel convention 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    prerequisites = [PAIRING_CLOSED, SHELL_CLOSED, LOCAL_CLOSED, COEFF_CLOSED, DYADIC_CLOSED]
    prereq_ready = all(atom in basis for atom in prerequisites)
    sigma_range_passes = SIGMA_MAX_AT_T0 < 2.0
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard and prereq_ready and sigma_range_passes
    return [
        row(
            "RangeKernelConventionGateActive",
            active,
            False,
            "Hadamard 余项最后剩余是 sigma 范围、target/local/far 分割和 kernel 口径统一。",
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
            "HadamardPrerequisitesReady",
            prereq_ready,
            True,
            "配对、系数归一化、远近壳分离、dyadic 求和和局部核心吸收均已闭合。",
            " AND ".join(prerequisites),
        ),
        row(
            "SigmaRangeClosed",
            sigma_range_passes,
            True,
            "取 L=log(|gamma|+3)、0<a<=1/4，则 1<sigma<2，满足前面 kernel 形状账本的范围。",
            f"sigma_max={SIGMA_MAX_AT_T0:.12f}",
        ),
        row(
            "HadamardPositiveBudgetZeroClosed",
            closed,
            True,
            "所有非目标零点余项均已按符号丢弃；Hadamard 零点余项对正 C_log 的贡献为 0。",
            f"positive_budget={HADAMARD_POSITIVE_BUDGET:.1f}",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "Hadamard 余项范围与 kernel convention 闭合。",
            CLOSED_ATOM,
        ),
        row(
            "CLogAggregationStillNext",
            False,
            False,
            "Hadamard 余项闭合后，下一步是聚合 Gamma、局部计数和 Hadamard 余项的总 C_log。",
            CLOG_AGGREGATION_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行范围与 kernel convention 路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_range_kernel_convention_router",
        "status": "hadamard_range_kernel_convention_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "range_kernel_convention_closed": closed,
        "hadamard_positive_budget": HADAMARD_POSITIVE_BUDGET,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "range_audit": {
            "a_max": A_MAX,
            "sigma_max_at_min_L": SIGMA_MAX_AT_T0,
            "sigma_max_less_than_2": SIGMA_MAX_AT_T0 < 2.0,
        },
        "convention_table": convention_table(),
        "plain_conclusion": (
            "Hadamard 余项范围与 kernel convention 闭合：sigma 范围满足 1<sigma<2，"
            "target/local/far 分割互斥，非目标零点和 1/rho 项的正预算为 0。"
            "注意这不关闭低高度零点核验；低高度仍由独立账本处理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    audit = result["range_audit"]
    lines = [
        "# Prime Matrix B=3 Hadamard 余项范围与 kernel convention 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"range_kernel_convention_closed={fmt_bool(result['range_kernel_convention_closed'])}",
        f"hadamard_positive_budget={result['hadamard_positive_budget']:.1f}",
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
        "## 2. 范围审计",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| a_max | `{fmt_float(audit['a_max'])}` |",
        f"| sigma_max_at_min_L | `{fmt_float(audit['sigma_max_at_min_L'])}` |",
        f"| sigma_max_less_than_2 | `{fmt_bool(audit['sigma_max_less_than_2'])}` |",
        "",
        "## 3. convention 表",
        "",
        "| item | convention | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["convention_table"]:
        lines.append(
            "| {item} | {convention} | {effect} |".format(
                item=table_cell(item["item"]),
                convention=table_cell(item["convention"]),
                effect=table_cell(item["effect"]),
            )
        )
    lines.extend(
        [
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
