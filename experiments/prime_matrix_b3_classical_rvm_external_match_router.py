#!/usr/bin/env python3
"""Prime Matrix B=3 经典 Riemann-von Mangoldt 外部公式匹配路由器。

用法示例：
  python3 experiments/prime_matrix_b3_classical_rvm_external_match_router.py

输出：
  docs/monograph/prime-matrix-b3-classical-rvm-external-match-router.json
  docs/monograph/prime-matrix-b3-classical-rvm-external-match-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-unsmoothed-perron-formula-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-classical-rvm-external-match-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-classical-rvm-external-match-router.md"

OLD_ATOM = "ClassicalVonMangoldtExplicitFormulaExternalAcceptanceOrInlineProofLedger"
HIGH_THRESHOLD_EXTERNAL_ATOM = "CullyHugillJohnstonRvMExplicitFormulaHighThresholdRegistered"
INTERNAL_ALL_X_ATOM = "InternalPsi0PerronFormulaAllXGe20000ConstantProofLedger"
PERRON_KERNEL_ATOM = "PerronKernelTruncationConstantForPsi0Ledger"
ZERO_SUM_ATOM = "ZeroFreeRegionZeroSumContourNumericalBudgetC1280T14Ledger"
FINITE_LOW_HEIGHT = "FiniteLowHeightZeroCheckLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000.0
ANCHOR_LOG = math.log(ANCHOR_X)
EXTERNAL_MIN_LOG_X = 40.0
EXTERNAL_MIN_T_AT_ANCHOR = ANCHOR_LOG**2
CONTRACT_MIN_T = 14.0


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


def replacement_pair() -> str:
    """写出外部候选与内部自足替代的二分包。"""
    return f"({HIGH_THRESHOLD_EXTERNAL_ATOM} OR {INTERNAL_ALL_X_ATOM})"


def replace_atom(text: str) -> str:
    """替换经典公式输入原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def external_contract() -> dict[str, Any]:
    """记录外部候选定理与本项目需求的参数匹配。"""
    threshold_match = EXTERNAL_MIN_LOG_X <= ANCHOR_LOG
    t_lower_match = EXTERNAL_MIN_T_AT_ANCHOR <= CONTRACT_MIN_T
    fixed_t_match = False
    psi0_match = False
    strict_match = threshold_match and t_lower_match and fixed_t_match and psi0_match
    return {
        "external_source": "Cully-Hugill and Johnston, On the error term in the explicit formula of Riemann-von Mangoldt II",
        "external_url": "https://arxiv.org/abs/2402.04272",
        "external_shape": "psi(x)=x-sum_{|gamma|<=T*}x^rho/rho+O*(M*x*(log x)^(1-omega)/T)",
        "external_min_log_x": EXTERNAL_MIN_LOG_X,
        "external_uses_T_star_in_T_2T": True,
        "contract_anchor_x": ANCHOR_X,
        "contract_log_anchor_x": ANCHOR_LOG,
        "contract_min_T": CONTRACT_MIN_T,
        "external_min_T_at_anchor_if_applicable": EXTERNAL_MIN_T_AT_ANCHOR,
        "threshold_match": threshold_match,
        "t_lower_bound_match": t_lower_match,
        "fixed_T_match": fixed_t_match,
        "psi0_half_weight_match": psi0_match,
        "strict_match_closed": strict_match,
    }


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


