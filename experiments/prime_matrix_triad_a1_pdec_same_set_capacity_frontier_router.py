#!/usr/bin/env python3
"""汇总 Triad-A1 PDEC 同集容量上界的当前前沿。

用法示例：
  python3 experiments/prime_matrix_triad_a1_pdec_same_set_capacity_frontier_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json
  docs/monograph/prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_LP = DOCS / "prime-matrix-triad-a1-lhb-lp-skeleton.json"
DEFAULT_DIRECTION = DOCS / "prime-matrix-triad-a1-lhb-direction-support-audit.json"
DEFAULT_FOURIER = DOCS / "prime-matrix-triad-a1-lhb-fourier-cap-scan.json"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MASS = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_CONFLUENCE = DOCS / "prime-matrix-triad-a1-terminal-confluence-router.json"
DEFAULT_CONTINUOUS = DOCS / "prime-matrix-triad-a1-continuous-direction-arc-dual.json"
DEFAULT_BRIDGE = DOCS / "prime-matrix-triad-a1-continuous-columntail-bridge.json"
DEFAULT_ACTUAL_PAYMENT = DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
DEFAULT_TERMINAL_DICHOTOMY = DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json"
DEFAULT_PDEC_SIGNATURE = DOCS / "prime-matrix-triad-a1-continuous-pdec-signature-input-ledger.json"
DEFAULT_PRIME_LIFT = DOCS / "prime-matrix-triad-a1-continuous-prime-lift-router.json"
DEFAULT_SELECTIVE_COMMUTATION = DOCS / "prime-matrix-triad-a1-selective-promotion-commutation.json"
DEFAULT_STANDARD_DELETION = DOCS / "prime-matrix-triad-a1-standard-prime-lift-deletion.json"
DEFAULT_NODELETION_TERMINAL = (
    DOCS / "prime-matrix-triad-a1-continuous-nodeletion-terminal-router.json"
)
DEFAULT_CLEAN_KLS_EXTERNAL = (
    DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
)
DEFAULT_KUZNETSOV_FRONTIER = (
    DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json"
)
DEFAULT_NCBLK_PROJECTION = (
    DOCS / "prime-matrix-triad-a1-ncblk-projection-gap-router.json"
)
DEFAULT_MOVING_BLOCK_OBSTRUCTION = (
    DOCS / "prime-matrix-triad-a1-moving-block-spread-obstruction.json"
)
DEFAULT_SOURCE_BLOCK_ENTROPY = (
    DOCS / "prime-matrix-triad-a1-source-block-entropy-router.json"
)
DEFAULT_EXACT_WFD_SOURCE_ENTROPY = (
    DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.json"
)
DEFAULT_EXACT_FACTOR_SUPPORT = (
    DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
)
DEFAULT_FACTOR_RESIDUE_INCIDENCE = (
    DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
)
DEFAULT_CANONICAL_RIW_SUPPORT = (
    DOCS / "prime-matrix-triad-a1-canonical-riw-support-router.json"
)
DEFAULT_SQUAREFREE_BUCHSTAB_SUPPORT = (
    DOCS / "prime-matrix-triad-a1-squarefree-buchstab-support-router.json"
)
DEFAULT_LAYER_TRANSFER = DOCS / "prime-matrix-triad-a1-layer-transfer-router.json"
DEFAULT_SELECTOR_RETENTION = DOCS / "prime-matrix-triad-a1-selector-retention-router.json"
DEFAULT_PATH_PARTITION = DOCS / "prime-matrix-triad-a1-path-partition-router.json"
DEFAULT_DECISION_TREE_FORMULA = (
    DOCS / "prime-matrix-triad-a1-decision-tree-formula-router.json"
)
DEFAULT_SOURCE_IDENTIFICATION = (
    DOCS / "prime-matrix-triad-a1-source-identification-router.json"
)
DEFAULT_SOURCE_LOCK_CONTRACT = (
    DOCS / "prime-matrix-triad-a1-source-lock-contract-router.json"
)
DEFAULT_CANONICAL_BRANCH_ADMISSION = (
    DOCS / "prime-matrix-triad-a1-canonical-branch-admission-router.json"
)
DEFAULT_BRANCH_STATEMENT_COVERAGE = (
    DOCS / "prime-matrix-triad-a1-branch-statement-coverage-router.json"
)
DEFAULT_GENERIC_WFD_DIBFI = (
    DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
)
DEFAULT_DIBFI_THEOREM_LOCATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
)
DEFAULT_DIBFI_WINDOW_MATCH = (
    DOCS / "prime-matrix-triad-a1-dibfi-window-match-router.json"
)
DEFAULT_DIBFI_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_DIBFI_TRANSFER_SCALE_CERTIFICATE = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_DIBFI_DIRECT_BFI_ATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.json"
)
DEFAULT_DIBFI_BFI_ATOM_MATCH = (
    DOCS / "prime-matrix-triad-a1-dibfi-bfi-atom-match-router.json"
)
DEFAULT_DIBFI_BFI_LEVEL_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.json"
)
DEFAULT_DIBFI_AP_RESIDUAL_IDENTITY = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-residual-identity-router.json"
)
DEFAULT_DIBFI_AP_SOURCE_BRANCH = (
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-branch-router.json"
)
DEFAULT_DIBFI_NONAP_DISPERSION = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-dispersion-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-pdec-same-set-capacity-frontier-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summarize_lp(lp: dict[str, Any]) -> dict[str, Any]:
    """汇总 LHB LP 骨架。"""
    obstruction_count = sum(
        1 for row in lp["prime_results"] if row["box_only_obstruction"]["exists"]
    )
    return {
        "q": int(lp["q"]),
        "p_count": len(lp["prime_results"]),
        "all_zero_blocks_ready": bool(lp["all_zero_blocks_ready"]),
        "box_only_global_closure": bool(lp["box_only_global_closure"]),
        "box_only_obstruction_count": obstruction_count,
        "row_generators_ready": [
            "nonnegativity",
            "phase_caps_g_le_M",
            "WHOLEDEF_zero_block",
            "BRIDGED_zero_block",
        ],
    }


def summarize_fourier(fourier: dict[str, Any]) -> dict[str, Any]:
    """汇总 Fourier cap 扫描的分类。"""
    class_counts: Counter[str] = Counter()
    for item in fourier["prime_results"]:
        for report in item["alpha_reports"]:
            class_counts.update(report["class_counts"])
    return {
        "q": int(fourier["q"]),
        "p_count": len(fourier["prime_results"]),
        "class_counts": dict(sorted(class_counts.items())),
        "has_persistent_cap": class_counts["PersistentCap"] > 0,
    }


def build_frontier_rows(
    lp: dict[str, Any],
    direction: dict[str, Any],
    fourier: dict[str, Any],
    dualcap: dict[str, Any],
    mass: dict[str, Any],
    confluence: dict[str, Any],
    continuous: dict[str, Any],
    bridge: dict[str, Any],
    actual_payment: dict[str, Any],
    terminal_dichotomy: dict[str, Any],
    pdec_signature: dict[str, Any],
    prime_lift: dict[str, Any],
    selective_commutation: dict[str, Any],
    standard_deletion: dict[str, Any],
    nodeletion_terminal: dict[str, Any],
    clean_kls_external: dict[str, Any],
    kuznetsov_frontier: dict[str, Any],
    ncblk_projection: dict[str, Any],
    moving_block_obstruction: dict[str, Any],
    source_block_entropy: dict[str, Any],
    exact_wfd_source_entropy: dict[str, Any],
    exact_factor_support: dict[str, Any],
    factor_residue_incidence: dict[str, Any],
    canonical_riw_support: dict[str, Any],
    squarefree_buchstab_support: dict[str, Any],
    layer_transfer: dict[str, Any],
    selector_retention: dict[str, Any],
    path_partition: dict[str, Any],
    decision_tree_formula: dict[str, Any],
    source_identification: dict[str, Any],
    source_lock_contract: dict[str, Any],
    canonical_branch_admission: dict[str, Any],
    branch_statement_coverage: dict[str, Any],
    generic_wfd_dibfi: dict[str, Any],
    dibfi_theorem_location: dict[str, Any],
    dibfi_window_match: dict[str, Any],
    dibfi_common_variable_table: dict[str, Any],
    dibfi_transfer_scale_certificate: dict[str, Any],
    dibfi_direct_bfi_atom: dict[str, Any],
    dibfi_bfi_atom_match: dict[str, Any],
    dibfi_bfi_level_ledger: dict[str, Any],
    dibfi_ap_residual_identity: dict[str, Any],
    dibfi_ap_source_branch: dict[str, Any],
    dibfi_nonap_dispersion: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成同集容量前沿行。"""
    lp_summary = summarize_lp(lp)
    fourier_summary = summarize_fourier(fourier)
    return [
        {
            "frontier": "SameSetAttachment",
            "status": "ready_current_lhb_branch"
            if mass["all_current_dualcap_mass_sources_verified"]
            else "attachment_gap",
            "evidence": "当前 DualCap 三族都有同一 M_Q 质量来源。",
            "next_action": "新 formal PDEC 分支仍必须先证明 S subset Z_theta。",
        },
        {
            "frontier": "ZeroBlockCapacityRows",
            "status": "closed_subbranch" if direction["all_empty"] else "nonempty",
            "evidence": (
                "WHOLEDEF/BRIDGED 与 supp(M) 交集为空。"
                if direction["all_empty"]
                else "方向支撑交集非空，需要 Sparse/Persistent 路由。"
            ),
            "next_action": "真实 PDEC 方向若落在零块并集，该 LHB 分支直接空。",
        },
        {
            "frontier": "BoxOnlyCapacity",
            "status": "structurally_insufficient"
            if not lp_summary["box_only_global_closure"]
            else "closed",
            "evidence": (
                f"{lp_summary['box_only_obstruction_count']} 个 P 都存在单相位 box-only 可行见证。"
            ),
            "next_action": "必须补方向、column/tail/cofactor、NoDeletion-KL 或 CleanKLS 行。",
        },
        {
            "frontier": "FourierCapDualFailure",
            "status": "dualcap_materialized"
            if dualcap["aggregate_class_counts"]
            else "no_dualcap",
            "evidence": (
                f"class_counts={dualcap['aggregate_class_counts']}；"
                f"route_counts={dualcap['aggregate_route_counts']}。"
            ),
            "next_action": "SparseCap 进 LocalSurvivor；Persistent/Forced 进 refined PDEC、升层或 CleanKLS。",
        },
        {
            "frontier": "CurrentPXPExit",
            "status": "closed"
            if mass["all_current_dualcap_pxp_exits_closed"]
            else "open",
            "evidence": "当前 DualCap 的 P×P 早期出口由 SparseLocalSurvivor/BTLS/LFTE 接住。",
            "next_action": "剩余不是 P 行出口，而是终端 PDEC/LocalSurvivor/CleanKLS 证书。",
        },
        {
            "frontier": "TerminalConfluence",
            "status": "no_fourth_exit"
            if confluence["no_fourth_exit_current_a1_chain"]
            else "routing_gap",
            "evidence": "APS、DualCap、升层删除、NoDeletion-KL、promotion 均汇入三终端。",
            "next_action": "直接攻三终端证书；首要为 PDEC same-set U_CRT<L_PDEC。",
        },
        {
            "frontier": "ContinuousDirectionArcDual",
            "status": "continuous_dualcap_materialized_not_closed",
            "evidence": (
                f"连续方向弧精确审计已提交；route_counts={continuous['route_counts']}；"
                f"max U_box/M={continuous['global_max_box_dual_value_over_total_m']:.6f}。"
            ),
            "next_action": "方向采样退路关闭；下一步补 column/tail/cofactor 同集结构行或转 CleanKLS。",
        },
        {
            "frontier": "ContinuousColumnTailBridge",
            "status": "actual_payment_selection_materialized",
            "evidence": (
                f"连续 cap 已接到 column-tail 暴露账本；route_counts={bridge['route_counts']}；"
                f"all_cap_recomputations_match={bridge['all_cap_recomputations_match']}。"
            ),
            "next_action": "从暴露候选桶提升到真实支付测度：集中给 PDEC，递归扩散给 CleanKLS/DLS。",
        },
        {
            "frontier": "ContinuousActualPaymentSelection",
            "status": "actual_payment_measure_constructed",
            "evidence": (
                f"canonical actual payment measure 已构造；route_counts={actual_payment['route_counts']}；"
                f"all_payment_counts_match_demand={actual_payment['all_payment_counts_match_demand']}。"
            ),
            "next_action": "终端只剩两引理：positive-limsup finite signature=>PDEC；diffuse=>CleanKLS/DLS。",
        },
        {
            "frontier": "ContinuousTerminalDichotomy",
            "status": "terminal_dichotomy_admission_closed_capacity_open",
            "evidence": (
                f"终端二分已路由；route_counts={terminal_dichotomy['route_counts']}；"
                f"open={terminal_dichotomy['open_terminal_obligations']}。"
            ),
            "next_action": "直接攻 PDEC-CAP 容量不等式，或攻/引用 KLS-EXT 大筛估计。",
        },
        {
            "frontier": "ContinuousPDECSignatureInput",
            "status": "positive_limsup_pdec_inputs_materialized_capacity_open",
            "evidence": (
                f"positive-limsup 有限签名已生成 PDEC 输入账本；"
                f"signature_rows={pdec_signature['signature_row_count']}；"
                f"route_counts={pdec_signature['route_counts']}；"
                f"min Fourier/total={pdec_signature['global_min_signature_fourier_abs_over_total']:.6f}。"
            ),
            "next_action": "对这些 g_b(t) 证明 U_CRT<L_PDEC；失败则输出更窄 DualCap/缺失行/KLS 回流。",
        },
        {
            "frontier": "ContinuousPrimeLiftCongruence",
            "status": "prime_lift_deletion_kl_ready_with_selective_commutation_gap",
            "evidence": (
                f"positive-limsup 签名均满足 prime-lift 同余；"
                f"route_counts={prime_lift['route_counts']}；"
                f"promoted_prime_counts={prime_lift['promoted_prime_counts']}。"
            ),
            "next_action": "39 行接标准晋升删除/KL；1 行补选择性晋升交换律或 cofactor-order PDEC。",
        },
        {
            "frontier": "SelectivePromotionCommutation",
            "status": "selective_promotion_resolved_by_finite_split",
            "evidence": (
                f"选择性晋升行已由 CRT 交换律有限拆分；"
                f"route_counts={selective_commutation['route_counts']}；"
                f"max_successor_count={selective_commutation['max_successor_count']}。"
            ),
            "next_action": "选择性行回到标准 prime-lift 或 diffuse KLS；继续攻标准晋升删除/KL 或 KLS-EXT。",
        },
        {
            "frontier": "StandardPrimeLiftDeletion",
            "status": "positive_deletion_potential_or_nodeletion_kl",
            "evidence": (
                f"标准 prime-lift 删除势已物化；deletion_rows={standard_deletion['deletion_row_count']}；"
                f"min_D={standard_deletion['global_min_deletion_potential_lower_bound']:.6f}；"
                f"route_counts={standard_deletion['route_counts']}。"
            ),
            "next_action": "无限标准晋升支付删除势；若删除停止则进入 NoDeletion-KL/PDEC 或 diffuse KLS。",
        },
        {
            "frontier": "ContinuousNoDeletionTerminal",
            "status": "nodeletion_terminal_routed_clean_kls_open"
            if nodeletion_terminal["no_independent_nodeletion_gap"]
            else "nodeletion_terminal_gap",
            "evidence": (
                f"NoDeletion 终端已接入 KL/PDEC/CleanKLS 门控；"
                f"route_counts={nodeletion_terminal['route_counts']}；"
                f"terminal_gap={nodeletion_terminal['terminal_dual_gap_after_router']}。"
            ),
            "next_action": "NoDeletion-KL 不再是独立出口；继续提交 CleanKLS/DLS 大筛证书或外部 KLS 输入。",
        },
        {
            "frontier": "A1CleanKLSExternalInput",
            "status": "external_kls_input_registered_self_contained_atom_open"
            if clean_kls_external["external_kls_input_registered"]
            else "clean_kls_external_input_gap",
            "evidence": (
                f"A1 clean KLS 外部输入已登记；"
                f"all_admission_verified_or_routed={clean_kls_external['all_admission_verified_or_routed']}；"
                f"terminal_gap={clean_kls_external['terminal_gap_after_router']}。"
            ),
            "next_action": "外部深定理版接入 DI/BFI/Kuznetsov；完全自足版只剩证明 Kuznetsov-LS atom (SC-9)。",
        },
        {
            "frontier": "A1KuznetsovLSAtomFrontier",
            "status": "sc9_routed_to_ncblk_or_external_dibfi"
            if kuznetsov_frontier["all_sc9_subatoms_routed"]
            else "sc9_subatom_gap",
            "evidence": (
                f"SC-9 已展开并路由；"
                f"terminal_gap={kuznetsov_frontier['terminal_gap_after_router']}；"
                f"self_contained={kuznetsov_frontier['self_contained_version_status']}。"
            ),
            "next_action": "无黑箱版直接证明 NC-BLK；外部版引用 DI/BFI 原始 dispersion 或等价窗口 KLS。",
        },
        {
            "frontier": "A1NCBLKProjectionGap",
            "status": "moving_block_spread_or_external_dibfi_required"
            if ncblk_projection["fixed_projection_gap_exists"]
            else "ncblk_projection_gap_closed",
            "evidence": (
                f"fixed-projection diffuse 到 moving-block NC-BLK 存在缺口；"
                f"terminal_gap={ncblk_projection['terminal_gap_after_router']}。"
            ),
            "next_action": "内部版证明 MovingBlockSpreadNCBLK；外部版引用带局部方差扣除的 DI/BFI dispersion。",
        },
        {
            "frontier": "A1MovingBlockSpreadObstruction",
            "status": "source_block_entropy_or_external_dibfi_required"
            if moving_block_obstruction["next_internal_target"] == "SourceBlockEntropyNCBLK"
            else "moving_block_spread_gap",
            "evidence": (
                f"MovingBlockSpread 不能由 fixed-projection diffuse 直接推出；"
                f"terminal_gap={moving_block_obstruction['terminal_gap_after_router']}。"
            ),
            "next_action": "内部版证明 SourceBlockEntropyNCBLK；外部版引用 DI/BFI 原始 dispersion。",
        },
        {
            "frontier": "A1SourceBlockEntropyRouter",
            "status": "exact_wfd_source_entropy_or_external_dibfi_required"
            if source_block_entropy["next_internal_target"] == "ExactWFDSourceEntropy"
            else "source_block_entropy_gap",
            "evidence": (
                f"SourceBlockEntropy 可推出 NC-BLK，但不能由形式 WFD 输入强制；"
                f"terminal_gap={source_block_entropy['terminal_gap_after_router']}。"
            ),
            "next_action": "内部版证明 exact WFD/source 筛权反集中；外部版引用 DI/BFI 原始 dispersion。",
        },
        {
            "frontier": "A1ExactWFDSourceEntropyRouter",
            "status": "exact_factor_support_or_external_dibfi_required"
            if exact_wfd_source_entropy["next_internal_target"]
            == "ExactFactorSupportLowerBound"
            else "exact_wfd_source_entropy_gap",
            "evidence": (
                f"ExactWFDSourceEntropy 已化为精确因子支撑下界；"
                f"terminal_gap={exact_wfd_source_entropy['terminal_gap_after_router']}。"
            ),
            "next_action": "内部版证明 exact factor support lower bound；外部版引用 DI/BFI 原始 dispersion。",
        },
        {
            "frontier": "A1ExactFactorSupportRouter",
            "status": "factor_residue_incidence_or_canonical_riw_support_required"
            if exact_factor_support["next_internal_target"]
            == "FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupport"
            else "exact_factor_support_gap",
            "evidence": (
                f"K4/K6 不能自动推出 moving factor support；"
                f"terminal_gap={exact_factor_support['terminal_gap_after_router']}。"
            ),
            "next_action": "证明 factor-residue incidence bridge，或直接证明 canonical RIW factor support。",
        },
        {
            "frontier": "A1FactorResidueIncidenceRouter",
            "status": "canonical_riw_factor_support_or_external_dibfi_required"
            if factor_residue_incidence["next_internal_target"]
            == "CanonicalRIWFactorSupportLowerBound"
            else "factor_residue_incidence_gap",
            "evidence": (
                f"朴素 incidence bridge 被内部 fiber 阻断；"
                f"terminal_gap={factor_residue_incidence['terminal_gap_after_router']}。"
            ),
            "next_action": "内部版直接证明 canonical RIW/Buchstab factor support；外部版引用 DI/BFI。",
        },
        {
            "frontier": "A1CanonicalRIWFactorSupportRouter",
            "status": "squarefree_buchstab_support_or_external_dibfi_required"
            if canonical_riw_support["next_internal_target"]
            == "SquarefreeBuchstabLayerSupportLowerBound"
            else "canonical_riw_support_gap",
            "evidence": (
                f"canonical RIW support 已化为 squarefree Buchstab 层局部支撑；"
                f"terminal_gap={canonical_riw_support['terminal_gap_after_router']}。"
            ),
            "next_action": "内部版证明 squarefree Buchstab layer support；外部版引用 DI/BFI。",
        },
        {
            "frontier": "A1SquarefreeBuchstabSupportRouter",
            "status": "layer_transfer_thin_return_or_external_dibfi_required"
            if squarefree_buchstab_support["next_internal_target"]
            == "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
            else "squarefree_buchstab_support_gap",
            "evidence": (
                f"厚区间 squarefree 计数层已由 Mertens/Buchstab 支付；"
                f"terminal_gap={squarefree_buchstab_support['terminal_gap_after_router']}。"
            ),
            "next_action": "证明 exact canonical 层承认/非零转移，并把薄或未承认块送回 PDEC/SAE；外部版引用 DI/BFI。",
        },
        {
            "frontier": "A1CanonicalLayerTransferRouter",
            "status": "selector_retention_clean_return_or_external_dibfi_required"
            if layer_transfer["next_internal_target"]
            == "CanonicalSelectorRetentionOrCleanReturn"
            else "layer_transfer_gap",
            "evidence": (
                f"exact 层转移已化为 selector 保留率或 clean 退出合同；"
                f"terminal_gap={layer_transfer['terminal_gap_after_router']}。"
            ),
            "next_action": "固定 exact RIW/Buchstab selector，证明其保留 log-power 支撑；失败块回 PDEC/SAE。",
        },
        {
            "frontier": "A1CanonicalSelectorRetentionRouter",
            "status": "finite_signature_no_cancellation_or_external_dibfi_required"
            if selector_retention["next_internal_target"]
            == "FiniteSignatureNoCancellationOrCleanReturn"
            else "selector_retention_gap",
            "evidence": (
                f"selector 保留率已化为有限签名 pigeonhole 加无抵消/退出合同；"
                f"terminal_gap={selector_retention['terminal_gap_after_router']}。"
            ),
            "next_action": "把 K6/polylog 标签提升为 exact path partition，证明无抵消；失败块回 PDEC/SAE。",
        },
        {
            "frontier": "A1PathPartitionNoCancellationRouter",
            "status": "exact_decision_tree_formula_or_external_dibfi_required"
            if path_partition["next_internal_target"]
            == "ExactRIWDecisionTreeFormulaOrCleanReturn"
            else "path_partition_gap",
            "evidence": (
                f"无抵消已化为完整 RIW/Buchstab 决策树公式与路径预算；"
                f"terminal_gap={path_partition['terminal_gap_after_router']}。"
            ),
            "next_action": "写出 canonical RIW/Buchstab exact decision-tree 系数公式；超预算或非互斥块回 PDEC/SAE。",
        },
        {
            "frontier": "A1DecisionTreeFormulaRouter",
            "status": "source_coefficient_identification_or_external_dibfi_required"
            if decision_tree_formula["next_internal_target"]
            == "ActualKZESourceCoefficientIdentificationOrCleanReturn"
            else "decision_tree_formula_gap",
            "evidence": (
                f"exact 决策树公式已化为 A1/KZ-E 源头系数识别；"
                f"terminal_gap={decision_tree_formula['terminal_gap_after_router']}。"
            ),
            "next_action": "证明实际 lambda_c 等于 canonical RIW/Buchstab 决策树系数；否则回 PDEC/SAE 或外部 DI/BFI。",
        },
        {
            "frontier": "A1SourceIdentificationRouter",
            "status": "canonical_source_lock_or_external_dibfi_required"
            if source_identification["next_internal_target"]
            == "CanonicalRIWBuchstabSourceLockContract"
            else "source_identification_gap",
            "evidence": (
                f"源头识别已化为 canonical source lock 合同；"
                f"terminal_gap={source_identification['terminal_gap_after_router']}。"
            ),
            "next_action": "锁定 KZ-E lambda_c 为 canonical RIW/Buchstab 决策树系数；否则回 PDEC/SAE 或外部 DI/BFI。",
        },
        {
            "frontier": "A1SourceLockContractRouter",
            "status": "canonical_source_branch_admission_or_external_dibfi_required"
            if source_lock_contract["next_internal_target"]
            == "A1CleanBranchCanonicalSourceAdmission"
            else "source_lock_contract_gap",
            "evidence": (
                f"source lock 已二分为 canonical 分支准入或 generic WFD 外部路由；"
                f"terminal_gap={source_lock_contract['terminal_gap_after_router']}。"
            ),
            "next_action": "证明当前 clean A1 分支使用 canonical RIW/Buchstab 源头；否则走外部 DI/BFI 或 PDEC/SAE。",
        },
        {
            "frontier": "A1CanonicalBranchAdmissionRouter",
            "status": "canonical_branch_statement_coverage_or_external_dibfi_required"
            if canonical_branch_admission["next_internal_target"]
            == "A1CanonicalSourceBranchStatementAndCoverage"
            else "canonical_branch_admission_gap",
            "evidence": (
                f"canonical 分支准入已化为主定理/账本分支陈述覆盖合同；"
                f"terminal_gap={canonical_branch_admission['terminal_gap_after_router']}。"
            ),
            "next_action": "明确 canonical 内部分支与 generic 外部分支覆盖关系；避免静默 generic 内部闭合。",
        },
        {
            "frontier": "A1BranchStatementCoverageRouter",
            "status": "canonical_source_branch_internal_gap_closed_generic_external_only"
            if branch_statement_coverage["next_internal_target"]
            == "NoFurtherInternalGapForCanonicalSourceBranch"
            else "branch_statement_coverage_gap",
            "evidence": (
                f"canonical source branch 陈述已采用；generic WFD 仅保留外部缺口；"
                f"terminal_gap={branch_statement_coverage['terminal_gap_after_router']}。"
            ),
            "next_action": "canonical 源头分支无 source-lock 内部缺口；若要求 generic WFD 自足，只剩外部 DI/BFI。",
        },
        {
            "frontier": "A1GenericWFDDIBFIRouter",
            "status": "generic_wfd_external_dibfi_contract_materialized_theorem_location_open"
            if generic_wfd_dibfi["external_dibfi_contract_materialized"]
            else "generic_wfd_dibfi_contract_gap",
            "evidence": (
                f"generic WFD 外部 DI/BFI 合同已物化；"
                f"closed_except_precise_external_citation={generic_wfd_dibfi['closed_except_precise_external_citation']}；"
                f"terminal_gap={generic_wfd_dibfi['terminal_gap_after_router']}。"
            ),
            "next_action": "核对 DI/BFI 原文精确定理位置与假设逐项匹配；不再回退到 canonical 支撑链。",
        },
        {
            "frontier": "A1DIBFITheoremLocationRouter",
            "status": "dibfi_theorem_locations_pinned_current_window_hypothesis_match_open"
            if dibfi_theorem_location["theorem_locations_pinned"]
            else "dibfi_theorem_location_gap",
            "evidence": (
                f"BFI Theorem 10 与 DI Theorem 12 已定位；"
                f"theorem_locations_pinned={dibfi_theorem_location['theorem_locations_pinned']}；"
                f"terminal_gap={dibfi_theorem_location['terminal_gap_after_router']}。"
            ),
            "next_action": "逐项证明当前未中心化 KE-13/WFD 窗口满足 BFI/DI 假设。",
        },
        {
            "frontier": "A1DIBFIWindowMatchRouter",
            "status": "dibfi_window_match_reduced_to_target_transfer_and_scale_inequalities"
            if dibfi_window_match["open_gates"]
            == ["OriginalAPToWFDTargetTransfer", "WindowScaleInequalities"]
            else "dibfi_window_match_unclassified",
            "evidence": (
                f"当前窗口匹配已压成对象转移与尺度不等式；"
                f"open_gates={dibfi_window_match['open_gates']}；"
                f"terminal_gap={dibfi_window_match['terminal_gap_after_router']}。"
            ),
            "next_action": "同时完成 AP->KE-13 对象不变转移与 C,S,H,Q,N,M 尺度不等式。",
        },
        {
            "frontier": "A1DIBFICommonVariableTableRouter",
            "status": "dibfi_common_variable_table_materialized_certificate_open"
            if dibfi_common_variable_table["no_variable_fork"]
            else "dibfi_common_variable_table_gap",
            "evidence": (
                f"DI/BFI 共同变量表已建立；"
                f"target_transfer_and_scale_share_variables="
                f"{dibfi_common_variable_table['target_transfer_and_scale_share_variables']}；"
                f"terminal_gap={dibfi_common_variable_table['terminal_gap_after_router']}。"
            ),
            "next_action": "在共同变量表上同时证明对象转移方程和尺度不等式。",
        },
        {
            "frontier": "A1DIBFITransferScaleCertificateRouter",
            "status": "dibfi_transfer_scale_certificate_reduced_to_quantified_no_projection_certificate_open"
            if not dibfi_transfer_scale_certificate["all_certificate_rows_closed"]
            else "dibfi_transfer_scale_certificate_closed",
            "evidence": (
                f"共同变量表合取证书已逐行审计；"
                f"open_transfer={dibfi_transfer_scale_certificate['open_transfer_gates']}；"
                f"open_scale={dibfi_transfer_scale_certificate['open_scale_gates']}；"
                f"terminal_gap={dibfi_transfer_scale_certificate['terminal_gap_after_router']}。"
            ),
            "next_action": "直接证明无投影未中心化 dispersion 恒等式，并完成 DI/BFI 量化窗口代入。",
        },
        {
            "frontier": "A1DIBFIDirectBFIAtomRouter",
            "status": "dibfi_quantified_no_projection_reduced_to_direct_bfi_atom_or_ke13_fallback_open",
            "evidence": (
                f"量化无投影终端已分叉为直接 BFI-AP 原子或 KE-13 fallback；"
                f"direct_bfi_atom_available={dibfi_direct_bfi_atom['direct_bfi_atom_available']}；"
                f"open_gates={dibfi_direct_bfi_atom['open_gates']}；"
                f"terminal_gap={dibfi_direct_bfi_atom['terminal_gap_after_router']}。"
            ),
            "next_action": "优先证明 PrimeAPResidualRepresentation、BFILevelSubstitution 与 WellFactorableLambdaLevel。",
        },
        {
            "frontier": "A1DIBFIBFIAtomMatchRouter",
            "status": "dibfi_direct_bfi_atom_match_reduced_to_ap_identity_and_level_ledger_open",
            "evidence": (
                f"直接 BFI 原子三门控已压成 AP 源等式与 level 指数账本；"
                f"open_terminal_targets={dibfi_bfi_atom_match['open_terminal_targets']}；"
                f"terminal_gap={dibfi_bfi_atom_match['terminal_gap_after_router']}。"
            ),
            "next_action": "直接写 OriginalResidualEqualsBFIAPError，或提交 BFILevelExponentLedger。",
        },
        {
            "frontier": "A1DIBFIBFILevelLedgerRouter",
            "status": "bfi_level_exponent_ledger_closed_ap_identity_open"
            if dibfi_bfi_level_ledger["bfi_level_exponent_ledger_closed"]
            else "bfi_level_exponent_ledger_support_normalization_open",
            "evidence": (
                f"BFI level 账本已核算；"
                f"closed={dibfi_bfi_level_ledger['bfi_level_exponent_ledger_closed']}；"
                f"open_level_gates={dibfi_bfi_level_ledger['open_level_gates']}；"
                f"terminal_gap={dibfi_bfi_level_ledger['terminal_gap_after_router']}。"
            ),
            "next_action": "直接证明 OriginalResidualEqualsBFIAPError，即原始 clean A1 残差等于 BFI prime-AP discrepancy。",
        },
        {
            "frontier": "A1DIBFIAPResidualIdentityRouter",
            "status": "ap_residual_identity_reduced_to_upstream_source_definition_open",
            "evidence": (
                f"AP 残差对象等式已压成源头定义合同；"
                f"open_gates={dibfi_ap_residual_identity['open_gates']}；"
                f"terminal_gap={dibfi_ap_residual_identity['terminal_gap_after_router']}。"
            ),
            "next_action": "在 Cauchy/dispersion 前写出 UpstreamCleanA1APSourceDefinition；失败则走 KE-13 fallback。",
        },
        {
            "frontier": "A1DIBFIAPSourceBranchRouter",
            "status": "ap_source_direct_bfi_branch_closed_nonap_fallback_open",
            "evidence": (
                f"AP-source 直接 BFI 分支已闭合；"
                f"ap_source_branch_closed={dibfi_ap_source_branch['ap_source_branch_closed']}；"
                f"open_branches={dibfi_ap_source_branch['open_branches']}；"
                f"terminal_gap={dibfi_ap_source_branch['terminal_gap_after_router']}。"
            ),
            "next_action": "若要覆盖非 AP generic WFD，必须完成原始 dispersion 外部定理假设匹配或 KE-13 无投影证明。",
        },
        {
            "frontier": "A1DIBFINonAPDispersionRouter",
            "status": "nonap_source_dispersion_reduced_to_quantified_no_projection_certificate_open",
            "evidence": (
                f"非 AP-source 已接回原始 dispersion 链；"
                f"open_terminal_targets={dibfi_nonap_dispersion['open_terminal_targets']}；"
                f"terminal_gap={dibfi_nonap_dispersion['terminal_gap_after_router']}。"
            ),
            "next_action": "直接攻 NoProjectionUncenteredDispersionIdentity 与 QuantifiedDIBFIWindowSubstitution。",
        },
    ]


