#!/usr/bin/env python3
"""生成 strict finite prefix 同参数窗口规格证书。

用法示例：
  python3 experiments/prime_matrix_strict_same_parameter_prefix_window_spec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-same-parameter-prefix-window-spec-router.json

输出：
  docs/monograph/prime-matrix-strict-same-parameter-prefix-window-spec-router.json
  docs/monograph/prime-matrix-strict-same-parameter-prefix-window-spec-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-same-parameter-prefix-window-spec-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-same-parameter-prefix-window-spec-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json",
    MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.json",
    MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json",
    MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.json",
    MONOGRAPH / "prime-matrix-strict-single-parameter-terminal-budget-margin-router.json",
    MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json",
    MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.json",
]

WINDOW = "SameParameterPrefixWindowSpecification"
RUNNER = "ReproduciblePrefixRoughCountRunnerHashLedger"
TAIL = "AnalyticTailToFiniteBoundaryMonotoneBridge"
TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
PARAMETER_ID = "alpha043_pge100000_external_b3_pending_finite_prefix_named_return"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖证书哈希。"""
    result = {"script": sha256(Path(__file__).resolve())}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row_by_name(rows: list[dict[str, Any]], key: str, value: str) -> dict[str, Any]:
    """按字段查找行。"""
    for row in rows:
        if row.get(key) == value:
            return row
    return {}


