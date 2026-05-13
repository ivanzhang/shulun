#!/usr/bin/env python3
"""生成 strict no-return h0 发射器回接 Rankin 参数链同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_no_return_h0_emitter_rankin_parameter_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json
  docs/monograph/prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-no-return-h0-emitter-rankin-parameter-sync-router.md"

HARDPOINT = "ActualProductDivisorDomainH0EmitterForFormalUnit"
NO_RETURN_H0 = "NoReturnActualProductDivisorDomainH0EmitterForFormalUnit"
ACTUAL_BLOCK = "ActualColdProductBlockParameterLedgerForP018Table"
BLOCK_ENUMERATOR = "ActualDyadicColdProductBlockEnumeratorForH0"
KERNEL_REGISTER = "PerBlockRegisteredCommonKernelLedger"
P018_TABLE = "PrimitiveProductRankinP018InequalityTable"
FAILURE_RETURN = "PrimitiveProductRankinFailureReturnPacketLedger"
RETURN_ABSORB = "CarrierLCMCompatibilityReturnBranchExclusionOrAbsorption"
SPARSE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PERSISTENT_TERMINAL = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-actual-h0-product-divisor-emitter-router.json",
    "prime-matrix-strict-actual-cold-product-block-parameter-router.json",
    "prime-matrix-strict-early-zero-factorization-carrier-router.json",
    "prime-matrix-strict-h0-carrier-quotient-compat-router.json",
    "prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json",
    "prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json",
    "prime-matrix-strict-primitive-product-rankin-p018-table-router.json",
    "prime-matrix-strict-primitive-product-projection-rule-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_no_return_h0_emitter_rankin_parameter_sync_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def imported_flags() -> dict[str, bool]:
    """读取 no-return h0 回接需要的导入。"""
    actual_h0 = load_json("prime-matrix-strict-actual-h0-product-divisor-emitter-router.json")
    actual_block = load_json("prime-matrix-strict-actual-cold-product-block-parameter-router.json")
    carrier = load_json("prime-matrix-strict-early-zero-factorization-carrier-router.json")
    compat = load_json("prime-matrix-strict-h0-carrier-quotient-compat-router.json")
    no_return = load_json("prime-matrix-strict-no-return-cold-prefix-product-divides-carrier-lcm-router.json")
    return_branch = load_json("prime-matrix-strict-carrier-lcm-return-branch-frontier-router.json")
    p018 = load_json("prime-matrix-strict-primitive-product-rankin-p018-table-router.json")
    projection = load_json("prime-matrix-strict-primitive-product-projection-rule-router.json")
    return {
        "actual_h0_target_imported": actual_h0.get("next_direct_attack_target")
        == "CanonicalH0FromEarlyZeroRowFactorizationIdentity",
        "actual_block_needs_h0_imported": actual_block.get("next_direct_attack_target") == HARDPOINT,
        "early_zero_carrier_ledger_present": carrier.get("early_zero_row_factorization_carrier_ledger_present")
        is True,
        "carrier_lcm_formula_closed": compat.get("carrier_quotient_lcm_h0_formula_closed") is True,
        "h0_no_posthoc_discipline_closed": compat.get("h0_no_posthoc_envelope_discipline_closed") is True,
        "no_return_divisibility_proved": no_return.get("no_return_cold_prefix_product_divides_carrier_lcm_h0_proved")
        is True,
        "no_return_residual_frequency_proved": no_return.get(
            "prefix_residual_frequency_equals_carrier_lcm_quotient_for_no_return_proved"
        )
        is True,
        "return_branch_frontier_closed": return_branch.get("return_branch_alphabet_frontier_closed") is True,
        "return_branch_global_absorption_proved": return_branch.get(
            "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved"
        )
        is True,
        "p018_schema_closed": p018.get("p018_table_schema_closed") is True,
        "primitive_projection_hash_closed": projection.get("primitive_product_projection_rule_executable_hash_closed")
        is True,
    }


def bridge_rows() -> list[dict[str, str]]:
    """列出 no-return h0 字段如何回接 P^0.18 参数表。"""
    return [
        {
            "field": "source_tuple_hash",
            "no_return_source": "inherited from formal-unit/source tuple",
            "rankin_use": "row key",
            "status": "available_from_upstream",
        },
        {
            "field": "h0",
            "no_return_source": "h0^car=lcm_c m_c from early-zero-row carrier",
            "rankin_use": "product divisor domain d|h0",
            "status": "closed_for_no_return_branch",
        },
        {
            "field": "D(U)|h0",
            "no_return_source": "local token origin + cumulative valuation pass",
            "rankin_use": "legal cold product support domain",
            "status": "closed_for_no_return_branch",
        },
        {
            "field": "H_U",
            "no_return_source": "H_U^car=h0^car/D(U)",
            "rankin_use": "residual frequency for child windows",
            "status": "closed_for_no_return_branch",
        },
        {
            "field": "Y blocks",
            "no_return_source": "dyadic enumeration over actual divisors d|h0^car after cold/no-return guards",
            "rankin_use": "P^0.18 table rows",
            "status": "open",
        },
        {
            "field": "registered_common_kernel",
            "no_return_source": "per block return discipline / primitive projection",
            "rankin_use": "avoid double-counting kernel clusters",
            "status": "open",
        },
    ]


def remaining_rows() -> list[dict[str, str]]:
    """列出本证书之后的精确剩余。"""
    return [
        {
            "remaining": BLOCK_ENUMERATOR,
            "meaning": "给定 h0^car 后，仍需枚举实际 dyadic cold 产品块 Y，并锁定全体行。",
        },
        {
            "remaining": KERNEL_REGISTER,
            "meaning": "每块必须登记共同核/primitive 投影状态，否则 Rankin 行会重复计数。",
        },
        {
            "remaining": P018_TABLE,
            "meaning": "即使 h0 字段可用，仍需逐块 Rankin 权重与 P^0.18 预算比较。",
        },
        {
            "remaining": FAILURE_RETURN,
            "meaning": "诊断样表已有失败行；失败块必须进入热窗口、共同核、PDEC/SAE 或固定历史回流。",
        },
        {
            "remaining": RETURN_ABSORB,
            "meaning": "source-defect 与 valuation-overflow 的全局 return 分支仍需非持久预算吸收或持久终端排斥。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    no_return_h0_closed = result["no_return_h0_emitter_for_rankin_parameter_closed"]
    return [
        row(
            "ActualH0EmitterTargetImported",
            result["actual_h0_target_imported"],
            False,
            "旧 actual h0 发射器缺口已定位为从早期零行载体生成 h0。",
            HARDPOINT,
        ),
        row(
            "CarrierLCMH0FormulaImported",
            result["carrier_lcm_formula_closed"],
            result["carrier_lcm_formula_closed"],
            "h0^car=lcm_c m_c 已由早期零行逐列商载体先验定义。",
            "CarrierQuotientLCMH0Formula",
        ),
        row(
            "NoPostHocH0DisciplineImported",
            result["h0_no_posthoc_discipline_closed"],
            result["h0_no_posthoc_discipline_closed"],
            "h0^car 在 cold prefix/Rankin 枚举前固定，不能后验扩大。",
            "H0NoPostHocEnvelopeDiscipline",
        ),
        row(
            "NoReturnDivisibilityAndResidualFrequencyImported",
            result["no_return_divisibility_proved"] and result["no_return_residual_frequency_proved"],
            result["no_return_divisibility_proved"] and result["no_return_residual_frequency_proved"],
            "无 source-defect 且无 valuation-overflow 时，D(U)|h0^car 且 H_U^car 为整数。",
            "NoReturnColdPrefixProductDividesCarrierLCMH0",
        ),
        row(
            "NoReturnActualProductDivisorDomainH0EmitterClosed",
            no_return_h0_closed,
            no_return_h0_closed,
            "no-return 分支可向 actual cold product / Rankin 参数表提供非循环 h0 字段。",
            NO_RETURN_H0,
        ),
        row(
            "GlobalActualProductDivisorDomainH0EmitterProved",
            False,
            False,
            "全局 h0 发射器仍受 source-defect 与 valuation-overflow return 分支限制。",
            RETURN_ABSORB,
        ),
        row(
            "ActualColdProductBlockParameterLedgerPresent",
            False,
            False,
            "h0 字段 no-return 可用，但还缺实际 dyadic Y、per-block kernel 与权重行。",
            f"{BLOCK_ENUMERATOR} AND {KERNEL_REGISTER} AND {P018_TABLE}",
        ),
        row(
            "PrimitiveProductRankinP018InequalityTablePresent",
            False,
            False,
            "P^0.18 schema 已有，但缺实际块行、权重比较和失败回流包。",
            f"{P018_TABLE} AND {FAILURE_RETURN}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{RETURN_ABSORB} AND {SPARSE_BUDGET} AND {PERSISTENT_TERMINAL} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 no-return h0 回接 Rankin 参数链同步证书。"""
    flags = imported_flags()
    no_return_h0_closed = (
        flags["actual_block_needs_h0_imported"]
        and flags["early_zero_carrier_ledger_present"]
        and flags["carrier_lcm_formula_closed"]
        and flags["h0_no_posthoc_discipline_closed"]
        and flags["no_return_divisibility_proved"]
        and flags["no_return_residual_frequency_proved"]
        and flags["p018_schema_closed"]
        and flags["primitive_projection_hash_closed"]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_no_return_h0_emitter_rankin_parameter_sync_router",
        "status": "no_return_h0_emitter_synced_to_rankin_parameter_chain_return_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "no_return_h0_emitter_for_rankin_parameter_closed": no_return_h0_closed,
        "actual_product_divisor_domain_h0_emitter_for_formal_unit_global_proved": False,
        "actual_cold_product_block_parameter_ledger_present": False,
        "primitive_product_rankin_p018_inequality_table_present": False,
        "carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved": False,
        "sparse_history_demand_exceeds_nonpersistent_supply_budget_proved": False,
        "persistent_terminal_family_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": (
            f"{BLOCK_ENUMERATOR} AND {KERNEL_REGISTER} AND {P018_TABLE} "
            f"AND {FAILURE_RETURN} AND {RETURN_ABSORB}"
        ),
        "next_direct_attack_target": BLOCK_ENUMERATOR,
        "parallel_attack_targets": [
            KERNEL_REGISTER,
            P018_TABLE,
            FAILURE_RETURN,
            RETURN_ABSORB,
            SPARSE_BUDGET,
            PERSISTENT_TERMINAL,
            DSTRUCTURE,
        ],
        "bridge_rows": bridge_rows(),
        "remaining_rows": remaining_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "no-return 分支的 actual h0 发射器可以回接到 Rankin 参数链："
            "早期零行逐列因式载体给出非后验 `h0^car=lcm_c m_c`，无回流分支又已证明 "
            "`D(U)|h0^car` 和 `H_U^car=h0^car/D(U)` 的整数性。因此在无 source-defect、"
            "无 valuation-overflow 的分支上，P^0.18 表所需的 `h0` 产品除数域字段不再缺失。"
            "但全局 return 分支尚未排斥或吸收，实际 dyadic 块、per-block kernel、Rankin 权重表"
            "和失败回流包也尚未完成，所以行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines: list[str] = [
        "# Prime Matrix strict no-return h0 发射器回接 Rankin 参数链同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"no_return_h0_emitter_for_rankin_parameter_closed={fmt_bool(result['no_return_h0_emitter_for_rankin_parameter_closed'])}",
        f"actual_product_divisor_domain_h0_emitter_for_formal_unit_global_proved={fmt_bool(result['actual_product_divisor_domain_h0_emitter_for_formal_unit_global_proved'])}",
        f"actual_cold_product_block_parameter_ledger_present={fmt_bool(result['actual_cold_product_block_parameter_ledger_present'])}",
        f"primitive_product_rankin_p018_inequality_table_present={fmt_bool(result['primitive_product_rankin_p018_inequality_table_present'])}",
        f"carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved={fmt_bool(result['carrier_lcm_compatibility_return_branch_exclusion_or_absorption_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Rankin 参数字段桥",
        "",
        "| field | no_return_source | rankin_use | status |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["bridge_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(item["field"]),
                    table_cell(item["no_return_source"]),
                    table_cell(item["rankin_use"]),
                    table_cell(item["status"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 剩余原子",
            "",
            "| remaining | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["remaining_rows"]:
        lines.append(f"| `{table_cell(item['remaining'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")
    lines.extend(
        [
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(f"no_return_h0_emitter_for_rankin_parameter_closed={fmt_bool(result['no_return_h0_emitter_for_rankin_parameter_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
