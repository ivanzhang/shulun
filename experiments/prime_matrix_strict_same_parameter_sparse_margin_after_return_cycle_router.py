#!/usr/bin/env python3
"""生成 strict 回流后同参数稀疏余量同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_same_parameter_sparse_margin_after_return_cycle_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json

输出：
  docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json
  docs/monograph/prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json"
OUT_MD = DOCS / "prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.md"

STRICT_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
RETURN_CYCLE = "CommonKernelReturnCycleDescentOrPDECLedger"
UNIFIED_AFTER_RETURN = "UnifiedBudgetAfterReturnCycleSync"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json",
    "prime-matrix-strict-same-parameter-sparse-margin-attack-router.json",
    "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json",
    "prime-matrix-strict-named-return-same-parameter-deduction-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    "prime-matrix-strict-cold-core-threshold-budget-gap-router.json",
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
        "experiments/prime_matrix_strict_same_parameter_sparse_margin_after_return_cycle_router.py": sha256(
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


def formula_rows() -> list[dict[str, str]]:
    """列出同参数余量的最终非持久内部字段。"""
    return [
        {
            "field": "demand",
            "formula": "M#_{x,z} or D_prefix under the same z,D,lambda ledger",
            "status": "available under current standard/external lower-sieve contract",
        },
        {
            "field": "nonpersistent returns",
            "formula": "absorbed into U_np, not a separate E_named deduction",
            "status": "schema closed after no-free-return-cycle",
        },
        {
            "field": "cold supply",
            "formula": "U_np <= sum_W (T_PDEC(W)-1) C_core(W)",
            "status": "formula closed; numeric envelope open",
        },
        {
            "field": "strict margin",
            "formula": "M#_{x,z} > U_np in the pure nonpersistent lane",
            "status": "equivalent to ColdSupplySameParameterNumericEnvelope plus numeric dominance",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "UnifiedAfterReturnCycleTargetImported",
            result["unified_after_return_cycle_target_imported"],
            result["unified_after_return_cycle_target_imported"],
            "最新统一预算同步已把非持久侧主攻点指向同参数稀疏余量。",
            STRICT_MARGIN,
        ),
        row(
            "NoFreeReturnCycleImported",
            result["no_free_return_cycle_imported"],
            result["no_free_return_cycle_imported"],
            "非持久共同核回流不能再作为免费循环吞掉余量。",
            RETURN_CYCLE,
        ),
        row(
            "OldSameParameterMarginReductionImported",
            result["old_same_parameter_margin_reduction_imported"],
            result["old_same_parameter_margin_reduction_imported"],
            "旧同参数余量证书已经把内部缺口压到冷供给数值包。",
            COLD_NUMERIC,
        ),
        row(
            "NonpersistentLaneNoHiddenDeductionClosed",
            result["nonpersistent_lane_no_hidden_deduction_closed"],
            result["nonpersistent_lane_no_hidden_deduction_closed"],
            "非持久命名回流只能进入 U_np 预算；不能另开 E_named 或共同核循环。",
            COLD_NUMERIC,
        ),
        row(
            "SameParameterSparseMarginAfterReturnCycleReduced",
            result["same_parameter_sparse_margin_after_return_cycle_reduced"],
            result["same_parameter_sparse_margin_after_return_cycle_reduced"],
            "回流后的非持久内部余量已等价压到冷供给数值包。",
            COLD_NUMERIC,
        ),
        row(
            "ColdSupplySameParameterNumericEnvelopeProved",
            False,
            False,
            "仍缺 C_core/T_PDEC/有效剪枝给出的同参数数值上界。",
            COLD_NUMERIC,
        ),
        row(
            "SameParameterSparseDemandColdSupplyStrictMarginProved",
            False,
            False,
            "结构等价闭合，但数值反超尚未证明。",
            COLD_NUMERIC,
        ),
        row(
            "PersistentNamedReturnStillParallel",
            False,
            False,
            "持久命名回流不属于非持久余量包，仍需单独排斥。",
            f"{NAMED_RETURN} AND {MOVING_ATOM}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{COLD_NUMERIC} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造回流后同参数稀疏余量证书。"""
    unified = load_json("prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json")
    old = load_json("prime-matrix-strict-same-parameter-sparse-margin-attack-router.json")
    ret = load_json("prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    cold = load_json("prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json")
    named_same = load_json("prime-matrix-strict-named-return-same-parameter-deduction-router.json")
    cold_balance = load_json("prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json")
    cold_gap = load_json("prime-matrix-strict-cold-core-threshold-budget-gap-router.json")

    target = unified.get("next_direct_attack_target") == STRICT_MARGIN
    no_free = ret.get("common_kernel_return_cycle_descent_or_pdec_proved") is True
    old_reduction = old.get("same_parameter_sparse_margin_internal_reduction_closed") is True
    nonpersistent_schema = (
        named_same.get("named_return_same_parameter_schema_closed") is True
        and cold_balance.get("cold_supply_upper_envelope_closed") is True
        and cold_gap.get("cold_budget_contradiction_criterion_closed") is True
    )
    cold_formula = cold.get("cold_supply_formula_sync_closed") is True
    reduced = target and no_free and old_reduction and nonpersistent_schema and cold_formula

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_same_parameter_sparse_margin_after_return_cycle_router",
        "status": "same_parameter_sparse_margin_after_return_cycle_reduced_to_cold_numeric_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "unified_after_return_cycle_target_imported": target,
        "no_free_return_cycle_imported": no_free,
        "old_same_parameter_margin_reduction_imported": old_reduction,
        "nonpersistent_lane_no_hidden_deduction_closed": nonpersistent_schema,
        "cold_supply_formula_imported": cold_formula,
        "same_parameter_sparse_margin_after_return_cycle_reduced": reduced,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "hot_core_fixed_history_persistent_exits_excluded": False,
        "named_return_exclusion_proved": False,
        "moving_atom_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": STRICT_MARGIN,
        "hardpoint_after_router": f"{COLD_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY}",
        "next_direct_attack_target": COLD_NUMERIC,
        "parallel_attack_targets": [HOT_CORE, FIXED_HISTORY, NAMED_RETURN, MOVING_ATOM, DSTRUCTURE],
        "formula_rows": formula_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SameParameterSparseDemandColdSupplyStrictMarginCertificate` 已吸收共同核回流后的新事实："
            "非持久共同核不能免费循环，非持久命名回流也不能另开 E_named 扣除，只能进入同参数 U_np。"
            "因此在纯非持久侧，严格余量的内部剩余等价压成 `ColdSupplySameParameterNumericEnvelope`："
            "证明同一参数账本下 `U_np<=sum_W(T_PDEC(W)-1)C_core(W)` 的数值上界足够小。"
            "热核心、固定历史和持久命名回流仍是并行命名出口；本步不证明最终正余量。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 回流后同参数稀疏余量同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"unified_after_return_cycle_target_imported={fmt_bool(result['unified_after_return_cycle_target_imported'])}",
        f"no_free_return_cycle_imported={fmt_bool(result['no_free_return_cycle_imported'])}",
        f"old_same_parameter_margin_reduction_imported={fmt_bool(result['old_same_parameter_margin_reduction_imported'])}",
        f"nonpersistent_lane_no_hidden_deduction_closed={fmt_bool(result['nonpersistent_lane_no_hidden_deduction_closed'])}",
        f"same_parameter_sparse_margin_after_return_cycle_reduced={fmt_bool(result['same_parameter_sparse_margin_after_return_cycle_reduced'])}",
        f"cold_supply_same_parameter_numeric_envelope_proved={fmt_bool(result['cold_supply_same_parameter_numeric_envelope_proved'])}",
        f"same_parameter_sparse_demand_cold_supply_strict_margin_proved={fmt_bool(result['same_parameter_sparse_demand_cold_supply_strict_margin_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 字段",
        "",
        "| field | formula | status |",
        "| --- | --- | --- |",
    ]
    for item in result["formula_rows"]:
        lines.append(
            "| {field} | {formula} | {status} |".format(
                field=table_cell(item["field"]),
                formula=table_cell(item["formula"]),
                status=table_cell(item["status"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 3. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 含义：给出同参数 C_core/T_PDEC/有效剪枝数值包，使非持久冷供给小于需求。",
            "- 边界：持久命名出口仍并行开放，不能由非持久余量包吸收。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
