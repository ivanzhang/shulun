#!/usr/bin/env python3
"""审计 RKS23 内部自足线的回环，并固定非循环剩余。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_self_contained_cycle_guard_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-self-contained-cycle-guard-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-self-contained-cycle-guard-frontier-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-self-contained-cycle-guard-frontier-router.md"

INTERIOR_SYNC = MONO / "prime-matrix-strict-rks23-interior-fiber-to-slope-conic-sync-router.json"
SLOPE_CENTERED = MONO / "prime-matrix-strict-rks23-slope-conic-centered-square-measure-router.json"
CENTERED_FOURIER = MONO / "prime-matrix-strict-rks23-centered-square-measure-fourier-router.json"
TRI_FACTOR = MONO / "prime-matrix-strict-rks23-tri-quadratic-fourier-factorization-router.json"
TRI_BARRIER = MONO / "prime-matrix-strict-rks23-tri-quadratic-plancherel-barrier-router.json"
QUAD_ENERGY = MONO / "prime-matrix-strict-rks23-quadratic-energy-square-difference-router.json"
SLOPE_RATIO = MONO / "prime-matrix-strict-rks23-slope-overlap-ratio-spectrum-router.json"
FINAL_CORRELATION = MONO / "prime-matrix-strict-rks23-final-correlation-atom-router.json"
JOINT_MIXED = MONO / "prime-matrix-strict-rks23-joint-mixed-incidence-router.json"
PRODUCT_INCIDENCE = MONO / "prime-matrix-strict-rks23-square-difference-product-incidence-router.json"
ZERO_PRODUCT = MONO / "prime-matrix-strict-rks23-zero-product-peeling-router.json"
NONZERO_CENTER = MONO / "prime-matrix-strict-rks23-nonzero-product-ratio-centering-router.json"
CENTERED_L2 = MONO / "prime-matrix-strict-rks23-centered-product-ratio-l2-reduction-router.json"
RECT_CONV = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json"
CHAR_MOMENT = MONO / "prime-matrix-strict-rks23-product-ratio-character-moment-router.json"
CHAR_AUDIT = MONO / "prime-matrix-strict-rks23-character-moment-to-promotion-audit-router.json"
DSTRUCTURE_REPLACEMENT = MONO / "prime-matrix-strict-dstructure-tail-rankin-replacement-compression-router.json"
RKS_LOG = MONO / "prime-matrix-strict-rks-log-internal-hardpoint-direct-attack-router.json"
WEIL_BARRIER = MONO / "prime-matrix-strict-rks23-internal-weil-barrier-and-bg-frontier-router.json"
BALANCED_ENERGY = MONO / "prime-matrix-strict-rks23-balanced-collar-l2-energy-reduction-router.json"
WEIGHTED_UNWEIGHTED = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
POWER_RELAX = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
MOBIUS_OVERLAP = MONO / "prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.json"
MOBIUS_SUMPRODUCT = MONO / "prime-matrix-strict-rks23-mobius-overlap-sumproduct-frontier-router.json"
INVERSE_FIBER = MONO / "prime-matrix-strict-rks23-inverse-smalldoubling-to-affine-fiber-router.json"

SOURCE_FILES = [
    INTERIOR_SYNC,
    SLOPE_CENTERED,
    CENTERED_FOURIER,
    TRI_FACTOR,
    TRI_BARRIER,
    QUAD_ENERGY,
    SLOPE_RATIO,
    FINAL_CORRELATION,
    JOINT_MIXED,
    PRODUCT_INCIDENCE,
    ZERO_PRODUCT,
    NONZERO_CENTER,
    CENTERED_L2,
    RECT_CONV,
    CHAR_MOMENT,
    CHAR_AUDIT,
    DSTRUCTURE_REPLACEMENT,
    RKS_LOG,
    WEIL_BARRIER,
    BALANCED_ENERGY,
    WEIGHTED_UNWEIGHTED,
    POWER_RELAX,
    MOBIUS_OVERLAP,
    MOBIUS_SUMPRODUCT,
    INVERSE_FIBER,
]

SLOPE_FRONTIER = "NontrivialSlopeLocalizedTernaryConicBundlePowerSaving"
CHAR_BRANCH = "RKS23AnalyticBranchClosedAuthorSide"
RKS_LOG_TARGET = "SelfContainedBGRKS2RKS3ReciprocalKloostermanLogSaving"
ENERGY_TARGET = "WeightedReciprocalIntervalAdditiveEnergyLogSavingForBalancedRKS23"
FIXED_POWER_ENERGY = "UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23"
MOBIUS_TARGET = "OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving"
INVERSE_TARGET = "SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar"
NONCIRCULAR_TARGET = "NonCircularSelfContainedReciprocalIntervalEnergyPowerSaving"
RNRS_TARGET = "SelfContainedRudnevRNRSReciprocalIntervalEnergyEstimateForInverseSmallDoubling"


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
    """构造回环守门证书。"""
    interior = load_json(INTERIOR_SYNC)
    slope_centered = load_json(SLOPE_CENTERED)
    centered_fourier = load_json(CENTERED_FOURIER)
    tri_factor = load_json(TRI_FACTOR)
    tri_barrier = load_json(TRI_BARRIER)
    quad_energy = load_json(QUAD_ENERGY)
    slope_ratio = load_json(SLOPE_RATIO)
    final_corr = load_json(FINAL_CORRELATION)
    joint_mixed = load_json(JOINT_MIXED)
    product_inc = load_json(PRODUCT_INCIDENCE)
    zero_product = load_json(ZERO_PRODUCT)
    nonzero_center = load_json(NONZERO_CENTER)
    centered_l2 = load_json(CENTERED_L2)
    rect_conv = load_json(RECT_CONV)
    char_moment = load_json(CHAR_MOMENT)
    char_audit = load_json(CHAR_AUDIT)
    d_replacement = load_json(DSTRUCTURE_REPLACEMENT)
    rks_log = load_json(RKS_LOG)
    weil = load_json(WEIL_BARRIER)
    balanced = load_json(BALANCED_ENERGY)
    weighted = load_json(WEIGHTED_UNWEIGHTED)
    power_relax = load_json(POWER_RELAX)
    mobius = load_json(MOBIUS_OVERLAP)
    mobius_sp = load_json(MOBIUS_SUMPRODUCT)
    inverse = load_json(INVERSE_FIBER)

    slope_chain_to_fourier_closed = all(
        [
            interior.get("reduction_chain_closed_to_slope_conic_frontier") is True,
            slope_centered.get("centered_deviation_is_only_remaining_input") is True,
            centered_fourier.get("fourier_expansion_closed") is True,
            tri_factor.get("tri_quadratic_factorization_closed") is True,
            tri_barrier.get("per_slope_cauchy_plancherel_envelope_closed") is True,
        ]
    )
    square_difference_and_ratio_ready = all(
        [
            quad_energy.get("m_autocorrelation_opened") is True,
            slope_ratio.get("slope_overlap_l2_divisor_ledger_closed") is True,
            final_corr.get("only_joint_nonconcentration_remains") is True,
        ]
    )
    mixed_product_route_closed_to_character_gate = all(
        [
            joint_mixed.get("mixed_incidence_identity_closed") is True,
            product_inc.get("mixed_incidence_product_form_closed") is True,
            zero_product.get("nonzero_product_ratio_normal_form_closed") is True,
            nonzero_center.get("centered_nonzero_product_ratio_correlation_identity_closed") is True,
            centered_l2.get("cauchy_reduction_to_product_ratio_l2_closed") is True,
            rect_conv.get("rectangular_product_ratio_convolution_identity_closed") is True,
            char_moment.get("centered_l2_equals_nonprincipal_four_interval_moment") is True,
        ]
    )
    character_audit_closes_analytic_branch = all(
        [
            char_audit.get("rks23_analytic_branch_closed_author_side") is True,
            char_audit.get("joint_nonconcentration_atom_proved_by_product_ratio_l2_route") is True,
        ]
    )
    replacement_compressed_to_rks_log = all(
        [
            d_replacement.get("rks_log_reciprocal_kloosterman_atom_isolated") is True,
            d_replacement.get("self_contained_dstructure_tail_log4_finite_rankin_replacement_package_proved")
            is False,
        ]
    )
    rks_log_to_balanced_energy_closed = all(
        [
            rks_log.get("rks2_rks3_deep_blocks_isolated") is True,
            weil.get("balanced_collar_is_only_deep_part") is True,
            balanced.get("plancherel_energy_transfer_closed") is True,
        ]
    )
    energy_to_inverse_frontier_closed = all(
        [
            weighted.get("divisor_weighted_to_unweighted_reduction_closed") is True,
            power_relax.get("fixed_power_saving_implies_required_log_saving") is True,
            mobius.get("mobius_overlap_identity_closed") is True,
            mobius_sp.get("energy_mobius_sumproduct_dictionary_closed") is True,
            inverse.get("reduction_chain_closed_to_interior_frontier") is True,
        ]
    )

    cycle_detected = all(
        [
            slope_chain_to_fourier_closed,
            square_difference_and_ratio_ready,
            mixed_product_route_closed_to_character_gate,
            character_audit_closes_analytic_branch,
            replacement_compressed_to_rks_log,
            rks_log_to_balanced_energy_closed,
            energy_to_inverse_frontier_closed,
        ]
    )
    noncircular_input_proved = False
    row_column_closed = False

    cycle_chain = [
        {
            "stage": "current-analytic-frontier",
            "from": INVERSE_TARGET,
            "to": SLOPE_FRONTIER,
            "status": "closed reduction only; slope conic still not a standalone proof",
        },
        {
            "stage": "slope-to-character",
            "from": SLOPE_FRONTIER,
            "to": "FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving",
            "status": "Fourier, square-difference, mixed/product-ratio reductions imported",
        },
        {
            "stage": "character-audit",
            "from": "BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment",
            "to": CHAR_BRANCH,
            "status": "character branch is author-side closed in the existing audit",
        },
        {
            "stage": "promotion-replacement",
            "from": CHAR_BRANCH,
            "to": RKS_LOG_TARGET,
            "status": "final promotion is not accepted; self-contained replacement compresses to RKS-log",
        },
        {
            "stage": "rks-log-energy",
            "from": RKS_LOG_TARGET,
            "to": ENERGY_TARGET,
            "status": "balanced collar Cauchy/L2/Plancherel reduction imported",
        },
        {
            "stage": "energy-inverse-sumproduct",
            "from": FIXED_POWER_ENERGY,
            "to": INVERSE_TARGET,
            "status": "reciprocal energy becomes Mobius overlap and returns to inverse sum-product frontier",
        },
    ]

    rows = [
        row(
            "SlopeConicToFourierPacketChainImported",
            slope_chain_to_fourier_closed,
            True,
            "当前 slope-conic 前沿已沿中心化测度、Fourier、三二次谱包压到 Plancherel 后相关问题。",
            "CorrelatedQuadraticFourierEnergyOverlapPowerSaving",
        ),
        row(
            "SquareDifferenceAndSlopeRatioSpectraImported",
            square_difference_and_ratio_ready,
            True,
            "二次 Fourier 能量与斜率重叠分别打开为平方差谱和低 L2 区间比值谱。",
            "JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum",
        ),
        row(
            "MixedProductRatioRouteImported",
            mixed_product_route_closed_to_character_gate,
            True,
            "联合非集中路线已归约到中心化非零乘积比值 L2/角色矩门。",
            "FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving",
        ),
        row(
            "CharacterMomentAuditClosesAnalyticBranch",
            character_audit_closes_analytic_branch,
            True,
            "已有审计把 RKS23 角色矩解析分支向上游回传为作者侧闭合。",
            "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage",
        ),
        row(
            "SelfContainedReplacementCompressedToRKSLog",
            replacement_compressed_to_rks_log,
            True,
            "DStructure/Tail-log4/finite Rankin 自足替代包的形式壳已压到 RKS-log 深估计。",
            RKS_LOG_TARGET,
        ),
        row(
            "RKSLogToBalancedEnergyImported",
            rks_log_to_balanced_energy_closed,
            True,
            "RKS2/RKS3 深块已压成平衡颈部倒数区间加权加性能量输入。",
            ENERGY_TARGET,
        ),
        row(
            "BalancedEnergyReturnsToInverseSumproductFrontier",
            energy_to_inverse_frontier_closed,
            True,
            "去权重、固定幂放松、Möbius 重叠谱与 inverse-sumproduct 字典把能量线带回当前解析前沿。",
            INVERSE_TARGET,
        ),
        row(
            "SelfContainedCycleDetected",
            cycle_detected,
            True,
            "若把 RKS-log 再用同一 RKS23/inverse-sumproduct 线证明，会形成回环，不能作为非循环自足证明。",
            NONCIRCULAR_TARGET,
        ),
        row(
            NONCIRCULAR_TARGET,
            noncircular_input_proved,
            False,
            "真正剩余必须是独立于该回环的倒数区间能量/sum-product/RNRS-Rudnev 型证明。",
            RNRS_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_closed,
            False,
            "本步关闭的是路线审计和循环守门；未补入独立能量定理，因此不宣称无条件闭合。",
            NONCIRCULAR_TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_self_contained_cycle_guard_frontier_router",
        "status": "self_contained_internal_route_cycle_detected_noncircular_reciprocal_energy_input_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "slope_chain_to_fourier_closed": slope_chain_to_fourier_closed,
        "square_difference_and_ratio_ready": square_difference_and_ratio_ready,
        "mixed_product_route_closed_to_character_gate": mixed_product_route_closed_to_character_gate,
        "character_audit_closes_analytic_branch": character_audit_closes_analytic_branch,
        "replacement_compressed_to_rks_log": replacement_compressed_to_rks_log,
        "rks_log_to_balanced_energy_closed": rks_log_to_balanced_energy_closed,
        "energy_to_inverse_frontier_closed": energy_to_inverse_frontier_closed,
        "self_contained_cycle_detected": cycle_detected,
        "noncircular_reciprocal_energy_input_proved": noncircular_input_proved,
        "row_column_unconditional_closed": row_column_closed,
        "next_direct_attack_target": NONCIRCULAR_TARGET,
        "next_required_input": RNRS_TARGET,
        "parallel_external_route": "AcceptRNRSRudnevOrEXTBGWithExplicitParameterMatch",
        "cycle_chain": cycle_chain,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮把当前唯一内部自足线完整串联审计后，得到一个必须保留的循环守门结论："
            "从 inverse-sumproduct/RKS23 解析前沿可以沿 slope-conic、Fourier、平方差谱、乘积比值谱和角色矩审计"
            "回传到作者侧解析闭合；但最终自足替代包又把剩余压回 RKS-log，而 RKS-log 经平衡颈部能量归约、"
            "Möbius 重叠谱和 inverse-sumproduct 字典又回到同一个解析前沿。"
            "因此这条内部路线不能被当作非循环证明闭合。真正剩余是补入独立的倒数区间能量/"
            "sum-product/RNRS-Rudnev 型固定幂节省证明，或接受外部定理参数匹配。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS23 自足线循环守门前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"self_contained_cycle_detected={fmt_bool(result['self_contained_cycle_detected'])}",
        f"noncircular_reciprocal_energy_input_proved={fmt_bool(result['noncircular_reciprocal_energy_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 回环链条",
        "",
        "| stage | from | to | status |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["cycle_chain"]:
        lines.append(
            "| `{stage}` | `{src}` | `{dst}` | {status} |".format(
                stage=table_cell(item["stage"]),
                src=table_cell(item["from"]),
                dst=table_cell(item["to"]),
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
            "## 3. 下一真正非循环目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            result["next_required_input"],
            "```",
            "",
            "## 4. 边界声明",
            "",
            "- 已归档的回环不是证明闭合；它只是阻止把同一内部路线重复引用为自足证明。",
            "- 行/列命题仍未无条件闭合。",
            "- 下一步必须证明独立的倒数区间能量/sum-product 输入，或明确接受外部 RNRS/Rudnev/BG 类型定理。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    MONO.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
