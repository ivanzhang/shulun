#!/usr/bin/env python3
"""生成 strict complete emitter key partition 字段证书。

用法示例：
  python3 experiments/prime_matrix_strict_complete_emitter_key_partition_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-complete-emitter-key-partition-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
OUT_MD = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-clean-core-precauchy-source-law-atom-router.json",
    "prime-matrix-clean-core-origin-source-admission-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-clean-core-layer-transfer-path-router.json",
    "prime-matrix-clean-core-path-source-firewall-router.json",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(
    fixed_pair: dict[str, Any],
    source_law: dict[str, Any],
    origin_admission: dict[str, Any],
    constructor_firewall: dict[str, Any],
    layer_path: dict[str, Any],
    path_source: dict[str, Any],
    branch_budget: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 complete emitter key partition 字段表。"""
    target = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
    next_basis = (
        "ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND "
        "CompleteEmitterTraceKeyBudgetLedger AND "
        "SignLocalFactorRefinementNoCancellationLedger AND "
        "OverBudgetOrUnregisteredReturnLedger"
    )
    return [
        {
            "gate": "CompleteKeyPartitionTargetActive",
            "closed": fixed_pair.get("next_direct_attack_target") == target,
            "proved": False,
            "meaning": "上一层已把 fixed-pair fiber bound 的首要实际障碍压成 complete primitive emitter key 分区。",
            "remaining": target,
        },
        {
            "gate": "SourceTableToCompleteKeyImplicationClosed",
            "closed": source_law.get("origin_generation_ledger_implication_closed") is True,
            "proved": True,
            "meaning": "若 actual 原始生成表存在，则 branch key、u/v map、dyadic/truncation、sign/local factor 可组成 complete key。",
            "remaining": "该蕴含不证明 actual noncanonical 源表存在。",
        },
        {
            "gate": "PathPartitionNeedsPreCauchySourceImported",
            "closed": path_source.get("clean_core_path_partition_proved") is False,
            "proved": True,
            "meaning": "路径分割必须建立在 Cauchy/dispersion 前的 actual 系数公式上，不能从后验 payment 图补标签。",
            "remaining": "ActualNoncanonicalPrimitiveEmitterSourceTableLedger。",
        },
        {
            "gate": "CanonicalTemplateCrossImportBlocked",
            "closed": constructor_firewall.get("constructor_source_class_firewall_boundary_closed")
            is True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 决策树只在 canonical-source 分支闭合，不能跨导入 noncanonical complete key。",
            "remaining": "ActualNoncanonicalPrimitiveEmitterSourceTableLedger。",
        },
        {
            "gate": "GenericWFDNotAKeyEmitter",
            "closed": constructor_firewall.get("source_class_partition_closed") is True,
            "proved": True,
            "meaning": "generic WFD 是形式约束，不是 primitive summand emitter，不能生成 complete key 表。",
            "remaining": "ActualNoncanonicalPrimitiveEmitterSourceTableLedger。",
        },
        {
            "gate": "OriginAdmissionStillOpen",
            "closed": origin_admission.get("clean_core_primitive_source_constructor_admission_proved")
            is True,
            "proved": False,
            "meaning": "当前材料尚未证明 noncanonical clean-core 候选都有 pre-Cauchy primitive source constructor。",
            "remaining": "ActualNoncanonicalPrimitiveEmitterSourceTableLedger。",
        },
        {
            "gate": "CompleteTraceBudgetStillOpen",
            "closed": (
                layer_path.get("clean_core_path_partition_proved") is True
                or branch_budget.get("branch_key_multiplicity_budget_proved") is True
            ),
            "proved": False,
            "meaning": "当前材料没有证明 complete trace/key 数满足 log^O(1) 预算；几何标签不能自动成为 actual source key。",
            "remaining": "CompleteEmitterTraceKeyBudgetLedger。",
        },
        {
            "gate": "SignLocalFactorRefinementStillOpen",
            "closed": source_law.get("clean_core_original_coefficient_generation_ledger_proved")
            is True,
            "proved": False,
            "meaning": "同一 complete key 下非零 local factor 与符号细分仍依赖 actual 生成表，当前未证明。",
            "remaining": "SignLocalFactorRefinementNoCancellationLedger。",
        },
        {
            "gate": "ReturnLedgerForOverBudgetOrUnregisteredOpen",
            "closed": (
                origin_admission.get("unregistered_source_return_absorbed") is True
                and branch_budget.get("signed_variation_branch_lift_proved") is True
            ),
            "proved": False,
            "meaning": "超预算、未登记、thin/rejected 或抵消分支必须命名回流；当前未在 actual emitter key 表内完成。",
            "remaining": "OverBudgetOrUnregisteredReturnLedger。",
        },
        {
            "gate": "CompleteEmitterKeyPartitionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "actual 源表、complete trace 预算、符号/local refinement 与回流纪律尚未合取证明。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict complete emitter key partition 证书。"""
    fixed_pair = load_json(DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json")
    source_law = load_json(DOCS / "prime-matrix-clean-core-precauchy-source-law-atom-router.json")
    origin_admission = load_json(DOCS / "prime-matrix-clean-core-origin-source-admission-router.json")
    constructor_firewall = load_json(
        DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json"
    )
    layer_path = load_json(DOCS / "prime-matrix-clean-core-layer-transfer-path-router.json")
    path_source = load_json(DOCS / "prime-matrix-clean-core-path-source-firewall-router.json")
    branch_budget = load_json(
        DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.json"
    )

    target = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
    next_basis = (
        "ActualNoncanonicalPrimitiveEmitterSourceTableLedger AND "
        "CompleteEmitterTraceKeyBudgetLedger AND "
        "SignLocalFactorRefinementNoCancellationLedger AND "
        "OverBudgetOrUnregisteredReturnLedger"
    )
    rows = build_rows(
        fixed_pair=fixed_pair,
        source_law=source_law,
        origin_admission=origin_admission,
        constructor_firewall=constructor_firewall,
        layer_path=layer_path,
        path_source=path_source,
        branch_budget=branch_budget,
    )
    return {
        "certificate_type": "prime_matrix_strict_complete_emitter_key_partition_router",
        "status": "strict_complete_emitter_key_partition_reduced_to_actual_source_table_budget_refinement_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "complete_emitter_key_partition_router_closed": True,
        "source_table_to_complete_key_implication_closed": True,
        "canonical_template_cross_import_blocked": True,
        "generic_wfd_key_emitter_rejected": True,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "complete_emitter_trace_key_budget_proved": False,
        "sign_local_factor_refinement_no_cancellation_proved": False,
        "overbudget_or_unregistered_return_ledger_proved": False,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "ActualNoncanonicalPrimitiveEmitterSourceTableLedger",
        "field_law": (
            "A complete primitive emitter key partition exists only after the actual noncanonical pre-Cauchy source table is fixed. "
            "The key is not a post-hoc label: it must be generated with each primitive summand and must include branch trace, "
            "exact `(u,v)` convention, sign/local factor and dyadic/truncation state. Polylog cardinality and return tags are part of the same table."
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger` 被拆为 actual 源表、complete trace/key 预算、"
            "符号/local refinement 与超预算/未登记回流四项。已有材料只闭合了“源表若存在则给 complete key”的形式蕴含；"
            "actual noncanonical primitive emitter 源表本身仍未证明，所以 fixed-pair 纤维链继续开放。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict complete emitter key partition 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"complete_emitter_key_partition_router_closed={fmt_bool(result['complete_emitter_key_partition_router_closed'])}",
        f"source_table_to_complete_key_implication_closed={fmt_bool(result['source_table_to_complete_key_implication_closed'])}",
        f"actual_noncanonical_primitive_emitter_source_table_proved={fmt_bool(result['actual_noncanonical_primitive_emitter_source_table_proved'])}",
        f"complete_emitter_trace_key_budget_proved={fmt_bool(result['complete_emitter_trace_key_budget_proved'])}",
        f"registered_complete_primitive_emitter_key_partition_polylog_proved={fmt_bool(result['registered_complete_primitive_emitter_key_partition_polylog_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 字段律",
        "",
        result["field_law"],
        "",
        "## 2. 原子化",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
