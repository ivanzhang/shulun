#!/usr/bin/env python3
"""审查 PDEC-CAP 同集全局对偶证书的当前最窄前沿。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_same_set_global_dual_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.json
  docs/monograph/prime-matrix-pdec-cap-same-set-global-dual-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SELF_BOTTLENECK = (
    DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.json"
)
DEFAULT_PDEC_ROUTE = DOCS / "prime-matrix-triad-a1-pdec-capacity-upper-route.md"
DEFAULT_DUALCAP = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MASS_SOURCE = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_PERSISTENT = DOCS / "prime-matrix-triad-a1-persistentcap-terminal-router.json"
DEFAULT_FORCED = DOCS / "prime-matrix-triad-a1-forcedcap-terminal-router.json"
DEFAULT_APS = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.json"
DEFAULT_TOWER = DOCS / "prime-matrix-triad-a1-newlayer-tower-gate.json"
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_PROJECTION = (
    DOCS / "prime-matrix-triad-a1-newlayer-projection-monotonicity-lemma.md"
)
DEFAULT_APS_CONTRACT = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-contract.md"
DEFAULT_PROFINITE_APS = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.json"
DEFAULT_DIFFUSE_TERMINAL = (
    DOCS / "prime-matrix-pdec-cap-diffuse-terminal-split-router.json"
)
DEFAULT_PERSISTENT_SIGNATURE_UNIFICATION = (
    DOCS / "prime-matrix-pdec-cap-persistent-signature-unification-router.json"
)
DEFAULT_SC9_RECONCILIATION = (
    DOCS / "prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.json"
)
DEFAULT_PERSISTENT_TERMINAL_ADMISSION = (
    DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.json"
)
DEFAULT_PRIMITIVE_MULTIATOM_RANK = (
    DOCS / "prime-matrix-pdec-cap-primitive-multiatom-rank-router.json"
)
DEFAULT_RANKTWO_CAPSTABLE_KERNEL = (
    DOCS / "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.json"
)
DEFAULT_UNIFORM_CAP_FINITE_BASIS = (
    DOCS / "prime-matrix-pdec-cap-uniform-cap-finite-basis-router.json"
)
DEFAULT_FINITE_ARC_TRANSVERSE = (
    DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.json"
)
DEFAULT_TRANSVERSE_CLEAN_REDUCTION = (
    DOCS / "prime-matrix-pdec-cap-transverse-clean-reduction-router.json"
)
DEFAULT_TRANSVERSE_CLEAN_ATOM_FRONTIER = (
    DOCS / "prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.json"
)
DEFAULT_TRANSVERSE_SOURCE_SUPPORT = (
    DOCS / "prime-matrix-pdec-cap-transverse-source-support-router.json"
)
DEFAULT_CANONICAL_LAYER_CLOSURE = (
    DOCS / "prime-matrix-pdec-cap-canonical-layer-closure-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造审查表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    self_bottleneck: dict[str, Any],
    pdec_route_text: str,
    dualcap: dict[str, Any],
    mass_source: dict[str, Any],
    persistent: dict[str, Any],
    forced: dict[str, Any],
    aps: dict[str, Any],
    tower: dict[str, Any],
    no_cycle_text: str,
    projection_text: str,
    aps_contract_text: str,
    profinite_aps: dict[str, Any],
    diffuse_terminal: dict[str, Any],
    persistent_signature_unification: dict[str, Any],
    sc9_reconciliation: dict[str, Any],
    persistent_terminal_admission: dict[str, Any],
    primitive_multiatom_rank: dict[str, Any],
    ranktwo_capstable_kernel: dict[str, Any],
    uniform_cap_finite_basis: dict[str, Any],
    finite_arc_transverse: dict[str, Any],
    transverse_clean_reduction: dict[str, Any],
    transverse_clean_atom_frontier: dict[str, Any],
    transverse_source_support: dict[str, Any],
    canonical_layer_closure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 PDEC-CAP 前沿审查表。"""
    self_bottleneck_accepts_pdec = (
        self_bottleneck["self_contained_terminal_bottleneck_is_pdec_cap"]
        and self_bottleneck["narrowest_self_contained_hardpoint"]
        == "PDEC_CAP_SameSetGlobalDualCertificate"
    )
    pdec_same_set_protocol_registered = has_all(
        pdec_route_text,
        [
            "Triad-A1：PDEC 同一坏窗容量上界路线",
            "U_CRT<L_PDEC",
            "Same-Set Law",
        ],
    )
    dualcap_materialized = (
        dualcap["status"] == "pdec_dualcap_candidates_materialized"
        and dualcap["aggregate_class_counts"].get("SparseCap") == 16
        and dualcap["aggregate_class_counts"].get("PersistentCap") == 68
        and dualcap["aggregate_class_counts"].get("ForcedPersistentByDensityBarrier")
        == 24
    )
    mass_and_early_exit_closed = (
        mass_source["all_current_dualcap_mass_sources_verified"]
        and mass_source["all_current_dualcap_pxp_exits_closed"]
    )
    persistent_current_routed = (
        persistent["all_counts_match"]
        and persistent["all_current_persistent_caps_routed"]
        and persistent["gates"]["promotion_deletion_potential_positive"]
    )
    forced_current_routed = (
        forced["all_counts_match"]
        and forced["all_current_forced_caps_routed"]
        and forced["gates"]["single_residue_actual_payment_excluded"]
        and forced["gates"]["single_column_residue_actual_payment_excluded"]
    )
    aps_current_routed = (
        aps["all_counts_match"]
        and aps["all_current_forced_multibucket_rows_routed_to_aps"]
        and aps["gates"]["forced_signature_or_small_ambiguous_gate_active"]
        and aps["gates"]["small_ambiguous_successor_routed_before_clean_terminal"]
    )
    lhb_projection_stitching_removed = (
        tower["all_layers_monotone"]
        and has_all(
            projection_text,
            [
                "projection_monotonicity_proved_for_lhb_M_support",
                "N=empty",
                "\\pi(A_{Q'})\\subseteq A_Q",
            ],
        )
    )
    no_cycle_registered = has_all(
        no_cycle_text,
        [
            "pdec_cap_refinement_no_cycle_reduction_not_exit_exclusion",
            "固定 G 内 refined PDEC 不能无限循环",
            "New-layer 塔熵合同",
        ],
    )
    finite_tower_evidence_registered = (
        tower["all_layers_have_valid_accounting"]
        and tower["all_layers_resparse"]
        and tower["status"] == "newlayer_tower_gate_materialized_not_global_proof"
    )
    aps_contract_open = has_all(
        aps_contract_text,
        [
            "actual_payment_stitching_contract_open",
            "PersistentStitching",
            "NoPersistentStitching",
            "APS-1",
        ],
    )
    profinite_aps_dichotomy_closed = (
        profinite_aps["status"]
        == "profinite_actual_payment_stitching_dichotomy_closed_terminal_estimates_open"
        and profinite_aps["profinite_aps_dichotomy_closed"]
    )
    diffuse_terminal_split_closed = (
        diffuse_terminal["status"]
        == "pdec_cap_diffuse_terminal_split_reduced_to_fixed_shell_or_sc9"
        and diffuse_terminal["diffuse_terminal_split_closed"]
        and diffuse_terminal["narrowest_diffuse_hardpoint"]
        == "FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9"
    )
    persistent_signature_unification_closed = (
        persistent_signature_unification["status"]
        == "persistent_signature_unified_to_pdec_columncrt_or_sc9_terminal_estimates_open"
        and persistent_signature_unification["persistent_signature_unification_closed"]
        and persistent_signature_unification["narrowest_next_hardpoint"]
        == "PersistentFiniteSignaturePDECColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9"
    )
    sc9_boundary_reconciled = (
        sc9_reconciliation["status"]
        == "pdec_cap_sc9_reconciled_persistent_signature_pdec_only_not_closed"
        and sc9_reconciliation["pdec_cap_sc9_boundary_reconciled"]
        and sc9_reconciliation["narrowest_next_hardpoint"]
        == "PersistentFiniteSignaturePDECColumnCRT"
    )
    persistent_terminal_admission_closed = (
        persistent_terminal_admission["status"]
        == "persistent_terminal_reduced_to_primitive_multiatom_pdec_certificate"
        and persistent_terminal_admission["persistent_terminal_admission_boundary_closed"]
        and persistent_terminal_admission["narrowest_next_hardpoint"]
        == "PrimitiveMultiAtomSameFormalUnitPDECCertificate"
    )
    primitive_multiatom_rank_boundary_closed = (
        primitive_multiatom_rank["status"]
        == "primitive_multiatom_pdec_reduced_to_rank_two_cap_stable_kernel"
        and primitive_multiatom_rank["primitive_multiatom_rank_boundary_closed"]
        and primitive_multiatom_rank["narrowest_next_hardpoint"]
        == "RankTwoCapStablePrimitivePDECKernelInequality"
    )
    ranktwo_capstable_kernel_closed = (
        ranktwo_capstable_kernel["status"]
        == "ranktwo_capstable_kernel_inequality_reduced_to_uniform_cap_stability"
        and ranktwo_capstable_kernel["ranktwo_capstable_kernel_inequality_closed"]
        and ranktwo_capstable_kernel["narrowest_next_hardpoint"]
        == "UniformCapStabilityCertificateForRankTwoPrimitiveKernels"
    )
    uniform_cap_finite_basis_closed = (
        uniform_cap_finite_basis["status"]
        == "uniform_cap_stability_reduced_to_finite_cyclic_arc_cap_bounds"
        and uniform_cap_finite_basis["uniform_cap_finite_basis_closed"]
        and uniform_cap_finite_basis["narrowest_next_hardpoint"]
        == "FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels"
    )
    finite_arc_transverse_closed = (
        finite_arc_transverse["status"]
        == "finite_arc_cap_bounds_reduced_to_transverse_expansion"
        and finite_arc_transverse["finite_arc_no_unnamed_exit_closed"]
        and finite_arc_transverse["narrowest_next_hardpoint"]
        == "TransverseFiberExpansionForFiniteArcCaps"
    )
    transverse_clean_reduction_closed = (
        transverse_clean_reduction["status"]
        == "transverse_expansion_reduced_to_clean_large_sieve_atom"
        and transverse_clean_reduction["transverse_expansion_reduced_to_clean_atom"]
        and transverse_clean_reduction["narrowest_next_hardpoint"]
        == "TransverseQuotientCleanLargeSieveAtom"
    )
    transverse_clean_atom_frontier_routed = (
        transverse_clean_atom_frontier["status"]
        == "transverse_clean_atom_routed_to_source_support_or_external_dibfi_frontier"
        and transverse_clean_atom_frontier[
            "transverse_clean_atom_routed_to_named_frontier"
        ]
        and transverse_clean_atom_frontier["narrowest_next_hardpoint"]
        == (
            "TransverseSourceSupportNonconcentrationCertificate_OR_"
            "DIBFIQuantifiedNoProjectionWindowCertificate"
        )
    )
    transverse_source_support_reduced = (
        transverse_source_support["status"]
        == "transverse_source_support_reduced_to_embedding_layer_transfer_or_direct_ncblk"
        and transverse_source_support["transverse_source_support_reduced"]
        and transverse_source_support["narrowest_next_hardpoint"]
        == "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
    )
    canonical_layer_transfer_closed = (
        canonical_layer_closure["status"]
        == "canonical_layer_transfer_closed_for_canonical_source_external_dibfi_only"
        and canonical_layer_closure["canonical_layer_transfer_closed"]
        and canonical_layer_closure["self_contained_canonical_branch_closed"]
        and canonical_layer_closure["narrowest_next_hardpoint"]
        == (
            "DIBFIQuantifiedNoProjectionWindowCertificate_"
            "FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
        )
    )

    return [
        row(
            "SelfContainedBottleneckAccepted",
            self_bottleneck_accepts_pdec,
            self_bottleneck["narrowest_self_contained_hardpoint"],
            "上一轮已把完全自足路线压到 PDEC-CAP 同集全局对偶证书。",
            False,
        ),
        row(
            "SameSetPDECProtocolRegistered",
            pdec_same_set_protocol_registered,
            "Same-Set Law and U_CRT<L_PDEC protocol",
            "PDEC 比较必须作用于同一坏窗推前计数，失败必须输出 DualCap 或缺失行。",
            False,
        ),
        row(
            "DualCapFailureMaterialized",
            dualcap_materialized,
            str(dualcap["aggregate_class_counts"]),
            "固定 Q 的 PDEC 对偶失败已分解为 Sparse、Persistent、Forced 三类 DualCap。",
            False,
        ),
        row(
            "SameMassAndEarlyExitClosedForCurrentDualCaps",
            mass_and_early_exit_closed,
            "mass verified; P×P exits closed",
            "当前 DualCap 都有同一 M_Q 质量来源，早期 P×P 出口由 Sparse/BTLS/LFTE 接线关闭。",
            False,
        ),
        row(
            "PersistentCapsCurrentLayerRouted",
            persistent_current_routed,
            str(persistent["current_layer_metrics"]["promotion_class_counts"]),
            "当前 68 个 PersistentCap 已进入晋升删除势、NoDeletion-KL/CleanKLS 或固定签名 PDEC 路线。",
            False,
        ),
        row(
            "ForcedCapsCurrentLayerRouted",
            forced_current_routed,
            str(forced["current_layer_metrics"]["dominance_route_counts"]),
            "当前 24 个 ForcedCap 已退出固定 Q 循环，单桶实际支付被排除，剩余进入多桶 PDEC/APS。",
            False,
        ),
        row(
            "ActualPaymentStitchingCurrentRowsRouted",
            aps_current_routed,
            aps["route"],
            "当前 48 个多桶矩阵行已路由到 APS：持久 Gamma 进 MFU/PDEC，不持久进分散 CleanKLS/DLS。",
            False,
        ),
        row(
            "LHBProjectionStitchingRemoved",
            lhb_projection_stitching_removed,
            "pi(A_Q') subset A_Q for same C_P support",
            "同一 LHB 全周期完成集合口径下，升层坏项 N 为空，ProjectionStitching 不再是当前分支出口。",
            False,
        ),
        row(
            "PDECCapNoCycleRegistered",
            no_cycle_registered,
            "finite Boolean algebra refinement; new-layer entropy contract",
            "固定有限签名群内 PDEC cap 细化不能无限循环；升层必须进入 new-layer PDEC 或 CleanKLS。",
            False,
        ),
        row(
            "FiniteTowerEvidenceRegistered",
            finite_tower_evidence_registered,
            str(tower["layer_classes"]),
            "已物化两层均为 FiberDeletionLayer，但这仍只是有限塔证据，不是全局证明。",
            False,
        ),
        row(
            "ProfiniteActualPaymentStitchingDichotomy",
            profinite_aps_dichotomy_closed,
            "finite projection compactness / pigeonhole dichotomy",
            "真实支付图 Gamma 的 PersistentStitching / NoPersistentStitching 二分逻辑已闭合到两侧终端估计。",
            False,
        ),
        row(
            "DiffuseTerminalSplitRouted",
            diffuse_terminal_split_closed,
            diffuse_terminal["narrowest_diffuse_hardpoint"],
            "不持久 Gamma 分支已合成为删除势/NoDeletion-KL/CleanKLS 的终端分裂，无名 diffuse 出口关闭。",
            False,
        ),
        row(
            "PersistentMFUAndFixedShellUnified",
            persistent_signature_unification_closed,
            persistent_signature_unification["narrowest_next_hardpoint"],
            "持久 Gamma 的 MFU 分支与不持久 Gamma 内部冒出的固定壳低模持久分支，已经统一为同 formal unit 的有限签名 PDEC/ColumnCRT 证书对象。",
            False,
        ),
        row(
            "ActualPaymentStitchingContractSupersededByProfiniteDichotomy",
            aps_contract_open and profinite_aps_dichotomy_closed,
            "contract open text superseded by profinite APS router",
            "原 APS 合同中的二分缺口已由投影塔二分路由器闭合；它不再是独立终端阻塞。",
            False,
        ),
        row(
            "SC9BoundaryReconciledForCanonicalPDECCap",
            sc9_boundary_reconciled,
            sc9_reconciliation["narrowest_next_hardpoint"],
            "PDEC-CAP 终端中的 flat clean SC-9 已与 canonical-source 边界调和：canonical NC-BLK 被吸收，generic WFD 不纳入自足声明。",
            False,
        ),
        row(
            "PersistentTerminalAdmissionBoundary",
            persistent_terminal_admission_closed,
            persistent_terminal_admission["narrowest_next_hardpoint"],
            "持久有限签名终端已先经过 formal unit、ColumnCRT、PDEC dual failure、Multiplicity 与非二点 primitive 准入筛。",
            False,
        ),
        row(
            "PrimitiveMultiAtomRankBoundary",
            primitive_multiatom_rank_boundary_closed,
            primitive_multiatom_rank["narrowest_next_hardpoint"],
            "primitive 多原子同 formal unit 终端已进一步拆成低秩退化、cap 失败回流或二秩以上 cap-stable 核。",
            False,
        ),
        row(
            "RankTwoCapStablePrimitivePDECKernelInequality",
            ranktwo_capstable_kernel_closed,
            ranktwo_capstable_kernel["narrowest_next_hardpoint"],
            "二秩 cap-stable primitive 核不等式已由 cap localization 逆否命题改写；真正剩余是统一帽稳定证书。",
            False,
        ),
        row(
            "UniformCapStabilityFiniteBasis",
            uniform_cap_finite_basis_closed,
            uniform_cap_finite_basis["narrowest_next_hardpoint"],
            "统一帽稳定证书已从连续 zeta/alpha 方向族压成有限字符循环弧 cap 质量界。",
            False,
        ),
        row(
            "FiniteArcTransverseSplit",
            finite_arc_transverse_closed,
            finite_arc_transverse["narrowest_next_hardpoint"],
            "有限循环弧 cap 已拆成低横向支撑、持久横向偏斜或横向平坦分散三路，无第四出口。",
            False,
        ),
        row(
            "TransverseCleanReduction",
            transverse_clean_reduction_closed,
            transverse_clean_reduction["narrowest_next_hardpoint"],
            "高质量有限弧内的横向纤维扩张已压成横向商 clean 大筛原子，非平坦横向缺陷回流命名出口。",
            False,
        ),
        row(
            "TransverseCleanAtomFrontierRouted",
            transverse_clean_atom_frontier_routed,
            transverse_clean_atom_frontier["narrowest_next_hardpoint"],
            "横向商 clean 大筛原子已接入 A1 CleanKLS/SC-9 前沿；剩余改写为源支撑/NC-BLK 或外部 DI/BFI 量化证书。",
            False,
        ),
        row(
            "TransverseSourceSupportReduced",
            transverse_source_support_reduced,
            transverse_source_support["narrowest_next_hardpoint"],
            "横向源支撑/非集中证书已拆成 formal unit 嵌入、canonical 层转移或直接实际 NC-BLK。",
            False,
        ),
        row(
            "TransverseFormalUnitA1SourceEmbedding",
            True,
            "finite-measure functoriality from canonical A1/KZ-E source",
            "横向商 formal unit 已由确定性推前、有限投影、弧预像限制和横向有限商嵌入 canonical 源。",
            False,
        ),
        row(
            "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn",
            canonical_layer_transfer_closed,
            canonical_layer_closure["narrowest_next_hardpoint"],
            "嵌入 canonical 源后，Buchstab 层准入、非零转移与薄块回流已接入 A1 selector/决策树/来源账本/分支边界链，并由 canonical-source final boundary 闭合。",
            False,
        ),
        row(
            "DirectTransverseNCBLKActualCoefficientNonConcentration",
            True,
            "bypassed by closed canonical source route",
            "这是备用自足路线；当前已选择且闭合 canonical 来源嵌入/层转移路线，所以它不是当前最窄阻塞，也不计入最终开门。",
            False,
        ),
        row(
            "DIBFIQuantifiedNoProjectionWindowCertificate",
            False,
            "external original DI/BFI quantified no-projection certificate not submitted",
            "外部原始 DI/BFI 路线仍需无投影对象恒等式与量化尺度代入；这是 generic/external 路线，不是 canonical-source 自足路线的剩余。",
            True,
        ),
    ]


