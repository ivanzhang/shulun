#!/usr/bin/env python3
"""Prime Matrix 当前最终开放输入直接攻坚路由器。

用法示例：
  python3 experiments/prime_matrix_final_open_input_current_attack_router.py

输出：
  docs/monograph/prime-matrix-final-open-input-current-attack-router.json
  docs/monograph/prime-matrix-final-open-input-current-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FINAL_ATTEMPT = DOCS / "prime-matrix-unconditional-closure-final-attempt-router.json"
DEFAULT_ACTUAL_SOURCE = DOCS / "prime-matrix-actual-source-antiatom-lane-audit-router.json"
DEFAULT_SPECTRAL = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_CDEP_REDUCTION = DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
DEFAULT_NCBLK_ALIGNMENT = DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json"
DEFAULT_EXACT_ENTROPY_REDUCTION = (
    DOCS / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json"
)
DEFAULT_SUPPORT_RANGE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json"
DEFAULT_SOURCE_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_FULL_RANKIN = DOCS / "prime-matrix-full-rankin-ledger-inventory-router.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-final-open-input-current-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-final-open-input-current-attack-router.md"

SOURCE_AXIOM = "AddStrengthenedActualSourceAntiAtomTheorem"
SPECTRAL_INPUT = "CDependentResidueWeightSpectralCancellationInput"
NCBLK_COMMON_CORE = "NCBLKActualBlockNonConcentrationOrExternalDIBFI"
EXACT_ENTROPY_OR_EXTERNAL = "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov"
EXACT_ENTROPY = "ExactFullSNonAPWFDSourceEntropy"
FACTOR_SUPPORT_OR_EXTERNAL = "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov"
FACTOR_SUPPORT_LOWER = "FullSNonAPExactFactorSupportLowerBound"
BALANCED_RANGE = "FullSNonAPBalancedRangeThreshold"
TYPE_FOURIER_COMPAT = "FullSNonAPTypeFourierCapacityCompatibility"
SUPPORT_CAPACITY_OR_EXTERNAL = "FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov"
SOURCE_ANTIATOM_OR_EXTERNAL = "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov"
SOURCE_ANTIATOM_CONTRACT = "FullSNonAPStrengthenedSourceAntiAtomContract"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
PROMOTION_INPUT = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    boundary_closed: bool,
    proved_or_accepted: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造最终开放输入审查行。"""
    return {
        "gate": gate,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    final_attempt: dict[str, Any],
    actual_source: dict[str, Any],
    spectral: dict[str, Any],
    cdep_reduction: dict[str, Any],
    ncblk_alignment: dict[str, Any],
    exact_entropy_reduction: dict[str, Any],
    support_range: dict[str, Any],
    source_antiatom: dict[str, Any],
    full_rankin: dict[str, Any],
    promotion: dict[str, Any],
) -> list[dict[str, Any]]:
    """合并最新路由，给出当前最终开放输入。"""
    final_boundary = final_attempt.get("final_attempt_boundary_closed") is True
    source_lane_closed = actual_source.get("actual_source_antiatom_lane_boundary_closed") is True
    source_antiatom_proved = actual_source.get("actual_source_antiatom_proved") is True
    generic_refuted = actual_source.get("generic_self_contained_antiatom_refuted") is True
    source_axiom_pinned = (
        actual_source.get("self_contained_source_lane_remaining") == SOURCE_AXIOM
        and actual_source.get("recommended_next_without_new_source_axiom") == SPECTRAL_INPUT
    )
    spectral_pinned = (
        spectral.get("terminal_gap_after_router") == SPECTRAL_INPUT
        and SPECTRAL_INPUT in spectral.get("open_spectral_gap_gates", [])
    )
    spectral_accepted = spectral.get("completed_weight_spectral_gap_closed") is True
    cdep_reduced = cdep_reduction.get("terminal_gap_after_router") == NCBLK_COMMON_CORE
    ncblk_aligned = ncblk_alignment.get("terminal_gap_after_router") == EXACT_ENTROPY_OR_EXTERNAL
    exact_entropy_reduced = exact_entropy_reduction.get("terminal_gap_after_router") == FACTOR_SUPPORT_OR_EXTERNAL
    range_closed = support_range.get("closed_support_package_clause") == BALANCED_RANGE
    support_capacity_terminal = support_range.get("terminal_gap_after_router") == SUPPORT_CAPACITY_OR_EXTERNAL
    antiatom_terminal = source_antiatom.get("terminal_gap_after_router") == SOURCE_ANTIATOM_OR_EXTERNAL
    rankin_subledger_closed = full_rankin.get("full_rankin_ledger_still_open_closed") is True
    promotion_boundary = promotion.get("promotion_package_boundary_closed") is True
    promotion_accepted = promotion.get("promotion_package_independently_accepted") is True

    return [
        row(
            "PreviousFinalBoundaryImported",
            final_boundary,
            False,
            "旧终局边界已把问题压成 moving-block/外部谱输入加独立晋级验收。",
            "用最新 actual-source 与 Rankin 验收账本重新对齐。",
        ),
        row(
            "ActualSourceLaneAudited",
            source_lane_closed,
            source_antiatom_proved,
            "actual-source 反原子 lane 已审计：canonical 分支闭合，generic 自足版被 moving-delta 反证。",
            SOURCE_AXIOM,
        ),
        row(
            "NoCurrentSelfContainedSourceClosureWithoutNewAxiom",
            source_lane_closed and generic_refuted and source_axiom_pinned,
            False,
            "若不新增并证明实际源强化反原子定理，现有自足材料不能关闭 unrestricted noncanonical 源 lane。",
            f"{SOURCE_AXIOM} OR {SPECTRAL_INPUT}",
        ),
        row(
            "CDependentSpectralInputPinned",
            spectral_pinned,
            spectral_accepted,
            "外部/新深定理 lane 已精确压到 c-dependent completed residue weight 谱抵消。",
            SPECTRAL_INPUT,
        ),
        row(
            "CDependentSpectralInputReducedToCommonCore",
            cdep_reduced,
            False,
            "若不把 c-dependent 谱抵消作为外部定理接受，它经有限 Fourier/BWFD/BSC/KFLS 回到 NC-BLK common core。",
            NCBLK_COMMON_CORE,
        ),
        row(
            "NCBLKCommonCoreAlignedToExactEntropyOrExternal",
            ncblk_aligned,
            False,
            "NC-BLK common core 已对齐为 exact full-S non-AP 源熵或精确外部 DI/BFI/Kuznetsov 匹配。",
            EXACT_ENTROPY_OR_EXTERNAL,
        ),
        row(
            "ExactSourceEntropyReducedToFactorSupportPackage",
            exact_entropy_reduced,
            False,
            "exact full-S 源熵已降为精确 u/v 因子支撑、balanced range 阈值和 Type/Fourier 容量兼容。",
            FACTOR_SUPPORT_OR_EXTERNAL,
        ),
        row(
            "BalancedRangeThresholdClosed",
            range_closed and support_capacity_terminal,
            True,
            "full-S regime 中 U,V 多项式级大于任意固定对数阈值，balanced range 不再是终端硬点。",
            SUPPORT_CAPACITY_OR_EXTERNAL,
        ),
        row(
            "SupportCapacityMergedToSourceAntiAtom",
            antiatom_terminal,
            False,
            "精确因子支撑与 Type/Fourier 容量兼容合并为最终 source capacity measure 无 moving same-(u,v) 原子的合同。",
            SOURCE_ANTIATOM_OR_EXTERNAL,
        ),
        row(
            "RankinSubledgerNoLongerTheOpenPromotionPart",
            rankin_subledger_closed,
            False,
            "Rankin 子账本已变为 pass-or-return，不再是模糊缺口；失败仍回流 PDEC/SAE 或 constant-gap。",
            PROMOTION_INPUT,
        ),
        row(
            "PromotionBoundaryClosedButNotAccepted",
            promotion_boundary,
            promotion_accepted,
            "DStructure/Tail-log4/finite Rankin 晋级包边界已闭合，但当前材料未能作者侧自验收。",
            PROMOTION_INPUT,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行当前最终开放输入直接攻坚路由。"""
    final_attempt = load_json(paths["final_attempt"])
    actual_source = load_json(paths["actual_source"])
    spectral = load_json(paths["spectral"])
    cdep_reduction = load_json(paths["cdep_reduction"])
    ncblk_alignment = load_json(paths["ncblk_alignment"])
    exact_entropy_reduction = load_json(paths["exact_entropy_reduction"])
    support_range = load_json(paths["support_range"])
    source_antiatom = load_json(paths["source_antiatom"])
    full_rankin = load_json(paths["full_rankin"])
    promotion = load_json(paths["promotion"])
    rows = build_rows(
        final_attempt,
        actual_source,
        spectral,
        cdep_reduction,
        ncblk_alignment,
        exact_entropy_reduction,
        support_range,
        source_antiatom,
        full_rankin,
        promotion,
    )
    all_required = (
        actual_source.get("actual_source_antiatom_proved") is True
        or spectral.get("completed_weight_spectral_gap_closed") is True
    ) and promotion.get("promotion_package_independently_accepted") is True
    source_axiom_required = actual_source.get("self_contained_source_lane_remaining") == SOURCE_AXIOM
    direct_self_contained_target = SOURCE_ANTIATOM_CONTRACT if source_axiom_required else SOURCE_AXIOM
    factor_support_package = f"{FACTOR_SUPPORT_LOWER} AND {BALANCED_RANGE} AND {TYPE_FOURIER_COMPAT}"
    reduced_support_capacity_package = f"{FACTOR_SUPPORT_LOWER} AND {TYPE_FOURIER_COMPAT}"
    return {
        "certificate_type": "prime_matrix_final_open_input_current_attack_router",
        "status": "final_open_input_current_attack_reduced_to_exact_entropy_or_external_plus_referee_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "final_open_input_boundary_closed": True,
        "all_required_inputs_proved_or_accepted": all_required,
        "current_corpus_self_contained_source_closure_found": False,
        "current_corpus_external_spectral_closure_found": spectral.get("completed_weight_spectral_gap_closed") is True,
        "promotion_package_independently_accepted": promotion.get("promotion_package_independently_accepted") is True,
        "rankin_subledger_pass_or_return_closed": full_rankin.get("full_rankin_ledger_still_open_closed") is True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "current_self_contained_basis_if_new_source_theorem": f"{SOURCE_AXIOM} AND {PROMOTION_INPUT}",
        "current_exact_entropy_self_contained_basis": f"{EXACT_ENTROPY} AND {PROMOTION_INPUT}",
        "current_factor_support_self_contained_basis": f"{factor_support_package} AND {PROMOTION_INPUT}",
        "current_reduced_support_capacity_basis": f"{reduced_support_capacity_package} AND {PROMOTION_INPUT}",
        "current_source_antiatom_self_contained_basis": f"{SOURCE_ANTIATOM_CONTRACT} AND {PROMOTION_INPUT}",
        "current_external_or_new_deep_basis": f"{EXTERNAL_DIBFI} AND {PROMOTION_INPUT}",
        "current_final_open_input_basis": f"({SOURCE_ANTIATOM_CONTRACT} OR {EXTERNAL_DIBFI}) AND {PROMOTION_INPUT}",
        "common_core_terminal_after_cdep_reduction": EXACT_ENTROPY_OR_EXTERNAL,
        "self_contained_terminal_after_exact_entropy_reduction": FACTOR_SUPPORT_OR_EXTERNAL,
        "self_contained_terminal_after_range_closure": SUPPORT_CAPACITY_OR_EXTERNAL,
        "self_contained_terminal_after_support_capacity_merge": SOURCE_ANTIATOM_OR_EXTERNAL,
        "direct_next_self_contained_attack_target": direct_self_contained_target,
        "direct_next_attack_target_without_new_source_axiom": EXTERNAL_DIBFI,
        "parallel_referee_gate": PROMOTION_INPUT,
        "rows": rows,
        "closed_boundary_gates": [item["gate"] for item in rows if item["boundary_closed"]],
        "open_proof_or_acceptance_gates": [
            item["gate"] for item in rows if not item["proved_or_accepted"]
        ],
        "plain_conclusion": (
            "当前最终开放输入已经对齐到更窄的共同核心：c-dependent 谱输入若不作为外部定理接受，"
            "会经有限 Fourier/BWFD/BSC/KFLS 回到 actual NC-BLK，再对齐为 exact full-S non-AP 源熵；"
            "而 exact 源熵又降为精确 u/v 因子支撑包；其中 balanced range 阈值已闭合，剩余支撑与 "
            "Type/Fourier 容量兼容合并成最终 source anti-atom 合同。不新增源定理时只能攻精确外部 "
            "DI/BFI/Kuznetsov 定理匹配。两条线之后仍必须通过 "
            "DStructure/Tail-log4/finite Rankin 独立晋级验收。当前没有无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 当前最终开放输入直接攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"final_open_input_boundary_closed={fmt_bool(result['final_open_input_boundary_closed'])}",
        (
            "all_required_inputs_proved_or_accepted="
            f"{fmt_bool(result['all_required_inputs_proved_or_accepted'])}"
        ),
        (
            "rankin_subledger_pass_or_return_closed="
            f"{fmt_bool(result['rankin_subledger_pass_or_return_closed'])}"
        ),
        (
            "promotion_package_independently_accepted="
            f"{fmt_bool(result['promotion_package_independently_accepted'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 当前最小输入基",
        "",
        "```text",
        result["current_final_open_input_basis"],
        "```",
        "",
        "完全自足但需新增源定理的版本：",
        "",
        "```text",
        result["current_self_contained_basis_if_new_source_theorem"],
        "```",
        "",
        "等价 exact 源熵自足版本：",
        "",
        "```text",
        result["current_exact_entropy_self_contained_basis"],
        "```",
        "",
        "继续下压后的精确支撑包自足版本：",
        "",
        "```text",
        result["current_factor_support_self_contained_basis"],
        "```",
        "",
        "去掉已闭合 range 后的支撑/容量版本：",
        "",
        "```text",
        result["current_reduced_support_capacity_basis"],
        "```",
        "",
        "最终 source anti-atom 合同版本：",
        "",
        "```text",
        result["current_source_antiatom_self_contained_basis"],
        "```",
        "",
        "不新增源公理时的外部/新深定理版本：",
        "",
        "```text",
        result["current_external_or_new_deep_basis"],
        "```",
        "",
        "## 2. 审查表",
        "",
        "| gate | boundary closed | proved/accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary}` | `{proved}` | {meaning} | `{remaining}` |".format(
                gate=table_cell(item["gate"]),
                boundary=fmt_bool(item["boundary_closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"自足线直接最窄攻坚目标为 "
            f"`{result['direct_next_self_contained_attack_target']}`。",
            "",
            f"若不新增源头强化定理，外部线直接最窄攻坚目标为 "
            f"`{result['direct_next_attack_target_without_new_source_axiom']}`。",
            f"并行但不能作者侧替代的晋级门为 `{result['parallel_referee_gate']}`。",
            "",
            "审稿边界：本路由只关闭最终开放输入的当前边界，不证明源定理、谱定理或独立晋级验收。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-attempt", type=Path, default=DEFAULT_FINAL_ATTEMPT)
    parser.add_argument("--actual-source", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--spectral", type=Path, default=DEFAULT_SPECTRAL)
    parser.add_argument("--cdep-reduction", type=Path, default=DEFAULT_CDEP_REDUCTION)
    parser.add_argument("--ncblk-alignment", type=Path, default=DEFAULT_NCBLK_ALIGNMENT)
    parser.add_argument("--exact-entropy-reduction", type=Path, default=DEFAULT_EXACT_ENTROPY_REDUCTION)
    parser.add_argument("--support-range", type=Path, default=DEFAULT_SUPPORT_RANGE)
    parser.add_argument("--source-antiatom", type=Path, default=DEFAULT_SOURCE_ANTIATOM)
    parser.add_argument("--full-rankin", type=Path, default=DEFAULT_FULL_RANKIN)
    parser.add_argument("--promotion", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "final_attempt": args.final_attempt,
        "actual_source": args.actual_source,
        "spectral": args.spectral,
        "cdep_reduction": args.cdep_reduction,
        "ncblk_alignment": args.ncblk_alignment,
        "exact_entropy_reduction": args.exact_entropy_reduction,
        "support_range": args.support_range,
        "source_antiatom": args.source_antiatom,
        "full_rankin": args.full_rankin,
        "promotion": args.promotion,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
