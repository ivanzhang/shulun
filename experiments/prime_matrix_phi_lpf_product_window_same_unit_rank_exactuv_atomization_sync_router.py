#!/usr/bin/env python3
"""归档 product-window same-unit rank 到 ExactUV/source-table 原子接口的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_same_unit_rank_exactuv_atomization_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-same-unit-rank-exactuv-atomization-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-same-unit-rank-exactuv-atomization-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-same-unit-rank-exactuv-atomization-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-same-unit-rank-exactuv-atomization-sync-router.md

本证书承接 product-window identity terminal downstream sync。它把当前第一硬点
`SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` 接入 strict
exact-UV map rank/incidence、ExactUV fiber noncycle、fixed-pair fiber bound、
complete key partition、actual emitter source table 与 signed macrocycle
ExactUV/source-table 链。结论只是一条非循环同步：same-unit rank 旧名不应继续作为
product-window 第一目标；它拆成 pre-Cauchy declaration/source-table/key/local
multiplicity 等 actual 接口。本证书不证明行/列命题。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-same-unit-rank-exactuv-atomization-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-identity-terminal-downstream-sync-router.json"
STRICT_MAP_RANK = DOCS / "prime-matrix-strict-exact-uv-map-rank-incidence-router.json"
EXACTUV_FIBER = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"
FIXED_PAIR = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"
COMPLETE_KEY = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
SOURCE_TABLE = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"
MACROCYCLE = DOCS / "prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.json"
POST_ANTISPLIT = DOCS / "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"
SOURCE_ATOM_BRIDGE = DOCS / "prime-matrix-source-atom-multiplicity-cap-exactuv-fixed-key-bridge-router.json"

SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
MAP_RANK = "PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem"
BOUNDED_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
FIXED_PAIR_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
COMPLETE_KEY_LEDGER = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_O1 = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SOURCE_TABLE_LEDGER = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
PRECAUCHY_DECL = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
PRIMITIVE_ROWS = "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable"
ALPHA_DELTA_IDENTITY = "AlphaDeltaCoefficientIdentityBeforePushforwardLedger"
NO_RECOVERY_RETURN = "SourceTableNoDownstreamRecoveryAndNamedReturnLedger"
SEED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
SUPPORT_LOWER = "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger"
TRACE_KEY_BUDGET = "CompleteEmitterTraceKeyBudgetLedger"
SIGN_LOCAL_REFINEMENT = "SignLocalFactorRefinementNoCancellationLedger"
OVERBUDGET_RETURN = "OverBudgetOrUnregisteredReturnLedger"

NO_FURTHER_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"
CLOSED_MODELGAP = "ProductWindowExplicitModelGapDownstreamSubledgerClosedByExistingFiniteB3MertensSync"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
SIGNED_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TRACE_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"

OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能被解释成证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """布尔值小写输出。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        STRICT_MAP_RANK,
        EXACTUV_FIBER,
        FIXED_PAIR,
        COMPLETE_KEY,
        SOURCE_TABLE,
        MACROCYCLE,
        POST_ANTISPLIT,
        SOURCE_ATOM_BRIDGE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出 same-unit rank 到 actual source/key/local multiplicity 的同步链。"""
    return [
        {
            "from": SAME_UNIT_RANK,
            "to": f"{MAP_RANK} / {BOUNDED_INCIDENCE}",
            "meaning": "same-unit rank 的正面内容不是 CRT 位置刚性，而是 actual emitter 到 exact (u,v) 的有界重数 incidence。",
        },
        {
            "from": SOURCE_RANK,
            "to": f"{SOURCE_ENTROPY} AND {REGISTERED_KEY} AND {FIXED_KEY_O1}",
            "meaning": "ExactUV fiber 最新非循环同步把 source-rank/no-collapse 原子化为源域熵、complete key 与 fixed-key 局部重数。",
        },
        {
            "from": FIXED_PAIR_FIBER,
            "to": f"{REGISTERED_KEY} AND {FIXED_KEY_O1}",
            "meaning": "fixed-pair polylog fiber bound 的形式不等式已闭合；实际输入是 key 分区与固定 key O(1) 原像。",
        },
        {
            "from": REGISTERED_KEY,
            "to": f"{SOURCE_TABLE_LEDGER} AND {TRACE_KEY_BUDGET} AND {SIGN_LOCAL_REFINEMENT} AND {OVERBUDGET_RETURN}",
            "meaning": "complete key 不能后验补标签，必须由 actual source table 生成并带预算、refinement 与回流。",
        },
        {
            "from": SOURCE_TABLE_LEDGER,
            "to": f"{PRECAUCHY_DECL} AND {PRIMITIVE_ROWS} AND {ALPHA_DELTA_IDENTITY} AND {NO_RECOVERY_RETURN}",
            "meaning": "actual emitter source table 的首行是 pre-Cauchy constructor declaration；无该行则 rows/key/return 都只是后验表。",
        },
        {
            "from": "product-window first same-unit rank target",
            "to": f"{PRECAUCHY_DECL} plus {FIXED_KEY_O1}",
            "meaning": "same-unit rank 旧名移出第一主攻；下一直接口是 pre-Cauchy declaration，并行保留 fixed-key local multiplicity。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    previous = data["previous"]
    map_rank = data["map_rank"]
    fiber = data["fiber"]
    fixed_pair = data["fixed_pair"]
    complete_key = data["complete_key"]
    source_table = data["source_table"]
    macrocycle = data["macrocycle"]
    post_antisplit = data["post_antisplit"]
    source_atom_bridge = data["source_atom_bridge"]

    previous_same_unit_active = (
        previous.get("next_primary_attack_target") == SAME_UNIT_RANK
        and previous.get("identity_removed_from_product_window_first_target") is True
        and previous.get("same_unit_exactuv_rank_multiplicity_certificate_proved") is False
    )
    map_rank_imported = (
        map_rank.get("exact_uv_map_rank_incidence_router_closed") is True
        and map_rank.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False
    )
    fiber_atomization_imported = (
        fiber.get("deterministic_source_atom_implication_closed") is True
        and fiber.get("map_rank_equivalent_to_bounded_incidence") is True
        and fiber.get("source_rank_converges_to_pointwise_kernel") is True
    )
    fixed_pair_imported = (
        fixed_pair.get("fixed_pair_fiber_bound_router_closed") is True
        and fixed_pair.get("deterministic_key_fiber_inequality_closed") is True
        and fixed_pair.get("registered_complete_primitive_emitter_key_partition_polylog_proved") is False
        and fixed_pair.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False
    )
    complete_key_imported = (
        complete_key.get("complete_emitter_key_partition_router_closed") is True
        and complete_key.get("source_table_to_complete_key_implication_closed") is True
        and complete_key.get("actual_noncanonical_primitive_emitter_source_table_proved") is False
    )
    source_table_imported = (
        source_table.get("actual_emitter_source_table_router_closed") is True
        and source_table.get("source_table_field_decomposition_pinned") is True
        and source_table.get("pre_cauchy_constructor_declaration_line_proved") is False
    )
    macrocycle_imported = (
        macrocycle.get("exactuv_atomization_imported") is True
        and macrocycle.get("fixed_pair_fiber_formal_inequality_closed") is True
        and macrocycle.get("registered_complete_key_reduced_to_source_table") is True
        and macrocycle.get("source_table_reduced_to_precauchy_declaration") is True
    )
    post_antisplit_imported = (
        post_antisplit.get("source_rank_package_atomized") is True
        and post_antisplit.get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True
    )
    source_atom_bridge_imported = (
        source_atom_bridge.get("source_atom_multiplicity_cap_reduced_to_exactuv_fixed_key_atoms") is True
        and source_atom_bridge.get("fixed_key_exact_uv_local_multiplicity_o1_ledger_proved") is False
    )
    same_unit_removed = all(
        [
            previous_same_unit_active,
            map_rank_imported,
            fiber_atomization_imported,
            fixed_pair_imported,
            complete_key_imported,
            source_table_imported,
            macrocycle_imported,
            post_antisplit_imported,
            source_atom_bridge_imported,
        ]
    )

    return [
        row(
            "ProductWindowSameUnitRankActiveBeforeSync",
            previous_same_unit_active,
            False,
            "上一 product-window identity terminal 证书把第一硬点推进到 same-unit ExactUV rank/multiplicity。",
            SAME_UNIT_RANK,
        ),
        row(
            "ExactUVMapRankIncidenceImported",
            map_rank_imported,
            False,
            "strict map-rank 路由把 rank/no-collapse 翻译为 actual emitter bounded multiplicity incidence。",
            BOUNDED_INCIDENCE,
        ),
        row(
            "ExactUVFiberAtomizationImported",
            fiber_atomization_imported,
            False,
            "ExactUV fiber 非循环同步给出 source entropy、complete key 与 fixed-key O(1) 的确定性蕴含框架。",
            f"{SOURCE_ENTROPY} AND {REGISTERED_KEY} AND {FIXED_KEY_O1}",
        ),
        row(
            "FixedPairFiberFormalInequalityImported",
            fixed_pair_imported,
            True,
            "fixed-pair fiber 的 key-count x fixed-key O(1) 形式不等式已闭合。",
            f"{REGISTERED_KEY} AND {FIXED_KEY_O1}",
        ),
        row(
            "CompleteKeyPartitionImported",
            complete_key_imported,
            False,
            "complete key 分区已被拆成 actual source table、trace/key 预算、sign/local refinement 与未登记回流。",
            f"{SOURCE_TABLE_LEDGER} AND {TRACE_KEY_BUDGET} AND {SIGN_LOCAL_REFINEMENT} AND {OVERBUDGET_RETURN}",
        ),
        row(
            "ActualEmitterSourceTableImported",
            source_table_imported,
            False,
            "actual source table 已拆成 pre-Cauchy declaration、primitive rows、推前前系数恒等式与 no-recovery return。",
            f"{PRECAUCHY_DECL} AND {PRIMITIVE_ROWS} AND {ALPHA_DELTA_IDENTITY} AND {NO_RECOVERY_RETURN}",
        ),
        row(
            "SignedMacrocycleExactUVAtomizationImported",
            macrocycle_imported,
            False,
            "signed macrocycle 证书把 ExactUV/source-table 侧同步到 pre-Cauchy declaration 与 fixed-key multiplicity。",
            f"{PRECAUCHY_DECL} AND {FIXED_KEY_O1}",
        ),
        row(
            "PostAntisplitSourceRankConvergenceImported",
            post_antisplit_imported,
            False,
            "post-antisplit convergence 显示 source-rank/no-collapse 路线仍汇到同 formal-unit primitive 核表。",
            "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
        ),
        row(
            "SourceAtomMultiplicityCapBridgeImported",
            source_atom_bridge_imported,
            False,
            "endpoint source-atom multiplicity cap 已桥接到 actual source table、complete key 与 fixed-key local multiplicity。",
            f"{SOURCE_TABLE_LEDGER} AND {COMPLETE_KEY_LEDGER} AND {FIXED_KEY_O1}",
        ),
        row(
            "SameUnitRankRemovedFromProductWindowFirstTarget",
            same_unit_removed,
            False,
            "same-unit rank 旧名不应再作为 product-window 第一主攻；它拆成 source-table/key/local multiplicity 接口。",
            f"{PRECAUCHY_DECL} AND {FIXED_KEY_O1}",
        ),
        row(
            "PreCauchyDeclarationStillOpen",
            source_table.get("pre_cauchy_constructor_declaration_line_proved") is False
            and macrocycle.get("pre_cauchy_constructor_declaration_line_proved") is False,
            False,
            "actual source table 的首行 declaration 仍未证明，是 source/key 侧第一实际入口。",
            PRECAUCHY_DECL,
        ),
        row(
            "FixedKeyLocalMultiplicityStillOpen",
            fixed_pair.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False
            and macrocycle.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False,
            False,
            "固定 complete key 与 fixed exact (u,v) 下 O(1) 原像仍未证明。",
            FIXED_KEY_O1,
        ),
        row(
            "OrientationExactUVInternalStillOpen",
            previous.get("orientation_parity_branch_side_proved") is False
            and previous.get("offdiagonal_exactuv_fixed_pair_return_ledger_proved") is False
            and previous.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "orientation、ExactUV return 与 internal transition 仍是 signed payload 的配套硬点。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只同步 same-unit rank 到 ExactUV/source-table 原子接口，不证明三命题无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    data = {
        "previous": load_json(PREVIOUS),
        "map_rank": load_json(STRICT_MAP_RANK),
        "fiber": load_json(EXACTUV_FIBER),
        "fixed_pair": load_json(FIXED_PAIR),
        "complete_key": load_json(COMPLETE_KEY),
        "source_table": load_json(SOURCE_TABLE),
        "macrocycle": load_json(MACROCYCLE),
        "post_antisplit": load_json(POST_ANTISPLIT),
        "source_atom_bridge": load_json(SOURCE_ATOM_BRIDGE),
    }
    rows = build_rows(data)
    same_unit_removed = rows[9]["closed"]
    latest_open_summary = (
        f"{PRECAUCHY_DECL} AND {FIXED_KEY_O1} AND {OFFDIAG_ORIENTATION} AND "
        f"{OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {RATE} AND {DSTRUCTURE}"
    )
    latest_basis = (
        f"(({NO_FURTHER_TERMINAL} AND {CLOSED_MODELGAP} AND {DSTRUCTURE} AND "
        f"{PRECAUCHY_DECL} AND {PRIMITIVE_ROWS} AND {ALPHA_DELTA_IDENTITY} "
        f"AND {NO_RECOVERY_RETURN} AND {FIXED_KEY_O1} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}) OR {SIGNED_FIELDS} OR "
        f"{POINTWISE_TABLE} OR {PRIMITIVE_ORIGIN} OR {TERMINAL_DESCENT} OR "
        f"{PDEC_SCOPE} OR {TRACE_BRIDGE} OR {SQRT_INPUT} OR {EXTERNAL_DIBFI}) AND {RATE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_same_unit_rank_exactuv_atomization_sync_router",
        "status": "product_window_same_unit_rank_synced_to_exactuv_source_table_atoms_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_absence_not_used": True,
        "product_window_same_unit_rank_active_before_sync": rows[0]["closed"],
        "exact_uv_map_rank_incidence_imported": rows[1]["closed"],
        "exactuv_fiber_atomization_imported": rows[2]["closed"],
        "fixed_pair_fiber_formal_inequality_imported": rows[3]["closed"],
        "complete_key_partition_imported": rows[4]["closed"],
        "actual_emitter_source_table_imported": rows[5]["closed"],
        "signed_macrocycle_exactuv_atomization_imported": rows[6]["closed"],
        "post_antisplit_source_rank_convergence_imported": rows[7]["closed"],
        "source_atom_multiplicity_cap_bridge_imported": rows[8]["closed"],
        "same_unit_rank_removed_from_product_window_first_target": same_unit_removed,
        "pre_cauchy_constructor_declaration_line_proved": False,
        "primitive_summand_emitter_formula_rows_proved": False,
        "alpha_delta_coefficient_identity_before_pushforward_proved": False,
        "source_table_no_downstream_recovery_and_named_return_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "orientation_parity_branch_side_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "row_column_unconditional_closed": False,
        "old_primary_attack_target": SAME_UNIT_RANK,
        "next_primary_attack_target": PRECAUCHY_DECL,
        "parallel_primary_attack_targets": [
            FIXED_KEY_O1,
            PRIMITIVE_ROWS,
            ALPHA_DELTA_IDENTITY,
            NO_RECOVERY_RETURN,
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            RATE,
            DSTRUCTURE,
        ],
        "parallel_bypass_attack_targets": [
            SIGNED_FIELDS,
            POINTWISE_TABLE,
            PRIMITIVE_ORIGIN,
            TRACE_BRIDGE,
            SQRT_INPUT,
            EXTERNAL_DIBFI,
        ],
        "latest_retained_basis_after_router": latest_basis,
        "latest_open_basis_summary": latest_open_summary,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window identity terminal downstream sync 留下的 "
            "`SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows` "
            "接入 strict exact-UV map rank/incidence、ExactUV fiber noncycle、fixed-pair "
            "fiber bound、complete key partition、actual emitter source table 与 signed macrocycle "
            "ExactUV/source-table 链。结论是：same-unit rank 旧名不应再作为 product-window "
            "第一主攻；它拆成 pre-Cauchy declaration/source table/key/local multiplicity 等 "
            "actual 接口。下一直接主攻为 `PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter`，"
            "并行保留 `FixedKeyExactUVLocalMultiplicityO1Ledger`。本证书不证明三命题无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window same-unit rank ExactUV atomization sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"exact_uv_map_rank_incidence_imported={fmt_bool(cert['exact_uv_map_rank_incidence_imported'])}",
        f"exactuv_fiber_atomization_imported={fmt_bool(cert['exactuv_fiber_atomization_imported'])}",
        f"fixed_pair_fiber_formal_inequality_imported={fmt_bool(cert['fixed_pair_fiber_formal_inequality_imported'])}",
        f"complete_key_partition_imported={fmt_bool(cert['complete_key_partition_imported'])}",
        f"actual_emitter_source_table_imported={fmt_bool(cert['actual_emitter_source_table_imported'])}",
        (
            "same_unit_rank_removed_from_product_window_first_target="
            f"{fmt_bool(cert['same_unit_rank_removed_from_product_window_first_target'])}"
        ),
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下游同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "product-window 总保留基：",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "仍开放的实际负载摘要：",
            "",
            "```text",
            cert["latest_open_basis_summary"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"] + cert["parallel_bypass_attack_targets"]),
            "```",
            "",
            "严格含义：本证书只同步 same-unit rank 到 ExactUV/source-table 原子接口，不证明行/列命题。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(
        "same_unit_rank_removed_from_product_window_first_target="
        f"{fmt_bool(cert['same_unit_rank_removed_from_product_window_first_target'])}"
    )
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
