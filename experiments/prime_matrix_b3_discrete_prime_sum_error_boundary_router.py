#!/usr/bin/env python3
"""Prime Matrix B=3 离散素和误差边界路由器。

用法示例：
  python3 experiments/prime_matrix_b3_discrete_prime_sum_error_boundary_router.py

输出：
  docs/monograph/prime-matrix-b3-discrete-prime-sum-error-boundary-router.json
  docs/monograph/prime-matrix-b3-discrete-prime-sum-error-boundary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json"
DEFAULT_AUDIT = DOCS / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-discrete-prime-sum-error-boundary-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-discrete-prime-sum-error-boundary-router.md"

DISCRETE_ATOM = "B3DiscretePrimeSumUniformErrorPGe100000"
STIELTJES_ATOM = "B3PrimeWordStieltjesIntegralUniformLedgerPGe100000"
BOUNDARY_ATOM = "B3AlternatingBoundaryRemainderOnePercentLedger"
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


def replace_discrete_atom(text: str, replacement: str) -> str:
    """替换离散素和误差原子。"""
    return text.replace(DISCRETE_ATOM, replacement)


def self_contained_replacement() -> str:
    """写出自足替换包。"""
    return f"({STIELTJES_ATOM} AND {BOUNDARY_ATOM})"


def audit_summary(audit: dict[str, Any]) -> dict[str, Any]:
    """提取 checkpoint 审计摘要。"""
    rows = audit.get("audit", {}).get("checkpoint_rows", [])
    if not rows:
        return {
            "checkpoint_count": 0,
            "min_checkpoint_ratio": None,
            "min_checkpoint_P": None,
            "all_checkpoints_pass_99pct": False,
            "min_surplus_to_99pct": None,
        }
    min_row = min(rows, key=lambda item: item["ratio_W_over_Vf"])
    return {
        "checkpoint_count": len(rows),
        "min_checkpoint_ratio": min_row["ratio_W_over_Vf"],
        "min_checkpoint_P": min_row["P"],
        "all_checkpoints_pass_99pct": all(item["passes_99pct"] for item in rows),
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
    """生成离散素和误差边界判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == DISCRETE_ATOM and DISCRETE_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    continuous_available = bool(previous.get("continuous_beta_sieve_surplus_proved"))
    checkpoint_pass = bool(summary["all_checkpoints_pass_99pct"])
    finite_not_tail = True
    reduced = active and guard and continuous_available and checkpoint_pass and finite_not_tail
    return [
        row(
            "DiscreteErrorGateActive",
            active,
            False,
            "上一层已经把 beta-sieve 内部点压到离散素和统一误差。",
            DISCRETE_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内处理筛权主系数误差，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ContinuousSurplusAvailable",
            continuous_available,
            True,
            "连续层给出 1% f(s) 的误差预算。",
            "离散统一误差必须小于该预算，或利用更强的正向离散余量。",
        ),
        row(
            "CheckpointAuditHasLargePositiveMargin",
            checkpoint_pass,
            False,
            "有限 checkpoint 全部通过，最小 W^-/Vf 约 1.553，远高于 0.99。",
            "有限审计不能推出全尾段。",
        ),
        row(
            "FiniteCheckpointCannotCloseUniformTail",
            finite_not_tail,
            True,
            "P>=100000 有无限多个素数阈值跳变；有限样本不能替代统一 Stieltjes/边界余项证明。",
            f"{STIELTJES_ATOM} AND {BOUNDARY_ATOM}",
        ),
        row(
            "DiscreteErrorReducedToTwoSelfContainedInputs",
            reduced,
            False,
            "离散误差已压成两个不可混淆的最小义务：素和到积分的统一账本，以及交错边界余项的一百分点预算。",
            f"{STIELTJES_ATOM} AND {BOUNDARY_ATOM}",
        ),
        row(
            STIELTJES_ATOM,
            False,
            False,
            "需要对所有 B=3 admissible prime words 建立从素数倒数迭代和到连续 Stieltjes 积分的统一显式下界。",
            STIELTJES_ATOM,
        ),
        row(
            BOUNDARY_ATOM,
            False,
            False,
            "需要控制交错截断边界、跳变端点和符号余项，总损失小于 0.01 f(s)，或证明其实际正向。",
            BOUNDARY_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "标准 Rosser-Iwaniec beta-sieve 基本引理可外部关闭这两个输入，但这不是内部自足闭合。",
            STANDARD_IMPORT_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。",
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
    """执行离散素和误差边界路由。"""
    previous = load_json(paths["previous"])
    audit = load_json(paths["audit"])
    summary = audit_summary(audit)
    rows = build_rows(previous, summary)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "DiscreteErrorReducedToTwoSelfContainedInputs"
    )
    latest_self = replace_discrete_atom(previous.get("latest_self_contained_basis", ""), self_contained_replacement())
    latest_cond = replace_discrete_atom(previous.get("latest_conditional_basis", ""), self_contained_replacement())
    latest_global = replace_discrete_atom(previous.get("latest_global_with_external_basis", ""), self_contained_replacement())
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_discrete_prime_sum_error_boundary_router",
        "status": "discrete_error_reduced_to_stieltjes_and_boundary_remainder_inputs_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "continuous_beta_sieve_surplus_proved": bool(previous.get("continuous_beta_sieve_surplus_proved")),
        "discrete_prime_sum_uniform_error_reduced": reduced,
        "discrete_prime_sum_uniform_error_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {DISCRETE_ATOM: self_contained_replacement()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": STIELTJES_ATOM,
        "secondary_priority": BOUNDARY_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "audit_summary": summary,
        "standard_external_closure_statement": (
            "Accepting the standard Rosser-Iwaniec beta-sieve fundamental lemma closes "
            "the discrete Stieltjes and boundary remainder package externally, but it is "
            "not a self-contained internal closure."
        ),
        "plain_conclusion": (
            "最后内部离散误差不能由有限 checkpoint 直接闭合。现有精确审计余量很大，"
            "但要覆盖所有 P>=100000，必须证明两个明确输入：所有 B=3 admissible words 的素数倒数迭代和 "
            "到连续 Stieltjes 积分的统一下界，以及交错边界/跳变余项的一百分点预算。"
            "这就是标准 beta-sieve 基本引理的内部化核心。"
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
        "# Prime Matrix B=3 离散素和误差边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"continuous_beta_sieve_surplus_proved={fmt_bool(result['continuous_beta_sieve_surplus_proved'])}",
        f"discrete_prime_sum_uniform_error_reduced={fmt_bool(result['discrete_prime_sum_uniform_error_reduced'])}",
        f"discrete_prime_sum_uniform_error_proved={fmt_bool(result['discrete_prime_sum_uniform_error_proved'])}",
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. checkpoint 余量摘要",
        "",
        "```text",
        f"checkpoint_count={summary['checkpoint_count']}",
        f"all_checkpoints_pass_99pct={fmt_bool(summary['all_checkpoints_pass_99pct'])}",
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
