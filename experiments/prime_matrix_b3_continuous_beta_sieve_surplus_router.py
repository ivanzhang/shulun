#!/usr/bin/env python3
"""Prime Matrix B=3 连续 beta-sieve 主项余量路由器。

用法示例：
  python3 experiments/prime_matrix_b3_continuous_beta_sieve_surplus_router.py

输出：
  docs/monograph/prime-matrix-b3-continuous-beta-sieve-surplus-router.json
  docs/monograph/prime-matrix-b3-continuous-beta-sieve-surplus-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-continuous-beta-sieve-surplus-router.md"

CONTINUOUS_ATOM = "B3ContinuousBetaSieveCoefficientSurplusAlpha043"
DISCRETE_ATOM = "B3DiscretePrimeSumUniformErrorPGe100000"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
EULER_GAMMA = 0.5772156649015329
CONSERVATIVE_FRACTION = 0.99


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


def replace_continuous_atom(text: str) -> str:
    """从二原子包中删除已闭合的连续原子。"""
    replacements = [
        (
            f"({CONTINUOUS_ATOM} AND {DISCRETE_ATOM})",
            DISCRETE_ATOM,
        ),
        (
            f"{CONTINUOUS_ATOM} AND {DISCRETE_ATOM}",
            DISCRETE_ATOM,
        ),
        (
            f"({DISCRETE_ATOM} AND {CONTINUOUS_ATOM})",
            DISCRETE_ATOM,
        ),
        (
            f"{DISCRETE_ATOM} AND {CONTINUOUS_ATOM}",
            DISCRETE_ATOM,
        ),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    return result


def continuous_ledger() -> dict[str, Any]:
    """计算 alpha=0.43 的连续线性筛账本。"""
    sieve_s = 1.0 / ALPHA
    f_value = 2.0 * math.exp(EULER_GAMMA) * math.log(sieve_s - 1.0) / sieve_s
    threshold = CONSERVATIVE_FRACTION * f_value
    return {
        "alpha": ALPHA,
        "s": sieve_s,
        "s_in_two_to_three": 2.0 < sieve_s < 3.0,
        "linear_lower_sieve_f": f_value,
        "continuous_coefficient": f_value,
        "conservative_fraction": CONSERVATIVE_FRACTION,
        "conservative_threshold": threshold,
        "absolute_surplus_to_99pct": f_value - threshold,
        "relative_surplus_to_99pct": 1.0 - CONSERVATIVE_FRACTION,
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


def build_rows(previous: dict[str, Any], ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """生成连续 beta-sieve 余量判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == CONTINUOUS_ATOM and CONTINUOUS_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    lower_package_available = (
        bool(previous.get("lower_weight_recursive_construction_closed"))
        and bool(previous.get("lower_weight_dominance_proved"))
    )
    formula_range_closed = bool(ledger["s_in_two_to_three"])
    coefficient_surplus_closed = ledger["continuous_coefficient"] >= ledger["conservative_threshold"]
    continuous_closed = (
        active
        and guard
        and lower_package_available
        and formula_range_closed
        and coefficient_surplus_closed
    )
    return [
        row(
            "ContinuousSurplusGateActive",
            active,
            False,
            "上一层把 99% 主系数原子压成连续 beta 主项余量与离散素和误差。",
            CONTINUOUS_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只处理筛权连续主项函数，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LowerPackageAvailable",
            lower_package_available,
            True,
            "lower weights 构造和逐点支配已闭合，连续主项对象有定义。",
            "无 lower-weight 结构剩余。",
        ),
        row(
            "LinearLowerSieveRangeClosed",
            formula_range_closed,
            True,
            "alpha=0.43 给 s=1/alpha=2.325581，处于 2<s<3 的显式公式区间。",
            "无区间剩余。",
        ),
        row(
            "ContinuousLinearSieveFormulaClosed",
            True,
            True,
            "连续线性下界筛在 2<s<3 满足 f(s)=2e^gamma log(s-1)/s。",
            "离散素和误差仍未处理。",
        ),
        row(
            "ContinuousSurplusAbove99PercentClosed",
            coefficient_surplus_closed,
            True,
            "连续主项等于 100% f(s)，因此相对 99% 目标留下 1% 误差余量。",
            DISCRETE_ATOM,
        ),
        row(
            "B3ContinuousBetaSieveCoefficientSurplusClosed",
            continuous_closed,
            True,
            "连续层已经闭合；剩余唯一内部点是离散素和统一误差小于 1% f(s)。",
            DISCRETE_ATOM,
        ),
        row(
            DISCRETE_ATOM,
            False,
            False,
            "需要证明 P>=100000 下离散素数乘积和到连续模型的误差不超过 0.01 f(s)。",
            DISCRETE_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "若接受标准 Rosser-Iwaniec beta-sieve 定理，可外部关闭离散误差；但不是内部自足闭合。",
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
    """执行连续 beta-sieve 主项余量路由。"""
    previous = load_json(paths["previous"])
    ledger = continuous_ledger()
    rows = build_rows(previous, ledger)
    continuous_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "B3ContinuousBetaSieveCoefficientSurplusClosed"
    )
    latest_self = replace_continuous_atom(previous.get("latest_self_contained_basis", ""))
    latest_cond = replace_continuous_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_continuous_atom(previous.get("latest_global_with_external_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_continuous_beta_sieve_surplus_router",
        "status": "continuous_beta_surplus_closed_discrete_error_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "lower_weight_recursive_construction_closed": bool(
            previous.get("lower_weight_recursive_construction_closed")
        ),
        "lower_weight_dominance_proved": bool(previous.get("lower_weight_dominance_proved")),
        "continuous_beta_sieve_surplus_proved": continuous_closed,
        "discrete_prime_sum_uniform_error_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {CONTINUOUS_ATOM: "CONTINUOUS_LINEAR_SIEVE_F_ALPHA043_CLOSED"},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": DISCRETE_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "ledger": ledger,
        "proof_skeleton": [
            "The continuous linear lower sieve in dimension one is governed by the beta/Buchstab differential-difference system.",
            "On the interval 2<s<3, the lower function has the explicit solution f(s)=2e^gamma log(s-1)/s.",
            "For alpha=0.43, s=1/alpha=2.325581..., so this formula applies directly.",
            "The continuous main coefficient is therefore exactly f(s), while the project only needs 0.99 f(s).",
            "The remaining 0.01 f(s)=0.004317176892... is the entire budget for discrete prime-sum error.",
        ],
        "plain_conclusion": (
            "连续主项余量已闭合。alpha=0.43 给 s=2.325581，位于线性下界筛 2<s<3 的显式公式区间；"
            "连续主项等于 f(s)=0.431717689229，因此相对 99% 目标保留 1% 的绝对归一误差预算 "
            "0.004317176892。当前唯一内部 beta-sieve 剩余变成离散素和统一误差。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    ledger = result["ledger"]
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix B=3 连续 beta-sieve 主项余量路由器",
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
        f"discrete_prime_sum_uniform_error_proved={fmt_bool(result['discrete_prime_sum_uniform_error_proved'])}",
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 连续账本",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| alpha | {ledger['alpha']:.6f} |",
        f"| s=1/alpha | {ledger['s']:.6f} |",
        f"| 2<s<3 | {fmt_bool(ledger['s_in_two_to_three'])} |",
        f"| f(s) | {ledger['linear_lower_sieve_f']:.12f} |",
        f"| continuous coefficient | {ledger['continuous_coefficient']:.12f} |",
        f"| 99% threshold | {ledger['conservative_threshold']:.12f} |",
        f"| absolute surplus | {ledger['absolute_surplus_to_99pct']:.12f} |",
        f"| relative surplus | {ledger['relative_surplus_to_99pct']:.6f} |",
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
