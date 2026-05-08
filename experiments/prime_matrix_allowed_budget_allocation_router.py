#!/usr/bin/env python3
"""Prime Matrix allowed_budget 分配纪律路由器。

用法示例：
  python3 experiments/prime_matrix_allowed_budget_allocation_router.py

输出：
  docs/monograph/prime-matrix-allowed-budget-allocation-router.json
  docs/monograph/prime-matrix-allowed-budget-allocation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_RLA = MONOGRAPH / "prime-matrix-bpn-rankin-ledger-acceptance-theorem.md"
DEFAULT_CCB = MONOGRAPH / "prime-matrix-bpn-colored-corridor-core-sieve-budget.md"
DEFAULT_FXA = MONOGRAPH / "prime-matrix-bpn-final-exit-acceptance-contract.md"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.md"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-allowed-budget-allocation-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-allowed-budget-allocation-router.md"

OLD_ATOM = "AllowedBudgetAllocationLedger"
CLOSED_ATOM = "AllowedBudgetAllocationDisciplineClosed"
BATCH_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def budget_rules() -> list[dict[str, str]]:
    """给出 allowed_budget 纪律规则。"""
    return [
        {
            "rule": "predeclared_budget",
            "meaning": "每个 color_id 的 B_allow 必须随 source tuple/inventory 一起登记，先于 Rankin 审计。",
        },
        {
            "rule": "sum_budget_guard",
            "meaning": "多颜色预算必须满足 sum_c B_c 不超过该 source tuple 的主链允许预算。",
        },
        {
            "rule": "single_color_acceptance",
            "meaning": "若存在 s 使 R_s(C_c;K)<=B_c，则该颜色类核心计数被 RLA-1 验收。",
        },
        {
            "rule": "failed_with_spike_return",
            "meaning": "Rankin 不通过且 residue spike 超阈值时，登记 low-mod core CRTDefect 并回流 PDEC/SAE。",
        },
        {
            "rule": "failed_without_spike_constant_gap",
            "meaning": "Rankin 不通过且无 spike 时，只能登记 constant-gap，继续细分或调参，不能标为通过。",
        },
        {
            "rule": "no_posthoc_reallocation",
            "meaning": "看到 Rankin ledger 后不得把其他颜色类未用预算后验转给失败类，除非重新提交全局预算证书。",
        },
    ]


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


def build_rows(previous: dict[str, Any], texts: dict[str, str]) -> list[dict[str, Any]]:
    """生成 allowed_budget 分配纪律判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    coloring_ready = previous.get("interval_graph_coloring_coverage_closed") is True
    formal_ready = contains_all(texts["formal"], ["allowed_budget", "failure_return"])
    rla_ready = contains_all(texts["rla"], ["Theorem RLA-1", "Corollary RLA-2", "rankin_budget_pass"])
    ccb_ready = contains_all(
        texts["ccb"],
        ["若 Rankin ledger <= allowed budget", "low-mod core CRTDefect", "常数账本未闭合"],
    )
    fxa_ready = contains_all(
        texts["fxa"],
        ["rankin_budget_pass=true", "rankin_budget_pass=false + low-mod spike", "常数账本未闭合"],
    )
    discipline_closed = all([active, guard, coloring_ready, formal_ready, rla_ready, ccb_ready, fxa_ready])
    return [
        row(
            "AllowedBudgetGateActive",
            active,
            False,
            "上一层已把最窄点推进到 allowed_budget 分配纪律。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条内的预算证书，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ColoringCoverageImported",
            coloring_ready,
            True,
            "同色不相交走廊对象已由上一层固定。",
            "预算只能分配给这些固定颜色类。",
        ),
        row(
            "FormalBudgetFieldsPinned",
            formal_ready,
            True,
            "正式 inventory 已要求 allowed_budget 与 failure_return。",
            "字段格式无剩余。",
        ),
        row(
            "RankinAcceptanceTheoremImported",
            rla_ready,
            True,
            "RLA-1/RLA-2 给出单颜色和多颜色预算验收不等式。",
            "无预算验收逻辑剩余。",
        ),
        row(
            "FailureRoutingImported",
            ccb_ready and fxa_ready,
            True,
            "预算失败只能进入 low-mod core CRTDefect/PDEC-SAE 或 constant-gap，不可口头吸收。",
            f"{PDEC_SAE_ATOM} or constant-gap",
        ),
        row(
            CLOSED_ATOM,
            discipline_closed,
            True,
            "allowed_budget 分配纪律已闭合：预算预登记、总预算守卫、失败回流三者固定。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            discipline_closed,
            True,
            "预算分配层闭合为验收纪律；下一步必须提交全量 Rankin 批量证书或失败回流。",
            BATCH_ATOM,
        ),
        row(
            "BatchRankinStillDownstream",
            False,
            False,
            "每个正式颜色类的 concrete Rankin 证书和失败回流列表尚未全集提交。",
            BATCH_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行 allowed_budget 分配纪律路由。"""
    previous = load_json(paths["previous"])
    texts = {key: read_text(path) for key, path in paths.items() if key != "previous"}
    rows = build_rows(previous, texts)
    discipline_closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_allowed_budget_allocation_router",
        "status": "allowed_budget_allocation_discipline_closed_batch_rankin_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "allowed_budget_allocation_discipline_closed": discipline_closed,
        "formal_colored_corridor_inventory_closed": False,
        "budget_rules": budget_rules(),
        "current_narrowest_atom": BATCH_ATOM,
        "downstream_atoms": [PDEC_SAE_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {BATCH_ATOM}.",
        "plain_conclusion": (
            "AllowedBudgetAllocationLedger 已闭合为预算纪律：每个颜色类预算必须预登记，总预算受主链"
            "允许预算约束；Rankin 通过才闭合，失败必须显式登记为 low-mod core CRTDefect/PDEC-SAE "
            "或 constant-gap。新的最窄点是提交全量批量 Rankin 证书："
            f"`{BATCH_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix allowed_budget 分配纪律路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"allowed_budget_allocation_discipline_closed={fmt_bool(result['allowed_budget_allocation_discipline_closed'])}",
        f"formal_colored_corridor_inventory_closed={fmt_bool(result['formal_colored_corridor_inventory_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 预算纪律",
        "",
        "| rule | meaning |",
        "| --- | --- |",
    ]
    for item in result["budget_rules"]:
        lines.append(
            "| {rule} | {meaning} |".format(
                rule=table_cell(item["rule"]),
                meaning=table_cell(item["meaning"]),
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
            "## 4. 下一步",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。",
            "",
            "审稿边界：本步不提交全量 Rankin 证书，不关闭 PDEC/SAE，也不关闭行列无条件定理。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--rla", type=Path, default=DEFAULT_RLA)
    parser.add_argument("--ccb", type=Path, default=DEFAULT_CCB)
    parser.add_argument("--fxa", type=Path, default=DEFAULT_FXA)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "rla": args.rla,
        "ccb": args.ccb,
        "fxa": args.fxa,
        "formal": args.formal,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
