#!/usr/bin/env python3
"""Prime Matrix B=3 prime-word Stieltjes 积分账本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_prime_word_stieltjes_integral_router.py

输出：
  docs/monograph/prime-matrix-b3-prime-word-stieltjes-integral-router.json
  docs/monograph/prime-matrix-b3-prime-word-stieltjes-integral-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-discrete-prime-sum-error-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-prime-word-stieltjes-integral-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-prime-word-stieltjes-integral-router.md"

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


def replace_stieltjes_atom(text: str) -> str:
    """从二原子包中删除已闭合的 Stieltjes 表示原子。"""
    replacements = [
        (
            f"({STIELTJES_ATOM} AND {BOUNDARY_ATOM})",
            BOUNDARY_ATOM,
        ),
        (
            f"{STIELTJES_ATOM} AND {BOUNDARY_ATOM}",
            BOUNDARY_ATOM,
        ),
        (
            f"({BOUNDARY_ATOM} AND {STIELTJES_ATOM})",
            BOUNDARY_ATOM,
        ),
        (
            f"{BOUNDARY_ATOM} AND {STIELTJES_ATOM}",
            BOUNDARY_ATOM,
        ),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    return result


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Stieltjes 积分账本判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == STIELTJES_ATOM and STIELTJES_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    discrete_boundary_reduced = bool(previous.get("discrete_prime_sum_uniform_error_reduced"))
    measure_pinned = True
    region_pinned = True
    exact_identity = True
    stieltjes_closed = (
        active
        and guard
        and discrete_boundary_reduced
        and measure_pinned
        and region_pinned
        and exact_identity
    )
    return [
        row(
            "StieltjesLedgerGateActive",
            active,
            False,
            "上一层把离散素和误差压成 prime-word Stieltjes 表示和交错边界余项。",
            STIELTJES_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只做精确表示，不使用真实零行缺席或有限样本外推。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "DiscreteErrorBoundaryReductionAvailable",
            discrete_boundary_reduced,
            True,
            "离散误差已经被拆成 Stieltjes 表示账本和边界余项账本。",
            "无拆分层剩余。",
        ),
        row(
            "PrimeReciprocalStepMeasurePinned",
            measure_pinned,
            True,
            "定义 H_P(t)=sum_{p<exp(t log P), p<P^0.43}1/p；其 Stieltjes 原子质量正好是 1/p。",
            "无测度自由度。",
        ),
        row(
            "B3AdmissibleWordRegionPinned",
            region_pinned,
            True,
            "B=3 admissible 条件在降序 log 坐标中是有限个线性半空间：sum_{i<2m}u_i+3u_{2m}<1。",
            "无区域自由度。",
        ),
        row(
            "FinitePrimeWordSumEqualsIteratedStieltjesIntegral",
            exact_identity,
            True,
            "对每个 word length r，离散 prime-word 倒数和精确等于该区域上 dH_P 的 r 重 Stieltjes 积分。",
            "无误差项。",
        ),
        row(
            "B3PrimeWordStieltjesIntegralLedgerClosed",
            stieltjes_closed,
            True,
            "Stieltjes 账本只是精确重写，已经闭合；全部误差集中到交错边界余项。",
            BOUNDARY_ATOM,
        ),
        row(
            BOUNDARY_ATOM,
            False,
            False,
            "仍需证明将阶梯测度 dH_P 替换为连续密度时，交错截断边界/跳变余项小于 1% f(s) 或整体正向。",
            BOUNDARY_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "标准 Rosser-Iwaniec beta-sieve 基本引理可外部关闭边界余项；但不是内部自足闭合。",
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
    """执行 B=3 prime-word Stieltjes 积分账本路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    stieltjes_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "B3PrimeWordStieltjesIntegralLedgerClosed"
    )
    latest_self = replace_stieltjes_atom(previous.get("latest_self_contained_basis", ""))
    latest_cond = replace_stieltjes_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_stieltjes_atom(previous.get("latest_global_with_external_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_prime_word_stieltjes_integral_router",
        "status": "prime_word_stieltjes_exact_ledger_closed_boundary_remainder_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "prime_word_stieltjes_integral_ledger_closed": stieltjes_closed,
        "alternating_boundary_remainder_one_percent_proved": False,
        "discrete_prime_sum_uniform_error_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {STIELTJES_ATOM: "EXACT_PRIME_WORD_STIELTJES_REPRESENTATION_CLOSED"},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": BOUNDARY_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "stieltjes_formula": (
            "For each r, sum_{p1>...>pr, B3-admissible} (-1)^r/(p1...pr) "
            "= (-1)^r int_{Omega_r(B=3)} dH_P(u1)...dH_P(ur), "
            "with H_P(u)=sum_{p<P^u, p<P^0.43} 1/p."
        ),
        "region_formula": (
            "Omega_r(B=3): 0<u_r<...<u_1<0.43 and "
            "u1+...+u_{2m-1}+3u_{2m}<1 for every 1<=2m<=r."
        ),
        "proof_skeleton": [
            "H_P is a finite right-continuous step function with jump 1/p at u=log p/log P.",
            "A one-dimensional Stieltjes integral against dH_P is exactly summation over prime atoms.",
            "Iterating the integral over the ordered region enforces p1>...>pr without multiplicity.",
            "The B=3 Rosser word gates are exactly the listed linear inequalities in log coordinates.",
            "Thus the Stieltjes expression is an exact rewriting of the finite prime-word sum, with no analytic error.",
            "All analytic loss is therefore isolated in the next atom: replacing dH_P by its continuous model across alternating moving boundaries.",
        ],
        "plain_conclusion": (
            "Stieltjes 账本已经闭合：prime-word 离散倒数和与迭代 Stieltjes 积分是同一个对象的两种写法。"
            "本步没有使用外部定理，也没有用有限 checkpoint 外推。剩余唯一内部 beta-sieve 点变成 "
            "B3AlternatingBoundaryRemainderOnePercentLedger，即阶梯测度到连续密度的交错边界余项控制。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix B=3 prime-word Stieltjes 积分账本路由器",
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
            "prime_word_stieltjes_integral_ledger_closed="
            f"{fmt_bool(result['prime_word_stieltjes_integral_ledger_closed'])}"
        ),
        (
            "alternating_boundary_remainder_one_percent_proved="
            f"{fmt_bool(result['alternating_boundary_remainder_one_percent_proved'])}"
        ),
        f"discrete_prime_sum_uniform_error_proved={fmt_bool(result['discrete_prime_sum_uniform_error_proved'])}",
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确公式",
        "",
        "```text",
        result["stieltjes_formula"],
        "",
        result["region_formula"],
        "```",
        "",
        "## 2. 证明骨架",
        "",
        *[f"- {item}" for item in result["proof_skeleton"]],
        "",
        "## 3. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 4. 判定表",
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
            "## 5. 最新输入基",
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
            "## 6. 下一步",
            "",
            f"直接攻 `{result['next_priority']}`。",
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
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
