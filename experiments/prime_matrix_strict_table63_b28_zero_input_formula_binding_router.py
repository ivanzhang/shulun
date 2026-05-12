#!/usr/bin/env python3
"""生成 strict Table 6.3 b=28 零点输入到显式公式绑定审计证书。

用法示例：
  python3 experiments/prime_matrix_strict_table63_b28_zero_input_formula_binding_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table63-b28-zero-input-formula-binding-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 50

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-table63-b28-zero-input-formula-binding-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table63-b28-zero-input-formula-binding-router.md"

PREVIOUS = DOCS / "prime-matrix-strict-table63-b28-generation-rounding-router.json"
INTERNAL_PSI0 = DOCS / "prime-matrix-b3-internal-psi0-perron-formula-router.json"
PERRON = DOCS / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
ZERO_SUM = DOCS / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
TRIVIAL_TAIL = DOCS / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
TRANSITION = DOCS / "prime-matrix-strict-finite-verified-zero-tail-transition-router.json"
LARGE_RH = DOCS / "prime-matrix-strict-large-finite-rh-verification-router.json"
ZERO_FREE = DOCS / "prime-matrix-strict-explicit-zero-free-table-tail-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [
    PREVIOUS,
    INTERNAL_PSI0,
    PERRON,
    ZERO_SUM,
    TRIVIAL_TAIL,
    TRANSITION,
    LARGE_RH,
    ZERO_FREE,
    CLAIM_STATUS,
]

TARGET = "Table63B28ZeroInputToExplicitFormulaBindingLedger"
FORMULA_DECLARATION = "Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger"
PSI_CONVENTION = "Table63B28PsiVsPsi0EndpointConventionLedger"
KERNEL = "Table63B28KernelTruncationAndSmoothingConventionLedger"
FINITE_RH = "Table63B28FiniteRHHeightEndpointAndZeroBlockLedger"
ZERO_TAIL = "Table63B28ZeroFreeTailConstantsAndStartHeightLedger"
NO_GAP = "Table63B28FiniteToTailNoGapNoOverlapLedger"
BUDGET = "Table63B28PsiEpsilonBudgetPartitionLedger"
ROUNDING = "Table63B28DirectedUpperRoundingAndIntervalPropagationLedger"
HASH = "Table63B28ReproducibleComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

EPS = Decimal("0.00002224")
TARGET_RELATIVE = Decimal(1) / Decimal(36260)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
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


def binding_matrix() -> list[dict[str, str]]:
    """列出零点输入绑定必须同时匹配的字段。"""
    return [
        {
            "field": "target_function",
            "current_internal_status": "psi_0 exact formula closed",
            "binding_gap": "Table 6.3 的 epsilon_psi 行必须声明使用 psi、psi_0 或端点跳变转换。",
            "next_gate": PSI_CONVENTION,
        },
        {
            "field": "kernel_truncation_smoothing",
            "current_internal_status": "unsmoothed Perron C=12128 closed for internal coarse route",
            "binding_gap": "内部非平滑核已闭合但过粗；Table 6.3 的实际核/截断/平滑规则未声明。",
            "next_gate": KERNEL,
        },
        {
            "field": "finite_zero_block",
            "current_internal_status": "Gourdon external source identified; repository self-contained data/hash open",
            "binding_gap": "需要把零点数量或高度端点转换为表公式实际使用的 H 与零点块。",
            "next_gate": FINITE_RH,
        },
        {
            "field": "zero_free_tail",
            "current_internal_status": "Kadiri external source identified; table constants/start height open",
            "binding_gap": "需要声明表尾项使用的零点自由常数、起点和适用范围。",
            "next_gate": ZERO_TAIL,
        },
        {
            "field": "split_no_gap_no_overlap",
            "current_internal_status": "common-variable taxonomy closed only",
            "binding_gap": "需要证明 finite block、zero-free tail 与截断余项覆盖连续且不重复扣费。",
            "next_gate": NO_GAP,
        },
        {
            "field": "budget_and_rounding",
            "current_internal_status": "cap fixed; component numerical budget/hash open",
            "binding_gap": "需要证明绑定后的各项和被外向舍入到 2.224E-5。",
            "next_gate": f"{BUDGET} AND {ROUNDING} AND {HASH}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造零点输入绑定审计证书。"""
    previous = load_json(PREVIOUS)
    internal_psi0 = load_json(INTERNAL_PSI0)
    perron = load_json(PERRON)
    zero_sum = load_json(ZERO_SUM)
    trivial_tail = load_json(TRIVIAL_TAIL)
    transition = load_json(TRANSITION)
    large_rh = load_json(LARGE_RH)
    zero_free = load_json(ZERO_FREE)

    active = previous.get("next_direct_attack_target") == TARGET
    internal_formula_identity_closed = internal_psi0.get("internal_psi0_exact_formula_closed") is True
    internal_perron_closed = perron.get("unsmoothed_perron_strict_self_contained_closed") is True
    internal_zero_sum_closed = zero_sum.get("zero_sum_contour_budget_self_contained_closed") is True
    internal_tail_closed = trivial_tail.get("trivial_tail_prime_power_budget_self_contained_closed") is True
    internal_chain_complete_for_coarse_formula = (
        internal_formula_identity_closed
        and internal_perron_closed
        and internal_zero_sum_closed
        and internal_tail_closed
    )
    coarse_gap = Decimal(str(previous.get("arithmetic", {}).get("coarse_template_gap_factor_high_tail_b28", "0")))
    internal_chain_rejected_as_table63_generator = internal_chain_complete_for_coarse_formula and coarse_gap > Decimal("1e12")
    common_variables_classified = transition.get("common_variable_interface_taxonomy_closed") is True
    external_inputs_available = (
        large_rh.get("external_gourdon_conditional_lane_available") is True
        and zero_free.get("kadiri_external_source_identified") is True
    )
    p51_margin = TARGET_RELATIVE - EPS

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            previous.get("counterexample_assumption_only") is True
            and previous.get("row_column_unconditional_closed") is False,
            True,
            "本步仍只审计假设反例链可调用的 Table 6.3 解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ZeroInputBindingGateActive",
            active,
            True,
            "上一证书已把最窄点压到 b=28 的有限零点/零点自由尾项与显式公式绑定。",
            TARGET,
        ),
        row(
            "InternalCoarseExplicitFormulaChainComplete",
            internal_chain_complete_for_coarse_formula,
            True,
            "仓库内部 psi_0 身份、非平滑 Perron、零点和粗预算、平凡尾项/素数幂账本已经自洽闭合。",
            "internal coarse Perron route",
        ),
        row(
            "InternalCoarseFormulaRejectedAsTable63Generator",
            internal_chain_rejected_as_table63_generator,
            True,
            "现有内部公式链虽自洽，但以 C=1280,C_Z=65536 口径生成 b=28 表值失败约 10^12 倍。",
            f"gap_factor={coarse_gap}",
        ),
        row(
            "ExternalZeroInputsAvailableButUnbound",
            external_inputs_available,
            False,
            "Gourdon 有限零点与 Kadiri 零点自由区可作为外部来源，但尚未进入同一 b=28 表公式。",
            f"{FINITE_RH} AND {ZERO_TAIL}",
        ),
        row(
            "CommonVariableTaxonomyImported",
            common_variables_classified,
            True,
            "六类共同变量已经分类：x 区间、高度端点、尾项阈值、公式核、预算、舍入/hash。",
            "taxonomy closed, numerical binding open",
        ),
        row(
            FORMULA_DECLARATION,
            False,
            False,
            "缺少 Table 6.3 b=28 实际表公式/算法工件；没有它，零点输入无法判断应绑定到哪个核、截断和端点约定。",
            f"{PSI_CONVENTION} AND {KERNEL} AND {FINITE_RH} AND {ZERO_TAIL}",
        ),
        row(
            TARGET,
            False,
            False,
            "零点输入绑定不能在公式声明之前闭合；现有内部粗公式不能替代 Table 6.3 表算法。",
            f"{FORMULA_DECLARATION} AND {NO_GAP}",
        ),
        row(
            "B28GenerationStillOpen",
            False,
            False,
            "即使完成绑定，仍需预算分摊、外向舍入、区间传播和可复现 hash 生成 2.224E-5。",
            f"{BUDGET} AND {ROUNDING} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "Table 6.3 零点输入绑定审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_table63_b28_zero_input_formula_binding_router",
        "status": "table63_b28_zero_input_binding_blocked_by_actual_table_formula_declaration",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "internal_coarse_explicit_formula_chain_complete": internal_chain_complete_for_coarse_formula,
        "internal_coarse_formula_rejected_as_table63_generator": internal_chain_rejected_as_table63_generator,
        "external_zero_inputs_available_but_unbound": external_inputs_available,
        "common_variable_taxonomy_closed": common_variables_classified,
        "table63_b28_actual_formula_declaration_closed": False,
        "table63_b28_zero_input_binding_closed": False,
        "table63_b28_no_gap_no_overlap_closed": False,
        "table63_b28_generation_rounding_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "arithmetic": {
            "epsilon_psi_28": str(EPS),
            "target_1_over_36260": str(TARGET_RELATIVE),
            "p51_high_tail_margin": str(p51_margin),
            "coarse_template_gap_factor_high_tail_b28": str(coarse_gap),
        },
        "binding_matrix": binding_matrix(),
        "replacement_self_contained": {
            TARGET: f"{FORMULA_DECLARATION} AND {NO_GAP}",
            FORMULA_DECLARATION: f"{PSI_CONVENTION} AND {KERNEL} AND {FINITE_RH} AND {ZERO_TAIL}",
        },
        "next_direct_attack_target": FORMULA_DECLARATION,
        "parallel_attack_targets": [PSI_CONVENTION, KERNEL, FINITE_RH, ZERO_TAIL, NO_GAP, BUDGET, ROUNDING, HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`Table63B28ZeroInputToExplicitFormulaBinding` 的首缺口不是再登记 Gourdon/Kadiri，"
            "而是声明 b=28 表行实际采用的显式公式/表算法。仓库内部粗 Perron 链已经自洽闭合，"
            "但它被数值压力排除为 Table 6.3 生成器；外部零点来源虽然可用，仍未绑定到同一核、"
            "截断、端点和尾项阈值。因此下一最窄点是 `Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Table 6.3 b=28 零点输入绑定审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"internal_coarse_explicit_formula_chain_complete={fmt_bool(result['internal_coarse_explicit_formula_chain_complete'])}",
        f"internal_coarse_formula_rejected_as_table63_generator={fmt_bool(result['internal_coarse_formula_rejected_as_table63_generator'])}",
        f"external_zero_inputs_available_but_unbound={fmt_bool(result['external_zero_inputs_available_but_unbound'])}",
        f"table63_b28_actual_formula_declaration_closed={fmt_bool(result['table63_b28_actual_formula_declaration_closed'])}",
        f"table63_b28_zero_input_binding_closed={fmt_bool(result['table63_b28_zero_input_binding_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 绑定矩阵",
        "",
        "| field | current internal status | binding gap | next gate |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["binding_matrix"]:
        lines.append(
            "| `{field}` | {status} | {gap} | `{next_gate}` |".format(
                field=table_cell(item["field"]),
                status=table_cell(item["current_internal_status"]),
                gap=table_cell(item["binding_gap"]),
                next_gate=table_cell(item["next_gate"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 数值边界",
            "",
            "| field | value |",
            "| --- | ---: |",
        ]
    )
    for key, value in result["arithmetic"].items():
        lines.append(f"| `{table_cell(key)}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"table63_b28_zero_input_binding_closed={fmt_bool(result['table63_b28_zero_input_binding_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
