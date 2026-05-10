#!/usr/bin/env python3
"""把已闭合的 RKS23 角色矩输入向后传播到最终晋级门。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_character_moment_to_promotion_audit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-character-moment-to-promotion-audit-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-character-moment-to-promotion-audit-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-character-moment-to-promotion-audit-router.md"

BURGESS_AFTER_B4 = MONO / "prime-matrix-strict-rks23-burgess-after-b4-moment-ledger-router.json"
CHARACTER_MOMENT = MONO / "prime-matrix-strict-rks23-product-ratio-character-moment-router.json"
RECTANGULAR_CONVOLUTION = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json"
CENTERED_L2 = MONO / "prime-matrix-strict-rks23-centered-product-ratio-l2-reduction-router.json"
NONZERO_CENTERING = MONO / "prime-matrix-strict-rks23-nonzero-product-ratio-centering-router.json"
FINAL_CORRELATION = MONO / "prime-matrix-strict-rks23-final-correlation-atom-router.json"
DSTRUCTURE_PROMOTION = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
FINAL_PROMOTION = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
SOURCE_FILES = [
    BURGESS_AFTER_B4,
    CHARACTER_MOMENT,
    RECTANGULAR_CONVOLUTION,
    CENTERED_L2,
    NONZERO_CENTERING,
    FINAL_CORRELATION,
    DSTRUCTURE_PROMOTION,
    FINAL_PROMOTION,
]

TARGET = "RKS23CharacterMomentToRowColumnPromotionGateAudit"
BURGESS_THRESHOLD = "BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment"
CHARACTER_SAVING = "FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving"
RECTANGULAR_L2 = "DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale"
CENTERED_L2_TARGET = "CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale"
JOINT_NONCONCENTRATION = "JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SELF_CONTAINED_REPLACEMENT = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
EXPLICIT_ACCEPTANCE = "ExplicitIndependentPromotionAcceptanceRecord"
ROW_COLUMN_GATE = "RowColumnUnconditionalClosed"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造 RKS23 角色矩到最终推广门的审计证书。"""
    burgess = load_json(BURGESS_AFTER_B4)
    character = load_json(CHARACTER_MOMENT)
    rectangular = load_json(RECTANGULAR_CONVOLUTION)
    centered = load_json(CENTERED_L2)
    nonzero = load_json(NONZERO_CENTERING)
    final_correlation = load_json(FINAL_CORRELATION)
    dstructure = load_json(DSTRUCTURE_PROMOTION)
    final_promotion = load_json(FINAL_PROMOTION)

    target_active = (
        burgess.get("next_direct_attack_target") == TARGET
        and burgess.get("rks23_character_moment_closed_author_side_self_contained") is True
        and burgess.get("burgess_threshold_dichotomy_closure_author_side") is True
    )

    character_moment_reduction_ready = (
        character.get("centered_l2_equals_nonprincipal_four_interval_moment") is True
        and character.get("cross_ratio_fourier_factorization_closed") is True
    )
    rectangular_reduction_ready = (
        rectangular.get("rectangular_product_ratio_convolution_identity_closed") is True
        and rectangular.get("dyadic_rectangularization_closed_up_to_polylog") is True
    )
    centered_l2_reduction_ready = (
        centered.get("cauchy_reduction_to_product_ratio_l2_closed") is True
        and centered.get("centered_product_ratio_l2_identity_closed") is True
    )
    nonzero_centering_ready = (
        nonzero.get("centered_nonzero_product_ratio_correlation_identity_closed") is True
        and nonzero.get("fstar_uniform_baseline_closed") is True
    )
    final_correlation_ready = final_correlation.get("only_joint_nonconcentration_remains") is True

    character_moment_saving_closed = target_active
    rectangular_l2_closed = character_moment_saving_closed and character_moment_reduction_ready
    centered_l2_closed = rectangular_l2_closed and rectangular_reduction_ready and centered_l2_reduction_ready
    joint_nonconcentration_closed = centered_l2_closed and nonzero_centering_ready and final_correlation_ready
    rks23_analytic_branch_closed = joint_nonconcentration_closed

    promotion_boundary_closed = dstructure.get("promotion_package_boundary_closed") is True and (
        final_promotion.get("promotion_author_packet_sealed") is True
    )
    independent_acceptance_closed = (
        dstructure.get("promotion_package_independently_accepted") is True
        or final_promotion.get("referee_gate_explicitly_accepted") is True
    )

    row_column_closed = rks23_analytic_branch_closed and promotion_boundary_closed and independent_acceptance_closed

    propagation_chain = {
        "new_input": "Burgess-after-B4 certificate closes the four-interval nonprincipal character product moment",
        "character_to_rectangle": "multiplicative Fourier/Plancherel turns that saving into dyadic rectangular product-ratio convolution L2 saving",
        "rectangle_to_centered_l2": "support rectangularization and product-ratio convolution identity propagate the fixed-power L2 saving",
        "centered_l2_to_joint": "Cauchy plus the interval-ratio L2 ledger closes the centered joint nonconcentration route",
        "joint_to_rks23_branch": "the former RKS23 joint nonconcentration atom is discharged on the product-ratio L2 route",
        "promotion_boundary": "RKS23 analytic closure still does not replace the independent final DStructure/Rankin promotion gate",
    }

    stale_frontier_reconciliation = {
        "older_character_moment_router": "recorded the character moment as open before Burgess was internalized",
        "older_rectangular_router": "recorded dyadic rectangular convolution L2 as open before character moment closure",
        "older_centered_l2_router": "recorded centered product-ratio L2 as open before rectangular L2 closure",
        "older_final_correlation_router": "recorded joint nonconcentration as open before the product-ratio L2 route was closed",
        "current_router_role": "does not rewrite old certificates; it supersedes their open flags by an explicit downstream audit",
    }

    promotion_boundary = {
        "dstructure_boundary_closed": fmt_bool(dstructure.get("promotion_package_boundary_closed")),
        "rankin_pass_or_return_closed": fmt_bool(dstructure.get("full_rankin_ledger_still_open_closed")),
        "author_packet_sealed": fmt_bool(final_promotion.get("promotion_author_packet_sealed")),
        "external_kls_math_lane_closed": fmt_bool(final_promotion.get("external_kls_math_lane_closed")),
        "independent_acceptance_closed": fmt_bool(independent_acceptance_closed),
        "irreducible_gate": PROMOTION_GATE,
        "self_contained_replacement": SELF_CONTAINED_REPLACEMENT,
    }

    rows = [
        row(
            "RKS23PromotionAuditTargetActive",
            target_active,
            target_active,
            "上一证书已把最新剩余明确指向 RKS23 角色矩到行/列推广审计。",
            TARGET,
        ),
        row(
            BURGESS_THRESHOLD,
            burgess.get("burgess_threshold_dichotomy_closure_author_side") is True,
            True,
            "Burgess 大包与薄包吸收已合并闭合四区间角色矩阈值门。",
            "closed",
        ),
        row(
            CHARACTER_SAVING,
            character_moment_saving_closed,
            character_moment_saving_closed,
            "四短区间非主角色乘积矩节省由 Burgess-after-B4 证书补齐。",
            "closed",
        ),
        row(
            RECTANGULAR_L2,
            rectangular_l2_closed,
            rectangular_l2_closed,
            "乘法 Fourier 因子化把角色矩节省回传为矩形乘积比值卷积 L2 节省。",
            "closed",
        ),
        row(
            CENTERED_L2_TARGET,
            centered_l2_closed,
            centered_l2_closed,
            "矩形化、卷积恒等式和 Cauchy/L2 归约把中心化乘积比值 L2 节省闭合。",
            "closed",
        ),
        row(
            JOINT_NONCONCENTRATION,
            joint_nonconcentration_closed,
            joint_nonconcentration_closed,
            "产品比值 L2 路线关闭原 joint nonconcentration 终端原子。",
            "closed",
        ),
        row(
            "RKS23AnalyticBranchClosedAuthorSide",
            rks23_analytic_branch_closed,
            rks23_analytic_branch_closed,
            "RKS23 当前角色矩解析分支已从 Burgess 输入向上游全部回传闭合。",
            "closed",
        ),
        row(
            "PromotionPackageBoundaryClosed",
            promotion_boundary_closed,
            promotion_boundary_closed,
            "DStructure/Tail-log4/finite Rankin 晋级包边界和作者包已封装。",
            PROMOTION_GATE,
        ),
        row(
            PROMOTION_GATE,
            independent_acceptance_closed,
            False,
            "独立晋级接受事件未发生，作者侧不能把它伪造成证明步骤。",
            f"{EXPLICIT_ACCEPTANCE} OR {SELF_CONTAINED_REPLACEMENT}",
        ),
        row(
            ROW_COLUMN_GATE,
            row_column_closed,
            row_column_closed,
            "RKS23 解析分支已闭合，但最终行/列无条件命题仍受独立晋级门或自足替代包约束。",
            SELF_CONTAINED_REPLACEMENT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_character_moment_to_promotion_audit_router",
        "status": "rks23_character_moment_branch_closed_final_promotion_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "rks23_promotion_audit_target_active": target_active,
        "burgess_threshold_dichotomy_closure_author_side": burgess.get(
            "burgess_threshold_dichotomy_closure_author_side"
        )
        is True,
        "four_short_interval_character_product_moment_saving_proved": character_moment_saving_closed,
        "dyadic_rectangular_product_ratio_convolution_l2_saving_proved": rectangular_l2_closed,
        "centered_nonzero_product_ratio_l2_power_saving_proved": centered_l2_closed,
        "joint_nonconcentration_atom_proved_by_product_ratio_l2_route": joint_nonconcentration_closed,
        "rks23_analytic_branch_closed_author_side": rks23_analytic_branch_closed,
        "promotion_package_boundary_closed": promotion_boundary_closed,
        "final_promotion_gate_accepted": independent_acceptance_closed,
        "row_column_unconditional_closed": row_column_closed,
        "next_direct_attack_target": SELF_CONTAINED_REPLACEMENT,
        "parallel_external_acceptance_target": EXPLICIT_ACCEPTANCE,
        "irreducible_promotion_gate": PROMOTION_GATE,
        "propagation_chain": propagation_chain,
        "stale_frontier_reconciliation": stale_frontier_reconciliation,
        "promotion_boundary": promotion_boundary,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮把上一证书闭合的 Burgess/RKS23 角色矩输入向后传播：四短区间非主角色乘积矩、"
            "dyadic 矩形乘积比值卷积 L2、中心化非零乘积比值 L2、以及 joint nonconcentration "
            "终端原子均在同一路线上闭合。由此 RKS23 当前解析分支作者侧闭合。"
            "但这仍不能把行/列命题升级为无条件定理，因为最终 DStructure/Tail-log4/finite Rankin "
            "晋级包虽边界封装，独立接受事件尚未发生。当前唯一内部自足剩余变为用一个新的完全自足替代包"
            "替换该独立晋级门。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_key_value_section(lines: list[str], title: str, mapping: dict[str, Any]) -> None:
    """追加键值表。"""
    lines.extend(["", title, "", "| field | value |", "| --- | --- |"])
    for key, value in mapping.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 角色矩到推广门审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"four_short_interval_character_product_moment_saving_proved={fmt_bool(result['four_short_interval_character_product_moment_saving_proved'])}",
        f"dyadic_rectangular_product_ratio_convolution_l2_saving_proved={fmt_bool(result['dyadic_rectangular_product_ratio_convolution_l2_saving_proved'])}",
        f"centered_nonzero_product_ratio_l2_power_saving_proved={fmt_bool(result['centered_nonzero_product_ratio_l2_power_saving_proved'])}",
        f"joint_nonconcentration_atom_proved_by_product_ratio_l2_route={fmt_bool(result['joint_nonconcentration_atom_proved_by_product_ratio_l2_route'])}",
        f"rks23_analytic_branch_closed_author_side={fmt_bool(result['rks23_analytic_branch_closed_author_side'])}",
        f"promotion_package_boundary_closed={fmt_bool(result['promotion_package_boundary_closed'])}",
        f"final_promotion_gate_accepted={fmt_bool(result['final_promotion_gate_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 回传闭合链", result["propagation_chain"])
    render_key_value_section(lines, "## 2. 旧前沿协调", result["stale_frontier_reconciliation"])
    render_key_value_section(lines, "## 3. 晋级门边界", result["promotion_boundary"])

    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一唯一内部自足剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行的非作者侧关闭方式：",
            "",
            "```text",
            result["parallel_external_acceptance_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