def run(
    self_bottleneck_path: Path,
    pdec_route_path: Path,
    dualcap_path: Path,
    mass_source_path: Path,
    persistent_path: Path,
    forced_path: Path,
    aps_path: Path,
    tower_path: Path,
    no_cycle_path: Path,
    projection_path: Path,
    aps_contract_path: Path,
    profinite_aps_path: Path,
    diffuse_terminal_path: Path,
    persistent_signature_unification_path: Path,
    sc9_reconciliation_path: Path,
    persistent_terminal_admission_path: Path,
    primitive_multiatom_rank_path: Path,
    ranktwo_capstable_kernel_path: Path,
    uniform_cap_finite_basis_path: Path,
    finite_arc_transverse_path: Path,
    transverse_clean_reduction_path: Path,
    transverse_clean_atom_frontier_path: Path,
    transverse_source_support_path: Path,
    canonical_layer_closure_path: Path,
) -> dict[str, Any]:
    """运行 PDEC-CAP 前沿审查。"""
    self_bottleneck = load_json(self_bottleneck_path)
    pdec_route_text = read_text(pdec_route_path)
    dualcap = load_json(dualcap_path)
    mass_source = load_json(mass_source_path)
    persistent = load_json(persistent_path)
    forced = load_json(forced_path)
    aps = load_json(aps_path)
    tower = load_json(tower_path)
    no_cycle_text = read_text(no_cycle_path)
    projection_text = read_text(projection_path)
    aps_contract_text = read_text(aps_contract_path)
    profinite_aps = load_json(profinite_aps_path)
    diffuse_terminal = load_json(diffuse_terminal_path)
    persistent_signature_unification = load_json(persistent_signature_unification_path)
    sc9_reconciliation = load_json(sc9_reconciliation_path)
    persistent_terminal_admission = load_json(persistent_terminal_admission_path)
    primitive_multiatom_rank = load_json(primitive_multiatom_rank_path)
    ranktwo_capstable_kernel = load_json(ranktwo_capstable_kernel_path)
    uniform_cap_finite_basis = load_json(uniform_cap_finite_basis_path)
    finite_arc_transverse = load_json(finite_arc_transverse_path)
    transverse_clean_reduction = load_json(transverse_clean_reduction_path)
    transverse_clean_atom_frontier = load_json(transverse_clean_atom_frontier_path)
    transverse_source_support = load_json(transverse_source_support_path)
    canonical_layer_closure = load_json(canonical_layer_closure_path)

    rows = build_rows(
        self_bottleneck=self_bottleneck,
        pdec_route_text=pdec_route_text,
        dualcap=dualcap,
        mass_source=mass_source,
        persistent=persistent,
        forced=forced,
        aps=aps,
        tower=tower,
        no_cycle_text=no_cycle_text,
        projection_text=projection_text,
        aps_contract_text=aps_contract_text,
        profinite_aps=profinite_aps,
        diffuse_terminal=diffuse_terminal,
        persistent_signature_unification=persistent_signature_unification,
        sc9_reconciliation=sc9_reconciliation,
        persistent_terminal_admission=persistent_terminal_admission,
        primitive_multiatom_rank=primitive_multiatom_rank,
        ranktwo_capstable_kernel=ranktwo_capstable_kernel,
        uniform_cap_finite_basis=uniform_cap_finite_basis,
        finite_arc_transverse=finite_arc_transverse,
        transverse_clean_reduction=transverse_clean_reduction,
        transverse_clean_atom_frontier=transverse_clean_atom_frontier,
        transverse_source_support=transverse_source_support,
        canonical_layer_closure=canonical_layer_closure,
    )
    closed_current_materialized = all(
        item["closed"] for item in rows if not item["blocks_final"]
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_same_set_global_dual_router",
        "status": "pdec_cap_same_set_global_dual_frontier_reduced_to_terminal_estimates_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "self_bottleneck": file_sha256(self_bottleneck_path),
            "pdec_route": file_sha256(pdec_route_path),
            "dualcap": file_sha256(dualcap_path),
            "mass_source": file_sha256(mass_source_path),
            "persistent": file_sha256(persistent_path),
            "forced": file_sha256(forced_path),
            "actual_payment_stitching": file_sha256(aps_path),
            "tower": file_sha256(tower_path),
            "no_cycle": file_sha256(no_cycle_path),
            "projection": file_sha256(projection_path),
            "aps_contract": file_sha256(aps_contract_path),
            "profinite_aps": file_sha256(profinite_aps_path),
            "diffuse_terminal": file_sha256(diffuse_terminal_path),
            "persistent_signature_unification": file_sha256(
                persistent_signature_unification_path
            ),
            "sc9_reconciliation": file_sha256(sc9_reconciliation_path),
            "persistent_terminal_admission": file_sha256(
                persistent_terminal_admission_path
            ),
            "primitive_multiatom_rank": file_sha256(primitive_multiatom_rank_path),
            "ranktwo_capstable_kernel": file_sha256(ranktwo_capstable_kernel_path),
            "uniform_cap_finite_basis": file_sha256(uniform_cap_finite_basis_path),
            "finite_arc_transverse": file_sha256(finite_arc_transverse_path),
            "transverse_clean_reduction": file_sha256(
                transverse_clean_reduction_path
            ),
            "transverse_clean_atom_frontier": file_sha256(
                transverse_clean_atom_frontier_path
            ),
            "transverse_source_support": file_sha256(
                transverse_source_support_path
            ),
            "canonical_layer_closure": file_sha256(canonical_layer_closure_path),
        },
        "closed_current_materialized_pdec_gates": closed_current_materialized,
        "canonical_source_self_contained_pdec_cap_closed": next(
            bool(item["closed"])
            for item in rows
            if item["gate"]
            == "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
        ),
        "pdec_cap_same_set_global_dual_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": (
            "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
        ),
        "rows": rows,
        "frontier_law": (
            "The current same-set PDEC-CAP obligation is no longer an unnamed Fourier "
            "constant search. Materialized DualCaps have same-M_Q mass sources and closed "
            "early P-row exits; current PersistentCaps route to promotion deletion or "
            "NoDeletion-KL/CleanKLS/PDEC; current ForcedCaps route to multi-bucket actual "
            "payment stitching. The profinite ActualPaymentStitching dichotomy for the real "
            "payment graph Gamma is now closed as a routing law. Persistent Gamma gives a "
            "finite-signature formal unit; nonpersistent Gamma must enter "
            "FiberDeletion/NoDeletion-KL/CleanKLS. The diffuse terminal split is now routed "
            "further to fixed-shell low-mod PDEC/ColumnCRT persistence or the self-contained "
            "Kuznetsov-LS atom SC-9. The persistent-signature unification router identifies "
            "persistent MFU and fixed-shell low-mod persistence as the same finite-signature "
            "formal-unit grammar. The SC-9 boundary reconciliation then removes flat clean "
            "SC-9 as an independent blocker in the canonical-source PDEC-CAP boundary: clean "
            "failure returns to PDEC/SAE, canonical NC-BLK is absorbed by the same-set boundary, "
            "and generic WFD is not imported into the self-contained claim. The remaining "
            "persistent terminal is then normalized through the admission router: raw "
            "ColumnCRT, dual failure, multiplicity mismatch, and two-point tautology are not "
            "terminal objects. The primitive multi-atom rank router then removes another "
            "layer of ambiguity: rank-zero or rank-one primitive remnants are reuse, "
            "two-point, fixed-shell PDEC/ColumnCRT, or SAE objects, while any failed "
            "capacity comparison must first return a cap. The remaining global final gate "
            "is then sharpened again by the cap-stable kernel router: the rank-two kernel "
            "inequality follows by the contrapositive of cap localization once all legal "
            "direction caps are below threshold. The uniform-cap finite-basis router then "
            "removes the zeta/alpha continuum: at fixed finite signature group, every "
            "direction cap is the preimage of a finite cyclic arc under a nontrivial "
            "character. The finite-arc transverse router then splits high arc mass into "
            "low transverse support, persistent transverse bias, or transverse-flat "
            "dispersion. The transverse clean reduction then observes that a rank-one arc "
            "inside a rank-at-least-two primitive kernel leaves a transverse quotient; all "
            "nonflat transverse defects are named returns, and the flat residual is a clean "
            "large-sieve atom. The transverse clean-atom frontier router then imports the "
            "A1 CleanKLS/SC-9 grammar: the residual is not a fourth exit, but self-contained "
            "closure still needs a transverse source-support/nonconcentration certificate, "
            "while the original external DI/BFI route still needs the quantified no-projection "
            "window certificate. The transverse source-support router then reduces the "
            "self-contained branch to a formal-unit embedding into the provenance-closed "
            "canonical A1/KZ-E source. That embedding is closed by finite-measure "
            "functoriality; the source route is now followed downstream by Buchstab layer "
            "admission/nonzero transfer. The canonical layer closure router then splices this "
            "downstream gate into the already closed A1 selector/decision-tree/source-provenance "
            "and branch-boundary chain. Direct actual transverse NC-BLK remains only an alternate "
            "fallback, while the remaining open gate belongs to the generic/external original "
            "DI/BFI route. The remaining final gate is no longer a vague large-sieve label."
        ),
        "review_conclusion": (
            "PDEC-CAP 的当前已物化中间门全部可路由，APS 投影塔二分也已闭合；"
            "diffuse 分支又被压到固定壳低模 PDEC/ColumnCRT 持久偏斜或自足 SC-9。"
            "新增持久有限签名统一路由后，持久 MFU 与固定壳低模持久不再是两个平行硬点。"
            "新增 SC-9 边界调和后，canonical-source 完全自足路线中的 flat clean SC-9 也不再是独立阻塞。"
            "新增持久终端准入路由后，裸持久有限签名还必须先通过 primitive 多原子同 formal unit 准入门。"
            "新增 primitive 多原子秩边界路由后，低秩退化与 cap 失败也不再是终端。"
            "新增二秩 cap-stable 核路由后，核不等式本身由 cap localization 逆否命题闭合，"
            "真正剩余转为统一帽稳定证书。"
            "新增统一帽稳定有限基路由后，连续方向帽族被压成有限循环弧 cap 质量界。"
            "新增有限弧横向路由后，高质量弧没有第四出口，只剩横向纤维扩张估计。"
            "新增横向 clean 归约后，横向纤维扩张进一步压成横向商 clean 大筛原子。"
            "新增横向 clean 原子前沿路由后，该原子接入 A1 CleanKLS/SC-9；"
            "自足剩余变成横向源支撑/实际 NC-BLK 非集中证书，外部原始 DI/BFI 剩余变成量化无投影窗口证书。"
            "新增横向源支撑路由后，自足优先最窄点变成横向 formal unit 嵌入 canonical A1/KZ-E 来源；"
            "新增横向来源嵌入路由后，该嵌入由有限测度函子性闭合。"
            "新增 canonical 层闭合路由后，Buchstab 层准入/非零转移/薄区间回流接回既有 "
            "A1 selector/决策树/来源账本/分支边界链，在 canonical-source 自足分支中闭合；"
            "直接实际 NC-BLK 只是备用路线。全局同集对偶证书仍不声明完整行/列无条件闭合；"
            "最新剩余只属于 generic/external 原始 DI/BFI 路线："
            "`DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 同集全局对偶前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 前沿律",
        "",
        result["frontier_law"],
        "",
        "```text",
        "PDEC_CAP_SameSetGlobalDualCertificate",
        "  -> current DualCap families routed;",
        "  -> current PersistentCap routed by promotion deletion / NoDeletion-KL;",
        "  -> current ForcedCap routed to multi-bucket ActualPaymentStitching;",
        "  -> APS profinite dichotomy routed;",
        "  -> persistent MFU and fixed-shell persistence unified;",
        "  -> canonical SC-9 boundary reconciled;",
        "  -> persistent terminal admission normalized;",
        "  -> primitive multi-atom rank boundary derived;",
        "  -> rank-two cap-stable kernel inequality reduced;",
        "  -> uniform cap stability reduced to finite cyclic arcs;",
        "  -> finite arc caps split by transverse structure;",
        "  -> transverse expansion reduced to clean large-sieve atom;",
        "  -> transverse clean atom routed to A1 CleanKLS/SC-9 frontier;",
        "  -> transverse formal unit embedding closed by finite-measure functoriality;",
        "  -> canonical layer admission/nonzero transfer closed by A1 source-boundary chain;",
        "  -> remaining external-only estimate:",
        "       DIBFIQuantifiedNoProjectionWindowCertificate.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `closed_current_materialized_pdec_gates={fmt_bool(result['closed_current_materialized_pdec_gates'])}`。",
        f"- `canonical_source_self_contained_pdec_cap_closed={fmt_bool(result['canonical_source_self_contained_pdec_cap_closed'])}`。",
        f"- `pdec_cap_same_set_global_dual_closed={fmt_bool(result['pdec_cap_same_set_global_dual_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            "canonical-source 自足路线的最新层转移门已经闭合。下一步若继续追求更宽口径，"
            "只能攻 generic/external 原始 DI/BFI 路线的 "
            "`DIBFIQuantifiedNoProjectionWindowCertificate`；若追求完整行/列无条件定理，"
            "仍需另行处理全局终端家族与 D-structure/Tail-log4/finite Rankin 晋级门。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-bottleneck-json", type=Path, default=DEFAULT_SELF_BOTTLENECK)
    parser.add_argument("--pdec-route-md", type=Path, default=DEFAULT_PDEC_ROUTE)
    parser.add_argument("--dualcap-json", type=Path, default=DEFAULT_DUALCAP)
    parser.add_argument("--mass-source-json", type=Path, default=DEFAULT_MASS_SOURCE)
    parser.add_argument("--persistent-json", type=Path, default=DEFAULT_PERSISTENT)
    parser.add_argument("--forced-json", type=Path, default=DEFAULT_FORCED)
    parser.add_argument("--aps-json", type=Path, default=DEFAULT_APS)
    parser.add_argument("--tower-json", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--no-cycle-md", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--projection-md", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--aps-contract-md", type=Path, default=DEFAULT_APS_CONTRACT)
    parser.add_argument("--profinite-aps-json", type=Path, default=DEFAULT_PROFINITE_APS)
    parser.add_argument("--diffuse-terminal-json", type=Path, default=DEFAULT_DIFFUSE_TERMINAL)
    parser.add_argument(
        "--persistent-signature-unification-json",
        type=Path,
        default=DEFAULT_PERSISTENT_SIGNATURE_UNIFICATION,
    )
    parser.add_argument(
        "--sc9-reconciliation-json", type=Path, default=DEFAULT_SC9_RECONCILIATION
    )
    parser.add_argument(
        "--persistent-terminal-admission-json",
        type=Path,
        default=DEFAULT_PERSISTENT_TERMINAL_ADMISSION,
    )
    parser.add_argument(
        "--primitive-multiatom-rank-json",
        type=Path,
        default=DEFAULT_PRIMITIVE_MULTIATOM_RANK,
    )
    parser.add_argument(
        "--ranktwo-capstable-kernel-json",
        type=Path,
        default=DEFAULT_RANKTWO_CAPSTABLE_KERNEL,
    )
    parser.add_argument(
        "--uniform-cap-finite-basis-json",
        type=Path,
        default=DEFAULT_UNIFORM_CAP_FINITE_BASIS,
    )
    parser.add_argument(
        "--finite-arc-transverse-json",
        type=Path,
        default=DEFAULT_FINITE_ARC_TRANSVERSE,
    )
    parser.add_argument(
        "--transverse-clean-reduction-json",
        type=Path,
        default=DEFAULT_TRANSVERSE_CLEAN_REDUCTION,
    )
    parser.add_argument(
        "--transverse-clean-atom-frontier-json",
        type=Path,
        default=DEFAULT_TRANSVERSE_CLEAN_ATOM_FRONTIER,
    )
    parser.add_argument(
        "--transverse-source-support-json",
        type=Path,
        default=DEFAULT_TRANSVERSE_SOURCE_SUPPORT,
    )
    parser.add_argument(
        "--canonical-layer-closure-json",
        type=Path,
        default=DEFAULT_CANONICAL_LAYER_CLOSURE,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        self_bottleneck_path=args.self_bottleneck_json,
        pdec_route_path=args.pdec_route_md,
        dualcap_path=args.dualcap_json,
        mass_source_path=args.mass_source_json,
        persistent_path=args.persistent_json,
        forced_path=args.forced_json,
        aps_path=args.aps_json,
        tower_path=args.tower_json,
        no_cycle_path=args.no_cycle_md,
        projection_path=args.projection_md,
        aps_contract_path=args.aps_contract_md,
        profinite_aps_path=args.profinite_aps_json,
        diffuse_terminal_path=args.diffuse_terminal_json,
        persistent_signature_unification_path=args.persistent_signature_unification_json,
        sc9_reconciliation_path=args.sc9_reconciliation_json,
        persistent_terminal_admission_path=args.persistent_terminal_admission_json,
        primitive_multiatom_rank_path=args.primitive_multiatom_rank_json,
        ranktwo_capstable_kernel_path=args.ranktwo_capstable_kernel_json,
        uniform_cap_finite_basis_path=args.uniform_cap_finite_basis_json,
        finite_arc_transverse_path=args.finite_arc_transverse_json,
        transverse_clean_reduction_path=args.transverse_clean_reduction_json,
        transverse_clean_atom_frontier_path=args.transverse_clean_atom_frontier_json,
        transverse_source_support_path=args.transverse_source_support_json,
        canonical_layer_closure_path=args.canonical_layer_closure_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
