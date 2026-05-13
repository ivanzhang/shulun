#!/usr/bin/env python3
"""生成 strict cold prefix 产品整除 carrier-lcm-h0 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_prefix_divides_carrier_lcm_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.json
  docs/monograph/prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-prefix-divides-carrier-lcm-router.md"

HARDPOINT = "ColdPrefixProductDividesCarrierLCMH0Ledger"
VALUATION_BUDGET = "PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn"
STEP_ORIGIN = "ColdPrefixStepQuotientOriginMapToCarrierRows"
OVERFLOW_RETURN = "CarrierLCMValuationOverflowNamedReturnLedger"
PREFIX_QUOTIENT = "PrefixResidualFrequencyEqualsCarrierLCMQuotient"
H0_COMPAT = "H0CarrierQuotientCompatibilityWithColdPrefixes"
CANONICAL_H0 = "CanonicalH0FromEarlyZeroRowFactorizationIdentity"
H0_EMITTER = "ActualProductDivisorDomainH0EmitterForFormalUnit"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.json",
    DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json",
    DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
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


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_prefix_divides_carrier_lcm_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def imported_flags() -> dict[str, bool]:
    """读取整除硬点需要的导入。"""
    compat = load_json(DOCS / "prime-matrix-strict-h0-carrier-quotient-compat-router.json")
    prefix = load_json(DOCS / "prime-matrix-strict-cold-history-prefix-branching-attack-router.json")
    fiber = load_json(DOCS / "prime-matrix-strict-product-fiber-multiplicity-router.json")
    common = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    return {
        "divisibility_target_imported": compat.get("next_direct_attack_target") == HARDPOINT,
        "carrier_lcm_formula_imported": bool(compat.get("carrier_quotient_lcm_h0_formula_closed")),
        "prefix_product_interface_imported": "D(U)" in json.dumps(prefix, ensure_ascii=False),
        "product_fiber_support_imported": "d" in json.dumps(fiber, ensure_ascii=False),
        "common_kernel_return_imported": bool(common.get("common_kernel_return_cycle_descent_or_pdec_proved")),
    }


def valuation_criterion_rows() -> list[dict[str, str]]:
    """列出整除等价判据。"""
    return [
        {
            "name": "carrier_lcm_valuation",
            "formula": "v_p(h0^car)=max_c v_p(m_c)",
            "status": "closed",
        },
        {
            "name": "prefix_product_valuation",
            "formula": "v_p(D(U))=sum_{step g in U} v_p(g)",
            "status": "closed",
        },
        {
            "name": "divisibility_criterion",
            "formula": "D(U)|h0^car iff for all p, sum_g v_p(g)<=max_c v_p(m_c)",
            "status": "closed",
        },
        {
            "name": "overflow_interpretation",
            "formula": "if inequality fails for some p, U cannot stay in carrier-lcm primitive branch",
            "status": "closed_as_return_condition",
        },
    ]


def obstruction_rows() -> list[dict[str, str]]:
    """列出剩余阻断。"""
    return [
        {
            "obstruction": "step_origin_not_registered",
            "meaning": "每个 prefix step g 必须指向 carrier rows；否则无法比较其 p-adic 用量。",
            "next": STEP_ORIGIN,
        },
        {
            "obstruction": "repeated_prime_power_overflow",
            "meaning": "即使每个 g 单独除某个 m_c，多个步骤的同素数指数和仍可能超过 lcm 最大指数。",
            "next": VALUATION_BUDGET,
        },
        {
            "obstruction": "overflow_return_not_closed",
            "meaning": "若指数超预算，必须登记共同核、固定历史、PDEC/SAE 或 ColumnCRT 回流。",
            "next": OVERFLOW_RETURN,
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


def decision_rows(flags: dict[str, bool]) -> list[dict[str, Any]]:
    """生成判定表。"""
    criterion_closed = flags["divisibility_target_imported"] and flags["carrier_lcm_formula_imported"]
    return [
        decision_row(
            "ColdPrefixDivisibilityTargetImported",
            True,
            flags["divisibility_target_imported"],
            "上一层已把最窄点压成 cold prefix 产品是否除 carrier-lcm h0。",
            HARDPOINT,
        ),
        decision_row(
            "CarrierLCMValuationCriterionClosed",
            criterion_closed,
            criterion_closed,
            "D(U)|h0^car 等价于逐素数 valuation 预算不超载。",
            "criterion closed",
        ),
        decision_row(
            "ColdPrefixStepQuotientOriginMapToCarrierRowsProved",
            False,
            False,
            "尚未为每个 prefix step g 登记其来自哪些 carrier quotient rows。",
            STEP_ORIGIN,
        ),
        decision_row(
            "PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturnProved",
            False,
            False,
            "尚未证明所有 cold prefix 满足 valuation 预算，或超载必回流。",
            VALUATION_BUDGET,
        ),
        decision_row(
            "CarrierLCMValuationOverflowNamedReturnLedgerClosed",
            False,
            False,
            "指数超载后的共同核/固定历史/PDEC/SAE/ColumnCRT 回流包未闭合。",
            OVERFLOW_RETURN,
        ),
        decision_row(
            "ColdPrefixProductDividesCarrierLCMH0LedgerProved",
            False,
            False,
            "整除判据已闭合，但 step origin、valuation 预算和溢出回流未证。",
            f"{STEP_ORIGIN} AND {VALUATION_BUDGET} AND {OVERFLOW_RETURN}",
        ),
        decision_row(
            "PrefixResidualFrequencyEqualsCarrierLCMQuotientProved",
            False,
            False,
            "整除未证，因此不能声明 H_U=h0^car/D(U) 是实际整数残频。",
            PREFIX_QUOTIENT,
        ),
        decision_row(
            "H0CarrierQuotientCompatibilityWithColdPrefixesProved",
            False,
            False,
            "cold prefix 整除未证，h0 商兼容仍未闭合。",
            H0_COMPAT,
        ),
        decision_row(
            "CanonicalH0FromEarlyZeroRowFactorizationIdentityProved",
            False,
            False,
            "h0 商兼容未闭合，规范 h0 恒等式仍未闭合。",
            CANONICAL_H0,
        ),
        decision_row(
            "ActualProductDivisorDomainH0EmitterForFormalUnitProved",
            False,
            False,
            "规范 h0 恒等式未闭合，h0 发射器仍未闭合。",
            H0_EMITTER,
        ),
        decision_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{VALUATION_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 cold prefix 整除 carrier-lcm-h0 证书。"""
    flags = imported_flags()
    rows = decision_rows(flags)
    criterion_closed = bool(
        next(item for item in rows if item["gate"] == "CarrierLCMValuationCriterionClosed")["proved"]
    )
    return {
        "certificate_type": "prime_matrix_strict_cold_prefix_divides_carrier_lcm_router",
        "status": "carrier_lcm_divisibility_criterion_closed_prefix_valuation_budget_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{VALUATION_BUDGET} AND {OVERFLOW_RETURN}",
        "next_direct_attack_target": VALUATION_BUDGET,
        "parallel_attack_targets": [STEP_ORIGIN, OVERFLOW_RETURN, DSTRUCTURE],
        "imported_flags": flags,
        "valuation_criterion_rows": valuation_criterion_rows(),
        "obstruction_rows": obstruction_rows(),
        "decision_table": rows,
        "carrier_lcm_valuation_criterion_closed": criterion_closed,
        "cold_prefix_step_quotient_origin_map_to_carrier_rows_proved": False,
        "prefix_valuation_budget_against_carrier_lcm_or_overflow_return_proved": False,
        "carrier_lcm_valuation_overflow_named_return_ledger_closed": False,
        "cold_prefix_product_divides_carrier_lcm_h0_ledger_proved": False,
        "prefix_residual_frequency_equals_carrier_lcm_quotient_proved": False,
        "h0_carrier_quotient_compatibility_with_cold_prefixes_proved": False,
        "canonical_h0_from_early_zero_row_factorization_identity_proved": False,
        "actual_product_divisor_domain_h0_emitter_for_formal_unit_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "`ColdPrefixProductDividesCarrierLCMH0Ledger` 已压到精确 valuation 判据："
            "`D(U)|h0^car` 当且仅当每个素数 p 上，prefix steps 的累计指数 "
            "`sum_g v_p(g)` 不超过载体商中的最大指数 `max_c v_p(m_c)`。"
            "这关闭了整除判定的代数部分，但没有证明所有 cold prefix 满足该预算；"
            "若超载，必须进入共同核/固定历史/PDEC/SAE/ColumnCRT 回流。"
            "最新最窄点为 `PrefixValuationBudgetAgainstCarrierLCMOrOverflowReturn`。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict cold prefix 整除 carrier-lcm-h0 路由器",
        "",
        "## 结论",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"status={result['status']}",
        f"hardpoint_before={result['hardpoint_before_router']}",
        f"hardpoint_after={result['hardpoint_after_router']}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"carrier_lcm_valuation_criterion_closed={fmt_bool(result['carrier_lcm_valuation_criterion_closed'])}",
        f"cold_prefix_product_divides_carrier_lcm_h0_ledger_proved={fmt_bool(result['cold_prefix_product_divides_carrier_lcm_h0_ledger_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## Valuation 判据",
        "",
        "| 名称 | 公式 | 状态 |",
        "|---|---|---|",
    ]
    for item in result["valuation_criterion_rows"]:
        lines.append(f"| `{table_cell(item['name'])}` | {table_cell(item['formula'])} | `{table_cell(item['status'])}` |")
    lines.extend(["", "## 剩余阻断", "", "| 阻断 | 含义 | 下一步 |", "|---|---|---|"])
    for item in result["obstruction_rows"]:
        lines.append(
            f"| `{table_cell(item['obstruction'])}` | {table_cell(item['meaning'])} | `{table_cell(item['next'])}` |"
        )
    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| Gate | Closed | Proved | Meaning | Remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["decision_table"]:
        lines.append(
            "| `{}` | `{}` | `{}` | {} | `{}` |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                fmt_bool(item["proved"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
            )
        )
    lines.extend(["", "## 依赖哈希", "", "| 文件 | SHA256 |", "|---|---|"])
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"carrier_lcm_valuation_criterion_closed={fmt_bool(result['carrier_lcm_valuation_criterion_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
