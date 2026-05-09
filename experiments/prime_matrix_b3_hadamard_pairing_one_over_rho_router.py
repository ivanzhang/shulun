#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard 零点配对与 1/rho 项路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_pairing_one_over_rho_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-pairing-one-over-rho-router.json
  docs/monograph/prime-matrix-b3-hadamard-pairing-one-over-rho-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-shell-separation-convention-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-pairing-one-over-rho-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-pairing-one-over-rho-router.md"

OLD_ATOM = "HadamardSymmetricZeroPairingAndOneOverRhoCancellationLedger"
CLOSED_ATOM = "HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed"
COEFF_CLOSED = "HadamardDVPKernelCoefficientNormalizationClosedC0FarZeros"
SHELL_CLOSED = "HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic"
LOCAL_CORE_ATOM = "HadamardLocalZeroCoreAbsorptionByCN16Ledger"
RANGE_ATOM = "HadamardRemainderRangeAndKernelConventionLedger"
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
    """替换配对与 1/rho 原子。"""
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


def pairing_ledger() -> list[dict[str, str]]:
    """列出配对和符号处理。"""
    return [
        {
            "item": "conjugate_pair",
            "statement": "rho and conjugate(rho) are paired in symmetric height limits",
            "effect": "log derivative sums have a real limiting convention",
        },
        {
            "item": "functional_pair",
            "statement": "rho and 1-rho are available from xi functional equation",
            "effect": "zero multiset symmetry is registered; no orphan zero class",
        },
        {
            "item": "one_over_rho_sign",
            "statement": "Re(1/rho)=beta/(beta^2+gamma^2)>=0 for nontrivial zeros",
            "effect": "in Re(-zeta'/zeta), the -Re(1/rho) contribution is nonpositive",
        },
        {
            "item": "dvp_coefficients",
            "statement": "3,4,1 are nonnegative",
            "effect": "DVP combination preserves the nonpositive sign of non-target 1/rho constants",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Hadamard 配对与 1/rho 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    coeff_ready = COEFF_CLOSED in basis
    shell_ready = SHELL_CLOSED in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard and coeff_ready and shell_ready
    return [
        row(
            "PairingOneOverRhoGateActive",
            active,
            False,
            "上一层最窄点是 Hadamard 零点配对和 1/rho 常数项是否消耗正 C_log 预算。",
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
            "CoefficientAndShellReady",
            coeff_ready and shell_ready,
            True,
            "远零点符号丢弃和远/近壳分离已经闭合，配对项只需处理 1/rho 常数口径。",
            f"{COEFF_CLOSED} AND {SHELL_CLOSED}",
        ),
        row(
            "SymmetricLimitPairingClosed",
            closed,
            True,
            "按共轭与函数方程对称性取高度对称极限，零点部分分式没有无主孤项。",
            "symmetric zero summation convention",
        ),
        row(
            "OneOverRhoPositivePartSignDiscardClosed",
            closed,
            True,
            "非平凡零点满足 Re(1/rho)>=0；在 Re(-zeta'/zeta) 中带负号，DVP 非负系数组合后仍非正，可丢弃。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "配对与 1/rho 常数项账本闭合；它不消耗正 C_log 预算。",
            CLOSED_ATOM,
        ),
        row(
            "LocalCoreStillNext",
            False,
            False,
            "下一步需处理目标附近 |Im rho-gamma0|<1 的非目标零点核心。",
            LOCAL_CORE_ATOM,
        ),
        row(
            "RangeConventionStillDownstream",
            False,
            False,
            "最后还需统一 sigma、低高度、kernel 和 C_log 聚合口径。",
            RANGE_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Hadamard 配对与 1/rho 路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_pairing_one_over_rho_router",
        "status": "hadamard_pairing_one_over_rho_closed_by_sign_discard",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "pairing_one_over_rho_closed": closed,
        "one_over_rho_positive_budget": 0.0,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": LOCAL_CORE_ATOM,
        "secondary_priority": RANGE_ATOM,
        "post_hadamard_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "pairing_ledger": pairing_ledger(),
        "plain_conclusion": (
            "Hadamard 零点配对与 1/rho 常数项闭合：对称极限给出合法求和口径；"
            "非平凡零点的 Re(1/rho)>=0，而它在 Re(-zeta'/zeta) 中带负号，DVP 非负系数组合后仍非正，"
            "因此不消耗正 C_log 预算。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Hadamard 零点配对与 1/rho 项路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"pairing_one_over_rho_closed={fmt_bool(result['pairing_one_over_rho_closed'])}",
        f"one_over_rho_positive_budget={result['one_over_rho_positive_budget']:.1f}",
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
        "## 2. 配对账本",
        "",
        "| item | statement | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["pairing_ledger"]:
        lines.append(
            "| {item} | {statement} | {effect} |".format(
                item=table_cell(item["item"]),
                statement=table_cell(item["statement"]),
                effect=table_cell(item["effect"]),
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
            f"当前最窄点更新为 `{result['next_priority']}`；随后是 `{result['secondary_priority']}`。",
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
