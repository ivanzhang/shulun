#!/usr/bin/env python3
"""生成 strict 稀疏终端强制负载下界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_sparse_terminal_forced_load_lower_bound_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-sparse-terminal-forced-load-lower-bound-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.md",
    MONOGRAPH / "prime-matrix-strict-prefix-residual-transfer-router.md",
    MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.md",
    MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md",
]

TARGET = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
TERMINAL_PROJECTION = "PrefixObligationToSparseTerminalHistoryProjectionNoLossOrNamedReturn"
NORMALIZED_POTENTIAL = "NormalizedPrefixResidualPotentialLowerBound"
ANTICOLLAPSE = "PrefixLabelSupportToSparseTerminalHistoryAntiCollapse"
RETURN_EXCLUSION = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
FORCED_BEATS_SUPPLY = "ForcedTerminalLoadBeatsColdCoreNonpersistentSupply"
UNIFIED_FACTOR = "UnifiedContradictionFieldPrefixToTerminalLoadFactor"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def lemmas() -> list[dict[str, str]]:
    """列出本轮压缩出的负载下界引理。"""
    return [
        {
            "name": "prefix_weighted_obligation_source",
            "formula": "Assume EarlyZeroRowWithinP.  M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}.",
            "status": "imported_closed",
            "meaning": "早期零行把 prefix 残洞转成容量归一化的加权义务。",
        },
        {
            "name": "terminal_projection_accounting",
            "formula": "M#_{x,z} <= L_terminal + E_PDEC + E_SAE + E_ColumnCRT + E_hot + E_fixed + E_quotient.",
            "status": "closed_as_no_loss_accounting",
            "meaning": "义务沿历史递归进入终端；不能进入终端的质量必须以命名回流出现。",
        },
        {
            "name": "sparse_terminal_forced_load_criterion",
            "formula": "If all named returns vanish or are excluded, then L_forced >= M#_{x,z}.",
            "status": "closed_criterion",
            "meaning": "这给出从早期零行到稀疏终端负载的精确条件下界。",
        },
        {
            "name": "budget_gap_composition",
            "formula": "If M#_{x,z}-E_named > U_cold, then L_forced > U_cold.",
            "status": "closed_composition",
            "meaning": "把本轮负载下界直接接到冷核心供需矛盾口。",
        },
        {
            "name": "anticollapse_boundary",
            "formula": "Weighted mass does not yet imply enough distinct terminal history instances without anti-collapse.",
            "status": "open_boundary_named",
            "meaning": "仍需防止 prefix 标签支撑在 sparse terminal history 投影下塌缩。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "所有结论都在假设早期零行反例链内推导，不使用真实零行缺席。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "PrefixWeightedSourceImported",
            "closed": True,
            "proved": True,
            "meaning": "prefix 残洞选择子、容量乘子和 M# 加权义务已由前置路由闭合。",
            "remaining": NORMALIZED_POTENTIAL,
        },
        {
            "gate": "TerminalProjectionNoLossClosed",
            "closed": True,
            "proved": True,
            "meaning": "每个加权义务沿历史递归只有终端、热核心、固定历史、PDEC/SAE/ColumnCRT 或 quotient 回流几类出口。",
            "remaining": TERMINAL_PROJECTION,
        },
        {
            "gate": "ForcedLoadCriterionClosed",
            "closed": True,
            "proved": True,
            "meaning": "若命名回流被排斥，则 L_forced 至少为 M# 的未回流部分。",
            "remaining": f"{NORMALIZED_POTENTIAL} AND {RETURN_EXCLUSION}",
        },
        {
            "gate": "TerminalHistoryAntiCollapseOpen",
            "closed": False,
            "proved": False,
            "meaning": "加权质量还不能自动变成足够多的不同 sparse terminal history 实例。",
            "remaining": ANTICOLLAPSE,
        },
        {
            "gate": "SparseTerminalForcedLoadLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 M# 足够大、命名回流可排斥、且终端历史投影不塌缩。",
            "remaining": f"{NORMALIZED_POTENTIAL} AND {ANTICOLLAPSE} AND {RETURN_EXCLUSION}",
        },
        {
            "gate": "ColdCoreBudgetContradictionReached",
            "closed": False,
            "proved": False,
            "meaning": "尚未得到 L_forced>U_cold，因此冷核心供需矛盾尚未最终触发。",
            "remaining": FORCED_BEATS_SUPPLY,
        },
        {
            "gate": "UnifiedFieldFactorRegistered",
            "closed": True,
            "proved": False,
            "meaning": "prefix 到终端负载的无损/回流因子已接入统一矛盾场，但还不是终局矛盾。",
            "remaining": UNIFIED_FACTOR,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_sparse_terminal_forced_load_lower_bound_router",
        "status": "forced_load_lower_bound_reduced_to_normalized_prefix_potential_terminal_anticollapse_named_return_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "prefix_weighted_source_imported": True,
        "terminal_projection_no_loss_or_named_return_closed": True,
        "forced_load_criterion_closed": True,
        "budget_gap_composition_closed": True,
        "unified_field_prefix_to_terminal_load_factor_registered": True,
        "normalized_prefix_potential_lower_bound_proved": False,
        "terminal_history_anticollapse_proved": False,
        "named_return_exclusion_proved": False,
        "sparse_terminal_forced_load_lower_bound_proved": False,
        "forced_terminal_load_beats_cold_supply_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NORMALIZED_POTENTIAL,
        "parallel_attack_targets": [ANTICOLLAPSE, RETURN_EXCLUSION, FORCED_BEATS_SUPPLY, UNIFIED_FACTOR],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "早期零行强制负载下界已被压成一个守恒型不等式：prefix 残洞经容量乘子归一化后形成 "
            "M#_{x,z}，这些加权义务沿固定商型/历史递归要么进入 sparse terminal history，"
            "要么以 PDEC、SAE、ColumnCRT、热核心、固定历史或 quotient/reuse 的命名方式回流。"
            "因此 L_forced 至少等于 M# 扣除命名回流后的质量。真正未闭合的是 M# 的全局正下界、"
            "终端历史投影抗塌缩，以及命名回流排斥；这些完成后才能触发 L_forced>U_cold。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 稀疏终端强制负载下界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prefix_weighted_source_imported={fmt_bool(result['prefix_weighted_source_imported'])}",
        f"terminal_projection_no_loss_or_named_return_closed={fmt_bool(result['terminal_projection_no_loss_or_named_return_closed'])}",
        f"forced_load_criterion_closed={fmt_bool(result['forced_load_criterion_closed'])}",
        f"budget_gap_composition_closed={fmt_bool(result['budget_gap_composition_closed'])}",
        f"unified_field_prefix_to_terminal_load_factor_registered={fmt_bool(result['unified_field_prefix_to_terminal_load_factor_registered'])}",
        f"normalized_prefix_potential_lower_bound_proved={fmt_bool(result['normalized_prefix_potential_lower_bound_proved'])}",
        f"terminal_history_anticollapse_proved={fmt_bool(result['terminal_history_anticollapse_proved'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"sparse_terminal_forced_load_lower_bound_proved={fmt_bool(result['sparse_terminal_forced_load_lower_bound_proved'])}",
        f"forced_terminal_load_beats_cold_supply_proved={fmt_bool(result['forced_terminal_load_beats_cold_supply_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 负载守恒式",
        "",
        "在假设早期零行存在时，prefix 残洞给出",
        "",
        "```text",
        "M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}.",
        "```",
        "",
        "沿历史递归与终端投影，有无损账本",
        "",
        "```text",
        "M#_{x,z} <= L_terminal",
        "          + E_PDEC + E_SAE + E_ColumnCRT",
        "          + E_hot + E_fixed + E_quotient.",
        "```",
        "",
        "所以若命名回流都被排斥或被上游终端门吸收，则",
        "",
        "```text",
        "L_forced >= M#_{x,z}.",
        "```",
        "",
        "更一般地，可用",
        "",
        "```text",
        "L_forced >= M#_{x,z}-E_named.",
        "```",
        "",
        "与冷核心供给上界合成：",
        "",
        "```text",
        "M#_{x,z}-E_named > U_cold  ==>  L_forced > U_cold.",
        "```",
        "",
        "## 2. 引理表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["lemmas"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    table_cell(row["formula"]),
                    f"`{table_cell(row['status'])}`",
                    table_cell(row["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步闭合 prefix 加权义务到 sparse terminal load 的无损/命名回流账本；"
            "尚未证明归一化 prefix 势足够大、终端历史投影抗塌缩或命名回流全部可排斥。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    MONOGRAPH.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
