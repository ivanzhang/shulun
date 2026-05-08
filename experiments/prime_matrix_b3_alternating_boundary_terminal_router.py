#!/usr/bin/env python3
"""Prime Matrix B=3 交错边界余项终端路由器。

用法示例：
  python3 experiments/prime_matrix_b3_alternating_boundary_terminal_router.py

输出：
  docs/monograph/prime-matrix-b3-alternating-boundary-terminal-router.json
  docs/monograph/prime-matrix-b3-alternating-boundary-terminal-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-prime-word-stieltjes-integral-router.json"
DEFAULT_AUDIT = DOCS / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-alternating-boundary-terminal-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-alternating-boundary-terminal-router.md"

BOUNDARY_ATOM = "B3AlternatingBoundaryRemainderOnePercentLedger"
MERTENS_ATOM = "B3PrimeHarmonicMertensUniformEnvelopePGe100000"
VARIATION_ATOM = "B3BoundaryVariationOnePercentTransferLedger"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
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


def replacement_pair() -> str:
    """写出自足替换包。"""
    return f"({MERTENS_ATOM} AND {VARIATION_ATOM})"


def replace_boundary_atom(text: str) -> str:
    """替换交错边界余项原子。"""
    return text.replace(BOUNDARY_ATOM, replacement_pair())


def audit_summary(audit: dict[str, Any]) -> dict[str, Any]:
    """提取 checkpoint 强余量。"""
    rows = audit.get("audit", {}).get("checkpoint_rows", [])
    if not rows:
        return {
            "checkpoint_count": 0,
            "min_checkpoint_ratio": None,
            "min_checkpoint_P": None,
            "min_surplus_to_99pct": None,
        }
    min_row = min(rows, key=lambda item: item["ratio_W_over_Vf"])
    return {
        "checkpoint_count": len(rows),
        "min_checkpoint_ratio": min_row["ratio_W_over_Vf"],
        "min_checkpoint_P": min_row["P"],
        "min_surplus_to_99pct": min_row["ratio_minus_0_99"],
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


def build_rows(previous: dict[str, Any], summary: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 B=3 交错边界终端判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == BOUNDARY_ATOM and BOUNDARY_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    stieltjes_closed = bool(previous.get("prime_word_stieltjes_integral_ledger_closed"))
    margin_registered = summary["min_surplus_to_99pct"] is not None
    no_direct_internal_closure = True
    reduced = active and guard and stieltjes_closed and margin_registered and no_direct_internal_closure
    return [
        row(
            "AlternatingBoundaryGateActive",
            active,
            False,
            "最新唯一内部 beta-sieve 点是 B=3 交错边界余项的一百分点控制。",
            BOUNDARY_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条中的筛主系数，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ExactStieltjesLedgerAvailable",
            stieltjes_closed,
            True,
            "prime-word 离散和已精确表示为 Stieltjes 积分；误差只来自阶梯测度到连续密度的替换。",
            "无表示层剩余。",
        ),
        row(
            "LargeFiniteMarginRegistered",
            margin_registered,
            False,
            "checkpoint 最小余量约 0.5628，高于 1% 目标许多；但有限余量不是全尾段证明。",
            "需要统一尾段误差界。",
        ),
        row(
            "DirectInternalClosureBlocked",
            no_direct_internal_closure,
            True,
            "当前仓库尚无显式 prime-harmonic 包络和 B=3 边界变差合成定理，不能把标准基本引理冒充自足证明。",
            f"{MERTENS_ATOM} AND {VARIATION_ATOM}",
        ),
        row(
            "BoundaryAtomSplitToMertensAndVariation",
            reduced,
            False,
            "交错边界余项被压成两个真正原子：一维素数倒数 Mertens 包络与 B=3 区域边界变差传递。",
            f"{MERTENS_ATOM} AND {VARIATION_ATOM}",
        ),
        row(
            MERTENS_ATOM,
            False,
            False,
            "需要显式证明 P>=100000、0<u<=0.43 下 H_P(u)=sum_{p<P^u}1/p 与 log u+C_P 的统一误差包络。",
            MERTENS_ATOM,
        ),
        row(
            VARIATION_ATOM,
            False,
            False,
            "需要证明该一维误差经过 B=3 admissible 多面体和交错截断后，总损失小于 1% f(s) 或被 checkpoint 正余量吸收。",
            VARIATION_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "标准 Rosser-Iwaniec beta-sieve 基本引理可外部关闭这两个原子；但不是内部自足闭合。",
            STANDARD_IMPORT_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部短区间 rough-number 下界仍可绕开整个内部 beta-sieve 包。",
            EXTERNAL_ROUGH_ATOM,
        ),
        row(
            EXTERNAL_DIBFI_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_DIBFI_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 B=3 交错边界余项终端路由。"""
    previous = load_json(paths["previous"])
    audit = load_json(paths["audit"])
    summary = audit_summary(audit)
    rows = build_rows(previous, summary)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "BoundaryAtomSplitToMertensAndVariation"
    )
    latest_self = replace_boundary_atom(previous.get("latest_self_contained_basis", ""))
    latest_cond = replace_boundary_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_boundary_atom(previous.get("latest_global_with_external_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_alternating_boundary_terminal_router",
        "status": "boundary_remainder_split_to_mertens_and_variation_inputs_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "alternating_boundary_remainder_atom_reduced": reduced,
        "alternating_boundary_remainder_one_percent_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {BOUNDARY_ATOM: replacement_pair()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": MERTENS_ATOM,
        "secondary_priority": VARIATION_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "audit_summary": summary,
        "standard_external_closure_statement": (
            "If the standard Rosser-Iwaniec beta-sieve fundamental lemma is accepted as an "
            "external theorem, the B=3 alternating boundary remainder closes externally. "
            "The current self-contained chain does not yet include that proof."
        ),
        "plain_conclusion": (
            "B=3 交错边界余项是当前内部 beta-sieve 线的真实终端。它不能靠有限 checkpoint "
            "直接闭合，也不能把标准基本引理改名为自足证明。本步把它拆成两个最小可攻输入："
            "显式 prime-harmonic/Mertens 统一包络，以及 B=3 admissible 区域的边界变差传递账本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    summary = result["audit_summary"]
    lines = [
        "# Prime Matrix B=3 交错边界余项终端路由器",
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
            "alternating_boundary_remainder_atom_reduced="
            f"{fmt_bool(result['alternating_boundary_remainder_atom_reduced'])}"
        ),
        (
            "alternating_boundary_remainder_one_percent_proved="
            f"{fmt_bool(result['alternating_boundary_remainder_one_percent_proved'])}"
        ),
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. checkpoint 余量",
        "",
        "```text",
        f"checkpoint_count={summary['checkpoint_count']}",
        f"min_checkpoint_P={summary['min_checkpoint_P']}",
        f"min_checkpoint_ratio={summary['min_checkpoint_ratio']}",
        f"min_surplus_to_99pct={summary['min_surplus_to_99pct']}",
        "```",
        "",
        "## 2. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        result["standard_external_closure_statement"],
        "",
        "## 3. 判定表",
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            f"先攻 `{result['next_priority']}`，再攻 `{result['secondary_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "audit": args.audit,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
