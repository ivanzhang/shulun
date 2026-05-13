#!/usr/bin/env python3
"""生成 strict 冷窗口兄弟收费/热回流账本证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_window_sibling_charging_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.json
  docs/monograph/prime-matrix-strict-cold-window-sibling-charging-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-window-sibling-charging-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-window-sibling-charging-router.md"

SIBLING_CHARGING = "CanonicalColdWindowSiblingChargingOrHotReturnLedger"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json",
    "prime-matrix-strict-effective-pruning-latest-sync-router.json",
    "prime-matrix-strict-cold-core-threshold-dyadic-invariance-router.json",
    "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
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
        "experiments/prime_matrix_strict_cold_window_sibling_charging_router.py": sha256(
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


def ledger_rows() -> list[dict[str, str]]:
    """列出兄弟收费账本规则。"""
    return [
        {
            "rule": "sibling family",
            "definition": "children W=U*g sharing the same prefix U and residual frequency H_U",
            "effect": "all sibling cold charges are compared in one parameter ledger",
        },
        {
            "rule": "family cold",
            "definition": "sum_{W child of U} C_core(W) <= C_sib(U)",
            "effect": "the whole sibling family may remain in cold supply",
        },
        {
            "rule": "family hot return",
            "definition": "sum_{W child of U} C_core(W) > C_sib(U)",
            "effect": "the excess is not cold supply; it routes to hot core/PDEC/SAE",
        },
        {
            "rule": "overlap return",
            "definition": "same terminal core charged through multiple child windows",
            "effect": "overlap debt is registered as fixed-history or ColumnCRT return",
        },
        {
            "rule": "same-parameter discipline",
            "definition": "C_core(W), C_sib(U), and T_PDEC(W) use the same Lambda/PDEC ledger",
            "effect": "prevents optimizing local and family budgets under different parameters",
        },
    ]


def sample_rows() -> list[dict[str, Any]]:
    """展示局部冷到整族冷的收费区别。"""
    rows: list[dict[str, Any]] = []
    for child_count, parent_budget in [(4, 6), (8, 6), (8, 10), (16, 10)]:
        local_sum = child_count
        family_cold = local_sum <= parent_budget
        rows.append(
            {
                "child_count": child_count,
                "per_child_C_core": 1,
                "local_all_cold": True,
                "C_sib_parent": parent_budget,
                "family_charge": local_sum,
                "family_cold": family_cold,
                "registered_return": max(0, local_sum - parent_budget),
            }
        )
    return rows


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    ledger_closed = result["canonical_cold_window_sibling_charging_ledger_closed"]
    return [
        row(
            "SiblingChargingTargetImported",
            result["sibling_charging_target_imported"],
            False,
            "上一层已把终端反级联压成兄弟窗口收费账本。",
            SIBLING_CHARGING,
        ),
        row(
            "FamilyColdPredicateDefined",
            ledger_closed,
            ledger_closed,
            "同父前缀兄弟窗口必须整体比较 sum C_core。",
            SIBLING_CHARGING,
        ),
        row(
            "FamilyHotReturnRegistered",
            ledger_closed,
            ledger_closed,
            "整族收费超过 C_sib(U) 时不能继续进入冷供给。",
            f"{HOT_CORE} OR {FIXED_HISTORY}",
        ),
        row(
            "OverlapReturnRegistered",
            ledger_closed,
            ledger_closed,
            "重复收费同一终端核心会登记为固定历史/ColumnCRT 回流。",
            FIXED_HISTORY,
        ),
        row(
            "CanonicalColdWindowSiblingChargingClosed",
            ledger_closed,
            ledger_closed,
            "兄弟窗口从局部冷升级为整族收费/热回流二分。",
            SIBLING_NUMERIC,
        ),
        row(
            "SiblingNumericEnvelopeProved",
            False,
            False,
            "尚未给出 C_sib(U) 的同参数数值表或全局求和界。",
            SIBLING_NUMERIC,
        ),
        row(
            "TerminalColdWindowAntiCascadeProved",
            False,
            False,
            "收费账本闭合，但数值包、热核心和固定历史排斥仍未完成。",
            f"{SIBLING_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{SIBLING_NUMERIC} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造冷窗口兄弟收费账本证书。"""
    anticascade = load_json("prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json")
    target_imported = anticascade.get("canonical_cold_window_sibling_charging_isolated") is True
    ledger_closed = target_imported

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_cold_window_sibling_charging_router",
        "status": "cold_window_sibling_charging_ledger_closed_numeric_envelope_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "sibling_charging_target_imported": target_imported,
        "family_cold_predicate_defined": ledger_closed,
        "family_hot_return_registered": ledger_closed,
        "overlap_return_registered": ledger_closed,
        "canonical_cold_window_sibling_charging_ledger_closed": ledger_closed,
        "sibling_cold_core_threshold_numeric_envelope_proved": False,
        "terminal_cold_window_anticascade_proved": False,
        "effective_cold_history_pruning_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SIBLING_CHARGING,
        "hardpoint_after_router": (
            f"{SIBLING_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY} "
            f"AND {COLD_CORE_TABLE} AND {PDEC_TABLE}"
        ),
        "next_direct_attack_target": SIBLING_NUMERIC,
        "parallel_attack_targets": [
            HOT_CORE,
            FIXED_HISTORY,
            COLD_CORE_TABLE,
            PDEC_TABLE,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "ledger_rows": ledger_rows(),
        "sample_rows": sample_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`CanonicalColdWindowSiblingChargingOrHotReturnLedger` 可作为账本规则关闭："
            "同一父前缀 `U` 下，所有兄弟窗口不能只逐个检查局部冷，而必须整体比较 "
            "`sum_child C_core(W)` 与父级整族预算 `C_sib(U)`。若整族收费超出预算，超出部分"
            "必须回流热核心、固定历史或 PDEC/ColumnCRT；若同一终端核心被多个孩子重复收费，"
            "重叠债也必须登记为命名回流。这样反级联的逻辑出口闭合，但还没有给出 `C_sib(U)` "
            "的同参数数值表，所以终端反级联和行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 冷窗口兄弟收费/热回流账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sibling_charging_target_imported={fmt_bool(result['sibling_charging_target_imported'])}",
        f"family_cold_predicate_defined={fmt_bool(result['family_cold_predicate_defined'])}",
        f"family_hot_return_registered={fmt_bool(result['family_hot_return_registered'])}",
        f"overlap_return_registered={fmt_bool(result['overlap_return_registered'])}",
        f"canonical_cold_window_sibling_charging_ledger_closed={fmt_bool(result['canonical_cold_window_sibling_charging_ledger_closed'])}",
        f"sibling_cold_core_threshold_numeric_envelope_proved={fmt_bool(result['sibling_cold_core_threshold_numeric_envelope_proved'])}",
        f"terminal_cold_window_anticascade_proved={fmt_bool(result['terminal_cold_window_anticascade_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 账本规则",
        "",
        "| rule | definition | effect |",
        "|---|---|---|",
    ]
    for item in result["ledger_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['rule'])}` | "
            f"{table_cell(item['definition'])} | "
            f"{table_cell(item['effect'])} |"
        )

    lines.extend(
        [
            "",
            "## 样本收费",
            "",
            "| child count | per child C_core | local all cold | C_sib(parent) | family charge | family cold | registered return |",
            "|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["sample_rows"]:
        lines.append(
            "| "
            f"{item['child_count']} | "
            f"{item['per_child_C_core']} | "
            f"`{fmt_bool(item['local_all_cold'])}` | "
            f"{item['C_sib_parent']} | "
            f"{item['family_charge']} | "
            f"`{fmt_bool(item['family_cold'])}` | "
            f"{item['registered_return']} |"
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
    for item in result["decision_rows"]:
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
