#!/usr/bin/env python3
"""Prime Matrix beta-sieve 99% 主系数终端攻击路由器。

用法示例：
  python3 experiments/prime_matrix_beta_sieve_main_coefficient_terminal_attack_router.py

输出：
  docs/monograph/prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json
  docs/monograph/prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-beta-sieve-lower-bound-dominance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.md"

MAIN_99_ATOM = "BetaSieveMainCoefficientExplicit99PercentPGe100000"
CONTINUOUS_ATOM = "B3ContinuousBetaSieveCoefficientSurplusAlpha043"
DISCRETE_ATOM = "B3DiscretePrimeSumUniformErrorPGe100000"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
WORD_EXPONENT = 3
EULER_GAMMA = 0.5772156649015329
CONSERVATIVE_FRACTION = 0.99
CHECKPOINTS = [100_000, 200_000, 500_000, 1_000_000, 2_000_000, 5_000_000, 10_000_000]


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


def replace_main_atom(text: str, replacement: str) -> str:
    """替换 99% 主系数原子。"""
    return text.replace(MAIN_99_ATOM, replacement)


def linear_sieve_f(alpha: float = ALPHA) -> float:
    """一维线性下界筛 f(1/alpha)。"""
    sieve_s = 1.0 / alpha
    return 2.0 * math.exp(EULER_GAMMA) * math.log(sieve_s - 1.0) / sieve_s


def prime_list_below(limit: float) -> list[int]:
    """列出小于 limit 的素数。"""
    upper = max(2, math.ceil(limit))
    primes: list[int] = []
    for candidate in range(2, upper):
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return primes


def lower_word_admissible(factors_desc: list[int], level: int) -> bool:
    """判定 B=3 降序 word 是否 lower admissible。"""
    if not factors_desc:
        return True
    product = math.prod(factors_desc)
    if product >= level:
        return False
    for pair_index in range(1, len(factors_desc) // 2 + 1):
        head_product = math.prod(factors_desc[: 2 * pair_index - 1])
        even_prime = factors_desc[2 * pair_index - 1]
        if head_product * (even_prime**WORD_EXPONENT) >= level:
            return False
    return True


def coefficient_audit(level: int) -> dict[str, Any]:
    """精确计算一个 checkpoint 的 B=3 主系数比值。"""
    z = level**ALPHA
    primes = prime_list_below(z)
    v_exact = 1.0
    for prime in primes:
        v_exact *= 1.0 - 1.0 / prime

    accepted_count = 0
    signed_weight_sum = 0.0
    max_supported_d = 1

    def dfs(start: int, product: int, factors: list[int]) -> None:
        nonlocal accepted_count
        nonlocal signed_weight_sum
        nonlocal max_supported_d
        factors_desc = sorted(factors, reverse=True)
        if lower_word_admissible(factors_desc, level):
            sign = -1 if len(factors_desc) % 2 else 1
            accepted_count += 1
            signed_weight_sum += sign / product
            max_supported_d = max(max_supported_d, product)
        for index in range(start, len(primes)):
            new_product = product * primes[index]
            if new_product >= level:
                continue
            dfs(index + 1, new_product, factors + [primes[index]])

    dfs(0, 1, [])
    f_value = linear_sieve_f()
    target = v_exact * f_value
    ratio = signed_weight_sum / target
    return {
        "P": level,
        "z": z,
        "prime_count_below_z": len(primes),
        "largest_prime_below_z": primes[-1] if primes else None,
        "accepted_weight_count": accepted_count,
        "max_supported_d": max_supported_d,
        "W_minus": signed_weight_sum,
        "V_exact": v_exact,
        "linear_sieve_f": f_value,
        "V_exact_times_f": target,
        "ratio_W_over_Vf": ratio,
        "ratio_minus_0_99": ratio - CONSERVATIVE_FRACTION,
        "passes_99pct": ratio >= CONSERVATIVE_FRACTION,
    }


def audit_checkpoints() -> dict[str, Any]:
    """生成 checkpoint 主系数审计。"""
    rows = [coefficient_audit(level) for level in CHECKPOINTS]
    min_row = min(rows, key=lambda item: item["ratio_W_over_Vf"])
    return {
        "word_exponent": WORD_EXPONENT,
        "alpha": ALPHA,
        "conservative_fraction": CONSERVATIVE_FRACTION,
        "checkpoint_rows": rows,
        "min_checkpoint_ratio": min_row["ratio_W_over_Vf"],
        "min_checkpoint_P": min_row["P"],
        "all_checkpoints_pass_99pct": all(item["passes_99pct"] for item in rows),
        "sample_only_not_tail_proof": True,
    }


def self_contained_replacement() -> str:
    """写出自足替换包。"""
    return f"({CONTINUOUS_ATOM} AND {DISCRETE_ATOM})"


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


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 99% 主系数终端攻击判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == MAIN_99_ATOM and MAIN_99_ATOM in basis
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
    exact_functional_pinned = True
    checkpoint_pass = bool(audit["all_checkpoints_pass_99pct"])
    promoted_to_tail = False
    reduced = active and guard and lower_package_available and exact_functional_pinned and checkpoint_pass
    return [
        row(
            "MainCoefficientGateActive",
            active,
            False,
            "最新内部唯一点是 B=3 lower word rule 的 99% 主系数尾段证明。",
            MAIN_99_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内处理筛主项，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LowerPackageAvailable",
            lower_package_available,
            True,
            "递归构造和逐点 lower-bound 支配已经闭合，主系数对象现在良定义。",
            "无 lower-weight 结构剩余。",
        ),
        row(
            "ExactCoefficientFunctionalPinned",
            exact_functional_pinned,
            True,
            "主系数精确定义为 W^-(P)=sum lambda_d^-/d，并以精确 V(z)f(1/0.43) 归一。",
            "无归一化自由度。",
        ),
        row(
            "FiniteCheckpointAuditStrongPositive",
            checkpoint_pass,
            False,
            "P=1e5 到 1e7 的 checkpoint 精确审计全部大幅超过 99%，最小比值仍超过 1.55。",
            "样本不是全尾段证明。",
        ),
        row(
            "SampleToTailPromotionBlocked",
            not promoted_to_tail,
            True,
            "有限 checkpoint 不能推出 P>=100000 全部整数尾段；还需连续主项和离散误差的统一控制。",
            f"{CONTINUOUS_ATOM} AND {DISCRETE_ATOM}",
        ),
        row(
            "MainCoefficientAtomReducedToTwoMicroInputs",
            reduced,
            False,
            "99% 主系数原子被压成两个最小自足输入：连续 beta 主项余量与离散素和误差账本。",
            f"{CONTINUOUS_ATOM} AND {DISCRETE_ATOM}",
        ),
        row(
            CONTINUOUS_ATOM,
            False,
            False,
            "需要证明 B=3 word rule 在 s=1/0.43 的连续 Buchstab/beta 主系数至少达到 0.99 f(s)，最好给出显式正余量。",
            CONTINUOUS_ATOM,
        ),
        row(
            DISCRETE_ATOM,
            False,
            False,
            "需要证明 P>=100000 下离散素数乘积和到连续积分模型的误差小于连续余量。",
            DISCRETE_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "若接受标准 Rosser-Iwaniec beta-sieve 定理，可外部关闭主系数；但这不是内部自足闭合。",
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
    """执行 beta-sieve 99% 主系数终端攻击路由。"""
    previous = load_json(paths["previous"])
    audit = audit_checkpoints()
    rows = build_rows(previous, audit)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "MainCoefficientAtomReducedToTwoMicroInputs"
    )
    latest_self = replace_main_atom(previous.get("latest_self_contained_basis", ""), self_contained_replacement())
    latest_cond = replace_main_atom(previous.get("latest_conditional_basis", ""), self_contained_replacement())
    latest_global = replace_main_atom(previous.get("latest_global_with_external_basis", ""), self_contained_replacement())
    source_paths = list(paths.values())
    return {
        "certificate_type": "beta_sieve_main_coefficient_terminal_attack_router",
        "status": "main_coefficient_reduced_to_continuous_and_discrete_error_inputs_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "lower_weight_recursive_construction_closed": bool(
            previous.get("lower_weight_recursive_construction_closed")
        ),
        "lower_weight_dominance_proved": bool(previous.get("lower_weight_dominance_proved")),
        "beta_sieve_main_coefficient_atom_reduced": reduced,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {MAIN_99_ATOM: self_contained_replacement()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": CONTINUOUS_ATOM,
        "secondary_priority": DISCRETE_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "audit": audit,
        "proof_obstruction": (
            "checkpoint exact computation gives strong positive evidence, but a finite set of "
            "P-values cannot imply the uniform all-P>=100000 inequality. The missing self-contained "
            "tail proof is exactly continuous beta coefficient surplus plus explicit discrete prime-sum error."
        ),
        "plain_conclusion": (
            "本步直接攻击 99% 主系数终端。具体 B=3 word rule 的精确 checkpoint 审计非常强："
            "P=100000 处 W^-/Vf≈1.694，审计到 10^7 的最小比值仍约 1.553。"
            "但这仍不能作为 P>=100000 全尾段证明。诚实的最窄闭合条件已经压成两个微输入："
            "连续 beta 主项余量，以及离散素和到连续模型的统一误差账本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    audit = result["audit"]
    lines = [
        "# Prime Matrix beta-sieve 99% 主系数终端攻击路由器",
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
            "lower_weight_recursive_construction_closed="
            f"{fmt_bool(result['lower_weight_recursive_construction_closed'])}"
        ),
        f"lower_weight_dominance_proved={fmt_bool(result['lower_weight_dominance_proved'])}",
        f"beta_sieve_main_coefficient_atom_reduced={fmt_bool(result['beta_sieve_main_coefficient_atom_reduced'])}",
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"standard_beta_sieve_import_accepted={fmt_bool(result['standard_beta_sieve_import_accepted'])}",
        (
            "external_short_interval_rough_lower_bound_accepted="
            f"{fmt_bool(result['external_short_interval_rough_lower_bound_accepted'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确 checkpoint 审计",
        "",
        "这些数值只证明有限点通过，不替代全尾段证明。",
        "",
        "| P | pi(z) | W^- | V(z)f(s) | ratio | ratio-0.99 |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in audit["checkpoint_rows"]:
        lines.append(
            "| {P} | {pi_z} | {W:.12f} | {Vf:.12f} | {ratio:.6f} | {surplus:.6f} |".format(
                P=item["P"],
                pi_z=item["prime_count_below_z"],
                W=item["W_minus"],
                Vf=item["V_exact_times_f"],
                ratio=item["ratio_W_over_Vf"],
                surplus=item["ratio_minus_0_99"],
            )
        )
    lines.extend(
        [
            "",
            "## 2. 审计结论",
            "",
            "```text",
            f"all_checkpoints_pass_99pct={fmt_bool(audit['all_checkpoints_pass_99pct'])}",
            f"min_checkpoint_P={audit['min_checkpoint_P']}",
            f"min_checkpoint_ratio={audit['min_checkpoint_ratio']:.12f}",
            f"sample_only_not_tail_proof={fmt_bool(audit['sample_only_not_tail_proof'])}",
            "```",
            "",
            result["proof_obstruction"],
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
            f"先攻 `{result['next_priority']}`，再攻 `{result['secondary_priority']}`。",
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
