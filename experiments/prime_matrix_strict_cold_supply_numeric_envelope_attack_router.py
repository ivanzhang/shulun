#!/usr/bin/env python3
"""生成 strict 冷供给同参数数值包攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_supply_numeric_envelope_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json
  docs/monograph/prime-matrix-strict-cold-supply-numeric-envelope-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-same-parameter-sparse-margin-attack-router.json",
    "prime-matrix-strict-cold-core-threshold-budget-gap-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    "prime-matrix-strict-iterated-threshold-collapse-router.json",
    "prime-matrix-strict-iterated-scaled-core-density-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
]

COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
DEPTH_CAP = "SameParameterColdHistoryEffectiveDepthCap"
CORE_CAP_TABLE = "ColdCoreThresholdFunctionNumericTable"
PERSISTENCE_TABLE = "SameParameterPDECThresholdNumericTable"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43


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
        "experiments/prime_matrix_strict_cold_supply_numeric_envelope_attack_router.py": sha256(
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


def crude_growth_rows() -> list[dict[str, Any]]:
    """给出粗历史包的增长审计。"""
    rows = []
    for lam in [1, 2, 4]:
        alphabet = 8 * lam * lam
        exponent = math.log(alphabet, 2)
        rows.append(
            {
                "lambda_floor": lam,
                "alphabet_cap_per_layer": alphabet,
                "full_depth_R_log2P_history_exponent": exponent,
                "demand_exponent_alpha": ALPHA,
                "beats_demand_by_crude_count": exponent < ALPHA,
            }
        )
    return rows


def component_rows() -> list[dict[str, str]]:
    """列出冷供给数值包的不可缺字段。"""
    return [
        {
            "component": "history_count",
            "current_formula": "sum_{r<=R} prod_{i<=r} A_{Lambda_i}, A_{Lambda_i}<=8Lambda_i^2",
            "attack_result": "crude full-depth envelope is too large",
            "next": DEPTH_CAP,
        },
        {
            "component": "cold_core_capacity",
            "current_formula": "C_core(W) bounds N_{H_W}(I_W) in the cold branch",
            "attack_result": "formula exists but no same-parameter numeric table",
            "next": CORE_CAP_TABLE,
        },
        {
            "component": "persistence_threshold",
            "current_formula": "nonpersistent allowance is (T_PDEC(W)-1)C_core(W)",
            "attack_result": "threshold tradeoff is disciplined but not numeric",
            "next": PERSISTENCE_TABLE,
        },
        {
            "component": "large or incompatible histories",
            "current_formula": "hot window or fixed-history recurrence must return to named exits",
            "attack_result": "this is the only way to shrink the crude sum without cheating",
            "next": PRUNING,
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成冷供给数值包判定表。"""
    sparse_margin = data["sparse_margin"]
    cold_gap = data["cold_gap"]
    cold_balance = data["cold_balance"]
    threshold = data["threshold"]
    density = data["density"]
    scaled = data["scaled"]

    target_imported = sparse_margin.get("next_direct_attack_target") == COLD_NUMERIC
    formula_closed = (
        cold_gap.get("cold_supply_upper_bound_closed") is True
        and cold_gap.get("history_sum_envelope_closed") is True
        and cold_balance.get("cold_supply_upper_envelope_closed") is True
    )
    discipline_closed = (
        cold_balance.get("same_parameter_lambda_schedule_closed") is True
        and cold_balance.get("adaptive_lambda_no_free_lunch_dichotomy_closed") is True
    )
    product_ledger = (
        threshold.get("collapse_inequality_closed") is True
        and density.get("density_loss_product_ledger_closed") is True
    )
    cold_hot_split = scaled.get("cold_hot_split_closed") is True

    return [
        row(
            "ColdNumericTargetImported",
            target_imported,
            False,
            "上一层已把纯非持久内部缺口压成冷供给同参数数值包。",
            COLD_NUMERIC,
        ),
        row(
            "ColdSupplyFormulaClosed",
            formula_closed,
            True,
            "U_np 的求和公式和历史数粗包已经闭合。",
            COLD_NUMERIC,
        ),
        row(
            "SameParameterDisciplineClosed",
            discipline_closed,
            True,
            "Lambda/PDEC 阈值不能自由调参；调参成本已锁入同一账本。",
            COLD_NUMERIC,
        ),
        row(
            "IteratedProductLedgerImported",
            product_ledger,
            True,
            "历史深度和字母表损耗由 prod A_Lambda 显式登记。",
            PRUNING,
        ),
        row(
            "ColdHotSplitImported",
            cold_hot_split,
            True,
            "单历史容量已拆成冷窗口或热核心回流。",
            f"{CORE_CAP_TABLE} OR {HOT_CORE}",
        ),
        row(
            "CrudeFullDepthHistoryEnvelopeRejected",
            True,
            True,
            "只用 full-depth 历史数粗包，增长阶远大于 alpha=0.43 的需求阶，不能证明数值反超。",
            PRUNING,
        ),
        row(
            "EffectiveColdHistoryPruningProved",
            False,
            False,
            "尚未证明大多数形式历史因除数窗口不兼容、LCM 高度、热核心或固定历史而退出冷供给。",
            PRUNING,
        ),
        row(
            "ColdCoreThresholdNumericTableProved",
            False,
            False,
            "尚未给出同参数 C_core(W) 的可求和数值表。",
            CORE_CAP_TABLE,
        ),
        row(
            "PDECThresholdNumericTableProved",
            False,
            False,
            "尚未给出同参数 T_PDEC(W) 的数值表。",
            PERSISTENCE_TABLE,
        ),
        row(
            "ColdSupplySameParameterNumericEnvelopeProved",
            False,
            False,
            "冷供给公式闭合，但有效剪枝、C_core 表、T_PDEC 表都未完成。",
            f"{PRUNING} AND {CORE_CAP_TABLE} AND {PERSISTENCE_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{PRUNING} AND {HOT_CORE} AND {FIXED_HISTORY} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造冷供给数值包攻坚证书。"""
    data = {
        "sparse_margin": load_json("prime-matrix-strict-same-parameter-sparse-margin-attack-router.json"),
        "cold_gap": load_json("prime-matrix-strict-cold-core-threshold-budget-gap-router.json"),
        "cold_balance": load_json("prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"),
        "threshold": load_json("prime-matrix-strict-iterated-threshold-collapse-router.json"),
        "density": load_json("prime-matrix-strict-iterated-scaled-core-density-router.json"),
        "scaled": load_json("prime-matrix-strict-scaled-terminal-core-divisor-window-router.json"),
    }
    rows = build_rows(data)
    formula_sync_closed = all(
        any(item["gate"] == gate and item["closed"] for item in rows)
        for gate in [
            "ColdNumericTargetImported",
            "ColdSupplyFormulaClosed",
            "SameParameterDisciplineClosed",
            "IteratedProductLedgerImported",
            "ColdHotSplitImported",
            "CrudeFullDepthHistoryEnvelopeRejected",
        ]
    )

    return {
        "certificate_type": "prime_matrix_strict_cold_supply_numeric_envelope_attack_router",
        "status": "cold_supply_numeric_envelope_reduced_to_effective_pruning_and_numeric_tables_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "cold_supply_formula_sync_closed": formula_sync_closed,
        "crude_full_depth_history_envelope_rejected_as_sufficient": True,
        "effective_cold_history_pruning_proved": False,
        "cold_core_threshold_numeric_table_proved": False,
        "pdec_threshold_numeric_table_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": COLD_NUMERIC,
        "hardpoint_after_router": f"{PRUNING} AND {CORE_CAP_TABLE} AND {PERSISTENCE_TABLE}",
        "next_direct_attack_target": PRUNING,
        "parallel_attack_targets": [
            CORE_CAP_TABLE,
            PERSISTENCE_TABLE,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "crude_growth_rows": crude_growth_rows(),
        "component_rows": component_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ColdSupplySameParameterNumericEnvelope` 不能由现有粗历史数包直接闭合。"
            "虽然 U_np<=sum_W(T_PDEC(W)-1)C_core(W) 和 Lambda/PDEC 调参纪律已经闭合，"
            "但 full-depth 历史数上界 `sum prod A_Lambda` 太宽：即使按最粗常数 Lambda=1，"
            "深度 R≈log_2 P 时也给出约 P^3 级别的历史包，远大于 alpha=0.43 的需求阶。"
            "因此下一真正硬点不是再调一个常数，而是证明有效冷历史剪枝：大多数形式历史必须因"
            "除数窗口不兼容、LCM 高度、热核心或固定历史回流而退出冷供给；同时还要给出 C_core 与 "
            "T_PDEC 的同参数数值表。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 冷供给同参数数值包攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cold_supply_formula_sync_closed={fmt_bool(result['cold_supply_formula_sync_closed'])}",
        f"crude_full_depth_history_envelope_rejected_as_sufficient={fmt_bool(result['crude_full_depth_history_envelope_rejected_as_sufficient'])}",
        f"effective_cold_history_pruning_proved={fmt_bool(result['effective_cold_history_pruning_proved'])}",
        f"cold_supply_same_parameter_numeric_envelope_proved={fmt_bool(result['cold_supply_same_parameter_numeric_envelope_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 粗包增长审计",
        "",
        "| lambda_floor | alphabet_cap_per_layer | full_depth_R_log2P_history_exponent | demand_exponent_alpha | beats_demand_by_crude_count |",
        "|---:|---:|---:|---:|---:|",
    ]
    for item in result["crude_growth_rows"]:
        lines.append(
            "| "
            f"{item['lambda_floor']} | "
            f"{item['alphabet_cap_per_layer']} | "
            f"{item['full_depth_R_log2P_history_exponent']:.6f} | "
            f"{item['demand_exponent_alpha']:.6f} | "
            f"`{fmt_bool(item['beats_demand_by_crude_count'])}` |"
        )

    lines.extend(
        [
            "",
            "## 组件表",
            "",
            "| component | current_formula | attack_result | next |",
            "|---|---|---|---|",
        ]
    )
    for item in result["component_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['component'])}` | "
            f"{table_cell(item['current_formula'])} | "
            f"{table_cell(item['attack_result'])} | "
            f"`{table_cell(item['next'])}` |"
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
