#!/usr/bin/env python3
"""生成 strict signed-source 固定点前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_signed_source_cycle_frontier_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-signed-source-cycle-frontier-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-signed-source-cycle-frontier-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-signed-source-cycle-frontier-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-actual-source-domain-entropy-atom-router.json",
    "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-signed-source-fixed-point-breaker-router.json",
    "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json",
    "prime-matrix-strict-precauchy-declaration-line-router.json",
    "prime-matrix-strict-actual-constructor-formula-line-router.json",
    "prime-matrix-strict-explicit-alpha-delta-rule-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
    "prime-matrix-strict-single-parameter-terminal-budget-margin-router.json",
]

SIGNED_SOURCE_INPUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
TERMINAL_FAMILY = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
MERTENS_TAIL = (
    "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
    "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
)


def load_json(name: str) -> dict[str, Any]:
    """读取已有 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本同步证书读取到的证据文件。"""
    hashes: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            hashes[f"docs/monograph/{name}"] = sha256(path)
    return hashes


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def route_steps() -> list[dict[str, str]]:
    """列出当前 signed-source 路线的闭环。"""
    return [
        {
            "step": "source-domain entropy",
            "frontier": "ActualPreCauchySourceDomainAbsoluteEntropyLedger",
            "next": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
        },
        {
            "step": "primitive coefficient law",
            "frontier": "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
            "next": "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows",
        },
        {
            "step": "basis/source coordinate cycle",
            "frontier": "BasisWeightSource -> ... -> WordCoordinateFormula",
            "next": SIGNED_SOURCE_INPUT,
        },
        {
            "step": "signed-source fixed point breaker",
            "frontier": "RowLevel -> ... -> RowLevel fixed point",
            "next": "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows",
        },
        {
            "step": "noncircular emission kernel",
            "frontier": "exact signed emitter before Cauchy",
            "next": "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter",
        },
        {
            "step": "declaration/formula line",
            "frontier": "actual noncanonical constructor declaration",
            "next": "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter",
        },
        {
            "step": "alpha row geometry",
            "frontier": "source tuple -> alpha row anchor/phase",
            "next": "AlphaFormulaSignedCoefficientLiftLedger",
        },
        {
            "step": "unsigned skeleton",
            "frontier": "carry-shell + P-column anchor + layered wheel",
            "next": "signed lift still open; unsigned geometry cannot emit signed weight",
        },
        {
            "step": "signed lift and weight law",
            "frontier": "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger",
            "next": "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger",
        },
        {
            "step": "identity taxonomy",
            "frontier": "independent noncanonical pre-Cauchy identity",
            "next": "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn",
        },
        {
            "step": "moving-block return",
            "frontier": "actual moving block / NC-BLK",
            "next": "global terminal family and terminal budget ledger",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步判定当前闭环与可继续攻击的非循环输入。"""
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    cycle = data["coordinate_cycle"]
    breaker = data["fixed_point_breaker"]
    kernel = data["noncircular_kernel"]
    declaration = data["declaration"]
    identity = data["identity"]
    moving = data["moving"]
    terminal_budget = data["terminal_budget"]

    return [
        row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本同步只在假设早期零行反例链内整理 signed-source 路径，不用真实零行缺席。",
            "direct_unconditional_contradiction_found=false",
        ),
        row(
            "UnsignedGeometryIntegrated",
            unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True,
            True,
            "carry-shell、P列锚、anchor-collar 与 layered-wheel 已关闭为 unsigned skeleton。",
            "AlphaFormulaSignedCoefficientLiftLedger",
        ),
        row(
            "UnsignedGeometryCannotEmitSignedWeight",
            signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is False,
            True,
            "上游几何刚性只缩小候选 row 形状，不能生成 pre-Cauchy signed coefficient。",
            "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger",
        ),
        row(
            "CoordinateSourceCycleDetected",
            cycle.get("seed_coordinate_source_cycle_detected") is True,
            True,
            "basis word、coefficient assignment、origin identity、row emitter 已形成闭合来源环。",
            SIGNED_SOURCE_INPUT,
        ),
        row(
            "SignedSourceFixedPointCutImported",
            breaker.get("current_internal_route_is_signed_source_fixed_point") is True,
            True,
            "逐行原始表下钻链回到自身；固定点不是证明，必须有非循环发射核或命名回流。",
            "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows",
        ),
        row(
            "NoncircularKernelStillNeedsDeclarationLine",
            kernel.get("pre_cauchy_constructor_declaration_line_proved") is False,
            False,
            "非循环发射核已把首字段钉到 pre-Cauchy declaration line，但该声明未证。",
            "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter",
        ),
        row(
            "DeclarationLineReturnsToConstructorFormula",
            declaration.get("pre_cauchy_constructor_declaration_line_proved") is False,
            False,
            "declaration line 已过滤到 actual constructor formula line；继续下钻又进入 alpha signed lift/weight law。",
            "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter",
        ),
        row(
            "IndependentIdentityTaxonomyReturnsToMovingBlock",
            identity.get("strict_identity_statement_taxonomy_adapter_closed") is True,
            True,
            "独立恒等式黑箱已分类为 actual moving-block/NC-BLK；不是新的第五出口。",
            "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn",
        ),
        row(
            "MovingBlockNoUnnamedExitButTerminalOpen",
            moving.get("strict_actual_moving_block_router_closed") is True,
            False,
            "moving-block/NC-BLK 不能作无名出口，但只回流到全局终端容量/模型余量账本。",
            moving.get("terminal_gap_after_router", TERMINAL_FAMILY),
        ),
        row(
            "TerminalBudgetStillNoPositiveMargin",
            terminal_budget.get("explicit_positive_terminal_budget_margin_proved") is False,
            False,
            "终端预算标准形已定为同参数正余量，但当前未证明 D_prefix-E_named-U_cold>0。",
            "ExplicitPositiveTerminalBudgetMarginInequality",
        ),
        row(
            "CurrentNonrecursiveInputPinned",
            True,
            False,
            "继续严格自足路线时，唯一非循环新增输入是 primitive basis 与 signed coefficient 的前置源输入；否则只能证明终端回流严格下降。",
            f"{SIGNED_SOURCE_INPUT} OR {TERMINAL_DESCENT}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造当前前沿同步证书。"""
    data = {
        "source_entropy": load_json("prime-matrix-strict-actual-source-domain-entropy-atom-router.json"),
        "signed_emitter": load_json("prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"),
        "primitive_law": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "coordinate_cycle": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "fixed_point_breaker": load_json("prime-matrix-strict-signed-source-fixed-point-breaker-router.json"),
        "noncircular_kernel": load_json("prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json"),
        "declaration": load_json("prime-matrix-strict-precauchy-declaration-line-router.json"),
        "constructor": load_json("prime-matrix-strict-actual-constructor-formula-line-router.json"),
        "explicit_rule": load_json("prime-matrix-strict-explicit-alpha-delta-rule-router.json"),
        "alpha_side": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "alpha_map": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "anchor_phase": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "weight_law": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "identity": load_json("prime-matrix-strict-independent-identity-statement-taxonomy-router.json"),
        "moving": load_json("prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"),
        "terminal_budget": load_json("prime-matrix-strict-single-parameter-terminal-budget-margin-router.json"),
    }
    rows = build_rows(data)
    route_closed_as_diagnosis = all(row_item["closed"] for row_item in rows[:9])
    direct = False
    return {
        "certificate_type": "prime_matrix_strict_signed_source_cycle_frontier_sync_router",
        "status": "strict_signed_source_frontier_cycle_synced_noncircular_input_or_terminal_descent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "signed_source_route_closed_as_diagnostic_cycle": route_closed_as_diagnosis,
        "unsigned_geometry_integrated": rows[1]["closed"],
        "signed_coefficient_emission_kernel_proved": False,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "actual_moving_block_spread_ncb_lk_proved": False,
        "terminal_positive_margin_proved": False,
        "acyclic_seed_cycle_cut_source_input_proved": False,
        "acyclic_terminal_return_well_founded_descent_proved": False,
        "direct_unconditional_contradiction_found": direct,
        "row_column_unconditional_closed": direct,
        "route_steps": route_steps(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "terminal_gap_after_router": f"({SIGNED_SOURCE_INPUT} OR {TERMINAL_DESCENT}) AND {MERTENS_TAIL} AND {DSTRUCTURE}",
        "with_external_mertens_high_tail_removed_basis": f"({SIGNED_SOURCE_INPUT} OR {TERMINAL_DESCENT}) AND {DSTRUCTURE}",
        "next_direct_attack_target": SIGNED_SOURCE_INPUT,
        "parallel_attack_target": TERMINAL_DESCENT,
        "plain_conclusion": (
            "本步把 signed-source 下钻链与 alpha row 几何链合并同步：早期零行刚性已经通过 "
            "carry-shell、P列锚、anchor-collar 和 layered-wheel 进入 unsigned skeleton，但它不能产生 signed "
            "coefficient。继续追逐 signed coefficient 会经 pre-Cauchy declaration、constructor formula、alpha signed "
            "lift、独立恒等式分类回到 actual moving-block/NC-BLK，再回流全局终端预算。因此当前严格自足路线的"
            "非循环新增输入被钉为 primitive basis 与 signed coefficient 的前置源输入；若不能提交该输入，就必须证明"
            "跨 PDEC/SAE/ColumnCRT/CleanKLS 回流有 well-founded strict descent。当前仍未形成无条件终端矛盾。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict signed-source 固定点前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_source_route_closed_as_diagnostic_cycle={fmt_bool(result['signed_source_route_closed_as_diagnostic_cycle'])}",
        f"unsigned_geometry_integrated={fmt_bool(result['unsigned_geometry_integrated'])}",
        f"signed_coefficient_emission_kernel_proved={fmt_bool(result['signed_coefficient_emission_kernel_proved'])}",
        f"pre_cauchy_constructor_declaration_line_proved={fmt_bool(result['pre_cauchy_constructor_declaration_line_proved'])}",
        f"actual_moving_block_spread_ncb_lk_proved={fmt_bool(result['actual_moving_block_spread_ncb_lk_proved'])}",
        f"terminal_positive_margin_proved={fmt_bool(result['terminal_positive_margin_proved'])}",
        f"acyclic_seed_cycle_cut_source_input_proved={fmt_bool(result['acyclic_seed_cycle_cut_source_input_proved'])}",
        f"acyclic_terminal_return_well_founded_descent_proved={fmt_bool(result['acyclic_terminal_return_well_founded_descent_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 闭环路线",
        "",
        "| step | frontier | next |",
        "| --- | --- | --- |",
    ]
    for item in result["route_steps"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['step'])}`",
                    table_cell(item["frontier"]),
                    table_cell(item["next"]),
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
    for item in result["rows"]:
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
            "## 3. 当前严格基",
            "",
            "严格自足线仍需：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "```",
            "",
            "若外部 Mertens/theta 高段显式输入被接受，则活动基暂时缩为：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "## 4. 下一最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行守门：",
            "",
            "```text",
            result["parallel_attack_target"],
            "```",
            "",
            "审稿边界：本文件关闭的是当前 signed-source 内部路线的固定点同步和非循环输入定位；"
            "它没有证明该输入，也没有证明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
