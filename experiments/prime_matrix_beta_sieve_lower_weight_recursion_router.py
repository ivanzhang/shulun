#!/usr/bin/env python3
"""Prime Matrix beta-sieve lower weight 递归构造路由器。

用法示例：
  python3 experiments/prime_matrix_beta_sieve_lower_weight_recursion_router.py

输出：
  docs/monograph/prime-matrix-beta-sieve-lower-weight-recursion-router.json
  docs/monograph/prime-matrix-beta-sieve-lower-weight-recursion-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-beta-sieve-self-contained-frontier-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-beta-sieve-lower-weight-recursion-router.json"
DEFAULT_MD = DOCS / "prime-matrix-beta-sieve-lower-weight-recursion-router.md"

CONSTRUCTION_ATOM = "BetaSieveLowerWeightRecursiveConstructionLedger"
DOMINANCE_ATOM = "BetaSieveLowerBoundDominanceProof"
MAIN_99_ATOM = "BetaSieveMainCoefficientExplicit99PercentPGe100000"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TAIL_START = 100_000
ALPHA = 0.43
AUDIT_WORD_EXPONENT = 3


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


def replace_construction_atom(text: str) -> str:
    """从常见三原子包中删除已闭合的构造原子。"""
    replacements = [
        (
            f"({CONSTRUCTION_ATOM} AND {DOMINANCE_ATOM} AND {MAIN_99_ATOM})",
            f"({DOMINANCE_ATOM} AND {MAIN_99_ATOM})",
        ),
        (
            f"{CONSTRUCTION_ATOM} AND {DOMINANCE_ATOM} AND {MAIN_99_ATOM}",
            f"{DOMINANCE_ATOM} AND {MAIN_99_ATOM}",
        ),
        (
            f"({CONSTRUCTION_ATOM} AND {DOMINANCE_ATOM})",
            DOMINANCE_ATOM,
        ),
        (
            f"{CONSTRUCTION_ATOM} AND {DOMINANCE_ATOM}",
            DOMINANCE_ATOM,
        ),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    return result


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


def lower_word_admissible(factors_desc: list[int], level: int, word_exponent: int) -> bool:
    """判定降序素因子 word 是否满足 lower Rosser 递归门。"""
    if word_exponent < 2:
        raise ValueError("word_exponent must be at least 2")
    if not factors_desc:
        return True
    product = math.prod(factors_desc)
    if product >= level:
        return False
    length = len(factors_desc)
    for pair_index in range(1, length // 2 + 1):
        head_product = math.prod(factors_desc[: 2 * pair_index - 1])
        even_prime = factors_desc[2 * pair_index - 1]
        if head_product * (even_prime**word_exponent) >= level:
            return False
    return True


def audit_tail_instance(
    level: int = TAIL_START,
    alpha: float = ALPHA,
    word_exponent: int = AUDIT_WORD_EXPONENT,
) -> dict[str, Any]:
    """对 P=100000 的有限递归支撑做轻量审计。"""
    z = level**alpha
    primes = prime_list_below(z)
    total_squarefree_under_level = 0
    accepted_count = 0
    positive_count = 0
    negative_count = 0
    max_supported_d = 1
    harmonic_weight_sum = 0.0

    def dfs(start: int, product: int, factors: list[int]) -> None:
        nonlocal total_squarefree_under_level
        nonlocal accepted_count
        nonlocal positive_count
        nonlocal negative_count
        nonlocal max_supported_d
        nonlocal harmonic_weight_sum

        total_squarefree_under_level += 1
        factors_desc = sorted(factors, reverse=True)
        if lower_word_admissible(factors_desc, level, word_exponent):
            sign = -1 if len(factors_desc) % 2 else 1
            accepted_count += 1
            if sign > 0:
                positive_count += 1
            else:
                negative_count += 1
            max_supported_d = max(max_supported_d, product)
            harmonic_weight_sum += sign / product

        for index in range(start, len(primes)):
            new_product = product * primes[index]
            if new_product >= level:
                continue
            dfs(index + 1, new_product, factors + [primes[index]])

    dfs(0, 1, [])
    return {
        "audit_level_P": level,
        "alpha": alpha,
        "z": z,
        "floor_z": math.floor(z),
        "word_exponent_for_audit": word_exponent,
        "small_prime_count": len(primes),
        "largest_small_prime": primes[-1] if primes else None,
        "total_squarefree_under_level": total_squarefree_under_level,
        "accepted_lower_weight_count": accepted_count,
        "positive_weight_count": positive_count,
        "negative_weight_count": negative_count,
        "max_supported_d": max_supported_d,
        "signed_harmonic_weight_sum": harmonic_weight_sum,
        "sample_only_not_main_coefficient_proof": True,
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


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 lower weight 递归构造判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == CONSTRUCTION_ATOM and CONSTRUCTION_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    definition_pinned = True
    finite_recursion = audit["accepted_lower_weight_count"] > 0 and audit["max_supported_d"] < audit["audit_level_P"]
    support_closed = definition_pinned and finite_recursion
    construction_closed = active and guard and support_closed
    return [
        row(
            "LowerWeightConstructionGateActive",
            active,
            False,
            "上一层最新最窄点正是 beta-sieve lower weights 的有限递归构造。",
            CONSTRUCTION_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内固定筛权对象，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "DescendingPrimeWordRulePinned",
            definition_pinned,
            True,
            "对 squarefree d|P(z)，按降序素因子 p1>...>pr 定义 lower admissible word；lambda_d^- 为 mu(d) 或 0。",
            "无定义自由度。",
        ),
        row(
            "FiniteRecursiveGenerationClosed",
            finite_recursion,
            True,
            "每次只追加更小素数，并在偶数位置检查 p1...p_{2m-1} p_{2m}^B<D；小素数集有限，递归终止。",
            "无算法性剩余。",
        ),
        row(
            "SupportSignAndLevelLedgerClosed",
            support_closed,
            True,
            "由定义立即得到 lambda_1^-=1、lambda_d^- in {-1,0,1}、squarefree、小素因子支撑；B>=2 给 d<D<=P。",
            "无支撑层剩余。",
        ),
        row(
            "LowerWeightRecursiveConstructionLedgerClosed",
            construction_closed,
            False,
            "构造原子已经降为显式有限对象，不再是黑箱输入。",
            f"{DOMINANCE_ATOM} AND {MAIN_99_ATOM}",
        ),
        row(
            DOMINANCE_ATOM,
            False,
            False,
            "下一步必须证明这些 lower weights 对筛剩余指示函数给出逐点下界。",
            DOMINANCE_ATOM,
        ),
        row(
            MAIN_99_ATOM,
            False,
            False,
            "随后还要证明该构造的主系数在 P>=100000 尾段达到 99% 归一目标。",
            MAIN_99_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "若允许标准 Rosser-Iwaniec beta-sieve 定理导入，可直接替代支配与主系数两步；但不是自足闭合。",
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
    """执行 beta-sieve lower weight 递归构造路由。"""
    previous = load_json(paths["previous"])
    audit = audit_tail_instance()
    rows = build_rows(previous, audit)
    construction_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "LowerWeightRecursiveConstructionLedgerClosed"
    )
    latest_self = replace_construction_atom(previous.get("latest_self_contained_basis", ""))
    latest_cond = replace_construction_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_construction_atom(previous.get("latest_global_with_external_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "beta_sieve_lower_weight_recursion_router",
        "status": "lower_weight_recursion_constructed_support_closed_dominance_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "lower_weight_recursive_construction_closed": construction_closed,
        "lower_weight_dominance_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {
            CONSTRUCTION_ATOM: "EXPLICIT_LOWER_WORD_RULE_DEFINITION_CLOSED"
        },
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": DOMINANCE_ATOM,
        "secondary_priority": MAIN_99_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "word_rule_definition": {
            "parameters": "D=P, z=P^0.43, fixed integer word exponent B>=2",
            "prime_word": "for squarefree d|P(z), write d=p1...pr with p1>...>pr",
            "lower_admissible": (
                "for every m with 1<=2m<=r, "
                "p1...p_{2m-1} * p_{2m}^B < D"
            ),
            "weight": "lambda_1^-=1; lambda_d^-=mu(d) if lower_admissible, else 0",
            "recursive_generation": (
                "append smaller primes only; after each even-position append, test the new "
                "p1...p_{2m-1}p_{2m}^B<D gate"
            ),
        },
        "support_proof": [
            "lambda_d^- is defined by mu(d) on squarefree words and 0 otherwise, hence lies in {-1,0,1}.",
            "All prime factors are drawn from primes <z by construction.",
            "If r is even, the final even gate gives p1...p_{r-1}p_r^B<D, hence d<D.",
            "If r is odd and r>=3, the previous even gate gives p1...p_{r-2}p_{r-1}^B<D; since p_r<=p_{r-1} and B>=2, d<D.",
            "If r=1, then d=p1<z<D because s=logD/logz=1/0.43>1.",
        ],
        "tail_start_audit": audit,
        "plain_conclusion": (
            "本步把 beta-sieve lower weight 构造原子闭成一个显式有限对象："
            "固定 D=P、z=P^0.43，对 squarefree d 的降序素因子 word 使用偶数位 Rosser 门，"
            "并定义 lambda_d^- 为 mu(d) 或 0。这样 lambda_1、符号、squarefree、小素因子支撑与 d<P "
            "都已经由有限递归和 B>=2 的代数检查闭合。真正剩余前移到逐点 lower-bound 支配证明，"
            "以及该具体权重的 99% 主系数显式误差。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    word_rule = result["word_rule_definition"]
    audit = result["tail_start_audit"]
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix beta-sieve lower weight 递归构造路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"lower_weight_recursive_construction_closed={fmt_bool(result['lower_weight_recursive_construction_closed'])}",
        f"lower_weight_dominance_proved={fmt_bool(result['lower_weight_dominance_proved'])}",
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
        "## 1. 显式 word rule",
        "",
        "```text",
        f"parameters: {word_rule['parameters']}",
        f"prime_word: {word_rule['prime_word']}",
        f"lower_admissible: {word_rule['lower_admissible']}",
        f"weight: {word_rule['weight']}",
        f"recursive_generation: {word_rule['recursive_generation']}",
        "```",
        "",
        "## 2. 支撑证明",
        "",
        *[f"- {item}" for item in result["support_proof"]],
        "",
        "## 3. P=100000 轻量审计",
        "",
        "该审计只验证递归对象有限且支撑正常，不作为 99% 主系数证明。",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| audit P | {audit['audit_level_P']} |",
        f"| z | {audit['z']:.6f} |",
        f"| floor z | {audit['floor_z']} |",
        f"| word exponent for audit | {audit['word_exponent_for_audit']} |",
        f"| small prime count | {audit['small_prime_count']} |",
        f"| largest small prime | {audit['largest_small_prime']} |",
        f"| squarefree candidates under P | {audit['total_squarefree_under_level']} |",
        f"| accepted lower weights | {audit['accepted_lower_weight_count']} |",
        f"| positive weights | {audit['positive_weight_count']} |",
        f"| negative weights | {audit['negative_weight_count']} |",
        f"| max supported d | {audit['max_supported_d']} |",
        f"| signed harmonic weight sum | {audit['signed_harmonic_weight_sum']:.12f} |",
        "",
        "## 4. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 5. 判定表",
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
            "## 6. 最新输入基",
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
            "## 7. 下一步",
            "",
            f"直接攻 `{result['next_priority']}`；随后攻 `{result['secondary_priority']}`。",
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