def build_rows(previous: dict[str, Any], contract: dict[str, Any]) -> list[dict[str, Any]]:
    """生成外部 RvM 匹配判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    upstream_reduced = bool(previous.get("unsmoothed_perron_formula_reduced"))
    external_registered = True
    strict_match = bool(contract["strict_match_closed"])
    reduced = active and guard and upstream_reduced and external_registered
    return [
        row(
            "ClassicalRvMGateActive",
            active,
            False,
            "上一层最窄点要求接受经典 von Mangoldt 显式公式或给出内联证明。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只审查假设链条解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ExternalRvMHighThresholdCandidateRegistered",
            external_registered,
            False,
            "Cully-Hugill/Johnston 给出显式截断 Riemann-von Mangoldt 公式候选。",
            HIGH_THRESHOLD_EXTERNAL_ATOM,
        ),
        row(
            "ExternalThresholdDoesNotMatchX20000",
            bool(contract["threshold_match"]),
            False,
            "该外部定理按 log x>=40 等高阈值使用，不能直接覆盖 x=20000。",
            "需要有限桥或内部 all-x Perron 证明。",
        ),
        row(
            "ExternalTWindowDoesNotMatchT14",
            bool(contract["t_lower_bound_match"]),
            False,
            "外部定理需要较大 T 下界且使用某个 T* in [T,2T]，不能直接替代固定 T>=14 合同。",
            "需要重新参数化或内部截断核账本。",
        ),
        row(
            "Psi0HalfWeightNotMatchedByExternalPsiStatement",
            bool(contract["psi0_half_weight_match"]),
            False,
            "外部候选以 psi(x) 叙述；本项目合同需要 psi_0 半权端点和端点误差口径。",
            INTERNAL_ALL_X_ATOM,
        ),
        row(
            "ExternalStrictMatchClosed",
            strict_match,
            False,
            "只有阈值、T 窗口、固定截断点和 psi_0 端点全部匹配后才能接受为本原子闭合。",
            HIGH_THRESHOLD_EXTERNAL_ATOM if strict_match else INTERNAL_ALL_X_ATOM,
        ),
        row(
            "ClassicalRvMExternalMatchReduced",
            reduced,
            False,
            "外部候选已登记但不能直接关闭；本原子被压成高阈值外部候选或内部 all-x Perron 证明。",
            replacement_pair(),
        ),
        row(
            OLD_ATOM,
            strict_match,
            False,
            "当前外部候选不满足严格对接，因此作者侧自足路线仍需内部 all-x 证明。",
            replacement_pair(),
        ),
        row(
            PERRON_KERNEL_ATOM,
            False,
            False,
            "内部 all-x 证明的核心仍是 Perron 截断核常数账本。",
            PERRON_KERNEL_ATOM,
        ),
        row(
            ZERO_SUM_ATOM,
            False,
            False,
            "经典公式或内联证明之后，仍需零点和轮廓数值预算。",
            ZERO_SUM_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行经典 RvM 外部匹配路由。"""
    previous = load_json(paths["previous"])
    contract = external_contract()
    rows = build_rows(previous, contract)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ClassicalRvMExternalMatchReduced"
    )
    strict = bool(contract["strict_match_closed"])
    return {
        "certificate_type": "b3_classical_rvm_external_match_router",
        "status": "classical_rvm_external_candidate_registered_strict_match_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "classical_rvm_external_match_reduced": reduced,
        "classical_rvm_external_strict_match_closed": strict,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": replace_atom(previous.get("latest_conditional_basis", "")),
        "latest_global_with_external_basis": replace_atom(previous.get("latest_global_with_external_basis", "")),
        "next_priority": INTERNAL_ALL_X_ATOM,
        "secondary_priority": PERRON_KERNEL_ATOM,
        "post_rvm_priority": ZERO_SUM_ATOM,
        "finite_low_height_priority": FINITE_LOW_HEIGHT,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "external_contract": contract,
        "plain_conclusion": (
            "外部 Riemann-von Mangoldt 显式公式候选已经定位，但它按高阈值 log x>=40、"
            "较大 T 下界和 T*∈[T,2T] 截断点工作，且以 psi(x) 而非 psi_0 半权端点叙述。"
            "因此它可以作为高阈值参考，不能严格关闭本项目 x>=20000,T>=14 的自足合同；"
            "下一步仍需内部 all-x Perron 证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    contract = result["external_contract"]
    lines = [
        "# Prime Matrix B=3 经典 Riemann-von Mangoldt 外部公式匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"classical_rvm_external_match_reduced={fmt_bool(result['classical_rvm_external_match_reduced'])}",
        f"classical_rvm_external_strict_match_closed={fmt_bool(result['classical_rvm_external_strict_match_closed'])}",
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
        "## 2. 外部候选合同",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in contract.items():
        lines.append(f"| {key} | `{table_cell(value)}` |")
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
                f"当前最窄点更新为 `{result['next_priority']}`；其核心计算账本是 "
                f"`{result['secondary_priority']}`，随后再进入 `{result['post_rvm_priority']}`。"
            ),
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
