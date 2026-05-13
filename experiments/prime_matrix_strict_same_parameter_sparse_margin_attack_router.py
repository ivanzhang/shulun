#!/usr/bin/env python3
"""生成 strict 同参数稀疏供需严格余量攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_same_parameter_sparse_margin_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-attack-router.json
  docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-same-parameter-sparse-margin-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-same-parameter-sparse-margin-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-sparse-budget-after-unified-sync-router.json",
    "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    "prime-matrix-strict-cold-core-threshold-budget-gap-router.json",
    "prime-matrix-strict-named-return-after-rowfree-sync-router.json",
    "prime-matrix-strict-named-return-same-parameter-deduction-router.json",
    "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json",
]

STRICT_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
BETA_APPENDIX = (
    "BetaSieveLowerWeightRecursiveConstructionLedger AND "
    "BetaSieveLowerBoundDominanceProof AND "
    "BetaSieveMainCoefficientExplicit99PercentPGe100000"
)


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
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
        "experiments/prime_matrix_strict_same_parameter_sparse_margin_attack_router.py": sha256(
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


def margin_fields() -> list[dict[str, str]]:
    """列出同参数稀疏余量字段。"""
    return [
        {
            "field": "parameter_id",
            "status": "closed",
            "meaning": "继承 alpha=0.43, P>=100000, same z/D/Lambda/T_PDEC 窗口。",
        },
        {
            "field": "M# demand",
            "status": "available_under_standard_external_contract",
            "meaning": "finite-prefix 需求侧在当前接受的 standard/external lower-sieve 合同下可用。",
        },
        {
            "field": "nonpersistent registered returns",
            "status": "absorbed_into_U_np_schema",
            "meaning": "纯非持久分支的塌缩和短回流并入 U_np；不能另作无名扣除。",
        },
        {
            "field": "hot/fixed/persistent exits",
            "status": "parallel_open",
            "meaning": "热核心、固定历史、持久终端族不属于 U_np，必须独立排斥或进入终端族验收。",
        },
        {
            "field": "U_np numeric envelope",
            "status": "open",
            "meaning": "已有公式 U_np<=sum_W(T_PDEC(W)-1)C_core(W)，但没有同参数数值上界。",
        },
        {
            "field": "strict margin",
            "status": "open",
            "meaning": "尚未证明 M#_{x,z}>U_np 的同参数严格不等式。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成同参数稀疏余量判定表。"""
    sparse_sync = data["sparse_sync"]
    finite = data["finite"]
    cold_balance = data["cold_balance"]
    cold_gap = data["cold_gap"]
    named = data["named"]
    same_param_named = data["same_param_named"]
    concrete = data["concrete"]

    target_imported = sparse_sync.get("next_direct_attack_target") == STRICT_MARGIN
    d0_available = finite.get("finite_boundary_prefix_certificate_external_or_standard_closed") is True
    lower_sieve_first_principles = (
        finite.get("finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed") is True
    )
    cold_formula = (
        cold_balance.get("cold_supply_upper_envelope_closed") is True
        and cold_gap.get("cold_supply_upper_bound_closed") is True
    )
    cold_discipline = (
        cold_balance.get("same_parameter_lambda_schedule_closed") is True
        and cold_balance.get("adaptive_lambda_no_free_lunch_dichotomy_closed") is True
        and cold_gap.get("cold_budget_contradiction_criterion_closed") is True
    )
    named_alphabet = named.get("named_return_alphabet_compression_closed") is True
    nonpersistent_schema = (
        same_param_named.get("nonpersistent_named_return_absorbed_by_budget") is False
        and same_param_named.get("named_return_same_parameter_schema_closed") is True
    )
    cold_numeric_open = concrete.get("u0_cold_supply_bound_available") is False

    return [
        row(
            "SparseStrictMarginTargetImported",
            target_imported,
            False,
            "上一层已把稀疏预算缺口压成同参数严格余量证书。",
            STRICT_MARGIN,
        ),
        row(
            "DemandTermAvailableUnderCurrentContract",
            d0_available,
            False,
            "M# / D0 需求项在当前 standard/external lower-sieve 合同下可用。",
            "closed under accepted current contract",
        ),
        row(
            "FirstPrinciplesLowerSieveStillSeparate",
            lower_sieve_first_principles,
            False,
            "若要求 lower-sieve 从零内联，仍需 beta-sieve 三项附录。",
            "closed" if lower_sieve_first_principles else BETA_APPENDIX,
        ),
        row(
            "NonpersistentReturnAbsorptionSchemaClosed",
            named_alphabet and nonpersistent_schema,
            False,
            "非持久回流不是额外 E 项，而是并入 U_np 预算；持久回流仍并行开放。",
            COLD_NUMERIC,
        ),
        row(
            "ColdSupplyFormulaAndParameterDisciplineClosed",
            cold_formula and cold_discipline,
            True,
            "U_np 的求和公式、Lambda 纪律和供需判据已闭合。",
            COLD_NUMERIC,
        ),
        row(
            "ColdSupplyNumericEnvelopeProved",
            False,
            False,
            "尚未把 sum_W(T_PDEC(W)-1)C_core(W) 数值压到小于需求项。",
            COLD_NUMERIC,
        ),
        row(
            "SameParameterSparseDemandColdSupplyStrictMarginProved",
            False,
            False,
            "在纯非持久分支内，唯一内部缺口已压成 ColdSupplySameParameterNumericEnvelope。",
            COLD_NUMERIC,
        ),
        row(
            "HotFixedPersistentParallelExitsExcluded",
            False,
            False,
            "热核心、固定历史、持久终端族仍未排斥，不能用本非持久余量包吞掉。",
            f"{HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM}",
        ),
        row(
            "SparseBudgetStrictMarginCurrentCorpusProved",
            False,
            False,
            "同参数结构闭合，但冷供给数值包与并行终端出口尚未关闭。",
            f"{COLD_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{COLD_NUMERIC} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
        row(
            "PreviousConcreteTableStillBlockedButD0Updated",
            cold_numeric_open,
            False,
            "旧 concrete table 仍缺 U0/E0 数值；本步仅把非持久内部主缺口更新为 U_np 数值包。",
            COLD_NUMERIC,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同参数稀疏严格余量攻坚证书。"""
    data = {
        "sparse_sync": load_json("prime-matrix-strict-sparse-budget-after-unified-sync-router.json"),
        "finite": load_json("prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json"),
        "cold_balance": load_json("prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"),
        "cold_gap": load_json("prime-matrix-strict-cold-core-threshold-budget-gap-router.json"),
        "named": load_json("prime-matrix-strict-named-return-after-rowfree-sync-router.json"),
        "same_param_named": load_json("prime-matrix-strict-named-return-same-parameter-deduction-router.json"),
        "concrete": load_json("prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"),
    }
    rows = build_rows(data)
    internal_reduction_closed = all(
        any(item["gate"] == gate and item["closed"] for item in rows)
        for gate in [
            "SparseStrictMarginTargetImported",
            "DemandTermAvailableUnderCurrentContract",
            "NonpersistentReturnAbsorptionSchemaClosed",
            "ColdSupplyFormulaAndParameterDisciplineClosed",
        ]
    )

    return {
        "certificate_type": "prime_matrix_strict_same_parameter_sparse_margin_attack_router",
        "status": "same_parameter_sparse_margin_reduced_to_cold_numeric_envelope_parallel_exits_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "same_parameter_sparse_margin_internal_reduction_closed": internal_reduction_closed,
        "demand_term_available_under_standard_external_contract": True,
        "first_principles_lower_sieve_closed": False,
        "nonpersistent_return_absorption_schema_closed": True,
        "cold_supply_formula_and_parameter_discipline_closed": True,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "hot_core_fixed_history_persistent_exits_excluded": False,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": STRICT_MARGIN,
        "hardpoint_after_router": f"{COLD_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM}",
        "next_direct_attack_target": COLD_NUMERIC,
        "parallel_attack_targets": [
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
            BETA_APPENDIX,
        ],
        "margin_fields": margin_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SameParameterSparseDemandColdSupplyStrictMarginCertificate` 已继续下钻："
            "在纯非持久分支内，需求项在当前 standard/external lower-sieve 合同下可用，"
            "非持久命名回流并入 U_np，冷供给公式和 Lambda/PDEC 调参纪律已闭合。"
            "因此该分支的唯一内部剩余是 `ColdSupplySameParameterNumericEnvelope`，即把 "
            "`sum_W(T_PDEC(W)-1)C_core(W)` 在同一参数账本下压到小于 M# 需求项。"
            "热核心、固定历史和持久终端族仍是并行出口，行/列命题仍未无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 同参数稀疏供需严格余量攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_parameter_sparse_margin_internal_reduction_closed={fmt_bool(result['same_parameter_sparse_margin_internal_reduction_closed'])}",
        f"cold_supply_same_parameter_numeric_envelope_proved={fmt_bool(result['cold_supply_same_parameter_numeric_envelope_proved'])}",
        f"same_parameter_sparse_demand_cold_supply_strict_margin_proved={fmt_bool(result['same_parameter_sparse_demand_cold_supply_strict_margin_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 字段表",
        "",
        "| field | status | meaning |",
        "|---|---|---|",
    ]
    for item in result["margin_fields"]:
        lines.append(
            "| "
            f"`{table_cell(item['field'])}` | "
            f"`{table_cell(item['status'])}` | "
            f"{table_cell(item['meaning'])} |"
        )

    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['gate'])}` | "
            f"`{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | "
            f"{table_cell(item['meaning'])} | "
            f"`{table_cell(item['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
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
            "## 证据哈希",
            "",
            "| file | sha256 |",
            "|---|---|",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