def run(
    lp_path: Path,
    direction_path: Path,
    fourier_path: Path,
    dualcap_path: Path,
    mass_path: Path,
    confluence_path: Path,
    continuous_path: Path,
    bridge_path: Path,
    actual_payment_path: Path,
    terminal_dichotomy_path: Path,
    pdec_signature_path: Path,
    prime_lift_path: Path,
    selective_commutation_path: Path,
    standard_deletion_path: Path,
    nodeletion_terminal_path: Path,
    clean_kls_external_path: Path,
    kuznetsov_frontier_path: Path,
    ncblk_projection_path: Path,
    moving_block_obstruction_path: Path,
    source_block_entropy_path: Path,
    exact_wfd_source_entropy_path: Path,
    exact_factor_support_path: Path,
    factor_residue_incidence_path: Path,
    canonical_riw_support_path: Path,
    squarefree_buchstab_support_path: Path,
    layer_transfer_path: Path,
    selector_retention_path: Path,
    path_partition_path: Path,
    decision_tree_formula_path: Path,
    source_identification_path: Path,
    source_lock_contract_path: Path,
    canonical_branch_admission_path: Path,
    branch_statement_coverage_path: Path,
    generic_wfd_dibfi_path: Path,
    dibfi_theorem_location_path: Path,
    dibfi_window_match_path: Path,
    dibfi_common_variable_table_path: Path,
    dibfi_transfer_scale_certificate_path: Path,
    dibfi_direct_bfi_atom_path: Path,
    dibfi_bfi_atom_match_path: Path,
    dibfi_bfi_level_ledger_path: Path,
    dibfi_ap_residual_identity_path: Path,
    dibfi_ap_source_branch_path: Path,
    dibfi_nonap_dispersion_path: Path,
) -> dict[str, Any]:
    """运行 PDEC 同集容量前沿路由。"""
    lp = load_json(lp_path)
    direction = load_json(direction_path)
    fourier = load_json(fourier_path)
    dualcap = load_json(dualcap_path)
    mass = load_json(mass_path)
    confluence = load_json(confluence_path)
    continuous = load_json(continuous_path)
    bridge = load_json(bridge_path)
    actual_payment = load_json(actual_payment_path)
    terminal_dichotomy = load_json(terminal_dichotomy_path)
    pdec_signature = load_json(pdec_signature_path)
    prime_lift = load_json(prime_lift_path)
    selective_commutation = load_json(selective_commutation_path)
    standard_deletion = load_json(standard_deletion_path)
    nodeletion_terminal = load_json(nodeletion_terminal_path)
    clean_kls_external = load_json(clean_kls_external_path)
    kuznetsov_frontier = load_json(kuznetsov_frontier_path)
    ncblk_projection = load_json(ncblk_projection_path)
    moving_block_obstruction = load_json(moving_block_obstruction_path)
    source_block_entropy = load_json(source_block_entropy_path)
    exact_wfd_source_entropy = load_json(exact_wfd_source_entropy_path)
    exact_factor_support = load_json(exact_factor_support_path)
    factor_residue_incidence = load_json(factor_residue_incidence_path)
    canonical_riw_support = load_json(canonical_riw_support_path)
    squarefree_buchstab_support = load_json(squarefree_buchstab_support_path)
    layer_transfer = load_json(layer_transfer_path)
    selector_retention = load_json(selector_retention_path)
    path_partition = load_json(path_partition_path)
    decision_tree_formula = load_json(decision_tree_formula_path)
    source_identification = load_json(source_identification_path)
    source_lock_contract = load_json(source_lock_contract_path)
    canonical_branch_admission = load_json(canonical_branch_admission_path)
    branch_statement_coverage = load_json(branch_statement_coverage_path)
    generic_wfd_dibfi = load_json(generic_wfd_dibfi_path)
    dibfi_theorem_location = load_json(dibfi_theorem_location_path)
    dibfi_window_match = load_json(dibfi_window_match_path)
    dibfi_common_variable_table = load_json(dibfi_common_variable_table_path)
    dibfi_transfer_scale_certificate = load_json(dibfi_transfer_scale_certificate_path)
    dibfi_direct_bfi_atom = load_json(dibfi_direct_bfi_atom_path)
    dibfi_bfi_atom_match = load_json(dibfi_bfi_atom_match_path)
    dibfi_bfi_level_ledger = load_json(dibfi_bfi_level_ledger_path)
    dibfi_ap_residual_identity = load_json(dibfi_ap_residual_identity_path)
    dibfi_ap_source_branch = load_json(dibfi_ap_source_branch_path)
    dibfi_nonap_dispersion = load_json(dibfi_nonap_dispersion_path)
    frontier_rows = build_frontier_rows(
        lp,
        direction,
        fourier,
        dualcap,
        mass,
        confluence,
        continuous,
        bridge,
        actual_payment,
        terminal_dichotomy,
        pdec_signature,
        prime_lift,
        selective_commutation,
        standard_deletion,
        nodeletion_terminal,
        clean_kls_external,
        kuznetsov_frontier,
        ncblk_projection,
        moving_block_obstruction,
        source_block_entropy,
        exact_wfd_source_entropy,
        exact_factor_support,
        factor_residue_incidence,
        canonical_riw_support,
        squarefree_buchstab_support,
        layer_transfer,
        selector_retention,
        path_partition,
        decision_tree_formula,
        source_identification,
        source_lock_contract,
        canonical_branch_admission,
        branch_statement_coverage,
        generic_wfd_dibfi,
        dibfi_theorem_location,
        dibfi_window_match,
        dibfi_common_variable_table,
        dibfi_transfer_scale_certificate,
        dibfi_direct_bfi_atom,
        dibfi_bfi_atom_match,
        dibfi_bfi_level_ledger,
        dibfi_ap_residual_identity,
        dibfi_ap_source_branch,
        dibfi_nonap_dispersion,
    )
    status_counts = Counter(row["status"] for row in frontier_rows)
    ready_or_routed = {
        "ready_current_lhb_branch",
        "closed_subbranch",
        "structurally_insufficient",
        "dualcap_materialized",
        "continuous_dualcap_materialized_not_closed",
        "actual_payment_selection_materialized",
        "actual_payment_measure_constructed",
        "terminal_dichotomy_admission_closed_capacity_open",
        "positive_limsup_pdec_inputs_materialized_capacity_open",
        "prime_lift_deletion_kl_ready_with_selective_commutation_gap",
        "selective_promotion_resolved_by_finite_split",
        "positive_deletion_potential_or_nodeletion_kl",
        "nodeletion_terminal_routed_clean_kls_open",
        "external_kls_input_registered_self_contained_atom_open",
        "sc9_routed_to_ncblk_or_external_dibfi",
        "moving_block_spread_or_external_dibfi_required",
        "source_block_entropy_or_external_dibfi_required",
        "exact_wfd_source_entropy_or_external_dibfi_required",
        "exact_factor_support_or_external_dibfi_required",
        "factor_residue_incidence_or_canonical_riw_support_required",
        "canonical_riw_factor_support_or_external_dibfi_required",
        "squarefree_buchstab_support_or_external_dibfi_required",
        "layer_transfer_thin_return_or_external_dibfi_required",
        "selector_retention_clean_return_or_external_dibfi_required",
        "finite_signature_no_cancellation_or_external_dibfi_required",
        "exact_decision_tree_formula_or_external_dibfi_required",
        "source_coefficient_identification_or_external_dibfi_required",
        "canonical_source_lock_or_external_dibfi_required",
        "canonical_source_branch_admission_or_external_dibfi_required",
        "canonical_branch_statement_coverage_or_external_dibfi_required",
        "canonical_source_branch_internal_gap_closed_generic_external_only",
        "generic_wfd_external_dibfi_contract_materialized_theorem_location_open",
        "dibfi_theorem_locations_pinned_current_window_hypothesis_match_open",
        "dibfi_window_match_reduced_to_target_transfer_and_scale_inequalities",
        "dibfi_common_variable_table_materialized_certificate_open",
        "dibfi_transfer_scale_certificate_reduced_to_quantified_no_projection_certificate_open",
        "dibfi_transfer_scale_certificate_closed",
        "dibfi_quantified_no_projection_reduced_to_direct_bfi_atom_or_ke13_fallback_open",
        "dibfi_direct_bfi_atom_match_reduced_to_ap_identity_and_level_ledger_open",
        "bfi_level_exponent_ledger_closed_ap_identity_open",
        "bfi_level_exponent_ledger_support_normalization_open",
        "ap_residual_identity_reduced_to_upstream_source_definition_open",
        "ap_source_direct_bfi_branch_closed_nonap_fallback_open",
        "nonap_source_dispersion_reduced_to_quantified_no_projection_certificate_open",
        "closed",
        "no_fourth_exit",
    }
    all_known_frontiers_routed = all(row["status"] in ready_or_routed for row in frontier_rows)
    return {
        "certificate_type": "triad_a1_pdec_same_set_capacity_frontier_router",
        "status": "same_set_capacity_frontier_materialized_nonap_quantified_no_projection_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "lhb_lp_skeleton_json": file_sha256(lp_path),
            "direction_support_json": file_sha256(direction_path),
            "fourier_cap_scan_json": file_sha256(fourier_path),
            "dualcap_extractor_json": file_sha256(dualcap_path),
            "pdec_mass_source_json": file_sha256(mass_path),
            "terminal_confluence_json": file_sha256(confluence_path),
            "continuous_direction_arc_json": file_sha256(continuous_path),
            "continuous_columntail_bridge_json": file_sha256(bridge_path),
            "continuous_actual_payment_selection_json": file_sha256(actual_payment_path),
            "continuous_terminal_dichotomy_json": file_sha256(terminal_dichotomy_path),
            "continuous_pdec_signature_input_json": file_sha256(pdec_signature_path),
            "continuous_prime_lift_json": file_sha256(prime_lift_path),
            "selective_promotion_commutation_json": file_sha256(selective_commutation_path),
            "standard_prime_lift_deletion_json": file_sha256(standard_deletion_path),
            "continuous_nodeletion_terminal_json": file_sha256(nodeletion_terminal_path),
            "a1_clean_kls_external_input_json": file_sha256(clean_kls_external_path),
            "a1_kuznetsov_ls_atom_frontier_json": file_sha256(kuznetsov_frontier_path),
            "a1_ncblk_projection_gap_json": file_sha256(ncblk_projection_path),
            "a1_moving_block_spread_obstruction_json": file_sha256(
                moving_block_obstruction_path
            ),
            "a1_source_block_entropy_json": file_sha256(source_block_entropy_path),
            "a1_exact_wfd_source_entropy_json": file_sha256(
                exact_wfd_source_entropy_path
            ),
            "a1_exact_factor_support_json": file_sha256(exact_factor_support_path),
            "a1_factor_residue_incidence_json": file_sha256(
                factor_residue_incidence_path
            ),
            "a1_canonical_riw_support_json": file_sha256(canonical_riw_support_path),
            "a1_squarefree_buchstab_support_json": file_sha256(
                squarefree_buchstab_support_path
            ),
            "a1_layer_transfer_json": file_sha256(layer_transfer_path),
            "a1_selector_retention_json": file_sha256(selector_retention_path),
            "a1_path_partition_json": file_sha256(path_partition_path),
            "a1_decision_tree_formula_json": file_sha256(decision_tree_formula_path),
            "a1_source_identification_json": file_sha256(source_identification_path),
            "a1_source_lock_contract_json": file_sha256(source_lock_contract_path),
            "a1_canonical_branch_admission_json": file_sha256(
                canonical_branch_admission_path
            ),
            "a1_branch_statement_coverage_json": file_sha256(
                branch_statement_coverage_path
            ),
            "a1_generic_wfd_dibfi_json": file_sha256(generic_wfd_dibfi_path),
            "a1_dibfi_theorem_location_json": file_sha256(
                dibfi_theorem_location_path
            ),
            "a1_dibfi_window_match_json": file_sha256(dibfi_window_match_path),
            "a1_dibfi_common_variable_table_json": file_sha256(
                dibfi_common_variable_table_path
            ),
            "a1_dibfi_transfer_scale_certificate_json": file_sha256(
                dibfi_transfer_scale_certificate_path
            ),
            "a1_dibfi_direct_bfi_atom_json": file_sha256(
                dibfi_direct_bfi_atom_path
            ),
            "a1_dibfi_bfi_atom_match_json": file_sha256(
                dibfi_bfi_atom_match_path
            ),
            "a1_dibfi_bfi_level_ledger_json": file_sha256(
                dibfi_bfi_level_ledger_path
            ),
            "a1_dibfi_ap_residual_identity_json": file_sha256(
                dibfi_ap_residual_identity_path
            ),
            "a1_dibfi_ap_source_branch_json": file_sha256(
                dibfi_ap_source_branch_path
            ),
            "a1_dibfi_nonap_dispersion_json": file_sha256(
                dibfi_nonap_dispersion_path
            ),
        },
        "lp_summary": summarize_lp(lp),
        "fourier_summary": summarize_fourier(fourier),
        "dualcap_summary": {
            "aggregate_class_counts": dualcap["aggregate_class_counts"],
            "aggregate_route_counts": dualcap["aggregate_route_counts"],
        },
        "frontier_rows": frontier_rows,
        "status_counts": dict(sorted(status_counts.items())),
        "all_known_frontiers_routed": all_known_frontiers_routed,
        "terminal_dual_gap": "DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource",
        "structural_law": (
            "同集容量上界只允许作用在同一个 g(t) 上。当前 LHB 分支的 Attachment、零块容量行、"
            "DualCap 输出、P×P 出口和终端回流均已接线；box-only 行结构上不足，"
            "连续方向弧精确审计已排除离散采样不足这一退路；连续 cap 也已接到 column-tail 暴露账本。"
            "actual payment measure 已由 canonical 选择律构造，终端投影塔二分也已闭合。"
            "positive-limsup 有限签名的 PDEC 输入账本已物化。"
            "这些签名又进一步满足 prime-lift 同余；唯一选择性晋升已由 CRT 交换律有限拆分；"
            "标准 prime-lift 已接入正删除势；删除势停止后的 NoDeletion 口也已路由到"
            " KL/PDEC 或 CleanKLS/DLS。A1 clean KLS 外部输入也已登记："
            "外部深定理版接入窗口化 DI/BFI/Kuznetsov；SC-9 又已展开到 KZ-A--KZ-E，"
            "NC-BLK 又被核查为 fixed-projection diffuse 到 moving-block spread 的真实缺口。"
            "MovingBlockSpread 进一步被投影不可见模型阻断。SourceBlockEntropy 可推出 NC-BLK，"
            "但形式 WFD/Type-I-II/Fourier 输入不强制该熵。ExactWFDSourceEntropy 又被压缩为"
            "精确因子支撑下界；ExactFactorSupport 又被 K4/K6 投影错配模型阻断。"
            "朴素 FactorResidueIncidenceBridge 又被内部 fiber 阻断。"
            "CanonicalRIWFactorSupportLowerBound 又被压缩为 squarefree Buchstab 层局部支撑下界。"
            "Squarefree Buchstab 的厚区间计数层已由 Mertens/Buchstab 支付；"
            "exact 层承认与非零转移已进一步化为 canonical selector 保留率或 clean 退出合同；"
            "selector 保留率又被 finite-signature pigeonhole 压成 exact path partition、无抵消与 clean 退出；"
            "无抵消进一步化为完整 RIW/Buchstab 决策树公式、路径数预算与 clean 退出；"
            "决策树公式本身又被压成 A1/KZ-E 实际源头系数识别；"
            "实际源头识别又被压成 canonical RIW/Buchstab source lock 合同；"
            "source lock 合同已严格二分为 canonical 源头分支准入或 generic WFD 外部路由；"
            "canonical 分支准入又被压成主定理/账本分支陈述与覆盖合同；"
            "分支陈述已落实：canonical source branch 在 source-lock 链条上无剩余内部缺口；"
            "generic WFD 宽口径的外部 DI/BFI 原始 dispersion 已物化为外部合同；"
            "DI/BFI 原文定理位置已定位为 BFI Theorem 10 与 DI Theorem 12；"
            "当前窗口假设匹配又被压成 AP 到 KE-13 的对象不变转移与 dyadic 尺度不等式；"
            "二者现在已锁到同一张共同变量表；共同变量表合取证书又被逐行审计为"
            "无投影未中心化 dispersion 恒等式与 DI/BFI 量化窗口代入；该终端又分叉为"
            "直接 BFI prime-AP 原子匹配，或保留 KE-13 无投影 fallback；直接 BFI 原子匹配"
            "又被压成 AP 源对象等式和 BFI level 指数账本；BFI level 指数账本在"
            "X≈P^2、Q<=P log^O P 与 well-factorable support 下已有正指数余量，"
            "所以最窄剩余变为 AP 源对象等式；AP 源对象等式又被压成 Cauchy/dispersion "
            "之前的原始 clean A1 残差定义合同；该合同作为 AP-source 分支已经允许直接 BFI "
            "闭合，非 AP generic WFD 分支则必须走原始 dispersion 外部定理匹配或 KE-13 fallback；"
            "非 AP 分支已接回既有原始 dispersion 链条，剩余为量化无投影窗口证书。"
        ),
        "review_conclusion": (
            "Triad-A1 的 PDEC same-set capacity 已被压到一个明确前沿："
            "当前合法行足以闭合零块子支并输出/路由 DualCap，连续方向弧也已精确物化为 persistent cap，"
            "连续 cap 已接入 column-tail 暴露账本，且 canonical actual payment measure 已精确构造。"
            "终端二分已说明没有第三出口；positive-limsup 分支也已生成具体 PDEC 输入行。"
            "prime-lift 刚性显示这些输入可升层路由，选择性晋升也已回到有限拆分，"
            "标准晋升支付正删除势；NoDeletion-KL 已作为独立出口消除。"
            "A1 clean KLS 外部输入已登记，SC-9 也已展开路由到 NC-BLK/外部 DI-BFI。"
            "NC-BLK 的 fixed-projection 到 moving-block 缺口也已命名。"
            "MovingBlockSpread 不能由 fixed-projection diffuse 直接推出。"
            "SourceBlockEntropy 虽能推出 NC-BLK，但不由当前形式 WFD 输入自动推出。"
            "ExactWFDSourceEntropy 已化为精确因子支撑下界。"
            "ExactFactorSupport 不能由 K4/K6 自动推出。"
            "FactorResidueIncidenceBridge 的朴素形式也被内部 fiber 阻断。"
            "CanonicalRIWFactorSupportLowerBound 已化为 squarefree Buchstab 层局部支撑下界。"
            "Squarefree Buchstab 的普通厚区间计数层已被压下去。"
            "exact 层转移又被压缩为 selector 保留率/clean 退出合同。"
            "selector 保留率已由有限签名 pigeonhole 处理到条件形式。"
            "无抵消已被决策树分割条件化。"
            "决策树公式已被压成源头系数识别。"
            "源头识别又被压成 canonical source lock 合同。"
            "source lock 已分裂成 canonical 内部分支和 generic WFD 外部分支。"
            "canonical 分支准入已被压成 theorem/ledger 分支陈述覆盖合同。"
            "分支陈述覆盖已落实。canonical RIW/Buchstab clean branch 在当前 source-lock 链条上"
            "不再有内部缺口。generic noncanonical WFD 的外部 DI/BFI 合同也已物化："
            "未中心化原始对象、相位归一化、well-factorable level、Type-I/II 范围与损失账本"
            "都已登记。DI/BFI 定理位置已进一步固定为 BFI Theorem 10 与 DI Theorem 12；"
            "当前 KE-13/WFD 窗口假设匹配已化为共同变量表上的单一合取证书："
            "对象不变转移与尺度不等式必须在同一变量表上同时成立。"
            "该合取证书现已继续压成 "
            "`DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 PDEC 同集容量前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "Same-set capacity upper:",
        "  only rows on the same g(t) are legal；",
        "  box-only rows are insufficient；",
        "  failure must output DualCap or missing row；",
        "  continuous cap exposes column-tail payment buckets；",
        "  canonical actual payment measure is constructed；",
        "  actual payment concentration returns to PDEC；",
        "  recursive diffusion returns to CleanKLS/DLS；",
        "  no third terminal route remains after finite-projection dichotomy；",
        "  positive-limsup finite signatures materialize legal PDEC input rows；",
        "  finite signatures force prime-lift congruence rows；",
        "  selective promotion commutes after finite splitting；",
        "  standard prime-lift pays positive deletion potential；",
        "  NoDeletion-KL is routed to recursive PDEC or CleanKLS/DLS；",
        "  A1 clean KLS is reduced to Kuznetsov-LS atom or external citation；",
        "  SC-9 is reduced to NC-BLK or external DI/BFI dispersion；",
        "  NC-BLK needs moving-block spread or external original dispersion；",
        "  MovingBlockSpread needs source-block entropy or external DI/BFI；",
        "  SourceBlockEntropy needs exact WFD source entropy or external DI/BFI；",
        "  ExactWFDSourceEntropy needs exact factor support lower bound or external DI/BFI；",
        "  ExactFactorSupport needs factor-residue incidence or canonical RIW support；",
        "  FactorResidueIncidence is blocked; remaining internal target is canonical RIW support；",
        "  CanonicalRIW support reduces to squarefree Buchstab layer support；",
        "  thick squarefree Buchstab counting is paid; exact layer transfer and thin return remain；",
        "  layer transfer reduces to canonical selector retention or clean return；",
        "  selector retention reduces to finite signatures, no-cancellation and clean return；",
        "  no-cancellation reduces to exact RIW/Buchstab decision tree formula or clean return；",
        "  decision-tree formula reduces to A1/KZ-E source coefficient identification；",
        "  source identification reduces to canonical RIW/Buchstab source lock contract；",
        "  source lock contract splits into canonical source branch admission or generic external route；",
        "  canonical branch admission reduces to theorem/ledger branch statement and coverage；",
        "  canonical source branch now has no source-lock internal gap;",
        "  generic WFD external DI/BFI contract is materialized;",
        "  DI/BFI theorem locations are pinned;",
        "  current WFD-window match reduces to target transfer and scale inequalities。",
        "  target transfer and scale inequalities now share one common variable table。",
        "  common-variable certificate reduces to quantified no-projection window certificate。",
        "  quantified no-projection terminal reduces to direct BFI-AP atom or KE-13 fallback。",
        "  direct BFI-AP atom match reduces to AP identity and BFI level ledger。",
        "  BFI level ledger has exponent slack; remaining gap is AP source identity。",
        "  AP source identity reduces to upstream clean A1 AP source definition。",
        "  AP-source branch closes by direct BFI; non-AP source returns to original dispersion match。",
        "  non-AP source dispersion match reduces to quantified no-projection window certificate。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `all_known_frontiers_routed={result['all_known_frontiers_routed']}`。",
        f"- `terminal_dual_gap={result['terminal_dual_gap']}`。",
        f"- `status_counts={result['status_counts']}`。",
        f"- `lp_summary={result['lp_summary']}`。",
        f"- `fourier_summary={result['fourier_summary']}`。",
        f"- `dualcap_summary={result['dualcap_summary']}`。",
        "",
        "## 3. 前沿表",
        "",
        "| frontier | status | evidence | next action |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["frontier_rows"]:
        lines.append(
            "| `{frontier}` | `{status}` | {evidence} | {next_action} |".format(
                frontier=row["frontier"],
                status=row["status"],
                evidence=row["evidence"],
                next_action=row["next_action"],
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "A1 的同集容量上界已经不再是一个模糊缺口。当前状态是：",
            "",
            "```text",
            "Attachment ready for current LHB branch；",
            "zero-block subbranch closed；",
            "box-only structurally insufficient；",
            "DualCap materialized and routed；",
            "P×P exits closed；",
            "no fourth exit in current A1 chain；",
            "continuous direction-arc dual materialized but not closed；",
            "continuous column-tail bridge materialized；",
            "canonical actual payment measure constructed；",
            "terminal finite-projection dichotomy closed；",
            "positive-limsup PDEC input rows materialized；",
            "prime-lift congruence routed；",
            "selective promotion commutation resolved；",
            "standard prime-lift deletion potential materialized；",
            "NoDeletion terminal routed；",
            "A1 clean KLS external input registered；",
            "SC-9 routed to NC-BLK / external DI-BFI；",
            "NC-BLK projection gap named；",
            "MovingBlockSpread obstruction materialized；",
            "SourceBlockEntropy router materialized；",
            "ExactWFDSourceEntropy router materialized；",
            "ExactFactorSupport router materialized；",
            "FactorResidueIncidence router materialized；",
            "CanonicalRIWFactorSupport router materialized；",
            "SquarefreeBuchstabSupport router materialized；",
            "CanonicalLayerTransfer router materialized；",
            "CanonicalSelectorRetention router materialized；",
            "PathPartitionNoCancellation router materialized；",
            "DecisionTreeFormula router materialized；",
            "SourceIdentification router materialized；",
            "SourceLockContract router materialized；",
            "CanonicalBranchAdmission router materialized；",
            "BranchStatementCoverage router materialized；",
            "GenericWFDDIBFI router materialized；",
            "DIBFITheoremLocation router materialized；",
            "DIBFIWindowMatch router materialized；",
            "DIBFICommonVariableTable router materialized；",
            "DIBFITransferScaleCertificate router materialized；",
            "DIBFIDirectBFIAtom router materialized；",
            "DIBFIBFIAtomMatch router materialized；",
            "DIBFIBFILevelLedger router materialized；",
            "DIBFIAPResidualIdentity router materialized；",
            "DIBFIAPSourceBranch router materialized；",
            "DIBFINonAPDispersion router materialized；",
            "remaining independent gap is DIBFIQuantifiedNoProjectionWindowCertificateForNonAPSource。",
            "```",
            "",
            "因此 canonical RIW/Buchstab source branch 的 source-lock 链条已闭合；",
            "DI/BFI 定理位置已固定为 BFI Theorem 10 与 DI Theorem 12；"
            "AP-source 直接 BFI 分支已闭合；非 AP generic WFD 外部引用版剩量化无投影窗口证书；"
            "完全自足版仍未证明原始 dispersion。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lp-json", type=Path, default=DEFAULT_LP)
    parser.add_argument("--direction-json", type=Path, default=DEFAULT_DIRECTION)
    parser.add_argument("--fourier-json", type=Path, default=DEFAULT_FOURIER)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--mass-json", type=Path, default=DEFAULT_MASS)
    parser.add_argument("--confluence-json", type=Path, default=DEFAULT_CONFLUENCE)
    parser.add_argument("--continuous-json", type=Path, default=DEFAULT_CONTINUOUS)
    parser.add_argument("--bridge-json", type=Path, default=DEFAULT_BRIDGE)
    parser.add_argument("--actual-payment-json", type=Path, default=DEFAULT_ACTUAL_PAYMENT)
    parser.add_argument(
        "--terminal-dichotomy-json", type=Path, default=DEFAULT_TERMINAL_DICHOTOMY
    )
    parser.add_argument("--pdec-signature-json", type=Path, default=DEFAULT_PDEC_SIGNATURE)
    parser.add_argument("--prime-lift-json", type=Path, default=DEFAULT_PRIME_LIFT)
    parser.add_argument(
        "--selective-commutation-json", type=Path, default=DEFAULT_SELECTIVE_COMMUTATION
    )
    parser.add_argument("--standard-deletion-json", type=Path, default=DEFAULT_STANDARD_DELETION)
    parser.add_argument(
        "--nodeletion-terminal-json", type=Path, default=DEFAULT_NODELETION_TERMINAL
    )
    parser.add_argument(
        "--clean-kls-external-json", type=Path, default=DEFAULT_CLEAN_KLS_EXTERNAL
    )
    parser.add_argument(
        "--kuznetsov-frontier-json", type=Path, default=DEFAULT_KUZNETSOV_FRONTIER
    )
    parser.add_argument(
        "--ncblk-projection-json", type=Path, default=DEFAULT_NCBLK_PROJECTION
    )
    parser.add_argument(
        "--moving-block-obstruction-json",
        type=Path,
        default=DEFAULT_MOVING_BLOCK_OBSTRUCTION,
    )
    parser.add_argument(
        "--source-block-entropy-json",
        type=Path,
        default=DEFAULT_SOURCE_BLOCK_ENTROPY,
    )
    parser.add_argument(
        "--exact-wfd-source-entropy-json",
        type=Path,
        default=DEFAULT_EXACT_WFD_SOURCE_ENTROPY,
    )
    parser.add_argument(
        "--exact-factor-support-json",
        type=Path,
        default=DEFAULT_EXACT_FACTOR_SUPPORT,
    )
    parser.add_argument(
        "--factor-residue-incidence-json",
        type=Path,
        default=DEFAULT_FACTOR_RESIDUE_INCIDENCE,
    )
    parser.add_argument(
        "--canonical-riw-support-json",
        type=Path,
        default=DEFAULT_CANONICAL_RIW_SUPPORT,
    )
    parser.add_argument(
        "--squarefree-buchstab-support-json",
        type=Path,
        default=DEFAULT_SQUAREFREE_BUCHSTAB_SUPPORT,
    )
    parser.add_argument("--layer-transfer-json", type=Path, default=DEFAULT_LAYER_TRANSFER)
    parser.add_argument(
        "--selector-retention-json", type=Path, default=DEFAULT_SELECTOR_RETENTION
    )
    parser.add_argument("--path-partition-json", type=Path, default=DEFAULT_PATH_PARTITION)
    parser.add_argument(
        "--decision-tree-formula-json",
        type=Path,
        default=DEFAULT_DECISION_TREE_FORMULA,
    )
    parser.add_argument(
        "--source-identification-json",
        type=Path,
        default=DEFAULT_SOURCE_IDENTIFICATION,
    )
    parser.add_argument(
        "--source-lock-contract-json",
        type=Path,
        default=DEFAULT_SOURCE_LOCK_CONTRACT,
    )
    parser.add_argument(
        "--canonical-branch-admission-json",
        type=Path,
        default=DEFAULT_CANONICAL_BRANCH_ADMISSION,
    )
    parser.add_argument(
        "--branch-statement-coverage-json",
        type=Path,
        default=DEFAULT_BRANCH_STATEMENT_COVERAGE,
    )
    parser.add_argument(
        "--generic-wfd-dibfi-json",
        type=Path,
        default=DEFAULT_GENERIC_WFD_DIBFI,
    )
    parser.add_argument(
        "--dibfi-theorem-location-json",
        type=Path,
        default=DEFAULT_DIBFI_THEOREM_LOCATION,
    )
    parser.add_argument(
        "--dibfi-window-match-json",
        type=Path,
        default=DEFAULT_DIBFI_WINDOW_MATCH,
    )
    parser.add_argument(
        "--dibfi-common-variable-table-json",
        type=Path,
        default=DEFAULT_DIBFI_COMMON_VARIABLE_TABLE,
    )
    parser.add_argument(
        "--dibfi-transfer-scale-certificate-json",
        type=Path,
        default=DEFAULT_DIBFI_TRANSFER_SCALE_CERTIFICATE,
    )
    parser.add_argument(
        "--dibfi-direct-bfi-atom-json",
        type=Path,
        default=DEFAULT_DIBFI_DIRECT_BFI_ATOM,
    )
    parser.add_argument(
        "--dibfi-bfi-atom-match-json",
        type=Path,
        default=DEFAULT_DIBFI_BFI_ATOM_MATCH,
    )
    parser.add_argument(
        "--dibfi-bfi-level-ledger-json",
        type=Path,
        default=DEFAULT_DIBFI_BFI_LEVEL_LEDGER,
    )
    parser.add_argument(
        "--dibfi-ap-residual-identity-json",
        type=Path,
        default=DEFAULT_DIBFI_AP_RESIDUAL_IDENTITY,
    )
    parser.add_argument(
        "--dibfi-ap-source-branch-json",
        type=Path,
        default=DEFAULT_DIBFI_AP_SOURCE_BRANCH,
    )
    parser.add_argument(
        "--dibfi-nonap-dispersion-json",
        type=Path,
        default=DEFAULT_DIBFI_NONAP_DISPERSION,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        lp_path=args.lp_json,
        direction_path=args.direction_json,
        fourier_path=args.fourier_json,
        dualcap_path=args.dualcap_json,
        mass_path=args.mass_json,
        confluence_path=args.confluence_json,
        continuous_path=args.continuous_json,
        bridge_path=args.bridge_json,
        actual_payment_path=args.actual_payment_json,
        terminal_dichotomy_path=args.terminal_dichotomy_json,
        pdec_signature_path=args.pdec_signature_json,
        prime_lift_path=args.prime_lift_json,
        selective_commutation_path=args.selective_commutation_json,
        standard_deletion_path=args.standard_deletion_json,
        nodeletion_terminal_path=args.nodeletion_terminal_json,
        clean_kls_external_path=args.clean_kls_external_json,
        kuznetsov_frontier_path=args.kuznetsov_frontier_json,
        ncblk_projection_path=args.ncblk_projection_json,
        moving_block_obstruction_path=args.moving_block_obstruction_json,
        source_block_entropy_path=args.source_block_entropy_json,
        exact_wfd_source_entropy_path=args.exact_wfd_source_entropy_json,
        exact_factor_support_path=args.exact_factor_support_json,
        factor_residue_incidence_path=args.factor_residue_incidence_json,
        canonical_riw_support_path=args.canonical_riw_support_json,
        squarefree_buchstab_support_path=args.squarefree_buchstab_support_json,
        layer_transfer_path=args.layer_transfer_json,
        selector_retention_path=args.selector_retention_json,
        path_partition_path=args.path_partition_json,
        decision_tree_formula_path=args.decision_tree_formula_json,
        source_identification_path=args.source_identification_json,
        source_lock_contract_path=args.source_lock_contract_json,
        canonical_branch_admission_path=args.canonical_branch_admission_json,
        branch_statement_coverage_path=args.branch_statement_coverage_json,
        generic_wfd_dibfi_path=args.generic_wfd_dibfi_json,
        dibfi_theorem_location_path=args.dibfi_theorem_location_json,
        dibfi_window_match_path=args.dibfi_window_match_json,
        dibfi_common_variable_table_path=args.dibfi_common_variable_table_json,
        dibfi_transfer_scale_certificate_path=args.dibfi_transfer_scale_certificate_json,
        dibfi_direct_bfi_atom_path=args.dibfi_direct_bfi_atom_json,
        dibfi_bfi_atom_match_path=args.dibfi_bfi_atom_match_json,
        dibfi_bfi_level_ledger_path=args.dibfi_bfi_level_ledger_json,
        dibfi_ap_residual_identity_path=args.dibfi_ap_residual_identity_json,
        dibfi_ap_source_branch_path=args.dibfi_ap_source_branch_json,
        dibfi_nonap_dispersion_path=args.dibfi_nonap_dispersion_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_known_frontiers_routed": result["all_known_frontiers_routed"],
                "terminal_dual_gap": result["terminal_dual_gap"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