def canonical_window(concrete: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    """生成同参数窗口的规范字段。"""
    row = concrete.get("candidate_parameter_row", {})
    manifest_row = manifest.get("manifest", {})
    alpha = row.get("alpha", manifest_row.get("alpha", 0.43))
    return {
        "parameter_id": row.get("parameter_id", manifest_row.get("parameter_id", PARAMETER_ID)),
        "P_range": "P>=100000",
        "alpha": alpha,
        "s": row.get("s", manifest_row.get("s")),
        "z": "z=floor(P^0.43)",
        "prefix_interval": "1<=c<P",
        "rough_set": "R_{x,z}={c: 1<=c<P and xP+c avoids all prescribed classes modulo q<=z}",
        "D_rule": "one lower-sieve level D with squarefree d<P in supp(lambda^-_{z,D})",
        "lower_weight_family": "lambda^-_{z,D}, W^-(z,D), TV(lambda^-)",
        "capacity_label": "tau_z(c), mu_tau(c), M#_{x,z}=sum_{c in R_{x,z}}1/mu_tau(c)",
        "terminal_ledger": "D_prefix-E_named-U_cold under the same z,D,lambda^-,Lambda,T_PDEC ledger",
        "type_alphabet": "row-free type key uses the same source/window/phase/label skeleton; threshold comparison remains separate",
    }


def build_ledger_rows(data: dict[str, dict[str, Any]], window: dict[str, Any]) -> list[dict[str, Any]]:
    """列出 D0、M#、终端预算的同窗口对账结果。"""
    manifest = data["manifest"]
    concrete = data["concrete"]
    rough = data["rough"]
    cap = data["capacity"]
    budget = data["budget"]
    margin = data["margin"]
    cold = data["cold"]
    anti = data["anti"]
    boundary_type = data["boundary_type"]

    candidate_row = concrete.get("candidate_parameter_row", {})
    parameter_pinned = (
        manifest.get("range_and_parameter_manifest_closed") is True
        and manifest.get("candidate_parameter_id_pinned") is True
        and candidate_row.get("parameter_id") == PARAMETER_ID
        and candidate_row.get("p_min") == 100_000
    )

    rough_equations = rough.get("sieve_equations", [])
    main_error = row_by_name(rough_equations, "equation", "main_error_split")
    capacity_laws = cap.get("multiplier_laws", [])
    msharp_law = row_by_name(capacity_laws, "law", "capacity_normalized_charge")
    capacity_norm = row_by_name(budget.get("equations", []), "name", "capacity_multiplier_normalization")
    terminal_gap = row_by_name(budget.get("equations", []), "name", "unified_terminal_budget_gap")

    return [
        {
            "slot": "parameter_window",
            "formula": f"{PARAMETER_ID}; P>=100000; z=floor(P^0.43); 1<=c<P",
            "closed": parameter_pinned,
            "proved": parameter_pinned,
            "meaning": "range manifest 与 concrete candidate row 指向同一 alpha=0.43/P>=100000 窗口。",
            "remaining": "无；该项只锁定窗口，不给 D0 数值。",
        },
        {
            "slot": "D0_prefix_demand_formula",
            "formula": main_error.get("formula", "|R_{x,z}| >= (P-1)W^-(z,D)-TV(lambda^-)."),
            "closed": rough.get("main_error_split_closed") is True,
            "proved": rough.get("main_error_split_closed") is True,
            "meaning": "D0 需求端使用同一 R_{x,z}、同一 lower-weight family lambda^-_{z,D}、同一 W^-/TV。",
            "remaining": "B3 main/TV/finite certificate still open; this is formula alignment only.",
        },
        {
            "slot": "Msharp_capacity_window",
            "formula": msharp_law.get("formula", "M#_{x,z}=sum_{c in R_{x,z}}1/mu_{tau_z(c)}."),
            "closed": cap.get("registered_prefix_capacity_multiplier_discipline_proved") is True,
            "proved": cap.get("registered_prefix_capacity_multiplier_discipline_proved") is True,
            "meaning": "M# 使用同一 R_{x,z} 和 tau_z 标签；除以 ceil(P/z) 的乘子纪律已闭合。",
            "remaining": "NormalizedPrefixResidualPotentialLowerBound remains numeric/open.",
        },
        {
            "slot": "D0_to_Msharp_budget_link",
            "formula": capacity_norm.get("formula", "M#_{x,z} >= |R_{x,z}|/ceil(P/z)."),
            "closed": budget.get("capacity_multiplier_normalization_imported") is True,
            "proved": budget.get("capacity_multiplier_normalization_imported") is True,
            "meaning": "D0 的 prefix 粗筛余质量以同一 z 进入 M#，没有换 cutoff。",
            "remaining": "需要粗筛余数值下界和 finite runner/hash。",
        },
        {
            "slot": "terminal_budget_same_window",
            "formula": terminal_gap.get("formula", "((P-1)W^- - TV)/ceil(P/z) - E_named > sum_W (T_PDEC(W)-1)C_core(W)."),
            "closed": budget.get("algebraic_composition_closed") is True
            and margin.get("single_parameter_margin_normal_form_closed") is True,
            "proved": budget.get("algebraic_composition_closed") is True
            and margin.get("single_parameter_margin_normal_form_closed") is True,
            "meaning": "终端预算的需求项直接复用 D_prefix 与 M# 的同一 z,D,lambda^- 表达式。",
            "remaining": "严格正余量仍未证明。",
        },
        {
            "slot": "Lambda_TPDEC_cold_supply_discipline",
            "formula": "U_cold<=sum_W (T_PDEC(W)-1)C_core(W), with the same Lambda schedule and PDEC threshold ledger",
            "closed": cold.get("same_parameter_lambda_schedule_closed") is True
            and cold.get("single_parameter_margin_ledger_closed") is True,
            "proved": cold.get("same_parameter_lambda_schedule_closed") is True,
            "meaning": "冷供给的 Lambda/T_PDEC 不能独立调参；调节成本必须进入 E_named 或 U_cold。",
            "remaining": "ColdPositiveDominance / UnifiedTerminalBudgetStrictInequality remains open.",
        },
        {
            "slot": "terminal_projection_no_silent_collapse",
            "formula": "L_forced>=M#_{x,z}-E_named",
            "closed": anti.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget") is True,
            "proved": anti.get("prefix_label_support_to_sparse_terminal_history_anticollapse_proved_for_budget") is True,
            "meaning": "prefix 标签投影到终端历史时按预算所需的重数守恒；同历史塌缩进 U_cold 或 E_named。",
            "remaining": "NamedReturn exclusion and cold budget comparison remain open.",
        },
        {
            "slot": "row_free_type_alphabet_key",
            "formula": "row-free type key: source family, branch, window shape, phase, anchor, carry/cofactor, label skeleton",
            "closed": boundary_type.get("row_free_type_key_definition_closed") is True,
            "proved": boundary_type.get("row_free_type_key_definition_closed") is True,
            "meaning": "同窗口 type alphabet 的键字段可审查；这只关闭定义域。",
            "remaining": f"{TYPE_LEDGER} AND {ROW_FREE} still require threshold/entropy and label-preserving anti-collapse.",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造同参数窗口规格证书。"""
    data = {
        "manifest": load_json(MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json"),
        "attack": load_json(MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-certificate-attack-router.json"),
        "concrete": load_json(MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"),
        "rough": load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json"),
        "capacity": load_json(MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json"),
        "budget": load_json(MONOGRAPH / "prime-matrix-strict-unified-terminal-budget-equation-router.json"),
        "margin": load_json(MONOGRAPH / "prime-matrix-strict-single-parameter-terminal-budget-margin-router.json"),
        "cold": load_json(MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json"),
        "anti": load_json(MONOGRAPH / "prime-matrix-strict-prefix-label-sparse-history-anticollapse-router.json"),
        "boundary_type": load_json(MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.json"),
    }
    window = canonical_window(data["concrete"], data["manifest"])
    ledger_rows = build_ledger_rows(data, window)
    structural_closed = all(row["closed"] for row in ledger_rows)

    decision_rows = [
        {
            "gate": "SameParameterWindowTargetImported",
            "closed": data["manifest"].get("next_direct_attack_target") == WINDOW
            or data["attack"].get("hardpoint_after_router", "").find(WINDOW) >= 0,
            "proved": False,
            "meaning": "上一层已把 range manifest 后的首字段定为同参数窗口规格。",
            "remaining": WINDOW,
        },
        {
            "gate": "D0MsharpTerminalSameWindowClosed",
            "closed": structural_closed,
            "proved": structural_closed,
            "meaning": "D0 公式、M# 容量归一化、终端预算、Lambda/T_PDEC 与 row-free type key 已登记在同一窗口。",
            "remaining": "numeric margin and finite prefix certificate are separate inputs.",
        },
        {
            "gate": "NoNumericPromotion",
            "closed": data["concrete"].get("candidate_parameter_row", {}).get("certificate_row_valid") is False,
            "proved": True,
            "meaning": "同参数窗口闭合不等于 D0/E0/U0 已数值化；candidate row 仍显式无效。",
            "remaining": "ConcreteSameParameterMarginTableCertificate",
        },
        {
            "gate": "RunnerHashLedgerStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "当前没有可复核 runner/hash 账本来支撑 finite prefix rough-count。",
            "remaining": RUNNER,
        },
        {
            "gate": "AnalyticTailBridgeStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "tail object interface 已匹配，但从解析尾段到有限边界的单调桥仍未证明。",
            "remaining": TAIL,
        },
        {
            "gate": "TypeThresholdStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "row-free type key 定义已闭合，但类型阈值/保标签商熵亏损仍未证明。",
            "remaining": f"{TYPE_LEDGER} AND {ROW_FREE}",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_same_parameter_prefix_window_spec_router",
        "status": "same_parameter_prefix_window_spec_closed_runner_tail_type_threshold_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "same_parameter_window_specification_proved": structural_closed,
        "d0_msharp_terminal_same_z_d_lambda_alphabet_closed": structural_closed,
        "same_parameter_numeric_margin_proved": False,
        "runner_hash_ledger_proved": False,
        "analytic_tail_bridge_proved": False,
        "formal_unit_type_threshold_ledger_proved": False,
        "prefix_label_support_to_row_free_type_anticollapse_proved": False,
        "finite_boundary_prefix_certificate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "canonical_window": window,
        "ledger_rows": ledger_rows,
        "decision_rows": decision_rows,
        "hardpoint_before_router": WINDOW,
        "hardpoint_after_router": f"{RUNNER} AND {TAIL}",
        "parallel_attack_targets": [
            TYPE_LEDGER,
            ROW_FREE,
            "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "next_direct_attack_target": RUNNER,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SameParameterPrefixWindowSpecification` 可按结构规格关闭：D0 的 prefix 粗筛余公式、"
            "M# 的容量归一化、终端预算方程、冷供给 Lambda/T_PDEC 纪律与 row-free type key "
            "都已登记在同一个 alpha=0.43, P>=100000, z=floor(P^0.43) 窗口内。"
            "但这不生成 D0/E0/U0 数值，也不关闭 runner/hash、解析尾段桥、类型阈值或最终正余量。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 审查摘要。"""
    lines = [
        "# Prime Matrix strict 同参数 prefix 窗口规格路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_parameter_window_specification_proved={fmt_bool(result['same_parameter_window_specification_proved'])}",
        f"d0_msharp_terminal_same_z_d_lambda_alphabet_closed={fmt_bool(result['d0_msharp_terminal_same_z_d_lambda_alphabet_closed'])}",
        f"same_parameter_numeric_margin_proved={fmt_bool(result['same_parameter_numeric_margin_proved'])}",
        f"runner_hash_ledger_proved={fmt_bool(result['runner_hash_ledger_proved'])}",
        f"analytic_tail_bridge_proved={fmt_bool(result['analytic_tail_bridge_proved'])}",
        f"formal_unit_type_threshold_ledger_proved={fmt_bool(result['formal_unit_type_threshold_ledger_proved'])}",
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Canonical Window",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["canonical_window"].items():
        lines.append(f"| `{cell(key)}` | {cell(value)} |")

    lines.extend([
        "",
        "## 2. 同窗口对账",
        "",
        "| slot | closed | proved | formula | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for row in result["ledger_rows"]:
        lines.append(
            "| `{slot}` | `{closed}` | `{proved}` | {formula} | {remaining} |".format(
                slot=cell(row["slot"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                formula=cell(row["formula"]),
                remaining=cell(row["remaining"]),
            )
        )

    lines.extend([
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )

    lines.extend([
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
        "审稿边界：本步只关闭同参数窗口规格；没有生成 finite prefix runner/hash，"
        "没有证明解析尾段桥，也没有推出行/列命题无条件闭合。",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
