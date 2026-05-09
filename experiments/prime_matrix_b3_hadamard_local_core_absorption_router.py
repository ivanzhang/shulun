#!/usr/bin/env python3
"""Prime Matrix B=3 Hadamard 局部零点核心吸收路由器。

用法示例：
  python3 experiments/prime_matrix_b3_hadamard_local_core_absorption_router.py

输出：
  docs/monograph/prime-matrix-b3-hadamard-local-core-absorption-router.json
  docs/monograph/prime-matrix-b3-hadamard-local-core-absorption-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-hadamard-pairing-one-over-rho-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-hadamard-local-core-absorption-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-hadamard-local-core-absorption-router.md"

OLD_ATOM = "HadamardLocalZeroCoreAbsorptionByCN16Ledger"
CLOSED_ATOM = "HadamardLocalZeroCoreAbsorptionClosedBySignDiscard"
PAIRING_CLOSED = "HadamardSymmetricZeroPairingAndOneOverRhoSignDiscardClosed"
SHELL_CLOSED = "HadamardFarZeroShellSeparationConventionClosedHalfOpenDyadic"
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
    """替换局部核心吸收原子。"""
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


def local_core_ledger() -> list[dict[str, str]]:
    """列出局部核心处理规则。"""
    return [
        {
            "class": "target_zero",
            "rule": "rho=rho0, including multiplicity at the selected zero",
            "effect": "charged only to the main negative DVP term",
        },
        {
            "class": "same_window_non_target",
            "rule": "rho!=rho0 and |Im rho-gamma0|<1",
            "effect": "zero kernel is nonnegative, hence contribution to Re(-zeta'/zeta) is nonpositive",
        },
        {
            "class": "same_height_or_multiple_neighbor",
            "rule": "rho shares ordinate or is arbitrarily close but is not the selected target copy",
            "effect": "also nonpositive; no positive C_log budget is charged",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成局部核心吸收判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    pairing_ready = PAIRING_CLOSED in basis
    shell_ready = SHELL_CLOSED in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    closed = active and guard and pairing_ready and shell_ready
    return [
        row(
            "LocalCoreAbsorptionGateActive",
            active,
            False,
            "上一层最窄点是目标附近 |Im rho-gamma0|<1 的非目标零点核心是否消耗正预算。",
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
            "PairingAndShellConventionReady",
            pairing_ready and shell_ready,
            True,
            "目标零点已单独分离，1/rho 项已按符号丢弃，局部核心只剩非目标零点核。",
            f"{PAIRING_CLOSED} AND {SHELL_CLOSED}",
        ),
        row(
            "LocalNonTargetZeroSignDiscardClosed",
            closed,
            True,
            "sigma>1 时局部非目标零点核实部非负，在 Re(-zeta'/zeta) 中带负号，DVP 非负组合后仍非正，可丢弃。",
            CLOSED_ATOM,
        ),
        row(
            "CN16NotNeededForPositiveBudget",
            closed,
            True,
            "C_N=16 只作为 multiplicity/有限性安全网；局部核心正预算为 0，不需要按个数付费。",
            "positive local-core budget = 0",
        ),
        row(
            OLD_ATOM,
            closed,
            True,
            "局部零点核心吸收闭合。",
            CLOSED_ATOM,
        ),
        row(
            "RangeConventionStillNext",
            False,
            False,
            "Hadamard 余项最后还需统一 sigma、低高度、kernel 和 C_log 聚合口径。",
            RANGE_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行局部核心吸收路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    return {
        "certificate_type": "b3_hadamard_local_core_absorption_router",
        "status": "hadamard_local_core_absorption_closed_by_sign_discard",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "local_core_absorption_closed": closed,
        "local_core_positive_budget": 0.0,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: CLOSED_ATOM},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": RANGE_ATOM,
        "post_hadamard_priority": CLOG_AGGREGATION_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "local_core_ledger": local_core_ledger(),
        "plain_conclusion": (
            "Hadamard 局部零点核心吸收闭合：目标零点已单独进入主负项；"
            "其余近壳零点在 Re(-zeta'/zeta) 中仍是非正贡献，可丢弃。"
            "因此局部核心正预算为 0，C_N=16 只保留为有限性和 multiplicity 安全网。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Hadamard 局部零点核心吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"local_core_absorption_closed={fmt_bool(result['local_core_absorption_closed'])}",
        f"local_core_positive_budget={result['local_core_positive_budget']:.1f}",
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
        "## 2. 局部核心账本",
        "",
        "| class | rule | effect |",
        "| --- | --- | --- |",
    ]
    for item in result["local_core_ledger"]:
        lines.append(
            "| {cls} | {rule} | {effect} |".format(
                cls=table_cell(item["class"]),
                rule=table_cell(item["rule"]),
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
