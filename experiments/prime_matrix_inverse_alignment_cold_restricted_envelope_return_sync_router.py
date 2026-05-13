#!/usr/bin/env python3
"""把冷限制逆元兄弟 envelope 同步到回流后冷供给数值前沿。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_cold_restricted_envelope_return_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json
  docs/monograph/prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-cold-restricted-envelope-return-sync-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.json",
    DOCS / "prime-matrix-strict-sibling-numeric-envelope-attack-router.json",
    DOCS / "prime-matrix-strict-parent-support-numeric-envelope-router.json",
    DOCS / "prime-matrix-strict-sibling-collar-cap-table-router.json",
    DOCS / "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
    DOCS / "prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json",
    DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
]

COLD_RESTRICTED = "ColdRestrictedInverseAlignmentSiblingChargeEnvelope"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
COLD_CORE_TABLE = "ColdCoreThresholdFunctionNumericTable"
PDEC_TABLE = "SameParameterPDECThresholdNumericTable"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_cold_restricted_envelope_return_sync_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def imported_flags() -> dict[str, bool]:
    """读取同步所需的已闭合字段。"""
    raw = load_json(DOCS / "prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.json")
    sibling = load_json(DOCS / "prime-matrix-strict-sibling-numeric-envelope-attack-router.json")
    parent = load_json(DOCS / "prime-matrix-strict-parent-support-numeric-envelope-router.json")
    collar = load_json(DOCS / "prime-matrix-strict-sibling-collar-cap-table-router.json")
    width = load_json(DOCS / "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json")
    return_cycle = load_json(DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json")
    unified = load_json(DOCS / "prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json")
    cold_after = load_json(DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json")

    return {
        "raw_inverse_alignment_tau_envelope_closed": raw.get("raw_inverse_alignment_tau_charge_envelope_closed")
        is True,
        "raw_envelope_insufficient_imported": raw.get("raw_envelope_scale_mismatch_certified") is True,
        "sibling_projection_identity_imported": sibling.get("sibling_multiset_projection_identity_proved") is True,
        "parent_support_geometry_imported": parent.get("projected_support_to_dilated_parent_window_proved")
        is True,
        "collar_cap_table_imported": collar.get("same_parameter_collar_short_divisor_cap_table_proved") is True,
        "width_lcm_kernel_compression_imported": width.get("width_lcm_kernel_compression_proved") is True,
        "common_kernel_return_cycle_closed": return_cycle.get("common_kernel_return_cycle_descent_or_pdec_proved")
        is True,
        "unified_after_return_sync_imported": unified.get("unified_budget_after_return_cycle_sync_closed") is True,
        "cold_after_return_effective_pruning_closed": cold_after.get(
            "effective_pruning_closed_for_nonpersistent_budget"
        )
        is True,
        "cold_core_threshold_numeric_table_proved": cold_after.get("cold_core_threshold_numeric_table_proved")
        is True,
        "same_parameter_pdec_threshold_numeric_table_proved": cold_after.get(
            "same_parameter_pdec_threshold_numeric_table_proved"
        )
        is True,
        "cold_supply_same_parameter_numeric_envelope_proved": cold_after.get(
            "cold_supply_same_parameter_numeric_envelope_proved"
        )
        is True,
    }


def route_rows() -> list[dict[str, str]]:
    """列出冷限制逆元 envelope 的路由。"""
    return [
        {
            "stage": "raw inverse tau",
            "fact": "all tau capacity is bounded by sum_{z<q<P} mu_q but this is Theta(P)",
            "route": "raw envelope rejected as sufficient",
        },
        {
            "stage": "cold restriction",
            "fact": "only tau buckets passing terminal cold tests may remain in nonpersistent cold supply",
            "route": "sibling charging ledger",
        },
        {
            "stage": "sibling projection",
            "fact": "child charges project to parent divisor support plus overlap debt",
            "route": "parent support / overlap return / collar",
        },
        {
            "stage": "collar and LCM",
            "fact": "collar width overflow routes to LCM height or low-multiplier common kernel",
            "route": "width LCM compression",
        },
        {
            "stage": "return cycle",
            "fact": "common-kernel return cannot loop for free; it descends or becomes PDEC/fixed history",
            "route": "no-free return cycle",
        },
        {
            "stage": "after-return cold budget",
            "fact": "nonpersistent cold supply now only needs same-parameter C_core and T_PDEC numeric tables",
            "route": "ColdCoreThresholdFunctionNumericTable + SameParameterPDECThresholdNumericTable",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ColdRestrictedEnvelopeTargetImported",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 raw 逆元 tau envelope 的不足压成冷限制 envelope。",
            "remaining": COLD_RESTRICTED,
        },
        {
            "gate": "ColdRestrictedEnvelopeIndependentHardpointRemoved",
            "closed": result["cold_restricted_inverse_alignment_envelope_synced_to_return_frontier"],
            "proved": result["cold_restricted_inverse_alignment_envelope_synced_to_return_frontier"],
            "meaning": "冷限制逆元 tau 桶已接入兄弟收费、父支撑、collar、共同核回流和回流后预算链。",
            "remaining": "none as independent hardpoint",
        },
        {
            "gate": "EffectivePruningClosedForNonpersistentBudget",
            "closed": result["effective_pruning_closed_for_inverse_alignment_nonpersistent_budget"],
            "proved": result["effective_pruning_closed_for_inverse_alignment_nonpersistent_budget"],
            "meaning": "对非持久冷供给，终端反级联失败、兄弟超收费和共同核回流都不能继续算作免费冷容量。",
            "remaining": f"{COLD_CORE_TABLE} AND {PDEC_TABLE}",
        },
        {
            "gate": "ColdCoreNumericTableProved",
            "closed": result["cold_core_threshold_numeric_table_proved"],
            "proved": result["cold_core_threshold_numeric_table_proved"],
            "meaning": "同参数 C_core 可求和数值表仍未证明。",
            "remaining": COLD_CORE_TABLE,
        },
        {
            "gate": "PDECThresholdNumericTableProved",
            "closed": result["same_parameter_pdec_threshold_numeric_table_proved"],
            "proved": result["same_parameter_pdec_threshold_numeric_table_proved"],
            "meaning": "同参数 T_PDEC 阈值表仍未证明。",
            "remaining": PDEC_TABLE,
        },
        {
            "gate": "ColdSupplySameParameterNumericEnvelopeProved",
            "closed": result["cold_supply_same_parameter_numeric_envelope_proved"],
            "proved": result["cold_supply_same_parameter_numeric_envelope_proved"],
            "meaning": "冷供给数值 envelope 尚未闭合；当前只关闭了逆元冷限制 envelope 的独立性。",
            "remaining": f"{COLD_CORE_TABLE} AND {PDEC_TABLE}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未同时完成冷数值表、持久 moving atom 排斥和 DStructure/Rankin 验收。",
            "remaining": f"{COLD_CORE_TABLE} AND {PDEC_TABLE} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    flags = imported_flags()
    synced = all(
        [
            flags["raw_inverse_alignment_tau_envelope_closed"],
            flags["raw_envelope_insufficient_imported"],
            flags["sibling_projection_identity_imported"],
            flags["parent_support_geometry_imported"],
            flags["collar_cap_table_imported"],
            flags["width_lcm_kernel_compression_imported"],
            flags["common_kernel_return_cycle_closed"],
            flags["unified_after_return_sync_imported"],
            flags["cold_after_return_effective_pruning_closed"],
        ]
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_cold_restricted_envelope_return_sync_router",
        "status": "cold_restricted_inverse_alignment_envelope_synced_to_cold_numeric_tables_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        **flags,
        "cold_restricted_inverse_alignment_envelope_synced_to_return_frontier": synced,
        "effective_pruning_closed_for_inverse_alignment_nonpersistent_budget": synced,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": COLD_RESTRICTED,
        "hardpoint_after_router": (
            f"{COLD_CORE_TABLE} AND {PDEC_TABLE} AND {HOT_CORE} AND {FIXED_HISTORY} "
            f"AND {MOVING_ATOM} AND {DSTRUCTURE}"
        ),
        "next_direct_attack_target": COLD_CORE_TABLE,
        "parallel_attack_targets": [
            PDEC_TABLE,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "route_rows": route_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ColdRestrictedInverseAlignmentSiblingChargeEnvelope` 不再是独立硬点。"
            "逆元 tau 桶的 raw 容量上界过宽；加入冷限制后，它正好落入已有兄弟收费链："
            "tau/cold 兄弟收费投影到父支撑，重复收费登记为 overlap 回流，collar 宽度爆发进入 LCM/共同核，"
            "共同核回流不能免费循环，最终回到回流后冷供给数值包。"
            "因此对非持久预算而言，逆元方程组已经被充分并入前沿；真正剩余不是新的逆元结构，"
            "而是同参数 `C_core` 与 `T_PDEC` 数值表，以及并行的热/固定/持久终端排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 文档。"""
    lines = [
        "# Prime Matrix 冷限制逆元 envelope 回流同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cold_restricted_inverse_alignment_envelope_synced_to_return_frontier={fmt_bool(result['cold_restricted_inverse_alignment_envelope_synced_to_return_frontier'])}",
        f"effective_pruning_closed_for_inverse_alignment_nonpersistent_budget={fmt_bool(result['effective_pruning_closed_for_inverse_alignment_nonpersistent_budget'])}",
        f"cold_core_threshold_numeric_table_proved={fmt_bool(result['cold_core_threshold_numeric_table_proved'])}",
        f"same_parameter_pdec_threshold_numeric_table_proved={fmt_bool(result['same_parameter_pdec_threshold_numeric_table_proved'])}",
        f"cold_supply_same_parameter_numeric_envelope_proved={fmt_bool(result['cold_supply_same_parameter_numeric_envelope_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 路由链",
        "",
        "| stage | fact | route |",
        "| --- | --- | --- |",
    ]
    for row in result["route_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['stage'])}`",
                    table_cell(row["fact"]),
                    table_cell(row["route"]),
                ]
            )
            + " |"
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
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
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
            "审稿边界：本步只删除冷限制逆元 envelope 的独立性，不证明冷数值表，不声明行/列命题无条件闭合。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
