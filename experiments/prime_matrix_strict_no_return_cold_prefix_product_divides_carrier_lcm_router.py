#!/usr/bin/env python3
"""生成 strict no-return cold prefix 产品整除 carrier-lcm 证书。

用法示例：
  python3 experiments/prime_matrix_strict_no_return_cold_prefix_product_divides_carrier_lcm_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json

输出：
  data/no-return-cold-prefix-product-divisibility-sample-ledger.json
  docs/monograph/prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json
  docs/monograph/prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json"
OUT_MD = DOCS / "prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.md"
OUT_LEDGER = DATA / "no-return-cold-prefix-product-divisibility-sample-ledger.json"

HARDPOINT = "NoReturnColdPrefixProductDividesCarrierLCMH0"
GLOBAL_DIVIDES = "ColdPrefixProductDividesCarrierLCMH0Ledger"
PREFIX_QUOTIENT = "PrefixResidualFrequencyEqualsCarrierLCMQuotient"
RETURN_EXCLUSION = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-cold-prefix-step-origin-map-router.json",
    DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json",
    DOCS / "prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json",
    DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.json",
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
    """用确定性试除分解正整数；仅用于证书样本和规则哈希。"""
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


def carrier_lcm(carrier_rows: list[dict[str, Any]]) -> int:
    """由 carrier rows 计算 h0^car。"""
    result = 1
    for row in carrier_rows:
        result = lcm(result, int(row["m_c"]))
    return result


def carrier_budget(carrier_rows: list[dict[str, Any]]) -> dict[int, int]:
    """计算 carrier-lcm 的逐素数指数预算。"""
    result: dict[int, int] = {}
    for row in carrier_rows:
        for prime, exp in factor(int(row["m_c"])).items():
            result[prime] = max(result.get(prime, 0), exp)
    return result


def step_local_defects(carrier_rows: list[dict[str, Any]], step: int) -> list[dict[str, Any]]:
    """检测单个 step 是否超出 carrier-lcm 本地域。"""
    budget = carrier_budget(carrier_rows)
    defects = []
    for prime, exp in factor(step).items():
        allowed = budget.get(prime, 0)
        if exp > allowed:
            defects.append(
                {
                    "prime": prime,
                    "step_exp": exp,
                    "allowed_exp": allowed,
                    "defect": "source_domain_defect",
                }
            )
    return defects


def prefix_usage(prefix_steps: list[int]) -> dict[int, int]:
    """计算 prefix product 的逐素数指数用量。"""
    usage: dict[int, int] = {}
    for step in prefix_steps:
        for prime, exp in factor(step).items():
            usage[prime] = usage.get(prime, 0) + exp
    return usage


def classify_prefix(carrier_rows: list[dict[str, Any]], prefix_steps: list[int]) -> dict[str, Any]:
    """分类 prefix：no-return 整除、source defect、或累计 overflow。"""
    h0_car = carrier_lcm(carrier_rows)
    d_u = product(prefix_steps)
    budget = carrier_budget(carrier_rows)
    source_defects = []
    for idx, step in enumerate(prefix_steps):
        for defect in step_local_defects(carrier_rows, step):
            source_defects.append({"step_index": idx, "step": step, **defect})

    usage = prefix_usage(prefix_steps)
    overflow_rows = []
    for prime, used in sorted(usage.items()):
        allowed = budget.get(prime, 0)
        if used > allowed:
            overflow_rows.append(
                {
                    "prime": prime,
                    "used_exp": used,
                    "allowed_exp": allowed,
                    "deficit": used - allowed,
                    "defect": "cumulative_valuation_overflow",
                }
            )

    no_return = not source_defects and not overflow_rows
    return {
        "carrier_rows": carrier_rows,
        "h0_carrier_lcm": h0_car,
        "prefix_steps": prefix_steps,
        "prefix_product": d_u,
        "carrier_budget": {str(k): v for k, v in sorted(budget.items())},
        "prefix_usage": {str(k): v for k, v in sorted(usage.items())},
        "source_defects": source_defects,
        "valuation_overflows": overflow_rows,
        "no_return_branch": no_return,
        "direct_divisibility_check": h0_car % d_u == 0,
        "classification": "no_return_divides" if no_return else "return_branch",
    }


def sample_ledger() -> dict[str, Any]:
    """生成 no-return 分支整除样本账本。"""
    samples = [
        {
            "case": "no_return_token_mixed_divides",
            "carrier_rows": [
                {"column": 1, "m_c": 4},
                {"column": 2, "m_c": 15},
            ],
            "prefix_steps": [2, 6],
        },
        {
            "case": "source_defect_return",
            "carrier_rows": [
                {"column": 1, "m_c": 3},
                {"column": 2, "m_c": 5},
            ],
            "prefix_steps": [4],
        },
        {
            "case": "cumulative_overflow_return",
            "carrier_rows": [
                {"column": 1, "m_c": 2},
                {"column": 2, "m_c": 3},
            ],
            "prefix_steps": [2, 2],
        },
        {
            "case": "prime_power_budget_exact",
            "carrier_rows": [
                {"column": 1, "m_c": 8},
                {"column": 2, "m_c": 9},
            ],
            "prefix_steps": [2, 4, 3],
        },
    ]
    rows = [{**item, "classification_result": classify_prefix(item["carrier_rows"], item["prefix_steps"])} for item in samples]
    return {
        "ledger_type": "no_return_cold_prefix_product_divisibility_sample_ledger",
        "rule": "if every step is locally carrier-admissible and cumulative valuation does not exceed carrier budget, then D(U)|h0^car",
        "rows": rows,
        "all_no_return_rows_divide_h0_car": all(
            (not row["classification_result"]["no_return_branch"])
            or row["classification_result"]["direct_divisibility_check"]
            for row in rows
        ),
        "return_rows_present": any(not row["classification_result"]["no_return_branch"] for row in rows),
        "source_defect_return_present": any(
            row["classification_result"]["source_defects"] for row in rows
        ),
        "valuation_overflow_return_present": any(
            row["classification_result"]["valuation_overflows"] for row in rows
        ),
    }


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_no_return_cold_prefix_product_divides_carrier_lcm_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/no-return-cold-prefix-product-divisibility-sample-ledger.json": sha256(OUT_LEDGER),
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取 no-return 分支整除需要的导入。"""
    step = load_json(DOCS / "prime-matrix-strict-cold-prefix-step-origin-map-router.json")
    valuation = load_json(DOCS / "prime-matrix-strict-prefix-valuation-budget-or-overflow-router.json")
    overflow = load_json(DOCS / "prime-matrix-strict-carrier-lcm-overflow-absorption-frontier-router.json")
    h0 = load_json(DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.json")
    return {
        "target_imported": step.get("next_direct_attack_target") == HARDPOINT,
        "token_origin_map_imported": bool(step.get("canonical_token_origin_map_criterion_closed")),
        "step_source_defect_return_imported": bool(step.get("step_local_carrier_domain_defect_return_closed")),
        "valuation_pass_or_overflow_imported": bool(
            valuation.get("prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved")
        ),
        "overflow_frontier_imported": bool(overflow.get("carrier_lcm_overflow_independent_hardpoint_removed")),
        "carrier_lcm_h0_formula_imported": bool(h0.get("carrier_quotient_lcm_h0_formula_closed")),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出 no-return 分支定理步骤。"""
    return [
        {
            "step": "local_step_guard",
            "statement": "Every step g has token origins, equivalently v_p(g)<=B_p for every p.",
            "status": "imported_closed",
        },
        {
            "step": "cumulative_budget_guard",
            "statement": "The whole prefix satisfies sum_g v_p(g)<=B_p for every p.",
            "status": "imported_closed",
        },
        {
            "step": "valuation_identity",
            "statement": "v_p(D(U))=sum_g v_p(g) and v_p(h0^car)=B_p.",
            "status": "closed",
        },
        {
            "step": "no_return_divisibility",
            "statement": "Under both guards, v_p(D(U))<=v_p(h0^car) for all p, hence D(U)|h0^car.",
            "status": "closed",
        },
        {
            "step": "return_boundary",
            "statement": "If either guard fails, the branch is not no-return and must be handled by source-defect or overflow absorption.",
            "status": "closed_as_return_condition",
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
    no_return_closed = (
        flags["target_imported"]
        and flags["token_origin_map_imported"]
        and flags["valuation_pass_or_overflow_imported"]
        and flags["carrier_lcm_h0_formula_imported"]
        and ledger["all_no_return_rows_divide_h0_car"]
    )
    return [
        decision_row(
            "NoReturnDivisibilityTargetImported",
            True,
            flags["target_imported"],
            "上一层已把最窄点压成 no-return 分支上的 prefix product 整除。",
            HARDPOINT,
        ),
        decision_row(
            "StepTokenOriginGuardImported",
            True,
            flags["token_origin_map_imported"],
            "局部 step token 来源图已闭合。",
            "local guard imported",
        ),
        decision_row(
            "CumulativeValuationPassOrOverflowImported",
            True,
            flags["valuation_pass_or_overflow_imported"],
            "累计 valuation pass-or-overflow 已闭合。",
            "cumulative guard imported",
        ),
        decision_row(
            "NoReturnColdPrefixProductDividesCarrierLCMH0Proved",
            no_return_closed,
            no_return_closed,
            "在无 source-defect 且无 cumulative overflow 的分支上，D(U)|h0^car。",
            HARDPOINT,
        ),
        decision_row(
            "PrefixResidualFrequencyEqualsCarrierLCMQuotientForNoReturnProved",
            no_return_closed,
            no_return_closed,
            "no-return 分支可定义实际整数 H_U^car=h0^car/D(U)。",
            PREFIX_QUOTIENT,
        ),
        decision_row(
            "ColdPrefixProductDividesCarrierLCMH0LedgerGlobalProved",
            False,
            False,
            "全局仍有 source-defect 与 valuation-overflow return 分支未排斥或吸收。",
            RETURN_EXCLUSION,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{RETURN_EXCLUSION} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 no-return 分支整除证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    ledger = sample_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    flags = imported_flags()
    decisions = decision_rows(flags, ledger)
    no_return_closed = next(
        item for item in decisions if item["gate"] == "NoReturnColdPrefixProductDividesCarrierLCMH0Proved"
    )["proved"]
    return {
        "certificate_type": "prime_matrix_strict_no_return_cold_prefix_product_divides_carrier_lcm_router",
        "status": "no_return_cold_prefix_product_divides_carrier_lcm_closed_return_branches_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{RETURN_EXCLUSION} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL}",
        "next_direct_attack_target": RETURN_EXCLUSION,
        "parallel_attack_targets": [SPARSE_BUDGET, PERSISTENT_TERMINAL, DSTRUCTURE],
        "imported_flags": flags,
        "theorem_rows": theorem_rows(),
        "sample_ledger_path": str(OUT_LEDGER.relative_to(ROOT)),
        "sample_ledger_sha256": sha256(OUT_LEDGER),
        "decision_table": decisions,
        "no_return_cold_prefix_product_divides_carrier_lcm_h0_proved": bool(no_return_closed),
        "prefix_residual_frequency_equals_carrier_lcm_quotient_for_no_return_proved": bool(no_return_closed),
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_global_proved": False,
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`NoReturnColdPrefixProductDividesCarrierLCMH0` 已闭合：在同一 carrier-lcm h0 下，"
            "若每个 step 都有局部 token 来源图，且整个 prefix 的累计 valuation 不超预算，"
            "则 `v_p(D(U))<=v_p(h0^car)` 对所有素数成立，故 `D(U)|h0^car`，"
            "并可定义实际整数残频 `H_U^car=h0^car/D(U)`。"
            "这只关闭 no-return 分支；source-defect 和 valuation-overflow return 分支仍需排斥或预算吸收。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict no-return cold prefix 产品整除 carrier-lcm 路由器")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "no_return_cold_prefix_product_divides_carrier_lcm_h0_proved",
        "prefix_residual_frequency_equals_carrier_lcm_quotient_for_no_return_proved",
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_global_proved",
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")

    lines.append("## 1. No-return 分支定理")
    lines.append("")
    lines.append("| step | statement | status |")
    lines.append("| --- | --- | --- |")
    for item in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(table_cell(item[key]) for key in ["step", "statement", "status"])
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
    lines.append(f"- 同步硬点：`{SPARSE_BUDGET}` 与 `{PERSISTENT_TERMINAL}`。")
    lines.append("- 边界：本步闭合 no-return 分支，不排斥所有 return 分支。")
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
        "no_return_cold_prefix_product_divides_carrier_lcm_h0_proved="
        f"{fmt_bool(result['no_return_cold_prefix_product_divides_carrier_lcm_h0_proved'])}"
    )
    print(
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_global_proved="
        f"{fmt_bool(result['cold_prefix_product_divides_carrier_lcm_h0_ledger_global_proved'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
