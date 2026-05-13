#!/usr/bin/env python3
"""生成 strict prefix valuation 预算或溢出回流路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_prefix_valuation_budget_or_overflow_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json

输出：
  data/prefix-valuation-budget-or-overflow-sample-ledger.json
  docs/monograph/prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json
  docs/monograph/prime-matrix-strict-prefix-valuation-budget-or-overflow-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json"
OUT_MD = DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.md"
OUT_LEDGER = DATA / "prefix-valuation-budget-or-overflow-sample-ledger.json"

HARDPOINT = "PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn"
OVERFLOW_LEDGER = "CarrierLCMValuationOverflowNamedReturnLedger"
DIVIDES_H0 = "ColdPrefixProductDividesCarrierLCMH0Ledger"
PREFIX_QUOTIENT = "PrefixResidualFrequencyEqualsCarrierLCMQuotient"
H0_COMPAT = "H0CarrierQuotientCompatibilityWithColdPrefixes"
OVERFLOW_EXCLUSION = "CarrierLCMValuationOverflowReturnExclusionOrAbsorption"
STEP_ORIGIN = "ColdPrefixStepQuotientOriginMapToCarrierRows"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
UNIFIED_BUDGET = "UnifiedTerminalBudgetStrictInequality"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def gcd(a: int, b: int) -> int:
    """计算最大公因数。"""
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """计算最小公倍数。"""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


def product(values: list[int]) -> int:
    """计算整数列表乘积。"""
    result = 1
    for value in values:
        result *= value
    return result


def factor(n: int) -> dict[int, int]:
    """用确定性试除分解正整数；这里只用于证书样本和规则哈希。"""
    if n <= 0:
        raise ValueError("n must be positive")
    x = n
    result: dict[int, int] = {}
    p = 2
    while p * p <= x:
        while x % p == 0:
            result[p] = result.get(p, 0) + 1
            x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        result[x] = result.get(x, 0) + 1
    return result


def merge_valuations(factors: list[dict[int, int]]) -> dict[int, int]:
    """把多个 valuation 相加。"""
    result: dict[int, int] = {}
    for item in factors:
        for prime, exp in item.items():
            result[prime] = result.get(prime, 0) + exp
    return result


def max_carrier_valuations(carrier_quotients: list[int]) -> dict[int, int]:
    """计算 h0^car=lcm(m_c) 的逐素数最大指数。"""
    result: dict[int, int] = {}
    for quotient in carrier_quotients:
        for prime, exp in factor(quotient).items():
            result[prime] = max(result.get(prime, 0), exp)
    return result


def classify_prefix(carrier_quotients: list[int], prefix_steps: list[int]) -> dict[str, Any]:
    """按 carrier-lcm valuation 预算分类一个 cold prefix。"""
    h0_car = 1
    for quotient in carrier_quotients:
        h0_car = lcm(h0_car, quotient)

    prefix_product = product(prefix_steps)
    carrier_budget = max_carrier_valuations(carrier_quotients)
    step_factor_rows = [factor(step) for step in prefix_steps]
    prefix_usage = merge_valuations(step_factor_rows)

    overflow_rows = []
    for prime, used_exp in sorted(prefix_usage.items()):
        allowed_exp = carrier_budget.get(prime, 0)
        if used_exp > allowed_exp:
            hit_steps = [idx for idx, row in enumerate(step_factor_rows) if row.get(prime, 0) > 0]
            overflow_rows.append(
                {
                    "prime": prime,
                    "used_exp": used_exp,
                    "allowed_exp": allowed_exp,
                    "deficit": used_exp - allowed_exp,
                    "step_indices": hit_steps,
                    "return_payload": "prime_power_cascade_or_common_kernel_overflow",
                }
            )

    budget_pass = len(overflow_rows) == 0
    if budget_pass:
        return_kind = "carrier_lcm_budget_pass"
        named_return_packet = None
    else:
        return_kind = "carrier_lcm_valuation_overflow_return"
        named_return_packet = {
            "return": OVERFLOW_LEDGER,
            "registered_as": [
                "prime_power_cascade",
                "low_multiplier_common_kernel",
                "fixed_history_or_pdec_if_persistent",
                "sae_or_cold_budget_debit_if_nonpersistent",
                "hot_core_if_family_overcharges",
            ],
            "overflow_rows": overflow_rows,
        }

    return {
        "carrier_quotients": carrier_quotients,
        "h0_carrier_lcm": h0_car,
        "prefix_steps": prefix_steps,
        "prefix_product": prefix_product,
        "prefix_usage": {str(k): v for k, v in sorted(prefix_usage.items())},
        "carrier_budget": {str(k): v for k, v in sorted(carrier_budget.items())},
        "budget_pass": budget_pass,
        "return_kind": return_kind,
        "overflow_rows": overflow_rows,
        "named_return_packet": named_return_packet,
        "direct_divisibility_check": h0_car % prefix_product == 0,
    }


def sample_ledger() -> dict[str, Any]:
    """生成 pass-or-return 分类样本账本。"""
    samples = [
        {
            "case": "squarefree_budget_pass",
            "carrier_quotients": [12, 35],
            "prefix_steps": [2, 3],
        },
        {
            "case": "repeated_prime_overflow",
            "carrier_quotients": [2, 3, 5],
            "prefix_steps": [2, 2],
        },
        {
            "case": "prime_power_fits_single_carrier_row",
            "carrier_quotients": [8, 9],
            "prefix_steps": [2, 4],
        },
        {
            "case": "mixed_overflow",
            "carrier_quotients": [6, 10],
            "prefix_steps": [2, 2, 3],
        },
    ]
    rows = []
    for item in samples:
        rows.append({**item, "classification": classify_prefix(item["carrier_quotients"], item["prefix_steps"])})
    return {
        "ledger_type": "prefix_valuation_budget_or_overflow_sample_ledger",
        "rule": "compare sum_step v_p(g) against max_carrier_row v_p(m_c); pass or emit overflow return",
        "rows": rows,
        "all_rows_have_pass_or_named_return": all(
            row["classification"]["budget_pass"] or row["classification"]["named_return_packet"]
            for row in rows
        ),
        "divisibility_matches_budget": all(
            row["classification"]["budget_pass"] == row["classification"]["direct_divisibility_check"]
            for row in rows
        ),
    }


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_prefix_valuation_budget_or_overflow_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/prefix-valuation-budget-or-overflow-sample-ledger.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取本层 pass-or-return 需要的导入。"""
    criterion = load_json(DOCS / "prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.json")
    kernel = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    prefix = load_json(DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    projection = load_json(DOCS / "prime-matrix-strict-primitive-product-projection-rule-router.json")
    return {
        "target_imported": criterion.get("next_direct_attack_target") == HARDPOINT,
        "valuation_criterion_imported": bool(criterion.get("carrier_lcm_valuation_criterion_closed")),
        "common_kernel_return_cycle_descent_imported": bool(
            kernel.get("common_kernel_return_cycle_descent_or_pdec_proved")
        ),
        "free_common_kernel_return_cycle_excluded": bool(kernel.get("free_common_kernel_return_cycle_excluded")),
        "prefix_structural_dichotomy_imported": bool(prefix.get("prefix_branching_structural_dichotomy_closed")),
        "primitive_projection_common_kernel_guard_imported": bool(
            projection.get("primitive_product_projection_rule_executable_hash_closed")
        ),
    }


def route_rows() -> list[dict[str, str]]:
    """列出 pass-or-return 路由规则。"""
    return [
        {
            "step": "compute_carrier_budget",
            "rule": "B_p=max_c v_p(m_c)=v_p(h0^car)",
            "effect": "给出 carrier-lcm 对每个素数 p 的最大可用指数。",
        },
        {
            "step": "compute_prefix_usage",
            "rule": "E_p(U)=sum_{g in U} v_p(g)=v_p(D(U))",
            "effect": "把前缀消耗压成逐素数 token 用量。",
        },
        {
            "step": "budget_pass",
            "rule": "if E_p(U)<=B_p for every p, then D(U)|h0^car",
            "effect": "该 prefix 可以继续留在 carrier-lcm 商分支。",
        },
        {
            "step": "overflow_return",
            "rule": "if some E_p(U)>B_p, emit CarrierLCMValuationOverflowNamedReturn",
            "effect": "该 prefix 不能留在 primitive carrier-lcm 分支，必须进入命名回流。",
        },
        {
            "step": "named_exit_map",
            "rule": "overflow is prime-power cascade / low common-kernel / fixed-history-PDEC / SAE / hot-core",
            "effect": "溢出不是第四类无名逃逸；最终排斥仍依赖命名出口验收。",
        },
    ]


def decision_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def decision_rows(flags: dict[str, bool], ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    classifier_closed = (
        flags["target_imported"]
        and flags["valuation_criterion_imported"]
        and ledger["all_rows_have_pass_or_named_return"]
        and ledger["divisibility_matches_budget"]
    )
    named_return_map_closed = (
        classifier_closed
        and flags["common_kernel_return_cycle_descent_imported"]
        and flags["prefix_structural_dichotomy_imported"]
        and flags["primitive_projection_common_kernel_guard_imported"]
    )
    pass_or_return_closed = classifier_closed and named_return_map_closed
    return [
        decision_row(
            "PrefixValuationBudgetTargetImported",
            True,
            flags["target_imported"],
            "上一层已把 cold prefix 整除问题压成 valuation 预算或溢出回流。",
            HARDPOINT,
        ),
        decision_row(
            "CarrierLCMValuationCriterionImported",
            True,
            flags["valuation_criterion_imported"],
            "已导入 D(U)|h0^car 等价于逐素数预算不超载。",
            "criterion imported",
        ),
        decision_row(
            "PassOrOverflowClassifierExecutableClosed",
            classifier_closed,
            classifier_closed,
            "给定 carrier quotients 与 prefix steps，分类器必输出预算通过或 valuation 溢出包。",
            OVERFLOW_LEDGER,
        ),
        decision_row(
            "OverflowNamedExitMapClosed",
            named_return_map_closed,
            named_return_map_closed,
            "valuation 溢出已映射到素数幂级联、共同核、固定历史/PDEC、SAE 或热核心。",
            NAMED_RETURN,
        ),
        decision_row(
            "PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturnProved",
            pass_or_return_closed,
            pass_or_return_closed,
            "每个已登记 prefix 产品要么满足 carrier-lcm 预算，要么被命名为 valuation overflow return。",
            OVERFLOW_EXCLUSION,
        ),
        decision_row(
            "CarrierLCMValuationOverflowNamedReturnLedgerClosed",
            named_return_map_closed,
            named_return_map_closed,
            "溢出包的命名、payload 与既有回流出口对接闭合；但未排斥这些出口。",
            NAMED_RETURN,
        ),
        decision_row(
            "ColdPrefixProductDividesCarrierLCMH0LedgerProved",
            False,
            False,
            "存在 overflow return 分支尚未排斥，不能声明所有 cold prefix 都整除 h0^car。",
            OVERFLOW_EXCLUSION,
        ),
        decision_row(
            "PrefixResidualFrequencyEqualsCarrierLCMQuotientProved",
            False,
            False,
            "只有预算通过的 prefix 可立刻得到 h0^car/D(U) 整数残频；溢出分支仍需排斥或吸收。",
            f"{DIVIDES_H0} OR {OVERFLOW_EXCLUSION}",
        ),
        decision_row(
            "H0CarrierQuotientCompatibilityWithColdPrefixesProved",
            False,
            False,
            "pass-or-return 已闭合，但命名 overflow 分支未全局排斥。",
            f"{OVERFLOW_EXCLUSION} AND {PREFIX_QUOTIENT}",
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{OVERFLOW_EXCLUSION} AND {UNIFIED_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 prefix valuation pass-or-return 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, ledger)
    pass_or_return = next(
        item for item in decisions if item["gate"] == "PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturnProved"
    )["proved"]
    overflow_ledger_closed = next(
        item for item in decisions if item["gate"] == "CarrierLCMValuationOverflowNamedReturnLedgerClosed"
    )["proved"]
    return {
        "certificate_type": "prime_matrix_strict_prefix_valuation_budget_or_overflow_router",
        "status": "prefix_valuation_pass_or_overflow_return_closed_overflow_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{OVERFLOW_EXCLUSION} AND {UNIFIED_BUDGET}",
        "next_direct_attack_target": OVERFLOW_EXCLUSION,
        "parallel_attack_targets": [STEP_ORIGIN, NAMED_RETURN, UNIFIED_BUDGET, DSTRUCTURE],
        "imported_flags": flags,
        "route_rows": route_rows(),
        "sample_ledger_path": str(OUT_LEDGER.relative_to(ROOT)),
        "sample_ledger_sha256": sha256(OUT_LEDGER),
        "decision_table": decisions,
        "pass_or_overflow_classifier_executable_closed": bool(
            next(item for item in decisions if item["gate"] == "PassOrOverflowClassifierExecutableClosed")["proved"]
        ),
        "overflow_named_exit_map_closed": bool(
            next(item for item in decisions if item["gate"] == "OverflowNamedExitMapClosed")["proved"]
        ),
        "prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved": bool(pass_or_return),
        "carrier_lcm_valuation_overflow_named_return_ledger_closed": bool(overflow_ledger_closed),
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_proved": False,
        "prefix_residual_frequency_equals_carrier_lcm_quotient_proved": False,
        "h0_carrier_quotient_compatibility_with_cold_prefixes_proved": False,
        "carrier_lcm_valuation_overflow_return_exclusion_or_absorption_proved": False,
        "named_return_exclusion_proved": False,
        "unified_terminal_budget_strict_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn` 已闭合为严格 pass-or-return："
            "对每个已登记 cold prefix，计算 `E_p(U)=sum_g v_p(g)` 与 `B_p=max_c v_p(m_c)`。"
            "若所有 `E_p(U)<=B_p`，则 `D(U)|h0^car`；若某个素数超载，立即输出 "
            "`CarrierLCMValuationOverflowNamedReturn`，并接入素数幂级联、共同核、固定历史/PDEC、SAE 或热核心出口。"
            "因此 valuation 超载不再是无名第四出口；但这些命名出口尚未被排斥，"
            "所以不能声明所有 cold prefix 都整除 `h0^car`，行/列命题仍未无条件闭合。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict prefix valuation 预算或溢出回流路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "pass_or_overflow_classifier_executable_closed",
        "overflow_named_exit_map_closed",
        "prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved",
        "carrier_lcm_valuation_overflow_named_return_ledger_closed",
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. 路由规则")
    lines.append("")
    lines.append("| step | rule | effect |")
    lines.append("| --- | --- | --- |")
    for item in result["route_rows"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["step", "rule", "effect"])
            + " |"
        )
    lines.append("")

    lines.append("## 2. 样本账本")
    lines.append("")
    lines.append(f"- path: `{result['sample_ledger_path']}`")
    lines.append(f"- sha256: `{result['sample_ledger_sha256']}`")
    lines.append("")

    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["decision_table"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )
    lines.append("")

    lines.append("## 4. 下一步最窄点")
    lines.append("")
    lines.append(f"- 主攻：`{result['next_direct_attack_target']}`。")
    lines.append("- 具体任务：排斥或吸收 valuation overflow return；否则只能得到条件分支闭合。")
    lines.append(f"- 并行守门：`{NAMED_RETURN}`、`{UNIFIED_BUDGET}`、`{DSTRUCTURE}`。")
    lines.append("")

    lines.append("## 5. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for file, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、Markdown 与样本账本。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(
        "prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved="
        f"{fmt_bool(result['prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved'])}"
    )
    print(
        "carrier_lcm_valuation_overflow_named_return_ledger_closed="
        f"{fmt_bool(result['carrier_lcm_valuation_overflow_named_return_ledger_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
